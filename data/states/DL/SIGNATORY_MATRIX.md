# DL — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (53 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 71 |
| PDFs with a detectable signature block | 71 |
| Signatures matched to a roster officer | 2 documents / 2 officers |
| Signatures not matched (person not in any roster, or moved) | 69 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| A & U Tibbia College & Hospital, Delhi | 7 | 0 | 3 | 0 | 0 |
| Administrative Reforms Department, Delhi | 7 | 0 | 2 | 0 | 0 |
| Ambedkar Institute of Advanced Communication Technologies & Research, Delhi | 3 | 0 | 1 | 0 | 0 |
| Archaeology Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Art, Culture and Language Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Bachelor of Education Program, Delhi | 2 | 0 | 1 | 0 | 0 |
| Ch. Brahm Prakash Government Engineering College, Delhi | 1 | 0 | 1 | 0 | 0 |
| Ch. Brahm Prakash Industrial Training Institute, Jaffarpur, Delhi | 7 | 0 | 2 | 0 | 0 |
| Chit Fund Department, Delhi | 5 | 0 | 1 | 0 | 0 |
| College of Art, Delhi | 7 | 0 | 0 | 0 | 0 |
| DIET, Bhola Nath Nagar, Shahdara, Delhi | 4 | 0 | 1 | 0 | 0 |
| DIET, Darya Ganj, New Delhi | 1 | 0 | 1 | 0 | 0 |
| DIET, Ghumanhera, New Delhi | 3 | 0 | 1 | 0 | 0 |
| DIET, Karkardooma, Delhi | 1 | 0 | 1 | 0 | 0 |
| DIET, Keshav Puram, New Delhi | 1 | 0 | 1 | 0 | 0 |
| DIET, Moti Bagh, New Delhi | 2 | 0 | 1 | 0 | 0 |
| DIET, Pitampura, Delhi | 1 | 0 | 1 | 0 | 0 |
| DIET, R K Puram, New Delhi | 7 | 0 | 1 | 0 | 0 |
| DIET, Rajinder Nagar, New Delhi | 4 | 0 | 1 | 0 | 0 |
| Delhi Archives Department, Delhi | 4 | 0 | 1 | 0 | 0 |
| Delhi Sanskrit Academy, Delhi | 2 | 0 | 1 | 0 | 0 |
| Department of Delhi Fire Service | 7 | 0 | 3 | 0 | 0 |
| Department of Homeopathy, Delhi | 7 | 0 | 3 | 0 | 0 |
| Department of Sociology, Delhi School of Economics | 1 | 0 | 0 | 0 | 0 |
| Development Department, Delhi | 7 | 0 | 2 | 0 | 0 |
| Directorate General of Health Services, Delhi | 7 | 0 | 0 | 0 | 0 |
| Directorate of AYUSH, Delhi | 7 | 0 | 4 | 0 | 0 |
| Directorate of Agricultural Marketing, Delhi | 7 | 0 | 2 | 0 | 0 |
| Directorate of Employment, Delhi | 7 | 0 | 1 | 0 | 0 |
| Directorate of Higher Education, Delhi | 7 | 0 | 1 | 0 | 0 |
| Directorate of Information & Publicity, Delhi | 7 | 0 | 1 | 0 | 0 |
| Directorate of National Cadet Corps, Delhi | 7 | 0 | 6 | 0 | 0 |
| Directorate of Prosecution, Delhi | 7 | 0 | 1 | 0 | 0 |
| Directorate of Small Savings, Delhi | 6 | 0 | 3 | 0 | 0 |
| Directorate of Training and Technical Education, Delhi | 7 | 0 | 0 | 0 | 0 |
| District Session Judge Department, Delhi | 7 | 0 | 2 | 0 | 0 |
| Dr. B. R. Ambedkar University, Delhi | 7 | 0 | 0 | 0 | 0 |
| Drugs Control Department, Delhi | 7 | 0 | 4 | 0 | 0 |
| Education Department, Delhi | 7 | 0 | 0 | 0 | 0 |
| Enviornment Department, Delhi | 7 | 0 | 2 | 1 | 1 |
| Excise, Entertainment & Luxury Tax Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Finance Department, Delhi | 7 | 0 | 4 | 0 | 0 |
| Food Safety Department, Delhi | 7 | 0 | 2 | 0 | 0 |
| Food Supplies and Consumer Affairs Department, Delhi | 7 | 0 | 0 | 0 | 0 |
| Forest Department, Delhi | 7 | 0 | 0 | 0 | 0 |
| General Administration Department, Delhi | 7 | 0 | 0 | 0 | 0 |
| Health and Family Welfare, Delhi | 7 | 0 | 0 | 0 | 0 |
| Home Department, Delhi | 7 | 0 | 0 | 0 | 0 |
| Income Tax Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Industries Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Information Technology Department, Delhi | 7 | 0 | 2 | 1 | 1 |
| Irrigation and Flood Control Department, Delhi | 7 | 0 | 1 | 0 | 0 |
| Jal Board Department, Delhi | 7 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Administrative Reforms Department, Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| HR: leave / pay / allowances / service rules |  |

### Secretary (UD, E&FC), Govt. of NCT of Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of National Cadet Corps, Delhi | CMDE CAESAR BASU | DIRECTOR, NCC | 3 |  |
| Finance Department, Delhi | SANJEEV SHARMA | OFFICER, IFMS / OFFICER, [FMS | 3 |  |
| Department of Delhi Fire Service | A.NEDUNCHEZHIY AN | Principal Director | 2 |  |
| Development Department, Delhi | PAWAN CHOPRA | DEPUTY DIRECTOR (HQ | 2 |  |
| Directorate of AYUSH, Delhi | Yogita Munjal | Director (AYU`H / Secretary, Executive Body, DSAS | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.