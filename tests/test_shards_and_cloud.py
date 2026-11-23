"""scripts/shards_to_md.py, scripts/cloud_md_worker.py, scripts/archive_shards.py with poppler/tesseract/rclone/curl faked."""
import csv
import gzip
import io
import json
import os
import sys
import types
import zipfile

import pytest

from helpers import read, write_csv


@pytest.fixture
def M(load):
    return load("shards_to_md")


def make_zip(path, members):
    with zipfile.ZipFile(path, "w") as z:
        for n, b in members.items():
            z.writestr(n, b)
    return str(path)


def fake_tools(monkeypatch, M, pages="Pages: 2\n", text="", ocr_text="OCR TEXT " * 20, images=("p-1.pgm",), fail=None):
    log = []

    def run(cmd, capture_output=True, text=True, timeout=None, env=None):
        log.append(cmd[0])
        if fail == cmd[0]:
            raise RuntimeError("tool failed")
        if cmd[0] == "pdfinfo":
            return types.SimpleNamespace(stdout=pages)
        if cmd[0] == "pdftotext":
            return types.SimpleNamespace(stdout=run.text)
        if cmd[0] == "pdftoppm":
            prefix = cmd[-1]
            for n in images:
                open(os.path.join(os.path.dirname(prefix), n), "wb").write(b"x")
            return types.SimpleNamespace(stdout="")
        if cmd[0] == "tesseract":
            return types.SimpleNamespace(stdout=ocr_text)
        raise AssertionError(cmd)
    run.text = text
    monkeypatch.setattr(M.subprocess, "run", run)
    return log, run


def test_script_of(M):
    assert M.script_of("Plain English text") == "LATIN"
    assert M.script_of("தமிழ் " * 12) == "TAMIL"
    assert M.script_of("தமிழ்") == "LATIN"                      # below the 20-character floor
    assert M.script_of("a" * 200 + "தமிழ் " * 12) == "LATIN"     # Latin outweighs 30%
    assert M.script_of("अ" * 25 + "x" * 50) == "DEVANAGARI"
    assert M.script_of("x" * 25000 + "अ" * 100) == "LATIN"       # only the first 20,000 characters are inspected


def test_to_markdown_text_layer(M, tmp_path, monkeypatch):
    z = make_zip(tmp_path / "s.zip", {"d1.pdf": b"%PDF fake"})
    page1 = "Hello wor-\nld of the order\n\n\n\nsecond   \nline"
    log, run = fake_tools(monkeypatch, M, "Pages: 2\n", text=page1 + "\f" + "Page two " * 30 + "\f")
    doc_id, md, row = M.to_markdown((z, "d1.pdf", {"source_url": 'http://x"y', "ministry": "M", "title": "T\nitle", "date": "2025-01-01"}))
    assert doc_id == "d1" and row["error"] == "" and row["needs_ocr"] == 0 and row["method"] == "pdftotext" and row["pages"] == 2
    assert row["script"] == "LATIN" and row["bytes"] == 9 and len(row["sha1"]) == 16
    assert md.startswith('---\ndoc_id: "d1"\nsource_url: "http://x\'y"\nministry: "M"\ntitle: "T itle"\ndate: "2025-01-01"\npages: 2\n')
    assert 'needs_ocr: false' in md and "<!-- page 1 -->\n\nHello world of the order\n\nsecond\nline" in md and "<!-- page 2 -->" in md
    assert log == ["pdfinfo", "pdftotext"]


def test_to_markdown_marks_scans_and_runs_ocr(M, tmp_path, monkeypatch):
    z = make_zip(tmp_path / "s.zip", {"d1.pdf": b"%PDF fake"})
    log, run = fake_tools(monkeypatch, M, "Pages: 3\n", text="\f\f\f")
    _, md, row = M.to_markdown((z, "d1.pdf", {}))
    assert row["needs_ocr"] == 1 and "<!-- no text layer: pending OCR -->" in md and "needs_ocr: true" in md
    log.clear()
    _, md, row = M.to_markdown((z, "d1.pdf", {"ocr_lang": "hin+eng", "ocr_pages": 2}))
    assert row["method"] == "tesseract:hin+eng" and row["needs_ocr"] == 0 and row["error"] == ""
    assert "OCR TEXT" in md and "needs_ocr: false" in md and log == ["pdfinfo", "pdftotext", "pdftoppm", "tesseract"]
    assert row["chars"] >= 60


