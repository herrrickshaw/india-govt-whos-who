"""scripts/igod_crawl.py and scripts/igod_org_details.py with the HTTP session faked."""
import csv

import pytest
import requests

from helpers import read, write_csv


class Resp:
    def __init__(self, text="", status=200):
        self.text, self.status_code = text, status


# ================================================================== igod_crawl
@pytest.fixture
def G(load, monkeypatch):
    m = load("igod_crawl")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def row_html(name, href=None, detail=None):
    title = f'<a class="search-title" href="{href}">{name}</a>' if href else f'<span class="search-title">{name}</span>'
    opts = f'<div class="search-opts"><a href="{detail}">d</a></div>' if detail else ""
    return f'<div class="search-result-row">{title}{opts}</div>'


def test_parse_rows(G):
    html = (row_html("  Ministry  of   X ", "https://x.gov.in", "https://igod.gov.in/organization/ABCDEFGHIJKLMNO123")
            + row_html("Internal link", "https://igod.gov.in/foo")
            + row_html("Short id", None, "https://igod.gov.in/organization/short")
            + '<div class="search-result-row"><a class="btn-detail" href="https://igod.gov.in/organization/ZZZZZZZZZZZZZZZZZZ"></a></div>'
            + '<div class="search-result-row"><span class="search-title"> </span></div>')
    rows = G.parse_rows(html)
    assert rows == [("Ministry of X", "ABCDEFGHIJKLMNO123", "https://x.gov.in"), ("Internal link", None, None), ("Short id", None, None)]


def test_get_retries_then_returns_none(G, monkeypatch):
    seq = iter([requests.ConnectionError("x"), Resp("", 500), Resp("ok", 200)])

    def fake(url, timeout, **kw):
        v = next(seq)
        if isinstance(v, Exception):
            raise v
        return v
    monkeypatch.setattr(G.session, "get", fake)
    assert G.get("http://u").text == "ok"
    monkeypatch.setattr(G.session, "get", lambda url, timeout, **kw: Resp("", 404))
    assert G.get("http://u") is None


def test_discover_listings_bfs(G, monkeypatch):
    pages = {
        "https://igod.gov.in/categories": '<a href="https://igod.gov.in/ug/E002/organizations?x=1">Ministries</a><a href="https://igod.gov.in/ug/categories">more</a>',
        "https://igod.gov.in/ug/categories": '<a href="https://igod.gov.in/ug/E002/organizations/">  </a><a href="https://igod.gov.in/ug/E003/organizations">Depts</a>',
        "https://igod.gov.in/sg/states": '<a href="https://igod.gov.in/sg/UP/E01/organizations">UP</a>',
    }
    monkeypatch.setattr(G, "SEEDS", ["https://igod.gov.in/categories", "https://igod.gov.in/sg/states", "https://igod.gov.in/missing"])
    monkeypatch.setattr(G, "get", lambda url, **kw: Resp(pages[url]) if url in pages else None)
    got = G.discover_listings()
    assert got == {"https://igod.gov.in/ug/E002/organizations": "Ministries", "https://igod.gov.in/ug/E003/organizations": "Depts",
                   "https://igod.gov.in/sg/UP/E01/organizations": "UP"}


def test_crawl_listing_lazy_load_and_classification(G, monkeypatch):
    url = "https://igod.gov.in/sg/UP/E01/organizations"
    first = ("var count='7'; var items_on_first_page = '3';" + row_html("A") + row_html("B") + row_html("C"))
    calls = []

    def fake_get(u, **kw):
        calls.append((u, kw.get("params"), (kw.get("headers") or {}).get("Referer")))
        if u == url:
            return Resp(first)
        start = int(u.rsplit("/", 2)[-2])
        return Resp("".join(row_html(f"R{start + i}") for i in range(int(u.rsplit("/", 1)[-1]))))
    monkeypatch.setattr(G, "get", fake_get)
    rows = G.crawl_listing(url, "Dept label")
    assert [r["name"] for r in rows] == ["A", "B", "C", "R3", "R4", "R5", "R6"]
    assert [c[0].rsplit("/", 2)[-2:] for c in calls[1:]] == [["3", "5"], ["8", "2"]] or [c[0] for c in calls[1:]] == [url + "_list_more/3/4"]
    r = rows[0]
    assert (r["branch"], r["state"], r["category_code"], r["category"]) == ("sg", "UP", "E01", "Dept label")
    assert calls[1][1] == {"keyword": ""} and calls[1][2] == url


