"""Characterisation tests for the pure helpers in scripts/link_policy_contacts.py."""
import link_policy_contacts as L


def test_norm_strips_noise_and_applies_aliases():
    assert L.norm("The Ministry of  Finance, Govt of India") == "ministry of finance"
    assert L.norm("MeitY") == "ministry of electronics and information technology"
    assert L.norm(None) == ""


def test_rank_of_first_matching_title():
    assert L.rank_of("Cabinet Minister") == 0
    assert L.rank_of("Joint Secretary") == L.RANK.index("secretary")
    assert L.rank_of("Director General") == L.RANK.index("director general")
    assert L.rank_of("Peon") == len(L.RANK)


def test_is_open():
    assert L.is_open({"status": "Active"})
    assert not L.is_open({"status": "Closed"})
    assert not L.is_open({"status": "lapsed"})
    assert L.is_open({"status": "", "verified_on_site": True})
    assert not L.is_open({})


def test_match_org_exact_contains_fuzzy():
    by_org = {"ministry of power": [], "ministry of coal": []}
    assert L.match_org("Ministry of Power", by_org) == "ministry of power"
    assert L.match_org("coal", by_org) == "ministry of coal"
    assert L.match_org("Ministry of Powr", by_org) == "ministry of power"
    assert L.match_org("zzzz qqqq", by_org) is None
