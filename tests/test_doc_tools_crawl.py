"""ministry_documents/tools: crawl_html, crawl_js, fingerprint, build_index, recrawl, run_*_all (all network/subprocess faked)."""
import csv
import json
import os
import subprocess
import sys
import types

import pytest

from conftest import run_script
from helpers import read, write_csv


def sites(repo, slug):
    return repo / "ministry_documents/data/sites" / slug


# ================================================================== crawl_html
@pytest.fixture
def CH(load, monkeypatch):
    m = load("mdtools_crawl_html")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def test_curl_parses_meta_and_insecure_flag(CH, monkeypatch):
    seen = []

    def run(cmd, capture_output):
        seen.append(cmd)
        return types.SimpleNamespace(stdout=b"<html>body</html>\n__META__200\ttext/html; charset=utf-8\thttps://x.gov.in/final")
    monkeypatch.setattr(CH.subprocess, "run", run)
    code, ctype, body, final = CH.curl("https://x.gov.in/a", insecure=True, timeout=7)
    assert (code, ctype, body, final) == (200, "text/html; charset=utf-8", b"<html>body</html>", "https://x.gov.in/final")
    assert seen[0][1] == "-k" and "--max-time" in seen[0] and "7" in seen[0]
    CH.curl("https://x.gov.in/a", insecure=False)
    assert "-k" not in seen[1]
    monkeypatch.setattr(CH.subprocess, "run", lambda cmd, capture_output: types.SimpleNamespace(stdout=b"no meta"))
    assert CH.curl("https://x/a", False) == (0, "", b"", "https://x/a")


def test_norm_strips_fragment_and_lowercases_host(CH):
    assert CH.norm("HTTPS://Example.GOV.in/a/b?x=1#frag") == "https://example.gov.in/a/b?x=1"
    assert CH.norm("https://x.in") == "https://x.in/"


def test_patterns(CH):
    assert CH.DOC.search("http://x/a.PDF") and CH.DOC.search("http://x/a.xlsx?dl=1") and not CH.DOC.search("http://x/a.pdfx")
    assert CH.SKIP.search("http://x/img.png") and CH.SKIP.search("http://x/hi/page") and CH.SKIP.search("mailto:a@b") and not CH.SKIP.search("http://x/en/page")
    assert CH.CHALLENGE.search("<title>Just a moment...</title>") and not CH.CHALLENGE.search("welcome")
    assert CH.NAV_HINT.search("/reports") and not CH.NAV_HINT.search("/zzz")


PAGES = {
    "https://m.gov.in/robots.txt": (200, "text/plain", b"User-agent: *\nDisallow: /private/\n"),
    "https://m.gov.in/": (200, "text/html", b"""<html><title> Home &amp; Co </title>
        <a href="/reports">Reports</a><a href="/misc/page">Misc</a><a href="/private/secret">Secret</a>
        <a href="/files/order.pdf">Order <b>One</b></a><a href="https://other.in/x">External</a><a href="mailto:a@b">mail</a>
        <a href="/img.png">img</a><a href="/hi/hindi">hindi</a><a href="#top">top</a></html>"""),
    "https://m.gov.in/reports": (200, "text/html", b'<html><title>Reports</title><a href="/reports/deep1">d1</a><a href="/files/two.docx">Two</a></html>'),
    "https://m.gov.in/misc/page": (200, "application/pdf", b"%PDF"),
    "https://m.gov.in/reports/deep1": (200, "text/html", b'<html><a href="/reports/deep2">d2</a><a href="/files/order.pdf">dup</a></html>'),
    "https://m.gov.in/reports/deep2": (200, "text/html", b'<html><a href="/reports/deep3">d3</a></html>'),
    "https://m.gov.in/reports/deep3": (200, "text/html", b'<html><a href="/reports/deep4">d4</a></html>'),
    "https://m.gov.in/reports/deep4": (500, "text/html", b""),
}


def fake_curl_factory(pages, log):
    def fake(url, insecure, timeout=40):
        log.append(url)
        v = pages.get(url)
        if callable(v):
            v = v()
        if v is None:
            return 404, "", b"", url
        return v[0], v[1], v[2], url
    return fake


