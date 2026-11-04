#!/usr/bin/env python3
"""Oracles for GATES.md. Each subcommand measures from the data files and prints 'VERIFIED <name> ...' only when its assertion holds."""
import csv, glob, os, shutil, subprocess, sys
from pathlib import Path
csv.field_size_limit(10**8)
R = Path(__file__).resolve().parent.parent
ST = R / "data/states"


def rows(p):
    p = Path(p)
    return list(csv.DictReader(open(p, newline=""))) if p.exists() else []


def need(name, ok, msg):
    if not ok:
        print(f"FAILED {name}: {msg}"); sys.exit(1)
    print(f"VERIFIED {name}: {msg}")


def portal(st, host, minimum):
    c = [r for r in rows(ST / st / "candidates.csv") if host in r["host"]]
    need(f"{st}-orders", len(c) >= minimum, f"{len(c)} {host} orders recorded (need >= {minimum})")


def signed(st, host, minimum):
    ids = {r["doc_id"] for r in rows(ST / st / "candidates.csv") if host in r["host"]}
    s = {r["doc_id"] for r in rows(ST / st / "signatures.csv")} & ids
    need(f"{st}-signed", len(s) >= minimum, f"{len(s)} of {len(ids)} {host} orders have a signature read (need >= {minimum})")


def main():
    a = sys.argv[1:]; k = a[0]
    if k == "portal": portal(a[1], a[2], int(a[3]))
    elif k == "signed": signed(a[1], a[2], int(a[3]))
    elif k == "ub_targets":
        t = rows(ST / "targets.csv"); n = [r for r in t if r["state"] == "UB"]
        need("ub-targets", len(n) >= int(a[1]), f"{len(n)} union-body sites targeted (need >= {a[1]})")
    elif k == "ub_crawled":
        n = [r for r in rows(ST / "targets.csv") if r["state"] == "UB"]
        ok = [r for r in n if (R / "ministry_documents/data/sites" / r["slug"] / "doc_links.csv").exists()]
        need("ub-crawled", len(ok) >= int(a[1]), f"{len(ok)} of {len(n)} union-body sites produced document links (need >= {a[1]})")
    elif k == "ub_candidates":
        c = rows(ST / "UB/candidates.csv"); need("ub-candidates", len(c) >= int(a[1]), f"{len(c)} union-body order PDFs selected (need >= {a[1]})")
    elif k == "ub_signed":
        s = rows(ST / "UB/signatures.csv"); d = rows(ST / "UB/signatory_directory.csv")
        need("ub-signed", len(s) >= int(a[1]) and len(d) >= int(a[2]), f"{len(s)} signatures, {len(d)} distinct signers (need >= {a[1]}, {a[2]})")
    elif k == "linked":
        p = rows(R / "data/policy_contacts_from_documents.csv"); lv = {r["level"] for r in p}
        miss = [x for x in a[1:] if x not in lv]
        need("policy-linked", not miss, f"levels with contacts: {sorted(lv)[:12]}...; missing {miss}")
    elif k == "disk":
        free = shutil.disk_usage("/").free / 2**30
        need("disk", free >= float(a[1]), f"{free:.1f} GiB free (need >= {a[1]})")
    elif k == "docs":
        txt = (R / "README.md").read_text() + (R / "data/RESULTS_SUMMARY.md").read_text() + (R / "docs/DATA_DICTIONARY.md").read_text()
        nums = {"UB signers": len(rows(ST / "UB/signatory_directory.csv")),
                "TS goir orders": len([r for r in rows(ST / "TS/candidates.csv") if "goir.telangana" in r["host"]]),
                "AP goir orders": len([r for r in rows(ST / "AP/candidates.csv") if "goir.ap" in r["host"]])}
        miss = [k2 for k2, v in nums.items() if v and f"{v:,}" not in txt and str(v) not in txt]
        need("docs", not miss and all(nums.values()), f"documents quote measured {nums}; missing {miss}")
    elif k == "pushed":
        g = lambda *c: subprocess.run(["git", "-C", str(R), *c], capture_output=True, text=True).stdout.strip()
        dirty = [l for l in g("status", "--short").splitlines() if "GATES.md" not in l and ".unlazy" not in l]
        subprocess.run(["git", "-C", str(R), "fetch", "-q", "origin"])
        need("pushed", not dirty and g("rev-parse", "HEAD") == g("rev-parse", "origin/main"), f"dirty={len(dirty)}, HEAD==origin/main {g('rev-parse','HEAD')[:7]==g('rev-parse','origin/main')[:7]}")
    else:
        print("unknown"); sys.exit(2)


main()
