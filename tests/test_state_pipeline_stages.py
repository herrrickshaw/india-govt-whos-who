"""Stages of scripts/state_pipeline.py on synthetic data; every network/OCR/subprocess call is faked."""
import argparse
import json
import types

import pandas as pd
import pytest

from helpers import read, write_csv

ORG_COLS = ["name", "branch", "state", "website", "igod_org_id", "category_code", "category"]


def ns(**kw):
    base = dict(states=[], max_sites=0, max_pages=60, max_docs=300, tranche2=False)
    base.update(kw)
    return argparse.Namespace(**base)


@pytest.fixture
def P(load):
    m = load("state_pipeline")
    m.S._WORDS = set()
    return m


@pytest.fixture
def orgs(repo):
    rows = [
        dict(name="Education Department", branch="sg", state="UP", website="https://edu.up.gov.in", igod_org_id="1", category_code="E1"),
        dict(name="UP Roads Directorate", branch="sg", state="UP", website="https://roads.up.gov.in", igod_org_id="2", category_code="E2"),
        dict(name="UP Dup", branch="sg", state="UP", website="https://edu.up.gov.in", igod_org_id="3", category_code="E1"),
        dict(name="Health Secretariat", branch="sg", state="TN", website="https://health.tn.gov.in", igod_org_id="4", category_code="E1"),
        dict(name="No site", branch="sg", state="TN", website="", igod_org_id="5", category_code="E1"),
        dict(name="Statutory Body X", branch="ug", state="DL", website="https://body.gov.in", igod_org_id="6", category_code="E9", category="Statutory Bodies"),
        dict(name="Ministry Y", branch="ug", state="DL", website="https://min.gov.in", igod_org_id="7", category_code="E2", category="Ministries"),
    ]
    write_csv(repo / "data/organizations_index.csv", rows, ORG_COLS)
    return rows


def test_targets_builds_state_and_union_body_rows(P, orgs, repo, capsys):
    P.targets(ns())
    t = read(repo / "data/states/targets.csv")
    assert list(t.columns) == ["state", "name", "website", "igod_org_id", "category_code", "slug"]
    assert set(t.website) == {"https://edu.up.gov.in", "https://roads.up.gov.in", "https://health.tn.gov.in", "https://body.gov.in"}
    assert t.set_index("website").loc["https://body.gov.in", "state"] == "UB"
    assert t.set_index("website").loc["https://edu.up.gov.in", "slug"] == "st-edu-up"
    # secretariat-style names sort before the rest
    up = t[t.state == "UP"].name.tolist()
    assert up[0] == "Education Department" and up[-1] == "UP Roads Directorate" or up[0].endswith("Department")
    assert "targets: 4 department sites" in capsys.readouterr().out


def test_targets_state_filter_max_sites_and_merge_with_previous(P, orgs, repo):
    P.targets(ns())
    P.targets(ns(states=["TN"]))                  # re-running one state keeps the other states' rows
    t = read(repo / "data/states/targets.csv")
    assert set(t.state) == {"UP", "TN", "UB"} and len(t) == 4
    write_csv(repo / "data/states/targets.csv", [dict(state="TN", name="old", website="http://old", igod_org_id="", category_code="", slug="s")])
    P.targets(ns(states=["UP"]))                  # 'UB' only added when no filter / UB selected
    t = read(repo / "data/states/targets.csv")
    assert set(t.state) == {"TN", "UP"} and "old" in set(t.name)
    P.targets(ns(max_sites=1))
    t = read(repo / "data/states/targets.csv")
    assert t[t.state == "UP"].shape[0] == 1


def test_sdir_creates_pdf_dir(P, repo):
    d = P.sdir("KL")
    assert d == repo / "data/states/KL" and (d / "pdf").is_dir()


