#!/usr/bin/env python3
"""Use this Mac's idle cores to convert the SAME queue as the AWS worker, from the opposite end (free).

Each round: ask the launcher for the shards that still have no markdown output, take the LAST one, download it by presigned URL,
convert it with OCR (nice'd, N worker processes), upload the markdown shard, repeat.  AWS works from the front, this from the back;
they meet in the middle (a shard converted twice just overwrites the same object).  Stops when nothing is left.
Run:  nice -n 15 /usr/bin/python3 scripts/local_md_runner.py [--workers 4]"""
import argparse, concurrent.futures as cf, io, json, multiprocessing as mp, os, sys, time, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloud_md_launch as L          # noqa: E402
import cloud_md_worker as W          # noqa: E402
import shards_to_md as M             # noqa: E402

WORK = Path.home() / ".cache/yp_local_md"; WORK.mkdir(parents=True, exist_ok=True)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--workers", type=int, default=4); a = ap.parse_args()
    os.nice(15)
    pool = cf.ProcessPoolExecutor(max_workers=a.workers, mp_context=mp.get_context("spawn"))
    while True:
        man = L.build_manifest(a.workers, final=True, dry=True)
        jobs = man["jobs"]
        if not jobs:
            print("nothing left", flush=True); break
        j = jobs[-1]; tree, shard = j["tree"], j["shard"]; t0 = time.time()
        try:
            src = WORK / shard; W.curl("-L", j["get_url"], "-o", str(src))
            meta_p = WORK / f"{tree}.meta.json"
            W.curl("-L", j["meta_url"], "-o", str(meta_p))
            meta = M.tree_meta(tree, str(meta_p))
            with zipfile.ZipFile(src) as z:
                members = [n for n in z.namelist() if n.lower().endswith(".pdf")]
            tasks = []
            for m in members:
                md = dict(meta.get(Path(m).stem, {})); md["ocr_lang"] = j.get("ocr_lang", ""); md["ocr_pages"] = j.get("ocr_pages", 10)
                tasks.append((str(src), m, md))
            results = list(pool.map(M.to_markdown, tasks, chunksize=2))
            out = WORK / shard.replace(".zip", ".md.zip"); rows = 0
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zo:
                idx = io.StringIO()
                for doc_id, md_text, row in results:
                    rows += 1
                    if md_text is not None:
                        zo.writestr(f"{doc_id}.md", md_text)
                    idx.write(json.dumps(row, ensure_ascii=False) + "\n")
                zo.writestr("index.jsonl", idx.getvalue())
            W.curl("-X", "PUT", "-T", str(out), j["put_url"])
            src.unlink(); out.unlink()
            print(f"{time.strftime('%H:%M:%S')} local: {shard}: {rows} docs in {time.time()-t0:.0f}s ({len(jobs)-1} left)", flush=True)
        except Exception as e:
            print("FAILED", shard, e, flush=True); time.sleep(60)


if __name__ == "__main__":
    main()
