# LD — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (8 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 92 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 15 |
| PDFs with a detectable signature block | 16 |
| Signatures matched to a roster officer | 1 documents / 1 officers |
| Signatures not matched (person not in any roster, or moved) | 15 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Electricity (Power) Department, Lakshadweep | 5 | 0 | 0 | 0 | 0 |
| Lakshadweep District | 26 | 0 | 2 | 0 | 0 |
| Lakshadweep Information Technology Services Society (LITSS), Lakshadweep | 6 | 0 | 1 | 0 | 0 |
| Lakshadweep Tourism, Society for Promotion of Nature Tourism and Sports, Lakshadweep | 2 | 0 | 0 | 0 | 0 |
| Mid Day Meal Scheme, Lakshadweep | 41 | 0 | 9 | 1 | 1 |
| Public Distribution System Portal, Lakshadweep | 9 | 0 | 3 | 0 | 0 |
| Public Works Department, Lakshadweep | 1 | 0 | 1 | 0 | 0 |
| ePermit - Online Entry Permit System, Lakshadweep | 2 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Customs / tariff / duty / GST | TOTAL |
|---|---|---|---|---|
| Shri Buzar Jamhar | Director of Food & Civil Supplies, Panchayat and LCMF | Lakshadweep District | 1 | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Lakshadweep District

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST | **Shri Buzar Jamhar** — Director of Food & Civil Supplies, Panchayat and LCMF — fcskvt@gmail.com (1) |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Public Distribution System Portal, Lakshadweep | Lakshadweep Govt. Press | Advisor to the Hon’ble Administrator UT of Lakshadweep. / Advisor to the Hon’ble Administrator, UT of Lakshadweep. | 3 |  |
| Mid Day Meal Scheme, Lakshadweep | Anant Kumar Singh | Joint Secretary to the Govt. of India | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.