# ------------------------------------------------------------------ crawl
def test_crawl_writes_job_file_and_invokes_xargs(P, repo, monkeypatch, capsys):
    write_csv(repo / "data/states/targets.csv", [
        dict(state="UP", name="A", website="https://a.up", igod_org_id="", category_code="", slug="st-a"),
        dict(state="UP", name="A2", website="https://a.up", igod_org_id="", category_code="", slug="st-a"),
        dict(state="UP", name="B", website="https://b.up", igod_org_id="", category_code="", slug="st-b"),
        dict(state="TN", name="C", website="https://c.tn", igod_org_id="", category_code="", slug="st-c"),
    ])
    (repo / "ministry_documents/data/sites/st-b").mkdir(parents=True)
    (repo / "ministry_documents/data/sites/st-b/doc_links.csv").write_text("url\n")      # already crawled
    seen = {}

    def fake_run(cmd, stdin=None, check=None):
        seen["cmd"], seen["stdin"], seen["check"] = cmd, stdin.read(), check
        (repo / "ministry_documents/data/sites/st-a").mkdir(parents=True)
        (repo / "ministry_documents/data/sites/st-a/doc_links.csv").write_text("url\n")
        return types.SimpleNamespace(returncode=0)
    monkeypatch.setattr(P.subprocess, "run", fake_run)
    monkeypatch.setenv("CRAWL_SITE_SECONDS", "77")
    P.crawl(ns(states=["UP"], max_pages=9))
    assert seen["cmd"][:5] == ["xargs", "-P", "8", "-L", "1"] and seen["check"] is False
    assert "alarm 77" in seen["cmd"][-1] and "--max-pages 9" in seen["cmd"][-1]
    assert seen["stdin"] == "https://a.up st-a\n"                       # dedup by slug, crawled sites skipped, other states ignored
    out = capsys.readouterr().out
    assert "crawl: 1 sites (max 9 pages each), 1 already crawled" in out or "crawl: 2 sites" in out
    assert "crawl: 1/1 sites produced document links" in out


# ------------------------------------------------------------------ select
def _write_links(repo, slug, rows):
    write_csv(repo / f"ministry_documents/data/sites/{slug}/doc_links.csv", rows, ["text", "url", "found_on"])


def test_select_candidates_latin_and_indic_titles(P, repo, capsys):
    write_csv(repo / "data/states/targets.csv", [
        dict(state="UP", name="Dept A", website="https://a.up.gov.in", igod_org_id="", category_code="", slug="st-a"),
        dict(state="UP", name="Dept B", website="https://b.up.gov.in", igod_org_id="", category_code="", slug="st-b"),
        dict(state="TN", name="Dept C", website="https://c.tn.gov.in", igod_org_id="", category_code="", slug="st-c"),
    ])
    _write_links(repo, "st-a", [
        dict(text="Government Order on transfers", url="https://a.up.gov.in/go1.pdf", found_on="p"),
        dict(text="Government Order on transfers", url="https://a.up.gov.in/go1.pdf", found_on="p"),         # duplicate
        dict(text="शासनादेश 2024", url="https://a.up.gov.in/hindi.PDF", found_on="p"),                       # Indic title word
        dict(text="Photo gallery", url="https://a.up.gov.in/pic.pdf", found_on="p"),                         # not an order
        dict(text="Circular", url="https://a.up.gov.in/page.html", found_on="p"),                            # not a pdf
        dict(text="G.O. Ms. No 5", url="https://a.up.gov.in/goms.pdf", found_on="p"),
    ])
    _write_links(repo, "st-b", [dict(text="Resolution of the board", url="https://b.up.gov.in/res.pdf", found_on="p")])
    P.select(ns(states=["UP"]))
    c = read(repo / "data/states/UP/candidates.csv")
    assert set(c.url) == {"https://a.up.gov.in/go1.pdf", "https://a.up.gov.in/hindi.PDF", "https://a.up.gov.in/goms.pdf", "https://b.up.gov.in/res.pdf"}
    assert (c.group == "UP").all() and c.doc_id.tolist() == [P.S.doc_id(u) for u in c.url]
    assert set(c.host) == {"a.up.gov.in", "b.up.gov.in"}
    assert "select UP: 4 candidate PDFs from 7 links (2 departments)" in capsys.readouterr().out
    # state with nothing crawled is reported
    P.select(ns(states=["TN"]))
    assert "select TN: nothing crawled" in capsys.readouterr().out


