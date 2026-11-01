# PY — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (24 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 600 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 112 |
| PDFs with a detectable signature block | 116 |
| Signatures matched to a roster officer | 8 documents / 6 officers |
| Signatures not matched (person not in any roster, or moved) | 109 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture and Farmers Welfare Department, Puducherry | 72 | 0 | 4 | 0 | 0 |
| Animal Husbandry and Animal Welfare Department, Puducherry | 1 | 0 | 1 | 0 | 0 |
| Arts and Culture Department, Puducherry | 4 | 0 | 1 | 0 | 0 |
| Commercial Taxes Department, Puducherry | 4 | 0 | 2 | 1 | 1 |
| District Industries Centre (DIC), Puducherry | 1 | 0 | 0 | 0 | 0 |
| District Institute of Education and Training (DIET), Puducherry | 72 | 0 | 17 | 0 | 0 |
| Dr. Sarvepalli Radhakrishnan Government Arts College, Yanam, Puducherry | 10 | 0 | 1 | 0 | 0 |
| Finance Department, Puducherry | 6 | 0 | 1 | 0 | 0 |
| Fire Services Department, Puducherry | 3 | 0 | 1 | 0 | 0 |
| Forest and Wild Life Department, Puducherry | 72 | 0 | 29 | 2 | 2 |
| Higher and Technical Education Department, Puducherry | 53 | 0 | 9 | 0 | 0 |
| Industries and Commerce Department, Puducherry | 8 | 0 | 5 | 1 | 1 |
| Information Technology Department, Puducherry | 10 | 0 | 4 | 2 | 1 |
| Law Department, Puducherry | 43 | 0 | 12 | 1 | 1 |
| Local Administration Department, Puducherry | 7 | 0 | 1 | 0 | 0 |
| Mahatma Gandhi Postgraduate Institute of Dental Sciences (MGPGIDS), Puducherry | 2 | 0 | 0 | 0 | 0 |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | 72 | 0 | 16 | 0 | 0 |
| Online Building Permission System, Puducherry | 5 | 0 | 0 | 0 | 0 |
| Portal for Single Windeows System for Licensing (LicenseSoft), Puducherry | 3 | 0 | 1 | 0 | 0 |
| Puducherry | 2 | 0 | 0 | 0 | 0 |
| Puducherry Industrial Promotion Development and Investment Corporation (PIPDIC), Puducherry | 17 | 0 | 1 | 0 | 0 |
| Puducherry Power Corporation Limited (PPCL), Puducherry | 72 | 0 | 4 | 0 | 0 |
| Puducherry State Disaster Management Authority | 1 | 0 | 0 | 0 | 0 |
| Puduvaicalal, Puducherry | 60 | 0 | 6 | 1 | 1 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Customs / tariff / duty / GST | HR: appointment / transfer / posting / promotion | HR: leave / pay / allowances / service rules | Scheme guidelines / implementation | TOTAL |
|---|---|---|---|---|---|---|---|
| Thiru. Shivraj Meena | The Regional Administrator, Yanam | Puducherry |  | 1 | 1 | 2 | 4 |
| Thiru. T. Sudhakar | Additional Collector-cum-Director, PSEC | Puducherry | 1 |  |  |  | 1 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Chief Secretary, Govt of Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST | **Thiru. T. Sudhakar** — Additional Collector-cum-Director, PSEC — Addl-Collectorpdy@py.gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (1) |
| HR: leave / pay / allowances / service rules | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (1) |
| Scheme guidelines / implementation | **Thiru. Shivraj Meena** — The Regional Administrator, Yanam — ra.yanam@py.gov.in (2) |

### Puduvaicalal, Puducherry

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| Customs / tariff / duty / GST |  |

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
| Law Department, Puducherry | N. MURUGAVEL | UNDER SECRETARY (LAW / UNDER SECRETARY TO GOVT. (LAW | 8 |  |
| Higher and Technical Education Department, Puducherry | SUNDARARAJAN. P | OFFICER ON SPECIAL DUTY | 7 |  |
| Forest and Wild Life Department, Puducherry | M.V. HIRAN | SECRETARY TO GOVERNMENT / UNDER SECRETARY TO GOVERNMENT | 6 |  |
| Forest and Wild Life Department, Puducherry | S. UDAYASANKAR | DIRECTOR | 3 |  |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | C Thiyagarajan | ADDITIONAL / Additional Commissioner | 3 |  |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | K. VENKAT RAM REDDY | ADDITIONAL COMMISSIONER | 3 |  |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | K. VENKAT REDDY | ADDITIONAL COMMISSIONER | 3 |  |
| Agriculture and Farmers Welfare Department, Puducherry | N.K. SHANMUGAVELU | JOINT DIRECTOR OF AGRICULTURE (HORTI / JOINT DIRECTOR OF AGRICULTURE (MCP | 2 |  |
| District Institute of Education and Training (DIET), Puducherry | M. LENTNRAJ | DEPUTY DIRECTOR / DIRECTOR | 2 |  |
| Forest and Wild Life Department, Puducherry | S. MURUGESAN | UNDER SECRETARY TO GOVT.(HEALTH-1 | 2 |  |
| Forest and Wild Life Department, Puducherry | Samir Kumar Das | Deputy Secretary to the Government of India | 2 |  |
| Industries and Commerce Department, Puducherry | G. M ALAR KANNAN | Additional Secretary / Additional Secretary to Government | 2 |  |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | D Jayapriya | ADDITIONAL COMMISSIONER / Additional Commissioner (PCCO | 2 |  |
| Office of the Principal Chief Commissioner of GST & Central Excise Tamil Nadu & Puducherry Zone, Puducherry | Poonam P. Thakare | Deputy Commissioner / Deputy Commissionerof GST & C. Ex. | 2 |  |
| Puduvaicalal, Puducherry | G. JOHNSON | Under Secretary to Government / Under Secretary to Government (Revenue). | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.