def test_crawl_listing_chunks_of_five_and_stop_conditions(G, monkeypatch, capsys):
    url = "https://igod.gov.in/ug/E002/organizations"
    first = "var count='12'; var items_on_first_page = '2';" + row_html("A") + row_html("B")
    seen = []

    def fake_get(u, **kw):
        if u == url:
            return Resp(first)
        seen.append(u)
        if len(seen) == 2:
            return None                                  # lazy load fails -> stop
        return Resp("".join(row_html(f"X{len(seen)}{i}") for i in range(5)))
    monkeypatch.setattr(G, "get", fake_get)
    rows = G.crawl_listing(url, "L")
    assert seen == [f"{url}_list_more/2/5", f"{url}_list_more/7/5"] and len(rows) == 7
    assert "lazy-load stopped at 7/12" in capsys.readouterr().err
    assert rows[0]["state"] == "" and rows[0]["branch"] == "ug" and rows[0]["category_code"] == "E002"
    monkeypatch.setattr(G, "get", lambda u, **kw: None)
    assert G.crawl_listing(url, "L") == []
    # a lazy-load answer without result rows also stops
    monkeypatch.setattr(G, "get", lambda u, **kw: Resp(first) if u == url else Resp("<p>nothing</p>"))
    assert len(G.crawl_listing(url, "L")) == 2
    # no page variables at all -> only the static rows
    monkeypatch.setattr(G, "get", lambda u, **kw: Resp(row_html("only")))
    assert [r["name"] for r in G.crawl_listing(url, "L")] == ["only"]


def test_main_dedups_and_writes_csv(G, repo, monkeypatch, capsys):
    monkeypatch.setattr(G, "discover_listings", lambda: {"u2": "b", "u1": "a"})
    mk = lambda name: {"branch": "ug", "state": "", "category_code": "E", "category": "c", "name": name, "igod_org_id": "", "website": "", "listing_url": "u"}
    monkeypatch.setattr(G, "crawl_listing", lambda url, label: [mk("A"), mk("A"), mk("B" + label)])
    G.main()
    rows = read(repo / "data/organizations_index.csv", keep_default_na=False)
    assert list(rows.name) == ["A", "Ba", "Bb"]                        # listings processed in sorted order; exact duplicates collapsed
    assert "wrote 3 rows" in capsys.readouterr().err


# ================================================================== igod_org_details
@pytest.fixture
def H(load, monkeypatch):
    m = load("igod_org_details")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def test_deobfuscate_and_clean(H):
    assert H.deobfuscate("secy[dot]moc [AT] nic [dot]in ") == "secy.moc@nic.in"
    assert H.clean("  a&amp;b \n c ") == "a&b c" and H.clean(None) == ""


PAGE = """<html><head><title>Foo : Organization Details : Ministry of Commerce</title></head><body>
Contact Details
Address: Udyog Bhawan
 New Delhi
Phone No: 011-2301
Fax: 011-2302
Email: a[at]gov[dot]in
Social Media: x
Website: https://commerce.gov.in
Quick Links
<table>
<tr><td>Amit Kumar</td><td>Secretary</td><td>Policy</td><td><a href="tel:011-1">011-1</a><a href="tel:011-2">011-2</a> Address: Room 1</td><td>amit[at]gov[dot]in</td></tr>
<tr><td>Bina Rao</td><td>Director</td><td>Admin</td><td>no phone</td><td><a href="mailto:bina@gov.in"></a></td></tr>
<tr><td>short</td><td>row</td></tr>
</table>
<script>var count='3';</script></body></html>"""


def test_parse_contact_block(H):
    from bs4 import BeautifulSoup
    c = H.parse_contact_block(BeautifulSoup(PAGE, "html.parser"))
    assert c == {"address": "Udyog Bhawan New Delhi", "phone": "011-2301", "fax": "011-2302", "email": "a@gov.in",
                 "website": "https://commerce.gov.in", "social": ""}
    empty = H.parse_contact_block(BeautifulSoup("<p>nothing</p>", "html.parser"))
    assert empty["email"] == "" and set(empty) == {"address", "phone", "fax", "email", "website", "social"}