def test_select_defaults_to_all_states_and_tranche2_keeps_old(P, repo, capsys):
    write_csv(repo / "data/states/targets.csv", [
        dict(state="UP", name="Dept A", website="https://a.up.gov.in", igod_org_id="", category_code="", slug="st-a")])
    _write_links(repo, "st-a", [dict(text="Order one", url="https://a.up.gov.in/1.pdf", found_on="p")])
    P.select(ns())
    first = read(repo / "data/states/UP/candidates.csv")
    assert len(first) == 1
    _write_links(repo, "st-a", [dict(text="Order one", url="https://a.up.gov.in/1.pdf", found_on="p"),
                                dict(text="Order two", url="https://a.up.gov.in/2.pdf", found_on="p")])
    P.select(ns(tranche2=True))
    both = read(repo / "data/states/UP/candidates.csv")
    assert set(both.url) == {"https://a.up.gov.in/1.pdf", "https://a.up.gov.in/2.pdf"}
    assert "select UP: 1 candidate PDFs" in capsys.readouterr().out.splitlines()[-1]


def test_select_max_docs_caps_per_ministry(P, repo):
    write_csv(repo / "data/states/targets.csv", [
        dict(state="UP", name="Dept A", website="https://a.up.gov.in", igod_org_id="", category_code="", slug="st-a")])
    _write_links(repo, "st-a", [dict(text=f"Order {i}", url=f"https://a.up.gov.in/{i}.pdf", found_on="p") for i in range(30)])
    P.select(ns(max_docs=8))
    assert len(read(repo / "data/states/UP/candidates.csv")) == 8


# ------------------------------------------------------------------ fetch / bind
def test_bind_sets_signatory_matrix_globals_and_fetch_delegates(P, repo, monkeypatch, capsys):
    calls = []
    monkeypatch.setattr(P.S, "fetch", lambda: calls.append((P.S.OUT, P.S.PDF, P.S.OCR_LANG)))
    P.fetch(ns(states=["TN", "ZZ"]))
    assert calls[0] == (repo / "data/states/TN", repo / "data/states/TN/pdf", "tam+eng")
    assert calls[1][2] == "eng"                                     # unknown state -> English
    assert "[TN]" in capsys.readouterr().out


# ------------------------------------------------------------------ extract
LATIN_TAIL = "Sd/-\n(Amit Kumar)\nUnder Secretary to the Government\n"
HINDI_TAIL = "अमित कुमार\nसंयुक्त सचिव\n"


def _setup_extract(P, repo, monkeypatch, texts):
    cand_rows = [dict(doc_id=d, ministry="Dept", title="t", group="UP", category="", date="", url=f"u{d}", host="h", website="w", found_on="p") for d in texts]
    write_csv(repo / "data/states/UP/candidates.csv", cand_rows)
    (repo / "data/states/UP/pdf").mkdir(parents=True, exist_ok=True)
    for d in list(texts) + ["not_a_candidate"]:
        (repo / f"data/states/UP/pdf/{d}.pdf").write_bytes(b"%PDF")
    texts = dict(texts, not_a_candidate=(1, "", ""))

    def fake_pdf_text(path, pages_tail=2):
        fake_pdf_text.last_ocr = path.stem == "hin"
        return texts[path.stem]
    fake_pdf_text.last_ocr = False
    monkeypatch.setattr(P.S, "pdf_text", fake_pdf_text)


