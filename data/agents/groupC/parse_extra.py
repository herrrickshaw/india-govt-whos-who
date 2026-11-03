#!/usr/bin/env /usr/bin/python3
"""Extra officer rows: CMS contact/RTI pages, scheme nodal officers, portals (TDB, ISM, ISRO, IN-SPACe, DoT eServices, PLI-telecom, DBN, ANRF), MeitY officer PDF."""
import json,csv,re,html
from bs4 import BeautifulSoup
M={"dot":("Department of Telecommunications (DoT)","https://www.dot.gov.in"),"meity":("Electronics and Information Technology (MeitY)","https://www.meity.gov.in"),
"dst":("Department of Science and Technology (DST)","https://www.dst.gov.in"),"dsir":("Department of Scientific and Industrial Research (DSIR)","https://www.dsir.gov.in"),
"moes":("Earth Sciences (MoES)","https://www.moes.gov.in"),"space":("Department of Space","https://www.isro.gov.in")}
def deob(s):
    s=re.sub(r'\s*[\[\(]\s*at\s*[\]\)]\s*','@',s,flags=re.I); s=re.sub(r'\s*[\[\(]\s*dot\s*[\]\)]\s*','.',s,flags=re.I); return s
EMAIL=re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+')
PHONE=re.compile(r'(?:\+?91[\s-]*)?(?:\(?0?\d{2,5}\)?[\s–-]*)?\d{3,4}[\s–-]?\d{3,5}(?:\s*(?:/|,)\s*\d{3,5})*')
STOP=re.compile(r'Bhavan|Bhawan|Niketan|Phone|Number|Information|Authority|Division|Cell|Email|E-mail|Contact|Room|Floor|Delhi|Department|Ministry|Mission|Scheme|Programme|Program|Office|Centre|Center|Institute|University|Technology|Science|Board|India|Government|Secretariat|Address|Website|Portal|Fax|Tel|Nodal|Officer|Director|Head|Section|Unit|Group|Wing|Complex|Road|Marg|National|Council|Foundation|Limited|Ltd|Corporation|Society|Laboratory|Lab|Fund|Policy|Details|Additional|General|Enquir|Query|Support|Help',re.I)
_N1=re.compile(r'^\s*(?:Dr|Shri|Sh|Smt|Ms|Mr|Mrs|Prof|Er|Sri|Km)\.?\s+[A-Z][\w.\' -]{2,60}$'); _N2=re.compile(r'^[A-Z][a-z]+(?: [A-Z][\w.\']+){1,4},?\s*(?:IAS|IDAS|IRS|IFS)?\s*$')
class _NAME:
    @staticmethod
    def match(x):
        x=x.strip()
        if _N1.match(x) and not STOP.search(re.sub(r'^(?:Dr|Shri|Sh|Smt|Ms|Mr|Mrs|Prof|Er|Sri|Km)\.?\s+','',x)): return True
        if _N2.match(x) and not STOP.search(x): return True
        return False
NAME=_NAME
DESIG=re.compile(r'Scientist|Director|Secretary|Advis[eo]r|DDG|ADG|ADET|Joint|Deputy|Under|Section Officer|Consultant|Coordinator|Head|Manager|Officer|Member|Chairman|CEO|Engineer|DGM|Controller|Assistant|Principal|Private|PPS|PS\b|Registrar|Professor|Fellow|Chief',re.I)
def txt(h):
    s=BeautifulSoup(h or '','html.parser'); [t.decompose() for t in s(['script','style'])]
    return [re.sub(r'\s+',' ',l).strip() for l in deob(html.unescape(s.get_text('\n'))).split('\n') if l.strip()]
def room(s):
    m=re.search(r'Room\s*(?:No\.?|Number)?\s*[:.-]?\s*([A-Za-z0-9\-/]+)',s or '',re.I); return m.group(1) if m else ''
rows=[]
def add(k,division,name,desig,phones,email,src,room_=''):
    mn,site=M[k]; email=' ; '.join(dict.fromkeys(e.lower() for e in EMAIL.findall(deob(email or ''))))
    rows.append(dict(ministry=mn,website=site,division=division.strip()[:120],name=re.sub(r'\s+',' ',name or '').strip(' ,'),designation=re.sub(r'\s+',' ',desig or '').strip(' ,'),room=room_,phones=re.sub(r'\s+',' ',phones or '').strip(' ,;'),email=email,source_url=src))
