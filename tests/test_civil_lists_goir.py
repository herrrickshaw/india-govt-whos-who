"""scripts/dopt_civil_list.py, scripts/ips_civil_list.py, scripts/goir_ap.py, scripts/goir_telangana.py (all network faked)."""
import csv
import datetime as dt
import sys
import types

import pytest
import requests

from helpers import read, write_csv


class Resp:
    def __init__(self, text="", status=200, content=b""):
        self.text, self.status_code, self.content = text, status, content

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(str(self.status_code))


# ================================================================== dopt_civil_list
@pytest.fixture
def DO(load, monkeypatch):
    m = load("dopt_civil_list")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


ROW = ('<tr><td><img src="data:image/png;base64,AAAA"><h3>अमित कुमार</h3>'
       '<a href="http://er/x?a=1&amp;b=2"><b>Name:</b> Amit   Kumar </a> DOB: 01/02/1980 '
       '<p><b>Identity No.:</b> 12345</p><p><b>Allotment Year:</b> 2005</p><p><b>Source of Recruitment:</b> Direct</p>'
       '<p><b>Qualification(Subject):</b> <i>M.A.</i> (History)</p><p><b>Pay Scale:</b> Level 14</p><p><b>Remarks:</b> none</p>'
       '<p><b>&</b> Uttar Pradesh</p>'
       '<b>Posting:-</b><ul><li>Joint Secretary, Ministry of Power Posting W.E.F.: 15/06/2024</li></ul></td></tr>')


def test_strip_images_and_clean(DO):
    assert DO.strip_images('<img src="data:image/png;base64,AAAA"> x') == '<img src=""> x'
    assert DO.clean("<b>a</b>  &amp; b\n") == "a & b" and DO.clean(None) == ""


def test_parse_row_extracts_all_fields(DO):
    r = DO.parse_row(ROW, "UP", 7)
    assert r == {"cadre_code": "UP", "sr_no": 7, "name_en": "Amit Kumar", "name_hi": "अमित कुमार", "identity_no": "12345", "allotment_year": "2005",
                 "source_of_recruitment": "Direct", "qualification": "M.A. (History)", "pay_scale": "Level 14", "remarks": "none",
                 "domicile_state": "Uttar Pradesh", "current_posting": "Joint Secretary, Ministry of Power", "posting_wef": "15/06/2024",
                 "dob": "01/02/1980", "er_sheet_url": "http://er/x?a=1&b=2"}
    assert list(r) == DO.FIELDS


def test_parse_row_missing_fields_default_blank(DO):
    r = DO.parse_row("<tr><td>nothing</td></tr>", "AP", 1)
    assert r["name_en"] == "" and r["dob"] == "" and r["current_posting"] == "" and r["posting_wef"] == "" and r["er_sheet_url"] == ""
    r = DO.parse_row('<b>Posting:-</b><li>Collector</li>', "AP", 1)
    assert r["current_posting"] == "Collector" and r["posting_wef"] == ""


def test_fetch_cadre_retries(DO, monkeypatch):
    seq = iter([requests.ConnectionError("x"), Resp("", 500), Resp("page", 200)])
    posted = []

    def fake_post(url, data, timeout):
        posted.append(data)
        v = next(seq)
        if isinstance(v, Exception):
            raise v
        return v
    monkeypatch.setattr(DO.session, "post", fake_post)
    assert DO.fetch_cadre("UP") == "page" and posted[0] == {"ViewCadreCode": "UP", "btn_submit": "Submit"} and len(posted) == 3
    monkeypatch.setattr(DO.session, "post", lambda url, data, timeout: Resp("", 500))
    assert DO.fetch_cadre("UP") is None


def test_main_collects_cadres(DO, repo, monkeypatch, capsys):
    page = "<table><tr><td>header</td></tr>" + ROW + ROW.replace("Amit   Kumar", "Bina Rao") + "<tr><td>Identity No only</td></tr></table>"
    monkeypatch.setattr(DO, "CADRES", ["UP", "BR", "XX"])
    monkeypatch.setattr(DO, "fetch_cadre", lambda c: None if c == "XX" else page)
    DO.main()
    d = read(repo / "data/ias_officers.csv", keep_default_na=False)
    assert list(d.cadre_code) == ["UP", "UP", "BR", "BR"] and list(d.sr_no) == [1, 2, 3, 4]
    assert list(d.name_en)[:2] == ["Amit Kumar", "Bina Rao"]
    err = capsys.readouterr().err
    assert "UP: 2 officers" in err and "FAILED cadre XX" in err


