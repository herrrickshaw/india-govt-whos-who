"""scripts/career_tracker.py with HTTP and the LLM faked."""
import argparse
import hashlib
import json
from datetime import datetime, timedelta

import pandas as pd
import pytest
import requests

from helpers import read, write_csv


@pytest.fixture
def C(load):
    m = load("career_tracker")
    m.S._WORDS = set()
    return m


def aid(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]


class R:
    def __init__(self, text="", status=200, js=None):
        self.text, self.status_code, self._js = text, status, js

    def json(self):
        if isinstance(self._js, Exception):
            raise self._js
        return self._js


# ------------------------------------------------------------------ http + storage
def test_get_rate_limits_per_host_and_handles_errors(C, monkeypatch):
    sleeps = []
    monkeypatch.setattr(C.time, "sleep", sleeps.append)
    monkeypatch.setattr(C.requests, "get", lambda u, headers, timeout: R("ok", 200 if "good" in u else 404))
    C._last.clear()
    assert C.get("https://h.in/good").text == "ok"
    assert sleeps == []                                         # first request to a host is immediate
    assert C.get("https://h.in/good2").status_code == 200 and len(sleeps) == 1 and 0 < sleeps[0] <= 1.0
    assert C.get("https://other.in/good") is not None and len(sleeps) == 1       # another host has its own clock
    assert C.get("https://h.in/missing") is None                                  # non-200
    monkeypatch.setattr(C.requests, "get", lambda u, headers, timeout: (_ for _ in ()).throw(requests.Timeout()))
    assert C.get("https://h.in/x") is None


def test_save_article_and_have(C, repo):
    assert C.have("http://a") is False
    assert C.save_article("src", "http://a", "T", "2025-01-01", "txt", {"x": 1}) is True
    assert C.have("http://a") is True
    saved = json.loads((repo / "data/career/articles" / f"{aid('http://a')}.json").read_text())
    assert saved == {"id": aid("http://a"), "source": "src", "url": "http://a", "title": "T", "date": "2025-01-01", "text": "txt", "x": 1}
    assert C.save_article("src", "http://a", "other", "", "") is False                # never overwrites
    assert C.save_article("src", "http://b", None, None, None) is True
    assert json.loads((repo / "data/career/articles" / f"{aid('http://b')}.json").read_text())["title"] == ""


ARTICLE = """<html><head><title>Site title</title><meta property="article:published_time" content="2025-03-04T10:00:00Z">
<meta name="description" content="Short description of the appointment news"></head>
<body><article><h1>IAS officer Amit Kumar appointed as Secretary</h1>
<p>Short.</p><p>This is a long paragraph with more than forty characters in it, certainly.</p>
<p>""" + "Another long paragraph of text about transfers. " * 2 + """</p></article></body></html>"""


def test_article_html_extracts_title_date_text(C, repo, monkeypatch):
    monkeypatch.setattr(C, "get", lambda url: R(ARTICLE))
    assert C.article_html("http://x/a", "whispers") is True
    a = json.loads((repo / "data/career/articles" / f"{aid('http://x/a')}.json").read_text())
    assert a["title"] == "IAS officer Amit Kumar appointed as Secretary" and a["date"] == "2025-03-04" and a["source"] == "whispers"
    lines = a["text"].split("\n")
    assert lines[0] == "Short description of the appointment news"                    # description prepended when not already in text
    assert "Short." not in lines and len(lines) == 3
    assert C.article_html("http://x/a", "whispers") is False                           # already saved
    monkeypatch.setattr(C, "get", lambda url: None)
    assert C.article_html("http://x/none", "s") is False


