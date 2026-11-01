# MN — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (31 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 464 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 155 |
| PDFs with a detectable signature block | 157 |
| Signatures matched to a roster officer | 44 documents / 16 officers |
| Signatures not matched (person not in any roster, or moved) | 120 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Art and Culture Department, Manipur | 20 | 0 | 1 | 0 | 0 |
| Chandel | 6 | 0 | 2 | 2 | 1 |
| Churachandpur | 4 | 0 | 3 | 3 | 3 |
| Co-operative Department, Manipur | 18 | 0 | 8 | 3 | 1 |
| Consumer Affairs, Food and Public Distribution Department, Manipur | 8 | 0 | 5 | 4 | 1 |
| Council of Higher Secondary Education, Manipur | 14 | 0 | 7 | 0 | 0 |
| Department of Horticulture & Soil Conservation, Manipur | 11 | 0 | 4 | 0 | 0 |
| Department of Information & Communication Technology, Manipur | 25 | 0 | 9 | 0 | 0 |
| Directorate of Health Services, Manipur | 55 | 0 | 19 | 0 | 0 |
| Directorate of Printing and Stationary, Manipur | 11 | 0 | 9 | 8 | 1 |
| Directorate of SCERT, Manipur | 20 | 0 | 6 | 0 | 0 |
| Education (School) Department, Manipur | 27 | 0 | 7 | 1 | 1 |
| Family Welfare Department, Manipur | 10 | 0 | 6 | 1 | 1 |
| GRAS-Government Receipt Accounting System, Manipur | 4 | 0 | 0 | 0 | 0 |
| General Administration Department, Manipur | 19 | 0 | 7 | 0 | 0 |
| Information Technology Department, Manipur | 18 | 0 | 1 | 1 | 1 |
| Liberal College, Luwangsangbam, Manipur | 3 | 0 | 1 | 0 | 0 |
| Manipur Police, Manipur | 1 | 0 | 0 | 0 | 0 |
| Manipur Pollution Control Board (MPCB), Manipur | 12 | 0 | 4 | 0 | 0 |
| Manipur Renewable Energy Development Agency (MANIREDA), Manipur | 34 | 0 | 26 | 15 | 4 |
| Minority Affairs Department, Manipur | 52 | 0 | 6 | 1 | 1 |
| National Health Mission, Manipur | 17 | 0 | 3 | 0 | 0 |
| Planning Department, Manipur | 9 | 0 | 4 | 0 | 0 |
| Public Health Engineering Department, Manipur | 12 | 0 | 2 | 0 | 0 |
| Public Works Department (PWD), Manipur | 13 | 0 | 5 | 0 | 0 |
| Sarva Shiksha Abhiyan (SSA), Manipur | 13 | 0 | 4 | 0 | 0 |
| State Academy of Training (SAT), Manipur | 13 | 0 | 1 | 0 | 0 |
| Tamenglong | 7 | 0 | 5 | 4 | 2 |
| The Modern College, Imphal East, Manipur | 3 | 0 | 0 | 0 | 0 |
| Thoubal | 2 | 0 | 2 | 1 | 1 |
| e-District, Manipur | 3 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | HR: leave / pay / allowances / service rules | Other / unclassified | Procurement / tenders / GeM | Statutory rules / gazette notifications (G.S.R. / S.O.) | TOTAL |
|---|---|---|---|---|---|---|---|
| Mayanglambam Rajkumar Singh | Deputy Commissioner | Imphal West |  | 1 | 1 |  | 2 |
| Wakambam Suraj Singh | Joint Director | Manipur Renewable Energy Development Agency (MANIREDA), Manipur | 2 |  |  |  | 2 |
| Robert Sharma | Director(IT) | Information Technology Department, Manipur |  | 1 |  |  | 1 |
| Kachamthai Faiga Gangmei | Chief Executive Officer, ADC Tamenglong | Tamenglong |  |  |  | 1 | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### CEO, Manipur and Commissioner-cum-Secretary (Cooperation/Power) & Member Secretary (MANIREDA) & Officer-in-Charge, Public Grievances Redressal & Anti-Corruption Cell, Chief Minister’s Office in addition and Resident Commissioner, New Delhi in addition

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Commissioner-cum-Secretary (WR) and SCERT/Adult Education/End.-S) CEO/MIDA)/ Hr. & Tech

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Deputed for Long Term Scholarship Program - Master Programme on International Relations, Graduate School of Asia-Pacific Studies, Waseda University from October 2025 to September 2027

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Deputy Commissioner, Churachandpur, Manipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Deputy Commissioner, Thoubal

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Director (Printing & Stationery) in his grade pay

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| HR: appointment / transfer / posting / promotion |  |
| Other / unclassified |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Director (Tribal Affairs & Hills/TRI) & MD/MTDC

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |
| Scheme guidelines / implementation |  |

