"""scripts/policy_contact_matcher.py and scripts/link_policy_contacts.py"""
import json
import sqlite3
import sys
from datetime import date, datetime, timedelta

import pytest

from helpers import read, write_csv


# ================================================================== policy_contact_matcher
@pytest.fixture
def M(load):
    return load("policy_contact_matcher")


def _contacts(repo):
    write_csv(repo / "data/policy_contacts.csv", [
        dict(instrument="PLI Scheme", offering_entity="Electronics", status="open", instrument_type="PLI", source_url="http://pli",
             contact_name="Amit Kumar", designation="Secretary", division="Div", phones="11, 22", email="a@gov.in"),
        dict(instrument="PLI Scheme", offering_entity="Electronics", status="open", instrument_type="PLI", source_url="http://pli",
             contact_name="Bina Rao", designation="Director", division="", phones="", email=""),
        dict(instrument="Old Scheme", offering_entity="Agri", status="closed", instrument_type="grant", source_url="",
             contact_name="", designation="", division="", phones="", email=""),
        dict(instrument="Open No Contact", offering_entity="Agri", status="Open (verified)", instrument_type="grant", source_url="",
             contact_name="", designation="", division="", phones="", email=""),
        dict(instrument="", offering_entity="x", status="open", instrument_type="", source_url="", contact_name="Ghost", designation="", division="", phones="", email=""),
    ])


def test_load_policy_contacts_missing_and_present(M, repo, capsys):
    assert M.load_policy_contacts() == []
    assert "File not found" in capsys.readouterr().out
    _contacts(repo)
    assert len(M.load_policy_contacts()) == 5


def test_load_policy_windows_parses_and_skips_bad_rows(M, repo):
    assert M.load_policy_windows() == {}
    write_csv(repo / "data/policy_windows.csv", [
        dict(instrument=" PLI Scheme ", application_start_date="2026-01-01", application_end_date="2026-12-31"),
        dict(instrument="Bad Dates", application_start_date="01/01/2026", application_end_date="2026-12-31"),
        dict(instrument="Missing End", application_start_date="2026-01-01", application_end_date=""),
        dict(instrument="", application_start_date="2026-01-01", application_end_date="2026-02-01"),
    ])
    w = M.load_policy_windows()
    assert w == {"PLI Scheme": (datetime(2026, 1, 1), datetime(2026, 12, 31))}


def test_load_eoi_contacts_normalises(M, repo):
    assert M.load_eoi_contacts() == []
    write_csv(repo / "data/policy_eoi_contacts.csv", [
        dict(instrument=" EOI Thing ", contact_name=" N ", designation="D", division=" Div ", email="e@x.in", phones="1", source="", source_url="u"),
        dict(instrument="", contact_name="skip"),
    ], ["instrument", "contact_name", "designation", "division", "email", "phones", "source", "source_url"])
    e = M.load_eoi_contacts()
    assert len(e) == 1
    assert e[0]["instrument"] == "EOI Thing" and e[0]["contact_name"] == "N" and e[0]["offering_entity"] == "Div"
    assert e[0]["status"] == "open (EOI)" and e[0]["instrument_type"] == "contact from official notification"
    assert e[0]["source"] == ""        # a present-but-empty source column is kept (default only applies when the column is absent)


def test_get_window_status_boundaries(M):
    s, e = datetime(2026, 1, 10), datetime(2026, 1, 20)
    assert M.get_window_status(s, e, datetime(2026, 1, 5)) == ("OPENING_SOON", 5)
    assert M.get_window_status(s, e, s) == ("ACTIVE", 10)                       # the start instant is active
    assert M.get_window_status(s, e, e) == ("ACTIVE", 0)                        # the end instant is still active
    assert M.get_window_status(s, e, e + timedelta(seconds=1)) == ("CLOSED", 0)
    assert M.get_window_status(s, e, datetime(2026, 2, 1)) == ("CLOSED", 12)
    assert M.get_window_status(s, e)[0] == "CLOSED"                             # default 'now' (2026-11 or later)


