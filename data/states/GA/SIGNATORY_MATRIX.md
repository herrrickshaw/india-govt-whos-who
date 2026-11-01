# GA — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (29 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 75 |
| PDFs with a detectable signature block | 77 |
| Signatures matched to a roster officer | 6 documents / 7 officers |
| Signatures not matched (person not in any roster, or moved) | 72 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Captain of Ports Department, Goa | 13 | 0 | 1 | 0 | 0 |
| Civil Aviation Department, Goa | 4 | 0 | 2 | 1 | 1 |
| Civil Supplies and Consumer Affairs Department, Goa | 13 | 0 | 4 | 0 | 0 |
| Co-operation Department, Goa | 11 | 0 | 2 | 0 | 0 |
| Directorate of Health Services, National Health Mission, Goa | 13 | 0 | 3 | 0 | 0 |
| Directorate of Mines and Geology, Goa | 13 | 0 | 5 | 0 | 0 |
| Directorate of Official Language, Goa | 10 | 0 | 3 | 0 | 0 |
| Directorate of Settlement & Land Records, Goa | 12 | 0 | 2 | 1 | 1 |
| Directorate of Small Savings and Lotteries, Goa | 13 | 0 | 3 | 0 | 0 |
| Directorate of Sports and Youth Affairs, Goa | 13 | 0 | 1 | 0 | 0 |
| Directorate of Technical Education, Goa | 13 | 0 | 5 | 0 | 0 |
| EDC Limited, Goa | 10 | 0 | 3 | 0 | 0 |
| Electricity (Power) Department, Goa | 13 | 0 | 4 | 1 | 1 |
| Environment & Climate Change Department, Goa | 8 | 0 | 0 | 0 | 0 |
| Fisheries Department, Goa | 13 | 0 | 2 | 0 | 0 |
| Forest Department, Goa | 13 | 0 | 1 | 0 | 0 |
| Gazetteer Department, Goa | 13 | 0 | 6 | 0 | 0 |
| Goa College of Architecture, Goa | 13 | 0 | 7 | 0 | 0 |
| Goa Dental College & Hospital, Goa | 3 | 0 | 0 | 0 | 0 |
| Goa Housing Board | 13 | 0 | 2 | 0 | 0 |
| Goa State Infrastructure Development Corporation Limited (GSIDL), Goa | 4 | 0 | 2 | 0 | 0 |
| Goa State Pollution Control Board, Goa | 13 | 0 | 5 | 0 | 0 |
| Goa State Urban Development Agency, Goa | 1 | 0 | 0 | 0 | 0 |
| Goa University, Goa | 13 | 0 | 2 | 0 | 0 |
| Government Polytechnic, Bicholim, Goa | 5 | 0 | 2 | 2 | 3 |
| Handicrafts, Textile and Coir Department, Goa | 1 | 0 | 0 | 0 | 0 |
| Health Services Department, Goa | 13 | 0 | 2 | 1 | 1 |
| Inspectorate of Factories & Boilers, Goa | 13 | 0 | 8 | 0 | 0 |
| Pernem Government Industrial Training Institute, Goa | 10 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Addl. PS to Hon'ble Speaker, Lok Sabha

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Civil Supplies and Consumer Affairs Department, Goa

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| HR: leave / pay / allowances / service rules |  |

### Dy. Commissioner, Kargil & CEO, LAHDC, Kargil UT of Ladakh 10.06.2025

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |
| Training / capacity building / workshops |  |

### Government Polytechnic, Bicholim, Goa

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |

### Joint Secretary, Cabinet Secretariat, Govt. of India

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |
| Procurement / tenders / GeM |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Health Services, National Health Mission, Goa | Geeta Kakodkar | Director of Health Services | 2 |  |
| Directorate of Mines and Geology, Goa | Narayan Gad | Additional Secretary Mines | 2 |  |
| Directorate of Mines and Geology, Goa | Narayan M. Gad | Director & ex-officio Additional Secretary / Director & | | 2 |  |
| Directorate of Official Language, Goa | Prakash Vazrikar | Director & ex officio Joint / Director of Official Language & | 2 |  |
| Directorate of Small Savings and Lotteries, Goa | Veera V. Nayak | Director | 2 |  |
| EDC Limited, Goa | Pranab G. Bhat | Under Secretary Finance (Bud-II / Under Secretary Finance (Budget-II | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.