import sys
from bs4 import BeautifulSoup
s=BeautifulSoup(open(sys.argv[1],'rb').read(),'html.parser')
for sc in s(['script','style']): sc.decompose()
ts=s.find_all('table')
print('TABLES',len(ts))
for i,t in enumerate(ts):
    rows=t.find_all('tr')
    print(f'--- table {i} rows={len(rows)}')
    for r in rows[:int(sys.argv[2]) if len(sys.argv)>2 else 6]:
        print(' || '.join(' '.join(c.get_text(' ',strip=True).split())[:60] for c in r.find_all(['th','td'])))
if not ts:
    txt=s.get_text('\n',strip=True); print(txt[:3000])