def test_filter_by_active_windows(M):
    now = datetime.now()
    windows = {
        "active": (now - timedelta(days=5), now + timedelta(days=5)),
        "soon": (now + timedelta(days=10, hours=1), now + timedelta(days=60)),
        "later": (now + timedelta(days=100), now + timedelta(days=200)),
        "closed": (now - timedelta(days=100), now - timedelta(days=50)),
    }
    contacts = [{"instrument": k} for k in ("active", "soon", "later", "closed", "nodata")] + [{"instrument": ""}, {}]
    res = M.filter_by_active_windows(contacts, windows, active_only=True)
    assert [c["instrument"] for c in res] == ["active"] and res[0]["window_status"] == "ACTIVE" and res[0]["days_info"] == "4"
    res = M.filter_by_active_windows(contacts, windows, active_only=False, days_ahead=30)
    assert [c["instrument"] for c in res] == ["active", "soon", "nodata"]
    assert res[1]["window_status"] == "OPENING_SOON" and res[2]["window_status"] == "NO_DATA" and res[2]["days_info"] == "N/A"
    res = M.filter_by_active_windows(contacts, windows, active_only=False, days_ahead=5)
    assert "soon" not in [c["instrument"] for c in res]
    assert "window_status" not in contacts[0]                                    # input rows are copied, not mutated


def test_group_and_open_policies(M):
    cs = [{"instrument": " A ", "status": "Open"}, {"instrument": "A", "status": "x"}, {"instrument": "B", "status": "closed"},
          {"instrument": "C", "status": "open (EOI)"}, {"instrument": "", "status": "open"}, {"status": "open"}]
    g = M.group_by_policy(cs)
    assert set(g) == {"A", "B", "C"} and len(g["A"]) == 2
    assert M.get_open_policies(cs) == ["A", "C"]


def test_rank_contacts_by_seniority(M):
    cs = [{"designation": "Director", "n": 1}, {"designation": "Minister of State", "n": 2}, {"designation": "Clerk", "n": 3},
          {"designation": "Minister", "n": 4}, {"designation": "Secretary", "n": 5}, {"n": 6}]
    ranked = [c["n"] for c in M.rank_contacts_by_seniority(cs)]
    assert ranked[0] in (2, 4) and ranked[-2:] == [3, 6] and ranked.index(1) > ranked.index(5)


@pytest.mark.xfail(strict=True, reason="rank_map is scanned in insertion order with substring tests, so 'Minister of State' "
                                       "matches 'minister' (rank 1) and 'Additional/Joint Secretary' match 'secretary' (rank 2) "
                                       "before their own, more specific, entries are reached")
def test_rank_contacts_respects_specific_titles(M):
    cs = [{"designation": "Joint Secretary", "n": "js"}, {"designation": "Secretary", "n": "s"}, {"designation": "Additional Secretary", "n": "as"},
          {"designation": "Minister of State", "n": "mos"}, {"designation": "Minister", "n": "m"}]
    assert [c["n"] for c in M.rank_contacts_by_seniority(cs)] == ["m", "s", "mos", "as", "js"]


def test_printers(M, capsys, repo):
    grouped = {
        "PLI Scheme": [
            {"instrument": "PLI Scheme", "status": "open", "offering_entity": "Electronics", "instrument_type": "PLI", "source_url": "http://pli",
             "window_status": "ACTIVE", "days_info": "4", "contact_name": "Amit Kumar", "designation": "Secretary", "division": "Div", "phones": "11, 22", "email": "a@gov.in"},
            {"instrument": "PLI Scheme", "contact_name": "Bina Rao", "designation": "Director", "email": ""},
            {"instrument": "PLI Scheme", "contact_name": "", "designation": ""},
        ],
        "Soon": [{"status": "open", "window_status": "OPENING_SOON", "days_info": "9", "contact_name": "C D"}],
        "NoData": [{"window_status": "NO_DATA", "contact_name": "E F"}],
        "Empty": [],
    }
    M.print_policy_contact_matrix(grouped)
    out = capsys.readouterr().out
    assert "PLI SCHEME" in out and "APPLICATION WINDOW: OPEN (4 days remaining)" in out and "Opens in 9 days" in out and "No data available" in out
    assert "Phone: 11, 22" in out and "Email: a@gov.in" in out and "Email: [Not available]" in out and "Website: http://pli" in out
    assert "EMPTY" not in out
    M.print_summary_by_sector(grouped)
    out = capsys.readouterr().out
    assert "Electronics\n  • PLI Scheme" in out and "Unknown" in out
    M.print_contact_lookup(grouped)
    out = capsys.readouterr().out
    assert "Amit Kumar\n  Designation: Secretary\n  Email: a@gov.in\n  Policies:\n    • PLI Scheme" in out
    M.print_application_window_template()
    assert "0 open policy instruments identified" in capsys.readouterr().out
    _contacts(repo)
    M.print_missing_contacts()
    out = capsys.readouterr().out
    assert "• Open No Contact" in out and "PLI Scheme" not in out.split("WITHOUT ASSIGNED CONTACTS")[1]
    write_csv(repo / "data/policy_contacts.csv", [dict(instrument="A", status="open", contact_name="X", designation="")])
    M.print_missing_contacts()
    assert "All open policies have assigned contacts" in capsys.readouterr().out