def test_to_markdown_ocr_too_short_or_failing_keeps_text_layer_result(M, tmp_path, monkeypatch):
    z = make_zip(tmp_path / "s.zip", {"d1.pdf": b"%PDF fake"})
    fake_tools(monkeypatch, M, "Pages: 1\n", text="", ocr_text="tiny")
    _, md, row = M.to_markdown((z, "d1.pdf", {"ocr_lang": "eng"}))
    assert row["needs_ocr"] == 1 and row["method"] == "pdftotext" and row["error"] == ""
    fake_tools(monkeypatch, M, "Pages: 1\n", text="", fail="tesseract")
    _, md, row = M.to_markdown((z, "d1.pdf", {"ocr_lang": "eng"}))
    assert row["error"] == "ocr:RuntimeError" and row["needs_ocr"] == 1


def test_to_markdown_density_rule_and_corrupt_inputs(M, tmp_path, monkeypatch):
    z = make_zip(tmp_path / "s.zip", {"d1.pdf": b"%PDF fake"})
    # 100 non-space characters over 10 pages = 10 per page < 25 -> needs OCR even though it exceeds 60 characters
    fake_tools(monkeypatch, M, "Pages: 10\n", text="x" * 100)
    assert M.to_markdown((z, "d1.pdf", {}))[2]["needs_ocr"] == 1
    fake_tools(monkeypatch, M, "Pages: 2\n", text="x" * 100)
    assert M.to_markdown((z, "d1.pdf", {}))[2]["needs_ocr"] == 0
    fake_tools(monkeypatch, M, "no page info", text="x" * 100)
    assert M.to_markdown((z, "d1.pdf", {}))[2]["pages"] == 1                         # falls back to the number of form-feed pages
    doc, md, row = M.to_markdown((str(tmp_path / "missing.zip"), "d1.pdf", {}))
    assert md is None and row["error"] == "FileNotFoundError" and doc == "d1"


def test_tree_meta(M, repo):
    write_csv(repo / "data/signatories/candidates.csv", [dict(doc_id="a", url="u1", ministry="M1", title="T1", date="d1")])
    write_csv(repo / "data/states/UP/candidates.csv", [dict(doc_id="b", url="u2", ministry="M2", title="T2", date="d2")])
    assert M.tree_meta("data__signatories__pdf") == {"a": {"source_url": "u1", "ministry": "M1", "title": "T1", "date": "d1"}}
    assert M.tree_meta("data__states__UP__pdf")["b"]["source_url"] == "u2"
    assert M.tree_meta("data__states__ZZ__pdf") == {} and M.tree_meta("something__else") == {}
    p = repo / "m.json"
    p.write_text('{"x": {}}')
    assert M.tree_meta("anything", str(p)) == {"x": {}}


def test_rclone_wrapper(M, monkeypatch):
    monkeypatch.setattr(M.subprocess, "run", lambda cmd, capture_output, text: types.SimpleNamespace(returncode=1, stdout="", stderr="e" * 500))
    with pytest.raises(RuntimeError) as e:
        M.rclone("lsf", "x")
    assert len(str(e.value)) == 300
    assert M.rclone("lsf", "x", check=False).returncode == 1


def test_append_index_writes_header_once(M, repo):
    M.append_index([dict(doc_id="a", tree="t", shard="s", extra="ignored")])
    M.append_index([dict(doc_id="b", tree="t")])
    with gzip.open(M.INDEX, "rt") as f:
        rows = list(csv.DictReader(f))
    assert [r["doc_id"] for r in rows] == ["a", "b"] and "extra" not in rows[0]
    assert list(rows[0])[:3] == ["tree", "shard", "doc_id"]


def test_log_writes_file(M, repo, capsys):
    M.log("hello")
    assert "hello" in capsys.readouterr().out and "hello" in (repo / "data/shards_to_md.log").read_text()


class InlinePool:
    def map(self, fn, jobs, chunksize=1):
        return [fn(j) for j in jobs]

    def shutdown(self):
        pass