### Director, M/o Housing & Urban Affairs, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Imphal West

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Mayanglambam Rajkumar Singh** — Deputy Commissioner — dc-impw@nic.in (1) |
| Procurement / tenders / GeM | **Mayanglambam Rajkumar Singh** — Deputy Commissioner — dc-impw@nic.in (1) |

### Information Technology Department, Manipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Robert Sharma** — Director(IT) — robert.sharma@gov.in (1) |

### Joint Secretary (MAHUD)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Joint Secretary, M/o Housing and Urban Affairs, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Manipur Renewable Energy Development Agency (MANIREDA), Manipur

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules | **Wakambam Suraj Singh** — Joint Director — wsuraj_singh@yahoo.co.in (2) |

### Secretary, Department of Commerce, Ministry of Commerce and Industry, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Special Secretary (MI/CADA)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Office administration / housekeeping |  |
| Other / unclassified |  |

### Tamenglong

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Kachamthai Faiga Gangmei** — Chief Executive Officer, ADC Tamenglong — kachanthai.f@manipur.govin (1) |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Health Services, Manipur | Somorjit Salam | Director of Medical Education / Director of Medical Education, Manipur | 9 |  |
| Manipur Renewable Energy Development Agency (MANIREDA), Manipur | N. Praveen Singh | Director, MANIREDA | 8 |  |
| Education (School) Department, Manipur | Ng. Bhogendra Meitei | Director o f Educations), Manipur / Director of Education (S), | 6 |  |
| Council of Higher Secondary Education, Manipur | Kh. Ashikumar | Secretary / Secretary, | 4 |  |
| Directorate of Health Services, Manipur | N Hemantakumar Singh | Director of Health Services / Director of Health Services, Govt. of Manipur | 4 |  |
| Family Welfare Department, Manipur | L. Tomcha Khuman | Director / Director, | 4 |  |
| General Administration Department, Manipur | Asem Rangina Chanu | Deputy Secretary / Deputy Secretary , | 4 |  |
| Planning Department, Manipur | N. Kulkarani Devi | Executive Officer / Joint Director (Planning | 4 |  |
| Department of Horticulture & Soil Conservation, Manipur | K. Debadutta Sharma | Director | 3 |  |
| Public Works Department (PWD), Manipur | PWD Manipur | Secretary to Hon’ble Chief Minister, Manipur / Secretary to Hon’ble Chief Minister, Manipur . | 3 |  |
| Directorate of SCERT, Manipur | A. Romel Singh | Director, SCERT / Director, SCERT, Manipur | 2 |  |
| Family Welfare Department, Manipur | Sonia Oinam | Joint Secretary (Family Welfare / Joint Secretary(Family Welfare | 2 |  |
| Manipur Pollution Control Board (MPCB), Manipur | BISHWANATH SINHA | Joint Secretary to Government of India / Jt. Secy | 2 |  |
| Manipur Pollution Control Board (MPCB), Manipur | W. Roshan Singh | Secretary | 2 |  |
| Minority Affairs Department, Manipur | Koshoni Phimu | Deputy Secretary (MA), | 2 |  |
| National Health Mission, Manipur | Suresh K. Mohammed | Director (NRHM/RCH/Donor Coordination) | 2 |  |
| Sarva Shiksha Abhiyan (SSA), Manipur | N. Praveen Singh | Director, | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.