"""scripts/generate_outreach_materials.py and scripts/build_dashboard.py"""
import csv
import json
import re

import pytest

from helpers import read, write_csv

# ================================================================== outreach
COLS = ["priority", "policy", "days_remaining", "deadline_date", "contact_name", "designation", "email", "phones", "organization",
        "contact_type", "outreach_channel", "follow_up_days"]


@pytest.fixture
def O(load):
    return load("generate_outreach_materials")


@pytest.fixture
def urgent(repo):
    rows = [
        dict(priority="2", policy="Scheme (A/B)", days_remaining="20", deadline_date="2026-12-31", contact_name="Asha Rao", designation="Program Director",
             email="asha@gov.in", phones="11", organization="Org", contact_type="EOI Program Director", outreach_channel="Email", follow_up_days="3"),
        dict(priority="2", policy="Scheme (A/B)", days_remaining="20", deadline_date="2026-12-31", contact_name="Bhim Das", designation="Senior Ministry Official",
             email="", phones="", organization="Org", contact_type="Senior Ministry", outreach_channel="Phone", follow_up_days=""),
        dict(priority="1", policy="Other Scheme", days_remaining="75", deadline_date="2027-02-01", contact_name="Chitra Nair", designation="Technical",
             email="c@gov.in", phones="22", organization="Org2", contact_type="Technical Lead", outreach_channel="", follow_up_days=""),
        dict(priority="5", policy="Late Scheme", days_remaining="200", deadline_date="2027-09-01", contact_name="Dev Roy", designation="Prog",
             email="d@gov.in", phones="33", organization="O", contact_type="Program Director", outreach_channel="Email", follow_up_days="7"),
        dict(priority="9", policy="", days_remaining="1", deadline_date="x", contact_name="No Policy", designation="", email="", phones="", organization="",
             contact_type="", outreach_channel="", follow_up_days=""),
    ]
    write_csv(repo / "data/urgent_outreach_contacts.csv", rows, COLS)
    return rows


def test_load_urgent_contacts(O, repo, capsys):
    assert O.load_urgent_contacts() == []
    assert "File not found" in capsys.readouterr().out


def test_generate_email_drafts_per_program(O, urgent, repo):
    contacts = O.load_urgent_contacts()
    files = O.generate_email_drafts(contacts)
    assert set(files) == {"Scheme (A/B)", "Other Scheme", "Late Scheme"}                  # contacts without a policy are ignored
    out = repo / "reports/outreach"
    names = sorted(p.name for p in out.glob("email_*.txt"))
    assert names == ["email_priority_01_other_scheme.txt", "email_priority_02_scheme_a_b.txt", "email_priority_05_late_scheme.txt"]
    t = (out / "email_priority_02_scheme_a_b.txt").read_text(encoding="utf-8")
    assert "URGENT OUTREACH EMAIL - PRIORITY 2" in t and "Days Remaining: 20" in t and "Application Deadline: 2026-12-31" in t
    assert "Name: Asha Rao" in t and "Dear Asha," in t and "Subject: Scheme (A/B) Application Support - Deadline 2026-12-31 (20 days)" in t
    assert "2. Bhim Das (Senior Ministry Official)" in t and "When: Phone | Follow-up:  days" in t         # a blank CSV cell is kept as '' (the '7' default only applies to a missing column)
    assert "1. Asha Rao" not in t.split("SECONDARY CONTACTS")[1]                                          # the EOI contact is not repeated as secondary


def test_email_draft_without_eoi_contact_has_no_primary_block(O, urgent, repo):
    O.generate_email_drafts(O.load_urgent_contacts())
    t = (repo / "reports/outreach/email_priority_01_other_scheme.txt").read_text(encoding="utf-8")
    assert "EMAIL DRAFT:" not in t and "1. Chitra Nair (Technical)" in t


def test_tracking_sheet_columns_and_status(O, urgent, repo, capsys):
    path = O.generate_excel_tracking_sheet(O.load_urgent_contacts())
    rows = list(csv.reader(open(path, encoding="utf-8")))
    assert rows[0][:5] == ["Priority", "Program", "Days Remaining", "Deadline", "Contact Name"] and len(rows[0]) == 17
    assert len(rows) == 6 and all(len(r) == 17 for r in rows)
    first = rows[1]
    assert first[0] == "2" and first[1] == "Scheme (A/B)" and first[6] == "asha@gov.in" and first[9] == "Email"
    assert first[10] == "" and first[15] == "🔴 TODO" and first[13] == "3"
    assert "Tracking sheet" in capsys.readouterr().out


def test_contact_summary_urgency_bands_and_labels(O, urgent, repo):
    path = O.generate_contact_summary(O.load_urgent_contacts())
    t = open(path, encoding="utf-8").read()
    assert "🔴 CRITICAL PRIORITY 2: SCHEME (A/B)" in t                      # 20 days <= 30
    assert "🟡 HIGH PRIORITY 1: OTHER SCHEME" in t                          # 75 days <= 90
    assert "🟢 NORMAL PRIORITY 5: LATE SCHEME" in t                         # 200 days
    assert "📱 PROGRAM LEAD" in t and "👤 MINISTRY" in t and "🔧 TECHNICAL" in t
    assert "Email: asha@gov.in" in t and t.count("Email:") == 3 and "Phone: 11" in t
    assert t.index("LATE SCHEME") < t.index("OTHER SCHEME") < t.index("SCHEME (A/B)")      # programs sorted alphabetically


