"""ministry_documents/tools site extractors (extract_postpage, extract_mospi, extract_tribal,
extract_wpv2_documents, resolve_missing_files, retry_bulk_pages).  urllib is faked everywhere: no network."""
import csv
import json
import sys
import urllib.error
import urllib.request

import pytest


# ------------------------------------------------------------------ fakes
class Resp:
    def __init__(self, payload, headers=None):
        self._b = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.headers = headers or {}

    def read(self):
        return self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def http_error(code):
    return urllib.error.HTTPError("http://x", code, "err", {}, None)


class Opener:
    """Fake of the object returned by urllib.request.build_opener."""

    def __init__(self, router, log):
        self.router, self.log = router, log

    def open(self, req, timeout=None):
        self.log.append((req.full_url, timeout))
        r = self.router(req.full_url, req)
        if isinstance(r, Exception):
            raise r
        return Resp(r)


@pytest.fixture
def sleeps(monkeypatch):
    out = []
    monkeypatch.setattr("time.sleep", lambda s: out.append(s))
    return out


def sitedir(repo, slug):
    d = repo / "ministry_documents/data/sites" / slug
    d.mkdir(parents=True, exist_ok=True)
    return d


def rows(path):
    with open(path, newline="") as f:
        return list(csv.reader(f))


def jl(path):
    return [json.loads(x) for x in open(path).read().splitlines()]


# ================================================================== extract_postpage
@pytest.fixture
def PP(load, sleeps):
    return load("mdtools_extract_postpage")


def make_client(PP, monkeypatch, router):
    log = []
    monkeypatch.setattr(PP.urllib.request, "build_opener", lambda *a: Opener(router, log))
    return PP.Client("https://api.x.in/"), log


def test_client_get_success_strips_base_slash_and_counts(PP, monkeypatch):
    cl, log = make_client(PP, monkeypatch, lambda u, r: {"ok": 1})
    assert cl.base == "https://api.x.in"
    assert cl.get("a/b") == {"ok": 1}
    assert log == [("https://api.x.in/a/b", 60)] and cl.calls == 1


def test_client_get_throttles_to_one_request_per_second(PP, monkeypatch, sleeps):
    cl, _ = make_client(PP, monkeypatch, lambda u, r: {})
    cl.get("a")
    sleeps.clear()
    cl.get("b")
    assert len(sleeps) == 1 and 0 < sleeps[0] <= 1.0           # second call right after the first must wait
    cl.last = 0.0
    sleeps.clear()
    cl.get("c")
    assert sleeps == []                                          # last call long ago: no wait


def test_client_get_retries_gateway_errors_with_growing_backoff(PP, monkeypatch, sleeps):
    seq = iter([http_error(502), http_error(503), {"ok": True}])
    cl, log = make_client(PP, monkeypatch, lambda u, r: next(seq))
    assert cl.get("p") == {"ok": True}
    assert cl.calls == 3 and [s for s in sleeps if s >= 10] == [10, 20]


def test_client_get_gives_up_after_tries_on_5xx(PP, monkeypatch, sleeps):
    cl, _ = make_client(PP, monkeypatch, lambda u, r: http_error(504))
    assert cl.get("p") == {"_error": 504}
    assert cl.calls == 3 and [s for s in sleeps if s >= 10] == [10, 20]
    cl2, _ = make_client(PP, monkeypatch, lambda u, r: http_error(502))
    assert cl2.get("p", tries=1) == {"_error": 502} and cl2.calls == 1


def test_client_get_does_not_retry_other_http_codes(PP, monkeypatch, sleeps):
    cl, _ = make_client(PP, monkeypatch, lambda u, r: http_error(404))
    assert cl.get("p") == {"_error": 404}
    assert cl.calls == 1 and not [s for s in sleeps if s >= 10]
    cl, _ = make_client(PP, monkeypatch, lambda u, r: http_error(500))
    assert cl.get("p") == {"_error": 500} and cl.calls == 1      # 500 is not in the retry set


def test_client_get_generic_error_retried_and_truncated(PP, monkeypatch, sleeps):
    seq = iter([OSError("boom"), {"ok": 2}])
    cl, _ = make_client(PP, monkeypatch, lambda u, r: next(seq))
    assert cl.get("p") == {"ok": 2} and cl.calls == 2
    cl, _ = make_client(PP, monkeypatch, lambda u, r: ValueError("x" * 500))
    out = cl.get("p")
    assert out == {"_error": "x" * 120} and cl.calls == 3


class FakeCl:
    def __init__(self, responses):
        self.responses, self.paths = list(responses), []

    def get(self, path):
        self.paths.append(path)
        return self.responses.pop(0)