def pages(k,slug): return [p for p in json.load(open(f'raw/{k}_pages.json')) if p['slug']==slug][0]['acf']
# A. contact_us_details
for k in M:
    if k=='space': continue
    a=pages(k,'contact-us')
    for d in a.get('contact_us_details') or []:
        add(k,d.get('category',''),d.get('name',''),d.get('designation',''),d.get('phone_number_') or d.get('phone_number',''),d.get('email',''),f"{M[k][1]}/contact-us",room(d.get('address')))
    # B. role blocks inside contact_us_address (DST/DSIR)
    L=txt(a.get('contact_us_address'))
    for i,l in enumerate(L):
        if re.match(r'^(Web Information Manager|Chief Information Officer|Nodal Officer|Grievance|CPIO|Public Information)',l,re.I) and i+2<len(L) and NAME.match(L[i+1]):
            blk=L[i+1:i+8]; em=next((x for x in blk if '@' in x),''); ph=next((x for x in blk if re.search(r'\d{4}',x) and '@' not in x and 'Room' not in x and 'New Delhi' not in x),'')
            add(k,l,L[i+1],L[i+2],ph,em,f"{M[k][1]}/contact-us",room(' '.join(blk)))
# C. MoES RTI CPIO/FAA table
s=BeautifulSoup(pages('moes','rti')['rti_content'],'html.parser')
for tr in s.find_all('tr'):
    tds=[deob(html.unescape(td.get_text('\n'))) for td in tr.find_all('td')]
    if len(tds)<4 or 'CPIO' in tds[2]: continue
    div=re.sub(r'\s+',' ',tds[1]).strip()
    for role,cell in (('CPIO',tds[2]),('First Appellate Authority',tds[3])):
        L=[re.sub(r'\s+',' ',x).strip() for x in cell.split('\n') if x.strip()]
        if not L or ',' not in L[0]: continue
        nm,_,dg=L[0].partition(','); ph=next((x.split(':',1)[1] for x in L if x.lower().startswith('telephone')),''); em=next((x for x in L if '@' in x),'')
        add('moes',f"RTI – {div}",nm,f"{dg.strip()} ({role})",ph,em,"https://www.moes.gov.in/rti",room(cell))
# D. scheme / division / organisation embedded contacts
OKDOM=re.compile(r'(gov\.in|nic\.in|ifciltd\.com|sidbi\.in|stpi\.in|tcoe\.in|ism\.gov\.in|meity\.in)$')
def strings(o):
    if isinstance(o,dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o,list):
        for v in o: yield from strings(v)
    elif isinstance(o,str) and ('@' in o or '[at]' in o.lower()): yield o
for k in ['dot','meity','dst','dsir','moes']:
    for t in ['schemes_and_services','our_division','our_organisation']:
        for p in json.load(open(f'raw/{k}_{t}.json')):
            title=html.unescape(p['title']['rendered']); seen=set()
            for h in strings(p.get('acf')):
                L=txt(h)
                for i,l in enumerate(L):
                    ems=[e for e in EMAIL.findall(l) if OKDOM.search(e.lower())]
                    if not ems: continue
                    # find name/designation in the preceding 4 lines (or same line)
                    nm=dg=''; ph=''
                    ctx=L[max(0,i-4):i]+[l]
                    for c in ctx:
                        c2=re.sub(r'(Email|E-mail|Phone|Tel|Contact)\s*[:.-]\s*','',c,flags=re.I)
                        if not nm and NAME.match(c2.split(',')[0].strip()): nm=c2.split(',')[0].strip(); 
                        if nm and not dg:
                            rest=c2.split(',',1)[1] if (',' in c2 and c2.startswith(nm)) else ('' if c2.startswith(nm) else c2)
                            if DESIG.search(rest) and '@' not in rest: dg=re.sub(r'\d[\d\s,/()-]{5,}','',rest).strip(' ,')
                        m=PHONE.search(c2)
                        if m and len(re.sub(r'\D','',m.group()))>=8 and '@' not in c2: ph=m.group().strip()
                    for e in ems:
                        key=(nm.lower(),e.lower())
                        if key in seen: continue
                        seen.add(key)
                        add(k,title,nm,dg if nm else 'Scheme contact / nodal mailbox',ph,e,f"{M[k][1]}/cms/wp-json/wp/v2/{t}/{p['id']}")