@pytest.mark.parametrize("days,label", [("30", "CRITICAL"), ("31", "HIGH"), ("90", "HIGH"), ("91", "NORMAL")])
def test_summary_urgency_boundaries(O, repo, days, label):
    write_csv(repo / "data/urgent_outreach_contacts.csv", [dict(priority="1", policy="P", days_remaining=days, deadline_date="d", contact_name="N")], COLS)
    assert label in open(O.generate_contact_summary(O.load_urgent_contacts()), encoding="utf-8").read()


def test_main(O, urgent, repo, capsys):
    assert O.main() == 0
    out = capsys.readouterr().out
    assert "Generating Outreach Materials" in out and "✓ Scheme (A/B)" in out and "All materials generated in" in out
    assert (repo / "reports/outreach/outreach_tracking_sheet.csv").exists() and (repo / "reports/outreach/contact_summary.txt").exists()


def test_main_without_contacts(O, repo, capsys):
    assert O.main() == 1
    assert "No urgent contacts loaded" in capsys.readouterr().out


# ================================================================== dashboard
@pytest.fixture
def B(load):
    return load("build_dashboard")


def _payload(html):
    m = re.search(r"const D=(\{.*?\});\nconst VIEWS", html, re.S)
    return json.loads(m.group(1))


def test_rows_missing_file(B):
    assert B.rows("nothing.csv") == []


def test_main_builds_payload(B, repo, capsys):
    write_csv(repo / "data/organizations_index.csv", [
        dict(name="Ministry A", branch="ug", state="", category="Min", website="https://a.in", igod_org_id="1"),
        dict(name="Ministry A", branch="ug", state="", category="Min", website="https://a.in", igod_org_id="1"),
        dict(name="Dept B", branch="sg", state="UP", category="Dept", website="", igod_org_id=""),
    ])
    write_csv(repo / "data/officials.csv", [
        dict(name="Amit", designation="Dir", org_name="Ministry A", state="", phones="1", email="a@x.in"),
        dict(name="Bina", designation="JS", org_name="Dept B", state="UP", phones="2", email="")])
    write_csv(repo / "data/ministry_officials.csv", [dict(name="C", designation="S", ministry="Ministry A", division="d", room="1", phones="3", email="c@x.in")])
    write_csv(repo / "data/org_contacts.csv", [dict(org_name="Ministry A", address="addr", phone="p", email="e", website="w")])
    write_csv(repo / "data/policy_contacts.csv", [
        dict(instrument="PLI", offering_entity="E", tier="National", status="open", contact_name="X", designation="D", email="x@y.in", source_url="http://p"),
        dict(instrument="PLI", offering_entity="E", tier="National", status="open", contact_name="Y", designation="D", email="", source_url="http://p")])
    write_csv(repo / "data/pib_ministry_contacts.csv", [
        dict(ministry="M1", releases_6y_total="10", releases_2024="4", releases_2025="6", releases_90d="2", contact_name="P1", designation="Sec"),
        dict(ministry="M1", releases_6y_total="10", releases_2024="4", releases_2025="6", releases_90d="2", contact_name="P2", designation="Dir"),
        dict(ministry="M1", releases_6y_total="10", releases_2024="4", releases_2025="6", releases_90d="2", contact_name="P3", designation="D3"),
        dict(ministry="M1", releases_6y_total="10", releases_2024="4", releases_2025="6", releases_90d="2", contact_name="P4", designation="D4"),
        dict(ministry="M2", releases_6y_total="50", releases_2024="", releases_2025="50", releases_90d="", contact_name="", designation="")])
    B.main()
    html = (repo / "dashboard/index.html").read_text()
    d = _payload(html)
    assert d["stats"] == {"orgs": 2, "withDetail": 1, "officials": 2, "emails": 1, "states": 1, "openPolicies": 1, "deepOfficials": 1}
    assert d["officials"][0] == ["Amit", "Dir", "Ministry A", "Centre", "1", "a@x.in"] and d["officials"][1][3] == "UP"
    assert d["pibYears"] == ["2024", "2025"]
    assert [row[0] for row in d["pib"]] == ["M2", "M1"]                                         # sorted by 6-year total, descending
    assert d["pib"][1] == ["M1", 10, 4, 6, 2, "P1 (Sec); P2 (Dir); P3 (D3)"]                     # at most 3 contacts
    assert d["pib"][0] == ["M2", 50, 0, 50, 0, ""]                                               # blanks become 0
    assert len(d["policies"]) == 2 and d["orgContacts"] == [["Ministry A", "addr", "p", "e", "w"]]
    assert "__DATA__" not in html and "<title>India Government Yellow Pages</title>" in html
    assert "wrote " in capsys.readouterr().out


def test_main_with_no_data_files(B, repo):
    B.main()
    d = _payload((repo / "dashboard/index.html").read_text())
    assert d["stats"]["orgs"] == 0 and d["pib"] == [] and d["pibYears"] == []
