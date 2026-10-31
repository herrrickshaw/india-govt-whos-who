#!/bin/bash
# One-screen status of the long-running jobs + archive/free-space. Frees archived+extracted PDFs each run.
cd "$HOME/india-govt-yellow-pages" || exit 1
echo "=== $(date '+%a %H:%M')"
df -h / | awk 'NR==2{print "disk free: "$4" ("$5" used)"}'
echo "--- archive"
[ -f data/archive_manifest.csv ] && echo "shards verified: $(grep -c '' data/archive_manifest.csv | awk '{print $1-1}') files in manifest; zips uploaded: $(cut -d, -f3 data/archive_manifest.csv | sort -u | grep -c zip)"
tail -2 data/archive_shards.log 2>/dev/null | cut -c1-120
echo "local shard zips pending: $(ls ~/.cache/yp_archive_shards 2>/dev/null | wc -l | tr -d ' ')"
/usr/bin/python3 scripts/archive_free.py --apply 2>&1 | tail -1
echo "local PDFs left: $(ls data/signatories/pdf 2>/dev/null | wc -l | tr -d ' ') centre, $(cat data/states/*/pdf/* 2>/dev/null | wc -c | awk '{printf "%.1f GB", $1/1e9}') states"
echo "--- jobs"
for n in "archive_shards.py" "signatory_matrix.py" "state_pipeline.py" "career_tracker.py" "new_policy_scanner.py" "policy_contact_linker.py"; do printf "%-26s %s\n" "$n" "$(pgrep -f "$n" | wc -l | tr -d ' ') proc"; done
echo "states: who's-who $(/usr/bin/python3 -c "import pandas as pd;d=pd.read_csv('data/states/state_officials.csv');r=d[d.name.notna()&(d.name.astype(str).str.strip()!='')];print(f'{d.website.nunique()}/3773 sites scanned, {len(r)} officers in {r.department.nunique()} depts')" 2>/dev/null); crawl $(ls -d ministry_documents/data/sites/st-*/doc_links.csv 2>/dev/null | wc -l | tr -d ' ')/3773 sites done, $(pgrep -f "python.*crawl_html.py" | wc -l | tr -d " ") crawlers running"
echo "state stage now: $(grep -E '^(select|\[..\] extract|\[..\])|=== ' data/states/run_all.out 2>/dev/null | tail -1 | cut -c1-80) (log is block-buffered; trust the counts above)"
echo "centre: pdfs $(ls data/signatories/pdf 2>/dev/null | wc -l | tr -d ' '), text caches $(ls data/signatories/text 2>/dev/null | wc -l | tr -d ' '), signature docs $(/usr/bin/python3 -c "import pandas as pd;print(pd.read_csv('data/signatories/signatures.csv',usecols=['doc_id']).doc_id.nunique())" 2>/dev/null)"
echo "career articles $(ls data/career/articles 2>/dev/null | wc -l | tr -d ' '); events file: $(ls data/career/career_events.csv 2>/dev/null || echo none); new-policy report: $(ls data/NEW_POLICIES.md 2>/dev/null || echo not yet)"
echo "--- recent problems"
grep -hE "GAVE UP|upload attempt .* failed|Traceback" data/archive_shards.log 2>/dev/null | tail -2
