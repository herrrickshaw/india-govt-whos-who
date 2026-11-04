# Data dictionary

Every table lives in `data/` (CSV) and, for the directory and signature tables, in `data/yellowpages.duckdb`. **All columns in the DuckDB
file are text** — cast numbers and dates (`cast(n_documents as int)`). Tables marked *CSV only* are not in the `.duckdb` file; read them with
`read_csv_auto('data/…csv')`. Row counts are as of 2 Nov 2026.

Common conventions: `ministry` is the name as used on the ministry's own site (with an acronym in brackets, e.g. `New and Renewable Energy (MNRE)`);
`doc_id` is the first 16 hex characters of the SHA-1 of the document URL and is the same everywhere (candidates, signatures, markdown);
dates are ISO `YYYY-MM-DD` or `YYYY-MM` when only the month is known; empty means unknown, not zero.

## 1. Directory (igod.gov.in)

### `organizations_index.csv` — 10,718 rows
Every organisation listed on igod.
| Column | Meaning |
|---|---|
| `branch` | `ug` union government, `sg` state government, `jud` judiciary, `leg` legislature, `int` international/missions, `apx` apex bodies |
| `state` | Two-letter state/UT code for state organisations (36 values) |
| `category_code`, `category` | igod category (e.g. `E002` ministries, `E003` departments) |
| `name`, `website`, `listing_url` | Organisation name, official site, the igod listing it came from |
| `igod_org_id` | igod detail-page id (blank for bodies with only an external link) |

### `org_contacts.csv` — 136 rows
Contact block from igod detail pages: `igod_org_id, org_name, branch, state, address, phone, fax, email, website, social` (emails de-obfuscated from `name[at]gov[dot]in`).

### `officials.csv` — 338 rows
igod "who's who": `igod_org_id, org_name, branch, state, name, designation, division, phones, office_address, email` — mainly ministers and secretaries.

## 2. Rosters (people)

### `ministry_officials.csv` — 10,679 rows, 47 ministries
Officers listed on each union ministry/department's own site (who's-who pages, officer directories, telephone-directory PDFs, shared-CMS directory endpoints).
| Column | Meaning |
|---|---|
| `ministry` | Ministry/department |
| `website` | Site the roster came from |
| `division` | Division, wing, section or scheme (blank if not published) |
| `name`, `designation` | As printed (honorifics kept) |
| `room`, `phones`, `email` | Contact details as published; emails de-obfuscated |
| `source_url` | The exact page or PDF |
| `agent_group` | Which collection batch added the row (`A`–`E`), blank for the original scrape |

### `states/state_officials.csv` — 19,306 rows (16,228 with a name)
State/UT department rosters: `state, department, website, name, designation, division, room, phones, email, source_url`. Rows without a name record a department that was scanned and had no usable who's-who (`source_url` says why).

### `ias_officers.csv` — 5,755 rows; `ips_officers.csv` — 4,553 rows
DoPT civil-list entries: cadre, allotment year, name in English/Hindi, source of recruitment, qualification, pay scale, domicile, `identity_no`, `current_posting`, `posting_wef` (date effective), `dob`, `er_sheet_url` (the DoPT ER sheet), plus other personal fields published in the list. See *Responsible use* in the README.

### `states/targets.csv` — 3,773 rows
State department sites crawled: `state, name, website, igod_org_id, category_code, slug`.

## 3. Documents

### `ministry_documents/data/all_documents.csv.gz` — 135,769 rows
One row per file found on a union ministry site: `ministry, slug, source` (`api` or `crawl`), `title, group, category, date, url, size, language, found_on`. Details and the per-site method are in `ministry_documents/README.md`.

### `data/md_index.csv.gz` — 40,708 rows
One row per converted document: `tree, shard` (which zip), `doc_id, source_url, ministry, title, date, pages, chars, bytes, sha1`, `method` (`pdftotext` or `tesseract:<languages>`), `script` (dominant script: `LATIN`, `DEVANAGARI`, `TAMIL`, …), `needs_ocr` (1 = no text could be read), `error`.

### `corpus/md/<tree>/<tree>-NNN.md.zip` — 109 shards
`<doc_id>.md` files plus `index.jsonl`; format in `corpus/README.md`.

## 4. Signatures (centre) — `data/signatories/`

### `signatory_directory.csv` — 2,958 rows
One row per distinct signer per ministry, built from the PDFs *before* any matching.
`ministry, signatory` (most common spelling), `name_variants, designations` (as printed, `|`-separated), `n_documents, first_date, last_date`, `email, phone` (printed under the signature, when present), `topics`, `example_titles, document_urls`, then the match to a roster officer: `roster_match, roster_designation, roster_email, match_confidence`, and the career layer: `latest_posting, latest_posting_org, latest_posting_date, latest_posting_source, latest_posting_url, posting_match_confidence, moved_since_signing, career_events_n`.

`moved_since_signing` is `yes` (a later post in a different organisation was found), `same org / older`, `ambiguous name` (the name matches several officers, so no claim is made), or `undated`.

### `notification_signatories.csv` — 9,861 rows
One row per signature found: `doc_id, sig_rank` (1 = last block on the page), `signatory, sig_designation` as printed, `match_status` (`matched` / `unmatched`), then the matched officer (`officer_id, officer_name, officer_designation, officer_ministry, officer_division, officer_email, officer_phones, roster`), `name_score` (0–1), `same_ministry`, `desig_match`, `confidence` (`high`, `medium`, `low (name only, other ministry)`, or `rejected (…)` for unmatched), and the document (`ministry, title, group, category, date, url`, `subject`, `file_number`, `scanned`).