def test_process_shard_roundtrip_with_fake_rclone(M, repo, monkeypatch, tmp_path):
    M.SCRATCH = tmp_path / "scratch"
    M.SCRATCH.mkdir()
    shard_zip = make_zip(tmp_path / "remote.zip", {"d1.pdf": b"%PDF 1", "d2.pdf": b"%PDF 2", "note.txt": b"skip"})
    uploaded = {}
    calls = []

    def fake_rclone(*a, check=True):
        calls.append(a[0])
        if a[0] == "copyto" and a[1].startswith("dropbox:") and "/zips/" in a[1]:
            open(a[2], "wb").write(open(shard_zip, "rb").read())
        elif a[0] == "copyto":
            uploaded["bytes"] = open(a[1], "rb").read()
            uploaded["size"] = len(uploaded["bytes"])
        elif a[0] == "lsjson":
            return types.SimpleNamespace(stdout=json.dumps([{"Size": uploaded["size"]}]))
        return types.SimpleNamespace(stdout="", returncode=0)
    monkeypatch.setattr(M, "rclone", fake_rclone)
    monkeypatch.setattr(M, "tree_meta", lambda tree: {"d1": {"title": "One"}})
    monkeypatch.setattr(M, "to_markdown", lambda job: (job[1][:-4], f"md of {job[1]}", dict(doc_id=job[1][:-4], needs_ocr=1 if job[1] == "d2.pdf" else 0, error="")))
    rows = M.process_shard("data__states__UP__pdf", "data__states__UP__pdf-001.zip", 2, InlinePool())
    assert [r["doc_id"] for r in rows] == ["d1", "d2"] and rows[0]["tree"] == "data__states__UP__pdf" and rows[0]["shard"].endswith("-001.zip")
    with zipfile.ZipFile(io.BytesIO(uploaded["bytes"])) as z:
        assert sorted(z.namelist()) == ["d1.md", "d2.md", "index.jsonl"] and z.read("d1.md") == b"md of d1.pdf"
    assert list(M.SCRATCH.iterdir()) == []                                                # scratch cleaned up
    assert "2 docs, 1 need OCR, 0 errors" in (repo / "data/shards_to_md.log").read_text()
    # a remote size mismatch raises
    monkeypatch.setattr(M, "rclone", lambda *a, check=True: types.SimpleNamespace(stdout="[]", returncode=0) if a[0] == "lsjson" else fake_rclone(*a, check=check))
    with pytest.raises(RuntimeError, match="size check failed"):
        M.process_shard("data__states__UP__pdf", "data__states__UP__pdf-001.zip", 2, InlinePool())


def test_main_skips_done_shards_and_survives_failures(M, repo, monkeypatch, tmp_path):
    import concurrent.futures as cf
    monkeypatch.setattr(cf, "ProcessPoolExecutor", lambda **kw: InlinePool())
    outputs = {
        ("lsf", f"{M.REMOTE}/zips", "--dirs-only"): "data__states__UP__pdf/\ndata__signatories__pdf/\nunrelated/\n",
        ("lsf", f"{M.REMOTE}/md", "-R", "--files-only"): "data__states__UP__pdf/data__states__UP__pdf-001.md.zip\n",
        ("lsf", f"{M.REMOTE}/zips/data__states__UP__pdf"): "data__states__UP__pdf-001.zip\ndata__states__UP__pdf-002.zip\nreadme.txt\n",
        ("lsf", f"{M.REMOTE}/zips/data__signatories__pdf"): "data__signatories__pdf-001.zip\n",
    }
    monkeypatch.setattr(M, "rclone", lambda *a, check=True: types.SimpleNamespace(stdout=outputs.get(a, "")))
    done = []

    def fake_process(tree, shard, workers, pool):
        done.append((tree, shard))
        if "signatories" in tree:
            raise RuntimeError("boom")
        return [dict(doc_id="x")]
    monkeypatch.setattr(M, "process_shard", fake_process)
    monkeypatch.setattr(M, "append_index", lambda rows: done.append(("indexed", len(rows))))
    monkeypatch.setattr(sys, "argv", ["x"])
    M.main()
    assert done == [("data__signatories__pdf", "data__signatories__pdf-001.zip"), ("data__states__UP__pdf", "data__states__UP__pdf-002.zip"), ("indexed", 1)]
    log = (repo / "data/shards_to_md.log").read_text()
    assert "2 shards to convert (2 PDF trees)" in log and "FAILED data__signatories__pdf/data__signatories__pdf-001.zip: boom" in log and "all shards processed" in log
    done.clear()
    monkeypatch.setattr(sys, "argv", ["x", "--only", "states", "--limit-shards", "1"])
    M.main()
    assert done[0] == ("data__states__UP__pdf", "data__states__UP__pdf-002.zip")


# ================================================================== cloud_md_worker
@pytest.fixture
def CW(load, monkeypatch, tmp_path):
    monkeypatch.setenv("YP_WORK", str(tmp_path / "work"))
    m = load("cloud_md_worker")
    monkeypatch.setattr(m.time, "sleep", lambda s: None)
    return m


