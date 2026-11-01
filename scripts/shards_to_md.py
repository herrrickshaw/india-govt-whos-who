#!/usr/bin/env python3
"""Convert the PDF shards stored in the cloud archive into machine-readable markdown shards (also in the cloud).

Source : dropbox:india-govt-yellow-pages-archive/zips/<tree>/<tree>-NNN.zip   (store-only zips of PDFs; tree = data__signatories__pdf, data__states__UP__pdf, ...)
Output : dropbox:india-govt-yellow-pages-archive/md/<tree>/<tree>-NNN.md.zip   containing  <doc_id>.md  +  index.jsonl
Local  : data/md_index.csv.gz (one row per document: provenance, size, language/script, method, needs_ocr) — no document text.

Each shard is streamed through scratch space one at a time (rclone copyto -> convert -> rclone copyto back -> delete), so nothing large
stays on the Mac.  Resumable: shards whose .md.zip already exists remotely are skipped.

A markdown file = YAML front matter (doc_id, source_url, ministry/department, title, date, pages, method, script, needs_ocr, sha1) + the text
in reading order with  <!-- page N -->  markers, hyphenated line breaks joined.  Text-layer PDFs use pdftotext; PDFs with (almost) no text
layer are written with an empty body and needs_ocr: true so a GPU/OCR pass (Colab, see scripts/ocr_flagged.py) can fill them in.

Usage:  scripts/shards_to_md.py [--only <tree-substring>] [--workers 4] [--limit-shards N]
"""
import argparse, concurrent.futures as cf, csv, gzip, hashlib, io, json, multiprocessing as mp, os, re, subprocess, sys, tempfile, time, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REMOTE = "dropbox:india-govt-yellow-pages-archive"
SCRATCH = Path.home() / ".cache/yp_md_shards"; SCRATCH.mkdir(parents=True, exist_ok=True)
INDEX = REPO / "data/md_index.csv.gz"
LOG = REPO / "data/shards_to_md.log"
MAX_PAGES = 80
SCRIPTS = {"DEVANAGARI": (0x0900, 0x097F), "BENGALI": (0x0980, 0x09FF), "GURMUKHI": (0x0A00, 0x0A7F), "GUJARATI": (0x0A80, 0x0AFF),
           "ORIYA": (0x0B00, 0x0B7F), "TAMIL": (0x0B80, 0x0BFF), "TELUGU": (0x0C00, 0x0C7F), "KANNADA": (0x0C80, 0x0CFF), "MALAYALAM": (0x0D00, 0x0D7F)}


def log(msg):
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def script_of(text):
    counts = {k: 0 for k in SCRIPTS}; latin = 0
    for ch in text[:20000]:
        o = ord(ch)
        if ch.isascii() and ch.isalpha():
            latin += 1
            continue
        for k, (a, b) in SCRIPTS.items():
            if a <= o <= b:
                counts[k] += 1
                break
    best = max(counts, key=counts.get)
    return best if counts[best] > max(20, latin * 0.3) else "LATIN"


