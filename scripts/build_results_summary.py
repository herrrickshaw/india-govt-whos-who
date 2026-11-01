#!/usr/bin/env python3
"""Rebuild data/results_by_ministry.csv, data/results_by_state.csv and data/RESULTS_SUMMARY.md from the current data."""
import glob, os, time
from pathlib import Path
import pandas as pd

R = Path(__file__).resolve().parent.parent; os.chdir(R)
d = pd.read_csv('ministry_documents/data/all_documents.csv.gz', compression='gzip', low_memory=False)
t = (d.title.fillna('') + ' ' + d.group.fillna('') + ' ' + d.category.fillna('')).str.lower()
d['order_type'] = t.str.contains(r'order|notification|gazette|circular|memorand|\bo\.?m\b|guideline|policy|rules|amendment|g\.s\.r|s\.o\.|advisory|scheme|incentive')
cand = pd.read_csv('data/signatories/candidates.csv'); sig = pd.read_csv('data/signatories/signatures.csv'); sig1 = sig[sig.sig_rank > 0]
dirc = pd.read_csv('data/signatories/signatory_directory.csv'); ros = pd.read_csv('data/ministry_officials.csv')
ns = pd.read_csv('data/signatories/notification_signatories.csv'); mt = ns[ns.match_status == 'matched']
ii = pd.read_csv('data/policy_instruments_index.csv')
rows = []
for m, g in d.groupby('ministry'):
    c = cand[cand.ministry == m]; s = sig1[sig1.doc_id.isin(set(c.doc_id))]; dr = dirc[dirc.ministry == m]
    rows.append(dict(ministry=m, docs_indexed=len(g), order_docs=int(g.order_type.sum()), pdfs_read=len(c), with_signature=s.doc_id.nunique(),
                     signers=len(dr), signers_email=int(dr.email.notna().sum()), roster_officers=int((ros.ministry == m).sum()),
                     matched_docs=mt[mt.ministry == m].doc_id.nunique(), officers_linked=mt[mt.ministry == m].officer_id.nunique(),
                     instruments=int((ii.ministry == m).sum()), instr_with_contact=int(((ii.ministry == m) & (ii.n_contacts > 0)).sum())))
M = pd.DataFrame(rows).sort_values(['signers', 'docs_indexed'], ascending=False); M.to_csv('data/results_by_ministry.csv', index=False)

tg = pd.read_csv('data/states/targets.csv'); so = pd.read_csv('data/states/state_officials.csv')
real = so[so.name.notna() & (so.name.astype(str).str.strip() != '')]
S = []
for st, g in tg.groupby('state'):
    r = real[real.state == st]
    crawled = sum(os.path.exists(f'ministry_documents/data/sites/{s}/doc_links.csv') for s in g.slug.unique())
    cpath = f'data/states/{st}/candidates.csv'; cands = len(pd.read_csv(cpath)) if os.path.exists(cpath) else 0
    sp = f'data/states/{st}/signatures.csv'; sg = pd.read_csv(sp, low_memory=False) if os.path.exists(sp) else pd.DataFrame()
    nsp = f'data/states/{st}/notification_signatories.csv'; n = pd.read_csv(nsp, low_memory=False) if os.path.exists(nsp) else pd.DataFrame()
    S.append(dict(state=st, departments=len(g), whoswho_depts=r.department.nunique(), officers=len(r), officers_email=int((r.email.fillna('') != '').sum()),
                  sites_crawled=crawled, candidate_pdfs=cands, docs_read=len(glob.glob(f'data/states/{st}/text/*.json')),
                  docs_with_signature=(sg[sg.sig_rank > 0].doc_id.nunique() if len(sg) else 0),
                  indic_script_signatures=(int(sg.sig_script.isin(['DEVANAGARI','TAMIL','MALAYALAM','KANNADA','TELUGU','BENGALI','GUJARATI','GURMUKHI','ORIYA']).sum()) if len(sg) else 0),
                  signers=(n.signatory.nunique() if len(n) else 0),
                  matched_docs=(n[n.match_status == 'matched'].doc_id.nunique() if len(n) else 0),
                  officers_linked=(n[n.match_status == 'matched'].officer_id.nunique() if len(n) else 0)))
