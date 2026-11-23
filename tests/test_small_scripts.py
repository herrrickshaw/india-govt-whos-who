"""Command-line data-wrangling scripts that run at import time: executed end to end on synthetic files."""
import gzip
import json
import os
import sys
import time

import pandas as pd
import pytest

from conftest import run_script
from helpers import read, write_csv, write_gz_csv


# ================================================================== archive_free
def _old(path, age=3600):
    t = time.time() - age
    os.utime(path, (t, t))


def test_archive_free_dry_run_and_apply(repo, capsys):
    pdf = repo / "data/states/UP/pdf"
    pdf.mkdir(parents=True)
    text = repo / "data/states/UP/text"
    text.mkdir()
    files = {"ok": b"x" * 100, "changed": b"y" * 50, "recent": b"z" * 10, "noext": b"w" * 10}
    for n, b in files.items():
        (pdf / f"{n}.pdf").write_bytes(b)
    (text / "ok.json").write_text("{}")
    (text / "changed.json").write_text("{}")
    (text / "recent.json").write_text("{}")
    for n in ("ok", "changed", "noext"):
        _old(pdf / f"{n}.pdf")
    write_csv(repo / "data/archive_manifest.csv", [
        dict(file="data/states/UP/pdf/ok.pdf", size="100"), dict(file="data/states/UP/pdf/changed.pdf", size="999"),
        dict(file="data/states/UP/pdf/recent.pdf", size="10"), dict(file="data/states/UP/pdf/noext.pdf", size="10"),
        dict(file="data/states/UP/pdf/missing.pdf", size="1"), dict(file="data/states/UP/text/ok.json", size="2"),
        dict(file="data/other/x.pdf", size="1")])
    run_script("archive_free")
    out = capsys.readouterr().out
    assert "would free: 1 PDFs, 0.00 GB; kept 1 not yet extracted, 2 changed/recent" in out
    assert (pdf / "ok.pdf").exists()
    run_script("archive_free", ["--apply"])
    assert "freed: 1 PDFs" in capsys.readouterr().out
    assert not (pdf / "ok.pdf").exists() and (pdf / "changed.pdf").exists() and (pdf / "noext.pdf").exists() and (text / "ok.json").exists()


def test_archive_free_without_manifest(repo, capsys):
    with pytest.raises(SystemExit) as e:
        run_script("archive_free")
    assert e.value.code == 0 and "no manifest yet" in capsys.readouterr().out


# ================================================================== build_db
def test_build_db_loads_present_csvs_only(repo, capsys):
    import duckdb
    write_csv(repo / "data/organizations_index.csv", [dict(id="1", name="Org, Inc")])
    write_csv(repo / "data/signatories/officer_documents.csv", [dict(a="1", b="x"), dict(a="2", b="y")])
    run_script("build_db", [])
    out = capsys.readouterr()
    assert "organizations_index: 1 rows" in out.out and "officer_documents: 2 rows" in out.out
    assert "skip officials:" in out.err and "skip career_events:" in out.err
    con = duckdb.connect(str(repo / "data/yellowpages.duckdb"))
    assert con.execute("select typeof(a) from officer_documents limit 1").fetchone()[0] == "VARCHAR"      # all_varchar keeps ids as text
    assert {r[0] for r in con.execute("show tables").fetchall()} == {"organizations_index", "officer_documents"}
    con.close()


# ================================================================== merge_agent_results
OFF_COLS = ["ministry", "website", "division", "name", "designation", "room", "phones", "email", "source_url"]


