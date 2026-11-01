# AP — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (47 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 700 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 83 |
| PDFs with a detectable signature block | 83 |
| Signatures matched to a roster officer | 8 documents / 7 officers |
| Signatures not matched (person not in any roster, or moved) | 75 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Acharya N. G. Ranga Agricultural University, Andhra Pradesh | 20 | 0 | 0 | 0 | 0 |
| Acharya Nagarjuna University, Centre for Distance Education, Andhra Pradesh | 20 | 0 | 0 | 0 | 0 |
| Alluri Sitharama Raju | 2 | 0 | 0 | 0 | 0 |
| Ananthapuramu | 11 | 0 | 0 | 0 | 0 |
| Andhra Pradesh Industrial Infrastructure Corporation | 20 | 0 | 2 | 1 | 1 |
| Andhra Pradesh Information Commission | 20 | 0 | 16 | 0 | 0 |
| Andhra Pradesh Mineral Development Corporation Limited | 20 | 0 | 0 | 0 | 0 |
| Andhra Pradesh Power Generation Corporation Limited (APGENCO), Andhra Pradesh | 20 | 0 | 5 | 0 | 0 |
| Andhra Pradesh Road Development Corporation (APRDC) | 11 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Disaster Management Authority (APSDMA) | 20 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Financial Corporation (APSFC), Andhra Pradesh | 4 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Level Police Recruitment Board | 17 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Road Transport Corporation (APSRTC) | 20 | 0 | 0 | 0 | 0 |
| Andhra Pradesh State Seeds Development Corporation Limited | 20 | 0 | 0 | 0 | 0 |
| Andhra University | 16 | 0 | 2 | 0 | 0 |
| Annamayya | 7 | 0 | 3 | 0 | 0 |
| Bapatla | 11 | 0 | 0 | 0 | 0 |
| Chittoor | 11 | 0 | 1 | 0 | 0 |
| Commissionerate of Health & Family Welfare, Andhra Pradesh | 2 | 0 | 0 | 0 | 0 |
| Consumer Affairs, Food and Civil Supplies Department, Andhra Pradesh | 20 | 0 | 1 | 0 | 0 |
| Directorate of Medical Education, Andhra Pradesh | 20 | 0 | 9 | 0 | 0 |
| Dr. B.R. Ambedkar Konaseema | 10 | 0 | 2 | 1 | 1 |
| Dr. Y.S.R Horticultural University, Andhra Pradesh | 20 | 0 | 3 | 0 | 0 |
| Dravidian University, Kuppam, Andhra Pradesh | 20 | 0 | 1 | 1 | 1 |
| East Godavari | 11 | 0 | 1 | 0 | 0 |
| Eluru | 3 | 0 | 0 | 0 | 0 |
| Fisheries Department, Andhra Pradesh | 1 | 0 | 0 | 0 | 0 |
| Guntur | 11 | 0 | 3 | 1 | 1 |
| Higher Education Department, Andhra Pradesh | 20 | 0 | 3 | 0 | 0 |
| Industries and Commerce Department, Andhra Pradesh | 20 | 0 | 1 | 1 | 1 |
| Institute for Development and Research in Banking Technology (IDRBT), Andhra Pradesh | 20 | 0 | 1 | 0 | 0 |
| Institute of Insurance and Risk Management (IIRM), Andhra Pradesh | 9 | 0 | 0 | 0 | 0 |
| Jawaharlal Nehru Technological University Hyderabad (JNTUH), Andhra Pradesh | 20 | 0 | 0 | 0 | 0 |
| Kakatiya University, Andhra Pradesh | 20 | 0 | 3 | 0 | 0 |
| Kakinada | 11 | 0 | 2 | 0 | 0 |
| Krishna | 6 | 0 | 0 | 0 | 0 |
| Labour, Employment Training and Factories Department, Andhra Pradesh | 8 | 0 | 2 | 0 | 0 |
| Mines and Geology Department, Andhra Pradesh | 20 | 0 | 9 | 1 | 1 |
| NALSAR University of Law, Andhra Pradesh | 16 | 0 | 0 | 0 | 0 |
| National Institute of Technology (NIT), Andhra Pradesh | 20 | 0 | 0 | 0 | 0 |
| Planning Department, Andhra Pradesh | 20 | 0 | 1 | 1 | 1 |
| Potti Sreeramulu Telugu University, Andhra Pradesh | 20 | 0 | 1 | 0 | 0 |
| Sri Venkateswara Institute Of Medical Sciences, Andhra Pradesh | 20 | 0 | 4 | 0 | 0 |
| Sri Venkateswara University, Tirupati, Andhra Pradesh | 18 | 0 | 3 | 0 | 0 |
| Sri Venkateswara Veterinary University, Tirupati, Andhra Pradesh | 20 | 0 | 3 | 1 | 1 |
| Vikrama Simhapuri University, Nellore, Andhra Pradesh | 20 | 0 | 0 | 0 | 0 |
| Yogi Vemana University, Andhra Pradesh | 4 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Procurement / tenders / GeM | Vigilance / disciplinary / court matters | TOTAL |
|---|---|---|---|---|---|
| C M Saikanth Varma, I.A.S. | Collector & District Magistrate | Guntur | 1 | 1 | 2 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Collector and District Magistrate, Dr.B.R. Ambedkar Konaseema District

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Guntur

| Topic | Contact officers (docs signed) |
|---|---|
| Procurement / tenders / GeM | **C M Saikanth Varma, I.A.S.** — Collector & District Magistrate — collector_gntr@ap.gov.in (1) |
| Vigilance / disciplinary / court matters | **C M Saikanth Varma, I.A.S.** — Collector & District Magistrate — collector_gntr@ap.gov.in (1) |

### Principal Secretary to Government, Finance Department

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Resident Commissioner, A.P. Bhavan, New Delhi.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Secretary to Government, Industries & Commerce Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Secretary to Government, School Education Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### State Project Director, Sarva Siksha Abhiyan (SSA)

| Topic | Contact officers (docs signed) |
|---|---|
| Procurement / tenders / GeM |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Andhra Pradesh Information Commission | MINNIE MATHEW | SECRETARY TO GOVERNMENT | 9 |  |
| Mines and Geology Department, Andhra Pradesh | GOPAL KRISHNA DWIVEDI | PRINCIPAL SECRETARY TO GOVERNMENT (MINES / PRINCIPAL SECRETARY TO GOVERNMENT(MINES | 4 |  |
| Andhra Pradesh Information Commission | JAGANNATH PRASAD MURTHY | PRINCIPAL SECRETARY TO GOVERNMENT. / SECRETARY TO GOVERNMENT | 2 |  |
| Andhra Pradesh Information Commission | S. BHALERAO | SECRETARY TO GOVERNMENT | 2 |  |
| Directorate of Medical Education, Andhra Pradesh | I.V.SUBBA RAO | PRINCIPAL SECRETARY TO GOVERNMENT | 2 |  |
| Directorate of Medical Education, Andhra Pradesh | L.V. SUBRAHMANYAM | PRINCIPAL SECRETARY TO GOVERNMENT (FP | 2 |  |
| Sri Venkateswara Veterinary University, Tirupati, Andhra Pradesh | M. MUTHA RAO | Officer In-Charge | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.