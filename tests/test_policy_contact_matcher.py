"""Characterisation tests for scripts/policy_contact_matcher.py (synthetic rows, no I/O)."""
from datetime import datetime

import policy_contact_matcher as m

TODAY = datetime(2026, 6, 15)
WINDOWS = {
    "Open Scheme": (datetime(2026, 6, 1), datetime(2026, 6, 30)),
    "Soon Scheme": (datetime(2026, 7, 1), datetime(2026, 7, 10)),
    "Far Scheme": (datetime(2026, 12, 1), datetime(2026, 12, 31)),
    "Old Scheme": (datetime(2025, 1, 1), datetime(2025, 2, 1)),
}


def _contacts():
    return [{"instrument": n, "contact_name": "X"} for n in
            ("Open Scheme", "Soon Scheme", "Far Scheme", "Old Scheme", "Undated")]


def test_window_status_branches():
    s, e = datetime(2026, 6, 1), datetime(2026, 6, 30)
    assert m.get_window_status(s, e, datetime(2026, 5, 30)) == ("OPENING_SOON", 2)
    assert m.get_window_status(s, e, TODAY) == ("ACTIVE", 15)
    assert m.get_window_status(s, e, datetime(2026, 7, 5)) == ("CLOSED", 5)


def test_filter_active_only():
    out = m.filter_by_active_windows(_contacts(), WINDOWS, True, 30, today=TODAY)
    assert [c["instrument"] for c in out] == ["Open Scheme"]
    assert out[0]["window_status"] == "ACTIVE" and out[0]["days_info"] == "15"


def test_filter_include_upcoming_and_nodata():
    out = m.filter_by_active_windows(_contacts(), WINDOWS, False, 30, today=TODAY)
    status = {c["instrument"]: c["window_status"] for c in out}
    assert status == {"Open Scheme": "ACTIVE", "Soon Scheme": "OPENING_SOON", "Undated": "NO_DATA"}


def test_parse_windows_skips_bad_rows():
    rows = [
        {"instrument": "A", "application_start_date": "2026-01-01", "application_end_date": "2026-02-01"},
        {"instrument": "B", "application_start_date": "bad", "application_end_date": "2026-02-01"},
        {"instrument": "", "application_start_date": "2026-01-01", "application_end_date": "2026-02-01"},
        {"instrument": "C", "application_start_date": "", "application_end_date": "2026-02-01"},
    ]
    assert list(m.parse_windows(rows)) == ["A"]


def test_seniority_first_listed_title_wins():
    # "minister of state" contains "minister", which is listed first -> rank 1 (existing behaviour).
    assert m.seniority_rank({"designation": "Minister of State"}) == 1
    assert m.seniority_rank({"designation": "Joint Secretary"}) == 2  # contains "secretary"
    assert m.seniority_rank({"designation": "Director"}) == 6
    assert m.seniority_rank({"designation": "Clerk"}) == 99
    assert m.seniority_rank({}) == 99


def test_rank_is_stable_sort():
    cs = [{"designation": "Director", "n": 1}, {"designation": "Secretary", "n": 2},
          {"designation": "Director", "n": 3}]
    assert [c["n"] for c in m.rank_contacts_by_seniority(cs)] == [2, 1, 3]


def test_group_and_open_policies():
    cs = [{"instrument": " A ", "status": "Open"}, {"instrument": "B", "status": "closed"},
          {"instrument": "", "status": "open"}, {"instrument": "A", "status": "x"}]
    assert list(m.group_by_policy(cs)) == ["A", "B"]
    assert m.get_open_policies(cs) == ["A"]


def test_find_unassigned_policies():
    cs = [{"instrument": "A", "status": "open", "contact_name": "", "instrument_type": "PLI"},
          {"instrument": "B", "status": "open", "contact_name": "Z"}]
    assert m.find_unassigned_policies(cs) == [("A", "PLI")]


def test_parse_args():
    assert m.parse_args(["prog"]) == (False, 30)
    assert m.parse_args(["prog", "--active-only", "--days-ahead", "7"]) == (True, 7)
    assert m.parse_args(["prog", "--days-ahead", "x"]) == (False, 30)


def test_main_with_synthetic_files(tmp_path, monkeypatch, capsys):
    (tmp_path / "policy_contacts.csv").write_text(
        "instrument,status,contact_name,designation,offering_entity\n"
        "Scheme A,open,Test Officer,Director,Test Ministry\n", encoding="utf-8")
    monkeypatch.setattr(m, "POLICY_CONTACTS_FILE", tmp_path / "policy_contacts.csv")
    monkeypatch.setattr(m, "POLICY_WINDOWS_FILE", tmp_path / "none.csv")
    monkeypatch.setattr(m, "POLICY_EOI_CONTACTS_FILE", tmp_path / "none2.csv")
    assert m.main(["prog"]) == 0
    out = capsys.readouterr().out
    assert "SCHEME A" in out and "Test Officer" in out and "Analysis complete" in out


def test_main_no_data_returns_1(tmp_path, monkeypatch):
    for name in ("POLICY_CONTACTS_FILE", "POLICY_WINDOWS_FILE", "POLICY_EOI_CONTACTS_FILE"):
        monkeypatch.setattr(m, name, tmp_path / "missing.csv")
    assert m.main(["prog"]) == 1