def test_merge_agent_results(repo, capsys):
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry="Big", name="Old One", designation="Dir", email="o1@x.in"), dict(ministry="Big", name="Old Two", designation="Dir"),
        dict(ministry="Big", name="Old Three", designation="Dir"), dict(ministry="Big", name="Old Four", designation="Dir"),
        dict(ministry="Big", name="Old Five", designation="Dir"), dict(ministry="Big", name="Old Six", designation="Dir"),
        dict(ministry="Keep", name="Kept Person", designation="S")], OFF_COLS)
    ga = repo / "data/agents/groupA"
    write_csv(ga / "officials.csv", [
        dict(ministry="Big", name="New A", designation="Dir", email="a[at]gov[dot]in"),
        dict(ministry="Big", name="Old One", designation="Dir"),                              # already in the roster (a smaller agent result)
        dict(ministry="Small", name="  Shri   S  Kumar ", designation="JS", email="sk(at)gov(dot)in"),
        dict(ministry="Small", name="Helpline Number", designation=""), dict(ministry="Small", name="011-23010101", designation=""),
        dict(ministry="Small", name="Ab", designation=""), dict(ministry="Small", name="Control Room", designation="")] + [
        dict(ministry="NewMin", name=f"Person Number{i}", designation=f"D{i}") for i in range(5)], OFF_COLS)
    write_csv(ga / "sources.csv", [dict(url="http://a", note="1"), dict(url="http://a", note="dup")], ["url", "note"])
    gb = repo / "data/agents/groupB"
    write_csv(gb / "sources.csv", [dict(url="http://b", note="2")], ["url", "note"])
    (repo / "data/agents/groupC").mkdir()
    (repo / "data/agents/groupC/officials.csv").write_text("not,a\n\"unterminated")
    run_script("merge_agent_results")
    out = capsys.readouterr().out
    assert "sources: 3 rows -> data/agents/sources_all.csv" in out and "dropped 3 non-person rows" in out
    src = read(repo / "data/agents/sources_all.csv")
    assert set(src.url) == {"http://a", "http://b"}
    m = read(repo / "data/ministry_officials.csv", dtype=str).fillna("")
    big = m[m.ministry == "Big"]
    assert len(big) == 7 and "New A" in set(big.name) and big[big.name == "New A"].email.iloc[0] == "a@gov.in"   # agent found fewer rows: only unseen officers appended
    assert set(m[m.ministry == "NewMin"].name) == {f"Person Number{i}" for i in range(5)}
    assert "Kept Person" in set(m.name)
    small = m[m.ministry == "Small"]
    assert list(small.name) == ["Shri S Kumar"] and small.email.iloc[0] == "sk@gov.in"
    assert "Old One" in set(big.name) and list(big.name).count("Old One") == 1


def test_merge_agent_results_replaces_roster_when_agent_is_larger(repo, capsys):
    write_csv(repo / "data/ministry_officials.csv", [dict(ministry="M", name="Only Old", designation="D")], OFF_COLS)
    write_csv(repo / "data/agents/groupA/officials.csv", [dict(ministry="M", name=f"Agent Person{i}", designation=f"D{i}") for i in range(5)], OFF_COLS)
    run_script("merge_agent_results")
    m = read(repo / "data/ministry_officials.csv", dtype=str)
    assert set(m.name) == {f"Agent Person{i}" for i in range(5)}                          # >= max(5, existing) -> replaced
    assert "ministry_officials.csv: 1 -> 1 ministries, 1 -> 5 rows" in capsys.readouterr().out


def test_merge_agent_results_without_agent_files(repo, capsys):
    (repo / "data/agents").mkdir()
    with pytest.raises(SystemExit) as e:
        run_script("merge_agent_results")
    assert e.value.code == 0 and "no officials.csv yet" in capsys.readouterr().out


# ================================================================== refresh_ministry_rosters
@pytest.mark.xfail(strict=True, reason="refresh_ministry_rosters concatenates the WHOLE new scrape onto the old rows of replaced ministries, so a "
                                       "ministry whose new scrape is too small to replace its roster (1 row vs 20) still gets that row appended")
def test_refresh_keeps_small_new_scrape_out_of_unreplaced_roster(load, repo):
    W = load("ministry_whoswho")
    write_csv(repo / "data/ministry_officials.csv", [dict(ministry="Big", name=f"Old{i} Person", designation="D") for i in range(20)], OFF_COLS)
    W.main = lambda: write_csv(W.OUT, [dict(ministry="Big", name="One Row", designation="D")], OFF_COLS)
    run_script("refresh_ministry_rosters")
    assert (read(repo / "data/ministry_officials.csv").ministry == "Big").sum() == 20


