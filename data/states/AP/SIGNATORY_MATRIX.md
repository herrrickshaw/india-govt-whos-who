# AP — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (37 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 34 |
| PDFs with a detectable signature block | 34 |
| Signatures matched to a roster officer | 3 documents / 3 officers |
| Signatures not matched (person not in any roster, or moved) | 31 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Acharya N. G. Ranga Agricultural University, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Acharya Nagarjuna University, Centre for Distance Education, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Alluri Sitharama Raju | 2 | 0 | 0 | 0 | 0 |
| Andhra Pradesh Industrial Infrastructure Corporation | 9 | 0 | 1 | 0 | 0 |
| Andhra Pradesh Information Commission | 9 | 0 | 9 | 0 | 0 |
| Andhra Pradesh Mineral Development Corporation Limited | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh Power Generation Corporation Limited (APGENCO), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh Road Development Corporation (APRDC) | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Disaster Management Authority (APSDMA) | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Financial Corporation (APSFC), Andhra Pradesh | 4 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Level Police Recruitment Board | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Road Transport Corporation (APSRTC) | 9 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Seeds Development Corporation Limited | 9 | 0 | 0 | 0 | 0 |
| Andhra University | 9 | 0 | 2 | 0 | 0 |
| Commissionerate of Health & Family Welfare, Andhra Pradesh | 2 | 0 | 0 | 0 | 0 |
| Consumer Affairs, Food and Civil Supplies Department, Andhra Pradesh | 9 | 0 | 1 | 0 | 0 |
| Directorate of Medical Education, Andhra Pradesh | 9 | 0 | 3 | 0 | 0 |
| Dr. Y.S.R Horticultural University, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Dravidian University, Kuppam, Andhra Pradesh | 9 | 0 | 1 | 1 | 1 |
| Fisheries Department, Andhra Pradesh | 1 | 0 | 0 | 0 | 0 |
| Higher Education Department, Andhra Pradesh | 9 | 0 | 1 | 0 | 0 |
| Industries and Commerce Department, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Institute for Development and Research in Banking Technology (IDRBT), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Institute of Insurance and Risk Management (IIRM), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Jawaharlal Nehru Technological University Hyderabad (JNTUH), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Kakatiya University, Andhra Pradesh | 9 | 0 | 2 | 0 | 0 |
| Labour, Employment Training and Factories Department, Andhra Pradesh | 8 | 0 | 2 | 0 | 0 |
| Mines and Geology Department, Andhra Pradesh | 9 | 0 | 5 | 1 | 1 |
| NALSAR University of Law, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| National Institute of Technology (NIT), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Planning Department, Andhra Pradesh | 9 | 0 | 1 | 1 | 1 |
| Potti Sreeramulu Telugu University, Andhra Pradesh | 9 | 0 | 1 | 0 | 0 |
| Sri Venkateswara Institute Of Medical Sciences, Andhra Pradesh | 9 | 0 | 3 | 0 | 0 |
| Sri Venkateswara University, Tirupati, Andhra Pradesh | 9 | 0 | 1 | 0 | 0 |
| Sri Venkateswara Veterinary University, Tirupati, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Vikrama Simhapuri University, Nellore, Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Yogi Vemana University, Andhra Pradesh | 4 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Principal Secretary to Government, Finance Department

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Resident Commissioner, A.P. Bhavan, New Delhi.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Secretary to Government, School Education Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Andhra Pradesh Information Commission | MINNIE MATHEW | SECRETARY TO GOVERNMENT | 8 |  |
| Mines and Geology Department, Andhra Pradesh | GOPAL KRISHNA DWIVEDI | PRINCIPAL SECRETARY TO GOVERNMENT (MINES / PRINCIPAL SECRETARY TO GOVERNMENT(MINES | 4 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.