def test_pages_walks_all_pages_and_builds_query(PP):
    cl = FakeCl([{"posts": [{"ID": 1}, {"ID": 2}], "total_pages": 2}, {"posts": [{"ID": 3}], "total_pages": 2}])
    assert [p["ID"] for p in PP.pages(cl, "post-page/x", 400)] == [1, 2, 3]
    assert cl.paths == ["post-page/x?limit=100&page=1", "post-page/x?limit=100&page=2"]
    cl = FakeCl([{"posts": [], "total_pages": 1}])
    assert list(PP.pages(cl, "document/documents?c=1", 400)) == []
    assert cl.paths == ["document/documents?c=1&limit=100&page=1"]


def test_pages_respects_max_pages_and_wraps_dict_posts(PP):
    cl = FakeCl([{"posts": {"ID": 9}, "total_pages": 5}])
    assert list(PP.pages(cl, "p", 1)) == [{"ID": 9}] and len(cl.paths) == 1
    cl = FakeCl([{"posts": None, "total_pages": "3"}, {"total_pages": 3}])
    assert list(PP.pages(cl, "p", 2)) == [] and len(cl.paths) == 2   # null posts tolerated, string page count coerced


def test_pages_error_handling(PP):
    # error on the first page: reported once, then stop
    cl = FakeCl([{"_error": 500}])
    assert list(PP.pages(cl, "p", 400)) == [{"_error": 500, "_page": 1}] and len(cl.paths) == 1
    # non-dict reply is a "bad" error
    cl = FakeCl(["junk"])
    assert list(PP.pages(cl, "p", 400)) == [{"_error": "bad", "_page": 1}]
    # once the page count is known a bad page is skipped and the walk continues
    cl = FakeCl([{"posts": [{"ID": 1}], "total_pages": 3}, {"_error": 500}, {"posts": [{"ID": 3}], "total_pages": 3}])
    got = list(PP.pages(cl, "p", 400))
    assert got == [{"ID": 1}, {"_error": 500, "_page": 2}, {"ID": 3}]


def post(i, **acf):
    return {"ID": i, "post_title": f"T{i}", "post_date": "2026-01-0%d" % i, "acf_data": acf}


SITE_ROUTES = {}


def build_site_router(slug_docs=True):
    central = {"posts": [
        post(1, title="  Policy One ", file_date="2026-02-01", language=["en", "hi"], pdf_type="Policy",
             pdf={"url": "https://x/1.pdf", "filesize": 10, "mime_type": "application/pdf"},
             pdf_hi={"url": "https://x/1h.pdf"}),
        post(2, language="en", other="nodict"),
        {"ID": 3, "post_title": "NoAcf"},
    ], "total_pages": 1}
    tax = {"documents_category": [
        {"slug": "child", "parent": 7, "count": 5},
        {"slug": "big root", "parent": 0, "count": 9},
        {"slug": "small-root", "parent": 0, "count": 2},
        {"slug": "empty", "parent": 0, "count": 0},
    ]}
    docs = {
        "big%20root": {"posts": [
            {"ID": 10, "post_title": "Doc10", "post_date": "d", "post_modified": "m", "post_name": "doc-10",
             "documents_category": [{"slug": "big-root"}, {"slug": "z"}],
             "acf_data": {"title": " Ten ", "date": "2026-03-03", "file": [
                 {"type": "file", "title": "A", "external_link": "", "file": [1, 2]},
                 {"type": "file", "title": "B", "external_link": "", "file": 5},
                 {"type": "link", "title": "C", "external_link": "https://e", "file": "oops"},
                 "notadict"]}},
            {"ID": 11, "post_title": "Doc11", "acf_data": {}},
        ], "total_pages": 1},
        "small-root": {"posts": [{"ID": 10, "post_title": "dup"}, {"ID": 12, "post_title": "Doc12"}], "total_pages": 1},
        "child": {"_error": 500},
    }
    types = {"schemes_and_services": {"posts": [{"ID": 20, "post_title": "S", "post_date": "d", "post_modified": "m",
                                                  "post_name": "s", "acf_data": {"a": 1}, "post_content": "<p>x</p>"}], "total_pages": 1}}

    def router(url, req):
        path = url.split("https://api.x.in/", 1)[1]
        if path.startswith("post-page/central_documents"):
            return central
        if path.startswith("taxonomy/documents_category"):
            return tax
        if path.startswith("document/documents?document_category="):
            slug = path.split("document_category=")[1].split("&")[0]
            return docs[slug]
        if path.startswith("post-page/"):
            t = path.split("post-page/")[1].split("?")[0]
            return types.get(t) or http_error(404)
        raise AssertionError(path)
    return router


