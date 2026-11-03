import sys,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
html=open(sys.argv[1],'rb').read()
base=sys.argv[2]
kw=re.compile(sys.argv[3] if len(sys.argv)>3 else r'who|officer|director|contact|telephone|organi|scheme|pli|notif|order|circular|gazette|tender|grievance|helpdesk|nodal|attached|subordinate|psu|policy|act|rule',re.I)
s=BeautifulSoup(html,'html.parser')
seen=set()
for a in s.find_all('a',href=True):
    u=urljoin(base,a['href']); t=' '.join(a.get_text(' ',strip=True).split())[:70]
    if u in seen: continue
    if kw.search(u) or kw.search(t):
        seen.add(u); print(t,'|',u)
