# Pipelines, commands and operations

This is the stage-by-stage guide to rebuilding the repository, with what each stage reads and writes, how long it took, and the operational
lessons that cost time the first time. Use `/usr/bin/python3` where DuckDB is needed (it was installed for the system Python only on the
author's Mac); other scripts run on any Python 3.9+ with `requirements.txt`, plus `pandas`, `duckdb`, `pdftotext`/`pdfinfo`/`pdftoppm` (poppler) and
`tesseract` with language packs.

## 0. Map

| # | Stage | Script | Reads | Writes |
|---|---|---|---|---|
| 1 | igod directory | `igod_crawl.py`, `igod_org_details.py` | igod.gov.in | `organizations_index.csv`, `org_contacts.csv`, `officials.csv` |
| 2 | Union rosters | `ministry_whoswho.py`, `refresh_ministry_rosters.py`, `merge_agent_results.py` | ministry sites | `ministry_officials.csv` |
| 3 | Civil lists | `dopt_civil_list.py`, `ips_civil_list.py` | DoPT PDFs | `ias_officers.csv`, `ips_officers.csv` |
| 4 | Document index | `ministry_documents/tools/*` | 89 ministry sites | `all_documents.csv.gz` |
| 5 | Centre signatures | `signatory_matrix.py` | document index, PDFs | `data/signatories/*` |
| 6 | State pipeline | `state_pipeline.py` | state sites | `data/states/*` |
| 7 | Policies | `policy_contact_linker.py`, `new_policy_scanner.py` | signatures, PIB index | `policy_*`, `new_policies_*` |
| 8 | Career | `career_tracker.py` | news, ER sheets | `data/career/*`, directory columns |
| 9 | Markdown | `shards_to_md.py`, `cloud_md_*.py`, `local_md_runner.py` | archived PDF shards | `corpus/md`, `md_index.csv.gz` |
| 10 | Archive | `archive_shards.py`, `archive_free.py`, `archive_states_watch.sh` | local PDFs | cloud zip shards |
| 11 | Reports | `build_results_summary.py`, `build_db.py`, `build_dashboard.py` | all tables | `RESULTS_SUMMARY.md`, DuckDB, dashboard |
| – | Operations | `status_check.sh`, `resource_guard.sh` | – | – |

## 1–3. Directory, rosters, civil lists
```bash
python3 scripts/igod_crawl.py            # ~431 listing pages -> organizations_index.csv
python3 scripts/igod_org_details.py      # contact blocks + igod who's-who
python3 scripts/ministry_whoswho.py      # each ministry's own who's-who page / PDF / CMS endpoint
python3 scripts/refresh_ministry_rosters.py   # re-probe with wider paths; keeps the LARGER roster per ministry
python3 scripts/merge_agent_results.py   # fold per-ministry-group collections (data/agents/group*/) into the roster
```
- igod quirks: the lazy-load endpoint accepts at most 5 rows per request; a session cookie from a prior page is required; officer pages paginate as `/list_contacts/<start>/10`; emails are obfuscated `name[at]gov[dot]in` and are de-obfuscated on parse.
- Most newer ministry sites are a Next.js shell over an open WordPress JSON API; the officer directory is `…/cms/wp-json/wp/v2/directory_post` (with `designation_tag` and `departments_tag` taxonomies). HTML crawling of those sites finds nothing, which is why the first scrape covered only 17 ministries and the API route raised it to 47.
- A ministry's roster is replaced only by a **larger** one (a one-row contact page once overwrote a 100-row roster).

## 4. Document index
See `ministry_documents/README.md`. Sites are fingerprinted by platform (shared CMS API, server-rendered HTML, JS-only, own API) and each uses the matching extractor; ~136,000 documents were indexed.

## 5. Centre: signatures → directory → matches → matrix
```bash
SIG_ALL_MINISTRIES=1 SIG_PER_MINISTRY_CAP=0 /usr/bin/python3 scripts/signatory_matrix.py all
# stages: select -> fetch -> extract -> directory -> match -> matrix -> directory
```
- `select` picks order-type PDFs (orders, notifications, circulars, OMs, guidelines, gazette notifications), policy/incentive titles first.
- `fetch` downloads at ≈1 request/second/host into the gitignored `data/signatories/pdf/` (24,262 PDFs, 30 GB).
- `extract` reads the last two pages for the signature block with `pdftotext` (OCR fallback with Tesseract for scans) and caches the text per document in `text/<doc_id>.json`, so later stages never need the PDF.
- `directory` builds the roster-independent **signer directory first**; `match` then links signers to roster officers; `matrix` builds the officer × topic tables.
- Environment: `SIG_ALL_MINISTRIES=1` widens beyond ministries that have a roster; `SIG_PER_MINISTRY_CAP=N` limits unrostered ministries to the newest N documents (the final run used `0`, meaning no cap, after a first pass at 250).

## 6. States and union territories
```bash
/usr/bin/python3 scripts/state_pipeline.py all --states UP,TN,KL --max-sites 20 --max-pages 60 --max-docs 300     # pilot
/usr/bin/python3 scripts/state_pipeline.py select fetch extract translate match matrix directory --states <ALL> --max-docs 400 --tranche2
```
Stages: `targets` (state department sites from igod, 3,773) → `whoswho` (reuses the ministry scraper with state-friendly page probes) → `crawl` (runs `ministry_documents/tools/crawl_html.py` under `xargs -P 8` with a 15-minute wall-clock limit per site) → `select` (order words in English **and** regional languages, e.g. आदेश, அரசாணை, ഉത്തരവ്) → `fetch` → `extract` (signature lines in Latin or the state's script, OCR with that state's Tesseract packs) → `translate` (romanise names, translate subject lines with an LLM; rule-based fallback) → `match` against the state who's-who plus the IAS/IPS officers of that cadre → `matrix`, `directory`.
- Portal collectors (they write into the same `candidates.csv` / `pdf/` layout, so `extract … directory` runs unchanged): `scripts/goir_telangana.py` (ASP.NET postbacks, resumable) and `scripts/goir_ap.py` (date windows, splits when the 100-row cap is hit; `--from/--to/--max`). `scripts/verify_coverage.py` is the check script for the coverage gates. Portals with a captcha (UP, MH) are not collected.
- Union bodies: `targets` adds rows with state `UB`; `select --states UB --max-docs 4000`, then the usual stages.
- State code → Tesseract languages and script are in `STATE_LANG` in the script (for example `TN` → `tam+eng`, `AS` → `asm+ben+eng`).
- IAS/IPS cadre codes differ from igod state codes (Karnataka `KA`→`KN`, Bihar `BR`→`BH`, Telangana `TS`→`TG`, UTs and Goa/Mizoram/Arunachal → `UT`); see `CADRE`.
- `--tranche2` selects the next documents per state without touching earlier selections; `extract` is incremental (it keeps earlier signature rows).
- **Do not re-run `extract` after the PDFs have been archived and freed** unless `signatures.csv` is backed up: it only sees PDFs still on disk. Run `translate match matrix directory` instead.

## 7. Policies and incentives
```bash
/usr/bin/python3 scripts/policy_contact_linker.py        # instruments -> signing contacts (centre + states)
/usr/bin/python3 scripts/new_policy_scanner.py --days 120   # PIB + ministry sites -> new/updated instruments
```
- The linker takes instruments from the curated list (`policy_windows.csv`), from titles ("Scheme", "Yojana", "Mission", "PLI", "Guidelines for …") and from the scanner's `discovered_instruments.csv`, finds the documents that name each one and attaches the people who signed them.
- The scanner reads the PIB release index (`india-trade-sector-policy-recommendations/scripts/pib_index.py --update`, a separate repo), shortlists by keyword, has an LLM classify each item (instrument or not, type, status, new or update), and for PIB items extracts outlay and period. When the LLM budget is exhausted it falls back to pattern extraction from the release text (`NO_LLM_DETAIL=1`).
- Contacts come from, in order: people who signed that instrument's documents; roster divisions named after it; the ministry's most active signers; the igod minister/secretary. `contact_evidence` records which.

## 8. Career events
```bash
/usr/bin/python3 scripts/career_tracker.py all --days 540 --max-articles 800
```
Collects appointment/transfer news (Whispers in the Corridors, PSU Watch, Sarkari Mirror — robots respected, 1 request/second, cached under the gitignored `data/career/articles/`), extracts events (regex on titles; an LLM for multi-officer reshuffle articles), adds each IAS officer's current posting and its effective date from the ER sheets, and attaches the latest event to every signer.

## 9. Markdown conversion
Local, text-layer only:
```bash
/usr/bin/python3 scripts/shards_to_md.py --only data__states__LA__pdf
```
Cloud with OCR (what produced the corpus):
```bash
/usr/bin/python3 scripts/cloud_md_launch.py feeder --workers 8   # keeps a live job queue of presigned URLs
/usr/bin/python3 scripts/cloud_md_launch.py aws --type c7g.2xlarge   # self-terminating instance, no credentials on it
nice /usr/bin/python3 scripts/local_md_runner.py --workers 4     # optional: idle laptop drains the queue from the other end
/usr/bin/python3 scripts/cloud_md_launch.py colab                 # or: a Colab cell running the same worker
```
- The instance receives only time-limited URLs for exactly the shards it processes and the places to put the markdown; it terminates itself when the queue is final and has a hard 14-hour stop.
- Throughput measured on 8 ARM cores: ~1 document per second for ordinary shards, ~0.2 per second for heavily scanned multi-language shards. The whole run cost ≈ $4 of AWS compute and about 14 hours.
- OCR cap: 10 pages per document, 150 dpi, `psm 6`, `OMP_THREAD_LIMIT=1` (see lessons).

## 10. Archive
PDFs are not kept in git. `archive_shards.py` zips each folder into ≈1.5 GB store-only shards and uploads them with rclone (`copy`, never `sync`), recording every file in `archive_manifest.csv`; `archive_free.py` deletes a local PDF only when it is in a verified shard **and** its text has been extracted; `archive_states_watch.sh` repeats both until the state pipeline ends. Restore a shard with `rclone copy <remote>/zips/<tree> /tmp/z && unzip`.

## 11. Reports
```bash
/usr/bin/python3 scripts/build_results_summary.py   # results_by_*.csv, RESULTS_SUMMARY.md
/usr/bin/python3 scripts/build_db.py                 # data/yellowpages.duckdb (use the Python that has duckdb)
python3 scripts/build_dashboard.py                   # dashboard/index.html
```
`scripts/refresh.sh` wires the directory stages together for a monthly cron run (`30 10 1 * *`).

## Operations: watching long runs
- `scripts/status_check.sh` prints disk, memory, running jobs, state progress and archive progress, and frees archived-and-extracted PDFs.
- `scripts/resource_guard.sh` pauses the pipeline (SIGSTOP) when free disk < 9 GB or free memory < 12%, resumes at 13 GB / 25%, and pauses the transfer and OCR processes at < 5 GB; it matches real Python processes only (never a shell that merely mentions a script name).

## Lessons that cost time
1. **Log files lie when Python output is buffered.** A "stuck" progress log was a healthy run; count output files instead, and run long jobs with `python -u`.
2. **Forking subprocesses from many Python threads can wedge the pool.** The crawl stage uses `xargs -P` with `perl -e 'alarm N; exec @ARGV'` so a hung site cannot hold a slot.
3. **Tesseract is multi-threaded by default.** With N parallel workers set `OMP_THREAD_LIMIT=1`, or the workers starve each other, time out, and produce silently empty documents.
4. **Free LLM tiers have per-day token caps per model** (Groq: 200,000 tokens/day each), not just per-minute limits. Cache successful answers only, never failures; cap `max_completion_tokens`; use a second model for a second budget.
5. **Never re-run an extract stage over a folder whose inputs were deleted** — it overwrites results with only what remains.
6. **Matching common two-token names needs an ambiguity rule.** Same name → several officers → no claim of a move.
7. **Cloud instances need an account-level check first**: this AWS user could use only S3 and EC2, with an 8-vCPU cap and almost no spot allowance, so the design avoids IAM roles and uses presigned URLs.
8. **A nightly backup elsewhere on the machine can spike disk use by ~10 GB**; the guard exists because of it.
