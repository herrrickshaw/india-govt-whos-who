import csv
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from src import (
    GraphifyClient, GraphifyOfficialRepository, GraphifyOrganizationRepository, GraphifyPolicyRepository,
    GraphifyPressReleaseRepository,
)
from src.domain import (
    ContactInfo, Designation, Location, Official, OfficialId, Organization, OrganizationId, Policy, PolicyId,
    PolicyStatus, PressRelease,
)


def _w(path, header, rows, bom=False):
    with open(path, "w", newline="", encoding="utf-8-sig" if bom else "utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ------------------------------------------------------------------ GraphifyClient
def test_graphify_nodes_edges_and_ids():
    g = GraphifyClient()
    assert g.get_node("organization:1") is None
    assert g.upsert_node("Organization", "1", {"name": "A"}) is True
    assert g.get_node("organization:1")["properties"]["name"] == "A"
    assert "updated_at" in g.get_node("organization:1")["properties"]
    g.upsert_node("Official", "official:7", {"name": "B"})        # ':' in id is kept verbatim
    assert g.get_node("official:7")["type"] == "Official"
    g.upsert_edge("Organization", "1", "EMPLOYS", "Official", "7", {"rank": 1})
    assert len(g.export_edges()) == 1
    e = g.export_edges()[0]
    assert (e["source"], e["target"], e["type"]) == ("organization:1", "official:7", "EMPLOYS")
    assert "created_at" in e["properties"] and e["properties"]["rank"] == 1
    # same edge again updates in place
    g.upsert_edge("Organization", "1", "EMPLOYS", "Official", "7", {"rank": 2})
    assert len(g.export_edges()) == 1
    assert g.export_edges()[0]["properties"]["rank"] == 2
    assert "updated_at" in g.export_edges()[0]["properties"]
    # different type or target is a new edge; None properties allowed
    g.upsert_edge("Organization", "1", "OFFERS", "Official", "7")
    g.upsert_edge("Organization", "1", "EMPLOYS", "Official", "8")
    assert len(g.export_edges()) == 3


def test_graphify_neighbors_incoming_and_stats():
    g = GraphifyClient()
    g.upsert_node("Organization", "1", {})
    g.upsert_node("Official", "7", {})
    g.upsert_node("Policy", "9", {})
    g.upsert_edge("Organization", "1", "EMPLOYS", "Official", "7", {"rank": 3})
    g.upsert_edge("Organization", "1", "OFFERS", "Policy", "9")
    g.upsert_edge("Organization", "1", "OFFERS", "Policy", "404")      # dangling target is skipped
    nb = g.get_neighbors("organization:1")
    assert {n["node"]["id"] for n in nb} == {"official:7", "policy:9"}
    assert [n["edge_properties"]["rank"] for n in g.get_neighbors("organization:1", "EMPLOYS")] == [3]
    assert g.get_neighbors("organization:1", "NOPE") == []
    assert g.get_neighbors("official:7") == []
    inc = g.get_incoming_edges("official:7")
    assert [i["node"]["id"] for i in inc] == ["organization:1"]
    assert g.get_incoming_edges("official:7", "OFFERS") == []
    assert g.get_incoming_edges("official:7", "EMPLOYS")[0]["edge_type"] == "EMPLOYS"
    st = g.get_stats()
    assert st["total_nodes"] == 3 and st["total_edges"] == 3
    assert st["node_counts_by_type"] == {"Organization": 1, "Official": 1, "Policy": 1}
    assert st["edge_counts_by_type"] == {"EMPLOYS": 1, "OFFERS": 2}
    assert len(g.export_nodes()) == 3


def test_graphify_metadata_query_commit():
    g = GraphifyClient("x.json")
    assert g.graph_file == "x.json"
    assert g.get_metadata("official_sync_timestamp") is None
    assert g.get_metadata("nope") is None
    g.set_metadata("k", 5)
    assert g.get_metadata("k") == 5
    assert g.query("MATCH (n)") == []
    assert g.commit() is True


# ------------------------------------------------------------------ organizations
@pytest.fixture
def org_repo(tmp_path):
    _w(tmp_path / "organizations_index.csv", ["id", "name", "branch", "state", "website", "category"], [
        ["1", "Ministry Alpha", "ug", "DL", "https://alpha.gov.in", "E002"],
        ["2", "State Beta", "sg", "UP", "", "E003"],
        ["3", "ab", "ug", "DL", "", ""],                      # name too short -> skipped
        ["4", "Bad Branch", "zz", "DL", "", ""],              # invalid branch -> skipped
        ["5", "Bad Site", "ug", "DL", "not-a-url", ""],       # invalid website -> skipped
    ], bom=True)
    _w(tmp_path / "org_contacts.csv", ["organization_id", "address", "phone", "fax", "email", "website"], [
        ["1", "Addr", "111", "222", "a@alpha.gov.in", "https://other.in"],
        ["2", "", "", "", "", "https://beta.gov.in"],
    ], bom=True)
    return GraphifyOrganizationRepository(GraphifyClient(), tmp_path)


def test_org_repo_loads_and_skips_invalid(org_repo):
    assert {o.org_id.value for o in org_repo.find_all()} == {"1", "2"}
    a = org_repo.find_by_id(OrganizationId("1"))
    assert a.contact_info.website == "https://alpha.gov.in"      # index website wins over contact website
    assert (a.contact_info.address, a.contact_info.phone, a.contact_info.fax, a.contact_info.email) == \
        ("Addr", "111", "222", "a@alpha.gov.in")
    assert org_repo.find_by_id(OrganizationId("2")).contact_info.website == "https://beta.gov.in"
    assert org_repo.find_by_id(OrganizationId("99")) is None
    assert org_repo.find_by_name("MINISTRY ALPHA").org_id.value == "1"
    assert org_repo.find_by_name("nope") is None
    assert [o.org_id.value for o in org_repo.find_by_branch("sg")] == ["2"]
    assert [o.org_id.value for o in org_repo.find_by_state("DL")] == ["1"]
    assert org_repo.find_by_branch("int") == [] and org_repo.find_by_state("ZZ") == []


def test_org_repo_defaults_and_missing_files(tmp_path):
    r = GraphifyOrganizationRepository(GraphifyClient(), tmp_path)      # no csv at all
    assert r.find_all() == []
    _w(tmp_path / "organizations_index.csv", ["igod_id", "name"], [["7", "Dept Gamma"]])
    r = GraphifyOrganizationRepository(GraphifyClient(), tmp_path)      # igod_id column, no contacts file
    o = r.find_by_id(OrganizationId("7"))
    assert (o.location.branch, o.location.state) == ("ug", "IN")


def test_org_repo_save_and_delete(org_repo):
    g = org_repo.graphify
    o = Organization(OrganizationId("10"), "New Org", Location("jud", "KA"), ContactInfo(email="x@y.in"), "cat")
    org_repo.save(o)
    assert org_repo.find_by_name("new org") is o
    node = g.get_node("organization:10")
    assert node["properties"]["branch"] == "jud" and node["properties"]["contact_email"] == "x@y.in"
    org_repo.delete(OrganizationId("10"))
    assert org_repo.find_by_id(OrganizationId("10")) is None and org_repo.find_by_name("new org") is None
    org_repo.delete(OrganizationId("not-there"))        # no-op, no error


@pytest.mark.xfail(strict=True, raises=KeyError,
                   reason="delete() does `del self._orgs_by_name[name]`, but two orgs sharing a name leave only one "
                          "name key, so the second delete raises KeyError")
def test_org_repo_delete_duplicate_name_is_safe(tmp_path):
    """Two organisations may share a name; deleting both must not raise KeyError."""
    _w(tmp_path / "organizations_index.csv", ["id", "name", "branch", "state"],
       [["1", "Same Name", "ug", "DL"], ["2", "Same Name", "sg", "UP"]])
    r = GraphifyOrganizationRepository(GraphifyClient(), tmp_path)
    r.delete(OrganizationId("1"))
    r.delete(OrganizationId("2"))
    assert r.find_all() == []


# ------------------------------------------------------------------ officials
@pytest.fixture
def off_repo(tmp_path):
    _w(tmp_path / "officials.csv", ["id", "name", "designation", "organization_id", "email", "phones", "office_address",
                                    "room_number", "source"], [
        ["a1", "Amit Kumar", "Joint Secretary", "o1", "Amit@Gov.in", "111", "Addr", "R1", "igod"],
        ["a2", "Bina Rao", "Secretary", "o1", "", "", "", "", ""],
        ["", "Chitra Das", "Director", "o2", "c@gov.in", "", "", "", "igod"],            # id derived from name-email
        ["a4", "ab", "Director", "o1", "", "", "", "", ""],                              # short name -> skipped
        ["a5", "Esha Rao", "Director", "o1", "bad-email", "", "", "", ""],               # invalid email -> skipped
    ], bom=True)
    _w(tmp_path / "ministry_officials.csv", ["id", "name", "designation", "organization_id", "email", "source"], [
        ["m1", "Deepak Rao", "Minister of State", "o1", "d@gov.in", "ministry"],
        ["m2", "Fatima Khan", "", "o1", "", "ministry"],
    ])
    return GraphifyOfficialRepository(GraphifyClient(), tmp_path)


def test_official_repo_loading_and_lookups(off_repo):
    r = off_repo
    assert {o.official_id.value for o in r.find_all()} == {"a1", "a2", "Chitra Das-c@gov.in", "m1"}      # m2 has a blank designation -> Designation("") is invalid -> row skipped
    assert r.find_by_id(OfficialId("a1")).designation.rank == 4
    assert r.find_by_id(OfficialId("a1")).contact_info.room_number == "R1"
    assert r.find_by_id(OfficialId("a2")).source == ""              # a blank source column is kept as-is (no default applied)
    assert r.find_by_id(OfficialId("m1")).source == "ministry"
    assert r.find_by_id(OfficialId("zzz")) is None
    assert [o.name for o in r.find_by_email("AMIT@gov.in")] == ["Amit Kumar"]
    assert r.find_by_email("none@x.in") == []
    # name search is a substring match in either direction, case-insensitive
    assert {o.name for o in r.find_by_name("amit")} == {"Amit Kumar"}
    assert {o.name for o in r.find_by_name("Dr Amit Kumar Sharma")} == {"Amit Kumar"}
    assert r.find_by_name("zzz") == []
    assert {o.name for o in r.find_by_organization(OrganizationId("o1"))} == {"Amit Kumar", "Bina Rao", "Deepak Rao"}
    assert r.find_by_organization(OrganizationId("nope")) == []
    assert {o.name for o in r.find_by_designation("secretary")} == {"Amit Kumar", "Bina Rao"}
    assert r.find_by_state("DL") == []


def test_official_repo_top_by_rank_orders_and_limits(off_repo):
    top = off_repo.find_top_by_rank(OrganizationId("o1"), limit=2)
    # Minister of State (1) < Secretary (2) < Joint Secretary (4) < Officer-default (5)
    assert [o.name for o in top] == ["Deepak Rao", "Bina Rao"]
    assert len(off_repo.find_top_by_rank(OrganizationId("o1"))) == 3          # default limit 5 returns all 3
    assert off_repo.find_top_by_rank(OrganizationId("o1"), limit=0) == []


def test_official_repo_save_delete(off_repo):
    o = Official(OfficialId("n1"), "New Person", Designation("Director", 5), ContactInfo(email="n@x.in"), OrganizationId("o9"))
    off_repo.save(o)
    assert off_repo.find_by_id(OfficialId("n1")) is o
    g = off_repo.graphify
    assert g.get_node("official:n1")["properties"]["rank"] == 5
    edge = g.export_edges()[0]
    assert (edge["source"], edge["target"], edge["type"]) == ("organization:o9", "official:n1", "EMPLOYS")
    off_repo.delete(OfficialId("n1"))
    assert off_repo.find_by_id(OfficialId("n1")) is None
    off_repo.delete(OfficialId("n1"))


def test_official_repo_missing_files(tmp_path):
    assert GraphifyOfficialRepository(GraphifyClient(), tmp_path).find_all() == []


# ------------------------------------------------------------------ policies
@pytest.fixture
def pol_repo(tmp_path):
    _w(tmp_path / "policy_contacts.csv", ["id", "instrument", "ministry_id", "tier", "status", "description", "source_url"], [
        ["p1", "PLI Electronics", "m1", "National", "Open for applications", "d1", "http://a"],
        ["p2", "Old Scheme", "m1", "State", "closed", "", ""],
        ["", "Fallback Instrument", "m2", "", "OPEN", "", ""],         # id falls back to instrument, tier '' kept
        ["p4", "ab", "m1", "National", "open", "", ""],                # too short -> skipped
        ["p5", "In Force Policy", "m2", "National", "in-force", "", ""],
    ])
    return GraphifyPolicyRepository(GraphifyClient(), tmp_path)


def test_policy_repo_loading_status_mapping(pol_repo):
    r = pol_repo
    assert {p.policy_id.value for p in r.find_all()} == {"p1", "p2", "Fallback Instrument", "p5"}
    assert r.find_by_id(PolicyId("p1")).status == PolicyStatus.OPEN
    assert r.find_by_id(PolicyId("p2")).status == PolicyStatus.CLOSED
    assert {p.policy_id.value for p in r.find_open()} == {"p1", "Fallback Instrument"}
    assert r.find_by_instrument("pli ELECTRONICS").policy_id.value == "p1"
    assert r.find_by_instrument("nothing") is None
    assert {p.policy_id.value for p in r.find_by_ministry(OrganizationId("m2"))} == {"Fallback Instrument", "p5"}
    assert r.find_by_ministry(OrganizationId("zz")) == []
    assert {p.policy_id.value for p in r.find_by_status("OPEN")} == {"p1", "Fallback Instrument"}
    assert {p.policy_id.value for p in r.find_by_status("closed")} == {"p2", "p5"}
    assert {p.policy_id.value for p in r.find_by_tier("national")} == {"p1", "p5"}


def test_policy_repo_save_delete_and_missing(pol_repo, tmp_path):
    p = Policy(PolicyId("n1"), "New Policy", OrganizationId("m9"), "National", PolicyStatus.OPEN, "desc")
    pol_repo.save(p)
    g = pol_repo.graphify
    assert g.get_node("policy:n1")["properties"]["description"] == "desc"
    e = g.export_edges()[0]
    assert (e["source"], e["target"], e["type"], e["properties"]["status"]) == ("organization:m9", "policy:n1", "OFFERS", "open")
    pol_repo.delete(PolicyId("n1"))
    assert pol_repo.find_by_id(PolicyId("n1")) is None
    pol_repo.delete(PolicyId("n1"))
    assert GraphifyPolicyRepository(GraphifyClient(), tmp_path / "empty").find_all() == []


@pytest.mark.xfail(strict=True, reason="PolicyStatus.IN_FORCE exists but the CSV loader maps every non-'open' "
                                       "status (including 'in-force') to CLOSED")
def test_policy_repo_in_force_status_is_preserved(pol_repo):
    assert pol_repo.find_by_id(PolicyId("p5")).status == PolicyStatus.IN_FORCE


# ------------------------------------------------------------------ press releases
@pytest.fixture
def rel_repo(tmp_path):
    now = datetime.utcnow()
    _w(tmp_path / "pib_ministry_contacts.csv", ["id", "ministry_id", "date", "title", "url", "category"], [
        ["r1", "m1", (now - timedelta(days=10)).isoformat(), "Recent", "http://r1", "c"],
        ["r2", "m1", (now - timedelta(days=89)).isoformat(), "Edge", "http://r2", ""],
        ["r3", "m1", (now - timedelta(days=91)).isoformat(), "Old", "http://r3", ""],
        ["r4", "m2", "2018-01-01", "Ancient", "http://r4", ""],
        ["r5", "m2", "", "No date", "http://r5", ""],                     # missing date -> now
        ["", "m2", "2024-01-01", "No id", "u", ""],                       # no id -> PressRelease ValueError
        ["r7", "m2", "not-a-date", "Bad date", "u", ""],                  # fromisoformat ValueError
        ["r8", "m2", "2024-01-01", "", "u", ""],                          # empty title -> skipped
    ])
    return GraphifyPressReleaseRepository(GraphifyClient(), tmp_path), now


def test_release_repo_loading_and_queries(rel_repo):
    r, now = rel_repo
    assert {x.release_id for x in r.find_all()} == {"r1", "r2", "r3", "r4", "r5"}
    assert r.find_by_id("r1").title == "Recent" and r.find_by_id("nope") is None
    assert {x.release_id for x in r.find_by_ministry(OrganizationId("m1"))} == {"r1", "r2", "r3"}
    assert r.find_by_ministry(OrganizationId("zz")) == []
    got = r.find_by_date_range(now - timedelta(days=95), now - timedelta(days=5))
    assert {x.release_id for x in got} == {"r1", "r2", "r3"}
    assert r.find_by_date_range(datetime(2018, 1, 1), datetime(2018, 1, 1)) == [r.find_by_id("r4")]   # inclusive both ends
    assert r.find_by_90day_recency(OrganizationId("m1")) == 2           # r3 (91d) excluded, r2 (89d) included
    assert r.find_by_90day_recency(OrganizationId("zz")) == 0


def test_release_repo_six_year_trend(rel_repo):
    r, now = rel_repo
    t = r.find_by_6year_trend()
    assert sorted(t) == list(range(now.year - 5, now.year + 1))
    assert t[now.year] + t[now.year - 1] >= 2 and sum(t.values()) == 4     # r4 (2018) is outside the window unless now.year<=2023
    assert 2018 not in t or now.year - 5 <= 2018


def test_release_repo_save_delete_and_missing(rel_repo, tmp_path):
    r, _ = rel_repo
    pr = PressRelease("n1", OrganizationId("m5"), datetime(2024, 2, 3), "T", "http://n", "cat")
    r.save(pr)
    g = r.graphify
    assert g.get_node("pressrelease:n1")["properties"]["date"] == "2024-02-03T00:00:00"
    e = g.export_edges()[0]
    assert (e["source"], e["target"], e["type"]) == ("organization:m5", "pressrelease:n1", "PUBLISHED")
    r.delete("n1")
    assert r.find_by_id("n1") is None
    r.delete("n1")
    assert GraphifyPressReleaseRepository(GraphifyClient(), tmp_path / "none").find_all() == []
