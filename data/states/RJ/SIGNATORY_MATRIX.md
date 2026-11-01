# RJ — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (36 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 700 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 138 |
| PDFs with a detectable signature block | 138 |
| Signatures matched to a roster officer | 24 documents / 11 officers |
| Signatures not matched (person not in any roster, or moved) | 122 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Central Goods & Services Tax, Jaipur Zone, Rajasthan | 16 | 0 | 13 | 0 | 0 |
| Co-operative Department, Rajasthan | 21 | 0 | 0 | 0 | 0 |
| College of Technology and Engineering, Maharana Pratap University of Agriculture and Technology Udaipur, Rajasthan | 27 | 0 | 0 | 0 | 0 |
| Department of Treasuries & Accounts (DTA), Rajasthan | 27 | 0 | 15 | 13 | 3 |
| Devasthan Department, Rajasthan | 1 | 0 | 0 | 0 | 0 |
| Directorate of Petroleum, Rajasthan | 13 | 0 | 2 | 0 | 0 |
| Disaster Management and Relief Department, Rajasthan | 27 | 0 | 0 | 0 | 0 |
| Engineering College Bikaner, Rajasthan | 9 | 0 | 1 | 0 | 0 |
| Environment and Climate Change Department, Rajasthan | 27 | 0 | 5 | 1 | 1 |
| Excise Department, Rajasthan | 27 | 0 | 5 | 2 | 2 |
| Factories and Boilers Inspection Department, Rajasthan | 27 | 0 | 8 | 3 | 2 |
| Finance Department, Rajasthan | 27 | 0 | 1 | 1 | 1 |
| Food and Civil Supplies Department, Rajasthan | 27 | 0 | 15 | 1 | 1 |
| Forest Department, Rajasthan | 27 | 0 | 0 | 0 | 0 |
| Government Polytechnic College, Kota, Rajasthan | 27 | 0 | 0 | 0 | 0 |
| Indira Gandhi Panchayati Raj and Gramin Vikas sansthan, Rajasthan | 21 | 0 | 0 | 0 | 0 |
| Integrated Financial Pension Management System, Rajasthan | 27 | 0 | 10 | 1 | 1 |
| Jagannath University, Rajasthan | 19 | 0 | 0 | 0 | 0 |
| Jaipur Metro Rail Corporation Limited (JMRC), Rajasthan | 27 | 0 | 4 | 0 | 0 |
| Labour Department Management System (LDMS), Rajasthan | 2 | 0 | 0 | 0 | 0 |
| Maharshi Dayanand Saraswati University, Ajmer, Rajasthan | 13 | 0 | 0 | 0 | 0 |
| Mohanlal Sukhadia University, Rajasthan | 7 | 0 | 1 | 0 | 0 |
| PDCOR Limited - A Project Development Company, Rajasthan | 1 | 0 | 0 | 0 | 0 |
| Price Statistics of Rajasthan | 8 | 0 | 3 | 0 | 0 |
| RajCOMP Info Services Limited, Rajasthan | 27 | 0 | 6 | 0 | 0 |
| Rajas than Police Academy, Rajasthan | 27 | 0 | 16 | 0 | 0 |
| Rajasthan Medical Services Corporation Limited, Rajasthan | 27 | 0 | 2 | 0 | 0 |
| Rajasthan Staff Selection Board, Jaipur, Rajasthan | 27 | 0 | 3 | 0 | 0 |
| Rajasthan State Consumer Disputes Redressal Commission, Rajasthan | 16 | 0 | 12 | 0 | 0 |
| Rajasthan State Human Rights Commission, Rajasthan | 16 | 0 | 0 | 0 | 0 |
| Rajasthan State Mines and Minerals Limited, Rajasthan | 27 | 0 | 5 | 0 | 0 |
| Rajasthan Tax Board, Rajasthan | 7 | 0 | 0 | 0 | 0 |
| Rajasthan University of Health Sciences, Jaipur, Rajasthan | 27 | 0 | 2 | 0 | 0 |
| Rajasthan University of Veterinary and Animal Sciences, Bikaner, Rajasthan | 1 | 0 | 0 | 0 | 0 |
| Revenue Board, Rajasthan | 16 | 0 | 8 | 2 | 1 |
| Vardhaman Mahaveer Open University (VMOU), Kota | 27 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Acts / commencement / legislation | HR: leave / pay / allowances / service rules | Licensing / approvals / standards / enlistment | TOTAL |
|---|---|---|---|---|---|---|
| Shri Harish Kumar Gupta | Chief Inspector of Factories & Boilers Factories & Boilers Inspection Department Govt. of Rajasthan 6-c, Jhalana Institutional Area Behind Commerce College JLN Marg, Jaipur-302004 Rajasthan Phone No:0141-2709659, 2709616 Mobile No.- 9928852083 E-mail: cifb[at]rajasthan[dot]gov[dot]in | Factories and Boilers Inspection Department, Rajasthan | 2 | 1 | 1 | 4 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary, Industries, Micro, Small & Medium Enterprise (M.S.M.E.), State Enterprises & Delhi Mumbai Industrial Corridor and O.S.D., BIDA & Additional Chief Secretary, Investment & NRIS, BIP, Rajasthan, Jaipur and Chairman, RIICO, Jaipur And Chairman And Managing Director, RAJSICO, Jaipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Additional Chief Secretary, Public Works Department, Rajasthan, Jaipur and Additional Chief Secretary, Tourism Department, Art, Literature, Culture & Archaeology Department and Director General, Jawahar Kala Kendra, Rajasthan, Jaipur and Chairman, Rajasthan Tourism Development Corporation, Rajasthan, Jaipur and Chief Executive Officer, Amber Development & Management Authority, Rajasthan, Jaipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Additional Chief Secretary, Water Resources Department, State Water Resources Planning Department, Rajasthan, Jaipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Chief Executive Officer, Zila Parishad-Cum- A.D.P.C., E.G.S & ex-officio Chief Project Officer (Mada), Bikaner

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |

