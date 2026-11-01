# KL — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (44 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 51 |
| PDFs with a detectable signature block | 51 |
| Signatures matched to a roster officer | 7 documents / 5 officers |
| Signatures not matched (person not in any roster, or moved) | 44 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Development and Farmers Welfare Department, Keral | 8 | 0 | 0 | 0 | 0 |
| Animal Husbandry Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| Archives Department, Kerala | 1 | 0 | 0 | 0 | 0 |
| Co-operation Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| Cochin University of Science and Technology, Kerala | 8 | 0 | 1 | 0 | 0 |
| College of Engineering Chengannur, Kerala | 8 | 0 | 6 | 0 | 0 |
| College of Engineering Thalassery, Kerala | 8 | 0 | 3 | 0 | 0 |
| College of Engineering Trikaripur, Kerala | 8 | 0 | 0 | 0 | 0 |
| College of Engineering Trivandrum, Kerala | 8 | 0 | 0 | 0 | 0 |
| College of Engineering Vadakara, Kerala | 7 | 0 | 0 | 0 | 0 |
| Dairy Development Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| Department of Sainik Welfare, Kerala | 8 | 0 | 0 | 0 | 0 |
| Directorate of Culture, Kerala | 8 | 0 | 2 | 0 | 0 |
| Directorate of Handlooms and Textiles, Kerala | 1 | 0 | 0 | 0 | 0 |
| Directorate of Health Services, Kerala | 8 | 0 | 1 | 0 | 0 |
| Directorate of Medical Education, Kerala | 8 | 0 | 4 | 0 | 0 |
| Directorate of Survey and Land Records, Kerala | 8 | 0 | 4 | 0 | 0 |
| Directorate of Technical Education, Kerala | 8 | 0 | 3 | 0 | 0 |
| Directorates of Factories and Boilers, Kerala | 3 | 0 | 0 | 0 | 0 |
| Drugs Control Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| Energy Management Centre, Kerala | 8 | 0 | 3 | 0 | 0 |
| Environment & Climate Change Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| Finance Department, Kerala | 4 | 0 | 0 | 0 | 0 |
| Food and Civil Supplies Department, Kerala | 1 | 0 | 0 | 0 | 0 |
| Forest and Wild Life Department, Kerala | 8 | 0 | 0 | 0 | 0 |
| General Education Department, Kerala | 8 | 0 | 1 | 0 | 0 |
| Goverment Engineering College Idukki, Kerala | 6 | 0 | 0 | 0 | 0 |
| Government Engineering College - Kozhikode, Kerala | 8 | 0 | 2 | 0 | 0 |
| Government Engineering College Palakkad, Sreekrishnapuram, Kerala | 8 | 0 | 0 | 0 | 0 |
| Handicrafts Development Corporation of Kerala Limited, Kerala | 4 | 0 | 1 | 0 | 0 |
| Kerala Academy for Skills Excellence (KASE), Kerala | 8 | 0 | 0 | 0 | 0 |
| Kerala Co-operative Milk Marketing Federation, Kerala | 8 | 0 | 4 | 2 | 1 |
| Kerala Co-operative Services Examination Board, Thiruvananthapuram, Kerala | 8 | 0 | 0 | 0 | 0 |
| Kerala Feeds Limited, Thrissur, Kerala | 8 | 0 | 2 | 0 | 0 |
| Kerala Financial Corporation (KFC), Kerala | 4 | 0 | 1 | 0 | 0 |
| Kerala Industrial Infrastructure Development Corporation (KINFRA), Kerala | 8 | 0 | 0 | 0 | 0 |
| Kerala Livestock Development Board, Kerala | 8 | 0 | 2 | 0 | 0 |
| Kerala Prisons & Correctional Services, Kerala | 8 | 0 | 5 | 1 | 1 |
| Kerala Shops and Commercial Establishments Workers Welfare Fund Board, Kerala | 8 | 0 | 0 | 0 | 0 |
| Kerala State Biodiversity Board, Kerala | 8 | 0 | 0 | 0 | 0 |
| Kerala State Disaster Management Authority, Kerala | 8 | 0 | 2 | 1 | 1 |
| Kerala State Housing Board, Kerala | 4 | 0 | 1 | 0 | 0 |
| Labour Commissionerate, Kerala | 8 | 0 | 3 | 3 | 2 |
| System for Easy and Legal Issuance of Fuel Permit and Fuel, Kerala | 1 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Other / unclassified | TOTAL |
|---|---|---|---|---|
| SREEJITH S | Deputy Collector RR | Kasaragod | 1 | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Director, NORKA

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Kasaragod

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **SREEJITH S** — Deputy Collector RR — rrkas.ker@nic.in (1) |

### Labour Commissioner

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |
| Other / unclassified |  |

### Secretary, General Education Department

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Revenue and Disaster Management Department

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| College of Engineering Chengannur, Kerala | A Praveen | Registrar | 3 |  |
| College of Engineering Thalassery, Kerala | A Praveen | Registrar | 3 |  |
| Directorate of Medical Education, Kerala | Viswanathan K V | DIRECTOR | 3 |  |
| Directorate of Survey and Land Records, Kerala | Sreekumar T | Officer / Officer. | 2 |  |
| Directorate of Technical Education, Kerala | SUMESH KUMAR.C | OFFICER | 2 |  |
| Kerala Feeds Limited, Thrissur, Kerala | M.N. Ramachandran M.P.I. Quarters | Director | 2 |  |
| Kerala Prisons & Correctional Services, Kerala | Balram Kumar Upadhyay | Director General of Prisons & Correctional Services | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.