# ================================================================== ips_civil_list
@pytest.fixture
def IP(load):
    return load("ips_civil_list")


def W(text, x0, top):
    return {"text": text, "x0": x0, "top": top}


def test_cluster_rows_and_columns(IP):
    words = [W("b", 10, 100.0), W("a", 5, 101.5), W("c", 50, 110.0), W("d", 60, 113.1)]
    bands = IP.cluster_rows(words)
    assert [[w["text"] for w in ws] for _, ws in bands] == [["b", "a"], ["c"], ["d"]]               # tolerance is 3.0 from the band's first word
    assert IP.cluster_rows([]) == []
    hdr = [W(f"({i})", 10 + 100 * (i - 1), 50) for i in range(1, 7)]
    assert IP.page_column_bounds(hdr) == [10, 110, 210, 310, 410, 510]
    assert IP.page_column_bounds(hdr[:5]) is None and IP.page_column_bounds([W("x", 1, 1)]) is None
    b = IP.page_column_bounds(hdr)
    assert IP.assign_column(108, b) == 1 and IP.assign_column(107.9, b) == 0 and IP.assign_column(10, b) == 0 and IP.assign_column(509, b) == 5


def test_cadre_state_for_page(IP):
    hdr = [W(f"({i})", 10 + 100 * (i - 1), 50) for i in range(1, 7)]
    b = IP.page_column_bounds(hdr)
    words = hdr + [W("Kerala", 450, 10), W("(Cadre)", 500, 10), W("1234", 460, 10), W("Left", 20, 10), W("below", 450, 60)]
    assert IP.cadre_state_for_page(words, b) == "Kerala (Cadre)"
    assert IP.cadre_state_for_page(hdr + [W("Left", 20, 10)], b) is None


def test_flush_record_assembles_columns(IP):
    def rows(*lines):
        return [[W(t, i * 10, 0) for i, t in enumerate(l.split())] for l in lines]
    rec = {1: rows("अमित कुमार\u0000", "AMIT KUMAR", "B.A. Hons"),
           2: rows("RR", "1234567", "Uttar Pradesh"),
           3: rows("01/02/1980", "05/06/2005", "01/01/2000"),
           4: rows("SP Kanpur Level 14 A 15/06/2024"),
           5: rows("Police Medal")}
    r = IP.flush_record(rec, "Uttar Pradesh", "2005", 4)
    assert r["name_hi"] == "अमित कुमार"           # the NUL byte from the broken ToUnicode map is stripped
    assert (r["name_en"], r["qualification"], r["source_of_recruitment"], r["officer_code"], r["domicile_state"]) == \
        ("AMIT KUMAR", "B.A. Hons", "RR", "1234567", "Uttar Pradesh")
    assert (r["dob"], r["appointment_date"]) == ("01/02/1980", "05/06/2005")
    assert r["pay_scale"] == "Level 14 A" and r["posting_wef"] == "15/06/2024" and r["current_posting"] == "SP Kanpur"
    assert r["awards"] == "Police Medal" and r["cadre_state"] == "Uttar Pradesh" and r["allotment_year"] == "2005" and r["sr_no"] == 4
    assert set(r) == set(IP.FIELDS)
    empty = IP.flush_record({}, "X", "", 1)
    assert empty["name_en"] == "" and empty["pay_scale"] == "" and empty["current_posting"] == ""


def _fake_pdfplumber(monkeypatch, pages):
    class Page:
        def __init__(self, words):
            self.words = words

        def extract_words(self, **kw):
            return self.words

    class Pdf:
        def __init__(self):
            self.pages = [Page(w) for w in pages]

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False
    monkeypatch.setitem(sys.modules, "pdfplumber", types.SimpleNamespace(open=lambda p: Pdf()))


def _page(cadre, rows_):
    """rows_: list of (top, [(x0, text)]) data rows below the header."""
    hdr = [W(f"({i})", 10 + 100 * (i - 1), 50) for i in range(1, 7)]
    words = hdr + [W(cadre, 450, 10)]
    for top, cells in rows_:
        words += [W(t, x, top) for x, t in cells]
    return words