def test_main_end_to_end(PP, repo, monkeypatch, capsys):
    cl_log = []
    monkeypatch.setattr(PP.urllib.request, "build_opener", lambda *a: Opener(build_site_router(), cl_log))
    monkeypatch.setattr(sys, "argv", ["x", "https://api.x.in", "demo"])
    PP.main()
    out = repo / "ministry_documents/data/sites/demo"
    fr = rows(out / "files.csv")
    assert fr[0] == ["file_id", "title", "file_date", "post_date", "language", "pdf_type", "url", "size", "mime", "hindi_url"]
    assert fr[1] == ["1", "Policy One", "2026-02-01", "2026-01-01", "en,hi", "Policy", "https://x/1.pdf", "10", "application/pdf", "https://x/1h.pdf"]
    assert fr[2] == ["2", "T2", "", "2026-01-02", "en", "", "", "", "", ""]      # string language kept; title falls back
    assert fr[3][:2] == ["3", "NoAcf"] and len(fr) == 4
    assert not (out / "files.csv.tmp").exists()
    assert json.load(open(out / "categories.json"))[0]["slug"] == "child"
    docs = jl(out / "documents.jsonl")
    assert [d["id"] for d in docs] == [10, 11, 12]                               # dup 10 skipped, empty category never queried
    d10 = docs[0]
    assert d10["title"] == "Ten" and d10["categories"] == ["big-root", "z"] and d10["slug"] == "doc-10"
    assert d10["files"] == [{"type": "file", "title": "A", "external_link": "", "file_ids": [1, 2]},
                            {"type": "file", "title": "B", "external_link": "", "file_ids": [5]},
                            {"type": "link", "title": "C", "external_link": "https://e", "file_ids": []}]
    assert docs[1]["title"] == "Doc11" and docs[1]["files"] == []
    cats = [u.split("document_category=")[1].split("&")[0] for u, _ in cl_log if "document_category=" in u]
    assert cats == ["big%20root", "small-root", "child"]                         # roots first, biggest first, parents last
    assert "empty" not in cats
    content = sorted(p.name for p in (out / "content").iterdir())
    assert content == ["schemes_and_services.jsonl"]                             # 404 types leave no empty files behind
    assert jl(out / "content/schemes_and_services.jsonl")[0] == {"id": 20, "title": "S", "date": "d", "modified": "m", "slug": "s",
                                                                  "acf": {"a": 1}, "content": "<p>x</p>"}
    s = json.load(open(out / "summary.json"))
    assert s["files"] == 3 and s["documents"] == 3 and s["types"] == {"schemes_and_services": 1}
    assert s["errors"] == [{"documents": "child", "_error": 500, "_page": 1}]
    assert s["api_base"] == "https://api.x.in" or s["api_base"] == "https://api.x.in"
    assert s["calls"] == len(cl_log)
    printed = json.loads(capsys.readouterr().out)
    assert printed == {"slug": "demo", "files": 3, "documents": 3, "types": {"schemes_and_services": 1}, "calls": len(cl_log)}


def test_main_max_pages_flag_and_error_recording(PP, repo, monkeypatch):
    seen = []

    def router(url, req):
        seen.append(url)
        if "central_documents" in url:
            return http_error(404)
        if "taxonomy" in url:
            return http_error(404)
        return http_error(404)
    monkeypatch.setattr(PP.urllib.request, "build_opener", lambda *a: Opener(router, []))
    monkeypatch.setattr(sys, "argv", ["x", "https://api.x.in", "bare", "--max-pages", "1"])
    PP.main()
    out = repo / "ministry_documents/data/sites/bare"
    s = json.load(open(out / "summary.json"))
    assert s["files"] == 0 and s["documents"] == 0 and s["types"] == {}
    assert s["errors"] == [{"central_documents": {"_error": 404, "_page": 1}}]
    assert json.load(open(out / "categories.json")) == []
    assert rows(out / "files.csv") == [["file_id", "title", "file_date", "post_date", "language", "pdf_type", "url", "size", "mime", "hindi_url"]]
    assert list((out / "content").iterdir()) == []


def test_main_max_pages_limits_walk(PP, repo, monkeypatch):
    calls = []

    def router(url, req):
        calls.append(url)
        if "central_documents" in url:
            return {"posts": [post(len(calls))], "total_pages": 9}
        return http_error(404)
    monkeypatch.setattr(PP.urllib.request, "build_opener", lambda *a: Opener(router, []))
    monkeypatch.setattr(sys, "argv", ["x", "https://api.x.in", "cap", "--max-pages", "2"])
    PP.main()
    assert len([c for c in calls if "central_documents" in c]) == 2


# ================================================================== extract_mospi
def run_mospi(load, monkeypatch, router, sleeps):
    calls = []

    def urlopen(req, timeout=None):
        body = json.loads(req.data)
        ep = req.full_url.split("/api/", 1)[1]
        calls.append((ep, body, req.get_method(), timeout))
        r = router(ep, body)
        if isinstance(r, Exception):
            raise r
        return Resp(r)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    m = load("mdtools_extract_mospi")
    return m, calls


