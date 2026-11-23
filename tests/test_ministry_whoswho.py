import csv
import json
import sys
import types

import pytest
import requests


@pytest.fixture
def W(load):
    return load("ministry_whoswho")


class Resp:
    def __init__(self, text="", status=200, url="https://x.gov.in/p", headers=None, content=b""):
        self.text, self.status_code, self.url = text, status, url
        self.headers = headers or {}
        self.content = content or text.encode()


TABLE = """
<table>
 <caption>Policy Division</caption>
 <thead><tr><th>S.No</th><th>Name of Officer</th><th>Designation</th><th>Room No</th><th>Telephone</th><th>E-mail</th></tr></thead>
 <tbody>
  <tr><td>1</td><td> Shri  A. K.  Singh </td><td>Joint Secretary</td><td>101</td><td>011-2301</td><td>aksingh[at]gov[dot]in</td></tr>
  <tr><td>2</td><td>Vacant</td><td>Director</td><td></td><td></td><td></td></tr>
  <tr><td>3</td><td>Ms Bina Rao</td><td>Director</td><td>102</td><td>011-2302</td><td></td></tr>
  <tr><td>4</td><td>Xy</td><td>Director</td><td></td><td></td><td></td></tr>
  <tr><td colspan="6"></td></tr>
 </tbody>
</table>"""


# ------------------------------------------------------------------ small helpers
def test_deob_variants(W):
    assert W.deob("a [at] b [dot] gov[in]") == "a@b.gov.in"
    assert W.deob("a[at]b[dot]com") == "a@b.com"
    assert W.deob("  x@y.in.;  ") == "x@y.in"
    assert W.deob(None) == "" and W.deob("") == ""
    assert W.deob("a[ AT ]b[ DOT ]in") == "a@b.in"
    assert W.deob("[x]") == "x"


def test_clean(W):
    assert W.clean("  a \n\t b  ") == "a b"
    assert W.clean(None) == ""


def test_skip_name_regex(W):
    for s in ("S.No", "s no.", "sr.", "#", "12", "12.", "Vacant", "---", "-", ""):
        assert W.SKIP_NAME.match(s), s
    for s in ("Amit", "Sr. Officer", "No 1 Singh"):
        assert not W.SKIP_NAME.match(s), s


# ------------------------------------------------------------------ parse_tables
def test_parse_tables_full_row(W):
    rows = W.parse_tables(TABLE, "http://page")
    assert [r["name"] for r in rows] == ["Shri A. K. Singh", "Ms Bina Rao"]      # Vacant, 'Xy' and empty rows dropped
    r = rows[0]
    assert r["designation"] == "Joint Secretary" and r["room"] == "101" and r["division"] == "Policy Division"
    assert r["email"] == "aksingh@gov.in" and r["phones"] == "011-2301" and r["source_url"] == "http://page"
    assert rows[1]["email"] == "" and rows[1]["phones"] == "011-2302"


def test_parse_tables_header_without_thead_and_email_from_row_text(W):
    html = """<table><tr><th>Name</th><th>Post</th><th>Contact</th></tr>
              <tr><td>Rajesh Kumar</td><td>Director</td><td>call 2301 mail rk[at]nic[dot]in</td></tr></table>"""
    rows = W.parse_tables(html, "u")
    assert rows[0]["email"] == "rk@nic.in"
    assert rows[0]["phones"].startswith("call 2301")


@pytest.mark.xfail(strict=True, reason="phone cells are filtered with SKIP_NAME, whose `\\d+\\.?` alternative also drops genuine "
                                       "all-digit phone numbers such as '23012345'")
def test_parse_tables_keeps_all_digit_phone_numbers(W):
    html = ("<table><thead><tr><th>Name</th><th>Designation</th><th>Phone</th></tr></thead>"
            "<tr><td>Amit Kumar</td><td>Director</td><td>23012345</td></tr></table>")
    assert W.parse_tables(html, "u")[0]["phones"] == "23012345"


def test_parse_tables_skips_tables_without_name_or_designation(W):
    assert W.parse_tables("<table><tr><th>Item</th><th>Value</th></tr><tr><td>a</td><td>b</td></tr></table>", "u") == []
    assert W.parse_tables("<table><tr><th>Name</th><th>Phone</th></tr><tr><td>Amit Kumar</td><td>1</td></tr></table>", "u") == []
    assert W.parse_tables("<table><tr><td>Name</td><td>Designation</td></tr><tr><td>Amit Kumar</td><td>D</td></tr></table>", "u") == []
    assert W.parse_tables("<p>none</p>", "u") == []


