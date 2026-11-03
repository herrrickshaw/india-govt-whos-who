import csv,re,json,html
from bs4 import BeautifulSoup
rows=[]
def deob(e):
    if not e: return ''
    e=html.unescape(e)
    e=re.sub(r'\s*[\[\(\{]\s*at\s*[\]\)\}]\s*|\s*\[@\]\s*','@',e,flags=re.I)
    e=re.sub(r'\s*[\[\(\{]\s*dot\s*[\]\)\}]\s*|(?<=[a-z])dot\]','.',e,flags=re.I)
    e=re.sub(r'@\[','@',e); e=re.sub(r'\[in\]in$','.in',e)
    e=re.sub(r'\[in\]$','.in',e); e=re.sub(r'\[dash\]|\(dash\)','-',e,flags=re.I)
    e=re.sub(r'[\s,;/]+',',',e.strip(' ,;/'))
    return e.lower()
def clean(x): return ' '.join((x or '').replace('\xa0',' ').split())
def add(ministry,website,division,name,designation,room,phones,email,src):
    name=clean(name); 
    if not name or name in ('-','--','Vacant','Name'): return
    rows.append(dict(ministry=ministry,website=website,division=clean(division),name=name,designation=clean(designation),room=clean(room),phones=clean(phones),email=deob(clean(email)),source_url=src))
def soup(f): return BeautifulSoup(open(f,'rb').read(),'html.parser')
def cells(tr): return [clean(c.get_text(' ',strip=True)) for c in tr.find_all(['td','th'])]

# ---------- STEEL ----------
M='Steel (MoS)'; W='https://steel.gov.in'
s=soup('raw/steel_telephone.html'); src=W+'/telephone'
for t in s.find_all('table'):
    for tr in t.find_all('tr')[1:]:
        c=cells(tr)
        if len(c)<6 or not c[0]: continue
        nm,div,room,epbax,off,em=c[:6]
        desig=''
        m=re.match(r'^(.*?)\s*[:：]\s*(.+)$',nm)
        if m and len(m.group(1))<60 and not re.search(r'\b(Shri|Smt|Ms|Dr)\b',m.group(1)):
            desig,nm=m.group(1),m.group(2)          # "PS: Harish Pandey"
        else:
            m=re.match(r'^(.+?),\s*([^,]+)$',nm)   # "X, PS to HSM"
            if m and re.search(r'PS|PA|OSD|Consultant|Steno|PPS|Director|Secretary|Officer|DDG|Adviser|Assistant|Section|Sr\.|Jr\.',m.group(2)):
                nm,desig=m.group(1),m.group(2)
            else:
                m=re.match(r'^(.+?)\s*\((.+)\)$',nm)
                if m: nm,desig=m.group(1),m.group(2)
        if nm.strip().lower() in ('vacant','secretary staff','pao','aao','sr. aca'): continue
        phones=' '.join(x for x in [off, ('EPBAX '+epbax) if epbax else ''] if x)
        add(M,W,div,nm,desig,room,phones,em,src)
# grievance page
s=soup('raw/steel_public-grievance.html'); src=W+'/public-grievance'
txt=s.get_text('\n',strip=True)
add(M,W,'Public Grievance (Appellate Authority)','Shri Daya Nidhan Pandey','Joint Secretary','3102, GPOA Block-3, Netaji Nagar','011-20903059','dn[dot]pandey74[at]ias[dot]nic[dot]in',src)
for t in s.find_all('table'):
    for tr in t.find_all('tr')[1:]:
        c=cells(tr)
        if len(c)>=6 and c[1]:
            add(M,W,'Public Grievance Officer - '+c[0],c[1],c[2],c[3],c[4],c[5],src)

# ---------- MINES ----------
M='Mines (MoM)'; W='https://mines.gov.in'; src='https://mines.gov.in/admin/whosData (rendered at https://mines.gov.in/webportal/whoswho)'
d=json.load(open('raw/mines_whosData.json'))
for r in d['result']:
    if r.get('bitDeletedFlag')==1 or r.get('tinPublishStatus')==0: continue
    cat=json.loads(r.get('jsonOptTxtDetails') or '{}').get('OFFICE_CATEGORY','')
    addr=html.unescape(r.get('ADDRESS') or '')
    m=re.search(r'Room\s*No\.?\s*:?\s*([^\n,]+)',addr,re.I); room=m.group(1).strip() if m else ''
    ph=', '.join(x for x in [r.get('CONTACTNO'),r.get('MOBILENO')] if x and x.strip('-'))
    add(M,W,'' if cat=='--' else cat,html.unescape(r['NAME']),html.unescape(r.get('DESIGNATION') or ''),room,ph,r.get('EMAILID'),src)