def test_main_paths(M, repo, capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["x"])
    assert M.main() == 1 and "No contacts loaded" in capsys.readouterr().out
    _contacts(repo)
    now = datetime.now()
    write_csv(repo / "data/policy_windows.csv", [dict(instrument="PLI Scheme", application_start_date=(now - timedelta(days=3)).strftime("%Y-%m-%d"),
                                                      application_end_date=(now + timedelta(days=30)).strftime("%Y-%m-%d"))])
    write_csv(repo / "data/policy_eoi_contacts.csv", [dict(instrument="PLI Scheme", contact_name="Eoi Person", designation="Director", division="", email="", phones="", source="", source_url="")])
    monkeypatch.setattr(sys, "argv", ["x", "--active-only", "--days-ahead", "x"])
    assert M.main() == 0
    out = capsys.readouterr().out
    assert "Total contacts (before filter): 6" in out and "Active window policies: 3" in out and "Window data available for 1 policies" in out
    assert "Policies with ACTIVE application windows: 1" in out and "Analysis complete" in out
    monkeypatch.setattr(sys, "argv", ["x", "--days-ahead", "5"])
    assert M.main() == 0
    write_csv(repo / "data/policy_windows.csv", [dict(instrument="Zzz", application_start_date="2020-01-01", application_end_date="2020-02-01")])
    monkeypatch.setattr(sys, "argv", ["x"])
    assert M.main() == 0                                         # windows exist but none match -> everything filtered away
    (repo / "data/policy_windows.csv").unlink()
    assert M.main() == 0                                         # no windows, no filtering


# ================================================================== link_policy_contacts
@pytest.fixture
def L(load):
    return load("link_policy_contacts")


def test_norm_aliases_and_stopwords(L):
    assert L.norm("MeitY") == "ministry of electronics and information technology"
    assert L.norm("Dept of Commerce / DGFT") == "dept of commerce dgft"          # punctuation collapses before the alias lookup, so this alias never fires
    assert L.norm("The Government of India, Ministry of Health & Family Welfare") == "ministry of health and family welfare"
    assert L.norm(None) == "" and L.norm("  A--B  ") == "a b"
    assert L.norm("Home Affairs") == "ministry of home affairs"
    assert L.norm("Dept of Fertilizers") == "ministry of chemicals and fertilizers"


@pytest.mark.xfail(strict=True, reason="norm() strips punctuation to spaces before the ALIASES lookup, so the six alias keys containing "
                                       "'(', ')', '/' or '+' (e.g. 'mod (ddp/drdo)', 'dept of commerce / dgft') can never match")
def test_every_alias_key_is_reachable_through_norm(L):
    dead = [k for k in L.ALIASES if L.norm(k) != L.ALIASES[k]]
    assert dead == [], dead


def test_rank_of_designations(L):
    assert L.rank_of("Cabinet Minister") == 0 and L.rank_of("Minister of State") == 1
    assert L.rank_of("Minister") == 2
    assert L.rank_of("Secretary") == L.RANK.index("secretary")
    assert L.rank_of("Director General") < L.rank_of("Director")
    assert L.rank_of("Peon") == len(L.RANK) and L.rank_of(None) == len(L.RANK) and L.rank_of("") == len(L.RANK)


@pytest.mark.xfail(strict=True, reason="RANK lists 'secretary' before 'additional/joint/under secretary' and rank_of does a plain "
                                       "substring scan, so every kind of Secretary gets the plain Secretary rank")
def test_rank_of_distinguishes_kinds_of_secretary(L):
    assert L.rank_of("Secretary") < L.rank_of("Additional Secretary") < L.rank_of("Joint Secretary") < L.rank_of("Under Secretary")


@pytest.mark.parametrize("inst,expected", [
    ({"status": "Active"}, True), ({"status": "In force till 2030"}, True), ({"status": "closed"}, False),
    ({"status": "lapsed in 2020"}, False), ({"status": "Site down"}, False), ({"status": "unverified"}, False),
    ({"status": "closed but open for review"}, True),                       # an open word beats a closed word
    ({"status": "", "application_status": "applications open"}, True),
    ({"what_companies_get": "A live portal"}, True),
    ({"status": "n/a", "verified_on_site": True}, True), ({"status": "n/a", "verified_on_site": "yes"}, False),
    ({}, False),
])
def test_is_open(L, inst, expected):
    assert L.is_open(inst) is expected