def test_parse_pdf_records_across_pages(load, monkeypatch):
    sys.modules.pop("pdfplumber", None)
    _fake_pdfplumber(monkeypatch, [
        _page("Kerala", [(70, [(300, "Allotment"), (330, "Year"), (360, ":"), (370, "2005")]),
                         (90, [(10, "1"), (110, "AMIT"), (140, "KUMAR"), (210, "RR"), (310, "01/02/1980"), (410, "SP"), (510, "Medal")]),
                         (110, [(110, "B.A."), (210, "Kerala")]),
                         (130, [(10, "2"), (110, "BINA"), (140, "RAO"), (210, "SPS")])]),
        [W("cover", 10, 10)],                                                                    # page without the (1)..(6) header
        _page("Kerala", [(90, [(10, "3"), (110, "CHITRA"), (140, "DAS")])]),
        _page("Not A Cadre", [(90, [(10, "4"), (110, "DEV"), (140, "ROY")])]),
    ])
    import importlib
    IP = load("ips_civil_list")
    rows = IP.parse_pdf("x.pdf")
    assert [(r["sr_no"], r["name_en"]) for r in rows] == [(1, "AMIT KUMAR"), (2, "BINA RAO"), (3, "CHITRA DAS")]       # invalid cadre dropped
    assert rows[0]["allotment_year"] == "2005" and rows[0]["cadre_state"] == "Kerala" and rows[0]["domicile_state"] == "Kerala"
    assert rows[1]["source_of_recruitment"] == "SPS"


def test_resolve_and_download_pdf(IP, repo, monkeypatch):
    class S:
        def __init__(self):
            self.headers = {}
            self.urls = []

        def get(self, url, timeout, headers=None):
            self.urls.append(url)
            if url == IP.HOME_URL:
                return Resp("home")
            return Resp('<a href="Empanelment/CivilList2026.pdf">x</a>' if "ips_civillist" in url else "", 200, b"%PDF data")
    s = S()
    assert IP.resolve_pdf_url(s) == "https://ips.gov.in/Empanelment/CivilList2026.pdf"
    monkeypatch.setattr(IP.requests, "Session", lambda: S())
    path = IP.download_pdf()
    assert path.read_bytes() == b"%PDF data"
    assert IP.download_pdf() == path                                           # cached unless forced
    monkeypatch.setattr(IP, "resolve_pdf_url", lambda s: "http://x/y.pdf")
    path.write_bytes(b"old")
    IP.download_pdf(force=True)
    assert path.read_bytes() == b"%PDF data"


def test_resolve_pdf_url_without_link(IP):
    class S:
        def get(self, url, timeout, headers=None):
            return Resp("nothing here")
    with pytest.raises(RuntimeError, match="could not find"):
        IP.resolve_pdf_url(S())


def test_main_writes_csv(IP, repo, monkeypatch, capsys):
    monkeypatch.setattr(IP, "download_pdf", lambda force=False: (setattr(IP, "forced", force), "p.pdf")[1])
    monkeypatch.setattr(IP, "parse_pdf", lambda p: [{**{f: "" for f in IP.FIELDS}, "cadre_state": "Kerala", "name_en": "A B"},
                                                   {**{f: "" for f in IP.FIELDS}, "cadre_state": "Kerala", "name_en": "C D"},
                                                   {**{f: "" for f in IP.FIELDS}, "cadre_state": "Bihar", "name_en": "E F"}])
    monkeypatch.setattr(sys, "argv", ["x", "--force"])
    IP.main()
    assert IP.forced is True and len(read(repo / "data/ips_officers.csv")) == 3
    err = capsys.readouterr().err
    assert "Bihar: 1 officers" in err and "Kerala: 2 officers" in err


# ================================================================== goir_telangana
GRID_TS = ('<input type="hidden" name="__VIEWSTATE" value="vs"><table id="FileMoveList2"><tr><th>h</th></tr>'
           '<tr><td>1</td><td>x</td><td>y</td><td>GO Ms</td><td>12</td><td>03/04/2025</td><td>Revenue</td><td>Abstract text</td><td>Download</td></tr>'
           '<tr><td>short</td></tr></table>')


class FakeSession:
    def __init__(self, routes):
        self.routes, self.headers, self.verify, self.calls = routes, {}, True, []

    def get(self, url, **kw):
        self.calls.append(("get", url))
        return self.routes("get", url, kw)

    def post(self, url, **kw):
        self.calls.append(("post", url, kw.get("data")))
        return self.routes("post", url, kw)