# E/F. TDB directory + ISM our-team (4-col tables preceded by a heading)
def tables(fn,k,prefix,src):
    s=BeautifulSoup(open(fn).read(),'html.parser'); sec=''
    for tb in s.find_all('table'):
        cap=tb.find('caption')
        if cap and cap.get_text(strip=True): sec=re.sub(r'\s+',' ',cap.get_text(' ')).strip()
        for tr in tb.find_all('tr'):
            td=[re.sub(r'\s+',' ',deob(html.unescape(x.get_text(' ')))).strip() for x in tr.find_all(['td','th'])]
            while td and not td[0]: td=td[1:]
            if len(td)==1 and td[0] and td[0]!='Name': sec=td[0]; continue
            if len(td)>=4 and td[0] and td[0]!='Name': add(k,f"{prefix}{sec}",td[0],td[1],td[3],td[2],src)
tables('raw/home_https_tdb_gov_in_tdb_directory.html','dst','TDB – ','https://tdb.gov.in/tdb-directory')
tables('raw/home_https_ism_gov_in_our_team.html','meity','ISM – ','https://ism.gov.in/our-team')
add('meity','India Semiconductor Mission','','General contact mailbox','','ism-dic@gov.in','https://ism.gov.in/contact-us')
# G. ISRO RTI pages (Designation | Name & Contact) + contact.html nodal items
for fn,pa,src in [('raw/home_https_www_isro_gov_in_DOS_list_html.html','Department of Space (DOS)','https://www.isro.gov.in/DOS_list.html'),('raw/home_https_www_isro_gov_in_ISRO_HQ_list_html.html','ISRO Headquarters','https://www.isro.gov.in/ISRO_HQ_list.html')]:
    s=BeautifulSoup(open(fn).read(),'html.parser')
    for tr in s.find_all('tr'):
        td=tr.find_all('td')
        if len(td)<3: continue
        role=re.sub(r'\s+',' ',td[1].get_text(' ')).strip(); L=txt(str(td[2]))
        if not L or role.lower()=='designation': continue
        nm=L[0]; dg=L[1] if len(L)>1 else ''; ph=' '.join(x for x in L if re.match(r'^(Tel|Phone)',x,re.I)); em=' '.join(x for x in L if '@' in x)
        add('space',f"RTI – {pa}",nm,f"{dg} ({role})",re.sub(r'^(Tel|Phone)[^:]*:\s*','',ph,flags=re.I),em,src)
L=txt(open('raw/home_https_www_isro_gov_in_contact_html.html').read())
for i,l in enumerate(L):
    if l.startswith('Nodal Officer'):
        blk=L[i:i+10]; dg=next((x for x in blk[1:] if DESIG.search(x) and not x.startswith('Nodal')),''); em=next((x for x in blk if '@' in x),''); ph=next((x for x in blk if re.search(r'\d{6,}',x)),'')
        add('space','Nodal officers (ISRO contact page)','',f"{dg} – {l[:90]}",ph,em,'https://www.isro.gov.in/contact.html')
for cat,ph,em in [('ISRO Centralised Recruitment Board (ICRB)','+91 80 22172465 / 22172264 / 22172260','icrb@isro.gov.in'),('Office of Media and Public Relations (OMPR)','+91 80 2217 2294 / 2296','isropr@isro.gov.in'),('NRSC Data Centre (satellite data products)','+91 40 23878560 / 23884422','sales@nrsc.gov.in')]:
    add('space',cat,'','Helpdesk / public contact',ph,em,'https://www.isro.gov.in/contact.html')
# H. IN-SPACe
d=json.load(open('raw/home_https_www_inspace_gov_in_api_now_sp_page_id_inspace_team.html'))
def walk(o):
    if isinstance(o,dict):
        if 'email' in o and 'title' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
