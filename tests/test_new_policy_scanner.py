"""scripts/new_policy_scanner.py with LLM and HTTP faked."""
import hashlib
import json
import sqlite3
import sys
from datetime import date, timedelta

import pandas as pd
import pytest
import requests

from helpers import read, write_csv, write_gz_csv


@pytest.fixture
def N(load):
    m = load("new_policy_scanner")
    m.S._WORDS = set()
    return m


def _key(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]


@pytest.mark.parametrize("title,hit", [
    ("Cabinet approves new PLI scheme for textiles", True), ("Interest subvention extended till 2026", True),
    ("Applications invited for EoI", True), ("Visit of Minister to Japan", False), ("Weekly cleanliness drive", False)])
def test_keyword_filters(N, title, hit):
    assert (bool(N.KEY.search(title)) and not N.NOISE.search(title)) is hit


def test_noise_blocks_even_keyword_titles(N):
    t = "Minister inaugurates scheme exhibition"
    assert N.KEY.search(t) and N.NOISE.search(t)


def test_instr_key(N):
    assert N.instr_key("PM Kisan Yojana Scheme 2024") == "kisan 2024"
    assert N.instr_key(None) == "none"
    assert N.instr_key("The Mission for A of") == ""


# ------------------------------------------------------------------ regex_detail
TEXT = ("The Cabinet approved an outlay of Rs. 12,000 crore for the scheme. The scheme is valid till 31 March 2030. "
        "Eligible units may apply on the portal at https://pli.gov.in/apply for registration. Posted On: 1 Jan 2025")


def test_regex_detail_extracts_outlay_period_howto(N):
    d = N.regex_detail(TEXT)
    assert d["outlay"] == "Rs. 12,000 crore"
    assert d["period"].startswith("valid till 31 March 2030") and "Posted" not in d["period"]
    assert "https://pli.gov.in/apply" in d["how_to_apply"]
    assert d["eligibility"] == "" and d["nodal_body"] == ""


def test_regex_detail_period_requires_year_or_duration_and_is_capped(N):
    assert N.regex_detail("valid until further orders are issued")["period"] == ""
    assert N.regex_detail("for a period of 5 years from now")["period"].startswith("for a period of 5 years")
    long = "till " + "2024 " * 40
    assert len(N.regex_detail(long)["period"]) <= 90
    d = N.regex_detail("nothing relevant here")
    assert d == {"outlay": "", "period": "", "eligibility": "", "how_to_apply": "", "nodal_body": ""}
    assert len(N.regex_detail("apply at " + "x" * 80 + " https://" + "a" * 200 + ".gov.in")["how_to_apply"]) <= 160


# ------------------------------------------------------------------ pib_text
class R:
    def __init__(self, text="", status=200):
        self.text, self.status_code = text, status


def test_pib_text_fetch_cache_and_url_rewrite(N, repo, monkeypatch):
    seen = []

    def fake_get(u, headers, timeout):
        seen.append(u)
        return R('<html><div class="innner-page-main-about-us-content-right-part"><p>Body   text\n here</p></div><footer>x</footer></html>')
    monkeypatch.setattr(N.requests, "get", fake_get)
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    t = N.pib_text("https://pib.gov.in/PressReleasePage.aspx?PRID=5")
    assert t == "Body text here"
    assert seen == ["https://www.pib.gov.in/PressReleasePage.aspx?PRID=5&reg=3&lang=1"]
    assert (repo / "data/new_policies/pib" / f"{_key('https://pib.gov.in/PressReleasePage.aspx?PRID=5')}.txt").read_text() == "Body text here"
    assert N.pib_text("https://pib.gov.in/PressReleasePage.aspx?PRID=5") == "Body text here" and len(seen) == 1       # cached
    N.pib_text("https://pib.gov.in/x")
    assert seen[-1] == "https://www.pib.gov.in/x?reg=3&lang=1"
    N.pib_text("https://pib.gov.in/y?lang=2")
    assert seen[-1] == "https://www.pib.gov.in/y?lang=2"                                # an explicit language is respected


