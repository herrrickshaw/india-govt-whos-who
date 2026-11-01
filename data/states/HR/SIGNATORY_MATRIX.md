# HR — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (44 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 69 |
| PDFs with a detectable signature block | 69 |
| Signatures matched to a roster officer | 18 documents / 11 officers |
| Signatures not matched (person not in any roster, or moved) | 56 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Department, Haryana | 9 | 0 | 0 | 0 | 0 |
| Ambala | 9 | 0 | 0 | 0 | 0 |
| Archives Department, Haryana | 9 | 0 | 1 | 0 | 0 |
| Art and Cultural Affairs Department, Haryana | 1 | 0 | 0 | 0 | 0 |
| Bhiwani | 3 | 0 | 0 | 0 | 0 |
| Board of School Education Haryana | 9 | 0 | 0 | 0 | 0 |
| Charkhi Dadri | 1 | 0 | 1 | 0 | 0 |
| Chief Secretary Office, Haryana | 9 | 0 | 7 | 0 | 0 |
| Civil Aviation Department, Haryana | 2 | 0 | 2 | 1 | 1 |
| Climate Change Cell, Haryana | 1 | 0 | 0 | 0 | 0 |
| Dakshin Haryana Bijli Vitran Nigam (DHBVN), Haryana | 9 | 0 | 2 | 0 | 0 |
| Department of Medical Education and Research, Haryana | 9 | 0 | 4 | 0 | 0 |
| Directorate of Medical Education & Research, Haryana | 9 | 0 | 1 | 0 | 0 |
| Directorate of Secondary Education, Haryana | 5 | 0 | 2 | 1 | 1 |
| Directorate of Skill Development & Industrial Training, Haryana | 9 | 0 | 4 | 1 | 1 |
| Directorate of Supplies and Disposals, Haryana | 6 | 0 | 1 | 0 | 0 |
| Divisional Commissioner Hisar, Haryana | 9 | 0 | 1 | 0 | 0 |
| Economic and Statistical Analysis Department, Haryana | 7 | 0 | 4 | 1 | 1 |
| Electronics and Information Technology Department, Haryana | 9 | 0 | 2 | 0 | 0 |
| Elementary Education Department, Haryana | 5 | 0 | 0 | 0 | 0 |
| Employment Department, Haryana | 9 | 0 | 3 | 0 | 0 |
| Excise and Taxation Department, Haryana | 9 | 0 | 5 | 4 | 1 |
| Fatehabad | 2 | 0 | 0 | 0 | 0 |
| Finance Department, Haryana | 9 | 0 | 5 | 0 | 0 |
| Fisheries Department, Haryana | 1 | 0 | 0 | 0 | 0 |
| Food and Drugs Administration Department, Haryana | 9 | 0 | 5 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Haryana | 3 | 0 | 1 | 1 | 1 |
| Forests Department, Haryana | 9 | 0 | 3 | 1 | 1 |
| Gurugram | 4 | 0 | 0 | 0 | 0 |
| Haryana Forest Development Corporation, Haryana | 4 | 0 | 0 | 0 | 0 |
| Haryana Land Reclamation and Development Corporation, Haryana | 9 | 0 | 0 | 0 | 0 |
| Haryana Power Generation Corporation Limited, Haryana | 9 | 0 | 2 | 0 | 0 |
| Haryana Right To Service Commission, Haryana | 9 | 0 | 0 | 0 | 0 |
| Haryana Shehri Vikas Pradhikaran, Haryana | 9 | 0 | 0 | 0 | 0 |
| Haryana State Industrial & Infrastructure Development Corporation Ltd. (HSIIDC), Haryana | 9 | 0 | 0 | 0 | 0 |
| Haryana State Technical Education Society (HSTES), Haryana | 9 | 0 | 0 | 0 | 0 |
| Haryana Women Development Corporation Ltd., Haryana | 1 | 0 | 0 | 0 | 0 |
| Health Department, Haryana | 9 | 0 | 3 | 3 | 2 |
| Higher Education Department, Haryana | 9 | 0 | 2 | 2 | 2 |
| Home & Administration of Justice Department, Haryana | 9 | 0 | 3 | 3 | 2 |
| Jamabandi, Land Records, Haryana | 9 | 0 | 0 | 0 | 0 |
| Shri Mata Mansa Devi Shrine Board (SMMDSB), Panchkula, Haryana | 9 | 0 | 1 | 0 | 0 |
| State Crime Record Bureau, Haryana | 2 | 0 | 0 | 0 | 0 |
| State Information commission (SIC), Haryana | 9 | 0 | 4 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | HR: appointment / transfer / posting / promotion | HR: leave / pay / allowances / service rules | Scheme guidelines / implementation | Statutory rules / gazette notifications (G.S.R. / S.O.) | TOTAL |
|---|---|---|---|---|---|---|---|
| Sh. Anand Mohan Sharan, IAS | Additional Chief Secretary to Government of Haryana | EIACP Hub Haryana |  |  | 1 | 1 | 2 |
| Shri S. Narayanan, IFS | Director General, Environment Haryana and Secretary to Government, Haryana, Environment & Climate Change Department | Climate Change Cell, Haryana | 1 |  |  |  | 1 |
| Sh. Manoj Kumar Goel | Director | Economic and Statistical Analysis Department, Haryana |  | 1 |  |  | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary to Government, Haryana, Health & Family Welfare, Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Other / unclassified |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Additional Chief Secretary to Government, Haryana, Home, Jails, Criminal Investigation and Administration of Justice Departments.

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| HR: appointment / transfer / posting / promotion |  |

