#!/usr/bin/env python3
"""Convert PDFs that have no markdown yet (per data/md_index.csv.gz) in data/states/<ST>/pdf to markdown, locally.

Output: corpus/md/data__states__<ST>__pdf/data__states__<ST>__pdf-new-NNN.md.zip (500 docs each; <doc_id>.md + index.jsonl),
and rows appended to data/md_index.csv.gz.  Same converter as the cloud run (scripts/shards_to_md.to_markdown).
Run:  nice /usr/bin/python3 scripts/new_pdfs_to_md.py --states UB AP TS [--workers 6] [--ocr-pages 10]"""
import argparse, concurrent.futures as cf, csv, gzip, io, json, multiprocessing as mp, os, sys, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shards_to_md as M  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OCR = {"UB": "eng", "AP": "tel+eng", "TS": "tel+eng+urd"}
BATCH = 500


def have_ids():
    s = set()
    if M.INDEX.exists():
        with gzip.open(M.INDEX, "rt", newline="") as f:
            for r in csv.DictReader(f):
                s.add(r["doc_id"])
    return s


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--states", nargs="+", default=["UB", "AP", "TS"])
    ap.add_argument("--workers", type=int, default=6); ap.add_argument("--ocr-pages", type=int, default=10); ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    os.nice(10)
    done = have_ids()
    pool = cf.ProcessPoolExecutor(max_workers=a.workers, mp_context=mp.get_context("spawn"))
    for st in a.states:
        pdfdir = REPO / f"data/states/{st}/pdf"
        cand = {r["doc_id"]: r for r in csv.DictReader(open(REPO / f"data/states/{st}/candidates.csv", newline=""))}
        todo = sorted(p for p in pdfdir.glob("*.pdf") if p.stem not in done)
        if a.limit: todo = todo[:a.limit]
        tree = f"data__states__{st}__pdf"; outdir = REPO / "corpus/md" / tree; outdir.mkdir(parents=True, exist_ok=True)
        print(f"[{st}] {len(todo)} PDFs without markdown", flush=True)
        for b in range(0, len(todo), BATCH):
            chunk = todo[b:b + BATCH]; n = len(list(outdir.glob("*-new-*.md.zip"))) + 1
            src = M.SCRATCH / f"{tree}-new-{n:03d}.zip"
            with zipfile.ZipFile(src, "w", zipfile.ZIP_STORED) as z:
                for p in chunk: z.write(p, p.name)
            jobs = []
            for p in chunk:
                c = cand.get(p.stem, {})
                jobs.append((str(src), p.name, dict(source_url=c.get("url", ""), ministry=c.get("ministry", ""), title=c.get("title", ""), date=c.get("date", ""),
                                                  ocr_lang=OCR.get(st, "eng"), ocr_pages=a.ocr_pages)))
            results = list(pool.map(M.to_markdown, jobs, chunksize=4))
            out = outdir / f"{tree}-new-{n:03d}.md.zip"; rows = []
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zo:
                idx = io.StringIO()
                for doc_id, md, row in results:
                    rows.append(row)
                    if md is not None: zo.writestr(f"{doc_id}.md", md)
                    idx.write(json.dumps(row, ensure_ascii=False) + "\n")
                zo.writestr("index.jsonl", idx.getvalue())
            for r in rows: r["tree"] = tree; r["shard"] = out.name.replace(".md.zip", ".zip")
            M.append_index(rows); src.unlink()
            print(f"[{st}] shard {n}: {len(rows)} docs, {sum(r['needs_ocr'] for r in rows)} need OCR, {sum(1 for r in rows if r['error'])} errors", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