def test_refresh_ministry_rosters_merges_only_better_rosters(load, repo, capsys):
    W = load("ministry_whoswho")
    write_csv(repo / "data/ministry_officials.csv", [dict(ministry="Big", name=f"Old{i} Person", designation="D") for i in range(20)] +
              [dict(ministry="Mid", name="Old Mid", designation="D")], OFF_COLS)

    def fake_main():
        write_csv(W.OUT, [dict(ministry="Big", name="One Row", designation="D")] +                             # 1 row cannot replace 20
                  [dict(ministry="Mid", name=f"New Mid{i}", designation="D") for i in range(6)] +
                  [dict(ministry="Fresh", name="Brand New", designation="D")] + [dict(ministry="Blank", name="  ", designation="D")], OFF_COLS)
    W.main = fake_main
    run_script("refresh_ministry_rosters")
    m = read(repo / "data/ministry_officials.csv", dtype=str)
    assert set(m[m.ministry == "Mid"].name) == {f"New Mid{i}" for i in range(6)}      # 6 >= max(5, 1 // 2) -> replaced
    assert "Brand New" in set(m.name) and "Blank" not in set(m.ministry)
    assert "merged: old 2 ministries / 21 rows; new scrape 2 ministries / 8 rows; result 3 ministries / 28 rows" in capsys.readouterr().err
    assert "/en/whos-who/" in W.PROBE_PATHS and "officers?" in W.WHO_RE.pattern


# ================================================================== verify_coverage
def _run_vc(args):
    return run_script("verify_coverage", args)


def test_verify_coverage_portal_signed_and_ub(repo, capsys):
    st = repo / "data/states"
    write_csv(st / "UP/candidates.csv", [dict(doc_id="a", host="goir.up.gov.in"), dict(doc_id="b", host="goir.up.gov.in"), dict(doc_id="c", host="other")])
    write_csv(st / "UP/signatures.csv", [dict(doc_id="a"), dict(doc_id="c")])
    _run_vc(["portal", "UP", "goir.up", "2"])
    assert "VERIFIED UP-orders: 2 goir.up orders recorded (need >= 2)" in capsys.readouterr().out
    with pytest.raises(SystemExit) as e:
        _run_vc(["portal", "UP", "goir.up", "3"])
    assert e.value.code == 1 and "FAILED UP-orders" in capsys.readouterr().out
    _run_vc(["signed", "UP", "goir.up", "1"])
    assert "1 of 2 goir.up orders have a signature read" in capsys.readouterr().out
    write_csv(st / "targets.csv", [dict(state="UB", slug="s1"), dict(state="UB", slug="s2"), dict(state="UP", slug="s3")])
    _run_vc(["ub_targets", "2"])
    assert "2 union-body sites targeted" in capsys.readouterr().out
    (repo / "ministry_documents/data/sites/s1").mkdir(parents=True)
    (repo / "ministry_documents/data/sites/s1/doc_links.csv").write_text("url\n")
    _run_vc(["ub_crawled", "1"])
    assert "1 of 2 union-body sites produced document links" in capsys.readouterr().out
    write_csv(st / "UB/candidates.csv", [dict(doc_id="a", host="h")])
    _run_vc(["ub_candidates", "1"])
    write_csv(st / "UB/signatures.csv", [dict(doc_id="a")])
    write_csv(st / "UB/signatory_directory.csv", [dict(n="x"), dict(n="y")])
    _run_vc(["ub_signed", "1", "2"])
    assert "1 signatures, 2 distinct signers" in capsys.readouterr().out.splitlines()[-1]
    with pytest.raises(SystemExit):
        _run_vc(["ub_signed", "1", "3"])