ST = pd.DataFrame(S); ST.to_csv('data/results_by_state.csv', index=False)


def md(df, cols, names):
    L = ["| " + " | ".join(names) + " |", "|" + "---|" * len(names)]
    for r in df[cols].itertuples(index=False):
        L.append("| " + " | ".join(f"{x:,}" if isinstance(x, (int,)) or (hasattr(x, 'item') and isinstance(x.item(), int)) else str(x) for x in r) + " |")
    return "\n".join(L)


tot = M[['docs_indexed', 'pdfs_read', 'with_signature', 'signers', 'signers_email', 'roster_officers', 'matched_docs', 'instruments', 'instr_with_contact']].sum()
Mm = M[M.pdfs_read > 0]
T = ["# Results summary — ministries and states\n",
     f"_Built {time.strftime('%Y-%m-%d %H:%M')} by `scripts/build_results_summary.py` from `data/results_by_ministry.csv` and `data/results_by_state.csv`._\n",
     "## Union ministries\n",
     f"{int(tot.docs_indexed):,} documents indexed; {int(tot.pdfs_read):,} order, notification, circular and guideline PDFs read; {int(tot.with_signature):,} with a detectable signature block; {int(tot.signers):,} distinct signers ({int(tot.signers_email):,} with a printed email); roster {int(tot.roster_officers):,} officers across 47 ministries; {int(tot.matched_docs):,} documents matched to a roster officer; {int(tot.instruments)} policy/incentive instruments mapped, {int(tot.instr_with_contact)} with at least one signing contact.\n",
     md(Mm, ['ministry', 'docs_indexed', 'pdfs_read', 'with_signature', 'signers', 'signers_email', 'roster_officers', 'matched_docs', 'officers_linked', 'instruments', 'instr_with_contact'],
        ['Ministry', 'Docs indexed', 'PDFs read', 'With signature', 'Signers', 'With email', 'Roster officers', 'Docs matched', 'Officers linked', 'Instruments', '…with contact']),
     "\n## States and union territories\n",
     f"{int(ST.departments.sum()):,} department sites targeted; who's-who found for {int(ST.whoswho_depts.sum())} of them ({int(ST.officers.sum()):,} officers, {int(ST.officers_email.sum()):,} with email); {int(ST.sites_crawled.sum()):,} sites crawled; {int(ST.candidate_pdfs.sum()):,} order/notification PDFs selected and {int(ST.docs_read.sum()):,} read; {int(ST.docs_with_signature.sum()):,} with a detectable signature ({int(ST.indic_script_signatures.sum()):,} signature lines in Indic scripts, romanised and translated); {int(ST.signers.sum()):,} signers; {int(ST.matched_docs.sum()):,} documents matched to {int(ST.officers_linked.sum())} roster officers.\n",
     md(ST.sort_values('docs_with_signature', ascending=False), ['state', 'departments', 'whoswho_depts', 'officers', 'officers_email', 'sites_crawled', 'candidate_pdfs', 'docs_read', 'docs_with_signature', 'signers', 'matched_docs', 'officers_linked'],
        ['State', 'Dept sites', "With who's-who", 'Officers', 'With email', 'Crawled', 'PDFs selected', 'Docs read', 'With signature', 'Signers', 'Docs matched', 'Officers linked']),
     "\n## How to read this\n",
     "- 'Roster officers' are the people the who's-who pages list; 'signers' are people read from signature blocks, most of whom are in no roster. 'Docs matched' links a signed document to a roster officer by name, ministry, designation and rank.\n- State rosters are the department who's-who pages plus the IAS and IPS cadre lists (5,755 and 4,553 officers) for that state's cadre; at most 300 order PDFs per state were read.\n- Instruments are policy and incentive schemes found in document titles, the curated list, or the PIB scan; 'with contact' means an official signed paperwork under that name.\n"]
Path('data/RESULTS_SUMMARY.md').write_text("\n".join(T))
print(f"ministries {len(Mm)}; states {len(ST)}"); print(ST[['docs_read', 'docs_with_signature', 'signers', 'matched_docs', 'officers_linked', 'indic_script_signatures']].sum().to_dict())
