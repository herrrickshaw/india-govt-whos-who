# WB — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (50 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 47 |
| PDFs with a detectable signature block | 47 |
| Signatures matched to a roster officer | 8 documents / 7 officers |
| Signatures not matched (person not in any roster, or moved) | 39 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Alipurduar | 5 | 0 | 0 | 0 | 0 |
| Animal Resources Development Department, West Bengal | 8 | 0 | 2 | 1 | 1 |
| Asansol Durgapur Police Commissionerate | 8 | 0 | 0 | 0 | 0 |
| Banglar Uchchashiksha, Higher Education Department, West Bengal | 8 | 0 | 3 | 2 | 2 |
| Bankura | 4 | 0 | 0 | 0 | 0 |
| Bankura University, West Bengal | 8 | 0 | 2 | 0 | 0 |
| Bina Mulya Samajik Suraksha Yojana, West Bengal | 8 | 0 | 5 | 0 | 0 |
| Birbhum | 3 | 0 | 0 | 0 | 0 |
| Chittaranjan National Cancer Institute (CNCI) | 8 | 0 | 0 | 0 | 0 |
| Co-operation Department, West Bengal | 2 | 0 | 0 | 0 | 0 |
| Computer Aided Design Centre, Jadavpur University, West Bengal | 2 | 0 | 1 | 0 | 0 |
| Consumer Affairs Department, West Bengal | 1 | 0 | 0 | 0 | 0 |
| Cooch Behar | 1 | 0 | 0 | 0 | 0 |
| Correctional Administration (Jails) Department, West Bengal | 2 | 0 | 0 | 0 | 0 |
| Darjeeling | 2 | 0 | 0 | 0 | 0 |
| Directorate of Open and Distance Learning (DODL) - University of Kalyani, West Bengal | 8 | 0 | 0 | 0 | 0 |
| Examinations, Admission and eCounselling Services, West Bengal | 8 | 0 | 0 | 0 | 0 |
| Excise Directorate, West Bengal | 2 | 0 | 0 | 0 | 0 |
| Finance Department, West Bengal | 8 | 0 | 2 | 1 | 1 |
| Fisheries Department, West Bengal | 8 | 0 | 0 | 0 | 0 |
| Forest Department, West Bengal | 8 | 0 | 0 | 0 | 0 |
| Government College of Engineering & Ceramic Technology (GCE&CT), Kolkata, West Bengal | 8 | 0 | 1 | 0 | 0 |
| Home and Hill Affairs Department, West Bengal | 8 | 0 | 2 | 1 | 1 |
| Hooghly | 2 | 0 | 0 | 0 | 0 |
| Indian Centre for Space Physics, Kolkata | 8 | 0 | 0 | 0 | 0 |
| Indian Institute of Social Welfare and Business Management (IISWBM), West Bengal | 8 | 0 | 1 | 0 | 0 |
| Information Commission, West Bengal | 4 | 0 | 0 | 0 | 0 |
| Information Technology and Electronics Department, West Bengal | 8 | 0 | 0 | 0 | 0 |
| Information and Cultural Affairs Department, West Bengal | 8 | 0 | 1 | 0 | 0 |
| Jalpaiguri | 1 | 0 | 0 | 0 | 0 |
| Kalyani Government Engineering College, Nadia, West Bengal | 4 | 0 | 0 | 0 | 0 |
| Maulana Abul Kalam Azad University of Technology, West Bengal | 8 | 0 | 3 | 0 | 0 |
| Rabindra Bharati University, West Bengal | 8 | 0 | 1 | 0 | 0 |
| Siliguri Jalpaiguri Development Authority (SJDA), West Bengal | 8 | 0 | 2 | 0 | 0 |
| State Load Despatch Center (SLDC), Howrah, West Bengal | 6 | 0 | 4 | 0 | 0 |
| Student Credit Card Scheme, Department of Higher Education, West Bengal | 3 | 0 | 1 | 1 | 1 |
| The University of Burdwan, West Bengal | 8 | 0 | 2 | 1 | 1 |
| The West Bengal University of Health Sciences, West Bengal | 8 | 0 | 1 | 0 | 0 |
| West Bengal Biodiversity Board (WBBB), West Bengal | 8 | 0 | 3 | 0 | 0 |
| West Bengal Board of Secondary Education (WBBSE), West Bengal | 8 | 0 | 1 | 0 | 0 |
| West Bengal Central School Service Commission, West Bengal | 8 | 0 | 2 | 1 | 1 |
| West Bengal College Service Commission, West Bengal | 8 | 0 | 0 | 0 | 0 |
| West Bengal Electricity Regulatory Commission (WBERC), West Bengal | 8 | 0 | 4 | 0 | 0 |
| West Bengal Electronics Industry Development Corporation Limited (WEBEL), West Bengal | 6 | 0 | 2 | 0 | 0 |
| West Bengal Forest Development Corporation Ltd. (WBDFC), Kolkata, West Bengal | 8 | 0 | 1 | 0 | 0 |
| West Bengal Housing Infrastructure Development Corporation Limited, (WBHIDCO), West Bengal | 8 | 0 | 0 | 0 | 0 |
| West Bengal Industrial Infrastructure Development Corporation (WBIIDC), West Bengal | 8 | 0 | 0 | 0 | 0 |
| West Bengal Khadi & Village Industries Board, West Bengal | 8 | 0 | 0 | 0 | 0 |
| West Bengal Tourism Development Corporation Ltd., West Bengal | 1 | 0 | 0 | 0 | 0 |
| West Bengal Transport Corporation, West Bengal | 1 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Other / unclassified | TOTAL |
|---|---|---|---|---|
| Sri Abhijit Chatterjee | Executive Engineer, Nadia Arsenic Civil Division No. -I | Nadia | 1 | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary, Irrigation & Waterways Department with additional charges of Additional Chief Secretary, Water Resources Investigation & Development Department & Project Director ADMI Project

| Topic | Contact officers (docs signed) |
|---|---|
| Scheme guidelines / implementation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Additional Chief Secretary, Land & Land Reforms and Refugee Relief & Rehabilitation Department and LRC with additional charges of Additional Chief Secretary, Animal Resources Development Department and OSD, Biswa Bangla Corporation in the office of the Resident Commissioner, New Delhi, West Bengal

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Additional Chief Secretary, North Bengal Development Department with additional charge of Principal Secretary, GTA and Additional Charge of the Additional Chief Secretary Correctional Administration Department

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Chief Secretary to the Government of West Bengal

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Nadia

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Sri Abhijit Chatterjee** — Executive Engineer, Nadia Arsenic Civil Division No. -I — nadiaarsenic@gmail.com (1) |

### Principal Secretary, Food and Supplies Department, West Bengal

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Principal Secretary, Housing Department with additional charge of Principal Secretary, Youth Services and Sports Department and Principal Secretary, Disaster Management & Civil Defence Department

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Bina Mulya Samajik Suraksha Yojana, West Bengal | GOPAL KRISHNA | Secretary to the Government of West Bengal. | 4 |  |
| State Load Despatch Center (SLDC), Howrah, West Bengal | HARPREET SINGH PRUTHI | Secy | 2 |  |
| State Load Despatch Center (SLDC), Howrah, West Bengal | SANOJ KUMAR JHA | Secy | 2 |  |
| West Bengal Biodiversity Board (WBBB), West Bengal | DESH DEEPAK VERMA | Joint Secretary / Jt. Secy | 2 |  |
| West Bengal Electricity Regulatory Commission (WBERC), West Bengal | Ajay Shankar | Additional Secretary to the Government of India | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.