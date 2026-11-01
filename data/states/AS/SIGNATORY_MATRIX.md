# AS — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (51 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 36 |
| PDFs with a detectable signature block | 36 |
| Signatures matched to a roster officer | 10 documents / 9 officers |
| Signatures not matched (person not in any roster, or moved) | 26 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Administrative Reforms and Training Department, Assam | 7 | 0 | 2 | 2 | 2 |
| Agriculture and Horticulture Department, Assam | 7 | 0 | 3 | 1 | 1 |
| Border Protection and Development Department, Assam | 7 | 0 | 1 | 0 | 0 |
| Civil Defence & Home Guards, Assam | 5 | 0 | 0 | 0 | 0 |
| Commissionerate of Food & Drugs Administration, Assam | 4 | 0 | 0 | 0 | 0 |
| Commissionerate of Industries & Commerce, Assam | 6 | 0 | 0 | 0 | 0 |
| Commissionerate of Labour, Assam | 6 | 0 | 0 | 0 | 0 |
| Commissionerate of Rural Development, Assam | 7 | 0 | 0 | 0 | 0 |
| Commissionerate of Taxes, Finance, Assam | 7 | 0 | 2 | 0 | 0 |
| Commissionerate of Transport, Assam | 4 | 0 | 0 | 0 | 0 |
| Cooperation Department, Assam | 5 | 0 | 1 | 0 | 0 |
| Cultural Affairs Department, Assam | 4 | 0 | 1 | 0 | 0 |
| Directorate of AYUSH, Assam | 5 | 0 | 1 | 1 | 1 |
| Directorate of Accounts & Treasuries, Assam | 6 | 0 | 1 | 0 | 0 |
| Directorate of Agriculture, Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Archives, Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Char Areas Development, Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Cultural Affairs, Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Economics and Statistics, Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Elementary Education,Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Employment and Craftsmen Training, Assam | 5 | 0 | 0 | 0 | 0 |
| Directorate of Forensic Science, Government of Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Geology & Mining, Assam | 7 | 0 | 0 | 0 | 0 |
| Directorate of Health Service (Family Welfare), Assam | 4 | 0 | 0 | 0 | 0 |
| Directorate of Health Service, Assam | 7 | 0 | 1 | 0 | 0 |
| Directorate of Historical and Antiquarian studies, Assam | 5 | 0 | 0 | 0 | 0 |
| Directorate of Information Technology, Electronics & Communication, Assam | 7 | 0 | 1 | 0 | 0 |
| Directorate of Information and Public Relations, Assam | 7 | 0 | 0 | 0 | 0 |
| Directorate of Land Records, Assam | 7 | 0 | 0 | 0 | 0 |
| Directorate of Land Requisition Acquisition & Reforms, Assam | 7 | 0 | 0 | 0 | 0 |
| Directorate of Medical Education, Assam | 7 | 0 | 2 | 0 | 0 |
| Directorate of Municipal Administration, Assam | 7 | 0 | 1 | 0 | 0 |
| Elementary Education Department, Assam | 7 | 0 | 0 | 0 | 0 |
| Environment and Forest Department, Assam | 6 | 0 | 0 | 0 | 0 |
| Excise Department, Assam | 5 | 0 | 0 | 0 | 0 |
| Finance Department, Assam | 7 | 0 | 1 | 1 | 1 |
| Fisheries Department, Assam | 7 | 0 | 1 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Assam | 7 | 0 | 1 | 0 | 0 |
| General Administration Department, Assam | 7 | 0 | 2 | 0 | 0 |
| Guwahati Developement Department, Assam | 7 | 0 | 3 | 0 | 0 |
| Handloom,Textile and Sericulture Department, Assam | 5 | 0 | 0 | 0 | 0 |
| Health and Family Welfare Department, Assam | 7 | 0 | 1 | 0 | 0 |
| Higher Education Department, Assam | 6 | 0 | 1 | 0 | 0 |
| Hill Areas Department, Assam | 5 | 0 | 4 | 2 | 2 |
| Home and Political Department, Assam | 4 | 0 | 0 | 0 | 0 |
| Horticulture Department, Assam | 7 | 0 | 0 | 0 | 0 |
| Housing & Urban Affairs Department, Assam | 7 | 0 | 0 | 0 | 0 |
| Industries and Commerce Department, Assam | 7 | 0 | 3 | 3 | 2 |
| Information Technology Department, Assam | 7 | 0 | 2 | 0 | 0 |
| Information, Public Relations, Printing & Stationery Department, Assam | 7 | 0 | 0 | 0 | 0 |
| Irrigation Department, Assam | 7 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary, Hill Areas Department, Food Public Distribution & Consumer Affairs Department, Parliamentary Affairs Department, Assam

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |

### Additional Chief Secretary, Hon'ble CM Assam and Power (E) Department, Chairman, AEGCL (addl) and Additional Principal Resident Commissioner, Assam Bhawan, New Delhi (addl)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Chief Secretary, Assam

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Commissioner & Secretary, Agriculture Department and Agriculture Production Commissioner, Chairman, ARIAS and Chairman, Assam Silk Outreach Mission (ASOM) (addl.) Chairman, State Level Nodal Agency (SLNA), WDC-PMKSY

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### MD, AIDC & Commissioner, Industries & Commerce, Assam (addl) and CEO, Corporate Social Responsibility Authority of Assam (CSRAA)

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Mission Director, National Health Mission (NHM), Assam and MD, Guwahati Smart City Limited and Secretary to the Govt. of Assam, Industries, Commerce & Public Enterprises Department (only limited to CMAAA) and Managing Director, AMSCL and Commissioner of Food Safety & Drugs Administration, Assam (Addl.)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Department of Justice, Ministry of Law & Justice, Govt. of India (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Hill Areas Department

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Secretary, Ministry of Civil Aviation, Govt. of India (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Guwahati Developement Department, Assam | Maninder Singh | Principal Secretary to the Govt. of Assam, / Secretary to the Govt. of Assam, | 3 |  |
| General Administration Department, Assam | P.K. Borthakur | Secretary to the Govt. of Assam, | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.