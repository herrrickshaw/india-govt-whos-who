# AR — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (46 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 286 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 69 |
| PDFs with a detectable signature block | 69 |
| Signatures matched to a roster officer | 21 documents / 11 officers |
| Signatures not matched (person not in any roster, or moved) | 54 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Department, Arunachal Pradesh | 11 | 0 | 1 | 0 | 0 |
| Anjaw | 7 | 0 | 5 | 5 | 1 |
| Arunachal Pradesh Energy Development Agency (APEDA) | 11 | 0 | 3 | 0 | 0 |
| Arunachal Pradesh Investment Portal | 11 | 0 | 3 | 1 | 1 |
| Arunachal Pradesh Space Application Center | 6 | 0 | 0 | 0 | 0 |
| Arunachal Pradesh Staff Selection Board | 11 | 0 | 4 | 3 | 2 |
| Arunachal Pradesh Startup Portal | 11 | 0 | 0 | 0 | 0 |
| Arunachal University of Studies (AUS), Arunachal Pradesh | 11 | 0 | 8 | 0 | 0 |
| Changlang | 2 | 0 | 2 | 0 | 0 |
| Civil Aviation Department, Arunachal Pradesh | 2 | 0 | 2 | 0 | 0 |
| Dera Natung Government College, Itanagar, Arunachal Pradesh | 2 | 0 | 0 | 0 | 0 |
| Dibang Valley | 2 | 0 | 1 | 1 | 1 |
| Directorate of Higher and Technical Education, Arunachal Pradesh | 11 | 0 | 10 | 0 | 0 |
| Directorate of Research, Arunachal Pradesh | 2 | 0 | 0 | 0 | 0 |
| Directorate of Urban Local Bodies, Arunachal Pradesh | 11 | 0 | 1 | 0 | 0 |
| Disaster Management Department, Arunachal Pradesh | 6 | 0 | 4 | 0 | 0 |
| East Kameng | 11 | 0 | 1 | 1 | 1 |
| East Siang | 6 | 0 | 3 | 0 | 0 |
| Economics & Statistics Department, Arunachal Pradesh | 11 | 0 | 1 | 1 | 1 |
| Education Department, Arunachal Pradesh | 3 | 0 | 2 | 2 | 1 |
| Finance-Planning & Investment Department, Arunachal Pradesh | 11 | 0 | 0 | 0 | 0 |
| Fisheries Department, Arunachal Pradesh | 11 | 0 | 2 | 1 | 1 |
| Food and Civil Supplies Department, Arunachal Pradesh | 11 | 0 | 0 | 0 | 0 |
| Government Receipt Accounting System, Arunachal Pradesh | 4 | 0 | 0 | 0 | 0 |
| Hydro Power Development Corporation of Arunachal Pradesh Limited | 5 | 0 | 1 | 0 | 0 |
| Industries Department, Arunachal Pradesh | 11 | 0 | 3 | 0 | 0 |
| Information Technology & Communication Department, Arunachal Pradesh | 11 | 0 | 2 | 1 | 1 |
| Information and Public Relations Department, Arunachal Pradesh | 11 | 0 | 4 | 3 | 1 |
| Itanagar Capital Complex, Arunachal Pradesh | 2 | 0 | 0 | 0 | 0 |
| Jarbom Gamlin Government Law College, Arunachal Pradesh | 9 | 0 | 1 | 0 | 0 |
| Kurung Kumey | 1 | 0 | 0 | 0 | 0 |
| Lohit | 2 | 0 | 0 | 0 | 0 |
| Longding | 3 | 0 | 0 | 0 | 0 |
| Lower Dibang Valley | 3 | 0 | 1 | 1 | 1 |
| Lower Subansiri | 1 | 0 | 0 | 0 | 0 |
| Online RTI Information System, Arunachal Pradesh | 1 | 0 | 0 | 0 | 0 |
| Papum Pare | 7 | 0 | 1 | 0 | 0 |
| Power Department, Arunachal Pradesh | 11 | 0 | 0 | 0 | 0 |
| Prison, Arunachal Pradesh | 6 | 0 | 0 | 0 | 0 |
| Raj Bhavan Visitor Booking, Arunachal Pradesh | 1 | 0 | 0 | 0 | 0 |
| SNA-SPARSH, Integrated Financial Management System, Arunachal Pradesh | 1 | 0 | 1 | 1 | 1 |
| Shi Yomi | 1 | 0 | 1 | 0 | 0 |
| Tawang | 10 | 0 | 0 | 0 | 0 |
| Tirap | 1 | 0 | 0 | 0 | 0 |
| Upper Subansiri | 2 | 0 | 1 | 0 | 0 |
| eServices Portal, Arunachal Pradesh | 1 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Customs / tariff / duty / GST | Other / unclassified | TOTAL |
|---|---|---|---|---|---|
| Shri Millo Kojin | Deputy Commissioner,Anjaw | Anjaw | 1 | 4 | 5 |
| TANYANG TATAK | Joint Director (Secondary Education) | Education Department, Arunachal Pradesh |  | 2 | 2 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Advisor to Administrator, DNH&DD

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Anjaw

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST | **Shri Millo Kojin** — Deputy Commissioner,Anjaw — dc-anjaw-arn@nic.in (1) |
| Other / unclassified | **Shri Millo Kojin** — Deputy Commissioner,Anjaw — dc-anjaw-arn@nic.in (4) |

### Chief Secretary, Govt. of Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Commissioner (Excise/Finance), Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Scheme guidelines / implementation |  |

### Commissioner (Industries, Trade & Commerce, Skill Development & Entrepreneurship, Labour and Employment, Transport), Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Commissioner (Land Management, Geology & Mining), Govt. of Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Education Department, Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **TANYANG TATAK** — Joint Director (Secondary Education) — dirschedn@gmail.com (2) |

### Lower Dibang Valley

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |

### Registrar of Cooperative Societies, Govt. of NCT of Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary (RD & PR, Cooperation, IT & Communication), Govt. of Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, APSSB & Secretary (AH, Vety. & DD), Govt. of Arunachal Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Higher and Technical Education, Arunachal Pradesh | Milorai Modi | Director | 9 |  |
| Arunachal University of Studies (AUS), Arunachal Pradesh | Divyanshu Goel | Registrar | 8 |  |
| Arunachal Pradesh Energy Development Agency (APEDA) | Marki Loya | Director | 3 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.