def test_parse_officials_rows(H):
    rows = H.parse_officials_rows(PAGE)
    assert [r["name"] for r in rows] == ["Amit Kumar", "Bina Rao"]
    a = rows[0]
    assert a["phones"] == "011-1, 011-2" and a["office_address"] == "Room 1" and a["email"] == "amit@gov.in" and a["designation"] == "Secretary"
    assert rows[1]["email"] == "bina@gov.in" and rows[1]["office_address"] == ""      # empty cell text falls back to the mailto: href


def test_fetch_org_paginates_list_contacts(H, monkeypatch):
    more = ('<table><tr><td>Chitra Das</td><td>JS</td><td>Law</td><td>x</td><td>c@gov.in</td></tr></table>')
    seen = []

    def fake_get(url, **kw):
        seen.append(url)
        if url.endswith("/organization/ORG1"):
            return Resp(PAGE)
        return Resp(more)
    monkeypatch.setattr(H, "get", fake_get)
    contact, officials, canonical = H.fetch_org("ORG1")
    assert canonical == "Ministry of Commerce" and contact["phone"] == "011-2301"
    assert [o["name"] for o in officials] == ["Amit Kumar", "Bina Rao", "Chitra Das"]
    assert seen[1].endswith("/organization/ORG1/list_contacts/2/1")
    # stops when the lazy endpoint fails or returns nothing
    monkeypatch.setattr(H, "get", lambda url, **kw: Resp(PAGE) if url.endswith("ORG1") else None)
    assert len(H.fetch_org("ORG1")[1]) == 2
    monkeypatch.setattr(H, "get", lambda url, **kw: Resp(PAGE) if url.endswith("ORG1") else Resp("<p>none</p>"))
    assert len(H.fetch_org("ORG1")[1]) == 2
    monkeypatch.setattr(H, "get", lambda url, **kw: None)
    assert H.fetch_org("ORG1") == (None, [], None)
    # no title with 3 parts -> no canonical name; count defaults to the rows found
    monkeypatch.setattr(H, "get", lambda url, **kw: Resp("<title>x</title><table><tr><td>N One</td><td>D</td><td>V</td><td>c</td></tr></table>"))
    c, offs, canon = H.fetch_org("ORG1")
    assert canon is None and len(offs) == 1


def test_get_retry(H, monkeypatch):
    monkeypatch.setattr(H.session, "get", lambda url, timeout, **kw: (_ for _ in ()).throw(requests.Timeout("t")))
    assert H.get("http://u") is None


def test_main_writes_contacts_and_officials(H, repo, monkeypatch, capsys):
    write_csv(repo / "data/organizations_index.csv", [
        dict(branch="ug", state="", name="Org One", igod_org_id="A1"),
        dict(branch="sg", state="UP", name="Org Two", igod_org_id="B2"),
        dict(branch="sg", state="UP", name="No detail", igod_org_id=""),
        dict(branch="ug", state="", name="Dup", igod_org_id="A1")])
    def fake_fetch(oid):
        if oid == "B2":
            return None, [], None
        return {"address": "a", "phone": "p", "fax": "f", "email": "e", "website": "w", "social": ""}, [
            {"name": "N", "designation": "D", "division": "dv", "phones": "1", "office_address": "o", "email": "e"}], "Canonical One"
    monkeypatch.setattr(H, "fetch_org", fake_fetch)
    H.main()
    c = read(repo / "data/org_contacts.csv", keep_default_na=False)
    o = read(repo / "data/officials.csv", keep_default_na=False)
    assert list(c.org_name) == ["Canonical One"] and list(c.igod_org_id) == ["A1"]
    assert list(o.columns) == ["igod_org_id", "org_name", "branch", "state", "name", "designation", "division", "phones", "office_address", "email"]
    assert len(o) == 1 and o.iloc[0].org_name == "Canonical One"
    assert "[2/2] Org Two: 0 officials" in capsys.readouterr().err
