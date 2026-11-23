"""Boundary cases that the first suite left unpinned (found by mutation testing): exact thresholds in the signatory matcher,
career tracker, instrument linker, civil-list record parser, fingerprint probe, archive_free and the CMS extractors."""
import csv
import io
import json
import os
import sys
import time
import types
import urllib.error
import urllib.request

import pandas as pd
import pytest

from conftest import run_script
from helpers import read, write_csv


# ------------------------------------------------------------------ signatory_matrix
@pytest.fixture
def S(load):
    m = load("signatory_matrix")
    m._WORDS = set()
    return m


SIG_COLS = ["doc_id", "sig_rank", "signatory", "sig_designation", "subject", "file_number", "scanned", "sig_email", "sig_phone"]
CAND_COLS = ["doc_id", "ministry", "title", "group", "category", "date", "url", "host"]
OFF_COLS = ["ministry", "website", "division", "name", "designation", "room", "phones", "email", "source_url"]


def mini_env(repo, sigs, officials, ministry="Ministry of Finance"):
    write_csv(repo / "data/signatories/candidates.csv", [
        dict(doc_id=f"d{i}", ministry=ministry, title="Order", group="g", category="c", date="2024-01-01", url=f"https://x/{i}.pdf", host="x")
        for i in range(len(sigs))], CAND_COLS)
    write_csv(repo / "data/signatories/signatures.csv", [
        dict(doc_id=f"d{i}", sig_rank=1, signatory=n, sig_designation=d, subject="", file_number="", scanned=0)
        for i, (n, d) in enumerate(sigs)], SIG_COLS)
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry=ministry, website="w", division="", name=n, designation=d, room="", phones="", email="", source_url="u") for n, d in officials], OFF_COLS)
    (repo / "data/officials.csv").write_text("org_name,name,designation,division,phones,email,igod_org_id\n")


def matched(S, repo):
    S.match()
    return read(repo / "data/signatories/notification_signatories.csv").set_index("signatory")


def test_name_sim_is_not_symmetric_for_equal_length_names(S):
    # equal token counts: the first argument is the 'short' side, so greedy assignment order differs
    assert S.name_sim("K Kumar", "Kumar Kishore") == 0.4
    assert S.name_sim("Kumar Kishore", "K Kumar") == 0.9


def test_name_sim_empty_inputs_score_zero(S):
    assert S.name_sim("", "Amit Kumar") == 0.0 and S.name_sim("Amit Kumar", "") == 0.0 and S.name_sim("", "") == 0.0


def test_match_rank_gap_of_exactly_two_is_rejected(S, repo):
    # Joint Secretary (4) signing vs Deputy Secretary (2) in the roster: gap 2 -> a different person
    mini_env(repo, [("Pia Rani Sen", "Joint Secretary")], [("Pia Rani Sen", "Deputy Secretary")])
    assert matched(S, repo).loc["Pia Rani Sen", "match_status"] == "unmatched"
    # one rank apart (Joint Secretary vs Director) is still the same person
    mini_env(repo, [("Pia Rani Sen", "Joint Secretary")], [("Pia Rani Sen", "Director")])
    r = matched(S, repo).loc["Pia Rani Sen"]
    assert r.match_status == "matched" and r.confidence == "high"


def test_match_name_score_of_exactly_point_eight_is_medium(S, repo):
    assert S.name_sim("Amit Kumar Singh Rao", "Amit Kumar Singh Rao Verma") == 0.8
    mini_env(repo, [("Amit Kumar Singh Rao", "Director")], [("Amit Kumar Singh Rao Verma", "Director")])
    r = matched(S, repo).loc["Amit Kumar Singh Rao"]
    assert (r.match_status, r.confidence, r.same_ministry) == ("matched", "medium", 1)


def test_matrix_header_lists_only_topics_signed_by_the_top_40_officers(S, repo):
    # 40 officers sign two HR documents each; a 41st signs a single legal-metrology document and falls outside head(40)
    rows = []
    cols = ["doc_id", "ministry", "sig_rank", "signatory", "sig_designation", "subject", "title", "group", "category", "date", "url", "match_status",
            "officer_id", "officer_name", "officer_designation", "officer_ministry", "officer_division", "officer_email", "officer_phones",
            "roster", "confidence", "name_score", "same_ministry", "desig_match", "officer_match"]
    for i in range(41):
        for k in range(2 if i < 40 else 1):
            title = "Transfer and posting order" if i < 40 else "Legal metrology packaged commodities rules"
            rows.append(dict(doc_id=f"d{i}_{k}", ministry="Ministry of Finance", sig_rank=1, signatory=f"O{i}", sig_designation="Director", subject="", title=title, group="g",
                             category="c", date="2024-01-01", url=f"u{i}_{k}", match_status="matched", officer_id=f"id{i:02d}",
                             officer_name=f"Officer {i:02d}", officer_designation="Director", officer_ministry="Ministry of Finance",
                             officer_division="", officer_email=f"o{i}@x.in", officer_phones="", roster="ministry_whoswho", confidence="high",
                             name_score=1.0, same_ministry=1, desig_match=1, officer_match=1))
    write_csv(repo / "data/signatories/notification_signatories.csv", rows, cols)
    write_csv(repo / "data/signatories/candidates.csv", [
        dict(doc_id=r["doc_id"], ministry="Ministry of Finance", title=r["title"], group="g", category="c", date="2024-01-01", url=r["url"], host="x")
        for r in rows], CAND_COLS)
    write_csv(repo / "data/signatories/signatures.csv", [
        dict(doc_id=r["doc_id"], sig_rank=1, signatory=r["signatory"], sig_designation="Director", subject="", file_number="", scanned=0) for r in rows], SIG_COLS)
    S.matrix()
    md = (repo / "data/signatories/SIGNATORY_MATRIX.md").read_text()
    header = next(l for l in md.splitlines() if l.startswith("| Officer | Designation (roster) | Ministry |"))
    assert "HR: appointment / transfer / posting / promotion" in header
    assert "Legal metrology" not in header
    pivot = read(repo / "data/signatories/officer_topic_pivot.csv")
    assert "Legal metrology / consumer protection rules" in pivot.columns                   # still in the full pivot