def test_extract_latin_indic_digital_and_unsigned(P, repo, monkeypatch, capsys):
    long_head = "Subject: Transfer of officers in the department\n\nSir,\n" + "body text " * 20
    hindi_head = "विषय: स्थानांतरण\n\n" + "अमित कुमार सिंह " * 10
    _setup_extract(P, repo, monkeypatch, {
        "lat": (2, long_head, LATIN_TAIL),
        "hin": (2, hindi_head, HINDI_TAIL + "\nअमित कुमार सिंह " * 5),
        "dig": (1, "digitally signed by Rohit Verma\nDate x " + "x" * 100, "nothing"),
        "uns": (1, "A substantive first line of the document here\n" + "y" * 100, "nothing"),
    })
    P.extract(ns(states=["UP"]))
    s = read(repo / "data/states/UP/signatures.csv").set_index("doc_id")
    assert "not_a_candidate" not in s.index
    lat = s.loc["lat"]
    assert (lat.sig_rank, lat.signatory, lat.sig_script, lat.script) == (1, "Amit Kumar", "LATIN", "LATIN")
    assert lat.subject_raw == "Transfer of officers in the department" and lat.scanned == 0
    hin = s.loc["hin"]
    assert hin.sig_rank == 1 and hin.sig_script == "DEVANAGARI" and hin.signatory_raw == "अमित कुमार" and pd.isna(hin.signatory)
    assert hin.sig_designation == "Joint Secretary" and hin.ocr == 1 and hin.script == "DEVANAGARI"
    dig = s.loc["dig"]
    assert (dig.signatory, dig.sig_designation, dig.strength) == ("Rohit Verma", "(digital signature only)", 2)
    uns = s.loc["uns"]
    assert uns.sig_rank == 0 and uns.subject_raw.startswith("A substantive first line")
    assert "[UP] extract: 5 PDFs" in capsys.readouterr().out


def test_extract_skips_already_read_documents(P, repo, monkeypatch):
    long_head = "Subject: Transfer of officers in the department\n\nSir,\n" + "body text " * 20
    _setup_extract(P, repo, monkeypatch, {"lat": (2, long_head, LATIN_TAIL)})
    P.extract(ns(states=["UP"]))
    calls = []
    monkeypatch.setattr(P.S, "pdf_text", lambda path, pages_tail=2: calls.append(path) or (1, "", ""))
    P.extract(ns(states=["UP"]))
    assert calls == [] and len(read(repo / "data/states/UP/signatures.csv")) == 1


def test_extract_keeps_at_most_three_signers(P, repo, monkeypatch):
    tail = "".join(f"(Person{c} Name{c})\nDirector\n\n" for c in "ABCDE")
    _setup_extract(P, repo, monkeypatch, {"many": (2, "Subject: x of the order\n\n" + "t " * 60, tail)})
    P.extract(ns(states=["UP"]))
    s = read(repo / "data/states/UP/signatures.csv")
    assert list(s.sig_rank) == [1, 2, 3]


# ------------------------------------------------------------------ translate
def _signatures(repo, rows):
    cols = ["doc_id", "script", "subject_raw", "sig_rank", "signatory_raw", "signatory", "sig_script", "sig_designation_raw", "sig_designation"]
    write_csv(repo / "data/states/UP/signatures.csv", rows, cols)


def test_translate_without_key_uses_rule_based_names(P, repo, monkeypatch, capsys):
    (repo / "data/states").mkdir(parents=True, exist_ok=True)
    _signatures(repo, [
        dict(doc_id="a", script="DEVANAGARI", subject_raw="विषय: आदेश " * 3, sig_rank=1, signatory_raw="अमित", signatory="", sig_script="DEVANAGARI"),
        dict(doc_id="b", script="LATIN", subject_raw="Subject in English", sig_rank=1, signatory_raw="Rohit Verma", signatory="Rohit Verma", sig_script="LATIN"),
    ])
    monkeypatch.setattr(P, "_groq_key", lambda: None)
    monkeypatch.setattr(P, "romanise_rule", lambda name, scr: f"rule:{name}")
    P.translate(ns(states=["UP", "TN"]))                  # TN has no signatures file -> skipped
    df = read(repo / "data/states/UP/signatures.csv").set_index("doc_id")
    assert df.loc["a", "signatory"] == "rule:अमित" and df.loc["a", "signatory_rule"] == "rule:अमित"
    assert df.loc["b", "signatory"] == "Rohit Verma" and pd.isna(df.loc["b", "signatory_rule"])
    assert df.loc["a", "subject_language"] == "Hindi" and df.loc["b", "subject_language"] == "en"
    assert df.loc["a", "subject"].startswith("विषय") and df.loc["b", "subject"] == "Subject in English"
    assert "no GROQ_API_KEY" in capsys.readouterr().out


