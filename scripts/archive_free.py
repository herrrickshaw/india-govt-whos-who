#!/usr/bin/env python3
"""Free local disk: delete PDFs that are (1) listed in data/archive_manifest.csv with an uploaded+verified shard,
(2) unchanged since archiving (same size), (3) older than 10 minutes, and (4) already extracted — their text cache
(<tree>/../text/<doc_id>.json) exists, so the pipeline never needs the PDF again.  Restore from the shard if ever needed:
  rclone copy dropbox:india-govt-yellow-pages-archive/zips/<tree> /tmp/z && unzip -n '/tmp/z/*.zip' -d ~/india-govt-yellow-pages
Never touches text caches, articles, rosters or anything committed.   Usage: archive_free.py [--apply]"""
import csv, os, sys, time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
apply = "--apply" in sys.argv
man = REPO / "data/archive_manifest.csv"
if not man.exists():
    print("no manifest yet"); sys.exit(0)
freed = n = skipped_noext = skipped_changed = 0
now = time.time()
for row in csv.DictReader(open(man)):
    f = row["file"]
    if not f.endswith(".pdf") or "/pdf/" not in f:
        continue
    p = REPO / f
    if not p.exists():
        continue
    st = p.stat()
    if st.st_size != int(row["size"]) or now - st.st_mtime < 600:
        skipped_changed += 1; continue
    cache = p.parent.parent / "text" / (p.stem + ".json")
    if not cache.exists():
        skipped_noext += 1; continue
    freed += st.st_size; n += 1
    if apply:
        p.unlink()
print(f"{'freed' if apply else 'would free'}: {n} PDFs, {freed/1e9:.2f} GB; kept {skipped_noext} not yet extracted, {skipped_changed} changed/recent")
