#!/usr/bin/env /usr/bin/python3
import json,csv,re,html
SITES={"dot":("Department of Telecommunications (DoT)","https://www.dot.gov.in"),
"meity":("Electronics and Information Technology (MeitY)","https://www.meity.gov.in"),
"dst":("Department of Science and Technology (DST)","https://www.dst.gov.in"),
"dsir":("Department of Scientific and Industrial Research (DSIR)","https://www.dsir.gov.in"),
"moes":("Earth Sciences (MoES)","https://www.moes.gov.in")}
def clean(s):
    if not s: return ""
    s=html.unescape(re.sub(r'<[^>]+>',' ',str(s)))
    return re.sub(r'\s+',' ',s).strip()
def deob(e):
    if not e: return ""
    e=clean(e).lower()
    e=re.sub(r'\s*\[\s*at\s*\]\s*|\s*\(\s*at\s*\)\s*|\s+at\s+','@',e)
    e=re.sub(r'\s*\[\s*dot\s*\]\s*|\s*\(\s*dot\s*\)\s*','.',e)
    return e.replace(' ','')
def room(addr):
    m=re.search(r'(?:Room|Rm\.?)\s*(?:No\.?|Number)?\s*[-:]?\s*([A-Za-z0-9\-/]+)',addr or '',re.I)
    if m: return m.group(1)
    m=re.match(r'^\s*(\d{2,4}[A-Z]?)\s*,',addr or '')
    return m.group(1) if m else ""
rows=[]
for k,(min_name,site) in SITES.items():
    dirp=json.load(open(f'raw/{k}_directory_post.json'))
    emp=json.load(open(f'raw/{k}_employees.json'))
    desig={t['id']:clean(t['name']) for t in json.load(open(f'raw/{k}_tax_designation_tag.json'))}
    dept={t['id']:clean(t['name']) for t in json.load(open(f'raw/{k}_tax_departments_tag.json'))}
    grp={}
    for e in emp:
        for tid in (e.get('acf') or {}).get('teams') or []:
            grp.setdefault(tid, clean(e['title']['rendered']))
    for p in dirp:
        a=p.get('acf') or {}
        name=clean(a.get('name')) or clean(p['title']['rendered'])
        pre=clean(a.get('title'))
        if pre and not name.lower().startswith(pre.lower()): name=f"{pre} {name}".strip()
        des=(desig.get(a.get('designation_tag')) if isinstance(a.get('designation_tag'),int) else None) or ' / '.join(filter(None,(desig.get(i,'') for i in p.get('designation_tag') or []))) or clean(a.get('designation'))
        div=grp.get(p['id']) or ' / '.join(filter(None,(dept.get(i) for i in p.get('departments_tag') or []))) or ' / '.join(filter(None,(clean(t.get('tag')) for t in (a.get('department_tag') or []) if isinstance(t,dict))))
        phones=' ; '.join(filter(None,[clean(a.get('phone_number')), (('Intercom '+clean(a['intercom_number'])) if a.get('intercom_number') else ''), (('Fax '+clean(a['fax'])) if a.get('fax') else '')]))
        emails=' ; '.join(filter(None,[deob(a.get('email_id')),deob(a.get('secondary_email_id'))]))
        rows.append(dict(ministry=min_name,website=site,division=div,name=name,designation=des,room=room(clean(a.get('address'))),phones=phones,email=emails,source_url=f"{site}/cms/wp-json/wp/v2/directory_post/{p['id']}"))
    seen={(r['name'].lower(),r['email']) for r in rows if r['ministry']==min_name}
    for e in emp:
        for o in (e.get('acf') or {}).get('our_employees') or []:
            if not isinstance(o,dict): continue
            name=clean(o.get('name')); 
            if not name: continue
            em=' ; '.join(filter(None,[deob(o.get('email')),deob(o.get('secondary_email_id'))]))
            if (name.lower(),em) in seen: continue
            seen.add((name.lower(),em))
            phones=' ; '.join(filter(None,[clean(o.get('phone_number')), (('Intercom '+clean(o['intercom_number'])) if o.get('intercom_number') else ''), (('Fax '+clean(o['fax'])) if o.get('fax') else '')]))
            rows.append(dict(ministry=min_name,website=site,division=clean(e['title']['rendered']),name=name,designation=clean(o.get('designation')),room=room(clean(o.get('address'))),phones=phones,email=em,source_url=f"{site}/cms/wp-json/wp/v2/employees/{e['id']}"))
    print(k,len(dirp),'officers;', sum(1 for r in rows if r['ministry']==min_name and r['division']),'with division')
with open('officials.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['ministry','website','division','name','designation','room','phones','email','source_url']); w.writeheader(); w.writerows(rows)
print('total',len(rows))
