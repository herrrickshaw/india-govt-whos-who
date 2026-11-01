# SK — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (10 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 273 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 64 |
| PDFs with a detectable signature block | 64 |
| Signatures matched to a roster officer | 11 documents / 4 officers |
| Signatures not matched (person not in any roster, or moved) | 56 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Department, Sikkim | 2 | 0 | 0 | 0 | 0 |
| Co-operation Department, Sikkim | 21 | 0 | 3 | 2 | 2 |
| Cultural Department, Sikkim | 9 | 0 | 2 | 0 | 0 |
| Energy and Power Department, Sikkim | 54 | 0 | 12 | 0 | 0 |
| Food, Civil Supplies and Consumer Affairs Department, Sikkim | 2 | 0 | 0 | 0 | 0 |
| Housing and Development Board, Sikkim | 11 | 0 | 0 | 0 | 0 |
| Information and Public Relations Department, Sikkim | 9 | 0 | 1 | 0 | 0 |
| Labour Department, Sikkim | 13 | 0 | 1 | 0 | 0 |
| Police Department, Sikkim | 64 | 0 | 10 | 0 | 0 |
| Rural Development Department, Sikkim | 88 | 0 | 35 | 9 | 2 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Secretary, Department of Expenditure, M/o Finance, Government of India, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |
| Other / unclassified |  |

### Commissioner-cum-Secretary, Women, Child, Senior Citizen and Divyangjan Welfare Department, Government of Sikkim

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Department of Personnel w.e.f. 18.09.2023 with the Additional charge of Secretary, Land Revenue & Disaster Management Department, Government of Sikkim w.e.f. 30.10.2025.

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Rural Development Department, Government of Sikkim

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| Office administration / housekeeping |  |
| Other / unclassified |  |
| Training / capacity building / workshops |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Rural Development Department, Sikkim | TSHERING LHADEN LACHUNGPA | ADDITIONAL SECRETARY / SPECIAL SECRETARY | 8 |  |
| Rural Development Department, Sikkim | BENU GURUNG | . SECRETARY / SPECIAL SECRETARY | 4 |  |
| Energy and Power Department, Sikkim | Above Officials | Secretary, Power Department. | 2 |  |
| Energy and Power Department, Sikkim | Bikash Deokota | Secretary | 2 |  |
| Energy and Power Department, Sikkim | GHANSHYAM PRASAD | Jt. Secy | 2 |  |
| Energy and Power Department, Sikkim | Power Departeni | Officer. | 2 |  |
| Energy and Power Department, Sikkim | SRIKANT NAGULAPALLI | Addl. Secy | 2 |  |
| Police Department, Sikkim | Sikkim Police | Director General of Police | 2 |  |
| Rural Development Department, Sikkim | KOSHI KAPIL | ADDITIONAL SECRETARY | 2 |  |
| Rural Development Department, Sikkim | Norgay Lepcha | Director (Finance & Accounts), RDD | 2 |  |
| Rural Development Department, Sikkim | Sisila Lama Tam | Director (T) / Officer | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.