#!/usr/bin/env python3
"""Telangana GOIR (goir.telangana.gov.in) -> data/states/TS/candidates.csv + pdf/<doc_id>.pdf

The portal is an open ASP.NET search form (no login, no captcha). For each department x year we post the
search, read the result grid (GO type/number/date/category/abstract) and download each GO with the grid's own
'Download' postback. ~1 request/second. Resumable: documents already in candidates.csv are skipped.
Usage: goir_telangana.py [--years 2026 2025 2024] [--depts AGLC ...] [--max N]
"""
import argparse, csv, hashlib, re, sys, time
from pathlib import Path
import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
U = "https://goir.telangana.gov.in/"
OUT = Path(__file__).resolve().parent.parent / "data" / "states" / "TS"
PDF = OUT / "pdf"; PDF.mkdir(parents=True, exist_ok=True)
COLS = ["doc_id", "ministry", "title", "group", "category", "date", "url", "host", "website", "found_on"]
S = requests.Session(); S.headers["User-Agent"] = "Mozilla/5.0 (research; india-govt-whos-who)"; S.verify = False


def hidden(soup):
    return {i["name"]: i.get("value", "") for i in soup.find_all("input", type="hidden") if i.get("name")}


def get(method, *a, **k):
    for t in range(3):
        try:
            return getattr(S, method)(*a, timeout=90, **k)
        except requests.RequestException:
            time.sleep(5 * (t + 1))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="+", default=["2026", "2025", "2024"])
    ap.add_argument("--depts", nargs="*")
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    cpath = OUT / "candidates.csv"
    have = {r["doc_id"] for r in csv.DictReader(open(cpath))} if cpath.exists() else set()
    new_file = not cpath.exists()
    f = open(cpath, "a", newline=""); w = csv.DictWriter(f, fieldnames=COLS)
    if new_file: w.writeheader()
    r = get("get", U); soup = BeautifulSoup(r.text, "html.parser")
    depts = [(o["value"], o.text.strip()) for o in soup.find(id="DDLDeptname").find_all("option") if o["value"] != "Select"]
    if a.depts: depts = [d for d in depts if d[0] in a.depts]
    n = 0
    for year in a.years:
        for code, dname in depts:
            r = get("get", U); soup = BeautifulSoup(r.text, "html.parser")
            d = hidden(soup); d.update({"DDLDeptname": code, "ddlyear": year, "DdlGo_cat": "Select", "DDLGoType": "Select", "BtnSearch": "Search"})
            r = get("post", U, data=d)
            if r is None: print("search failed", code, year, flush=True); continue
            res = BeautifulSoup(r.text, "html.parser"); grid = res.find(id="FileMoveList2")
            if grid is None: continue
            rows = [tr for tr in grid.find_all("tr")[1:] if len(tr.find_all("td")) >= 9]
            print(f"{year} {code}: {len(rows)} orders", flush=True)
            for i, tr in enumerate(rows):
                td = [c.get_text(" ", strip=True) for c in tr.find_all("td")]
                typ, gono, dt, cat, abstract = td[3], td[4], td[5], td[6], td[7]
                key = f"{year}{code}_{typ}{gono}"
                pseudo = f"{U}#{key}"; did = hashlib.sha1(pseudo.encode()).hexdigest()[:16]
                if did in have: continue
                d2 = hidden(res); d2.update({"DDLDeptname": code, "ddlyear": year, "DdlGo_cat": "Select", "DDLGoType": "Select",
                                             "__EVENTTARGET": "FileMoveList2", "__EVENTARGUMENT": f"Select${i}"})
                time.sleep(1)
                p = get("post", U, data=d2)
                if p is None or p.content[:4] != b"%PDF":
                    continue
                (PDF / f"{did}.pdf").write_bytes(p.content)
                m = re.match(r"(\d\d)/(\d\d)/(\d{4})", dt)
                iso = f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else ""
                w.writerow(dict(doc_id=did, ministry=f"{dname.title()} Department, Telangana", title=abstract[:300], group="TS",
                                category=cat, date=iso, url=pseudo, host="goir.telangana.gov.in", website=U, found_on=U))
                f.flush(); have.add(did); n += 1
                if a.max and n >= a.max: return
    print("downloaded", n)


if __name__ == "__main__":
    main()
