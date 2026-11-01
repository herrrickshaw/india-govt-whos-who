# PY — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (24 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 220 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 32 |
| PDFs with a detectable signature block | 32 |
| Signatures matched to a roster officer | 6 documents / 4 officers |
| Signatures not matched (person not in any roster, or moved) | 27 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture and Farmers Welfare Department, Puducherry | 17 | 0 | 0 | 0 | 0 |
| Animal Husbandry and Animal Welfare Department, Puducherry | 1 | 0 | 1 | 0 | 0 |
| Arts and Culture Department, Puducherry | 4 | 0 | 1 | 0 | 0 |
| Commercial Taxes Department, Puducherry | 4 | 0 | 2 | 1 | 1 |
| District Industries Centre (DIC), Puducherry | 1 | 0 | 0 | 0 | 0 |
| District Institute of Education and Training (DIET), Puducherry | 17 | 0 | 1 | 0 | 0 |
| Dr. Sarvepalli Radhakrishnan Government Arts College, Yanam, Puducherry | 10 | 0 | 1 | 0 | 0 |
| Finance Department, Puducherry | 6 | 0 | 1 | 0 | 0 |
| Fire Services Department, Puducherry | 3 | 0 | 1 | 0 | 0 |
| Forest and Wild Life Department, Puducherry | 17 | 0 | 5 | 1 | 1 |
| Higher and Technical Education Department, Puducherry | 17 | 0 | 2 | 0 | 0 |
| Industries and Commerce Department, Puducherry | 8 | 0 | 5 | 1 | 1 |
| Information Technology Department, Puducherry | 10 | 0 | 4 | 2 | 1 |
| Law Department, Puducherry | 17 | 0 | 4 | 1 | 1 |
| Local Administration Department, Puducherry | 7 | 0 | 1 | 0 | 0 |
| Mahatma Gandhi Postgraduate Institute of Dental Sciences (MGPGIDS), Puducherry | 2 | 0 | 0 | 0 | 0 |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | 17 | 0 | 1 | 0 | 0 |
| Online Building Permission System, Puducherry | 5 | 0 | 0 | 0 | 0 |
| Portal for Single Windeows System for Licensing (LicenseSoft), Puducherry | 3 | 0 | 1 | 0 | 0 |
| Puducherry | 2 | 0 | 0 | 0 | 0 |
| Puducherry Industrial Promotion Development and Investment Corporation (PIPDIC), Puducherry | 17 | 0 | 1 | 0 | 0 |
| Puducherry Power Corporation Limited (PPCL), Puducherry | 17 | 0 | 0 | 0 | 0 |
| Puducherry State Disaster Management Authority | 1 | 0 | 0 | 0 | 0 |
| Puduvaicalal, Puducherry | 17 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | HR: appointment / transfer / posting / promotion | HR: leave / pay / allowances / service rules | Scheme guidelines / implementation | TOTAL |
|---|---|---|---|---|---|---|
| Thiru. Shivraj Meena | The Regional Administrator, Yanam | Puducherry | 1 | 1 | 2 | 4 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Chief Secretary, Govt of Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (1) |
| HR: leave / pay / allowances / service rules | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (1) |
| Scheme guidelines / implementation | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (2) |

### Secretary (Cooperation, Food & Supplies, Consumer Affairs & Legal Metrology) and CEO, Waqf Board, Chandigarh

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Customs / tariff / duty / GST |  |

### Secretary (Industries, Trade & Commerce, Civil Supplies, Cooperation & Law, HRI, Waqf) & Excise Commissioner, Govt. of Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Industries and Commerce Department, Puducherry | G. M ALAR KANNAN | Additional Secretary / Additional Secretary to Government | 2 |  |
| Law Department, Puducherry | N. MURUGAVEL | UNDER SECRETARY(LAW | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.