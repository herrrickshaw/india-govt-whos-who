#!/usr/bin/env python3
"""Zip the repo's bulky, regenerable, gitignored data into ~1.5 GB shards and upload each to Dropbox
(dropbox:india-govt-yellow-pages-archive/zips/<tree>/<tree>-NNN.zip), deleting each local shard after rclone has
verified the upload (Dropbox content hash). Writes data/archive_manifest.csv (file -> shard, size) for restore.

Why shards: ~25k small files upload far slower than a few large ones, and the disk has too little free space for one
30 GB zip.  PDFs are stored (zip -0: they are already compressed); text/JSON trees are deflated.

Restore one tree:  rclone copy dropbox:india-govt-yellow-pages-archive/zips/<tree> /tmp/z && unzip -n '/tmp/z/*.zip' -d ~/india-govt-yellow-pages
Usage: scripts/archive_shards.py [--shard-mb 1500] [--only <tree-prefix>]
"""
import argparse, csv, glob, os, subprocess, sys, threading, time, zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REMOTE = "dropbox:india-govt-yellow-pages-archive/zips"
SCRATCH = Path.home() / ".cache/yp_archive_shards"; SCRATCH.mkdir(parents=True, exist_ok=True)
MANIFEST = REPO / "data/archive_manifest.csv"
LOG = REPO / "data/archive_shards.log"
lock = threading.Lock()


def log(msg):
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def trees():
    t = [("data/signatories/pdf", 0), ("data/signatories/text", 6), ("data/career/articles", 6), ("ministry_documents/data/sites", 6)]
    for st in sorted(glob.glob(str(REPO / "data/states/??"))):
        n = os.path.basename(st)
        t += [(f"data/states/{n}/pdf", 0), (f"data/states/{n}/text", 6)]
    t += [(f"data/agents/{g}", 6) for g in ("groupA", "groupC", "groupD")]
    return [(p, lvl) for p, lvl in t if (REPO / p).is_dir()]


def shards_for(tree, limit):
    files = []
    cutoff = time.time() - 120          # skip files still being written by running jobs
    for root, _, names in os.walk(REPO / tree):
        for n in names:
            if n.endswith(".part"):
                continue
            p = Path(root) / n
            try:
                st = p.stat()
            except OSError:
                continue
            if st.st_mtime < cutoff:
                files.append((str(p.relative_to(REPO)), st.st_size))
    files.sort()
    cur, size = [], 0
    for f, s in files:
        if cur and size + s > limit:
            yield cur; cur, size = [], 0
        cur.append((f, s)); size += s
    if cur:
        yield cur


def upload(path, remote_dir, tree, idx, members):
    for attempt in range(3):
        r = subprocess.run(["rclone", "copy", str(path), remote_dir, "--transfers", "1", "--dropbox-chunk-size", "128M",
                            "--retries", "3", "--low-level-retries", "10"], capture_output=True, text=True)
        if r.returncode == 0:
            # rclone has verified size+hash on upload; confirm the object is listed with the right size
            ls = subprocess.run(["rclone", "lsjson", f"{remote_dir}/{path.name}"], capture_output=True, text=True)
            if ls.returncode == 0 and str(path.stat().st_size) in ls.stdout:
                with lock, open(MANIFEST, "a", newline="") as f:
                    w = csv.writer(f)
                    for fn, sz in members:
                        w.writerow([fn, sz, f"{remote_dir}/{path.name}", path.stat().st_size])
                log(f"uploaded+verified {tree} shard {idx:03d}: {len(members)} files, {path.stat().st_size/1e6:.0f} MB")
                path.unlink()
                return True
        log(f"upload attempt {attempt+1} failed for {path.name}: {r.stderr[-200:]}")
        time.sleep(20)
    log(f"GAVE UP on {path.name}; local zip kept at {path}")
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard-mb", type=int, default=1500)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    if not MANIFEST.exists():
        MANIFEST.write_text("file,size,remote_zip,zip_size\n")
    done_files = set()
    with open(MANIFEST) as f:
        for row in csv.DictReader(f):
            done_files.add(row["file"])
    limit = a.shard_mb * 1_000_000
    ex = ThreadPoolExecutor(max_workers=2)
    slots = threading.Semaphore(2)          # at most 2 shards on disk
    futs = []
    for tree, level in trees():
        if a.only and not tree.startswith(a.only):
            continue
        rdir = f"{REMOTE}/{tree.replace('/', '__')}"
        # shard numbering continues after existing shards of this tree
        existing = subprocess.run(["rclone", "lsf", rdir], capture_output=True, text=True).stdout.split()
        idx = len(existing)
        for members in shards_for(tree, limit):
            members = [(f, s) for f, s in members if f not in done_files]
            if not members:
                continue
            idx += 1
            slots.acquire()
            zpath = SCRATCH / f"{tree.replace('/', '__')}-{idx:03d}.zip"
            t0 = time.time()
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_STORED if level == 0 else zipfile.ZIP_DEFLATED, compresslevel=None if level == 0 else level) as z:
                for fn, _ in members:
                    try:
                        z.write(REPO / fn, fn)
                    except OSError as e:
                        log(f"skip {fn}: {e}")
            log(f"built {zpath.name}: {len(members)} files {zpath.stat().st_size/1e6:.0f} MB in {time.time()-t0:.0f}s")
            fut = ex.submit(lambda p=zpath, d=rdir, t=tree, i=idx, m=members: (upload(p, d, t, i, m), slots.release())[0])
            futs.append(fut)
    for f in futs:
        f.result()
    log("all shards done")


if __name__ == "__main__":
    main()