### Additional Chief Secretary to Government, Haryana, Town & Country Planning and Urban Estates Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Administrator, Trade Fair Authority of Haryana, New Delhi.

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution |  |
| Customs / tariff / duty / GST |  |
| Procurement / tenders / GeM |  |

### Climate Change Cell, Haryana

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Shri S. Narayanan, IFS** — Director General, Environment Haryana and Secretary to Government, Haryana, Environment & Climate Change Department — environment@hry.nic.in (1) |

### Commissioner & Secretary to Government, Haryana, Department of Future.

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Commissioner & Secretary to Government, Haryana, Excise & Taxation Department.

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Commissioner & Secretary to Government, Haryana, Printing & Stationery Development Department.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### EIACP Hub Haryana

| Topic | Contact officers (docs signed) |
|---|---|
| Scheme guidelines / implementation | **Sh. Anand Mohan Sharan, IAS** — Additional Chief Secretary to Government of Haryana — psenv2016@gmail.com (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Sh. Anand Mohan Sharan, IAS** — Additional Chief Secretary to Government of Haryana — psenv2016@gmail.com (1) |

### Economic and Statistical Analysis Department, Haryana

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules | **Sh. Manoj Kumar Goel** — Director — esa@hry.nic.in (1) |

### Joint Secretary, Department of Pharmaceuticals, M/o Chemicals and Fertilizers (GOI), New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| RTI / appellate authority / CPIO |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Chief Secretary Office, Haryana | Rohtak Divisions | Officer, Haryana. | 6 |  |
| Employment Department, Haryana | Rajni Singh | DeputY Di rector / Deputy Director, | 3 |  |
| Food and Drugs Administration Department, Haryana | RAJEEV ARORA | Secretary to Government Haryana, | 3 |  |
| Dakshin Haryana Bijli Vitran Nigam (DHBVN), Haryana | HVPN Chairman | Director, Town and Country | 2 |  |
| Directorate of Skill Development & Industrial Training, Haryana | R.S. Saini | Assistant Director (Estt.-] | 2 |  |
| Finance Department, Haryana | T.V.S.N. Prasad | Secretary to Government Haryana | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.