def test_mospi_end_to_end(load, repo, monkeypatch, sleeps, capsys):
    pub = "publications-reports/get-web-publications-report-list"

    def router(ep, body):
        if ep == pub and body.get("data_source") == "archive":
            return {"status": "success", "data": [{"id": 1, "title": "Dup <b>Pub</b>"}, {"id": 2, "title": "Arch"}],
                    "pagination": {"totalPages": 1}}
        if ep == pub:
            if body["page_no"] == 1:
                return {"status": "success", "pagination": {"totalPages": 2}, "data": [
                    {"id": 1, "title": "Pub  <i>One</i>\n x", "published_year": "2025",
                     "file_one": {"path": "/docs/a.pdf", "filesize": 11, "filemime": "application/pdf"},
                     "file_two": {"path": "docs/b.pdf"}, "file_three": {"nopath": 1}, "file": "notdict"}]}
            return {"status": "success", "pagination": {"totalPages": 2}, "data": [
                {"id": 3, "name": "Named", "release_date": "2024-01-01", "file_url": "https://ext/x.pdf"}]}
        if ep.startswith("latest-release"):
            return {"status": "fail", "message": "denied"}
        if ep.startswith("announcement"):
            return OSError("socket down " + "z" * 300)
        if ep.startswith("public-doc"):
            return {"status": "success", "data": None}
        if ep.startswith("tender"):
            return {"status": "success", "data": [{"id": 1, "title": "Tender", "created_at": "c", "document": {"path": "t.pdf"}}]}
        return {"status": "success", "data": [], "pagination": {}}
    m, calls = run_mospi(load, monkeypatch, router, sleeps)
    out = repo / "ministry_documents/data/sites/mospi"
    s = json.load(open(out / "summary.json"))
    assert s["endpoints"][pub] == 2                                              # pages 1+2: ids 1 and 3
    assert s["endpoints"][pub + " [archive]"] == 2
    assert s["endpoints"]["tender/get-web-tender-list"] == 1
    assert s["endpoints"]["public-doc/get-web-pub-doc-list"] == 0
    assert s["errors"][0]["page"] == 1
    assert s["errors"][0]["latest-release/get-web-latest-release-list"] == "denied"
    ann = [e for e in s["errors"] if "announcement/get-web-announcement-list" in e][0]
    assert ann["announcement/get-web-announcement-list"] == "socket down " + "z" * 88      # truncated to 100 chars
    assert len(s["errors"]) == 2
    assert all(c[2] == "POST" and c[3] == 60 and c[1]["page_size"] == 100 and c[1]["lang"] == "en" for c in calls)
    assert [c[1].get("data_source") for c in calls if c[0] == pub] == [None, None, "archive"]
    assert not any(c[1].get("data_source") for c in calls if not c[0].startswith("publications"))
    docs = jl(out / "documents.jsonl")
    assert [(d["id"], d["_endpoint"]) for d in docs] == [(1, pub), (3, pub), (2, pub + " [archive]"), (1, "tender/get-web-tender-list")]
    assert s["documents"] == 4
    fr = rows(out / "files.csv")
    assert fr[0][-1] == "doc_type" and len(fr[0]) == 11
    by = {r[0]: r for r in fr[1:]}
    assert by["1:file_one"][1:] == ["Pub One x", "2025", "", "", "", "https://www.mospi.gov.in/docs/a.pdf", "11", "application/pdf", "", pub]
    assert by["1:file_two"][6] == "https://www.mospi.gov.in/docs/b.pdf" and by["1:file_two"][7] == ""
    assert "1:file_three" not in by and "1:file" not in by
    assert by["3:file_url"][1:4] == ["", "2024-01-01", ""]
    assert by["3:file_url"][6] == "https://ext/x.pdf"
    assert by["1:document"][2] == "c"
    assert s["files"] == len(fr) - 1 == 4
    assert not (out / "files.csv.tmp").exists()
    assert json.loads(capsys.readouterr().out)["slug"] == "mospi"
    assert sleeps.count(1) == len(calls)                                           # one request per second, every call


def test_mospi_clean_helper(load, repo, monkeypatch, sleeps):
    m, _ = run_mospi(load, monkeypatch, lambda ep, b: {"status": "success", "data": []}, sleeps)
    assert m.clean("  a <b>b</b>\n\n c  ") == "a b c"
    assert m.clean(None) == "" and m.clean("") == ""
    assert len(m.ENDPOINTS) == 10


# ================================================================== extract_tribal
def run_tribal(load, monkeypatch, router, sleeps):
    calls = []

    def urlopen(req, timeout=None):
        calls.append((req.full_url, timeout, req.get_header("Accept")))
        return Resp(router(req.full_url))
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    return load("mdtools_extract_tribal"), calls