def test_translate_with_key_prefers_llm_names_and_translates_subjects(P, repo, monkeypatch):
    (repo / "data/states").mkdir(parents=True, exist_ok=True)
    subj = "विषय: आदेश " * 3
    _signatures(repo, [dict(doc_id="a", script="DEVANAGARI", subject_raw=subj, sig_rank=1, signatory_raw="अमित", signatory="", sig_script="DEVANAGARI")])
    monkeypatch.setattr(P, "_groq_key", lambda: "k")
    monkeypatch.setattr(P, "translate_batch", lambda cache, names, texts, lang: (cache["names"].update({"अमित": "Amit"}), cache["text"].update({subj: "Subject: Order"}), cache)[2])
    monkeypatch.setattr(P, "romanise_rule", lambda name, scr: "rule")
    P.translate(ns(states=["UP"]))
    df = read(repo / "data/states/UP/signatures.csv").iloc[0]
    assert df.signatory == "Amit" and df.signatory_rule == "rule" and df.subject == "Subject: Order"


# ------------------------------------------------------------------ rosters / directory / match / matrix
@pytest.fixture
def rosters(repo):
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry="Ministry of Finance", website="w", division="Div", name="Amit Kumar", designation="Joint Secretary", room="", phones="1", email="a@gov.in", source_url="u"),
        dict(ministry="Ministry of Finance", website="w", division="", name="", designation="", room="", phones="", email="", source_url="u"),
    ])
    write_csv(repo / "data/states/state_officials.csv", [
        dict(state="UP", department="Edu", website="w", name="Rohit Verma", designation="Secretary", division="", room="", phones="", email="rv@up.gov.in", source_url="u"),
        dict(state="UP", department="Edu", website="w", name="", designation="", division="", room="", phones="", email="", source_url="(none: x)"),
        dict(state="TN", department="Health", website="w", name="Other State", designation="", division="", room="", phones="", email="", source_url="u"),
        dict(state="UP", department="Edu", website="w", name="vacant", designation="", division="", room="", phones="", email="", source_url="u"),
    ])
    write_csv(repo / "data/ias_officers.csv", [
        dict(name_en="Sita Devi", cadre_code="UP", current_posting="Collector, Lucknow", er_sheet_url="http://er1"),
        dict(name_en="Karan Kumar", cadre_code="KN", current_posting="Secretary, Bengaluru", er_sheet_url="http://er2"),
        dict(name_en="Tara Das", cadre_code="UP CADRE", current_posting="DM, Agra", er_sheet_url="http://er3"),
        dict(name_en="Uma Rao", cadre_code="TN", current_posting="X", er_sheet_url="http://er4"),
    ])
    write_csv(repo / "data/ips_officers.csv", [dict(name_en="Vikram Singh", other="x", current_posting="SP, Kanpur")])


def test_state_rosters_union_and_cadre_filter(P, repo, rosters):
    r = P.state_rosters("UP")
    assert set(r.roster) == {"state_whoswho", "ias_civil_list"}              # ips file has no cadre column -> skipped
    assert set(r.name) == {"Rohit Verma", "Sita Devi", "Tara Das"}           # blank / 'vacant' dropped, other states and cadres filtered
    assert r.officer_id.is_unique
    sv = r[r.name == "Rohit Verma"].iloc[0]
    assert (sv.ministry, sv.email) == ("Edu", "rv@up.gov.in")
    kn = P.state_rosters("KA")                                               # igod code KA -> DoPT cadre KN
    assert set(kn.name) == {"Karan Kumar"}
    assert P.state_rosters("ZZ").empty


