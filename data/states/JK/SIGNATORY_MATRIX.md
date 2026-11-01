# JK — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (42 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 27 |
| PDFs with a detectable signature block | 27 |
| Signatures matched to a roster officer | 1 documents / 1 officers |
| Signatures not matched (person not in any roster, or moved) | 26 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Bandipora | 3 | 0 | 0 | 0 | 0 |
| Baramulla | 11 | 0 | 0 | 0 | 0 |
| Bhadarwah Development Authority (J&K Tourism), Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Bhaderwah Campus, University of Jammu, Jammu and Kashmir | 6 | 0 | 0 | 0 | 0 |
| Budgam | 1 | 0 | 0 | 0 | 0 |
| Central University of Jammu, Jammu and Kashmir | 11 | 0 | 2 | 0 | 0 |
| Department of Food, Civil Supplies & Consumer Affairs, Jammu & Kashmir | 11 | 0 | 2 | 0 | 0 |
| Department of School Education, Jammu and Kashmir | 11 | 0 | 1 | 0 | 0 |
| Directorate of Economics and Statistics, Jammu and Kashmir | 4 | 0 | 1 | 0 | 0 |
| Directorate of School Education Jammu, Jammu and Kashmir | 11 | 0 | 1 | 0 | 0 |
| Divisional Commissioner Jammu, Jammu and Kashmir | 11 | 0 | 1 | 0 | 0 |
| Doda | 10 | 0 | 1 | 0 | 0 |
| Employee Performance Monitoring Portal (EPM), Jammu and Kashmir | 2 | 0 | 0 | 0 | 0 |
| Ganderbal | 4 | 0 | 0 | 0 | 0 |
| General Administration Department, Jammu and Kashmir | 4 | 0 | 0 | 0 | 0 |
| Government Degree College For Women, Anantnag, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Government Polytechnic for Women Jammu, Jammu and Kashmir | 11 | 0 | 1 | 0 | 0 |
| Government Women College, Gandhi Nagar, Jammu, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Health and Medical Education Department, Jammu and Kashmir | 11 | 0 | 2 | 0 | 0 |
| Hospitality and Protocol Department, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| J&K Tourism Development Corporation, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Jammu | 1 | 0 | 0 | 0 | 0 |
| Jammu and Kashmir Police, Jammu and Kashmir | 11 | 0 | 3 | 0 | 0 |
| Jammu and Kashmir Services Selection Board, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Kathua | 4 | 0 | 1 | 1 | 1 |
| Kulgam | 2 | 0 | 0 | 0 | 0 |
| Kupwara | 2 | 0 | 0 | 0 | 0 |
| Maulana Azad Memorial College, Jammu and Kashmir | 2 | 0 | 0 | 0 | 0 |
| New Central Sector Scheme for Industrial Development, Jammu and Kashmir | 4 | 0 | 1 | 0 | 0 |
| Pollution Control Committee, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Poonch | 4 | 0 | 1 | 0 | 0 |
| Pulwama | 2 | 0 | 0 | 0 | 0 |
| Rajouri | 2 | 0 | 1 | 0 | 0 |
| Ramban | 11 | 0 | 4 | 0 | 0 |
| Reasi | 5 | 0 | 0 | 0 | 0 |
| Sher-e-Kashmir University of Agricultural Sciences and Technology of Jammu (SKUAST-Jammu), Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Shopian | 2 | 0 | 0 | 0 | 0 |
| Shri Mata Vaishno Devi Shrine Board, Jammu and Kashmir | 1 | 0 | 1 | 0 | 0 |
| Shri Mata Vaishno Devi University, Katra, Jammu and Kashmir | 11 | 0 | 0 | 0 | 0 |
| Srinagar | 4 | 0 | 0 | 0 | 0 |
| University of Jammu, Jammu and Kashmir | 11 | 0 | 1 | 0 | 0 |
| University of Kashmir, Jammu and Kashmir | 11 | 0 | 2 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | HR: appointment / transfer / posting / promotion | TOTAL |
|---|---|---|---|---|
| SBDU Kathua | SBDU | Mission YUVA Portal, Jammu and Kashmir | 1 | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Mission YUVA Portal, Jammu and Kashmir

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **SBDU Kathua** — SBDU — sbdukathua08@gmail.com (1) |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Jammu and Kashmir Police, Jammu and Kashmir | Abhishek Mahajan | Director General of Police / Director General of Police, | 3 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.