def test_tribal_end_to_end(load, repo, monkeypatch, sleeps, capsys):
    def router(url):
        if url.endswith("page=1"):
            return {"totalPages": 2, "items": [
                {"id": 1, "title": {"en": "One"}, "documentDate": "2026-01-01", "publishedAt": "p", "language": "en",
                 "file": {"url": "/files/one.pdf", "sizeKb": 2.5, "mimeType": "application/pdf"}, "type": "Order",
                 "division": "Div", "financialYear": "2025-26"},
                {"id": 2, "title": {}, "file": {"url": "https://cdn/two.pdf", "sizeKb": 0}},
                {"id": 3, "file": None, "externalUrl": "https://ext/3"}]}
        return {"totalPages": 2, "items": [{"id": 4, "title": None, "file": {}}]}
    m, calls = run_tribal(load, monkeypatch, router, sleeps)
    assert [c[0] for c in calls] == ["https://tribal.gov.in/api/v1/documents?pageSize=100&page=1",
                                     "https://tribal.gov.in/api/v1/documents?pageSize=100&page=2"]
    assert all(c[1] == 60 and c[2] == "application/json" for c in calls) and sleeps == [1, 1]
    out = repo / "ministry_documents/data/sites/tribal"
    fr = rows(out / "files.csv")
    assert len(fr[0]) == 13 and fr[0][-1] == "financial_year"
    assert fr[1] == ["1", "One", "2026-01-01", "p", "en", "", "https://tribal.gov.in/files/one.pdf", "2560", "application/pdf", "",
                     "Order", "Div", "2025-26"]
    assert fr[2][6] == "https://cdn/two.pdf" and fr[2][7] == "" and fr[2][1] == ""     # absolute kept; 0 kB -> blank size
    assert fr[3][6] == "https://ext/3"                                                  # externalUrl fallback
    assert fr[4][:2] == ["4", ""] and fr[4][6] == "" and fr[4][4] == ""
    assert [d["id"] for d in jl(out / "documents.jsonl")] == [1, 2, 3, 4]
    assert json.load(open(out / "summary.json")) == {"api_base": "https://tribal.gov.in/api/v1", "slug": "tribal", "files": 4, "documents": 4}
    assert capsys.readouterr().out.strip() == "4 documents"


# ================================================================== extract_wpv2_documents
def run_wpv2(load, monkeypatch, router, sleeps, argv):
    calls = []

    def urlopen(req, timeout=None):
        calls.append(req.full_url)
        body, headers = router(req.full_url)
        return Resp(body, headers)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(sys, "argv", ["x", *argv])
    return load("mdtools_extract_wpv2_documents"), calls