def test_article_html_fallbacks(C, repo, monkeypatch):
    html = "<html><head><title>Fallback title</title></head><body><time datetime='2024-12-25T01:02'>x</time><p>" + "p" * 50 + "</p></body></html>"
    monkeypatch.setattr(C, "get", lambda url: R(html))
    C.article_html("http://x/b", "s")
    a = json.loads((repo / "data/career/articles" / f"{aid('http://x/b')}.json").read_text())
    assert a["title"] == "Fallback title" and a["date"] == "2024-12-25" and a["text"] == "p" * 50
    html2 = "<html><body><time>2023-01-02 text</time><p>" + "q" * 50 + "</p></body></html>"
    monkeypatch.setattr(C, "get", lambda url: R(html2))
    C.article_html("http://x/c", "s")
    assert json.loads((repo / "data/career/articles" / f"{aid('http://x/c')}.json").read_text())["date"] == "2023-01-02"
    html3 = '<html><head><meta name="publish-date" content="2022-05-06"><meta name="description" content="' + "q" * 50 + '"></head><body><p>' + "q" * 50 + "</p></body></html>"
    monkeypatch.setattr(C, "get", lambda url: R(html3))
    C.article_html("http://x/d", "s")
    d = json.loads((repo / "data/career/articles" / f"{aid('http://x/d')}.json").read_text())
    assert d["date"] == "2022-05-06" and d["text"] == "q" * 50                          # description not duplicated when its first 60 chars are in the text


# ------------------------------------------------------------------ collectors
def test_collect_sarkarimirror_pages_until_short_page_and_dedups(C, repo, monkeypatch, capsys):
    urls = []

    def fake_get(url):
        urls.append(url)
        if "search=appointed" in url and "page=1&" in url:
            return R(js=[{"link": f"http://sm/{i}", "date": "2025-01-0" + str(i % 9 + 1) + "T00:00:00", "title": {"rendered": f"<b>T{i}</b>"},
                          "content": {"rendered": "<p>Body one</p><p>two</p>"}, "excerpt": {"rendered": ""}} for i in range(100)])
        if "search=appointed" in url:
            return R(js=[])
        if "search=transferred" in url:
            return R(text="x", js=ValueError("bad json"))
        if "search=posted" in url:
            return R(js=[{"link": "http://sm/0", "title": {"rendered": "dup"}}])                  # already saved from the first term
        if "search=reshuffle" in url:
            return R(js=[{"link": "http://sm/new", "date": None, "title": None, "content": None, "excerpt": {"rendered": "<p>Excerpt</p>"}}])
        return None
    monkeypatch.setattr(C, "get", fake_get)
    C.collect_sarkarimirror(max_articles=1000)
    assert "per_page=100&page=2" in "".join(urls)                                          # a full page triggers the next one
    a0 = json.loads((C.ART / f"{aid('http://sm/0')}.json").read_text())
    assert a0["title"] == "T0" and a0["text"] == "Body one\ntwo" and a0["date"] == "2025-01-01"
    new = json.loads((C.ART / f"{aid('http://sm/new')}.json").read_text())
    assert new["text"] == "Excerpt" and new["title"] == "" and new["date"] == ""
    assert "sarkarimirror: 101 new articles" in capsys.readouterr().out


def test_collect_sarkarimirror_stops_at_max_articles(C, repo, monkeypatch, capsys):
    monkeypatch.setattr(C, "get", lambda url: R(js=[{"link": f"http://sm/{url[-30:]}{i}", "title": {"rendered": "t"}, "content": {"rendered": "c"}} for i in range(100)]))
    C.collect_sarkarimirror(max_articles=50)
    assert "sarkarimirror: 100 new articles" in capsys.readouterr().out                     # stops after the first full page overshoots the cap


def test_collect_psuwatch_filters_urls_and_respects_cap(C, repo, monkeypatch, capsys):
    today = datetime.utcnow().date()
    day0 = f"/sitemap/sitemap-daily-{today.isoformat()}.xml"
    pages = {day0: "<loc>https://psuwatch.com/bureaucracywatch/a</loc><loc>https://psuwatch.com/news/appointed-md-x</loc><loc>https://psuwatch.com/sports/cricket</loc>"}
    monkeypatch.setattr(C, "get", lambda url: R(pages[url.replace("https://psuwatch.com", "")]) if url.replace("https://psuwatch.com", "") in pages else None)
    fetched = []
    monkeypatch.setattr(C, "article_html", lambda u, s: (fetched.append((u, s)), True)[1])
    C.collect_psuwatch(max_articles=10, days=3)
    assert fetched == [("https://psuwatch.com/bureaucracywatch/a", "psuwatch"), ("https://psuwatch.com/news/appointed-md-x", "psuwatch")]
    assert "psuwatch: 2 candidate urls, 2 new articles" in capsys.readouterr().out
    fetched.clear()
    C.save_article("psuwatch", "https://psuwatch.com/bureaucracywatch/a", "", "", "")
    C.collect_psuwatch(max_articles=1, days=1)
    assert fetched == [("https://psuwatch.com/news/appointed-md-x", "psuwatch")]            # saved article skipped; cap of 1 stops the loop


