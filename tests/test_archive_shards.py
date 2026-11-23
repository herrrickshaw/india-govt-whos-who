"""scripts/archive_shards.py with rclone faked and a throw-away repo tree."""
import csv
import os
import sys
import time
import types
import zipfile

import pytest

from helpers import read


@pytest.fixture
def A(load, monkeypatch):
    m = load("archive_shards")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def _make(repo, rel, data=b"x", age=3600):
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    t = time.time() - age
    os.utime(p, (t, t))
    return p


def test_trees_lists_existing_directories_and_text_only_after_extraction(A, repo):
    (repo / "data/signatories/pdf").mkdir(parents=True)
    (repo / "data/states/UP/pdf").mkdir(parents=True)
    (repo / "data/states/UP/text").mkdir()
    (repo / "data/states/UP/signatures.csv").write_text("a")
    (repo / "data/states/TN/pdf").mkdir(parents=True)
    (repo / "data/states/TN/text").mkdir()
    (repo / "data/agents/groupA").mkdir(parents=True)
    (repo / "data/agents/groupB").mkdir()
    got = dict(A.trees())
    assert got == {"data/signatories/pdf": 0, "data/states/UP/pdf": 0, "data/states/UP/text": 6, "data/states/TN/pdf": 0, "data/agents/groupA": 6}
    # the UP text cache is only archived once signatures.csv exists; TN's is skipped
    assert "data/states/TN/text" not in got and "data/agents/groupB" not in got


def test_shards_for_splits_by_size_and_skips_recent_and_part_files(A, repo):
    for n, size in (("a", 40), ("b", 40), ("c", 40), ("d", 40)):
        _make(repo, f"data/states/UP/pdf/{n}.pdf", b"x" * size)
    _make(repo, "data/states/UP/pdf/fresh.pdf", b"x" * 10, age=5)
    _make(repo, "data/states/UP/pdf/partial.part", b"x" * 10)
    shards = list(A.shards_for("data/states/UP/pdf", 100))
    assert [[f for f, _ in s] for s in shards] == [["data/states/UP/pdf/a.pdf", "data/states/UP/pdf/b.pdf"], ["data/states/UP/pdf/c.pdf", "data/states/UP/pdf/d.pdf"]]
    assert list(A.shards_for("data/nothing", 100)) == []
    big = list(A.shards_for("data/states/UP/pdf", 10))
    assert [len(s) for s in big] == [1, 1, 1, 1]                                      # every file exceeds the limit -> one per shard


def test_log_appends(A, repo, capsys):
    A.log("m1")
    A.log("m2")
    assert (repo / "data/archive_shards.log").read_text().count("m") >= 2 and "m1" in capsys.readouterr().out


def _fake_rclone(monkeypatch, A, ls_ok=True, copy_rc=0, existing=""):
    calls = []

    def run(cmd, capture_output=True, text=True):
        calls.append(cmd)
        if cmd[1] == "copy":
            zp = cmd[2]
            run.last_size = os.path.getsize(zp)
            return types.SimpleNamespace(returncode=copy_rc, stdout="", stderr="copy failed " * 30)
        if cmd[1] == "lsjson":
            return types.SimpleNamespace(returncode=0 if ls_ok else 1, stdout=f'[{{"Size": {run.last_size}}}]', stderr="")
        if cmd[1] == "lsf":
            return types.SimpleNamespace(returncode=0, stdout=existing, stderr="")
        raise AssertionError(cmd)
    monkeypatch.setattr(A.subprocess, "run", run)
    return calls


def test_upload_verifies_then_deletes_and_records_manifest(A, repo, monkeypatch):
    A.MANIFEST.write_text("file,size,remote_zip,zip_size\n")
    z = A.SCRATCH / "t-001.zip"
    z.write_bytes(b"zipdata")
    calls = _fake_rclone(monkeypatch, A)
    assert A.upload(z, "remote/dir", "tree", 1, [("a.pdf", 5), ("b.pdf", 6)]) is True
    assert not z.exists()
    m = read(A.MANIFEST)
    assert list(m.file) == ["a.pdf", "b.pdf"] and list(m.remote_zip) == ["remote/dir/t-001.zip"] * 2 and list(m.zip_size) == [7, 7]
    assert calls[0][:3] == ["rclone", "copy", str(z)] and "--transfers" in calls[0]


def test_upload_retries_then_gives_up_and_keeps_local_zip(A, repo, monkeypatch):
    A.MANIFEST.write_text("file,size,remote_zip,zip_size\n")
    z = A.SCRATCH / "t-002.zip"
    z.write_bytes(b"zipdata")
    calls = _fake_rclone(monkeypatch, A, copy_rc=1)
    assert A.upload(z, "remote/dir", "tree", 2, [("a.pdf", 5)]) is False
    assert z.exists() and len([c for c in calls if c[1] == "copy"]) == 3 and read(A.MANIFEST).empty
    assert "GAVE UP on t-002.zip" in (repo / "data/archive_shards.log").read_text()
    # copy succeeds but the listing does not confirm the size -> also retried and kept
    calls = _fake_rclone(monkeypatch, A, ls_ok=False)
    assert A.upload(z, "remote/dir", "tree", 2, [("a.pdf", 5)]) is False and z.exists()


def test_main_builds_numbered_shards_and_skips_archived_files(A, repo, monkeypatch, capsys):
    for n in ("a", "b"):
        _make(repo, f"data/states/UP/pdf/{n}.pdf", b"%PDF " + n.encode())
    _make(repo, "data/signatories/pdf/s.pdf", b"%PDF s")
    A.MANIFEST.write_text("file,size,remote_zip,zip_size\ndata/states/UP/pdf/a.pdf,6,r,10\n")      # 'a' already archived
    calls = _fake_rclone(monkeypatch, A, existing="t-001.zip\nt-002.zip\n")
    monkeypatch.setattr(sys, "argv", ["x", "--shard-mb", "1", "--only", "data/states"])
    A.main()
    m = read(A.MANIFEST)
    assert list(m.file) == ["data/states/UP/pdf/a.pdf", "data/states/UP/pdf/b.pdf"]                 # signatories excluded by --only
    assert m.iloc[1].remote_zip == f"{A.REMOTE}/data__states__UP__pdf/data__states__UP__pdf-003.zip"   # numbering continues after existing shards
    assert "all shards done" in capsys.readouterr().out and list(A.SCRATCH.iterdir()) == []


def test_main_creates_manifest_when_missing(A, repo, monkeypatch):
    _fake_rclone(monkeypatch, A)
    monkeypatch.setattr(sys, "argv", ["x"])
    A.main()
    assert A.MANIFEST.read_text() == "file,size,remote_zip,zip_size\n"