def test_pib_text_fallbacks_and_errors(N, repo, monkeypatch):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: R('<div id="PdfDiv">pdf  body</div>'))
    assert N.pib_text("https://pib.gov.in/a") == "pdf body"
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: R("<p>plain page</p>"))
    assert N.pib_text("https://pib.gov.in/b") == "plain page"
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: R("x" * 9000))
    assert len(N.pib_text("https://pib.gov.in/c")) == 6000
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: R("nope", 500))
    assert N.pib_text("https://pib.gov.in/d") == "" and not (repo / "data/new_policies/pib" / f"{_key('https://pib.gov.in/d')}.txt").exists()
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: (_ for _ in ()).throw(requests.Timeout()))
    assert N.pib_text("https://pib.gov.in/e") == ""


def test_pib_text_rate_limits_to_one_request_per_second(N, repo, monkeypatch):
    sleeps = []
    monkeypatch.setattr(N.time, "sleep", sleeps.append)
    monkeypatch.setattr(N.requests, "get", lambda u, headers, timeout: R("<p>x</p>"))
    N._last[0] = N.time.time()
    N.pib_text("https://pib.gov.in/rate")
    assert len(sleeps) == 1 and 0 < sleeps[0] <= 1.0


# ------------------------------------------------------------------ shortlists
def test_shortlist_pib_filters_by_date_kind_keywords_and_noise(N, repo):
    db = repo / "pib.sqlite"
    con = sqlite3.connect(db)
    con.execute("create table pib_items (date text, ministry text, title text, url text, kind text)")
    con.executemany("insert into pib_items values (?,?,?,?,?)", [
        ("2025-03-02", "Ministry  A", "Cabinet approves   PLI scheme", "http://1", "release"),
        ("2025-03-01", "Ministry B", "Minister inaugurates exhibition of scheme", "http://2", "release"),
        ("2025-03-01", "Ministry B", "Plain statistics", "http://3", "release"),
        ("2025-03-01", "Ministry B", "Subsidy extended", "http://4", "feature"),
        ("2024-12-31", "Ministry C", "Old scheme", "http://5", "release"),
        ("2025-01-01", None, None, "http://6", "release"),
    ])
    con.commit()
    con.close()
    df = N.shortlist_pib(db, "2025-01-01")
    assert list(df.url) == ["http://1"]
    assert df.iloc[0].to_dict() == {"source": "PIB", "date": "2025-03-02", "ministry": "Ministry A", "title": "Cabinet approves PLI scheme", "url": "http://1", "subject": ""}
    assert list(N.shortlist_pib(db, "2025-03-02").url) == ["http://1"]                 # >= since is inclusive
    assert N.shortlist_pib(db, "2026-01-01").empty


def test_shortlist_ministry_uses_dates_keywords_and_signature_subjects(N, repo):
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz", [
        dict(ministry="M", title="Revised guidelines for Rooftop scheme", category="", group="", url="http://m/1.pdf", date="2025-02-01"),
        dict(ministry="M", title="Meeting with  visiting delegation", category="scheme", group="", url="http://m/2.pdf", date="2025-02-01"),
        dict(ministry="M", title="Untitled", category="incentive", group="", url="http://m/3.pdf", date="2025-02-02"),
        dict(ministry="M", title="Old scheme", category="", group="", url="http://m/4.pdf", date="2020-01-01"),
        dict(ministry="M", title="Scheme with bad date", category="", group="", url="http://m/5.pdf", date="n/a"),
    ])
    write_csv(repo / "data/signatories/signatures.csv", [dict(doc_id=N.S.doc_id("http://m/1.pdf"), subject="Subject line", sig_rank=1),
                                                         dict(doc_id=N.S.doc_id("http://m/1.pdf"), subject="dup", sig_rank=2)])
    df = N.shortlist_ministry("2025-01-01")
    assert set(df.url) == {"http://m/1.pdf", "http://m/3.pdf"}                      # noise title and old / undated rows dropped
    assert df.set_index("url").loc["http://m/1.pdf", "subject"] == "Subject line"
    assert df.set_index("url").loc["http://m/3.pdf", "subject"] == ""
    assert set(df.source) == {"ministry site"}


# ------------------------------------------------------------------ classify / enrich
def _items(n=3, source="PIB"):
    return pd.DataFrame([dict(source=source, date=f"2025-01-0{i+1}", ministry="M", title=f"Scheme {i}", url=f"http://u/{i}", subject="") for i in range(n)])


