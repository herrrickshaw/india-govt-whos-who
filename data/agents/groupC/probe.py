#!/usr/bin/env /usr/bin/python3
import requests,re,sys,time,json,warnings,os
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
from urllib.parse import urljoin
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
KW=re.compile(r"who|officer|director|contact|telephone|organi[sz]ation|scheme|notif|circular|order|gazette|tender|nodal|grievance|help|pli|incentive|policy|guideline|act|rule|about",re.I)
LOG=open("raw/fetch_log.txt","a")
def get(u):
    try:
        r=requests.get(u,headers=UA,timeout=40,allow_redirects=True)
        LOG.write(f"{time.strftime('%H:%M:%S')} {r.status_code} {u} -> {r.url}\n"); LOG.flush(); time.sleep(1)
        return r
    except Exception as e:
        LOG.write(f"ERR {u} {e}\n"); LOG.flush(); return None
for u in sys.argv[1:]:
    r=get(u)
    if r is None: print("###",u,"ERROR (see log)"); continue
    print("###",u,r.status_code,r.url,len(r.text),"server:",r.headers.get("server"),"| waf:",bool(re.search(r"captcha|cloudflare|akamai|access denied|challenge",r.text[:3000],re.I)))
    fn="raw/home_"+re.sub(r"\W+","_",u)[:60]+".html"; open(fn,"w").write(r.text)
    soup=BeautifulSoup(r.text,"html.parser")
    seen=set()
    for a in soup.find_all("a",href=True):
        t=re.sub(r"\s+"," ",a.get_text(" ",strip=True))[:60]; h=urljoin(r.url,a["href"])
        if (KW.search(t) or KW.search(h)) and h not in seen and not h.startswith(("javascript","mailto")):
            seen.add(h); print("   ",t,"=>",h)
