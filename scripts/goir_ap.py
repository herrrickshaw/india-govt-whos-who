#!/usr/bin/env python3
"""Andhra Pradesh GOIR (goir.ap.gov.in) -> data/states/AP/candidates.csv + pdf/<doc_id>.pdf

Open ASP.NET search form (no login, no captcha). The result grid shows at most 100 rows per search, so a date window
that returns 100 rows is split in half (and, at one day, split by department). Each English GO is fetched from the
portal's own handler dgo.ashx?gid=<id>&fileType=E, about one request per second. Resumable via candidates.csv.
Usage: goir_ap.py [--from 2025-01-01] [--to 2026-11-03] [--max N]
"""
import argparse, csv, datetime as dt, hashlib, re, time
from pathlib import Path
import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
U = "https://goir.ap.gov.in/"; P = "ctl00$ContentPlaceHolder1$"
OUT = Path(__file__).resolve().parent.parent / "data" / "states" / "AP"
PDF = OUT / "pdf"; PDF.mkdir(parents=True, exist_ok=True)
COLS = ["doc_id", "ministry", "title", "group", "category", "date", "url", "host", "website", "found_on"]
S = requests.Session(); S.headers["User-Agent"] = "Mozilla/5.0 (research; india-govt-whos-who)"; S.verify = False


def get(m, *a, **k):
    for t in range(3):
        try:
            return getattr(S, m)(*a, timeout=90, **k)
        except requests.RequestException:
            time.sleep(5 * (t + 1))


def hid(s):
    return {i["name"]: i.get("value", "") for i in s.find_all("input", type="hidden") if i.get("name")}


def search(a, b, dept="-1"):
    s = BeautifulSoup(get("get", U).text, "html.parser")
    d = hid(s); d.update({P + "DDLDeptname": dept, P + "sectddl": "-1", P + "DDLGoType": "-1", P + "DdlGo_cat": "-1",
                          P + "txtfrmdate": a.strftime("%d-%m-%Y"), P + "txttodate": b.strftime("%d-%m-%Y"), P + "BtnSearch": "Search"})
    r = get("post", U, data=d)
    g = BeautifulSoup(r.text, "html.parser").find(id="FileMoveList2") if r else None
    out = []
    for tr in (g.find_all("tr")[1:] if g else []):
        td = tr.find_all("td")
        m = re.search(r'downloadFile\("(\d+)", "E"\)', str(tr))
        if len(td) >= 8 and m:
            c = [x.get_text(" ", strip=True) for x in td]
            out.append(dict(gid=m.group(1), no=c[1], date=c[2], cat=c[3], abstract=c[4], org=re.sub(r"\s+", " ", c[5]), section=c[6]))
        elif len(td) >= 8:
            out.append(None)      # a row without an English file still counts towards the 100-row cap
    return out, depts_of(BeautifulSoup(get("get", U).text, "html.parser")) if False else None


def depts_of(s):
    return [o["value"] for o in s.find(id="DDLDeptname").find_all("option") if o["value"] != "-1"]


def windows(a, b, dept, depts):
    rows, _ = search(a, b, dept)
    if len(rows) >= 100:
        if a < b:
            mid = a + (b - a) // 2
            yield from windows(a, mid, dept, depts); yield from windows(mid + dt.timedelta(1), b, dept, depts)
            return
        if dept == "-1":
            for dd in depts:
                yield from windows(a, b, dd, depts)
            return
    yield from (r for r in rows if r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="a", default="2025-01-01"); ap.add_argument("--to", default=str(dt.date.today()))
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    cpath = OUT / "candidates.csv"
    have = {r["doc_id"] for r in csv.DictReader(open(cpath))} if cpath.exists() else set()
    f = open(cpath, "a", newline=""); w = csv.DictWriter(f, fieldnames=COLS)
    if not have: w.writeheader()
    depts = depts_of(BeautifulSoup(get("get", U).text, "html.parser"))
    lo, hi = dt.date.fromisoformat(a.a), dt.date.fromisoformat(a.to)
    n, cur = 0, lo
    while cur <= hi:                       # month by month, split automatically when a window hits the 100-row cap
        end = min((cur.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - dt.timedelta(1), hi)
        got = 0
        for r in windows(cur, end, "-1", depts):
            pseudo = f"{U}dgo.ashx?gid={r['gid']}&fileType=E"; did = hashlib.sha1(pseudo.encode()).hexdigest()[:16]
            if did in have: continue
            time.sleep(1)
            p = get("get", pseudo)
            if p is None or p.content[:4] != b"%PDF": continue
            (PDF / f"{did}.pdf").write_bytes(p.content)
            m = re.match(r"(\d\d)/(\d\d)/(\d{4})", r["date"])
            w.writerow(dict(doc_id=did, ministry=r["org"].split("-", 1)[-1].strip().title() + ", Andhra Pradesh", title=f"GO {r['no']} - {r['abstract']}"[:300],
                            group="AP", category=r["cat"], date=f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else "", url=pseudo,
                            host="goir.ap.gov.in", website=U, found_on=U))
            f.flush(); have.add(did); n += 1; got += 1
            if a.max and n >= a.max: return
        print(cur, end, got, flush=True)
        cur = end + dt.timedelta(1)
    print("downloaded", n)


if __name__ == "__main__":
    main()
