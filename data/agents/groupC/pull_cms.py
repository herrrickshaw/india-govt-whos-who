#!/usr/bin/env /usr/bin/python3
"""Pull officer directory + scheme/division data from the shared digifootprint WP CMS behind each ministry site."""
import json, sys, time, requests, os
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36","Accept":"application/json"}
SITES={"dot":"https://www.dot.gov.in","meity":"https://www.meity.gov.in","dst":"https://www.dst.gov.in","dsir":"https://www.dsir.gov.in","moes":"https://www.moes.gov.in"}
TYPES=["directory_post","employees","schemes_and_services","our_division","our_organisation","pages"]
TAX=["departments_tag","designation_tag","schemes_services_category","division_category","organisation_category"]
LOG=open("raw/fetch_log.txt","a")
nreq={}
def get(url, key):
    nreq[key]=nreq.get(key,0)+1
    for attempt in range(2):
        try:
            r=requests.get(url,headers=UA,timeout=40)
            LOG.write(f"{time.strftime('%H:%M:%S')} {r.status_code} {url}\n"); LOG.flush()
            time.sleep(1.0)
            if r.status_code==200: return r
            if r.status_code in (400,404): return r
        except Exception as e:
            LOG.write(f"ERR {url} {e}\n"); time.sleep(2)
    return None
def paged(base, path, key, extra=""):
    out=[]; page=1
    while True:
        r=get(f"{base}/cms/wp-json/wp/v2/{path}?per_page=100&page={page}{extra}", key)
        if r is None or r.status_code!=200: break
        try: d=r.json()
        except Exception: break
        if not isinstance(d,list) or not d: break
        out+=d
        tot=int(r.headers.get("X-WP-TotalPages","1") or 1)
        if page>=tot: break
        page+=1
    return out
only=sys.argv[1:] or list(SITES)
for key in only:
    base=SITES[key]
    for t in TYPES:
        fn=f"raw/{key}_{t}.json"
        if os.path.exists(fn): continue
        extra="&_fields=id,slug,link,title,acf,departments_tag,designation_tag,schemes_services_category,division_category,organisation_category,content,excerpt,parent,modified" 
        d=paged(base,t,key,extra)
        json.dump(d,open(fn,"w"),ensure_ascii=False)
        print(key,t,len(d),flush=True)
    for tx in TAX:
        fn=f"raw/{key}_tax_{tx}.json"
        if os.path.exists(fn): continue
        d=paged(base,tx,key,"&_fields=id,name,slug,parent,count")
        json.dump(d,open(fn,"w"),ensure_ascii=False)
        print(key,tx,len(d),flush=True)
    print(key,"requests:",nreq.get(key,0),flush=True)