def test_classify_calls_llm_in_chunks_and_caches(N, repo, monkeypatch):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    reqs = []

    def fake_groq(system, user, **kw):
        req = json.loads(user)
        reqs.append(req)
        return {"items": [{"i": it["i"], "is_instrument": it["i"] % 2 == 0, "instrument": f"Inst {it['title']}", "type": "scheme", "status": "launched",
                           "new_or_update": "new", "beneficiaries": "b", "summary": "s"} for it in req["items"]]}
    monkeypatch.setattr(N, "groq_json", fake_groq)
    df, calls = N.classify(_items(12), {}, max_llm=5)
    assert calls == 2 and [len(r["items"]) for r in reqs] == [10, 2]
    assert df.is_instrument.tolist() == [True, False] * 6 and df.instrument.iloc[0] == "Inst Scheme 0"
    cached = json.loads((repo / "data/new_policies/classify_cache.json").read_text())
    assert len(cached) == 12
    # a second run makes no LLM calls
    monkeypatch.setattr(N, "groq_json", lambda *a, **k: pytest.fail("cache should be used"))
    df2, calls2 = N.classify(_items(12), cached, max_llm=5)
    assert calls2 == 0 and df2.is_instrument.tolist() == df.is_instrument.tolist()


def test_classify_respects_max_llm_and_does_not_cache_failures(N, repo, monkeypatch):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    monkeypatch.setattr(N, "groq_json", lambda *a, **k: None)
    cache = {}
    df, calls = N.classify(_items(25), cache, max_llm=2)
    assert calls == 2 and cache == {} and df.is_instrument.isna().all()
    assert not (repo / "data/new_policies/classify_cache.json").exists()
    n = {"c": 0}

    def groq(system, user, **kw):
        n["c"] += 1
        return {"items": []}                                 # model omitted every item -> cached as unknown
    monkeypatch.setattr(N, "groq_json", groq)
    cache = {}
    df, calls = N.classify(_items(3), cache, max_llm=1)
    assert calls == 1 and all(v == {"is_instrument": None} for v in cache.values()) and len(cache) == 3


def test_enrich_pib_regex_mode_llm_mode_and_limits(N, repo, monkeypatch):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    df = _items(4)
    df["key"] = df.url.map(_key)
    df["is_instrument"] = [True, True, True, False]
    df.loc[2, "source"] = "ministry site"
    texts = {"http://u/0": TEXT + " " * 0 + "x" * 200, "http://u/1": "short"}
    monkeypatch.setattr(N, "pib_text", lambda u: texts.get(u, ""))
    monkeypatch.setenv("NO_LLM_DETAIL", "1")
    out, calls = N.enrich_pib(df, {}, max_llm=5)
    assert calls == 0
    assert out.loc[0, "outlay"] == "Rs. 12,000 crore" and out.loc[1, "outlay"] == "" and out.loc[3, "outlay"] == ""
    assert json.loads((repo / "data/new_policies/classify_cache.json").read_text())["detail:" + df.key[1]] == {}
    # LLM mode
    monkeypatch.delenv("NO_LLM_DETAIL")
    sleeps = []
    monkeypatch.setattr(N.time, "sleep", sleeps.append)
    seen = []
    monkeypatch.setattr(N, "groq_json", lambda s, u, **kw: (seen.append((len(u), kw)), {"outlay": "Rs 1", "period": "p", "eligibility": "e", "how_to_apply": "h", "nodal_body": "n"})[1])
    out, calls = N.enrich_pib(df, {}, max_llm=5)
    assert calls == 1 and out.loc[0, "nodal_body"] == "n" and seen[0][1] == {"max_tokens": 450} and 7.0 in sleeps and seen[0][0] <= 2600
    # failed call is not cached; max_llm=0 never calls
    monkeypatch.setattr(N, "groq_json", lambda *a, **k: None)
    cache = {}
    out, calls = N.enrich_pib(df, cache, max_llm=5)
    assert "detail:" + df.key[0] not in cache and out.loc[0, "outlay"] == ""
    monkeypatch.setattr(N, "groq_json", lambda *a, **k: pytest.fail("limit reached"))
    out, calls = N.enrich_pib(df, {}, max_llm=0)
    assert calls == 0


