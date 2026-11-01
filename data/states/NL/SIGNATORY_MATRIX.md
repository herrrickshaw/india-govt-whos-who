# NL — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (19 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 156 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 35 |
| PDFs with a detectable signature block | 35 |
| Signatures matched to a roster officer | 2 documents / 2 officers |
| Signatures not matched (person not in any roster, or moved) | 33 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Department of Taxes, Nagaland | 20 | 0 | 1 | 1 | 1 |
| Directorate of Home Guards, Civil Defence & State Disaster Response Force (SDRF), Nagaland | 3 | 0 | 0 | 0 | 0 |
| Directorate of Technical Education, Nagaland | 20 | 0 | 14 | 0 | 0 |
| Economics and Statistics Department, Nagaland | 6 | 0 | 3 | 0 | 0 |
| Food and Civil Supplies Department, Nagaland | 1 | 0 | 0 | 0 | 0 |
| Higher Education Department, Nagaland | 20 | 0 | 1 | 0 | 0 |
| Home Department, Nagaland | 4 | 0 | 1 | 0 | 0 |
| Information Technology and Communications Department, Nagaland | 1 | 0 | 0 | 0 | 0 |
| Information and Public Relations Department, Nagaland | 5 | 0 | 0 | 0 | 0 |
| Kiphire | 7 | 0 | 1 | 0 | 0 |
| Motor Vehicles Department, Nagaland | 20 | 0 | 3 | 0 | 0 |
| New and Renewable Energy Department, Nagaland | 1 | 0 | 0 | 0 | 0 |
| Peren | 1 | 0 | 0 | 0 | 0 |
| Planning and Transformation Department, Nagaland | 10 | 0 | 4 | 0 | 0 |
| Police Department, Nagaland | 12 | 0 | 1 | 1 | 1 |
| Public Health Engineering Department, Nagaland | 4 | 0 | 3 | 0 | 0 |
| School Education Department, Nagaland | 16 | 0 | 2 | 0 | 0 |
| Tuensang | 2 | 0 | 1 | 0 | 0 |
| Wokha | 3 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Chief Secretary, Nagaland

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST |  |

### Home Commissioner, Principal Secretary to CM, Nagaland and Principal Resident Commissioner, Nagaland House, New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Technical Education, Nagaland | VIPULHOU LHOUNGU | Director | 12 |  |
| Motor Vehicles Department, Nagaland | ELIAS T. LOTHA | Commissioner / Commissioner. | 3 |  |
| Planning and Transformation Department, Nagaland | R. RAMAKRISHNAN | Principal Secretary to the Govt. of Nagaland | 3 |  |
| Economics and Statistics Department, Nagaland | NEIDILHOU ANGAMI | . Director & HOD / Additional Director & HoD | 2 |  |
| School Education Department, Nagaland | RAZOUSEYI VESE | Director | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.