def test_state_rosters_union_bodies_use_ministry_roster_and_all_cadres(P, repo, rosters):
    r = P.state_rosters("UB")
    assert set(r.roster) == {"ministry_whoswho", "ias_civil_list"}
    assert {"Amit Kumar", "Sita Devi", "Karan Kumar", "Uma Rao"} <= set(r.name)
    assert "Rohit Verma" not in set(r.name)                                   # state who's-who never feeds union bodies


def test_directory_aggregates_all_states(P, repo, monkeypatch):
    for st in ("UP", "TN"):
        write_csv(repo / f"data/states/{st}/signatures.csv", [dict(doc_id="d", sig_rank=1, signatory="X")])
    monkeypatch.setattr(P.S, "directory", lambda: write_csv(P.S.OUT / "signatory_directory.csv", [dict(ministry="M", signatory=f"S-{P.S.OUT.name}")]))
    P.directory(ns(states=["UP", "TN", "KL"]))                                # KL has no signatures -> skipped
    d = read(repo / "data/states/signatory_directory_all_states.csv")
    assert list(d.state) == ["UP", "TN"] and list(d.signatory) == ["S-UP", "S-TN"]
    # nothing to aggregate -> no file written
    (repo / "data/states/signatory_directory_all_states.csv").unlink()
    P.directory(ns(states=["KL"]))
    assert not (repo / "data/states/signatory_directory_all_states.csv").exists()


def test_match_binds_state_roster_and_filters_blank_signers(P, repo, rosters, monkeypatch, capsys):
    write_csv(repo / "data/states/UP/signatures.csv", [
        dict(doc_id="d1", sig_rank=1, signatory="Rohit Verma"), dict(doc_id="d2", sig_rank=1, signatory="")])
    seen = {}

    def fake_match():
        seen["roster"] = P.S.load_rosters()
        seen["sig"] = read(P.S.OUT / "signatures.csv")
        seen["central"] = P.S.CENTRAL.pattern
        seen["mk"] = P.S.ministry_key("anything")
    monkeypatch.setattr(P.S, "match", fake_match)
    P.match(ns(states=["UP", "KL"]))                                           # KL has no roster rows -> skipped
    assert set(seen["roster"].name) == {"Rohit Verma", "Sita Devi", "Tara Das"}
    assert list(seen["sig"].signatory) == ["Rohit Verma"]
    assert seen["central"] == "." and seen["mk"] == {"_same_state"}
    out = capsys.readouterr().out
    assert "[UP] match: roster 3" in out and "[KL] match: no roster or no signatures" in out


def test_matrix_stage_writes_overview(P, repo, monkeypatch):
    for st in ("UP", "TN"):
        d = repo / f"data/states/{st}"
        write_csv(d / "candidates.csv", [dict(doc_id="d1", ministry="M")])
        write_csv(d / "signatures.csv", [dict(doc_id="d1", sig_rank=1, sig_script="DEVANAGARI" if st == "UP" else "LATIN")])
        (d / "pdf").mkdir(parents=True, exist_ok=True)
        (d / "pdf/d1.pdf").write_bytes(b"x")
        write_csv(d / "notification_signatories.csv", [dict(doc_id="d1", match_status="matched", officer_id="o1")])

    def fake_matrix():
        (P.S.OUT / "SIGNATORY_MATRIX.md").write_text("# Who signed what\nbody")
    monkeypatch.setattr(P.S, "matrix", fake_matrix)
    P.matrix(ns(states=["UP", "TN", "KL"]))
    assert (repo / "data/states/UP/SIGNATORY_MATRIX.md").read_text().startswith("# UP — who signed what")
    allns = read(repo / "data/states/notification_signatories_all_states.csv")
    assert list(allns.state) == ["UP", "TN"]
    md = (repo / "data/states/STATE_MATRIX.md").read_text()
    assert "| UP (Hindi) | 1 | 1 | 1 | 1 | 1 | 1 | [UP/SIGNATORY_MATRIX.md](UP/SIGNATORY_MATRIX.md) |" in md
    assert "| TN (Tamil) | 1 | 1 | 1 | 1 | 1 | 0 |" in md
    # no notification files at all -> no overview
    (repo / "data/states/STATE_MATRIX.md").unlink()
    P.matrix(ns(states=["KL"]))
    assert not (repo / "data/states/STATE_MATRIX.md").exists()


