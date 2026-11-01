# MZ — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (48 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 645 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 300 |
| PDFs with a detectable signature block | 302 |
| Signatures matched to a roster officer | 52 documents / 15 officers |
| Signatures not matched (person not in any roster, or moved) | 275 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Administrative Training Institute (ATI), Mizoram | 2 | 0 | 0 | 0 | 0 |
| Aizawl | 6 | 0 | 2 | 0 | 0 |
| Animal Husbandry and Veterinary Department, Mizoram | 27 | 0 | 3 | 0 | 0 |
| Anti Corruption Bureau, Mizoram | 8 | 0 | 5 | 0 | 0 |
| Art and Culture Department, Mizoram | 6 | 0 | 3 | 0 | 0 |
| Champhai | 7 | 0 | 4 | 2 | 1 |
| Co-operation Department, Mizoram | 5 | 0 | 3 | 0 | 0 |
| Commerce and Industries Department, Mizoram | 27 | 0 | 21 | 2 | 2 |
| Directorate Of Geology & Mining, Mizoram | 6 | 0 | 4 | 0 | 0 |
| Directorate of State Council of Educational Research and Training, Mizoram | 7 | 0 | 2 | 1 | 1 |
| Disaster management and Rehabilitation Department, Mizoram | 27 | 0 | 16 | 3 | 1 |
| District Council Affairs Department, Mizoram | 27 | 0 | 9 | 0 | 0 |
| Economics and Statistics Department, Mizoram | 19 | 0 | 13 | 0 | 0 |
| Environment, Forests & Climate Change Department, Mizoram | 25 | 0 | 17 | 9 | 2 |
| Excise and Narcotic Department, Mizoram | 27 | 0 | 22 | 0 | 0 |
| Finance Department, Mizoram | 27 | 0 | 15 | 0 | 0 |
| Fisheries Department, Mizoram | 8 | 0 | 2 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | 24 | 0 | 13 | 2 | 1 |
| Forensic Science Laboratory, Mizoram | 16 | 0 | 7 | 0 | 0 |
| General Administration Department, Mizoram | 27 | 0 | 21 | 18 | 2 |
| Government Aizawl North College, Mizoram | 9 | 0 | 4 | 0 | 0 |
| Govt. Hrangbana College, Mizoram | 2 | 0 | 0 | 0 | 0 |
| Health and Family Welfare Department, Mizoram | 8 | 0 | 4 | 0 | 0 |
| Higher and Technical Education Department, Mizoram | 13 | 0 | 5 | 0 | 0 |
| Home Department, Mizoram | 15 | 0 | 3 | 0 | 0 |
| Horticulture Department, Mizoram | 22 | 0 | 5 | 0 | 0 |
| Information and Public Relations Department, Mizoram | 10 | 0 | 5 | 2 | 1 |
| Institutional Finance and State Lottery, Mizoram | 16 | 0 | 5 | 0 | 0 |
| Irrigation & Water Resources Department, Mizoram | 7 | 0 | 3 | 0 | 0 |
| KVK Lawngtlai, Mizoram | 3 | 0 | 0 | 0 | 0 |
| KVK Serchhip, Mizoram | 3 | 0 | 0 | 0 | 0 |
| Labour, Employment, Skill Development and Entrepreneurship Department, Mizoram | 18 | 0 | 6 | 0 | 0 |
| Land Resources, Soil and Water Conservation Department, Mizoram | 8 | 0 | 4 | 1 | 1 |
| Land Revenue and Settlement Department, Mizoram | 27 | 0 | 19 | 3 | 1 |
| Law and Judicial Department, Mizoram | 20 | 0 | 7 | 1 | 1 |
| Lawngtlai | 9 | 0 | 5 | 4 | 2 |
| Legal Metrology, Mizoram | 16 | 0 | 2 | 0 | 0 |
| Local Administration Department, Mizoram | 17 | 0 | 9 | 0 | 0 |
| Mamit | 15 | 0 | 5 | 3 | 2 |
| Mizoram Food And Allied Industries Corporation Limited (MIFCO), Mizoram | 1 | 0 | 1 | 0 | 0 |
| Mizoram State Sports Council | 16 | 0 | 5 | 0 | 0 |
| Mizoram State Tobacco Control Society | 1 | 0 | 0 | 0 | 0 |
| Sarva Shiksha Abhiyan (SSA), Mizoram | 14 | 0 | 3 | 0 | 0 |
| Serchhip | 2 | 0 | 1 | 0 | 0 |
| Siaha | 5 | 0 | 1 | 0 | 0 |
| State Institute of Rural Development & Panchayati Raj (SIRD & PR), Mizoram | 23 | 0 | 12 | 1 | 1 |
| State Load Despatch Centre (SLDC), Mizoram | 15 | 0 | 5 | 0 | 0 |
| Zoram Energy Development Agency, Mizoram | 2 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | HR: appointment / transfer / posting / promotion | RTI / appellate authority / CPIO | TOTAL |
|---|---|---|---|---|---|
| DONNY LALRUATSANGA | Deputy Commissioner | Lawngtlai | 2 | 2 | 4 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Addl. Chief Secretary (I&FC, PWD & GAD), Govt. of NCT of Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Procurement / tenders / GeM |  |