### `officer_topic_matrix.csv` — 898 rows; `officer_topic_pivot.csv`
Per officer and topic: `n_documents, first_date, last_date, signed_as, confidence, example_titles, document_urls, doc_ids`. The pivot has one row per officer and one column per topic. Topic buckets are listed in `docs/METHODS_AND_LIMITATIONS.md`.

### `officer_documents.csv` — 2,444 rows
One row per matched document with its topic labels (the long form of the matrix).

### `candidates.csv`
The PDFs selected for reading: `doc_id, ministry, title, group, category, date, url, found_on, host`.

## 5. Signatures (states) — `data/states/`

Per state `data/states/<ST>/`: `candidates.csv` (selected PDFs), `signatures.csv` (one row per signature: `signatory_raw` in the original script, `signatory` romanised, `sig_script`, `sig_designation_raw`, `signatory_rule` (the rule-based romanisation kept for comparison), `sig_designation` in English, `subject_raw` / `subject` translated with `subject_language`, `script`, `ocr` (1 = OCR was used), `indic_chars` / `latin_chars`), `notification_signatories.csv` (matched as above), `officer_topic_matrix.csv`, `SIGNATORY_MATRIX.md`.
Extra "states": `UB` holds union bodies outside the ministries (447 signers), `TS` and `AP` include orders collected from their GOIR portals (`goir.telangana.gov.in`, 1305 orders; `goir.ap.gov.in`, 5689 orders, Jan–Apr 2025) under pseudo-URLs of the form `https://goir.telangana.gov.in/#<year><dept>_<type><gono>` or `.../dgo.ashx?gid=<id>&fileType=E`.
Combined: `notification_signatories_all_states.csv` (4,293 rows), `signatory_directory_all_states.csv` (2,823 rows), `translations.json` (cache of romanised names and translated subjects), `go_portals.csv` (each state's official order portal and whether it answered), `STATE_MATRIX.md` (overview).

## 6. Policies and incentives

### `policy_contacts.csv` — 334 rows (original curated join)
Open incentive instruments joined to the owning ministry's senior officials: `instrument, offering_entity, tier, status, instrument_type, source_url, matched_org, contact_name, designation, division, phones, email`. `policy_windows.csv` holds application windows: `instrument, application_start_date, application_end_date, notification_url, last_updated`.

### `policy_instruments_index.csv` — 718 rows (CSV only)
One row per instrument: `instrument, instrument_source` (`curated`, `documents`, `pib/ministry-site`), `level` (`centre` or state code), `ministry, n_documents, first_date, last_date, n_contacts, top_contacts, example_titles, example_urls`.

### `policy_contacts_from_documents.csv` — 1,227 rows (CSV only)
One row per instrument–contact: `instrument, instrument_source, level, ministry, contact, designation, evidence` (`signed documents` or `roster division matches instrument`), `n_documents_signed, last_signed, email, phone, roster_match, roster_designation, latest_posting, latest_posting_date, moved_since_signing, document_urls`.

### `new_policies_incentives.csv` — 768 rows (CSV only); `discovered_instruments.csv` — 233 rows
Items from PIB and ministry sites since 4 Jul 2026 that look like policy news: `source, date, ministry, title, url, subject`, then the model's classification (`is_instrument, instrument, type, status, new_or_update, beneficiaries, summary`), details pulled from the release text (`outlay, period, eligibility, how_to_apply, nodal_body` — mostly `outlay` and `period`), what the repository already knows (`known_curated_instrument, seen_in_document_index, docs_in_index`) and the best contacts (`contacts, contact_evidence`).

### `pib_ministry_contacts.csv` — 181 rows
PIB press activity per ministry (releases per year, last 90 days, latest release) with the top contacts.

## 7. People over time

### `career/career_events.csv` — 7,083 rows (CSV only)
`name, service, cadre, batch, event` (`appointed`, `transferred`, `current posting (ER sheet)`…), `new_post, new_org, event_date, source` (`dopt_er_sheet`, `sarkarimirror`, `psuwatch`, `whispersinthecorridors`), `url, snippet, method, name_key`.

## 8. Coverage and bookkeeping

| File | Contents |
|---|---|
| `results_by_ministry.csv` (81 rows), `results_by_state.csv` (36) | Funnel per ministry/state: documents indexed, read, signed, signers, roster size, matches, instruments |
| `RESULTS_SUMMARY.md`, `MINISTRY_PLAN.md` | The same as readable tables, and the plan to close gaps |
| `archive_manifest.csv` | Which cloud shard holds each archived PDF: `file, size, remote_zip, zip_size` |
| `ministry_documents/data/coverage.csv`, `fingerprint.csv`, `targets.csv` | Per-site crawl status and site platform |
| `agents/group*/` | Raw officer lists and source URLs collected per ministry group |

## Keys that join the tables

- `doc_id` joins `md_index`, `candidates`, `signatures`, `notification_signatories`, `officer_documents`.
- `officer_id` (a hash of roster, ministry, name, designation) joins `notification_signatories`, `officer_topic_matrix`, `officer_documents`.
- `ministry` joins the directories, signatory tables, instrument tables and results tables (spelling is consistent because it comes from the same site list).
- `igod_org_id` joins `organizations_index`, `org_contacts`, `officials`.