def test_verify_coverage_linked_disk_docs_and_unknown(repo, capsys, monkeypatch):
    write_csv(repo / "data/policy_contacts_from_documents.csv", [dict(level="centre"), dict(level="UP")])
    _run_vc(["linked", "centre", "UP"])
    assert "missing []" in capsys.readouterr().out
    with pytest.raises(SystemExit):
        _run_vc(["linked", "centre", "KL"])
    assert "missing ['KL']" in capsys.readouterr().out
    _run_vc(["disk", "0.0001"])
    with pytest.raises(SystemExit):
        _run_vc(["disk", "999999999"])
    capsys.readouterr()
    write_csv(repo / "data/states/UB/signatory_directory.csv", [dict(n="x")] * 3)
    write_csv(repo / "data/states/TS/candidates.csv", [dict(doc_id="1", host="goir.telangana.gov.in")] * 2)
    write_csv(repo / "data/states/AP/candidates.csv", [dict(doc_id="1", host="goir.ap.gov.in")])
    (repo / "README.md").write_text("We read 3 signers, 2 TS orders and 1 AP order")
    (repo / "data/RESULTS_SUMMARY.md").write_text("")
    (repo / "docs").mkdir()
    (repo / "docs/DATA_DICTIONARY.md").write_text("")
    _run_vc(["docs"])
    assert "documents quote measured" in capsys.readouterr().out
    (repo / "README.md").write_text("nothing")
    with pytest.raises(SystemExit):
        _run_vc(["docs"])
    with pytest.raises(SystemExit) as e:
        _run_vc(["bogus"])
    assert e.value.code == 2 and "unknown" in capsys.readouterr().out


def test_verify_coverage_pushed_uses_git(repo, capsys, monkeypatch):
    import subprocess
    calls = []

    def fake_run(cmd, capture_output=False, text=False):
        calls.append(cmd)
        out = ""
        if "status" in cmd:
            out = " M GATES.md\n?? .unlazy/x\n"
        elif "rev-parse" in cmd:
            out = "abc1234"
        return subprocess.CompletedProcess(cmd, 0, stdout=out, stderr="")
    monkeypatch.setattr(subprocess, "run", fake_run)
    _run_vc(["pushed"])
    assert "dirty=0, HEAD==origin/main True" in capsys.readouterr().out and any("fetch" in c for c in calls)


# ================================================================== build_results_summary
def test_build_results_summary(repo, capsys):
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz", [
        dict(ministry="Ministry A", title="Office Order", group="g", category="c"),
        dict(ministry="Ministry A", title="Photo gallery", group="", category=""),
        dict(ministry="Ministry B", title="Scheme guidelines", group="", category="")])
    write_csv(repo / "data/signatories/candidates.csv", [dict(doc_id="d1", ministry="Ministry A"), dict(doc_id="d2", ministry="Ministry A")])
    write_csv(repo / "data/signatories/signatures.csv", [dict(doc_id="d1", sig_rank=1), dict(doc_id="d2", sig_rank=0)])
    write_csv(repo / "data/signatories/signatory_directory.csv", [dict(ministry="Ministry A", email="a@x.in"), dict(ministry="Ministry A", email=None)])
    write_csv(repo / "data/ministry_officials.csv", [dict(ministry="Ministry A", name="N")])
    write_csv(repo / "data/signatories/notification_signatories.csv", [dict(ministry="Ministry A", match_status="matched", doc_id="d1", officer_id="o1"),
                                                                       dict(ministry="Ministry A", match_status="unmatched", doc_id="d2", officer_id="")])
    write_csv(repo / "data/policy_instruments_index.csv", [dict(ministry="Ministry A", n_contacts=2), dict(ministry="Ministry A", n_contacts=0)])
    write_csv(repo / "data/states/targets.csv", [dict(state="UP", slug="s1"), dict(state="UP", slug="s2"), dict(state="TN", slug="s3")])
    write_csv(repo / "data/states/state_officials.csv", [dict(state="UP", name="Amit", department="Edu", email="a@x.in"), dict(state="UP", name="", department="Edu", email=""),
                                                         dict(state="UP", name="Bina", department="Health", email="")])
    (repo / "ministry_documents/data/sites/s1").mkdir(parents=True)
    (repo / "ministry_documents/data/sites/s1/doc_links.csv").write_text("url\n")
    write_csv(repo / "data/states/UP/candidates.csv", [dict(doc_id="x")] * 3)
    write_csv(repo / "data/states/UP/signatures.csv", [dict(doc_id="x1", sig_rank=1, sig_script="DEVANAGARI"), dict(doc_id="x2", sig_rank=0, sig_script="LATIN")])
    write_csv(repo / "data/states/UP/notification_signatories.csv", [dict(signatory="S1", match_status="matched", doc_id="x1", officer_id="o9")])
    (repo / "data/states/UP/text").mkdir()
    (repo / "data/states/UP/text/a.json").write_text("{}")
    run_script("build_results_summary")
    m = read(repo / "data/results_by_ministry.csv").set_index("ministry")
    a = m.loc["Ministry A"]
    assert (a.docs_indexed, a.order_docs, a.pdfs_read, a.with_signature, a.signers, a.signers_email, a.roster_officers, a.matched_docs, a.officers_linked, a.instruments, a.instr_with_contact) == \
        (2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1)
    assert m.loc["Ministry B"].order_docs == 1 and m.loc["Ministry B"].pdfs_read == 0
    s = read(repo / "data/results_by_state.csv").set_index("state")
    up = s.loc["UP"]
    assert (up.departments, up.whoswho_depts, up.officers, up.officers_email, up.sites_crawled, up.candidate_pdfs, up.docs_read, up.docs_with_signature,
            up.indic_script_signatures, up.signers, up.matched_docs, up.officers_linked) == (2, 2, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1)
    tn = s.loc["TN"]
    assert (tn.officers, tn.candidate_pdfs, tn.signers) == (0, 0, 0)
    md = (repo / "data/RESULTS_SUMMARY.md").read_text()
    assert "# Results summary — ministries and states" in md and "| Ministry A | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 |" in md and "Ministry B" not in md.split("## States")[0].split("|---")[1]
    assert "ministries 1; states 2" in capsys.readouterr().out


