# ML — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (33 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 60 |
| PDFs with a detectable signature block | 60 |
| Signatures matched to a roster officer | 20 documents / 6 officers |
| Signatures not matched (person not in any roster, or moved) | 42 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture and Family Welfare Department, Meghalaya | 11 | 0 | 6 | 0 | 0 |
| Animal Husbandry and Veterinary Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| Arts and Culture Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| Border Areas Development Department, Meghalaya | 11 | 0 | 1 | 0 | 0 |
| Co-operation Department, Meghalaya | 11 | 0 | 1 | 1 | 1 |
| Commerce and Industries Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| Directorate of Civil Defence & Home Guards, Meghalaya | 2 | 0 | 0 | 0 | 0 |
| District Council Affairs Department, Meghalaya | 11 | 0 | 4 | 4 | 1 |
| East Garo Hills | 2 | 0 | 0 | 0 | 0 |
| East Jaintia Hills | 3 | 0 | 0 | 0 | 0 |
| East Khasi Hills | 10 | 0 | 3 | 1 | 1 |
| Education Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| Fire & Emergency Service, Meghalaya | 11 | 0 | 1 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| General Administration Department, Meghalaya | 11 | 0 | 2 | 2 | 1 |
| Health and Family Welfare Department, Meghalaya | 11 | 0 | 1 | 0 | 0 |
| Home (Police) Department, Meghalaya | 11 | 0 | 5 | 0 | 0 |
| Home (Political) Department, Meghalaya | 11 | 0 | 7 | 3 | 2 |
| Housing Department, Meghalaya | 11 | 0 | 0 | 0 | 0 |
| Information Technology & Communication Department, Meghalaya | 11 | 0 | 1 | 0 | 0 |
| Information and Public Relations Department, Meghalaya | 11 | 0 | 2 | 1 | 1 |
| Labour and Employment Department, Meghalaya | 2 | 0 | 0 | 0 | 0 |
| Martin Luther Christian University, (MICU), Shillong, Meghalaya | 11 | 0 | 2 | 0 | 0 |
| Meghalaya Board of School Education (MBOSE), Meghalaya | 3 | 0 | 0 | 0 | 0 |
| Meghalaya State Agricultural Marketing Board, Meghalaya | 11 | 0 | 3 | 0 | 0 |
| Meghalaya State Commission for Protection of Child Rights, Meghalaya | 4 | 0 | 1 | 0 | 0 |
| Meghalaya State Electricity Regulatory Commission (MSERC), Meghalaya | 11 | 0 | 8 | 6 | 1 |
| Meghalaya State Higher Education Council | 6 | 0 | 0 | 0 | 0 |
| Meghalaya State Planning Board, Meghalaya | 11 | 0 | 1 | 0 | 0 |
| Mid Day Meal Scheme, Directorate of School Education & Literacy, Meghalaya | 8 | 0 | 2 | 0 | 0 |
| Office of the State Commissioner for Persons with Disabilities, Meghalaya | 11 | 0 | 4 | 2 | 1 |
| State Institute of Rural Development (SIRD), Meghalaya | 11 | 0 | 1 | 0 | 0 |
| The Institute of Chartered Financial Analysts of India University (ICFAI), Meghalaya | 7 | 0 | 4 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Acts / commencement / legislation | Budget / sanction / release of funds / grants | Committees / meetings / minutes / constitution of | Customs / tariff / duty / GST | HR: appointment / transfer / posting / promotion | Licensing / approvals / standards / enlistment | Other / unclassified | Scheme guidelines / implementation | Statutory rules / gazette notifications (G.S.R. / S.O.) | TOTAL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shri. Cyril V. Darlong Diengdoh, IAS | Commissioner & Secretary | General Administration Department, Meghalaya | 1 | 1 | 2 | 1 | 2 | 1 | 2 |  | 1 | 11 |
| Shri. P. S. Lyngdoh | Superintendent of Taxes, Shillong | Office of the State Commissioner for Persons with Disabilities, Meghalaya | 1 |  | 1 |  |  |  |  |  |  | 2 |
| Shri Sampath Kumar IAS | Chairman (SCSM) Principal Secretary, Health & Family Welfare Department, Govt. of Meghalaya | State Cancer Society of Meghalaya, Govt. of Meghalaya |  |  | 1 |  |  |  |  | 1 |  | 2 |
| Dr. P. Vijay Kumar IAS | Commissioner and Secretary, Finance Department, Government of Meghalaya, Shillong | State Cancer Society of Meghalaya, Govt. of Meghalaya |  |  |  |  |  |  | 1 |  |  | 1 |
| Shri D Lyngdoh | DDMO East Jaintia Hills | State Disaster Management Authority, Shillong, Meghalaya |  |  |  |  |  |  | 1 |  |  | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### General Administration Department, Meghalaya

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (1) |
| Budget / sanction / release of funds / grants | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (2) |
| Customs / tariff / duty / GST | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (2) |
| Licensing / approvals / standards / enlistment | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (1) |
| Other / unclassified | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (2) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri. Cyril V. Darlong Diengdoh, IAS** — Commissioner & Secretary — cyril.diengdoh@gov.in (1) |

### Meghalaya State Electricity Regulatory Commission (MSERC), Meghalaya

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution |  |
| Budget / sanction / release of funds / grants |  |
| Committees / meetings / minutes / constitution of |  |
| Customs / tariff / duty / GST |  |
| Licensing / approvals / standards / enlistment |  |
| Other / unclassified |  |

### Office of the State Commissioner for Persons with Disabilities, Meghalaya

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri. P. S. Lyngdoh** — Superintendent of Taxes, Shillong — pynsan13@gmail.com (1) |
| Committees / meetings / minutes / constitution of | **Shri. P. S. Lyngdoh** — Superintendent of Taxes, Shillong — pynsan13@gmail.com (1) |

### State Cancer Society of Meghalaya, Govt. of Meghalaya

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of | **Shri Sampath Kumar IAS** — Chairman (SCSM) Principal Secretary, Health & Family Welfare Department, Govt. of Meghalaya — officeofsampthkumar2020@gmail.com (1) |
| Other / unclassified | **Dr. P. Vijay Kumar IAS** — Commissioner and Secretary, Finance Department, Government of Meghalaya, Shillong — vijaymeghalaya@gmail.com (1) |
| Scheme guidelines / implementation | **Shri Sampath Kumar IAS** — Chairman (SCSM) Principal Secretary, Health & Family Welfare Department, Govt. of Meghalaya — officeofsampthkumar2020@gmail.com (1) |

### State Disaster Management Authority, Shillong, Meghalaya

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Shri D Lyngdoh** — DDMO East Jaintia Hills — ddma-ejh-meg@gov.in luid82@gmail.com (1) |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Agriculture and Family Welfare Department, Meghalaya | P. Kharkongor | Principal Secretary to the Govt. of Meghalaya / Principal Secretary to the Govt. of Meghalaya, | 5 |  |
| Home (Political) Department, Meghalaya | W. KHYLLEP | Commissioner & Secretary to the Govt. of Meghalaya, / Secretary to the Govt. of Meghalaya, | 3 |  |
| East Khasi Hills | Hon'ble Minister | Secretary. | 2 |  |
| East Khasi Hills | Rebecca V. Suchiang | Secretary | 2 |  |
| Office of the State Commissioner for Persons with Disabilities, Meghalaya | By Orders Etc | Deputy secretary Hie Govt. of Meghalaya, / Deputy seoretar MS Govt of Meghalaya, | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.