def test_collect_whispers_sitemap_and_category_pages(C, repo, monkeypatch, capsys):
    host = "https://whispersinthecorridors.in"
    pages = {
        f"{host}/sitemap-news.xml": "<loc>https://whispersinthecorridors.in/news/ias-transfer-1</loc><loc>https://whispersinthecorridors.in/news/cricket-2</loc>",
        f"{host}/category/bureaucracy?page=1": '<a href="/news/new-secretary-appointed-3">x</a><a href="/news/gossip-4">y</a>',
        f"{host}/category/bureaucracy?page=2": '<a href="/news/ips-posted-5">x</a>',
    }
    monkeypatch.setattr(C, "get", lambda url: R(pages[url]) if url in pages else None)
    fetched = []
    monkeypatch.setattr(C, "article_html", lambda u, s: (fetched.append(u), True)[1])
    C.collect_whispers(max_articles=100, days=10)
    assert sorted(fetched) == sorted([f"{host}/news/ias-transfer-1", f"{host}/news/new-secretary-appointed-3", f"{host}/news/ips-posted-5"])
    assert "whispersinthecorridors: 3 candidate urls, 3 new articles" in capsys.readouterr().out


def test_collect_whispers_alternate_pagination_pattern_and_cap(C, repo, monkeypatch, capsys):
    host = "https://whispersinthecorridors.in"
    pages = {f"{host}/category/archives/page/1": '<a href="/news/ias-a">x</a><a href="/news/ias-b">y</a>'}
    monkeypatch.setattr(C, "get", lambda url: R(pages[url]) if url in pages else None)
    fetched = []
    monkeypatch.setattr(C, "article_html", lambda u, s: (fetched.append(u), True)[1])
    C.collect_whispers(max_articles=1, days=10)
    assert fetched == [f"{host}/news/ias-a"]


def test_collect_runs_all_sources(C, repo, monkeypatch, capsys):
    called = []
    monkeypatch.setattr(C, "collect_sarkarimirror", lambda n: called.append(("sm", n)))
    monkeypatch.setattr(C, "collect_psuwatch", lambda n, d: called.append(("psu", n, d)))
    monkeypatch.setattr(C, "collect_whispers", lambda n, d: called.append(("wh", n, d)))
    C.collect(argparse.Namespace(max_articles=7, days=9))
    assert called == [("sm", 7), ("psu", 7, 9), ("wh", 7, 9)] and "articles on disk: 0" in capsys.readouterr().out


# ------------------------------------------------------------------ events
def test_regex_events_title_and_body(C):
    art = {"id": "x", "source": "psuwatch", "url": "http://u", "date": "2025-02-02",
           "title": "Rohit Sharma, IAS (KN: 2001) appointed as Secretary in the Ministry of Power.",
           "text": "Neha Jain has been transferred to Director of Customs.\nsecond line\nSita Devi has been posted as Joint Secretary at the Department of Revenue;"}
    ev = C.regex_events(art)
    names = [e["name"] for e in ev]
    assert "Rohit Sharma" in names and "Neha Jain" in names
    t = ev[0]
    assert (t["service"], t["cadre"], t["batch"], t["event"], t["method"]) == ("IAS", "KN", "2001", "appointed", "regex-title")
    assert t["new_post"] == "Secretary" and t["new_org"] == "Ministry of Power" and t["event_date"] == "2025-02-02"
    b = next(e for e in ev if e["name"] == "Neha Jain")
    assert b["method"] == "regex-body" and b["event"] == "transferred" and b["new_post"].startswith("Director")
    assert all(e["url"] == "http://u" and e["source"] == "psuwatch" for e in ev)


def test_regex_events_rejects_non_people(C):
    art = {"id": "x", "source": "s", "url": "u", "title": "The Government has been appointed as Chairman of Board", "text": ""}
    assert C.regex_events(art) == []
    art2 = {"id": "x", "source": "s", "url": "u", "title": "Amit appointed as Director", "text": None}
    assert C.regex_events(art2) == []                                      # one-word name
    art3 = {"id": "x", "source": "s", "url": "u", "title": "", "text": ""}
    assert C.regex_events(art3) == []
    C.S._WORDS = {"rowan", "tree"}
    assert C.regex_events({"id": "x", "source": "s", "url": "u", "title": "Rowan Tree appointed as Director", "text": ""}) == []