# ---------- COAL ----------
M='Coal'; W='https://coal.nic.in'; src=W+'/about-us/whos-who'
s=soup('raw/coal_about-us_whos-who.html')
for t in s.find_all('table'):
    h=t.find_previous(['h2','h3','h4','h5','caption','strong'])
    div=clean(h.get_text()) if h else ''
    if div in ('Phone No','Email Id',''): div="Minister's Office" if not rows or rows[-1]['ministry']!='Coal' else ''
    for tr in t.find_all('tr')[1:]:
        c=cells(tr)
        if len(c)<10: continue
        sn,nm,des,ic,ip,tel,iptel,room,addr,em=c[:10]
        ph='; '.join(x for x in [tel and 'Tel '+tel, iptel and 'IP Tel '+iptel, ic and 'Intercom '+ic, ip and 'IP Phone '+ip] if x)
        add(M,W,div,nm,des,room,ph,em,src)
add(M,W,'Public Grievance Cell','Shri Animesh Bharti','Economic Adviser / Director (PG)','5th Floor, Lok Nayak Bhawan, New Delhi','24655949','',W+'/public-information/public-grievance-cell')
# Coal Controller Organisation (attached office)
W2='https://www.coalcontroller.gov.in'; src=W2+'/who-s-who'
s=soup('raw/cco_whoswho.html')
for t in s.find_all('table'):
    for tr in t.find_all('tr')[1:]:
        c=cells(tr)
        if len(c)<6: continue
        sn,nm,reg,des,em,tel=c[:6]
        add(M,W2,'Coal Controller Organisation'+(f' ({reg})' if reg and reg!='-' else ''),nm,des,'',tel if tel!='-' else '',em if em!='-' else '',src)
add(M,W2,'Coal Controller Organisation','Shri Nirutpal Singh','OSD (contact point)','5th Floor Core-1, Scope Minar, Laxmi Nagar, Delhi-110092','011-21210315, 011-21210317, +91 7523862335','coalcont-wb[at]nic[dot]in',W2+'/contact-us')
add(M,W2,'Coal Controller Organisation - Public Grievance','Dr. S.C. Agrawal','Director (PG)','5th Floor, Core I, Scope Minar, Laxmi Nagar, Delhi','21210315','',W2+'/public-grievances')

# ---------- MoPNG ----------
M='Petroleum and Natural Gas (MoPNG)'; W='https://mopng.gov.in'; src=W+'/en/page/38'
s=soup('raw/mopng_page_38.html'); div=''
for tr in s.find('table').find_all('tr'):
    c=cells(tr)
    if len(c)==1 or (len(c)>1 and not any(c[1:])):
        if c[0] and 'Name of Officer' not in c[0]: div=c[0]
        continue
    if len(c)<6 or 'Name of Officer' in c[0]: continue
    nm,des,room,ph,ic,em=c[:6]
    add(M,W,div,nm,des,room,' '.join(x for x in [ph, ic and 'Intercom '+ic] if x),em,src)
# PNGRB directory PDF
W2='https://pngrb.gov.in'; src=W2+'/pdf/Directory-eng.pdf'; div=''
for line in open('raw/pngrb_directory.txt',encoding='utf-8',errors='ignore'):
    L=line.rstrip('\n')
    if not L.strip() or 'S. No.' in L or 'PNGRB Contact' in L or 'Annexure' in L or 'Reception' in L or 'World Trade' in L: continue
    m=re.match(r'^\s*(\d+)\s+(.*)$',L)
    if not m:
        div=L.strip(); continue
    rest=m.group(2)
    parts=re.split(r'\s{2,}',rest.strip())
    if len(parts)<2: continue
    nm=parts[0]; des=parts[1] if len(parts)>1 else ''; tel=parts[2] if len(parts)>2 else ''; em=parts[3] if len(parts)>3 else ''
    if nm.strip() in ('-','Vacant'): continue
    if len(parts)==3 and '@' not in parts[2] and 'at]' not in parts[2]: tel=parts[2]; em=''
    add(M,W2,'PNGRB - '+div,nm,des,'',tel.strip('-'),em.strip('-'),src)

# ---------- CHEMICALS ----------
M='Department of Chemicals and Petro-Chemicals (DoCP)'; W='https://chemicals.gov.in'; src=W+'/who-who'
s=soup('raw/chem_who-who.html'); div=''
for tr in s.find('table').find_all('tr'):
    c=cells(tr)
    if len(c)==1 or (len(c)>1 and not any(c[1:])):
        if c[0] and c[0]!='S.NO': div=c[0]
        continue
    if len(c)<7 or c[0]=='S.NO': continue
    sn,nm,des,room,ic,ph,em=c[:7]
    add(M,W,div,nm,des,room,' '.join(x for x in [ph, ic and 'Intercom '+ic] if x),em,src)