def test_parse_tables_phone_skip_and_length_cap(W):
    html = ("<table><thead><tr><th>Name</th><th>Designation</th><th>Phone</th><th>Phone 2</th></tr></thead>"
            f"<tr><td>Amit Kumar</td><td>Director</td><td>{'9-' * 150}</td><td>0-1</td></tr></table>")
    r = W.parse_tables(html, "u")[0]
    assert r["phones"] == ("9-" * 150)[:200]                      # capped at 200 chars; a second 'Phone' header gets no role


def test_parse_tables_division_column_goes_to_address_only_with_caption(W):
    html = """<table><caption>Cap</caption><thead><tr><th>Name</th><th>Designation</th><th>Section</th></tr></thead>
              <tr><td>Amit Kumar</td><td>Director</td><td>Sec A</td></tr></table>"""
    assert W.parse_tables(html, "u")[0]["division"] == "Cap"
    html2 = html.replace("<caption>Cap</caption>", "")
    assert W.parse_tables(html2, "u")[0]["division"] == "Sec A"


def test_parse_tables_first_role_wins_for_duplicate_headers(W):
    html = """<table><thead><tr><th>Name</th><th>Officer Name</th><th>Designation</th></tr></thead>
              <tr><td>First Name</td><td>Second Name</td><td>Dir</td></tr></table>"""
    # the second 'name'-looking header is not assigned a role a second time
    assert W.parse_tables(html, "u")[0]["name"] == "First Name"


# ------------------------------------------------------------------ get / urls
def test_get_returns_200_only_and_handles_errors(W, monkeypatch):
    calls = []

    def fake_get(url, **kw):
        calls.append((url, kw))
        return Resp(status=404 if "404" in url else 200)
    monkeypatch.setattr(W.session, "get", fake_get)
    assert W.get("https://a.gov.in/ok").status_code == 200
    assert W.get("https://a.gov.in/404") is None
    assert calls[0][1]["verify"] is False and calls[0][1]["timeout"] == 25 and calls[0][1]["allow_redirects"] is True


def test_get_retries_dead_nic_domain_as_gov_in(W, monkeypatch):
    seen = []

    def fake_get(url, **kw):
        seen.append(url)
        if ".nic.in" in url:
            raise requests.ConnectionError("dead")
        return Resp(status=200, url=url)
    monkeypatch.setattr(W.session, "get", fake_get)
    assert W.get("https://dept.nic.in/x").url == "https://dept.gov.in/x"
    assert seen == ["https://dept.nic.in/x", "https://dept.gov.in/x"]
    # non-nic hosts are not retried; a failing retry returns None
    seen.clear()
    monkeypatch.setattr(W.session, "get", lambda url, **kw: (_ for _ in ()).throw(requests.Timeout()))
    assert W.get("https://dept.gov.in/x") is None
    assert W.get("https://dept.nic.in/x") is None
    # a non-200 on the first request is returned as None without a retry
    monkeypatch.setattr(W.session, "get", lambda url, **kw: Resp(status=500))
    assert W.get("https://dept.nic.in/x") is None


def test_find_whoswho_urls_prefers_quick_links(W, monkeypatch):
    monkeypatch.setattr(W, "get", lambda *a, **k: pytest.fail("no probing when quick links exist"))
    links = ["https://m.gov.in/about", "https://m.gov.in/whos-who", "https://m.gov.in/who-is-who"]
    assert W.find_whoswho_urls("https://m.gov.in", links) == ["https://m.gov.in/whos-who", "https://m.gov.in/who-is-who"]


