# UP — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (41 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 34 |
| PDFs with a detectable signature block | 34 |
| Signatures matched to a roster officer | 5 documents / 4 officers |
| Signatures not matched (person not in any roster, or moved) | 31 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Acharya Narendra Deva University of Agriculture & Technology, Ayodhya, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Additional Sources of Energy Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Administrative Reforms Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Appointment and Personnel Department, Uttar Pradesh | 2 | 0 | 0 | 0 | 0 |
| Basic Education Department, Uttar Pradesh | 8 | 0 | 5 | 2 | 2 |
| Chhatrapati Shahu Ji Maharaj University, Kanpur, Uttar Pradesh | 8 | 0 | 2 | 0 | 0 |
| Dairy Development Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Department of IT & Electronics, Government of Uttar Pradesh | 5 | 0 | 0 | 0 | 0 |
| Department of Legal Metrology (Weights & Measures), Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Directorate of Agricultural Marketing and Agriculture Foreign Trade, Uttar Pradesh | 8 | 0 | 3 | 1 | 1 |
| Directorate of Geology & Mining, Uttar Pradesh | 8 | 0 | 3 | 0 | 0 |
| Directorate of Local Bodies, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Directorate of Medical Education and Training, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Directorate of Printing and Stationery, Uttar Pradesh | 8 | 0 | 8 | 0 | 0 |
| Directorate of Sainik Welfare and Rehabilitation, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Dr. A.P.J. Abdul Kalam Technical University, Lucknow, Uttar Pradesh | 8 | 0 | 1 | 0 | 0 |
| Dr. Shakuntala Misra National Rehabilitation University, Lucknow | 3 | 0 | 0 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| G.S.V.M. Medical College, Kanpur, Uttar Pradesh | 2 | 0 | 0 | 0 | 0 |
| Gautam Buddha University, Uttar Pradesh | 8 | 0 | 1 | 0 | 0 |
| Govind Ballabh Pant Social Science Institute, Allahabad, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Ground Water Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Harcourt Butler Technical University (HBTU), Kanpur, Uttar Pradesh | 8 | 0 | 1 | 0 | 0 |
| Harcourt Butler Technical University, Admission and eCounselling Services | 8 | 0 | 0 | 0 | 0 |
| Higher Education Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Horticulture and Food Processing Department, Uttar Pradesh | 4 | 0 | 1 | 0 | 0 |
| Indian Insttitute of Technology (BHU), Varanassi | 8 | 0 | 0 | 0 | 0 |
| Information & Public Relations Department, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Institute of Engineering and Technology, Lucknow, Uttar Pradesh | 5 | 0 | 0 | 0 | 0 |
| Joint Entrance Examination Council (Polytechnic), Uttar Pradesh | 8 | 0 | 1 | 0 | 0 |
| Kendriya Hindi Sansthan, Agra | 8 | 0 | 0 | 0 | 0 |
| King George's Medical University, Lucknow, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Madan Mohan Malaviya University of Technology, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Madhymic Shiksha Parishad, Prayagraj, Uttar Pradesh | 8 | 0 | 1 | 0 | 0 |
| Moradabad Development Authority, Uttar Pradesh | 8 | 0 | 2 | 2 | 1 |
| Paschimanchal Vidyut Vitaran Nigam Limited (PVVNL) , Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| UP Housing and Development Board, Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Uttar Pradesh Eco-Tourism Development Board | 8 | 0 | 0 | 0 | 0 |
| Uttar Pradesh Expressways Industrial Development Authority (UPEIDA), Uttar Pradesh | 8 | 0 | 0 | 0 | 0 |
| Uttar Pradesh Jal Nigam (Urban), Uttar Pradesh | 8 | 0 | 5 | 0 | 0 |
| Uttar Pradesh Police Recruitment & Promotion Board, Uttar Pradesh | 7 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Other / unclassified | TOTAL |
|---|---|---|---|---|
| Col. Sanjay Singh | CGM (Technical) | Uttar Pradesh Expressways Industrial Development Authority (UPEIDA), Uttar Pradesh | 2 | 2 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Etah

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Principal Staff Officer to Chief Secretary, Govt. of UP + Project Director, UP AIDS Control Society + Director, Revenue & Special Intelligence Directorate + DG, UP Outsource Services Corporation, Lucknow

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary to GOI, Agriculture & Farmers' Welfare Deptt., M/O Agriculture & Farmers Welfare, New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Uttar Pradesh Expressways Industrial Development Authority (UPEIDA), Uttar Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Col. Sanjay Singh** — CGM (Technical) — defcorup@gmail.com (2) |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Printing and Stationery, Uttar Pradesh | RAJIV MANI | Secretary to the Govt. of India. | 8 |  |
| Basic Education Department, Uttar Pradesh | Amitabh Tripathi | Joint Secretary | 2 |  |
| Directorate of Agricultural Marketing and Agriculture Foreign Trade, Uttar Pradesh | Ramakant Pandey | Director | 2 |  |
| Directorate of Geology & Mining, Uttar Pradesh | Hriday Narayan Singh Yadav | Under Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.