# ------------------------------------------------------------------ career_tracker
def test_attach_to_ambiguous_when_two_strong_events_score_exactly_point_95(load, repo):
    C = load("career_tracker")
    C.S._WORDS = set()
    assert C.S.name_sim("Bhaskar Rajendran", "Bhaskar Rajendram") == 0.95
    write_csv(repo / "data/signatories/signatory_directory.csv",
              [dict(ministry="Ministry of Power", signatory="Bhaskar Rajendran", designations="Director", n_documents=3, last_date="2023-05-01")],
              ["ministry", "signatory", "designations", "n_documents", "last_date"])
    cols = ["name", "service", "cadre", "batch", "event", "new_post", "new_org", "event_date", "source", "url", "snippet", "method"]
    base = {c: "" for c in cols}
    ev = pd.DataFrame([{**base, "name": "Bhaskar Rajendram", "cadre": "UP", "batch": "2005", "new_post": "Director", "new_org": "X",
                        "event_date": "2024-06-01", "source": "sm", "url": "http://a"},
                       {**base, "name": "Bhaskar Rajendram", "cadre": "BR", "batch": "2007", "new_post": "Director", "new_org": "Y",
                        "event_date": "2024-07-01", "source": "sm", "url": "http://b"}])
    d = C.attach_to(repo / "data/signatories/signatory_directory.csv", ev)
    assert d.iloc[0].posting_match_confidence == "ambiguous" and d.iloc[0].moved_since_signing == "ambiguous name"


# ------------------------------------------------------------------ policy_contact_linker
def test_instruments_from_titles_key_length_boundary(load):
    K = load("policy_contact_linker")
    K.S._WORDS = set()
    assert K.instr_key("Abcde Scheme") == "abcde" and K.instr_key("Abcd Scheme") == "abcd"
    five = pd.DataFrame([dict(doc_id=str(i), title="see the Abcde Scheme now", subject="") for i in range(2)])
    four = pd.DataFrame([dict(doc_id=str(i), title="see the Abcd Scheme now", subject="") for i in range(2)])
    assert [r["key"] for r in K.instruments_from_titles(five)] == ["abcde"]
    assert K.instruments_from_titles(four) == []


# ------------------------------------------------------------------ ips_civil_list
def test_flush_record_column3_only_first_source_code_and_first_officer_code_are_taken(load):
    IP = load("ips_civil_list")

    def rows(*lines):
        return [[{"text": t, "x0": i * 10, "top": 0} for i, t in enumerate(l.split())] for l in lines]
    rec = {1: rows("AMIT KUMAR"), 2: rows("1234567", "RR", "SPS", "7654321", "Uttar Pradesh")}
    r = IP.flush_record(rec, "Uttar Pradesh", "2005", 1)
    # an officer code before the source code must not be taken as the source; a second code is not a new source
    assert r["source_of_recruitment"] == "RR" and r["officer_code"] == "1234567"
    assert r["domicile_state"] == "SPS 7654321 Uttar Pradesh"


# ------------------------------------------------------------------ fingerprint
def test_fingerprint_get_reads_at_most_4000_bytes_of_an_error_body(load, monkeypatch):
    FP = load("mdtools_fingerprint")
    monkeypatch.setattr(FP.time, "sleep", lambda s: None)

    class Op:
        def open(self, req, timeout=None):
            raise urllib.error.HTTPError("http://x", 404, "nf", {"Content-Type": "text/html"}, io.BytesIO(b"a" * 5000))
    code, ctype, body, url, hdrs = FP.get(Op(), "http://x/p", [0.0])
    assert (code, ctype, url) == (404, "text/html", "http://x/p") and len(body) == 4000


# ------------------------------------------------------------------ archive_free
def test_archive_free_age_boundary_is_ten_minutes(repo, capsys, monkeypatch):
    now = 2_000_000_000.0
    monkeypatch.setattr(time, "time", lambda: now)
    pdf = repo / "data/states/UP/pdf"
    pdf.mkdir(parents=True)
    (repo / "data/states/UP/text").mkdir()
    rows = []
    for name, age in (("exact", 600), ("young", 599), ("old", 601)):
        p = pdf / f"{name}.pdf"
        p.write_bytes(b"x" * 10)
        os.utime(p, (now - age, now - age))
        (repo / f"data/states/UP/text/{name}.json").write_text("{}")
        rows.append(dict(file=f"data/states/UP/pdf/{name}.pdf", size="10"))
    write_csv(repo / "data/archive_manifest.csv", rows)
    run_script("archive_free", ["--apply"])
    out = capsys.readouterr().out
    assert "freed: 2 PDFs" in out and "1 changed/recent" in out
    assert (pdf / "young.pdf").exists() and not (pdf / "exact.pdf").exists() and not (pdf / "old.pdf").exists()