def test_llm_events_parses_filters_and_caches(C, repo, monkeypatch):
    (repo / "data/career").mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(C.time, "sleep", lambda s: None)
    seen = []

    def fake_groq(system, user, **kw):
        seen.append(user)
        return {"events": [
            {"name": "Rohit Sharma", "service": "IAS", "batch": "KN:2001", "event": "Transferred", "new_post": "Secretary", "new_org": "Power", "previous_post": "JS"},
            {"name": "Solo", "event": "x"},
            {"name": "Government Of India", "event": "x"},
            {"name": "", "event": "x"},
            "not a dict",
            {"name": "Neha Jain"},
        ]}
    monkeypatch.setattr(C, "groq_json", fake_groq)
    art = {"id": "a1", "source": "sm", "url": "http://u", "date": "2025-01-01", "title": "Big reshuffle", "text": "x" * 7000}
    cache = {}
    rows = C.llm_events(art, cache)
    assert [r["name"] for r in rows] == ["Rohit Sharma", "Neha Jain"]
    r = rows[0]
    assert (r["event"], r["method"], r["snippet"], r["service"], r["batch"]) == ("transferred", "llm", "JS", "IAS", "KN:2001")
    assert len(seen[0]) <= 6000 + 2 and cache["a1"] == rows
    assert json.loads(C.LLM_CACHE.read_text())["a1"][0]["name"] == "Rohit Sharma"
    monkeypatch.setattr(C, "groq_json", lambda *a, **k: pytest.fail("cached"))
    assert C.llm_events(art, cache) == rows
    monkeypatch.setattr(C, "groq_json", lambda *a, **k: None)
    assert C.llm_events({**art, "id": "a2"}, cache) == [] and cache["a2"] == []             # failures are cached as empty (current behaviour)


def _put_article(C, **kw):
    a = dict(id=kw["id"], source="sm", url=f"http://u/{kw['id']}", title="", date="2025-01-01", text="")
    a.update(kw)
    (C.ART / f"{a['id']}.json").write_text(json.dumps(a))


def test_events_combines_regex_llm_and_ias_er_sheets(C, repo, monkeypatch, capsys):
    _put_article(C, id="a1", title="Rohit Sharma appointed as Secretary in Ministry of Power")
    _put_article(C, id="a2", title="Mass reshuffle of officers", text="")
    _put_article(C, id="a3", title="Nothing relevant", text="")
    calls = []
    monkeypatch.setattr(C, "llm_events", lambda a, cache: (calls.append(a["id"]), cache.__setitem__(a["id"], []), [dict(
        name="Llm Person", service="", cadre="", batch="", event="posted", new_post="Director", new_org="X", event_date="2025-01-01", source="sm", url=a["url"], snippet="", method="llm")])[2])
    write_csv(repo / "data/ias_officers.csv", [
        dict(name_en="Sita Devi", current_posting="Collector, Pune, Maharashtra", posting_wef="15/06/2024", cadre_code="MH", allotment_year="2010", er_sheet_url="http://er"),
        dict(name_en="No Post", current_posting="", posting_wef="", cadre_code="MH", allotment_year="2010", er_sheet_url=""),
        dict(name_en="Bad Date", current_posting="DM, Agra", posting_wef="June 2024", cadre_code="UP", allotment_year="2011", er_sheet_url="http://er2")])
    C.events(argparse.Namespace(max_llm=10))
    ev = read(C.CAREER / "career_events.csv", keep_default_na=False)
    assert calls == ["a2", "a3"]            # multi-officer title, and an article with no regex hit
    assert set(ev.method) == {"regex-title", "llm", "civil-list"}
    er = ev[ev.method == "civil-list"].set_index("name")
    assert er.loc["Sita Devi", "event_date"] == "2024-06-15" and er.loc["Sita Devi", "new_post"] == "Collector" and er.loc["Sita Devi", "service"] == "IAS"
    assert er.loc["Bad Date", "event_date"] == "" and "No Post" not in er.index
    assert "events: " in capsys.readouterr().out


