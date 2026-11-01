# TR — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (11 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 133 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 11 |
| PDFs with a detectable signature block | 11 |
| Signatures matched to a roster officer | 2 documents / 2 officers |
| Signatures not matched (person not in any roster, or moved) | 9 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Digital India Land Records Modernization Programme (DILRMP), Tripura | 7 | 0 | 0 | 0 | 0 |
| Digital Seva e-District Portal, Tripura | 2 | 0 | 1 | 1 | 1 |
| KTDS Police Training Academy, Tripura | 1 | 0 | 0 | 0 | 0 |
| The Tripura State Medical Council, Tripura | 1 | 0 | 0 | 0 | 0 |
| Tripura Farmers Portal & Kisan Call Center (KCC), Tripura | 32 | 0 | 8 | 1 | 1 |
| Tripura JICA Project - Sustainable Catchment Forest Management (SCATFORM), Tripura | 32 | 0 | 0 | 0 | 0 |
| Tripura Nursing Council, Tripura | 4 | 0 | 0 | 0 | 0 |
| Tripura Renewable Energy Development Agency, Tripura | 4 | 0 | 0 | 0 | 0 |
| Tripura State Blood Transfusion Council, Tripura | 2 | 0 | 0 | 0 | 0 |
| Tripura State Council For Science & Technology, Tripura | 16 | 0 | 0 | 0 | 0 |
| Tripura Tribal Areas Autonomous District Council (TTAADC), Tripura | 32 | 0 | 2 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Secretary & Financial Advisor, GOI, M/o. Road Transport & Highways (MoRTH) and M/o. Ports, Shipping & Waterways, New Delhi.

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Tripura JICA Project - Sustainable Catchment Forest Management (SCATFORM), Tripura

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Tripura Farmers Portal & Kisan Call Center (KCC), Tripura | K. V. Satyanarayanan | Principal Secretary to the | 2 |  |
| Tripura Farmers Portal & Kisan Call Center (KCC), Tripura | V. K. Bahuguna | Principal Secretary to the | 2 |  |
| Tripura Tribal Areas Autonomous District Council (TTAADC), Tripura | B. K. Goswami | Principal Officer(Law / Principal Ofﬁcer(Law | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.