def test_goir_telangana_downloads_and_resumes(load, repo, monkeypatch, capsys):
    T = load("goir_telangana")
    monkeypatch.setattr(T.time, "sleep", lambda s: None)
    home = '<input type="hidden" name="__VIEWSTATE" value="vs"><select id="DDLDeptname"><option value="Select">Select</option><option value="REV">Revenue</option><option value="EDU">Education</option></select>'

    def routes(m, url, kw):
        if m == "get":
            return Resp(home)
        d = kw["data"]
        if "BtnSearch" in d:
            return Resp(GRID_TS) if d["DDLDeptname"] == "REV" else Resp("<p>no grid</p>")
        return Resp(content=b"%PDF-1.4 pdf")
    sess = FakeSession(routes)
    monkeypatch.setattr(T, "S", sess)
    monkeypatch.setattr(sys, "argv", ["x", "--years", "2025", "--depts", "REV", "EDU"])
    T.main()
    c = read(repo / "data/states/TS/candidates.csv", keep_default_na=False)
    assert len(c) == 1
    r = c.iloc[0]
    assert (r.ministry, r.title, r.date, r.category, r.group, r.host) == ("Revenue Department, Telangana", "Abstract text", "2025-04-03", "Revenue", "TS", "goir.telangana.gov.in")
    assert (repo / f"data/states/TS/pdf/{r.doc_id}.pdf").read_bytes().startswith(b"%PDF")
    assert "2025 REV: 1 orders" in capsys.readouterr().out
    post = [c for c in sess.calls if c[0] == "post" and "__EVENTTARGET" in (c[2] or {})][0]
    assert post[2]["__EVENTARGUMENT"] == "Select$0" and post[2]["__VIEWSTATE"] == "vs"
    # second run: already-known documents are skipped without downloading
    sess.calls.clear()
    T.main()
    assert not [c for c in sess.calls if c[0] == "post" and "__EVENTTARGET" in (c[2] or {})]
    assert len(read(repo / "data/states/TS/candidates.csv")) == 1


def test_goir_telangana_skips_non_pdf_failed_search_and_max(load, repo, monkeypatch, capsys):
    T = load("goir_telangana")
    monkeypatch.setattr(T.time, "sleep", lambda s: None)
    home = '<select id="DDLDeptname"><option value="Select">S</option><option value="A">A dept</option><option value="B">B dept</option></select>'
    grid = GRID_TS.replace("</table>", '<tr><td>2</td><td>x</td><td>y</td><td>GO Rt</td><td>13</td><td>bad date</td><td>Cat</td><td>Second</td><td>Download</td></tr></table>')

    def routes(m, url, kw):
        if m == "get":
            return Resp(home)
        d = kw["data"]
        if "BtnSearch" in d:
            return None if d["DDLDeptname"] == "B" else Resp(grid)
        return Resp(content=b"<html>" if d["__EVENTARGUMENT"] == "Select$0" else b"%PDF ok")
    monkeypatch.setattr(T, "S", FakeSession(routes))
    monkeypatch.setattr(sys, "argv", ["x", "--years", "2025", "--max", "1"])
    T.main()
    c = read(repo / "data/states/TS/candidates.csv", keep_default_na=False)
    assert list(c.title) == ["Second"] and list(c.date) == [""]                    # first GO served HTML (skipped); unparsable date -> ''
    assert "downloaded" not in capsys.readouterr().out                              # --max returns before the summary line


# ================================================================== goir_ap
def grid_ap(n, gid_start=1):
    rows = "".join(f'<tr><td>{i}</td><td>GO.{i}</td><td>0{(i % 9) + 1}/03/2025</td><td>Cat</td><td>Abs {i}</td><td>IT -  Dept\n  of X</td><td>Sec</td><td>x</td>'
                   f'<td><a onclick=\'downloadFile("{gid_start + i}", "E")\'>E</a></td></tr>' for i in range(n))
    return f'<table id="FileMoveList2"><tr><th>h</th></tr>{rows}<tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>no english file</td></tr></table>'


