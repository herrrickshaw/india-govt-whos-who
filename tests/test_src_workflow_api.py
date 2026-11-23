import csv
import json
from datetime import datetime, timedelta

import pytest

import src.workflows.refresh_workflow as rw
from src import QueryAPI, RefreshPhase, RefreshState, RefreshWorkflow
from src.domain import repositories as R
from src.domain import OrganizationId
from src.infrastructure.graphify_client import GraphifyClient
from src.infrastructure.repositories_impl import (
    GraphifyOfficialRepository, GraphifyOrganizationRepository, GraphifyPolicyRepository,
    GraphifyPressReleaseRepository,
)
from src.main import export_graph_snapshot, initialize_system, main, run_refresh_workflow, demo_queries


def _w(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


@pytest.fixture
def data_dir(tmp_path):
    now = datetime.utcnow()
    _w(tmp_path / "organizations_index.csv", ["id", "name", "branch", "state", "website"],
       [["m1", "Ministry One", "ug", "DL", "https://one.gov.in"], ["m2", "Ministry Two", "sg", "UP", ""]])
    _w(tmp_path / "officials.csv", ["id", "name", "designation", "organization_id", "email", "phones", "office_address", "room_number", "source"],
       [["o1", "Amit Kumar", "Secretary", "m1", "a@gov.in", "11", "Addr", "R1", "igod"],
        ["o2", "Bina Rao", "Joint Secretary", "m1", "b@gov.in", "", "", "", "igod"],
        ["o3", "Chitra Das", "Director", "m2", "", "", "", "", "igod"]])
    _w(tmp_path / "ministry_officials.csv", ["id", "name", "designation", "organization_id", "email", "source"],
       [["o4", "Deepak Rao", "Minister", "m1", "d@gov.in", "ministry"]])
    _w(tmp_path / "policy_contacts.csv", ["id", "instrument", "ministry_id", "tier", "status", "description", "source_url"],
       [["p1", "PLI Scheme", "m1", "National", "open", "desc", "http://p"], ["p2", "Old Policy", "m2", "State", "closed", "", ""]])
    _w(tmp_path / "pib_ministry_contacts.csv", ["id", "ministry_id", "date", "title", "url", "category"],
       [["r1", "m1", (now - timedelta(days=5)).isoformat(), "T1", "http://r1", "c"],
        ["r2", "m1", "2020-01-01", "T2", "http://r2", ""],
        ["r3", "m2", (now - timedelta(days=1)).isoformat(), "T3", "http://r3", ""]])
    return tmp_path


def _system(data_dir):
    g = GraphifyClient()
    repos = (GraphifyOrganizationRepository(g, data_dir), GraphifyOfficialRepository(g, data_dir),
             GraphifyPolicyRepository(g, data_dir), GraphifyPressReleaseRepository(g, data_dir))
    return g, repos


# ------------------------------------------------------------------ abstract repositories
@pytest.mark.parametrize("abc_cls", [R.OrganizationRepository, R.OfficialRepository, R.PolicyRepository,
                                     R.PressReleaseRepository])
def test_repository_interfaces_are_abstract_and_bodies_are_noops(abc_cls):
    with pytest.raises(TypeError):
        abc_cls()
    names = sorted(abc_cls.__abstractmethods__)
    assert names and "save" in names and "find_all" in names
    impl = type("Impl", (abc_cls,), {n: (lambda self, *a, **k: getattr(abc_cls, "_x", None)) for n in names})
    inst = impl()
    for n in names:
        # the abstract bodies themselves just `pass`
        assert getattr(abc_cls, n)(inst, *([None] * (getattr(abc_cls, n).__code__.co_argcount - 1))) is None


# ------------------------------------------------------------------ RefreshState / workflow
def test_refresh_state_to_dict():
    s = RefreshState(phase=RefreshPhase.SYNC, discovered_orgs=2, sync_errors=["x"])
    d = s.to_dict()
    assert d["phase"] == "sync" and d["discovered_orgs"] == 2 and d["sync_errors"] == ["x"]
    assert set(d) >= {"timestamp", "linked_policies", "graph_nodes_upserted", "graph_edges_upserted", "pib_contacts_created"}
    assert RefreshState(RefreshPhase.DISCOVERY).sync_errors == []        # default list is per-instance
    assert RefreshState(RefreshPhase.DISCOVERY).sync_errors is not RefreshState(RefreshPhase.DISCOVERY).sync_errors


def test_workflow_manual_fallback_full_run(data_dir, monkeypatch, capsys):
    monkeypatch.setattr(rw, "StateGraph", None)
    g, (orgs, offs, pols, rels) = _system(data_dir)
    wf = RefreshWorkflow(orgs, offs, pols, rels, g)
    assert wf.graph is None and wf.edges[0] == ("discover", "link_policies") and len(wf.edges) == 4
    st = wf.run()
    assert st.phase == RefreshPhase.COMPLETE and st.sync_errors == []
    assert st.discovered_orgs == 2
    assert st.discovered_officials_t1 == 3 and st.discovered_officials_t2 == 1
    assert st.linked_policies == 1                       # only p1 is open
    assert st.policy_contacts_created == 3               # top-3 of m1: Minister, Secretary, Joint Secretary
    assert st.linked_pib_releases == 3
    assert st.pib_contacts_created == 3 + 1              # m1 -> 3, m2 -> 1
    assert st.graph_nodes_upserted == 2 + 4 + 2 + 3
    assert st.graph_edges_upserted == 4 + 2 + 3
    assert g.get_metadata("official_sync_timestamp")
    out = capsys.readouterr().out
    assert "[DISCOVER]" in out and "[SYNC]" in out and "[COMPLETE] Refresh successful" in out


def test_workflow_stops_on_failure_but_runs_complete(data_dir, monkeypatch, capsys):
    monkeypatch.setattr(rw, "StateGraph", None)
    g, (orgs, offs, pols, rels) = _system(data_dir)

    def boom():
        raise RuntimeError("db down")
    pols.find_open = boom
    wf = RefreshWorkflow(orgs, offs, pols, rels, g)
    st = wf.run()
    assert st.phase == RefreshPhase.FAILED
    assert st.sync_errors == ["Policy linkage failed: db down"]
    assert st.graph_nodes_upserted == 0                  # sync never ran
    assert "Refresh failed with 1 errors" in capsys.readouterr().out


@pytest.mark.parametrize("breaker,msg", [
    ("org_repo.find_all", "Discovery failed: x"),
    ("release_repo.find_all", "PIB linkage failed: x"),
])
def test_workflow_phase_errors(data_dir, monkeypatch, breaker, msg):
    monkeypatch.setattr(rw, "StateGraph", None)
    g, (orgs, offs, pols, rels) = _system(data_dir)
    wf = RefreshWorkflow(orgs, offs, pols, rels, g)
    obj, meth = breaker.split(".")
    def boom(*a, **k):
        raise ValueError("x")
    setattr(getattr(wf, obj), meth, boom)
    st = wf.run()
    assert st.phase == RefreshPhase.FAILED and st.sync_errors == [msg]


def test_workflow_sync_error_is_recorded(data_dir, monkeypatch):
    monkeypatch.setattr(rw, "StateGraph", None)
    g, (orgs, offs, pols, rels) = _system(data_dir)
    def boom(*a, **k):
        raise OSError("disk")
    g.upsert_node = boom
    st = RefreshWorkflow(orgs, offs, pols, rels, g).run()
    assert st.phase == RefreshPhase.FAILED and st.sync_errors == ["Graph sync failed: disk"]


def test_workflow_uses_state_graph_when_available(data_dir, monkeypatch):
    calls = {"nodes": [], "edges": [], "entry": None}

    class FakeRunnable:
        def __init__(self, nodes):
            self.nodes = nodes

        def invoke(self, state):
            for n in ("discover", "link_policies", "link_pib", "sync", "complete"):
                state = self.nodes[n](state)
            return state

    class FakeGraph:
        def __init__(self, schema):
            calls["schema"] = schema
            self.nodes = {}

        def add_node(self, name, fn):
            calls["nodes"].append(name)
            self.nodes[name] = fn

        def add_edge(self, a, b):
            calls["edges"].append((a, b))

        def set_entry_point(self, n):
            calls["entry"] = n

        def compile(self):
            return FakeRunnable(self.nodes)

    monkeypatch.setattr(rw, "StateGraph", FakeGraph)
    g, (orgs, offs, pols, rels) = _system(data_dir)
    wf = rw.create_refresh_workflow(orgs, offs, pols, rels, g)
    assert calls["schema"] is RefreshState and calls["entry"] == "discover"
    assert calls["nodes"] == ["discover", "link_policies", "link_pib", "sync", "complete"]
    assert calls["edges"] == [("discover", "link_policies"), ("link_policies", "link_pib"),
                              ("link_pib", "sync"), ("sync", "complete")]
    assert wf.run().phase == RefreshPhase.COMPLETE


# ------------------------------------------------------------------ QueryAPI
@pytest.fixture
def api(data_dir):
    g, (orgs, offs, pols, rels) = _system(data_dir)
    RefreshWorkflow(orgs, offs, pols, rels, g).run()
    return QueryAPI(orgs, offs, pols, rels, g)


def test_api_officials(api):
    assert [o["id"] for o in api.search_officials(email="A@gov.in")] == ["o1"]
    assert [o["name"] for o in api.search_officials(name="bina")] == ["Bina Rao"]
    assert {o["id"] for o in api.search_officials(ministry_id="m1")} == {"o1", "o2", "o4"}
    assert {o["id"] for o in api.search_officials(designation="director")} == {"o3"}
    assert api.search_officials(state="DL") == []
    assert len(api.search_officials()) == 4
    # email wins over name when both given
    assert [o["id"] for o in api.search_officials(email="a@gov.in", name="zzz")] == ["o1"]
    d = api.get_official("o1")
    assert d == {"id": "o1", "name": "Amit Kumar", "designation": "Secretary", "rank": 2, "email": "a@gov.in",
                 "phones": "11", "office_address": "Addr", "room_number": "R1", "organization_id": "m1", "source": "igod"}
    assert api.get_official("nope") is None


def test_api_organizations(api):
    assert [o["id"] for o in api.search_organizations(name="ministry one")] == ["m1"]
    assert api.search_organizations(name="zzz") == []
    assert [o["id"] for o in api.search_organizations(branch="sg")] == ["m2"]
    assert [o["id"] for o in api.search_organizations(state="DL")] == ["m1"]
    assert len(api.search_organizations()) == 2
    o = api.get_organization("m1")
    assert o["website"] == "https://one.gov.in" and o["branch"] == "ug" and o["state"] == "DL"
    assert api.get_organization("zz") is None
    assert [x["id"] for x in api.get_organization_officials("m1", limit=2)] == ["o4", "o1"]
    assert [x["id"] for x in api.get_organization_policies("m1")] == ["p1"]


def test_api_policies(api):
    assert [p["id"] for p in api.search_policies(instrument="pli scheme")] == ["p1"]
    assert api.search_policies(instrument="zzz") == []
    assert [p["id"] for p in api.search_policies(ministry_id="m2")] == ["p2"]
    assert [p["id"] for p in api.search_policies(status="open")] == ["p1"]
    assert [p["id"] for p in api.search_policies(tier="state")] == ["p2"]
    assert len(api.search_policies()) == 2
    assert api.get_policy("p1") == {"id": "p1", "instrument": "PLI Scheme", "ministry_id": "m1", "tier": "National",
                                    "status": "open", "description": "desc", "source_url": "http://p"}
    assert api.get_policy("zz") is None
    assert [c["id"] for c in api.get_policy_contacts("p1", limit=2)] == ["o4", "o1"]
    assert [c["id"] for c in api.get_policy_contacts("p1")] == ["o4", "o1", "o2"]      # default limit 3
    assert api.get_policy_contacts("zz") == []


def test_api_pib_activity_stats_and_traversal(api):
    a = api.get_ministry_pib_activity("m1")
    assert a["total_releases"] == 2 and a["releases_90d"] == 1 and a["ministry_id"] == "m1"
    assert a["latest_release"] == max(r["date"] for r in a["releases"])
    assert len(a["trend_6years"]) == 6
    empty = api.get_ministry_pib_activity("zz")
    assert empty["total_releases"] == 0 and empty["latest_release"] is None and empty["releases"] == []
    st = api.get_stats()
    assert (st["organizations"], st["officials"], st["policies"], st["press_releases"]) == (2, 4, 2, 3)
    assert st["graph_stats"]["total_nodes"] > 0 and "timestamp" in st

    t = api.traverse_graph("organization:m1", depth=1)
    assert t["root"] == "organization:m1"
    assert "official:o1" in t["nodes"] and t["node_count"] == len(t["nodes"]) and t["edge_count"] == len(t["edges"])
    assert all(e["source"] == "organization:m1" for e in t["edges"])        # depth 1 only fans out from the root
    t0 = api.traverse_graph("organization:m1", depth=0)
    assert "organization:m1" in t0["nodes"]
    assert t0["edge_count"] == t1_edges_from_root(api)
    # unknown start node: no nodes, no edges
    tz = api.traverse_graph("nope:1")
    assert tz["nodes"] == {} and tz["edges"] == []


def t1_edges_from_root(api):
    return len(api.graphify.get_neighbors("organization:m1"))


def test_api_traversal_handles_cycles(data_dir):
    g = GraphifyClient()
    g.upsert_node("A", "1", {})
    g.upsert_node("B", "2", {})
    g.upsert_edge("A", "1", "X", "B", "2")
    g.upsert_edge("B", "2", "Y", "A", "1")
    api = QueryAPI(None, None, None, None, g)
    t = api.traverse_graph("a:1", depth=5)
    assert t["node_count"] == 2 and t["edge_count"] == 2


# ------------------------------------------------------------------ main.py
def test_initialize_system_and_demo(data_dir, capsys):
    system = initialize_system(data_dir)
    assert set(system) == {"graphify", "org_repo", "official_repo", "policy_repo", "release_repo", "refresh_workflow", "query_api"}
    demo_queries(system)
    out = capsys.readouterr().out
    assert "Organizations: 2" in out and "Officials: 4" in out and "Policies: 2" in out and "Press Releases: 3" in out
    assert "Ministry PIB Activity" in out and "Total releases:" in out


def test_main_writes_reports_into_repo_reports_dir(data_dir, tmp_path, monkeypatch, capsys):
    import src.main as m
    fake_root = tmp_path / "fake_repo"
    (fake_root / "src").mkdir(parents=True)
    (fake_root / "data").mkdir()
    for f in [x for x in data_dir.iterdir() if x.is_file()]:
        (fake_root / "data" / f.name).write_text(f.read_text())
    monkeypatch.setattr(m, "__file__", str(fake_root / "src" / "main.py"))
    monkeypatch.setattr(rw, "StateGraph", None)
    assert main() == 0
    state = json.loads((fake_root / "reports" / "workflow_state.json").read_text())
    assert state["phase"] == "complete" and state["discovered_orgs"] == 2
    snap = json.loads((fake_root / "reports" / "graph_snapshot.json").read_text())
    assert len(snap["nodes"]) == snap["stats"]["total_nodes"] > 0 and len(snap["edges"]) == snap["stats"]["total_edges"]
    assert "All operations completed successfully" in capsys.readouterr().out


def test_main_returns_1_on_error(monkeypatch, capsys):
    import src.main as m

    def boom(*a, **k):
        raise RuntimeError("kaput")
    monkeypatch.setattr(m, "initialize_system", boom)
    assert m.main() == 1
    assert "kaput" in capsys.readouterr().err


def test_run_refresh_and_export_without_data(tmp_path, monkeypatch):
    import src.main as m
    monkeypatch.setattr(m, "__file__", str(tmp_path / "src" / "main.py"))
    monkeypatch.setattr(rw, "StateGraph", None)
    system = initialize_system(tmp_path / "nodata")
    run_refresh_workflow(system)
    export_graph_snapshot(system)
    assert json.loads((tmp_path / "reports" / "workflow_state.json").read_text())["phase"] == "complete"
    assert json.loads((tmp_path / "reports" / "graph_snapshot.json").read_text())["nodes"] == []