def test_find_whoswho_urls_probes_paths_then_homepage(W, monkeypatch):
    monkeypatch.setattr(W.time, "sleep", lambda s: None)
    probed = []

    def fake_get(url, timeout=25):
        probed.append(url)
        if url == "https://m.gov.in/whos-who":
            return Resp("<h1>Who's Who</h1>", url=url)
        return None
    monkeypatch.setattr(W, "get", fake_get)
    assert W.find_whoswho_urls("https://m.gov.in/", []) == ["https://m.gov.in/whos-who"]
    assert probed[0] == "https://m.gov.in/about-us/whos-who" and probed[1] == "https://m.gov.in/whos-who" and len(probed) == 2

    # a probe that answers but does not mention who's who is ignored; homepage nav link is the last resort
    def fake_get2(url, timeout=25):
        if url == "https://m.gov.in":
            return Resp('<a href="/about">About</a><a href="/staff/whos-who.html">x</a>', url="https://m.gov.in/")
        return None
    monkeypatch.setattr(W, "get", fake_get2)
    assert W.find_whoswho_urls("https://m.gov.in", []) == ["https://m.gov.in/staff/whos-who.html"]
    monkeypatch.setattr(W, "get", lambda url, timeout=25: None)
    assert W.find_whoswho_urls("https://m.gov.in", []) == []
    # link text (not href) can carry the who's-who hint
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp('<a href="/p1">Who is Who</a>', url="https://m.gov.in/") if url == "https://m.gov.in" else None)
    assert W.find_whoswho_urls("https://m.gov.in", []) == ["https://m.gov.in/p1"]


def test_quick_links_for(W, monkeypatch):
    html = ('<a href="http://top.in">t</a> Quick Links <a href="https://m.gov.in/whos-who">w</a>'
            '<a href="https://m.gov.in/other">o</a> Organizations Under <a href="https://under.in">u</a>')
    seen = []
    monkeypatch.setattr(W, "get", lambda url, timeout=25: (seen.append(url), Resp(html))[1])
    assert W.quick_links_for("42") == ["https://m.gov.in/whos-who", "https://m.gov.in/other"]
    assert seen == ["https://igod.gov.in/organization/42"]
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp("<p>no links section</p>"))
    assert W.quick_links_for("42") == []
    monkeypatch.setattr(W, "get", lambda url, timeout=25: None)
    assert W.quick_links_for("42") == []


# ------------------------------------------------------------------ PDF + Next.js
def _fake_pdfplumber(monkeypatch, pages):
    class Page:
        def __init__(self, tables, text):
            self._t, self._x = tables, text

        def extract_tables(self):
            return self._t

        def extract_text(self):
            return self._x

    class Pdf:
        def __init__(self, pages):
            self.pages = [Page(*p) for p in pages]

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False
    mod = types.SimpleNamespace(open=lambda f: Pdf(pages))
    monkeypatch.setitem(sys.modules, "pdfplumber", mod)


def test_parse_pdf_tables(W, monkeypatch):
    table = [["Name", "Designation", "Phone", "Email", "Division"],
             ["Amit Kumar", "Director", "2301", "ak[at]gov[dot]in", "Policy"],
             ["Vacant", "Director", "", "", ""],
             ["12", "x", "", "", ""],
             ["Bina Rao", "", "9 8", "", ""],
             [None, "Dir", None, None, None]]
    _fake_pdfplumber(monkeypatch, [([table, [["only one col"]], None, [["Item", "Value"], ["a", "b"]]], "")])
    rows = W.parse_pdf(b"%PDF", "http://pdf")
    assert [r["name"] for r in rows] == ["Amit Kumar", "Bina Rao"]
    assert rows[0] == {"division": "Policy", "name": "Amit Kumar", "designation": "Director", "room": "", "phones": "2301",
                       "email": "ak@gov.in", "source_url": "http://pdf"}
    assert rows[1]["phones"] == "9 8"


def test_parse_pdf_text_fallback_only_when_no_table_rows(W, monkeypatch):
    text = ("1. Shri Ramesh Kumar, Joint Secretary rk@gov.in call 011-23012345\n"
            "Dr. Sita Devi Director sd[at]nic[dot]in\n"
            "random line without match\n")
    _fake_pdfplumber(monkeypatch, [([], text)])
    rows = W.parse_pdf(b"x", "u")
    assert [r["name"] for r in rows] == ["Shri Ramesh Kumar", "Dr. Sita Devi"]
    assert rows[0]["email"] == "rk@gov.in" and "011-23012345" in rows[0]["phones"] and rows[0]["designation"] == "Joint Secretary"
    assert rows[1]["email"] == "sd@nic.in"
    # once a page produced table rows, the later page's text fallback is still attempted only if out is empty
    table = [["Name", "Designation"], ["Amit Kumar", "Director"]]
    _fake_pdfplumber(monkeypatch, [([table], "Shri Other Person, Director o@gov.in")])
    assert [r["name"] for r in W.parse_pdf(b"x", "u")] == ["Amit Kumar"]


