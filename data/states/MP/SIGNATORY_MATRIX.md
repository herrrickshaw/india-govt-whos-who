# MP — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (47 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 38 |
| PDFs with a detectable signature block | 38 |
| Signatures matched to a roster officer | 2 documents / 2 officers |
| Signatures not matched (person not in any roster, or moved) | 36 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Alirajpur | 1 | 0 | 0 | 0 | 0 |
| Anuppur | 2 | 0 | 0 | 0 | 0 |
| Ashoknagar | 2 | 0 | 0 | 0 | 0 |
| Backward Classes and Minorities Welfare Department, Madhya Pradesh | 3 | 0 | 0 | 0 | 0 |
| Bhopal Gas Tragedy Relief and Rehabilitation Department, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Board of Secondary Education, Madhya Pradesh | 10 | 0 | 3 | 0 | 0 |
| Burhanpur | 1 | 0 | 0 | 0 | 0 |
| Chhindwara | 3 | 0 | 0 | 0 | 0 |
| Computer Proficiency Certification Test (CPCT), Madhya Pradesh | 2 | 0 | 0 | 0 | 0 |
| Culture Department, Madhya Pradesh | 10 | 0 | 1 | 0 | 0 |
| Damoh | 1 | 0 | 0 | 0 | 0 |
| Devi Ahilya Vishwavidyalaya, Indore, Madhya Pradesh | 10 | 0 | 3 | 0 | 0 |
| Dhar | 6 | 0 | 0 | 0 | 0 |
| Dindori | 2 | 0 | 2 | 0 | 0 |
| Directorate of Estates, Madhya Pradesh | 5 | 0 | 0 | 0 | 0 |
| Directorate of Institutional Finance, Madhya Pradesh | 10 | 0 | 2 | 1 | 1 |
| Directorate of Pension Provident Fund and Insurance (DoPPFI), Madhya Pradesh | 1 | 0 | 1 | 0 | 0 |
| Directorate of Sainik Welfare, Madhya Pradesh | 1 | 0 | 0 | 0 | 0 |
| Directorate of Technical Education, Madhya Pradesh | 10 | 0 | 5 | 0 | 0 |
| Directorate of Town and Country Planning, Madhya Pradesh | 10 | 0 | 1 | 0 | 0 |
| Disaster Management Institute (DMI), Madhya Pradesh | 1 | 0 | 0 | 0 | 0 |
| Environmental Planning & Coordination Organisation (EPCO), Madhya Pradesh | 7 | 0 | 0 | 0 | 0 |
| Farmer Welfare and Agriculture Development Department, Madhya Pradesh | 10 | 0 | 1 | 0 | 0 |
| Forest Department, Madhya Pradesh | 10 | 0 | 3 | 1 | 1 |
| Government Holkar (Model, Autonomous) Science College, Indore, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Higher Education Department, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| ICFRE - Tropical Forest Research Institute, Jabalpur, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| IForms MPOnline Limited Portal | 10 | 0 | 0 | 0 | 0 |
| Income Tax Department, Madhya Pradesh and Chhattisgarh | 3 | 0 | 0 | 0 | 0 |
| Indore | 3 | 0 | 0 | 0 | 0 |
| Jabalpur | 1 | 0 | 0 | 0 | 0 |
| Jiwaji University, Gwalior, Madhya Pradesh | 10 | 0 | 1 | 0 | 0 |
| M.P Power Generating Company Limited (MPPGCL), Madhya Pradesh | 10 | 0 | 6 | 0 | 0 |
| M.P. Housing and Infrastructure Development Board, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| M.P. Power Management Company Limited, Jabalpur, Madhya Pradesh | 4 | 0 | 1 | 0 | 0 |
| Madhya Pradesh Commercial Tax Appellate Board, Madhya Pradesh | 2 | 0 | 0 | 0 | 0 |
| Madhya Pradesh Madhya Kshetra Vidyut Vitaran Co. Ltd., Bhopal, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Madhya Pradesh Pollution Control Board, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Madhya Pradesh Power Transmission Company Ltd. (MPPTCL), Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Madhya Pradesh State Pharmacy Council, Madhya Pradesh | 10 | 0 | 4 | 0 | 0 |
| Mahatma Gandhi Chitrakoot Gramodaya University, Chitrakoot, Satna | 7 | 0 | 3 | 0 | 0 |
| Pt. Khushilal Sharma Government (Autonomous) Ayurveda College & Institute Bhopal, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| RCVP Noronha Academy of Administration, Bhopal, Madhya Pradesh | 1 | 0 | 0 | 0 | 0 |
| Rajiv Gandhi Proudyogiki Vishwavidyalaya, State Technical University, Madhya Pradesh | 7 | 0 | 0 | 0 | 0 |
| Rajmata Vijayaraje Scindia Krishi Vishwavidyalaya (RVSKVV), Gwalior, Madhya Pradesh | 10 | 0 | 0 | 0 | 0 |
| Staff Selection Commission (SSC), Madhya Pradesh Region | 10 | 0 | 1 | 0 | 0 |
| The National Law Institute University, Bhopal (NLIU), Madhya Pradesh | 4 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Commissioner, Gwalior Division, Madhya Pradesh

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### OSD-cum-Commissioner- cum-Director, Institutional Finance & Director, Budget, MP, Bhopal (Addl. charge).

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Madhya Pradesh State Pharmacy Council, Madhya Pradesh | ANIL MITTAL | Registrar-Cum-Secretary | 4 |  |
| Devi Ahilya Vishwavidyalaya, Indore, Madhya Pradesh | Umesh Balonda | Secretary, NCAHP | 2 |  |
| Dindori | VARSHA SOLANKI | DEPUTY SECRETARY | 2 |  |
| Directorate of Technical Education, Madhya Pradesh | Til P | Assistant / Commissioner | 2 |  |
| M.P Power Generating Company Limited (MPPGCL), Madhya Pradesh | Jabalpur | Assistant / Joint Secretary | 2 |  |
| M.P Power Generating Company Limited (MPPGCL), Madhya Pradesh | M.P. PO Jan. K. Li. Jabalpur | Director | 2 |  |
| Mahatma Gandhi Chitrakoot Gramodaya University, Chitrakoot, Satna | Sachindra Rao | Under Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.