def test_events_respects_llm_budget_and_kill_switch(C, repo, monkeypatch, capsys):
    for i in range(3):
        _put_article(C, id=f"m{i}", title="Mass reshuffle of officers")
    calls = []
    monkeypatch.setattr(C, "llm_events", lambda a, cache: (calls.append(a["id"]), [dict(name=f"Person{a['id']} Name{a['id']}", service="", cadre="", batch="", event="posted", new_post="D", new_org="X",
                                                                                             event_date="2025-01-01", source="sm", url=a["url"], snippet="", method="llm")])[1])
    C.events(argparse.Namespace(max_llm=2))
    assert calls == ["m0", "m1"]
    calls.clear()
    monkeypatch.setenv("CAREER_NO_LLM", "1")
    C.events(argparse.Namespace(max_llm=5))
    assert calls == []
    assert "events: none" in capsys.readouterr().out


def test_events_none_when_nothing_found(C, repo, capsys):
    C.events(argparse.Namespace(max_llm=0))
    assert "events: none" in capsys.readouterr().out and not (C.CAREER / "career_events.csv").exists()


# ------------------------------------------------------------------ attach
def _ev(rows):
    cols = ["name", "service", "cadre", "batch", "event", "new_post", "new_org", "event_date", "source", "url", "snippet", "method"]
    df = pd.DataFrame([{**{c: "" for c in cols}, **r} for r in rows])
    return df


def _directory(repo, rows, path="data/signatories/signatory_directory.csv"):
    write_csv(repo / path, rows, ["ministry", "signatory", "designations", "n_documents", "last_date"])


def test_attach_to_moved_same_org_and_confidence(C, repo):
    _directory(repo, [
        dict(ministry="Ministry of Power", signatory="Rohit Verma Sharma", designations="Joint Secretary", n_documents=3, last_date="2023-05-01"),
        dict(ministry="Ministry of Power", signatory="Neha Jain", designations="Director", n_documents=2, last_date="2023-05-01"),
        dict(ministry="Ministry of Power", signatory="Zed Unknown", designations="Director", n_documents=1, last_date="2023-05-01"),
        dict(ministry="Ministry of Coal", signatory="Sita Devi", designations="Secretary", n_documents=4, last_date="2024-01-15"),
        dict(ministry="Ministry of Power", signatory="Under Person", designations="Under Secretary", n_documents=1, last_date="2023-01-01"),
    ])
    ev = _ev([
        dict(name="Rohit Verma Sharma", new_post="Secretary", new_org="Pune Collectorate", event_date="2024-06-01", source="sm", url="http://e1"),
        dict(name="Neha Jain", new_post="Director", new_org="Ministry of Power", event_date="2024-06-01", source="sm", url="http://e2"),
        dict(name="Sita Devi", new_post="Collector", new_org="Pune", event_date="2023-06-01", source="sm", url="http://e3"),
        dict(name="Under Person", new_post="Chief Secretary", new_org="Elsewhere", event_date="2024-06-01", source="sm", url="http://e4"),
    ])
    d = C.attach_to(repo / "data/signatories/signatory_directory.csv", ev).set_index("signatory")
    r = d.loc["Rohit Verma Sharma"]
    assert (r.latest_posting, r.latest_posting_org, r.posting_match_confidence, r.moved_since_signing) == ("Secretary", "Pune Collectorate", "high", "yes")
    assert r.career_events_n == 1 and r.latest_posting_url == "http://e1"
    assert d.loc["Neha Jain", "posting_match_confidence"] == "medium"                                        # two-token name
    assert d.loc["Neha Jain", "moved_since_signing"] == "same org / older"                                     # same ministry token 'power'
    assert d.loc["Sita Devi", "moved_since_signing"] == "same org / older"                                     # event is older than the last signing
    assert pd.isna(d.loc["Zed Unknown", "latest_posting"]) or d.loc["Zed Unknown", "latest_posting"] == ""
    assert d.loc["Zed Unknown", "career_events_n"] == 0
    assert pd.isna(d.loc["Under Person", "latest_posting"]) or d.loc["Under Person", "latest_posting"] == ""    # Under Secretary -> Chief Secretary jump of >= 3 ranks is rejected
    assert read(repo / "data/signatories/signatory_directory.csv").shape[0] == 5                                # written back in place