def test_wpv2_end_to_end(load, repo, monkeypatch, sleeps, capsys):
    media_ids = list(range(100, 151))                        # 51 media ids -> batches of 50 + 1

    def router(url):
        if "wp/v2/documents" in url and "&page=1&" in url:
            docs = [{"id": 1, "date": "2026-01-01", "modified": "m1", "slug": "s1", "title": {"rendered": " Title1 "},
                     "acf": {"title": "", "date": "ad", "select_documents_type": "Policy",
                             "file": [{"pdf": i, "title": f" F{i} ", "language": ["en", "hi"], "file_date": "fd"} for i in media_ids[:50]]
                             + [{"pdf": "notint", "title": "skipme"}, "junk"]}},
                    {"id": 2, "date": "d2", "title": {"rendered": "T2"}, "acf": {"file": [{"pdf": 150}]}},
                    {"id": 3, "date": "d3", "title": {}, "acf": None}]
            return docs, {"X-WP-TotalPages": "2"}
        if "wp/v2/documents" in url:
            return [{"id": 4, "date": "d4", "title": {"rendered": "T4"}, "acf": {"file": [{"pdf": 9999}]}}], {"X-WP-TotalPages": "2"}
        if "wp/v2/media" in url:
            inc = [int(x) for x in url.split("include=")[1].split("&")[0].split(",")]
            return [{"id": i, "source_url": f"https://x/{i}.pdf", "mime_type": "application/pdf", "media_details": {"filesize": i * 2}}
                    for i in inc if i != 120], {}
        raise AssertionError(url)
    m, calls = run_wpv2(load, monkeypatch, router, sleeps, ["https://rural.gov.in/wp-json/", "rural"])
    assert calls[0] == "https://rural.gov.in/wp-json/wp/v2/documents?per_page=100&page=1&_fields=id,date,modified,slug,title,acf"
    assert "&page=2&" in calls[1]
    media_calls = [c for c in calls if "wp/v2/media" in c]
    assert len(media_calls) == 2                                               # 52 integer media ids -> batches of 50 + 2
    out = repo / "ministry_documents/data/sites/rural"
    s = json.load(open(out / "summary.json"))
    assert s["documents"] == 4 and s["files"] == 52 and s["resolved"] == 51 and s["method"] == "wp/v2/documents + wp/v2/media"
    assert s["api_base"] == "https://rural.gov.in/wp-json" and s["slug"] == "rural" and s["errors"] == []
    fr = rows(out / "files.csv")
    assert fr[0] == ["file_id", "title", "file_date", "post_date", "language", "pdf_type", "url", "size", "mime", "hindi_url"]
    assert fr[1] == ["100", "F100", "fd", "2026-01-01", "en,hi", "", "https://x/100.pdf", "200", "application/pdf", ""]
    r120 = [r for r in fr if r[0] == "120"][0]
    assert r120[6] == "" and r120[7] == "" and r120[8] == ""                   # media id missing from API reply
    r150 = [r for r in fr if r[0] == "150"][0]
    assert r150[1] == "" and r150[2] == "" and r150[3] == "d2" and r150[4] == ""
    assert [r[6] for r in fr if r[0] == "notint"] == [""] and len(fr) == 1 + 51 + 1 + 1   # non-int media id still gets a (url-less) row
    docs = jl(out / "documents.jsonl")
    assert [d["id"] for d in docs] == [1, 2, 3, 4]
    assert docs[0]["title"] == "Title1" and docs[0]["date"] == "ad" and docs[0]["categories"] == ["Policy"]
    assert docs[0]["files"][0] == {"type": "PDF", "title": " F100 ", "external_link": "", "file_ids": [100]}
    assert len(docs[0]["files"]) == 51                                          # junk string skipped, non-int pdf kept as file entry
    assert docs[2]["title"] == "" and docs[2]["files"] == [] and docs[2]["categories"] == [""]
    assert docs[3]["slug"] is None and docs[3]["post_date"] == "d4"
    assert not (out / "files.csv.tmp").exists()
    assert json.loads(capsys.readouterr().out) == {"slug": "rural", "documents": 4, "files": 52, "resolved": 51}


def test_wpv2_single_page_no_header(load, repo, monkeypatch, sleeps):
    def router(url):
        if "wp/v2/documents" in url:
            return [{"id": 1, "date": "d", "title": {"rendered": "A"}, "acf": {"file": []}}], {}
        raise AssertionError("no media call expected: " + url)
    m, calls = run_wpv2(load, monkeypatch, router, sleeps, ["https://s.in/api", "solo"])
    assert len(calls) == 1
    out = repo / "ministry_documents/data/sites/solo"
    s = json.load(open(out / "summary.json"))
    assert (s["documents"], s["files"], s["resolved"]) == (1, 0, 0)
    assert len(rows(out / "files.csv")) == 1


# ================================================================== resolve_missing_files
def make_site(repo, slug, base, have, doc_files):
    d = sitedir(repo, slug)
    json.dump({"api_base": base}, open(d / "summary.json", "w"))
    with open(d / "files.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file_id", "title", "file_date", "post_date", "language", "pdf_type", "url", "size", "mime", "hindi_url"])
        for h in have:
            w.writerow([h, "t", "", "", "", "", "u", "", "", ""])
    with open(d / "documents.jsonl", "w") as f:
        for files in doc_files:
            f.write(json.dumps({"id": 1, "files": files}) + "\n")
    return d


def load_resolver(load, monkeypatch, router, argv):
    calls = []

    def urlopen(req, timeout=None):
        calls.append((req.full_url, timeout))
        r = router(req.full_url)
        if isinstance(r, Exception):
            raise r
        return Resp(r)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(sys, "argv", ["x", *argv])
    return load("mdtools_resolve_missing_files"), calls


