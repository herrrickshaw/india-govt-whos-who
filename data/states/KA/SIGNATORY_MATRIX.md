# KA — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (35 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 66 |
| PDFs with a detectable signature block | 66 |
| Signatures matched to a roster officer | 1 documents / 1 officers |
| Signatures not matched (person not in any roster, or moved) | 66 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agricultural Marketing Department, Karnataka | 9 | 0 | 2 | 0 | 0 |
| Agriculture Department, Karnataka | 9 | 0 | 1 | 0 | 0 |
| Agriculture Secretariat, Karnataka | 9 | 0 | 7 | 0 | 0 |
| Backward Classes Department, Karnataka | 9 | 0 | 1 | 0 | 0 |
| Bangalore Metropolitan Transport Corporation (BMTC), Karnataka | 9 | 0 | 1 | 0 | 0 |
| Chamundeshwari Electricity Supply Corporation Limited Mysore, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Commissionerate of Health & Family Welfare Service, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Department of School Education & Literacy, Karnataka | 9 | 0 | 8 | 1 | 1 |
| Department of Technical Education | 9 | 0 | 1 | 0 | 0 |
| Directorates of Minorities, Karnataka | 9 | 0 | 3 | 0 | 0 |
| Drug Control Department, Karnataka | 9 | 0 | 4 | 0 | 0 |
| Ecology and Environment Department, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Empowerment of Differently Abled and Senior Citizens Department, Karnataka | 9 | 0 | 1 | 0 | 0 |
| Energy Department, Karnataka | 9 | 0 | 6 | 0 | 0 |
| Handlooms and Textiles Department, Karnataka | 1 | 0 | 0 | 0 | 0 |
| Higher Education Department, Karnataka | 9 | 0 | 2 | 0 | 0 |
| Home Department, Karnataka | 9 | 0 | 5 | 0 | 0 |
| Industries and Commerce Department, Karnataka | 9 | 0 | 6 | 0 | 0 |
| International Institute of Information Technology Bangalore, Karnataka | 9 | 0 | 2 | 0 | 0 |
| Karnataka Housing Board, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Karnataka Minorities Development Corporation Limited, Karnataka | 9 | 0 | 5 | 0 | 0 |
| Karnataka Power Transmission Corporation Limited, Karnataka | 9 | 0 | 3 | 0 | 0 |
| Karnataka Real Estate Regulatory Authority | 9 | 0 | 1 | 0 | 0 |
| Karnataka Rural Infrastructure Development Limited, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Karnataka School Examination and Assessment Board, Karnataka | 9 | 0 | 3 | 0 | 0 |
| Karnataka State Diploma in Nursing Examination Board, Karnataka | 7 | 0 | 2 | 0 | 0 |
| Karnataka State Electronics Development Corporation Limited (KEONICS), Karnataka | 9 | 0 | 1 | 0 | 0 |
| Karnataka State Industrial and Infrastructure Development Corporation | 9 | 0 | 0 | 0 | 0 |
| Karnataka State Warehousing Corporation, Karnataka | 9 | 0 | 0 | 0 | 0 |
| Malnad College of Engineering, Hassan, Karnataka | 8 | 0 | 0 | 0 | 0 |
| Mangalore Electricity Supply Company, Karnataka | 5 | 0 | 0 | 0 | 0 |
| Mangalore University, Konaje, Karnataka | 9 | 0 | 0 | 0 | 0 |
| National Law School of India University, Bengaluru,, Karnataka | 9 | 0 | 1 | 0 | 0 |
| Visveswaraiah Technological University, Belagaiv, Karnataka | 9 | 0 | 0 | 0 | 0 |
| e-Mapan, Legal Metrology Department, Karnataka | 9 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary to Government, School Education and Literacy Department, Bengaluru

| Topic | Contact officers (docs signed) |
|---|---|
| Scheme guidelines / implementation |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Agriculture Secretariat, Karnataka | Prati | Director / Secretary | 4 |  |
| Karnataka Minorities Development Corporation Limited, Karnataka | Nagaraja | Under Secretary | 4 |  |
| Department of School Education & Literacy, Karnataka | Shubhamangala R.V | Under Secretary to Government (Planning | 3 |  |
| Directorates of Minorities, Karnataka | Prati Mahithigagi | Secretary | 2 |  |
| Drug Control Department, Karnataka | pratiyannu | Principal Secretary / Secretary | 2 |  |
| Energy Department, Karnataka | SAMEER MADIMAN | Officer / Officer, | 2 |  |
| Industries and Commerce Department, Karnataka | ivarage | Commissioner / Director | 2 |  |
| Industries and Commerce Department, Karnataka | mattu avara hesarindalli | Under Secretary | 2 |  |
| Industries and Commerce Department, Karnataka | Prati Mahithigagi | Principal Secretary | 2 |  |
| Industries and Commerce Department, Karnataka | sevegalu mattu samanvaya | Commissioner | 2 |  |
| Karnataka Minorities Development Corporation Limited, Karnataka | mattu avara hesarindalli | Under Secretary | 2 |  |
| Karnataka State Diploma in Nursing Examination Board, Karnataka | Prati | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.