@pytest.mark.xfail(strict=True, reason="'moved_since_signing' compares raw norm_tokens of the old ministry and new organisation, so the generic "
                                       "tokens 'ministry' and 'of' always overlap: a move from one ministry to another is reported as 'same org / older'")
def test_attach_to_flags_move_between_ministries(C, repo):
    _directory(repo, [dict(ministry="Ministry of Power", signatory="Rohit Verma Sharma", designations="Joint Secretary", n_documents=3, last_date="2023-05-01")])
    ev = _ev([dict(name="Rohit Verma Sharma", new_post="Secretary", new_org="Ministry of Finance", event_date="2024-06-01", source="sm", url="http://e1")])
    d = C.attach_to(repo / "data/signatories/signatory_directory.csv", ev)
    assert d.iloc[0].moved_since_signing == "yes"


def test_attach_to_ambiguous_names_and_er_sheets(C, repo):
    _directory(repo, [dict(ministry="Ministry of Power", signatory="Amit Kumar Singh", designations="Director", n_documents=3, last_date="2023-05-01"),
                      dict(ministry="Ministry of Power", signatory="Raj Das", designations="Director", n_documents=3, last_date="2023-05-01")])
    ev = _ev([
        dict(name="Amit Kumar Singh", cadre="UP", batch="2005", new_post="Director", new_org="X", event_date="2024-06-01", source="dopt_er_sheet", url="http://a"),
        dict(name="Amit Kumar Singh", cadre="BR", batch="2007", new_post="Director", new_org="Y", event_date="2024-07-01", source="dopt_er_sheet", url="http://b"),
        dict(name="Raj Das", cadre="", batch="", new_post="Director", new_org="X", event_date="2024-06-01", source="dopt_er_sheet", url="http://c"),
        dict(name="Raj Das", cadre="", batch="", new_post="Director", new_org="Z", event_date="2024-06-02", source="dopt_er_sheet", url="http://d"),
    ])
    d = C.attach_to(repo / "data/signatories/signatory_directory.csv", ev).set_index("signatory")
    assert d.loc["Amit Kumar Singh", "posting_match_confidence"] == "ambiguous" and d.loc["Amit Kumar Singh", "moved_since_signing"] == "ambiguous name"
    assert d.loc["Raj Das", "posting_match_confidence"] == "ambiguous"                  # two-token name with 2 ER-sheet hits


def test_attach_to_missing_or_empty_directory(C, repo):
    assert C.attach_to(repo / "data/nope.csv", _ev([dict(name="A B")])) is None
    write_csv(repo / "data/empty.csv", [], ["ministry", "signatory"])
    assert C.attach_to(repo / "data/empty.csv", _ev([dict(name="A B")])).empty


def test_attach_stage_writes_summary(C, repo):
    _directory(repo, [dict(ministry="Ministry of Power", signatory="Rohit Verma Sharma", designations="Joint Secretary | Director", n_documents=3, last_date="2023-05-01")])
    _directory(repo, [dict(ministry="Ministry of Coal", signatory="Nobody Special", designations="", n_documents=1, last_date="")], "data/states/signatory_directory_all_states.csv")
    ev = _ev([dict(name="Rohit Verma Sharma", new_post="Secretary", new_org="Pune Collectorate", event_date="2024-06-01", source="sm", url="http://e1"),
              dict(name="Undated Person", new_post="X", new_org="Y", event_date="", source="sm", url="http://e9")])
    ev.to_csv(C.CAREER / "career_events.csv", index=False)
    C.attach(argparse.Namespace())
    md = (C.CAREER / "CAREER_TRACKER.md").read_text()
    assert "| centre | 1 | 1 | 1 | 1 |" in md and "| states | 1 | 0 | 0 | 0 |" in md
    assert "Events: 1 " in md                                    # the undated, non-ER-sheet event is excluded
    assert "| centre | Rohit Verma Sharma | Joint Secretary (Ministry of Power) | 2023-05-01 | Secretary — Pune Collectorate | 2024-06-01 | [sm](http://e1) |" in md


def test_main_dispatch(C, repo, monkeypatch):
    from conftest import run_script
    run_script("career_tracker", ["events"])