def test_resolve_missing_files_end_to_end(load, repo, monkeypatch, sleeps, capsys):
    d1 = make_site(repo, "a", "https://a.in/api", ["1"], [
        [{"file_ids": [1, 2, 3]}, {"file_ids": [3, 4]}, {"file_ids": None}, {}], [{"file_ids": [5, 2]}]])
    d2 = make_site(repo, "b", "https://b.in/api", [], [[{"file_ids": [9]}]])

    def router(url):
        fid = url.rsplit("id=", 1)[1]
        if fid == "3":
            return OSError("nope")                                     # skipped, not counted as added
        if fid == "4":
            return {"posts": None}                                      # no posts: blank row still written
        if fid == "5":
            return {"posts": {"post_title": " Five ", "post_date": "pd", "acf_data": {"file": {"url": "https://f/5.pdf", "filesize": 7, "mime_type": "m"}, "language": ["en", "hi"], "file_date": "fd", "pdf_type": "T"}}}
        if fid == "9":
            return {"posts": {"acf_data": {"pdf": {"url": "https://f/9.pdf"}, "language": "en"}, "post_title": "Nine"}}
        return {"posts": {"acf_data": {"title": "Title %s" % fid, "pdf": "notdict"}}}
    m, calls = load_resolver(load, monkeypatch, router, ["a", "b"])
    assert [c[0] for c in calls if c[0].startswith("https://a.in")] == [f"https://a.in/api/post-page/post?id={i}" for i in ("2", "3", "4", "5")]
    assert all(c[1] == 60 for c in calls)
    out = capsys.readouterr().out.splitlines()
    assert out == ["a: 4 missing ids, 3 resolved", "b: 1 missing ids, 1 resolved"]
    fr = rows(d1 / "files.csv")
    assert [r[0] for r in fr[1:]] == ["1", "2", "4", "5"]
    assert fr[2] == ["2", "Title 2", "", "", "", "", "", "", "", ""]
    assert fr[3] == ["4", "", "", "", "", "", "", "", "", ""]
    assert fr[4] == ["5", "Five", "fd", "pd", "en,hi", "T", "https://f/5.pdf", "7", "m", ""]
    fb = rows(d2 / "files.csv")
    assert fb[1] == ["9", "Nine", "", "", "en", "", "https://f/9.pdf", "", "", ""]
    assert sleeps.count(1) == len(calls)


def test_resolve_missing_files_cap(load, repo, monkeypatch, sleeps, capsys):
    ids = list(range(1, 11))
    make_site(repo, "c", "https://c.in", ["1"], [[{"file_ids": ids + ids}]])
    seen = []
    m, calls = load_resolver(load, monkeypatch, lambda u: seen.append(u) or {"posts": {}}, ["c"])
    assert m.CAP == 3000
    capsys.readouterr()
    # CAP applies after de-duplication and ordering is preserved
    make_site(repo, "d", "https://d.in", [], [[{"file_ids": [7, 8, 7, 9, 10]}]])
    m.CAP = 3
    calls.clear()
    assert m.resolve("d") == "d: 3 missing ids, 3 resolved"
    assert [c[0].rsplit("=", 1)[1] for c in calls] == ["7", "8", "9"]


# ================================================================== retry_bulk_pages
def load_retry(load, monkeypatch, router, sleeps, argv=()):
    calls = []

    class Op:
        def open(self, req, timeout=None):
            calls.append((req.full_url, timeout))
            r = router(req.full_url)
            if isinstance(r, Exception):
                raise r
            return Resp(r)
    monkeypatch.setattr(urllib.request, "build_opener", lambda *a: Op())
    monkeypatch.setattr(sys, "argv", ["x", *argv])
    sys.modules.pop("mdtools_retry_bulk_pages", None)
    return load("mdtools_retry_bulk_pages"), calls


def test_retry_get_status_handling(load, monkeypatch, sleeps):
    seq = iter([http_error(500), http_error(503), {"ok": 1}])
    m, calls = load_retry(load, monkeypatch, lambda u: next(seq), sleeps)
    assert m.get("http://x/a") == {"ok": 1}
    assert len(calls) == 3 and [s for s in sleeps if s >= 5] == [5, 10] and calls[0][1] == 45
    sleeps.clear()
    m2, calls2 = load_retry(load, monkeypatch, lambda u: http_error(404), sleeps)
    assert m2.get("http://x/a") is None and len(calls2) == 1 and not [s for s in sleeps if s >= 5]
    m3, calls3 = load_retry(load, monkeypatch, lambda u: http_error(502), sleeps)
    assert m3.get("http://x/a") is None and len(calls3) == 3
    assert m3.get("http://x/a", tries=1) is None and len(calls3) == 4
    seq = iter([OSError("x"), {"ok": 2}])
    m4, calls4 = load_retry(load, monkeypatch, lambda u: next(seq), sleeps)
    assert m4.get("http://x/u") == {"ok": 2} and len(calls4) == 2
    m5, calls5 = load_retry(load, monkeypatch, lambda u: OSError("x"), sleeps)
    assert m5.get("http://x/u") is None and len(calls5) == 3


def test_retry_row_shapes(load, monkeypatch, sleeps):
    m, _ = load_retry(load, monkeypatch, lambda u: {}, sleeps)
    p = {"ID": 5, "post_title": "PT", "post_date": "pd", "acf_data": {
        "title": " Ti ", "file_date": "fd", "language": ["en", "hi"], "pdf_type": "X",
        "a": {"url": "https://a", "filesize": 3, "mime_type": "m"}, "b": {"url": "https://b"}, "c": {"nourl": 1}, "d": "str"}}
    assert m.row(p) == [5, "Ti", "fd", "pd", "en,hi", "X", "https://a", 3, "m", "https://b"]
    assert m.row({"ID": 6, "post_title": " Only "}) == [6, "Only", "", "", "", "", "", "", "", ""]
    assert m.row({"ID": 7, "acf_data": {"language": "en"}})[4] == "en"