# ================================================================== new_pdfs_to_md
def test_new_pdfs_to_md_converts_missing_documents(load, repo, monkeypatch, capsys, tmp_path):
    import concurrent.futures as cf
    import zipfile
    M = load("shards_to_md")
    (repo / "data/states/UB/pdf").mkdir(parents=True)
    for n in ("a", "b", "c"):
        (repo / f"data/states/UB/pdf/{n}.pdf").write_bytes(b"%PDF " + n.encode())
    write_csv(repo / "data/states/UB/candidates.csv", [dict(doc_id="a", url="http://a", ministry="M", title="T", date="2025")])
    M.append_index([dict(doc_id="b")])                                          # 'b' already has markdown
    monkeypatch.setattr(M, "SCRATCH", tmp_path / "scratch")
    (tmp_path / "scratch").mkdir()
    seen = []

    class FakePool:
        def __init__(self, **kw):
            pass

        def map(self, fn, jobs, chunksize=1):
            seen.extend(jobs)
            return [(Path_stem(j[1]), None if j[1] == "c.pdf" else f"# md {j[1]}", dict(doc_id=Path_stem(j[1]), needs_ocr=0, error="oops" if j[1] == "c.pdf" else "", method="pdftotext", pages=1))
                    for j in jobs]
    def Path_stem(n):
        return n[:-4]
    monkeypatch.setattr(cf, "ProcessPoolExecutor", FakePool)
    monkeypatch.setattr(os, "nice", lambda n: 0)
    run_script("new_pdfs_to_md", ["--states", "UB", "--workers", "1", "--ocr-pages", "3"])
    assert [j[1] for j in seen] == ["a.pdf", "c.pdf"]
    meta = {j[1]: j[2] for j in seen}
    assert meta["a.pdf"]["source_url"] == "http://a" and meta["a.pdf"]["ocr_lang"] == "eng" and meta["a.pdf"]["ocr_pages"] == 3
    assert meta["c.pdf"]["source_url"] == ""                                       # no candidate row -> blank provenance
    out = repo / "corpus/md/data__states__UB__pdf/data__states__UB__pdf-new-001.md.zip"
    with zipfile.ZipFile(out) as z:
        assert sorted(z.namelist()) == ["a.md", "index.jsonl"]                     # no markdown member for the failed document
        idx = [json.loads(l) for l in z.read("index.jsonl").decode().splitlines()]
    assert [r["doc_id"] for r in idx] == ["a", "c"]
    index = read(repo / "data/md_index.csv.gz", dtype=str).fillna("")
    assert set(index.doc_id) == {"b", "a", "c"}
    assert "[UB] 2 PDFs without markdown" in capsys.readouterr().out