for o in walk(d): add('space',f"IN-SPACe – {o.get('directorate','') or 'Team'}",o.get('name',''),o.get('title',''),'',o['email'],'https://www.inspace.gov.in/inspace?id=inspace_team')
for dg,em in [('Chairman, IN-SPACe','chairman@inspace.gov.in'),('Joint Secretary, IN-SPACe (office)','js-office@inspace.gov.in'),('Promotion Directorate','director-pd@inspace.gov.in'),('Program Management & Authorization Directorate','director-pmad@inspace.gov.in'),('Technical Directorate','director-td@inspace.gov.in'),('IN-SPACe Digital Platform / registration helpdesk','it-connect@inspace.gov.in'),('General Enquiry','contact-us@inspace.gov.in')]:
    add('space','IN-SPACe – contact mailboxes','',dg,'+91 80 22075050' if 'General' in dg else '',em,'https://www.inspace.gov.in/inspace?id=inspace_contact_us')
# I. DoT eServices policy contacts PDF (fixed-width, wrapped rows)
L=open('raw/pdf/dot_eservices_contacts.txt').read().split('\n'); recs=[]
for l in L:
    if re.match(r'^(Sh\.|Shri|Smt|Ms|Dr)',l): recs.append([l])
    elif recs and l.strip() and not l.startswith('Name') and 'Remarks' not in l and 'Number' not in l.strip()[:6]: recs[-1].append(l)
for r in recs:
    nm=' '.join(x[:21].strip() for x in r).strip(); em=''.join(x[21:43].strip() for x in r); ph=' '.join(x[43:59].strip() for x in r).strip(); rem=' '.join(x[59:].strip() for x in r).strip()
    nm,_,dg=nm.partition(','); add('dot',f"Telecom eServices / Saral Sanchar – {rem}",nm.strip(),dg.strip(),ph,em,'https://eservices.dot.gov.in/sites/default/files/editor-files/contact_details_of_officials_of_dot.pdf')
add('dot','Telecom eServices / Saral Sanchar helpdesk','','Technical helpdesk','','saralsancharhelp@gmail.com ; helpdesk4-ett@gov.in','https://eservices.dot.gov.in/contact-us')
add('dot','Digital Bharat Nidhi (DBN)','','Administrative Registry (official email)','+91 11 2303 6000','admn.dbn-dot@gov.in','https://dbn.gov.in/contact')
for nm,dg,ph in [('Ankur Dey','Manager, SIDBI (PMA, PLI Telecom)','91-7977560804'),('Sachin Modi','Manager, SIDBI (PMA, PLI Telecom)','91-8901380968'),('Pratyush Mishra','DGM, SIDBI (PMA, PLI Telecom)','91-8289076509')]:
    add('dot','PLI Scheme for Telecom & Networking Products – PMA (SIDBI)',nm,dg,ph,'pli.telecom@sidbi.in','https://pli-telecom.udyamimitra.in/Home/Contact')
add('dst','ANRF (anrfonline.in) portal helpdesk','','Portal technical support','011-26552179, 26552197','support@anrfonline.in','https://www.anrfonline.in/ANRF/ContactUs')
# K. MeitY officer-list PDF (names+designations only; add those not already in directory)
have={re.sub(r'^(shri|smt|ms|dr|sh|mrs|mr)\.?\s+','',r['name'].lower()).strip() for r in csv.DictReader(open('officials.csv')) if 'MeitY' in r['ministry']}
n=0
for l in open('raw/pdf/meity_officers_list.txt'):
    m=re.match(r'^\s*\d+\s+\d+\s+(.+?)\s{2,}(\S.*?)\s*$',l)
    if not m: continue
    nm,dg=m.groups(); key=re.sub(r'^(shri|smt|ms|dr|sh|mrs|mr)\.?\s+','',nm.lower()).strip()
    if key in have: continue
    have.add(key); n+=1; add('meity','',nm,dg,'','','https://www.meity.gov.in/static/uploads/2026/04/2056d5f2fec67378ad1433568dbb1ef3.pdf')
print('meity pdf new',n)
# dedupe against existing + write
ex=list(csv.DictReader(open('officials.csv'))); seen={(r['ministry'],r['name'].lower(),r['email'],r['designation'].lower()) for r in ex}
new=[r for r in rows if (r['ministry'],r['name'].lower(),r['email'],r['designation'].lower()) not in seen and (r['name'] or r['email'])]
with open('officials.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(ex[0].keys())); w.writeheader(); w.writerows(ex+new)
import collections; print('extra rows',len(new)); print(collections.Counter(r['ministry'] for r in new))