def to_markdown(args):
    """worker (runs in a spawned process): (zip_path, member, meta) -> (doc_id, markdown, index_row)"""
    zip_path, member, meta = args
    doc_id = Path(member).stem
    row = dict(doc_id=doc_id, **{k: meta.get(k, "") for k in ("source_url", "ministry", "title", "date")}, pages=0, chars=0, method="", script="", needs_ocr=0, error="")
    try:
        with zipfile.ZipFile(zip_path) as z, tempfile.TemporaryDirectory() as td:
            data = z.read(member)
            row["sha1"] = hashlib.sha1(data).hexdigest()[:16]; row["bytes"] = len(data)
            p = Path(td) / "d.pdf"; p.write_bytes(data)
            info = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, timeout=60).stdout
            m = re.search(r"Pages:\s+(\d+)", info); pages = int(m.group(1)) if m else 0
            r = subprocess.run(["pdftotext", "-enc", "UTF-8", "-l", str(MAX_PAGES), str(p), "-"], capture_output=True, text=True, timeout=120)
            raw = r.stdout
    except Exception as e:  # corrupt / encrypted / timeout
        row["error"] = f"{type(e).__name__}"[:40]
        return doc_id, None, row
    pgs = raw.split("\f")
    if pgs and not pgs[-1].strip():
        pgs = pgs[:-1]
    cleaned = []
    for i, pg in enumerate(pgs, 1):
        t = re.sub(r"-\n(?=[a-z])", "", pg)                 # join hyphenated line breaks
        t = re.sub(r"[ \t]+\n", "\n", t)
        t = re.sub(r"\n{3,}", "\n\n", t).strip()
        cleaned.append(f"<!-- page {i} -->\n\n{t}" if t else f"<!-- page {i} -->")
    body = "\n\n".join(cleaned)
    chars = len(re.sub(r"\s", "", raw))
    npages = max(pages, len(pgs))
    needs_ocr = int(chars < 60 or (npages and chars / max(1, min(npages, MAX_PAGES)) < 25))
    method = "pdftotext"
    ocr_lang = meta.get("ocr_lang", "")
    if needs_ocr and ocr_lang:                       # cloud workers: CPU tesseract in the state's language(s)
        try:
            with zipfile.ZipFile(zip_path) as z2, tempfile.TemporaryDirectory() as td2:
                p2 = Path(td2) / "d.pdf"; p2.write_bytes(z2.read(member))
                maxp = int(meta.get("ocr_pages", 10))
                env1 = dict(os.environ, OMP_THREAD_LIMIT="1", OMP_NUM_THREADS="1")     # one tesseract thread per worker process: no oversubscription
                subprocess.run(["pdftoppm", "-r", "150", "-gray", "-f", "1", "-l", str(maxp), str(p2), str(Path(td2) / "p")], capture_output=True, timeout=300, env=env1)
                texts = []
                for i, img in enumerate(sorted(Path(td2).glob("p*.p*m")), 1):
                    t = subprocess.run(["tesseract", str(img), "-", "-l", ocr_lang, "--psm", "6"], capture_output=True, text=True, timeout=300, env=env1).stdout
                    t = re.sub(r"[ \t]+\n", "\n", t); t = re.sub(r"\n{3,}", "\n\n", t).strip()
                    texts.append(f"<!-- page {i} -->\n\n{t}" if t else f"<!-- page {i} -->")
                ocr_body = "\n\n".join(texts)
                ocr_chars = len(re.sub(r"<!--.*?-->|\s", "", ocr_body))
                if ocr_chars >= 60:
                    body, chars, method, needs_ocr = ocr_body, ocr_chars, "tesseract:" + ocr_lang, 0
                    raw = re.sub(r"<!--.*?-->", "", ocr_body)
        except Exception as e:
            row["error"] = ("ocr:" + type(e).__name__)[:40]      # keep the text-layer result, record why OCR failed
    scr = script_of(raw)
    row.update(pages=npages, chars=chars, method=method, script=scr, needs_ocr=needs_ocr)
    esc = lambda s: str(s).replace('"', "'").replace("\n", " ")[:300]
    fm = ["---", f'doc_id: "{doc_id}"', f'source_url: "{esc(row["source_url"])}"', f'ministry: "{esc(row["ministry"])}"', f'title: "{esc(row["title"])}"',
          f'date: "{esc(row["date"])}"', f"pages: {npages}", f'method: "{method}"', f'script: "{scr}"', f"needs_ocr: {str(bool(needs_ocr)).lower()}", f'sha1: "{row["sha1"]}"', "---", ""]
    return doc_id, "\n".join(fm) + "\n" + (body if not needs_ocr else "<!-- no text layer: pending OCR -->") + "\n", row