def test_crawl_html_main_collects_docs_and_respects_robots_and_depth(CH, repo, monkeypatch, capsys):
    log = []
    monkeypatch.setattr(CH, "curl", fake_curl_factory(PAGES, log))
    monkeypatch.setattr(sys, "argv", ["x", "https://m.gov.in/", "m", "--max-pages", "50"])
    CH.main()
    out = sites(repo, "m")
    docs = {r["url"]: r for r in csv.DictReader((out / "doc_links.csv").open())}
    assert set(docs) == {"https://m.gov.in/files/order.pdf", "https://m.gov.in/files/two.docx"}
    assert " ".join(docs["https://m.gov.in/files/order.pdf"]["text"].split()) == "Order One" and docs["https://m.gov.in/files/order.pdf"]["found_on"] == "https://m.gov.in/"
    pages = list(csv.DictReader((out / "pages.csv").open()))
    assert pages[0]["title"] == "Home & Co" and pages[0]["depth"] == "0"
    crawled = [p["url"] for p in pages]
    assert "https://m.gov.in/private/secret" not in log and "https://other.in/x" not in log and "https://m.gov.in/img.png" not in log   # robots, off-site, SKIP
    assert log.index("https://m.gov.in/reports") < log.index("https://m.gov.in/misc/page")                     # document-ish sections are crawled first
    assert "https://m.gov.in/reports/deep2" in crawled and "https://m.gov.in/reports/deep3" not in log          # links on depth-3 pages are not followed
    summary = json.loads((out / "summary.json").read_text())
    assert summary["blocked"] is False and summary["doc_links"] == 2 and summary["pages"] == len(pages)
    assert "doc_links" in capsys.readouterr().out


def test_crawl_html_stops_on_bot_challenge(CH, repo, monkeypatch):
    pages = {"https://c.gov.in/robots.txt": (404, "", b""), "https://c.gov.in/": (200, "text/html", b"<title>Just a moment...</title>")}
    monkeypatch.setattr(CH, "curl", fake_curl_factory(pages, []))
    monkeypatch.setattr(sys, "argv", ["x", "https://c.gov.in/", "c"])
    CH.main()
    s = json.loads((sites(repo, "c") / "summary.json").read_text())
    assert s["blocked"] is True and s["pages"] == 0


def test_crawl_html_retry_pass_and_errors(CH, repo, monkeypatch):
    state = {"flaky": 0}

    def flaky():
        state["flaky"] += 1
        return (503, "text/html", b"") if state["flaky"] == 1 else (200, "text/html", b"<title>Flaky</title>")
    pages = {"https://r.gov.in/robots.txt": (200, "text/plain", b""), "https://r.gov.in/": (200, "text/html", b'<a href="/flaky">f</a><a href="/gone">g</a><a href="/boom">b</a>'),
             "https://r.gov.in/flaky": flaky, "https://r.gov.in/gone": (404, "text/html", b""), "https://r.gov.in/boom": (500, "text/html", b"")}
    monkeypatch.setattr(CH, "curl", fake_curl_factory(pages, []))
    monkeypatch.setattr(sys, "argv", ["x", "https://r.gov.in/", "r", "--insecure"])
    CH.main()
    s = json.loads((sites(repo, "r") / "summary.json").read_text())
    assert s["retried_ok"] == 1 and s["errors"] == 2 and s["pages"] == 2          # flaky page recovered in the retry pass; 404 and the still-failing 500 counted
    failed = list(csv.DictReader((sites(repo, "r") / "failed.csv").open()))
    assert [f["url"] for f in failed] == ["https://r.gov.in/boom"] and failed[0]["status"] == "500"