add(M,W,'Nodal Officer under IT Rule 2009','Shri W B Santhosh','Director','','','wb[dot]santhosh[at]gov[dot]in',W+'/nodal-officer-under-it-rule-2009')
add(M,W,'Web Information Manager','Ms. Divya Parmar','Economic Adviser','22019 (KB-II), Kartavya Bhawan, New Delhi-110001','24015639','divya[dot]parmar[at]gov[dot]in',W+'/contact-us')

# ---------- FERTILIZERS ----------
M='Department of Fertilizers (DoFz)'; W='https://fert.gov.in'; src=W+'/en/department/telephone-directory'
s=soup('raw/fert_department_telephone-directory.html')
for tr in s.find('table').find_all('tr'):
    tds=tr.find_all('td')
    if len(tds)<3: continue
    des=tds[0].find(class_='designation'); nm=tds[0].find(class_='name'); dep=tds[0].find(class_='departmentBadge')
    vals=[clean(d.get_text(' ',strip=True)) for d in tds[1].find_all(class_='our_team_address')]
    ext,ph,fax,em=(vals+['','','',''])[:4]
    room=clean(tds[2].get_text(' ',strip=True))
    add(M,W,clean(dep.get_text()) if dep else '',nm.get_text() if nm else '',des.get_text() if des else '',room,' '.join(x for x in [ph.replace('--',''), ext and ext!='--' and 'Ext '+ext] if x),em if em!='--' else '',src)
add(M,W,'Web Information Manager','Shri Surendra Thakur','Deputy Secretary (IT)','23064, Kartavya Bhawan-2, New Delhi 110001','+91 11-24014818','surendra[dot]thakur54[at]nic[dot]in',W+'/en/connect/contact-us')
add(M,W,'Chief Information Officer / Nodal officer for Court Cases','Ms. Aparna S. Sharma','Additional Secretary','23012, Kartavya Bhawan-2, New Delhi 110001','+91 11-24014804, +91 11-24014805','sharma[dot]aparna[at]nic[dot]in',W+'/en/connect/contact-us')
# RTI cell CPIO / FAA
s=soup('raw/fert_rticell.html'); src=W+'/en/connect/rti-cell'
def split_person(txt):
    txt=clean(txt)
    m=re.match(r'^(.*?)\s+(Under Secretary|Deputy Secretary|Director|Joint Director|Assistant Commissioner|Assistant Director|Senior Accounts Officer|Deputy Director \(Official Language\)|Deputy Director|Joint Secretary|Economic Adviser|Adviser)\s*(.*)$',txt)
    if not m: return txt,'','',''
    nm,des,rest=m.group(1),m.group(2),m.group(3)
    em=re.search(r'\S+(?:\[at\]|@)\S+',rest); ph=re.sub(r'\S+(?:\[at\]|@)\S+','',rest).strip(' ,')
    return nm,des,(em.group(0) if em else ''),ph
seen=set()
for tr in s.find('table').find_all('tr')[1:]:
    c=cells(tr)
    if len(c)==4: cp,work,fa=c[1],c[2],c[3]
    elif len(c)==2: cp,work,fa='',c[0],c[1]
    else: continue
    if cp and not cp.startswith('Vacant'):
        nm,des,em,ph=split_person(cp)
        k=(nm,'CPIO',work)
        if k not in seen: seen.add(k); add(M,W,'RTI CPIO - '+work,nm,des+' (CPIO)','',ph,em,src)
    if fa:
        nm,des,em,ph=split_person(fa)
        k=(nm,'FAA',work)
        if k not in seen: seen.add(k); add(M,W,'RTI First Appellate Authority - '+work,nm,des+' (FAA)','',ph,em,src)

# ---------- PHARMA ----------
M='Department of Pharmaceuticals (DoPs)'; W='https://pharma-dept.gov.in'; src=W+'/en/whos-who'
s=soup('raw/pharma_en_whos-who.html')
for tr in s.find('table').find_all('tr')[1:]:
    c=cells(tr)
    if len(c)<7: continue
    sn,nm,des,ph,ic,addr,em=c[:7]
    add(M,W,'',nm,des,addr,' '.join(x for x in [ph, ic and 'Intercom '+ic] if x),em,src)

with open('officials.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['ministry','website','division','name','designation','room','phones','email','source_url']); w.writeheader(); w.writerows(rows)
from collections import Counter
print(Counter(r['ministry'] for r in rows)); print(len(rows))