def tree_meta(tree, meta_json=None):
    if meta_json:
        return json.load(open(meta_json))
    """doc_id -> {source_url, ministry, title, date} for a tree name like data__states__UP__pdf"""
    parts = tree.split("__")
    meta = {}
    cands = []
    if parts[:2] == ["data", "signatories"]:
        cands = [REPO / "data/signatories/candidates.csv"]
    elif parts[:2] == ["data", "states"] and len(parts) >= 3:
        cands = [REPO / f"data/states/{parts[2]}/candidates.csv"]
    for c in cands:
        if c.exists():
            with open(c, newline="") as f:
                for r in csv.DictReader(f):
                    meta[r["doc_id"]] = dict(source_url=r.get("url", ""), ministry=r.get("ministry", ""), title=r.get("title", ""), date=r.get("date", ""))
    return meta


def rclone(*a, check=True):
    r = subprocess.run(["rclone", *a], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    return r


def process_shard(tree, shard, workers, pool):
    out_name = shard.replace(".zip", ".md.zip")
    src = SCRATCH / shard
    t0 = time.time()
    rclone("copyto", f"{REMOTE}/zips/{tree}/{shard}", str(src), "--retries", "5", "--transfers", "1")
    meta = tree_meta(tree)
    with zipfile.ZipFile(src) as z:
        members = [n for n in z.namelist() if n.lower().endswith(".pdf")]
    jobs = [(str(src), m, meta.get(Path(m).stem, {})) for m in members]
    results = list(pool.map(to_markdown, jobs, chunksize=8))
    out = SCRATCH / out_name
    rows = []
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zo:
        idx = io.StringIO()
        for doc_id, md, row in results:
            rows.append(row)
            if md is not None:
                zo.writestr(f"{doc_id}.md", md)
            idx.write(json.dumps(row, ensure_ascii=False) + "\n")
        zo.writestr("index.jsonl", idx.getvalue())
    rclone("copyto", str(out), f"{REMOTE}/md/{tree}/{out_name}", "--retries", "5")
    ok = rclone("lsjson", f"{REMOTE}/md/{tree}/{out_name}", check=False)
    if str(out.stat().st_size) not in ok.stdout:
        raise RuntimeError(f"size check failed for {out_name}")
    src.unlink(); out.unlink()
    for r in rows:
        r["tree"] = tree; r["shard"] = shard
    n_ocr = sum(r["needs_ocr"] for r in rows); n_err = sum(1 for r in rows if r["error"])
    log(f"{tree}/{shard}: {len(rows)} docs, {n_ocr} need OCR, {n_err} errors, {time.time()-t0:.0f}s")
    return rows


def append_index(rows):
    cols = ["tree", "shard", "doc_id", "source_url", "ministry", "title", "date", "pages", "chars", "bytes", "sha1", "method", "script", "needs_ocr", "error"]
    new = not INDEX.exists()
    with gzip.open(INDEX, "at", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit-shards", type=int, default=0)
    a = ap.parse_args()
    trees = [l.rstrip("/") for l in rclone("lsf", f"{REMOTE}/zips", "--dirs-only").stdout.split() if l.rstrip("/").endswith("__pdf")]
    done = set(rclone("lsf", f"{REMOTE}/md", "-R", "--files-only", check=False).stdout.split())
    todo = []
    for tree in sorted(trees):
        if a.only and a.only not in tree:
            continue
        for shard in sorted(s for s in rclone("lsf", f"{REMOTE}/zips/{tree}").stdout.split() if s.endswith(".zip")):
            if f"{tree}/{shard.replace('.zip', '.md.zip')}" in done:
                continue
            todo.append((tree, shard))
    if a.limit_shards:
        todo = todo[:a.limit_shards]
    log(f"{len(todo)} shards to convert ({len(trees)} PDF trees)")
    pool = cf.ProcessPoolExecutor(max_workers=a.workers, mp_context=mp.get_context("spawn"))
    for tree, shard in todo:
        try:
            append_index(process_shard(tree, shard, a.workers, pool))
        except Exception as e:  # noqa: one bad shard must not stop the run
            log(f"FAILED {tree}/{shard}: {e}")
    pool.shutdown()
    log("all shards processed")


if __name__ == "__main__":
    main()