def test_crawl_html_max_pages_cap(CH, repo, monkeypatch):
    links = "".join(f'<a href="/p{i}">p</a>' for i in range(10))
    pages = {"https://z.gov.in/robots.txt": (404, "", b""), "https://z.gov.in/": (200, "text/html", links.encode())}
    pages.update({f"https://z.gov.in/p{i}": (200, "text/html", b"<title>x</title>") for i in range(10)})
    monkeypatch.setattr(CH, "curl", fake_curl_factory(pages, []))
    monkeypatch.setattr(sys, "argv", ["x", "https://z.gov.in/", "z", "--max-pages", "3"])
    CH.main()
    assert json.loads((sites(repo, "z") / "summary.json").read_text())["pages"] == 3


# ================================================================== crawl_js
def test_crawl_js(load, repo, monkeypatch):
    J = load("mdtools_crawl_js")
    monkeypatch.setattr(J.time, "sleep", lambda s: None)
    outputs = {
        "https://js.gov.in/": "Fetching https://js.gov.in/\nPage loaded\nhttps://js.gov.in/reports\tReports\nhttps://js.gov.in/a.pdf\tPDF A\nhttps://www.js.gov.in/other\tNo hint\nnot a link\n",
        "https://js.gov.in/reports": "https://js.gov.in/b.xlsx\tSheet\nhttps://js.gov.in/reports/deeper\tdeeper reports\n",
        "https://js.gov.in/reports/deeper": "https://js.gov.in/reports/deepest\tmore reports\nhttps://js.gov.in/c.zip\tZip\n",
    }
    log = []

    def run(cmd, capture_output, text, timeout):
        log.append(cmd[2])
        if cmd[2] == "https://js.gov.in/reports/deeper":
            raise subprocess.TimeoutExpired(cmd, timeout)
        return types.SimpleNamespace(stdout=outputs.get(cmd[2], ""))
    monkeypatch.setattr(J.subprocess, "run", run)
    monkeypatch.setattr(sys, "argv", ["x", "https://www.js.gov.in/", "js"])
    outputs["https://www.js.gov.in/"] = outputs["https://js.gov.in/"]
    J.main()
    s = json.loads((sites(repo, "js") / "summary.json").read_text())
    assert s["method"] == "obscura-render" and s["blocked"] is False
    docs = [r["url"] for r in csv.DictReader((sites(repo, "js") / "doc_links.csv").open())]
    assert docs == ["https://js.gov.in/a.pdf"] or "https://js.gov.in/a.pdf" in docs
    monkeypatch.setattr(J.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout="Just a moment..."))
    monkeypatch.setattr(sys, "argv", ["x", "https://js.gov.in/", "js2", "--max-pages", "5"])
    J.main()
    assert json.loads((sites(repo, "js2") / "summary.json").read_text())["blocked"] is True
    links, raw = J.render_links("https://js.gov.in/")
    assert links == [] and raw == "Just a moment..."


# ================================================================== fingerprint
@pytest.fixture
def FP(load, monkeypatch):
    m = load("mdtools_fingerprint")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def test_text_len_and_jsonish(FP):
    assert FP.text_len(b"<html><script>var x=1;</script><style>a{}</style><p>Hello   world</p></html>") == 11
    assert FP.jsonish(b'{"a": 1}') == {"a": 1} and FP.jsonish(b"nope") is None


def _route(table):
    def get(op, url, last):
        for suffix, resp in table.items():
            if url.endswith(suffix):
                return resp
        return 404, "", b"", url, {}
    return get


