# CH — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (29 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 594 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 68 |
| PDFs with a detectable signature block | 68 |
| Signatures matched to a roster officer | 8 documents / 3 officers |
| Signatures not matched (person not in any roster, or moved) | 61 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| A. C. Joshi Library, Panjab University, Chandigarh | 39 | 0 | 3 | 0 | 0 |
| Agriculture Department, Chandigarh | 43 | 0 | 12 | 6 | 3 |
| Animal Husbandry and Fisheries Department, Chandigarh | 20 | 0 | 0 | 0 | 0 |
| Centralized Online Admission Portal, Chandigarh | 5 | 0 | 0 | 0 | 0 |
| Centre for Distance and Online Education, Panjab University, Chandigarh | 43 | 0 | 2 | 0 | 0 |
| Chandigarh College of Engineering and Technology (Diploma Wing) | 24 | 0 | 0 | 0 | 0 |
| Chandigarh Industrial and Tourism Development Corporation (CITCO) - Luxury Hotels in Chandigarh | 15 | 0 | 0 | 0 | 0 |
| Chandigarh Pollution Control Committee | 16 | 0 | 1 | 0 | 0 |
| Chandigarh Transport Undertaking | 43 | 0 | 1 | 0 | 0 |
| Cultural Affairs Department, Chandigarh | 8 | 0 | 0 | 0 | 0 |
| Department of Economics, Panjab University, Chandigarh | 18 | 0 | 1 | 0 | 0 |
| Department of Gandhian and Peace Studies, Panjab University, Chandigarh | 42 | 0 | 3 | 0 | 0 |
| Department of Geology, Panjab University, Chandigarh | 43 | 0 | 16 | 0 | 0 |
| Department of Laws, Panjab University, Chandigarh | 43 | 0 | 6 | 0 | 0 |
| Education Department, Chandigarh | 1 | 0 | 1 | 0 | 0 |
| Environment Department, Chandigarh | 25 | 0 | 9 | 0 | 0 |
| Government Medical College and Hospital, Chandigarh | 3 | 0 | 0 | 0 | 0 |
| Government Rehabilitation Institute for Intellectual Disabilities (GRIID), Chandigarh | 11 | 0 | 3 | 0 | 0 |
| Joint Admission Committee, Chandigarh | 12 | 0 | 0 | 0 | 0 |
| Mathematics Department, Panjab University, Chandigarh | 13 | 0 | 2 | 0 | 0 |
| P.U. Swami Sarvanand Giri Regional Centre, Panjab University, Chandigarh | 43 | 0 | 2 | 0 | 0 |
| Panjab University Examination Results, Chandigarh | 3 | 0 | 0 | 0 | 0 |
| Panjab University, Chandigarh | 43 | 0 | 2 | 0 | 0 |
| Post Graduate Government College for Girls, Sector 11, Chandigarh | 6 | 0 | 2 | 0 | 0 |
| Post Graduate Government College, Sector 11, Chandigarh | 7 | 0 | 0 | 0 | 0 |
| Public Relations Department, Chandigarh | 17 | 0 | 2 | 2 | 1 |
| Punjab Engineering College (PEC), Chandigarh | 5 | 0 | 0 | 0 | 0 |
| Revenue Department, Chandigarh | 1 | 0 | 0 | 0 | 0 |
| e-Gazette, Chandigarh | 2 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Acts / commencement / legislation | Other / unclassified | Statutory rules / gazette notifications (G.S.R. / S.O.) | TOTAL |
|---|---|---|---|---|---|---|
| Shri Mandip Singh Brar, IAS | Home Secretary | Chandigarh | 2 | 2 | 2 | 6 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### 1. Chairman (CITCO), Chief Electoral Officer & Secretary (Personnel & Estt., Hospitality), Chandigarh 2. Secretary (Personnel/HAC/Hospitality) 3. Chief Electoral Officer, Chandigarh

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Chandigarh

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Mandip Singh Brar, IAS** — Home Secretary — hs-chd@nic.in (2) |
| Other / unclassified | **Shri Mandip Singh Brar, IAS** — Home Secretary — hs-chd@nic.in (2) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Mandip Singh Brar, IAS** — Home Secretary — hs-chd@nic.in (2) |

### Chief Secretary, Chandigarh

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Department of Geology, Panjab University, Chandigarh | Mahesh Thakur | Principal Investigator (DST Project / Principal Investigator, DST Project, | 8 |  |
| Department of Laws, Panjab University, Chandigarh | Lakshita Goyal | Joint Secretary | 2 |  |
| Department of Laws, Panjab University, Chandigarh | Y P Verma | Registrar | 2 |  |
| Environment Department, Chandigarh | ARUN KUMAR GUPTA | Principal Secretary Environment, | 2 |  |
| Environment Department, Chandigarh | Chandigarh Administration | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.