### Commissioner, Colonisation Department and Commissioner, Command Area Development and Water Utility Department, Bikaner

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Commissioner, Jaipur Development Authority, Jaipur

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Factories and Boilers Inspection Department, Rajasthan

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Harish Kumar Gupta** — Chief Inspector of Factories & Boilers Factories & Boilers Inspection Department Govt. of Rajasthan 6-c, Jhalana Institutional Area Behind Commerce College JLN Marg, Jaipur-302004 Rajasthan Phone No:0141-2709659, 2709616 Mobile No.- 9928852083 E-mail: cifb[at]rajasthan[dot]gov[dot]in — cifb@rajasthan.gov.in (2) |
| HR: leave / pay / allowances / service rules | **Shri Harish Kumar Gupta** — Chief Inspector of Factories & Boilers Factories & Boilers Inspection Department Govt. of Rajasthan 6-c, Jhalana Institutional Area Behind Commerce College JLN Marg, Jaipur-302004 Rajasthan Phone No:0141-2709659, 2709616 Mobile No.- 9928852083 E-mail: cifb[at]rajasthan[dot]gov[dot]in — cifb@rajasthan.gov.in (1) |
| Licensing / approvals / standards / enlistment | **Shri Harish Kumar Gupta** — Chief Inspector of Factories & Boilers Factories & Boilers Inspection Department Govt. of Rajasthan 6-c, Jhalana Institutional Area Behind Commerce College JLN Marg, Jaipur-302004 Rajasthan Phone No:0141-2709659, 2709616 Mobile No.- 9928852083 E-mail: cifb[at]rajasthan[dot]gov[dot]in — cifb@rajasthan.gov.in (1) |

### HCMRIPA - Rajasthan State Institute of Public Administration, Rajasthan

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| HR: appointment / transfer / posting / promotion |  |
| HR: leave / pay / allowances / service rules |  |
| Other / unclassified |  |
| Procurement / tenders / GeM |  |

### Principal Secretary to Government, Agriculture and Horticulture And Panchayati Raj (Agriculture) Department, Rajasthan, Jaipur and Chairman, Rajasthan State Seeds Corporation Limited, Jaipur

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Rajasthan State Consumer Disputes Redressal Commission, Rajasthan | Registrar | Assistant / Secretary | 11 |  |
| Rajas than Police Academy, Rajasthan | Rajasthan Police Academy | Director | 10 |  |
| Rajas than Police Academy, Rajasthan | Jaipur | Director | 8 |  |
| Rajas than Police Academy, Rajasthan | Rajiv Dasot | Director | 5 |  |
| Central Goods & Services Tax, Jaipur Zone, Rajasthan | Sharma Surya Prakash Gulabchand | Commissioner | 4 |  |
| Central Goods & Services Tax, Jaipur Zone, Rajasthan | Ajay Gupta | Commissioner | 3 |  |
| Central Goods & Services Tax, Jaipur Zone, Rajasthan | Sharma Suryaprakash Gulabchand | Joint Commissioner / Joint Commissioner (CCU | 3 |  |
| Food and Civil Supplies Department, Rajasthan | Jaipur | Commissioner | 3 |  |
| Food and Civil Supplies Department, Rajasthan | Poonam Prasad Sagar | Commissioner | 3 |  |
| Food and Civil Supplies Department, Rajasthan | Rajastan Jaipur | Commissioner / Director | 3 |  |
| Integrated Financial Pension Management System, Rajasthan | Sanjay Solanki | Director | 3 |  |
| Food and Civil Supplies Department, Rajasthan | Ranu Meena | Commissioner | 2 |  |
| Food and Civil Supplies Department, Rajasthan | Rohit Gupta | Secretary | 2 |  |
| Food and Civil Supplies Department, Rajasthan | Sunil Poonia | Deputy Commissioner and Deputy Secretary to the Government. / Deputy Secretary to the Government. | 2 |  |
| RajCOMP Info Services Limited, Rajasthan | Sanjay Jangdeesh Karnik | Joint Secretary | 2 |  |
| RajCOMP Info Services Limited, Rajasthan | Sanjay Karnik | Joint Secretary / Secretary | 2 |  |
| Rajasthan Staff Selection Board, Jaipur, Rajasthan | BC Badhal | Secretary | 2 |  |
| Revenue Board, Rajasthan | Jayveer Singh | Deputy Secretary | 2 |  |
| Revenue Board, Rajasthan | Mahendra Prakash Sharma | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.