# MZ — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (33 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 144 |
| PDFs with a detectable signature block | 146 |
| Signatures matched to a roster officer | 22 documents / 5 officers |
| Signatures not matched (person not in any roster, or moved) | 135 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Aizawl | 4 | 0 | 2 | 0 | 0 |
| Animal Husbandry and Veterinary Department, Mizoram | 11 | 0 | 1 | 0 | 0 |
| Anti Corruption Bureau, Mizoram | 8 | 0 | 5 | 0 | 0 |
| Art and Culture Department, Mizoram | 6 | 0 | 3 | 0 | 0 |
| Co-operation Department, Mizoram | 5 | 0 | 3 | 0 | 0 |
| Commerce and Industries Department, Mizoram | 11 | 0 | 9 | 0 | 0 |
| Directorate Of Geology & Mining, Mizoram | 6 | 0 | 4 | 0 | 0 |
| Directorate of State Council of Educational Research and Training, Mizoram | 7 | 0 | 2 | 1 | 1 |
| Disaster management and Rehabilitation Department, Mizoram | 11 | 0 | 6 | 0 | 0 |
| District Council Affairs Department, Mizoram | 11 | 0 | 5 | 0 | 0 |
| Economics and Statistics Department, Mizoram | 11 | 0 | 8 | 0 | 0 |
| Environment, Forests & Climate Change Department, Mizoram | 11 | 0 | 8 | 6 | 1 |
| Excise and Narcotic Department, Mizoram | 11 | 0 | 9 | 0 | 0 |
| Finance Department, Mizoram | 11 | 0 | 6 | 0 | 0 |
| Fisheries Department, Mizoram | 8 | 0 | 2 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | 11 | 0 | 6 | 2 | 1 |
| General Administration Department, Mizoram | 11 | 0 | 9 | 8 | 1 |
| Government Aizawl North College, Mizoram | 9 | 0 | 4 | 0 | 0 |
| Govt. Hrangbana College, Mizoram | 2 | 0 | 0 | 0 | 0 |
| Health and Family Welfare Department, Mizoram | 8 | 0 | 4 | 0 | 0 |
| Higher and Technical Education Department, Mizoram | 11 | 0 | 5 | 0 | 0 |
| Home Department, Mizoram | 11 | 0 | 2 | 0 | 0 |
| Horticulture Department, Mizoram | 11 | 0 | 0 | 0 | 0 |
| Information and Public Relations Department, Mizoram | 10 | 0 | 5 | 2 | 1 |
| Irrigation & Water Resources Department, Mizoram | 7 | 0 | 3 | 0 | 0 |
| KVK Serchhip, Mizoram | 3 | 0 | 0 | 0 | 0 |
| Labour, Employment, Skill Development and Entrepreneurship Department, Mizoram | 11 | 0 | 4 | 0 | 0 |
| Land Resources, Soil and Water Conservation Department, Mizoram | 8 | 0 | 4 | 1 | 1 |
| Land Revenue and Settlement Department, Mizoram | 11 | 0 | 9 | 2 | 1 |
| Law and Judicial Department, Mizoram | 11 | 0 | 1 | 0 | 0 |
| Legal Metrology, Mizoram | 11 | 0 | 1 | 0 | 0 |
| Local Administration Department, Mizoram | 11 | 0 | 7 | 0 | 0 |
| State Institute of Rural Development & Panchayati Raj (SIRD & PR), Mizoram | 11 | 0 | 9 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Commissioner & Secretary (Health & Family Welfare, Power & Electricity), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Commissioner & Secretary (Personnel & Admin. Reforms, Higher & Technical Education), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Recruitment rules / RRs |  |

### Commissioner & Secretary (Rural Development & Admin.), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Principal Secretary (GAD, EF&CC), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| HR: leave / pay / allowances / service rules |  |
| Office administration / housekeeping |  |
| Other / unclassified |  |
| Training / capacity building / workshops |  |

### Special Secretary, Power

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Economics and Statistics Department, Mizoram | B. LALRINHLUA | Director | 7 |  |
| State Institute of Rural Development & Panchayati Raj (SIRD & PR), Mizoram | LALHMUNSANGA HNAMTE | Director | 7 |  |
| Commerce and Industries Department, Mizoram | R. LALRAMNGHAKA | Secretary to the Govt, of Mizoram / Secretary to the Govt. of Mizoram | 6 |  |
| Land Revenue and Settlement Department, Mizoram | LALHRUAI TLUANGA | Under Secretary to the Govt. of Mizoram / Under Secretary to the Govt. of Mizoram. | 5 |  |
| Finance Department, Mizoram | REBECCA CHAWNGTHANPUII | Deputy Secretary to the Govt. of Mizoram, | 4 |  |
| Anti Corruption Bureau, Mizoram | H. LALENGMAWIA | Commissioner & Secretary to the Govt. of Mizoram, | 3 |  |
| Directorate Of Geology & Mining, Mizoram | Lalzirmawia Chhangte | Commissioner & Secretary to the Govt. of Mizoram, | 3 |  |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | AMIT MEHTA | Jt. Secy | 3 |  |
| Land Resources, Soil and Water Conservation Department, Mizoram | VANLALMUANPUIA CHHANGTE | Director | 3 |  |
| Local Administration Department, Mizoram | RITA LALNUNMAWII PACHUAU | Director | 3 |  |
| Anti Corruption Bureau, Mizoram | R. Malsawma | Joint Secretary to the Govt. of Mizoram, | 2 |  |
| Commerce and Industries Department, Mizoram | FLORENCE ZOTLUANGPUII | Director | 2 |  |
| Disaster management and Rehabilitation Department, Mizoram | Renu Sharma | Secretary, Mizoram & Chairman, | 2 |  |
| Excise and Narcotic Department, Mizoram | C. IALRUAIA | Secretary to the Govt. of Mizoram, | 2 |  |
| Excise and Narcotic Department, Mizoram | C. LALRUAIA | Secretary to the Govt. of Mizoram, | 2 |  |
| Excise and Narcotic Department, Mizoram | NGURCHUNGNUNGA SAILO | Commissioner / Commissioner of Excise & Narcotics | 2 |  |
| Excise and Narcotic Department, Mizoram | ZOHMINGTHANGI FANAD | Under Secretary to the Govt. of Mizoram | 2 |  |
| Excise and Narcotic Department, Mizoram | ZOHMINGTHANGI FANAI | Under Secretary to the Govt. of Mizoram | 2 |  |
| General Administration Department, Mizoram | CHRISTINA LALMUANZUALI | Under Secretary to the Govt. of Mizoram | 2 |  |
| General Administration Department, Mizoram | LALRINCHHANI RALTE | Deputy Secretary to the Govt. of Mizoram | 2 |  |
| General Administration Department, Mizoram | LALRINPUII HNAMTE | Deputy Secretary to the Govt. of Mizoram | 2 |  |
| Health and Family Welfare Department, Mizoram | LALRINKIMI PACHUAU | Officer (Licensing Authority | 2 |  |
| Higher and Technical Education Department, Mizoram | H. LALENGMAWIA | Secretary to the Govt. of Mizoram | 2 |  |
| Labour, Employment, Skill Development and Entrepreneurship Department, Mizoram | ANGELA ZOTHANPUII | Director / Director, . | 2 |  |
| Land Revenue and Settlement Department, Mizoram | ANGELA ZOTHANPUIL | Director, | 2 |  |
| Local Administration Department, Mizoram | K. LALROHLUA | Director | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.