def test_probe_platform_detection(FP, monkeypatch):
    base = lambda text: (200, "text/html", text, "https://s.gov.in/", {})
    row = {"name": "Dept", "website": "https://s.gov.in"}
    cases = {
        "digifootprint-postpage": {"https://s.gov.in": base(b"x" * 2000), "schemes_and_services?limit=1&page=1": (200, "", b'{"posts": []}', "", {})},
        "digifootprint-wpv2": {"https://s.gov.in": base(b"x" * 2000), "/cms/wp-json/wp/v2/types": (200, "", b'{"post": {}, "page": {}, "documents": {}, "news": {}}', "", {})},
        "wordpress": {"https://s.gov.in": base(b"x" * 2000), "/wp-json/": (200, "", b'{"namespaces": ["wp/v2"]}', "", {})},
        "html": {"https://s.gov.in": base(b"<p>" + b"word " * 400 + b"</p>")},
        "js-shell": {"https://s.gov.in": base(b"<div id=root></div>")},
    }
    for expected, table in cases.items():
        monkeypatch.setattr(FP, "get", _route(table))
        out = FP.probe(dict(row))
        assert out["platform"] == expected, expected
    monkeypatch.setattr(FP, "get", _route(cases["digifootprint-wpv2"]))
    out = FP.probe(dict(row))
    assert out["api_base"] == "https://s.gov.in/cms/wp-json" and out["notes"] == "types=documents,news"
    monkeypatch.setattr(FP, "get", _route({"https://s.gov.in": base(b"<meta name=\"generator\" content=\"Drupal 9\">" + b"word " * 400)}))
    out = FP.probe(dict(row))
    assert out["generator"] == "Drupal 9" and out["platform"] == "html"
    monkeypatch.setattr(FP, "get", _route({"https://s.gov.in": base(b"<script src='/_next/static/x.js'></script>" + b"word " * 400)}))
    out = FP.probe(dict(row))
    assert out["generator"] == "Next.js" and out["platform"] == "js-shell"


def test_probe_dead_blocked_missing_and_tls(FP, monkeypatch):
    assert FP.probe({"name": "N", "website": ""})["platform"] == "no-website"
    monkeypatch.setattr(FP, "get", lambda op, url, last: (0, "", b"x", url, {}))
    assert FP.probe({"name": "Finance (MoF)", "website": ""})["website"] == "https://finmin.gov.in"
    monkeypatch.setattr(FP, "get", _route({"https://s.gov.in": (0, "", b"connection refused", "https://s.gov.in", {})}))
    out = FP.probe({"name": "N", "website": "https://s.gov.in"})
    assert out["platform"] == "dead" and "connection refused" in out["notes"]
    monkeypatch.setattr(FP, "get", _route({"https://s.gov.in": (200, "text/html", b"<title>Just a moment...</title>", "https://s.gov.in", {})}))
    assert FP.probe({"name": "N", "website": "https://s.gov.in"})["platform"] == "blocked"
    calls = []

    def tls(op, url, last):
        calls.append(url)
        return (0, "", b"CERTIFICATE_VERIFY_FAILED", url, {}) if len(calls) == 1 else (200, "text/html", b"word " * 400, url, {})
    monkeypatch.setattr(FP, "get", tls)
    out = FP.probe({"name": "N", "website": "https://s.gov.in"})
    assert out["notes"].startswith("bad-TLS-chain; ") and out["platform"] == "html" and len(calls) >= 5


def test_get_wrapper(FP, monkeypatch):
    class Op:
        def open(self, req, timeout):
            return self._open(req)

        def _open(self, req):
            if "err" in req.full_url:
                raise OSError("fail")
            if "http404" in req.full_url:
                import urllib.error
                raise urllib.error.HTTPError(req.full_url, 404, "nf", {"Content-Type": "text/html"}, None)

            class R:
                status = 200
                headers = {"Content-Type": "text/html"}

                def __enter__(self):
                    return self

                def __exit__(self, *a):
                    return False

                def read(self, n):
                    return b"data"

                def geturl(self):
                    return req.full_url
            return R()
    last = [0.0]
    assert FP.get(Op(), "https://x/ok", last)[:3] == (200, "text/html", b"data")
    assert FP.get(Op(), "https://x/err", last)[0] == 0
    assert FP.get(Op(), "https://x/http404", last)[0] == 404


def test_fingerprint_main(FP, repo, monkeypatch, capsys):
    write_csv(repo / "ministry_documents/data/targets.csv", [dict(name="A", website="https://a.gov.in"), dict(name="B", website="")])
    monkeypatch.setattr(FP, "probe", lambda r: dict(r, final_url="", status="200", platform="html" if r["website"] else "no-website", api_base="", text_chars="9", generator="", notes=""))
    FP.main()
    out = read(repo / "ministry_documents/data/fingerprint.csv", keep_default_na=False)
    assert list(out.platform) == ["html", "no-website"]
    assert "html" in capsys.readouterr().out


