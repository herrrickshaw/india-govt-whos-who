# TS — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (50 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 45 |
| PDFs with a detectable signature block | 45 |
| Signatures matched to a roster officer | 12 documents / 8 officers |
| Signatures not matched (person not in any roster, or moved) | 34 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Adilabad | 1 | 0 | 0 | 0 | 0 |
| Bhadradri Kothagudem | 5 | 0 | 1 | 0 | 0 |
| Central Detective Training Institute in Hyderabad | 1 | 0 | 0 | 0 | 0 |
| Commissioner and Director of Municipal Administration, Telangana | 9 | 0 | 2 | 0 | 0 |
| Directorate of Government Examinations, Telangana | 9 | 0 | 2 | 0 | 0 |
| Directorate of Treasuries and Accounts, Telangana | 9 | 0 | 5 | 1 | 1 |
| Dr. B.R. Ambedkar Open University, Telangana | 9 | 0 | 0 | 0 | 0 |
| Endowments Department, Telangana | 9 | 0 | 1 | 1 | 1 |
| Forest Department, Telangana | 9 | 0 | 2 | 1 | 1 |
| General Administration Department, Telangana | 2 | 0 | 0 | 0 | 0 |
| Hanumakonda | 1 | 0 | 0 | 0 | 0 |
| Health, Medical & Family Welfare Department, Telangana | 3 | 0 | 0 | 0 | 0 |
| Horticulture Department, Telangana | 9 | 0 | 0 | 0 | 0 |
| Hyderabad | 9 | 0 | 0 | 0 | 0 |
| Hyderabad Metropolitan Development Authority (HMDA), Telangana | 9 | 0 | 1 | 1 | 1 |
| Hyderabad Metropolitan Water Supply & Sewerage Board (HMWSSB), Telangana | 9 | 0 | 0 | 0 | 0 |
| Industries and Commerce Department, Telangana | 9 | 0 | 2 | 2 | 2 |
| Information Commission, Telangana | 9 | 0 | 8 | 1 | 1 |
| Information Technology, Electronics and Communications Department, Telangana | 1 | 0 | 0 | 0 | 0 |
| International Institute of Information Technology, Hyderabad, Telangana | 9 | 0 | 0 | 0 | 0 |
| Jagitial | 2 | 0 | 0 | 0 | 0 |
| Jangoan | 3 | 0 | 0 | 0 | 0 |
| Jayashankar Bhupalapally | 9 | 0 | 2 | 0 | 0 |
| Jogulamba Gadwal | 2 | 0 | 0 | 0 | 0 |
| Kamareddy | 4 | 0 | 0 | 0 | 0 |
| Karimnagar | 2 | 0 | 0 | 0 | 0 |
| Khammam | 9 | 0 | 0 | 0 | 0 |
| Kumuram Bheem Asifabad | 9 | 0 | 0 | 0 | 0 |
| Labour Department, Telangana | 7 | 0 | 0 | 0 | 0 |
| Law Department, Telangana | 9 | 0 | 0 | 0 | 0 |
| Mahabubabad | 9 | 0 | 0 | 0 | 0 |
| Mahabubnagar | 7 | 0 | 0 | 0 | 0 |
| Medak | 5 | 0 | 0 | 0 | 0 |
| Medchal Malkajgiri | 9 | 0 | 2 | 1 | 1 |
| Medicinal Plants Board, Telangana | 9 | 0 | 0 | 0 | 0 |
| Mines & Geology Department, Telangana | 9 | 0 | 2 | 0 | 0 |
| Mulugu | 1 | 0 | 1 | 0 | 0 |
| Nagarkurnool | 5 | 0 | 2 | 0 | 0 |
| Nalgonda | 2 | 0 | 0 | 0 | 0 |
| Narayanpet | 2 | 0 | 0 | 0 | 0 |
| Nirmal | 2 | 0 | 1 | 0 | 0 |
| Nizam's Institute of Medical Sciences, Hyderabad, Telangana | 9 | 0 | 2 | 0 | 0 |
| Nizamabad | 9 | 0 | 1 | 1 | 1 |
| Northern Power Distribution Company of Telangana Limited, Telangana | 1 | 0 | 0 | 0 | 0 |
| Peddapalli | 1 | 0 | 0 | 0 | 0 |
| Rajanna Sircilla | 4 | 0 | 0 | 0 | 0 |
| Telangana Admission and Fee Regulatory Committee, Telangana | 9 | 0 | 5 | 2 | 1 |
| Telangana State Renewable Energy Development Corporation Ltd., (TSREDCO), Telangana | 9 | 0 | 1 | 0 | 0 |
| Telangana Vigilance Commission, Telangana | 2 | 0 | 1 | 1 | 1 |
| The Gandhigram Rural Institute (Deemed to be University), Telangana | 9 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Chief Secretary to Government - Service extended upto 30.06.2026

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |
| Vigilance / disciplinary / court matters |  |

### Collector & District Magistrate, Yadadri-Bhongir

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Principal Secretary to Government, EFS & T Department

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

### Special Chief Secretary to Government (Services & HRM) and (GPM & ART), GAD

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST |  |
| RTI / appellate authority / CPIO |  |

### Special Chief Secretary to Government, Revenue (DM) Department

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |
| Scheme guidelines / implementation |  |

### Special Chief Secretary to Government, TR & B Department

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Special Chief Secretary to Govt., Metropolitan Area & Urban Development

| Topic | Contact officers (docs signed) |
|---|---|
| Scheme guidelines / implementation |  |

### Voluntary Retirement w.e.f 31.10.2025 AN

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Treasuries and Accounts, Telangana | K.SRC Murthy | Director of Treasuries & Accounts / Director of Treasuries and Accounts | 3 |  |
| Information Commission, Telangana | SANTHI KUMARI | SECRETARY TO GOVERNMENT | 3 |  |
| Telangana Admission and Fee Regulatory Committee, Telangana | KARUNA VAKATI | SECRETARY TO GOVERNMENT / SECRETARY TO GOVERNMET | 3 |  |
| Mines & Geology Department, Telangana | R. SRIDHARAN | Addl. Secy | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.