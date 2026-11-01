#!/usr/bin/env python3
"""Runs ANYWHERE (AWS EC2 spot instance, Google Colab, any Linux box) with no cloud credentials.

Input : a manifest.json of jobs, each with time-limited presigned URLs:
        {"jobs": [{"tree", "shard", "get_url", "put_url", "meta_url", "ocr_lang", "ocr_pages"}], "status_put_url": "...", "workers": N}
For each job: download the PDF shard (HTTPS GET), convert every PDF to markdown with scripts/shards_to_md.to_markdown
(pdftotext, then CPU tesseract in `ocr_lang` for documents with no text layer), write <shard>.md.zip (<doc_id>.md + index.jsonl)
and upload it (HTTPS PUT).  Progress is PUT to status_put_url after every shard.  Needs: poppler-utils, tesseract-ocr (+ language
packs), python3.  Usage:  python3 cloud_md_worker.py --manifest manifest.json [--workers N]
"""
import argparse, concurrent.futures as cf, io, json, multiprocessing as mp, os, subprocess, sys, tempfile, time, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shards_to_md as M  # noqa: E402

WORK = Path(os.environ.get("YP_WORK", "/tmp/yp_work")); WORK.mkdir(parents=True, exist_ok=True)


def curl(*args):
    for attempt in range(4):
        r = subprocess.run(["curl", "-fsS", "--retry", "3", "--max-time", "3000", *args], capture_output=True, text=True)
        if r.returncode == 0:
            return r
        time.sleep(10 * (attempt + 1))
    raise RuntimeError(r.stderr[-300:])


def put_json(url, obj):
    if not url:
        return
    p = WORK / "status.json"; p.write_text(json.dumps(obj))
    try:
        curl("-X", "PUT", "-H", "Content-Type: application/json", "-T", str(p), url)
    except Exception as e:  # status is best-effort
        print("status upload failed", e, flush=True)


def load_manifest(src):
    if src.startswith("http"):
        return json.loads(curl("-L", src).stdout)
    return json.load(open(src))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--manifest", required=True, help="path or presigned URL; re-read between shards so the queue can grow")
    ap.add_argument("--workers", type=int, default=0); ap.add_argument("--idle-sleep", type=int, default=120)
    a = ap.parse_args()
    man = load_manifest(a.manifest); workers = a.workers or man.get("workers") or os.cpu_count() or 2
    pool = cf.ProcessPoolExecutor(max_workers=workers, mp_context=mp.get_context("spawn"))
    status = {"started": time.strftime("%F %T"), "done": 0, "docs": 0, "needs_ocr_left": 0, "errors": 0, "shards": []}
    done, failed = set(), {}
    while True:
        try:
            man = load_manifest(a.manifest)
        except Exception as e:
            print("manifest fetch failed", e, flush=True); time.sleep(60); continue
        todo = [j for j in man["jobs"] if j["shard"] not in done and failed.get(j["shard"], 0) < 3]
        status["queue"] = len(todo)
        if not todo:
            if man.get("final"):
                break
            put_json(man.get("status_put_url"), {**status, "updated": time.strftime("%F %T"), "waiting_for_shards": True})
            time.sleep(a.idle_sleep); continue
        j = todo[0]; t0 = time.time(); tree, shard = j["tree"], j["shard"]
        try:
            src = WORK / shard; curl("-L", j["get_url"], "-o", str(src))
            meta_p = WORK / f"{tree}.meta.json"
            if not meta_p.exists():
                curl("-L", j["meta_url"], "-o", str(meta_p))
            meta = M.tree_meta(tree, str(meta_p))
            with zipfile.ZipFile(src) as z:
                members = [n for n in z.namelist() if n.lower().endswith(".pdf")]
            tasks = []
            for m in members:
                md = dict(meta.get(Path(m).stem, {})); md["ocr_lang"] = j.get("ocr_lang", ""); md["ocr_pages"] = j.get("ocr_pages", 10)
                tasks.append((str(src), m, md))
            results = list(pool.map(M.to_markdown, tasks, chunksize=4))
            out = WORK / shard.replace(".zip", ".md.zip"); rows = []
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zo:
                idx = io.StringIO()
                for doc_id, md_text, row in results:
                    rows.append(row)
                    if md_text is not None:
                        zo.writestr(f"{doc_id}.md", md_text)
                    idx.write(json.dumps(row, ensure_ascii=False) + "\n")
                zo.writestr("index.jsonl", idx.getvalue())
            curl("-X", "PUT", "-T", str(out), j["put_url"])
            src.unlink(); out.unlink(); done.add(shard)
            status["done"] += 1; status["docs"] += len(rows)
            status["needs_ocr_left"] += sum(r["needs_ocr"] for r in rows); status["errors"] += sum(1 for r in rows if r["error"])
            status["shards"].append({"shard": shard, "docs": len(rows), "ocr_docs": sum(1 for r in rows if str(r["method"]).startswith("tesseract")), "seconds": round(time.time() - t0)})
            print(f"{time.strftime('%H:%M:%S')} {shard}: {len(rows)} docs in {time.time()-t0:.0f}s", flush=True)
        except Exception as e:
            failed[shard] = failed.get(shard, 0) + 1
            status["shards"].append({"shard": shard, "error": str(e)[:200]}); print("FAILED", shard, e, flush=True)
        status["updated"] = time.strftime("%F %T"); put_json(man.get("status_put_url"), status)
    status["finished"] = time.strftime("%F %T"); put_json(man.get("status_put_url"), status)
    print("done", flush=True)


if __name__ == "__main__":
    main()