# ------------------------------------------------------------------ attach_known_and_contacts
def _attach_world(repo):
    write_csv(repo / "data/policy_windows.csv", [dict(instrument="Rooftop Solar Programme (RSP)")])
    write_csv(repo / "data/policy_instruments_index.csv", [dict(instrument="Textile PLI Scheme", n_documents=7)])
    write_csv(repo / "data/policy_contacts_from_documents.csv", [
        dict(instrument="Textile PLI Scheme", contact="Amit Kumar", designation="JS", email="a@gov.in", evidence="signed documents"),
        dict(instrument="Textile PLI Scheme", contact="Roster Guy", designation="D", email="", evidence="roster division matches instrument")])
    write_csv(repo / "data/signatories/signatory_directory.csv", [
        dict(ministry="Ministry of Power", signatory="Bina Rao", designations="Director | Under Secretary", n_documents=5, email="b@gov.in"),
        dict(ministry="Ministry of Power", signatory="Clerk Person", designations="Assistant", n_documents=9, email=""),
        dict(ministry="Ministry of Power", signatory="Dee Kay", designations="Joint Secretary", n_documents=2, email=""),
        dict(ministry="Ministry of Coal", signatory="Coal Person", designations="Scientist", n_documents=1, email="")])
    write_csv(repo / "data/pib_ministry_contacts.csv", [
        dict(ministry="Ministry of Culture", contact_name="Raj Singh", designation="Secretary", email="r@gov.in"),
        dict(ministry="Ministry of Culture", contact_name="", designation="x", email=""),
        dict(ministry="Ministry of Culture", contact_name="Lal Roy", designation="Director", email="")])


def test_attach_known_and_contacts_three_evidence_levels(N, repo):
    _attach_world(repo)
    df = pd.DataFrame([
        dict(instrument="Rooftop Solar Programme", title="t", ministry="Ministry of Power"),
        dict(instrument="Textile PLI Scheme extension", title="t", ministry="Ministry of Textiles"),
        dict(instrument="Heritage thing", title="t", ministry="Ministry of Culture"),
        dict(instrument=None, title="Nothing known about Zebra", ministry="Mystery Org"),
    ])
    out = N.attach_known_and_contacts(df)
    r0, r1, r2, r3 = (out.iloc[i] for i in range(4))
    assert r0.known_curated_instrument == "Rooftop Solar Programme (RSP)" and r0.seen_in_document_index == ""
    assert r0.contact_evidence == "most active signers in this ministry"
    assert r0.contacts == "Bina Rao (Director, b@gov.in); Dee Kay (Joint Secretary)"           # assistants excluded, most documents first
    assert r1.seen_in_document_index == "Textile PLI Scheme" and r1.docs_in_index == 7
    assert r1.contacts == "Amit Kumar (JS, a@gov.in)" and r1.contact_evidence == "signed this instrument's documents"
    assert r2.contact_evidence == "igod minister/secretary contact" and r2.contacts == "Raj Singh (Secretary, r@gov.in); Lal Roy (Director)"
    assert r3.contacts == "" and r3.contact_evidence == "" and r3.known_curated_instrument == "" and r3.docs_in_index == 0
    assert list(out.index) == [0, 1, 2, 3]


def test_attach_known_and_contacts_without_any_reference_files(N):
    out = N.attach_known_and_contacts(pd.DataFrame([dict(instrument="X Scheme", title="t", ministry="M")]))
    assert out.iloc[0].contacts == "" and out.iloc[0].docs_in_index == 0