def test_retry_end_to_end(load, repo, monkeypatch, sleeps, capsys):
    d = sitedir(repo, "mnre")
    base = "https://mnre.in/cms"
    json.dump({"api_base": base, "files": 1, "errors": [
        {"central_documents": {"_error": 500, "_page": 2}}, {"central_documents": {"_error": 500, "_page": 2}},
        {"documents": "x", "_error": 1}]}, open(d / "summary.json", "w"))
    with open(d / "files.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file_id"])
        w.writerow(["14"])

    def router(url):
        q = url.split(base + "/post-page/central_documents?")[1]
        if q == "limit=10&page=13":
            return http_error(404)                                  # whole 10-record page fails
        if q.startswith("limit=1&page="):
            k = int(q.split("page=")[1])
            if k == 125:
                return http_error(404)
            return {"posts": [{"ID": 1000 + k, "post_title": f"R{k}"}]}
        n = int(q.split("page=")[1])
        if n == 14:
            return {"posts": [{"ID": 14, "post_title": "have"}]}          # already known: not appended
        if n == 15:
            return {"posts": None}
        return {"posts": [{"ID": n, "post_title": f"P{n}"}]}
    m, calls = load_retry(load, monkeypatch, router, sleeps, ["mnre"])
    assert capsys.readouterr().out.strip() == "mnre: 1 failed pages -> recovered 16 records; 1 single records still failing"
    qs = [c[0].split("?")[1] for c in calls]
    assert qs[:3] == ["limit=10&page=11", "limit=10&page=12", "limit=10&page=13"]
    assert "limit=10&page=20" in qs and "limit=10&page=21" not in qs and "limit=10&page=10" not in qs
    singles = [q for q in qs if q.startswith("limit=1&")]
    assert singles[0] == "limit=1&page=121" and singles[-1] == "limit=1&page=130" and len(singles) == 10
    fr = rows(d / "files.csv")
    ids = [r[0] for r in fr[1:]]
    assert ids[0] == "14" and "14" not in ids[1:]
    assert len(ids) == 1 + 16 and "1125" not in ids and "1121" in ids and "1130" in ids
    assert "13" not in ids and "11" in ids and "20" in ids
    s = json.load(open(d / "summary.json"))
    assert s["errors"] == [{"documents": "x", "_error": 1}, {"central_documents_unrecoverable_records(limit=1 pages)": [125]}]
    assert s["files"] == 1 + 16 and "T" in s["retried"]


def test_retry_all_recovered_clears_errors(load, repo, monkeypatch, sleeps, capsys):
    d = sitedir(repo, "ok")
    json.dump({"api_base": "https://o.in", "errors": [{"central_documents": {"_page": 1}}]}, open(d / "summary.json", "w"))
    (d / "files.csv").write_text("file_id\n")
    m, calls = load_retry(load, monkeypatch, lambda u: {"posts": [{"ID": u.rsplit("=", 1)[1]}]}, sleeps, ["ok"])
    assert capsys.readouterr().out.strip() == "ok: 1 failed pages -> recovered 10 records; 0 single records still failing"
    s = json.load(open(d / "summary.json"))
    assert s["errors"] == [] and s["files"] == 10
    assert len(calls) == 10


def test_retry_no_failed_pages(load, repo, monkeypatch, sleeps, capsys):
    d = sitedir(repo, "none")
    json.dump({"api_base": "https://o.in", "files": 5}, open(d / "summary.json", "w"))
    (d / "files.csv").write_text("file_id\n1\n2\n")
    m, calls = load_retry(load, monkeypatch, lambda u: pytest.fail("no request expected"), sleeps, ["none"])
    assert capsys.readouterr().out.strip() == "none: 0 failed pages -> recovered 0 records; 0 single records still failing"
    assert json.load(open(d / "summary.json"))["files"] == 2
    assert calls == []


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="extract_wpv2_documents.py:49 joins f.get('language') directly; a string language 'en' becomes 'e,n'")
def test_wpv2_string_language_not_split_into_characters(load, repo, monkeypatch, sleeps):
    def router(url):
        if "wp/v2/documents" in url:
            return [{"id": 1, "date": "d", "title": {"rendered": "A"}, "acf": {"file": [{"pdf": 5, "language": "en"}]}}], {}
        return [{"id": 5, "source_url": "u", "mime_type": "m", "media_details": {}}], {}
    run_wpv2(load, monkeypatch, router, sleeps, ["https://s.in/api", "lang"])
    assert rows(repo / "ministry_documents/data/sites/lang/files.csv")[1][4] == "en"