def test_stage_list_and_main_dispatch(P, repo, orgs):
    assert P.STAGES == ["targets", "whoswho", "crawl", "select", "fetch", "extract", "translate", "directory", "match", "matrix", "directory"]
    from conftest import run_script
    run_script("state_pipeline", ["targets", "--states", "up, tn", "--max-sites", "1"])
    t = read(repo / "data/states/targets.csv")
    assert set(t.state) == {"UP", "TN"}


# ------------------------------------------------------------------ whoswho stage
def _targets(repo, rows):
    write_csv(repo / "data/states/targets.csv", rows, ["state", "name", "website", "igod_org_id", "category_code", "slug"])


def test_whoswho_stage_scrapes_and_resumes(P, repo, monkeypatch, capsys):
    import requests
    _targets(repo, [
        dict(state="UP", name="Dept A", website="https://a.up", igod_org_id="1", slug="a"),
        dict(state="UP", name="Dept Dead", website="https://dead.up", igod_org_id="2", slug="d"),
        dict(state="UP", name="Dept Boom", website="https://boom.up", igod_org_id="3", slug="b"),
        dict(state="UP", name="Dept None", website="https://none.up", igod_org_id="", slug="n"),
        dict(state="TN", name="Dept T", website="https://t.tn", igod_org_id="5", slug="t"),
    ])
    W = P.W if hasattr(P, "W") else None

    class Head:
        pass

    def fake_head(url, **kw):
        if "dead" in url:
            raise requests.ConnectionError("x")
        return Head()

    class StreamResp:
        def close(self):
            pass

    def fake_get(url, **kw):
        if "dead" in url:
            raise requests.ConnectionError("x")
        return StreamResp()
    monkeypatch.setattr(requests, "head", fake_head)
    monkeypatch.setattr(requests, "get", fake_get)
    import ministry_whoswho as MW

    def fake_scrape(row):
        if "boom" in row["website"]:
            raise RuntimeError("scraper exploded")
        if "none" in row["website"]:
            return row["name"], row["website"], "", []
        return row["name"], row["website"], row["website"] + "/whos-who", [
            {"name": "Amit Kumar", "designation": "Dir", "division": "d", "room": "1", "phones": "11", "email": "a@b.in"},
            {"name": "Bina Rao", "designation": "", "phones": ["2", "3"]}]
    monkeypatch.setattr(MW, "scrape_ministry", fake_scrape)
    P.whoswho(ns(states=["UP"]))
    df = read(repo / "data/states/state_officials.csv", keep_default_na=False)
    by = df.groupby("department").size().to_dict()
    assert by == {"Dept A": 2, "Dept Dead": 1, "Dept Boom": 1, "Dept None": 1}
    a = df[df.department == "Dept A"]
    assert set(a.name) == {"Amit Kumar", "Bina Rao"} and "2; 3" in set(a.phones) and a.source_url.iloc[0] == "https://a.up/whos-who"
    assert df[df.department == "Dept Dead"].source_url.iloc[0] == "(none: unreachable: ConnectionError)"
    assert df[df.department == "Dept Boom"].source_url.iloc[0] == "(none: scraper exploded)"
    assert df[df.department == "Dept None"].source_url.iloc[0] == "(none: )"
    assert "whoswho: 2 officers across 1 departments" in capsys.readouterr().out
    # the wider probe list was installed on the shared module
    assert "/telephone-directory" in MW.PROBE_PATHS and "officials" in MW.WHO_RE.pattern
    # second run: every attempted website is skipped
    monkeypatch.setattr(MW, "scrape_ministry", lambda row: pytest.fail("already attempted"))
    P.whoswho(ns(states=["UP"]))
    assert "0 sites to scan (4 done)" in capsys.readouterr().out