def test_goir_ap_search_and_windows(load, monkeypatch):
    A = load("goir_ap")
    posted = []
    home = '<input type="hidden" name="__VIEWSTATE" value="v"><select id="DDLDeptname"><option value="-1">All</option><option value="D1">One</option><option value="D2">Two</option></select>'

    def get(m, url, **k):
        if m == "get":
            return Resp(home)
        posted.append(k["data"])
        a, b = k["data"][A.P + "txtfrmdate"], k["data"][A.P + "txttodate"]
        dept = k["data"][A.P + "DDLDeptname"]
        n = 100 if (a != b or dept == "-1") else 2           # a multi-day or all-department window is 'full'
        return Resp(grid_ap(n if n < 100 else 99))
    monkeypatch.setattr(A, "get", get)
    rows, _ = A.search(dt.date(2025, 3, 1), dt.date(2025, 3, 2))
    assert len(rows) == 100 and rows[-1] is None and rows[0]["gid"] == "1" and rows[0]["date"] == "01/03/2025"
    assert A.depts_of(__import__("bs4").BeautifulSoup(home, "html.parser")) == ["D1", "D2"]
    assert posted[0][A.P + "txtfrmdate"] == "01-03-2025" and posted[0][A.P + "BtnSearch"] == "Search" and posted[0]["__VIEWSTATE"] == "v"


def test_goir_ap_windows_split_by_date_then_department(load, monkeypatch):
    A = load("goir_ap")
    calls = []

    def fake_search(a, b, dept="-1"):
        calls.append((a, b, dept))
        full = (a < b) or dept == "-1"
        return ([{"gid": f"{a}-{dept}-{i}"} for i in range(99)] + [None]) if full else ([{"gid": f"{a}-{dept}"}, None]), None
    monkeypatch.setattr(A, "search", fake_search)
    out = list(A.windows(dt.date(2025, 3, 1), dt.date(2025, 3, 2), "-1", ["D1", "D2"]))
    assert [o["gid"] for o in out] == ["2025-03-01-D1", "2025-03-01-D2", "2025-03-02-D1", "2025-03-02-D2"]
    assert calls[0] == (dt.date(2025, 3, 1), dt.date(2025, 3, 2), "-1")
    # a window below the cap yields its rows (None entries dropped) without splitting
    monkeypatch.setattr(A, "search", lambda a, b, dept="-1": ([{"gid": "x"}, None], None))
    assert list(A.windows(dt.date(2025, 3, 1), dt.date(2025, 3, 5), "-1", [])) == [{"gid": "x"}]


def test_goir_ap_main_downloads_month_by_month(load, repo, monkeypatch, capsys):
    A = load("goir_ap")
    monkeypatch.setattr(A.time, "sleep", lambda s: None)
    home = '<select id="DDLDeptname"><option value="-1">All</option><option value="D1">One</option></select>'
    month_rows = {dt.date(2025, 1, 1): [dict(gid="11", no="12", date="05/01/2025", cat="Cat", abstract="Abs A", org="IT - Dept of X", section="s"),
                                        dict(gid="12", no="13", date="bad", cat="Cat", abstract="Abs B", org="Plain Org", section="s")],
                  dt.date(2025, 2, 1): [dict(gid="21", no="22", date="01/02/2025", cat="Cat", abstract="Abs C", org="Org", section="s")]}

    def fake_get(m, url, **k):
        if url == A.U:
            return Resp(home)
        gid = url.split("gid=")[1].split("&")[0]
        return Resp(content=b"%PDF" if gid != "12" else b"html page")
    monkeypatch.setattr(A, "get", fake_get)
    monkeypatch.setattr(A, "windows", lambda cur, end, dept, depts: iter(month_rows.get(cur, [])))
    monkeypatch.setattr(sys, "argv", ["x", "--from", "2025-01-01", "--to", "2025-02-10"])
    A.main()
    c = read(repo / "data/states/AP/candidates.csv", keep_default_na=False)
    assert list(c.title) == ["GO 12 - Abs A", "GO 22 - Abs C"]                               # gid 12 served HTML -> skipped
    assert list(c.date) == ["2025-01-05", "2025-02-01"] and c.ministry.iloc[0] == "Dept Of X, Andhra Pradesh"
    out = capsys.readouterr().out
    assert "2025-01-01 2025-01-31 1" in out and "2025-02-01 2025-02-10 1" in out and "downloaded 2" in out
    # resumable and --max
    monkeypatch.setattr(sys, "argv", ["x", "--from", "2025-01-01", "--to", "2025-01-31"])
    A.main()
    assert len(read(repo / "data/states/AP/candidates.csv")) == 2


def test_goir_ap_get_retries(load, monkeypatch):
    A = load("goir_ap")
    monkeypatch.setattr(A.time, "sleep", lambda s: None)
    n = {"c": 0}

    class S:
        def get(self, *a, **k):
            n["c"] += 1
            raise requests.Timeout()
    monkeypatch.setattr(A, "S", S())
    assert A.get("get", "http://u") is None and n["c"] == 3