# ================================================================== build_index
def test_build_index_merges_sites(repo, monkeypatch, capsys):
    d = repo / "ministry_documents/data"
    write_csv(d / "fingerprint.csv", [dict(name="Ministry A", api_base="https://www.a.gov.in/cms/wp-json", final_url="", website="", platform="digifootprint-postpage"),
                                       dict(name="Ministry B", api_base="", final_url="https://b.nic.in/", website="", platform="html"),
                                       dict(name="Nowhere", api_base="", final_url="", website="", platform="dead")])
    a = d / "sites/a"
    a.mkdir(parents=True)
    write_csv(a / "files.csv", [dict(file_id="1", title="Order One", file_date="05/03/2025", post_date="2025-03-06T00:00", url="http://a/1.pdf", hindi_url="", size="10", language="en", doc_type=""),
                                dict(file_id="2", title="Order Two", file_date="", post_date="2025-04-07T00:00", url="", hindi_url="http://a/2h.pdf", size="", language="", doc_type="notice")])
    (a / "documents.jsonl").write_text(json.dumps({"title": "Group", "categories": ["circulars", "orders"], "type": "x", "files": [{"file_ids": [1]}]}) + "\n")
    (a / "summary.json").write_text(json.dumps({"pages": 5, "blocked": False, "errors": ["e1", "e2"]}))
    b = d / "sites/b"
    b.mkdir()
    write_csv(b / "doc_links.prev.csv", [dict(url="http://b/2024/05/x.pdf", text="Old", found_on="p1")])
    write_csv(b / "doc_links.csv", [dict(url="http://b/y.pdf", text="New", found_on="p2"), dict(url="http://b/2024/05/x.pdf", text="Newer", found_on="p3")])
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: None)
    run_script("mdtools_build_index")
    docs = read(d / "all_documents.csv", keep_default_na=False)
    assert len(docs) == 4
    one = docs[docs.title == "Order One"].iloc[0]
    assert (one.ministry, one.slug, one.source, one.group, one.category, one.date) == ("Ministry A", "a", "api", "Group", "circulars,orders", "2025-03-05")
    two = docs[docs.title == "Order Two"].iloc[0]
    assert two.url == "http://a/2h.pdf" and two.date == "2025-04-07" and two.category == "notice"
    crawl = docs[docs.source == "crawl"].set_index("url")
    assert set(crawl.index) == {"http://b/2024/05/x.pdf", "http://b/y.pdf"} and crawl.loc["http://b/2024/05/x.pdf", "date"] == "2024-05"
    assert crawl.loc["http://b/2024/05/x.pdf", "title"] == "Newer"                      # the latest crawl wins over doc_links.prev.csv
    cov = read(d / "coverage.csv", keep_default_na=False).set_index("slug")
    assert (int(cov.loc["a", "documents"]), int(cov.loc["a", "with_url"]), int(cov.loc["a", "errors"])) == (2, 2, 2) and cov.loc["a", "platform"] == "digifootprint-postpage"
    assert cov.loc["b", "ministry"] == "Ministry B" and int(cov.loc["b", "documents"]) == 2
    assert "4 documents from 2 sites" in capsys.readouterr().out


# ================================================================== recrawl / run_*_all
def test_recrawl_merge_prev_and_run(repo, monkeypatch, capsys):
    d = repo / "ministry_documents/data"
    write_csv(d / "fingerprint.csv", [dict(final_url="https://tls.gov.in/", website="", notes="bad-TLS-chain; "), dict(final_url="https://ok.gov.in/", website="", notes="")])
    site = d / "sites/tls"
    site.mkdir(parents=True)
    write_csv(site / "doc_links.prev.csv", [dict(url="u1", text="prev", found_on="f")])
    write_csv(site / "doc_links.csv", [dict(url="u1", text="current", found_on="f"), dict(url="u2", text="t2", found_on="f")])
    (repo / "ministry_documents/logs").mkdir()
    cmds = []
    monkeypatch.setattr(subprocess, "run", lambda cmd, stdout, stderr, text: (cmds.append(cmd), types.SimpleNamespace(stdout='{"slug": "x"}\n', returncode=0))[1])
    run_script("mdtools_recrawl", ["tls=https://tls.gov.in/:50", "ok=https://ok.gov.in", "empty=https://e.gov.in:abc"])
    prev = read(site / "doc_links.prev.csv")
    assert set(prev.url) == {"u1", "u2"} and prev.set_index("url").loc["u1", "text"] == "prev"        # earlier text wins (setdefault, prev first)
    by = {c[3].split("//")[1].split(".")[0]: c for c in cmds}
    assert "--insecure" in by["tls"] and by["tls"][-2:] == ["--max-pages", "50"][::1] or by["tls"][5:7] == ["--max-pages", "50"]
    assert "--insecure" not in by["ok"] and "300" in by["ok"]
    assert capsys.readouterr().out.count('{"slug": "x"}') == 3