def test_parse_pdf_handles_exceptions(W, monkeypatch, capsys):
    def boom(f):
        raise ValueError("corrupt")
    monkeypatch.setitem(sys.modules, "pdfplumber", types.SimpleNamespace(open=boom))
    assert W.parse_pdf(b"x", "http://bad") == []
    assert "pdf parse failed http://bad: corrupt" in capsys.readouterr().err


def test_parse_pdf_page_limit(W, monkeypatch):
    table = [["Name", "Designation"], ["Amit Kumar", "Director"]]
    _fake_pdfplumber(monkeypatch, [([table], "")] * 70)
    assert len(W.parse_pdf(b"x", "u")) == 60


def _next_page(build="b1"):
    return f'<html><script id="__NEXT_DATA__" type="application/json">{json.dumps({"buildId": build})}</script></html>'


def test_parse_nextjs_extracts_embedded_tables(W, monkeypatch):
    table = "<table><tr><th>Name</th><th>Designation</th></tr><tr><td>Amit Kumar</td><td>Director</td></tr></table>"
    seen = []
    monkeypatch.setattr(W, "get", lambda url, timeout=25: (seen.append(url), Resp(json.dumps({"pageProps": {"body": table}})))[1])
    rows = W.parse_nextjs(_next_page(), "https://m.gov.in/about/whos-who")
    assert [r["name"] for r in rows] == ["Amit Kumar"]
    assert seen == ["https://m.gov.in/_next/data/b1/about/whos-who.json?parentslug=about/whos-who"]
    seen.clear()
    W.parse_nextjs(_next_page(), "https://m.gov.in/")
    assert seen == ["https://m.gov.in/_next/data/b1/index.json?parentslug=index"]


def test_parse_nextjs_degenerate_inputs(W, monkeypatch):
    monkeypatch.setattr(W, "get", lambda *a, **k: pytest.fail("must not fetch"))
    assert W.parse_nextjs("<html></html>", "https://m.gov.in/x") == []
    assert W.parse_nextjs('<script id="__NEXT_DATA__" type="application/json">{not json</script>', "https://m.gov.in/x") == []
    assert W.parse_nextjs(_next_page(build=""), "https://m.gov.in/x") == []
    monkeypatch.setattr(W, "get", lambda *a, **k: None)
    assert W.parse_nextjs(_next_page(), "https://m.gov.in/x") == []


@pytest.mark.xfail(strict=True, reason="parse_nextjs round-trips the JSON text through .encode().decode('unicode_escape'), which "
                                       "re-decodes UTF-8 bytes as Latin-1: non-ASCII names in a raw-UTF-8 payload come out garbled")
def test_parse_nextjs_preserves_non_ascii_names(W, monkeypatch):
    table = "<table><tr><th>Name</th><th>Designation</th></tr><tr><td>José Núñez</td><td>Director</td></tr></table>"
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp(json.dumps({"b": table}, ensure_ascii=False)))
    assert W.parse_nextjs(_next_page(), "https://m.gov.in/x")[0]["name"] == "José Núñez"


# ------------------------------------------------------------------ scrape_ministry / main
ROW = {"name": "Ministry X", "website": "https://x.gov.in", "igod_org_id": "7"}


def test_scrape_ministry_html_table(W, monkeypatch):
    monkeypatch.setattr(W, "quick_links_for", lambda oid: ["https://x.gov.in/whos-who"])
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp(TABLE, url=url, headers={"Content-Type": "text/html"}))
    name, website, used, offs = W.scrape_ministry(ROW)
    assert (name, website, used) == ("Ministry X", "https://x.gov.in", "https://x.gov.in/whos-who") and len(offs) == 2
    # without an igod id quick links are not requested
    monkeypatch.setattr(W, "quick_links_for", lambda oid: pytest.fail("no id"))
    monkeypatch.setattr(W, "find_whoswho_urls", lambda w, l: [])
    assert W.scrape_ministry({**ROW, "igod_org_id": ""}) == ("Ministry X", "https://x.gov.in", "", [])