def test_load_officials_and_match_org(L, repo):
    write_csv(repo / "data/officials.csv", [
        dict(org_name="Ministry of Finance", name="B", designation="Director", division="d", phones="", email=""),
        dict(org_name="Ministry of Finance", name="A", designation="Secretary", division="d", phones="", email=""),
        dict(org_name="Ministry of Health and Family Welfare", name="H", designation="Minister", division="", phones="", email=""),
    ])
    by = L.load_officials()
    assert [o["name"] for o in by["ministry of finance"]] == ["A", "B"]          # most senior first
    assert L.match_org("Ministry of Finance", by) == "ministry of finance"
    assert L.match_org("health and family welfare", by) == "ministry of health and family welfare"      # alias hit
    assert L.match_org("ministry of finance (revenue)", by) == "ministry of finance"                      # containment
    assert L.match_org("Ministery of Finnance", by) == "ministry of finance"                              # fuzzy cutoff .75
    assert L.match_org("Totally unrelated xyz", by) is None
    assert L.match_org(None, {}) is None


def _build_pib(path, rows):
    con = sqlite3.connect(str(path))
    con.execute("create table pib_items (ministry text, date text, title text)")
    con.executemany("insert into pib_items values (?,?,?)", rows)
    con.commit()
    con.close()


def test_main_writes_both_outputs(L, repo, monkeypatch, tmp_path, capsys):
    write_csv(repo / "data/officials.csv", [
        dict(org_name="Ministry of Finance", name="A", designation="Secretary", division="d1", phones="1", email="a@x.in"),
        dict(org_name="Ministry of Finance", name="B", designation="Director", division="d2", phones="2", email="b@x.in"),
    ])
    home = tmp_path / "home"
    twin = home / "digital-twin-for-ipa/layers"
    twin.mkdir(parents=True)
    (twin / "13_flat_instrument_index.json").write_text(json.dumps({"instruments": [
        {"instrument": "PLI X", "offering_entity": "Ministry of Finance", "tier": "National", "status": "Active", "instrument_type": "PLI", "source_url": "http://x"},
        {"instrument": "Closed Y", "offering_entity": "Ministry of Finance", "status": "closed"},
        {"instrument": "Unmatched Z", "offering_entity": "Nowhere Dept", "application_status": "open"},
        {"instrument": "Inferred", "offering_entity": "Ministry of Finance", "verified_on_site": True},
    ]}))
    pib_dir = home / "india-trade-sector-policy-recommendations/data"
    pib_dir.mkdir(parents=True)
    today = date.today()
    _build_pib(pib_dir / "pib_index.sqlite", [
        ("Ministry of Finance", today.isoformat(), "Latest"),
        ("Ministry of Finance", (today - timedelta(days=200)).isoformat(), "Older"),
        ("Unknown Ministry", f"{today.year - 5}-02-01", "Ancient"),
        ("Pre-window", f"{today.year - 7}-02-01", "Too old"),
    ])
    monkeypatch.setattr(L, "TWIN", twin / "13_flat_instrument_index.json")
    monkeypatch.setattr(L, "PIB", pib_dir / "pib_index.sqlite")
    L.main()
    pc = read(repo / "data/policy_contacts.csv", keep_default_na=False)
    assert list(pc.instrument) == ["PLI X", "PLI X", "Unmatched Z", "Inferred", "Inferred"]       # 'Closed Y' skipped, top-5 officials per match
    assert list(pc.contact_name[:2]) == ["A", "B"] and pc.status.iloc[3] == "open (inferred)" and pc.matched_org.iloc[2] == ""
    pm = read(repo / "data/pib_ministry_contacts.csv", keep_default_na=False)
    years = [f"releases_{y}" for y in range(today.year - 5, today.year + 1)]
    assert set(years) <= set(pm.columns)
    fin = pm[pm.ministry == "Ministry of Finance"]
    assert len(fin) == 2 and fin.releases_6y_total.iloc[0] == 2 and fin.releases_90d.iloc[0] == 1
    assert fin.latest_release_date.iloc[0] == today.isoformat() and list(fin.contact_name) == ["A", "B"]
    unk = pm[pm.ministry == "Unknown Ministry"].iloc[0]
    assert unk.releases_6y_total == 1 and unk[f"releases_{today.year - 5}"] == 1 and unk.contact_name == ""
    assert "Pre-window" not in set(pm.ministry)
    assert list(pm.ministry)[0] == "Ministry of Finance"                                        # sorted by 6-year volume
    err = capsys.readouterr().err
    assert "instruments: 2 matched, 1 unmatched" in err or "instruments: 2 matched" in err