# ------------------------------------------------------------------ report + main
def test_write_report_sections(N, repo):
    df = pd.DataFrame([
        dict(is_instrument=True, new_or_update="new", known_curated_instrument="Known", docs_in_index=2, contacts="C", date="2025-02-01", ministry="M",
             instrument="Alpha", type="scheme", status="launched", summary="S" * 300, outlay="Rs 1", period="p", source="PIB", url="http://a"),
        dict(is_instrument=True, new_or_update="update", known_curated_instrument="", docs_in_index=0, contacts="", date="2025-03-01", ministry="M",
             instrument="Beta", type="PLI", status="extended", summary="s", outlay="", period="", source="PIB", url="http://b"),
        dict(is_instrument=False, new_or_update=None, known_curated_instrument="", docs_in_index=0, contacts="", date="2025-01-01", ministry="M",
             instrument=None, type=None, status=None, summary=None, outlay="", period="", source="PIB", url="http://c"),
    ])
    N.write_report(df, "2025-01-01")
    md = (repo / "data/NEW_POLICIES.md").read_text()
    assert "# New policies & incentives since 2025-01-01" in md and "Shortlisted 3 items" in md and "2 classified as policy/incentive" in md
    assert "| Instruments: new | 1 |" in md and "| Instruments: updates / amendments / extensions | 1 |" in md
    assert "| Already in the curated incentive list | 1 |" in md and "| With a named contact | 1 |" in md
    assert "| 2025-02-01 | M | **Alpha** | scheme / launched | " + "S" * 160 + " |" in md and "S" * 161 not in md
    assert "| 2025-03-01 | M | Beta | PLI / extended |" in md
    assert "Gamma" not in md and "http://c" not in md


def test_main_end_to_end(N, repo, monkeypatch, capsys):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    monkeypatch.setenv("NO_LLM_DETAIL", "1")
    today = date.today()
    recent = (today - timedelta(days=10)).isoformat()
    db = repo / "pib.sqlite"
    con = sqlite3.connect(db)
    con.execute("create table pib_items (date text, ministry text, title text, url text, kind text)")
    con.execute("insert into pib_items values (?,?,?,?,?)", (recent, "Ministry of Power", "Cabinet approves Rooftop Solar scheme", "http://pib/1", "release"))
    con.execute("insert into pib_items values (?,?,?,?,?)", (recent, "Ministry of Power", "Scheme statistics report", "http://pib/2", "release"))
    con.commit()
    con.close()
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz", [
        dict(ministry="Ministry of Coal", title="Incentive notification", category="", group="", url="http://m/1.pdf", date=recent),
        dict(ministry="Ministry of Power", title="Dup", category="scheme", group="", url="http://pib/1", date=recent)])

    def fake_groq(system, user, **kw):
        req = json.loads(user)
        if "items" in req:
            return {"items": [{"i": it["i"], "is_instrument": "Rooftop" in it["title"] or "Incentive" in it["title"],
                               "instrument": "Rooftop Solar Scheme" if "Rooftop" in it["title"] else "Coal Incentive",
                               "type": "scheme", "status": "launched", "new_or_update": "new", "summary": "s"} for it in req["items"]]}
        return {}
    monkeypatch.setattr(N, "groq_json", fake_groq)
    monkeypatch.setattr(N, "pib_text", lambda u: "")
    monkeypatch.setattr(sys, "argv", ["x", "--days", "30", "--max-llm", "5", "--pib-db", str(db)])
    N.main()
    out = read(repo / "data/new_policies_incentives.csv", keep_default_na=False)
    assert set(out.url) == {"http://pib/1", "http://pib/2", "http://m/1.pdf"}        # duplicate url across sources collapsed
    flags = dict(zip(out.url, out.is_instrument.astype(str).str.lower()))
    assert flags == {"http://pib/1": "true", "http://pib/2": "false", "http://m/1.pdf": "true"}
    disc = read(repo / "data/discovered_instruments.csv")
    assert set(disc.instrument) == {"Rooftop Solar Scheme", "Coal Incentive"}
    assert (repo / "data/NEW_POLICIES.md").exists() and "key" not in out.columns
    assert "shortlist: 3 items since" in capsys.readouterr().out


def test_main_without_pib_database_uses_ministry_site_only(N, repo, monkeypatch):
    monkeypatch.setattr(N.time, "sleep", lambda s: None)
    recent = (date.today() - timedelta(days=5)).isoformat()
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz", [dict(ministry="M", title="Subsidy scheme order", category="", group="", url="http://m/1.pdf", date=recent)])
    monkeypatch.setattr(N, "groq_json", lambda s, u, **kw: {"items": [{"i": 0, "is_instrument": True, "instrument": "Subsidy Scheme", "type": "subsidy", "status": "notified", "new_or_update": "update", "summary": "x"}]})
    monkeypatch.setattr(sys, "argv", ["x", "--pib-db", str(repo / "missing.sqlite")])
    N.main()
    assert list(read(repo / "data/discovered_instruments.csv").instrument) == ["Subsidy Scheme"]