### Art and Culture Department, Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Commissioner & Secretary (Health & Family Welfare, Power & Electricity), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Commissioner & Secretary (Personnel & Admin. Reforms, Higher & Technical Education), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Office administration / housekeeping |  |
| Recruitment rules / RRs |  |

### Commissioner & Secretary (Rural Development & Admin.), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Deputy Commissioner (Champhai), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Deputy Commissioner (Mamit), Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| RTI / appellate authority / CPIO |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Director (Commerce & Industries), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |
| Office administration / housekeeping |  |

### Lawngtlai

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **DONNY LALRUATSANGA** — Deputy Commissioner — dclawngtlai2010@gmail.com (2) |
| RTI / appellate authority / CPIO | **DONNY LALRUATSANGA** — Deputy Commissioner — dclawngtlai2010@gmail.com (2) |

### Lunglei

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| Other / unclassified |  |

### Mamit

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Officer, Govt. of NCT of Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| RTI / appellate authority / CPIO |  |

### Principal Secretary (GAD, EF&CC), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| HR: leave / pay / allowances / service rules |  |
| Office administration / housekeeping |  |
| Other / unclassified |  |
| RTI / appellate authority / CPIO |  |
| Training / capacity building / workshops |  |

### Special Secretary (School Education), Govt. of Mizoram

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Special Secretary, Power

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Excise and Narcotic Department, Mizoram | NGURCHUNGNUNGA SAILO | Commissioner / Commissioner of Excise & Narcotics | 11 |  |
| Commerce and Industries Department, Mizoram | R. LALRAMNGHAKA | Secretary to the Govt, of Mizoram / Secretary to the Govt. of Mizoram | 7 |  |
| Economics and Statistics Department, Mizoram | B. LALRINHLUA | Director | 7 |  |
| State Institute of Rural Development & Panchayati Raj (SIRD & PR), Mizoram | LALHMUNSANGA HNAMTE | Director | 7 |  |
| Forensic Science Laboratory, Mizoram | T. LALROPUIA | Director / Director, | 6 |  |
| Land Revenue and Settlement Department, Mizoram | LALHRUAI TLUANGA | Under Secretary to the Govt. of Mizoram / Under Secretary to the Govt. of Mizoram. | 6 |  |
| Finance Department, Mizoram | REBECCA CHAWNGTHANPUII | Deputy Secretary to the Govt. of Mizoram, / Secretary to the covi olMizoram, | 5 |  |
| General Administration Department, Mizoram | CHRISTINA LALMUANZUALI | Under Secretary to the Govt. of Mizoram | 5 |  |
| Disaster management and Rehabilitation Department, Mizoram | LALNUNMAWIA CHUAUNGO | Secretary / Secretary to the Govt. of Mizoram | 4 |  |
| Environment, Forests & Climate Change Department, Mizoram | VANLALRUATA PAUTU | Under Secretary limate Change Department. / Under Secretary to the Govt. of Mizoram, | 4 |  |
| Finance Department, Mizoram | VANLAL CHHUANGA | Commissioner / Principal Secretary to Govt. of Mizoram, | 4 |  |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | AMIT MEHTA | Jt. Secy | 4 |  |
| Labour, Employment, Skill Development and Entrepreneurship Department, Mizoram | ANGELA ZOTHANPUII | Director / Director, | 4 |  |
| Local Administration Department, Mizoram | RITA LALNUNMAWII PACHUAU | Director | 4 |  |
| Anti Corruption Bureau, Mizoram | H. LALENGMAWIA | Commissioner & Secretary to the Govt. of Mizoram, | 3 |  |
| Commerce and Industries Department, Mizoram | MARIA CT ZUALI | Director | 3 |  |
| Directorate Of Geology & Mining, Mizoram | Lalzirmawia Chhangte | Commissioner & Secretary to the Govt. of Mizoram, | 3 |  |
| Disaster management and Rehabilitation Department, Mizoram | JC. RAMTHANGA | Secretary to the Chief Minister / Secretary to the Govt. of Mizoram | 3 |  |
| Economics and Statistics Department, Mizoram | MARY LALRINCHHUNGI | Director / Joint Director | 3 |  |
| Finance Department, Mizoram | CHRISTINA LALMUANZUALI | Secretary to the Govt. of Mizoram, / Under Secretary to the Govt. of Mizoram, | 3 |  |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | ANDREW H. VANLALDIKA | Director / Director, | 3 |  |
| Land Resources, Soil and Water Conservation Department, Mizoram | VANLALMUANPUIA CHHANGTE | Director | 3 |  |
| Local Administration Department, Mizoram | K. LALROHLUA | Director | 3 |  |
| Anti Corruption Bureau, Mizoram | R. Malsawma | Joint Secretary to the Govt. of Mizoram, | 2 |  |
| Commerce and Industries Department, Mizoram | FLORENCE ZOTLUANGPUII | Director | 2 |  |
| Commerce and Industries Department, Mizoram | LALZIRMAWIA CHHANGTE | Commissioner & Secretary to the Govt. of Mizoram / Commissioner & Secretary to the Govt. of Mizoram, | 2 |  |
| Disaster management and Rehabilitation Department, Mizoram | LALNUNMAWTA CHUAUNGO | Secretary, Mizoram & Chairman, | 2 |  |
| Disaster management and Rehabilitation Department, Mizoram | Renu Sharma | Secretary, Mizoram & Chairman, | 2 |  |
| District Council Affairs Department, Mizoram | H. Lalthlangliana | Secretary to the Govt. of Mizoram, | 2 |  |
| Environment, Forests & Climate Change Department, Mizoram | VANLALNUNPUII FIMAR | Officer | 2 |  |
| Excise and Narcotic Department, Mizoram | C. IALRUAIA | Secretary to the Govt. of Mizoram, | 2 |  |
| Excise and Narcotic Department, Mizoram | C. LALRUAIA | Secretary to the Govt. of Mizoram, | 2 |  |
| Excise and Narcotic Department, Mizoram | NGURCHUNGNUNGA SArLO | Commissioner / Commissioner of Excisb | 2 |  |
| Excise and Narcotic Department, Mizoram | ZOHMINGTHANGI FANAD | Under Secretary to the Govt. of Mizoram | 2 |  |
| Excise and Narcotic Department, Mizoram | ZOHMINGTHANGI FANAI | Under Secretary to the Govt. of Mizoram | 2 |  |
| Food, Civil Supplies and Consumer Affairs Department, Mizoram | ANUPAM MISHRA | Jt. Secy | 2 |  |
| General Administration Department, Mizoram | J.C. Ramthanga | Secretary to the Govt. of Mizoram / Secretary to the Govt. of Mizzoram | 2 |  |
| General Administration Department, Mizoram | LALRINCHHANI RALTE | Deputy Secretary to the Govt. of Mizoram | 2 |  |
| General Administration Department, Mizoram | LALRINPUII HNAMTE | Deputy Secretary to the Govt. of Mizoram | 2 |  |
| Health and Family Welfare Department, Mizoram | LALRINKIMI PACHUAU | Officer (Licensing Authority | 2 |  |
| Higher and Technical Education Department, Mizoram | H. LALENGMAWIA | Secretary to the Govt. of Mizoram | 2 |  |
| Horticulture Department, Mizoram | ELIZABETH SAIPARI | Director / Director, | 2 |  |
| Institutional Finance and State Lottery, Mizoram | L.N. Tochhawng | Commissioner, / Commissioner. | 2 |  |
| Land Revenue and Settlement Department, Mizoram | ANGELA ZOTHANPUII | Director / Director, | 2 |  |
| Land Revenue and Settlement Department, Mizoram | ANGELA ZOTHANPUIL | Director, | 2 |  |
| Land Revenue and Settlement Department, Mizoram | K. VANLALTHIANA | Director / Director, pie | 2 |  |
| Land Revenue and Settlement Department, Mizoram | LALTLANZOVI SAILO | Deputy Director (Admn. / Deputy Director(Admn. | 2 |  |
| Law and Judicial Department, Mizoram | MARLI VANKUNG | Secretary to the Govt. of Mizoram | 2 |  |
| Mizoram State Sports Council | HENRY C. LALRAWNKIMA | Secretary | 2 |  |
| State Load Despatch Centre (SLDC), Mizoram | Shubha Sarma | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.