def test_curl_retries_and_raises(CW, monkeypatch):
    seq = iter([types.SimpleNamespace(returncode=1, stderr="e", stdout=""), types.SimpleNamespace(returncode=0, stderr="", stdout="ok")])
    cmds = []
    monkeypatch.setattr(CW.subprocess, "run", lambda cmd, capture_output, text: (cmds.append(cmd), next(seq))[1])
    assert CW.curl("-L", "http://x").stdout == "ok" and cmds[0][:4] == ["curl", "-fsS", "--retry", "3"] and cmds[0][-2:] == ["-L", "http://x"]
    monkeypatch.setattr(CW.subprocess, "run", lambda cmd, capture_output, text: types.SimpleNamespace(returncode=22, stderr="x" * 400, stdout=""))
    with pytest.raises(RuntimeError) as e:
        CW.curl("http://x")
    assert len(str(e.value)) == 300


def test_put_json_and_load_manifest(CW, monkeypatch, capsys, tmp_path):
    seen = []
    monkeypatch.setattr(CW, "curl", lambda *a: seen.append(a) or types.SimpleNamespace(stdout='{"jobs": []}'))
    CW.put_json(None, {"a": 1})
    assert seen == []
    CW.put_json("http://put", {"a": 1})
    assert seen[0][:4] == ("-X", "PUT", "-H", "Content-Type: application/json") and json.loads((CW.WORK / "status.json").read_text()) == {"a": 1}
    monkeypatch.setattr(CW, "curl", lambda *a: (_ for _ in ()).throw(RuntimeError("down")))
    CW.put_json("http://put", {})                                           # best effort: no exception
    assert "status upload failed" in capsys.readouterr().out
    monkeypatch.setattr(CW, "curl", lambda *a: types.SimpleNamespace(stdout='{"jobs": [1]}'))
    assert CW.load_manifest("https://x/m.json") == {"jobs": [1]}
    p = tmp_path / "m.json"
    p.write_text('{"jobs": [2]}')
    assert CW.load_manifest(str(p)) == {"jobs": [2]}


def test_main_converts_queue_until_final(CW, monkeypatch, tmp_path, capsys):
    import concurrent.futures as cf
    monkeypatch.setattr(cf, "ProcessPoolExecutor", lambda **kw: InlinePool())
    src_zip = make_zip(tmp_path / "src.zip", {"d1.pdf": b"x", "d2.pdf": b"y"})
    jobs = [dict(tree="t__pdf", shard="s1.zip", get_url="g1", put_url="p1", meta_url="m1", ocr_lang="eng"),
            dict(tree="t__pdf", shard="s2.zip", get_url="g2", put_url="p2", meta_url="m1")]
    calls = {"n": 0}

    def manifest(src):
        calls["n"] += 1
        if calls["n"] == 1:
            return dict(jobs=jobs, workers=1, status_put_url="http://status")
        return dict(jobs=jobs, final=calls["n"] > 8, status_put_url="http://status")      # the queue can grow; 'final' arrives later
    monkeypatch.setattr(CW, "load_manifest", manifest)
    puts, statuses = [], []

    def fake_curl(*a):
        if "-o" in a:
            dest = a[a.index("-o") + 1]
            if "g2" in a:
                raise RuntimeError("download failed")
            open(dest, "wb").write(open(src_zip, "rb").read() if dest.endswith(".zip") else b"{}")
        elif "-T" in a:
            puts.append(a[a.index("-T") + 1])
        return types.SimpleNamespace(stdout="")
    monkeypatch.setattr(CW, "curl", fake_curl)
    monkeypatch.setattr(CW, "put_json", lambda url, obj: statuses.append(json.loads(json.dumps(obj))))
    monkeypatch.setattr(CW.M, "tree_meta", lambda tree, path: {"d1": {"title": "One"}})
    monkeypatch.setattr(CW.M, "to_markdown", lambda job: (job[1][:-4], "md", dict(doc_id=job[1][:-4], needs_ocr=1, error="", method="tesseract:eng")))
    monkeypatch.setattr(sys, "argv", ["x", "--manifest", "m.json", "--idle-sleep", "1"])
    CW.main()
    last = statuses[-1]
    assert last["done"] == 1 and last["docs"] == 2 and last["needs_ocr_left"] == 2 and last["errors"] == 0 and "finished" in last
    assert last["shards"][0]["ocr_docs"] == 2 and any("error" in s for s in last["shards"])
    assert len(puts) == 1 and puts[0].endswith("s1.md.zip")
    assert "FAILED s2.zip" in capsys.readouterr().out
    assert calls["n"] >= 5                                                   # s2 is retried up to 3 times before the worker waits for 'final'
    assert any(s.get("waiting_for_shards") for s in statuses)
