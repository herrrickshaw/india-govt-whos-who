from datetime import datetime

import pytest

from src.domain import (
    ContactInfo, Designation, Location, Official, OfficialId, Organization, OrganizationId, Policy, PolicyId,
    PolicyStatus, PressRelease,
)


@pytest.mark.parametrize("cls", [OrganizationId, OfficialId, PolicyId])
def test_ids_reject_empty_and_blank(cls):
    assert cls("x").value == "x"
    for bad in ("", "   ", None):
        with pytest.raises(ValueError):
            cls(bad)


def test_ids_are_frozen_and_hashable():
    a = OrganizationId("1")
    assert {a: 1}[OrganizationId("1")] == 1
    with pytest.raises(Exception):
        a.value = "2"


def test_contact_info_validation():
    assert ContactInfo(email="a.b@gov.in", website="https://x.gov.in").email == "a.b@gov.in"
    assert ContactInfo().email is None
    for bad in ("nobody", "a@b", "a@b.c", "@x.in"):
        with pytest.raises(ValueError):
            ContactInfo(email=bad)
    for bad in ("ftp://x.in", "x.gov.in", "http://"):
        with pytest.raises(ValueError):
            ContactInfo(website=bad)
    assert ContactInfo(website="http://a").website == "http://a"


@pytest.mark.parametrize("title,rank", [
    ("Minister of Finance", 1), ("Principal Secretary", 2), ("Additional Secretary", 3),
    ("Joint Secretary (Admin)", 4), ("Director", 5), ("Secretary", 2),
    ("SECRETARY to the Govt", 2), ("Under Secretary", 2),   # 'secretary' substring wins: documented behaviour
    ("Clerk", 5),
])
def test_designation_from_title_ranks(title, rank):
    d = Designation.from_title(title)
    assert d.rank == rank and d.title == title


def test_designation_validation_bounds():
    assert Designation("x", 1).rank == 1 and Designation("x", 5).rank == 5
    for r in (0, 6, -1):
        with pytest.raises(ValueError):
            Designation("x", r)
    for t in ("", "  "):
        with pytest.raises(ValueError):
            Designation(t, 3)


def test_location_validation():
    for b in ("ug", "sg", "apx", "jud", "leg", "int"):
        assert Location(b, "DL").branch == b
    with pytest.raises(ValueError):
        Location("xx", "DL")
    for s in ("", "  "):
        with pytest.raises(ValueError):
            Location("ug", s)


def _org(**kw):
    base = dict(org_id=OrganizationId("o1"), name="Ministry of Test", location=Location("ug", "DL"),
                contact_info=ContactInfo(email="a@b.in", website="https://b.in"), category="E002")
    base.update(kw)
    return Organization(**base)


def test_organization_name_rules():
    assert _org(name="abc").name == "abc"
    for bad in ("", "  ", "ab"):
        with pytest.raises(ValueError):
            _org(name=bad)


def test_organization_graph_node_and_update():
    o = _org()
    n = o.to_graph_node()
    assert n["id"] == "org:o1" and n["type"] == "Organization"
    p = n["properties"]
    assert (p["name"], p["branch"], p["state"], p["category"], p["website"], p["contact_email"], p["source"]) == \
        ("Ministry of Test", "ug", "DL", "E002", "https://b.in", "a@b.in", "igod")
    before = o.updated_at
    o.update_contact_info(ContactInfo(email="c@d.in"))
    assert o.contact_info.email == "c@d.in" and o.updated_at >= before
    assert o.to_graph_node()["properties"]["website"] is None


def _official(**kw):
    base = dict(official_id=OfficialId("p1"), name="Amit Shah", designation=Designation("Joint Secretary", 4),
                contact_info=ContactInfo(email="a@b.in", phone="123", address="Room", room_number="12"),
                organization_id=OrganizationId("o1"))
    base.update(kw)
    return Official(**base)


def test_official_name_rules():
    for bad in ("", "  ", "ab", "Minister", "secretary", "Director", "OFFICER", "staff"):
        with pytest.raises(ValueError):
            _official(name=bad)
    assert _official(name="Dir").name == "Dir"      # 3 chars and not a marker is fine
    assert _official(name="Directors").name == "Directors"


def test_official_graph_node_edge_update():
    o = _official()
    n = o.to_graph_node()
    assert n["id"] == "official:p1"
    assert n["properties"]["rank"] == 4 and n["properties"]["phones"] == "123"
    assert n["properties"]["room_number"] == "12" and n["properties"]["office_address"] == "Room"
    e = o.to_graph_edge(OrganizationId("zz"))
    assert e == {"source": "org:zz", "target": "official:p1", "type": "EMPLOYS",
                 "properties": {"rank": 4, "source": "igod"}}
    o.update_contact_info(ContactInfo())
    assert o.contact_info.email is None


def _policy(**kw):
    base = dict(policy_id=PolicyId("pol1"), instrument="PLI Scheme", organization_id=OrganizationId("o1"),
                tier="National", status=PolicyStatus.OPEN, description="d", source_url="http://u")
    base.update(kw)
    return Policy(**base)


def test_policy_rules_and_serialisation():
    for bad in ("", " ", "ab"):
        with pytest.raises(ValueError):
            _policy(instrument=bad)
    p = _policy()
    assert p.to_graph_node()["properties"]["status"] == "open"
    assert p.to_graph_node()["id"] == "policy:pol1"
    assert p.to_graph_edge(OrganizationId("o9")) == {
        "source": "org:o9", "target": "policy:pol1", "type": "OFFERS",
        "properties": {"status": "open", "tier": "National"}}
    p.update_status(PolicyStatus.IN_FORCE)
    assert p.status.value == "in-force"
    assert {s.value for s in PolicyStatus} == {"open", "closed", "in-force"}


def test_press_release_rules_and_serialisation():
    d = datetime(2024, 5, 6, 7, 8)
    r = PressRelease("r1", OrganizationId("o1"), d, "Title", "http://u", "cat")
    n = r.to_graph_node()
    assert n["id"] == "pib:r1" and n["properties"]["date"] == d.isoformat()
    assert r.to_graph_edge(OrganizationId("o2")) == {
        "source": "org:o2", "target": "pib:r1", "type": "PUBLISHED", "properties": {"category": "cat"}}
    for rid, title in (("", "t"), (" ", "t"), (None, "t"), ("r", ""), ("r", "  ")):
        with pytest.raises(ValueError):
            PressRelease(rid, OrganizationId("o1"), d, title, "u")