def test_run_html_all_selects_html_sites(repo, monkeypatch, capsys):
    d = repo / "ministry_documents/data"
    rows = [dict(name="A", website="https://www.a.gov.in", final_url="https://www.a.gov.in/", platform="html", notes="bad-TLS-chain; "),
            dict(name="B", website="https://dbt.gov.in", final_url="", platform="dead", notes=""),
            dict(name="C", website="https://x.gov.in", final_url="https://www.mib.gov.in", platform="blocked", notes=""),
            dict(name="D", website="https://heavy.gov.in", final_url="https://heavyindustries.gov.in/hi", platform="blocked", notes=""),
            dict(name="E", website="https://e.gov.in", final_url="https://e.gov.in", platform="js-shell", notes="")]
    write_csv(d / "fingerprint.csv", rows)
    (d / "sites/dbt").mkdir(parents=True)
    (d / "sites/dbt/pages.csv").write_text("url\n")
    cmds = []
    monkeypatch.setattr(subprocess, "run", lambda cmd, stdout, stderr, text: (cmds.append(cmd), types.SimpleNamespace(stdout="", returncode=3))[1])
    run_script("mdtools_run_html_all", ["--resume"])
    starts = {c[3]: c for c in cmds}
    assert set(starts) == {"https://www.a.gov.in/", "https://www.mib.gov.in", "https://heavyindustries.gov.in/"}     # dbt (allow-listed 'dead' site) is already done; '/hi' is stripped; E is a js-shell
    assert "--insecure" in starts["https://www.a.gov.in/"] and "--insecure" not in starts["https://www.mib.gov.in"]
    out = capsys.readouterr().out
    assert "dbt: skipped (done)" in out and "exit 3" in out and "<- A" in out


def test_run_postpage_all(repo, monkeypatch, capsys):
    d = repo / "ministry_documents/data"
    write_csv(d / "fingerprint.csv", [dict(name="A", api_base="https://www.a.gov.in/cms/wp-json", platform="digifootprint-postpage"),
                                       dict(name="A2", api_base="https://www.a.gov.in/cms/wp-json", platform="digifootprint-postpage"),
                                       dict(name="B", api_base="https://b.nic.in/cms/wp-json", platform="digifootprint-postpage"),
                                       dict(name="C", api_base="", platform="html")])
    (d / "sites/b").mkdir(parents=True)
    (d / "sites/b/summary.json").write_text("{}")
    cmds = []
    monkeypatch.setattr(subprocess, "run", lambda cmd, stdout, stderr, text: (cmds.append(cmd), types.SimpleNamespace(stdout='{"slug": "a"}', returncode=0))[1])
    run_script("mdtools_run_postpage_all", ["--resume"])
    assert len(cmds) == 1 and cmds[0][3:] == ["https://www.a.gov.in/cms/wp-json", "a"]
    out = capsys.readouterr().out
    assert '{"slug": "a"}' in out and "b: skipped (done)" in out
    monkeypatch.setattr(subprocess, "run", lambda cmd, stdout, stderr, text: types.SimpleNamespace(stdout="", returncode=5))
    run_script("mdtools_run_postpage_all", [])
    assert "exit 5" in capsys.readouterr().out