def test_scrape_ministry_pdf_by_extension_and_content_type(W, monkeypatch):
    monkeypatch.setattr(W, "quick_links_for", lambda oid: [])
    monkeypatch.setattr(W, "find_whoswho_urls", lambda w, l: ["https://x.gov.in/a.PDF", "https://x.gov.in/b"])
    parsed = []
    monkeypatch.setattr(W, "parse_pdf", lambda c, u: (parsed.append(u), [{"name": "N"}] if u.endswith("b") else [])[1])
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp("x", url=url, headers={"Content-Type": "application/pdf" if url.endswith("b") else ""}))
    _, _, used, offs = W.scrape_ministry(ROW)
    assert parsed == ["https://x.gov.in/a.PDF", "https://x.gov.in/b"] and used == "https://x.gov.in/b" and offs == [{"name": "N"}]


def test_scrape_ministry_falls_back_to_nextjs_and_linked_pdf(W, monkeypatch):
    monkeypatch.setattr(W, "quick_links_for", lambda oid: [])
    monkeypatch.setattr(W, "find_whoswho_urls", lambda w, l: ["https://x.gov.in/p"])
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp("<html>__NEXT_DATA__</html>", url=url))
    monkeypatch.setattr(W, "parse_nextjs", lambda html, u: [{"name": "From Next"}])
    assert W.scrape_ministry(ROW)[3] == [{"name": "From Next"}]

    pages = {"https://x.gov.in/p": '<a href="/files/other.pdf">other</a><a href="/files/WhosWho.pdf">pdf</a>',
             "https://x.gov.in/files/WhosWho.pdf": "binary"}
    monkeypatch.setattr(W, "get", lambda url, timeout=25: Resp(pages[url], url=url) if url in pages else None)
    monkeypatch.setattr(W, "parse_pdf", lambda c, u: [{"name": "From PDF", "u": u}])
    got = W.scrape_ministry(ROW)
    assert got[3] == [{"name": "From PDF", "u": "https://x.gov.in/files/WhosWho.pdf"}]
    # a linked pdf that cannot be fetched, or that has no rows, yields nothing; unreachable pages are skipped
    monkeypatch.setattr(W, "parse_pdf", lambda c, u: [])
    assert W.scrape_ministry(ROW)[3] == []
    monkeypatch.setattr(W, "get", lambda url, timeout=25: None)
    assert W.scrape_ministry(ROW)[2:] == ("", [])


def test_main_writes_union_ministry_roster(W, repo, monkeypatch, capsys):
    with (repo / "data" / "organizations_index.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "branch", "category_code", "website", "igod_org_id"])
        w.writeheader()
        w.writerows([
            {"name": "M1", "branch": "ug", "category_code": "E002", "website": "https://m1.gov.in", "igod_org_id": "1"},
            {"name": "M1 dup", "branch": "ug", "category_code": "E003", "website": "https://m1.gov.in", "igod_org_id": "2"},
            {"name": "State", "branch": "sg", "category_code": "E002", "website": "https://s.gov.in", "igod_org_id": "3"},
            {"name": "Other cat", "branch": "ug", "category_code": "X", "website": "https://o.gov.in", "igod_org_id": "4"},
            {"name": "No site", "branch": "ug", "category_code": "E053", "website": "", "igod_org_id": "5"},
            {"name": "M2", "branch": "ug", "category_code": "E053", "website": "https://m2.gov.in", "igod_org_id": "6"},
        ])
    def fake_scrape(row):
        if row["name"] == "M1":
            return "M1", row["website"], "https://m1.gov.in/whos-who", [{"division": "d", "name": "Amit Kumar", "designation": "Dir",
                                                                          "room": "1", "phones": "2", "email": "a@b.in", "source_url": "u"}]
        return row["name"], row["website"], "", []
    monkeypatch.setattr(W, "scrape_ministry", fake_scrape)
    W.main()
    rows = list(csv.DictReader((repo / "data" / "ministry_officials.csv").open()))
    assert rows == [{"ministry": "M1", "website": "https://m1.gov.in", "division": "d", "name": "Amit Kumar", "designation": "Dir",
                     "room": "1", "phones": "2", "email": "a@b.in", "source_url": "u"}]
    err = capsys.readouterr().err
    assert "2 ministry/department websites" in err and "[1/2] M1: 1 officials (https://m1.gov.in/whos-who)" in err
    assert "M2: 0 officials (no whos-who found)" in err and "wrote 1 officials" in err
