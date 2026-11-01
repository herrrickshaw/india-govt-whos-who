# JH — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (42 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 51 |
| PDFs with a detectable signature block | 51 |
| Signatures matched to a roster officer | 7 documents / 3 officers |
| Signatures not matched (person not in any roster, or moved) | 48 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture, Animal Husbandry and Cooperative Department, Jharkhand | 11 | 0 | 0 | 0 | 0 |
| Birsa Agricultural University, Ranchi, Jharkhand | 2 | 0 | 0 | 0 | 0 |
| Birsa Munda Tribal University, Jharkhand | 11 | 0 | 1 | 0 | 0 |
| Chief Minister's Office, Jharkhand | 11 | 0 | 2 | 0 | 0 |
| Deoghar | 1 | 0 | 0 | 0 | 0 |
| Department of Forest, Environment & Climate Change, Jharkhand | 11 | 0 | 0 | 0 | 0 |
| Division of Legal Metrology, Jharkhand | 6 | 0 | 0 | 0 | 0 |
| Dumka | 11 | 0 | 0 | 0 | 0 |
| East Singhbum | 8 | 0 | 1 | 0 | 0 |
| Finance Department, Jharkhand | 11 | 0 | 3 | 1 | 1 |
| Garhwa | 11 | 0 | 0 | 0 | 0 |
| Giridih | 4 | 0 | 0 | 0 | 0 |
| Gumla | 4 | 0 | 2 | 0 | 0 |
| Guruji Student Credit Card (GSCC) Scheme | 3 | 0 | 0 | 0 | 0 |
| Hazaribagh | 5 | 0 | 1 | 1 | 1 |
| Jamtara | 9 | 0 | 1 | 1 | 1 |
| Jharkhand Bijli Vitran Nigam Limited, Jharkhand | 11 | 0 | 0 | 0 | 0 |
| Jharkhand Council on Science, Technology and Innovation | 11 | 0 | 2 | 0 | 0 |
| Jharkhand Recruitment Portal | 11 | 0 | 0 | 0 | 0 |
| Jharkhand Rural Health Mission Society | 8 | 0 | 1 | 0 | 0 |
| Jharkhand State AIDS Control Society, Jharkhand | 4 | 0 | 1 | 0 | 0 |
| Jharkhand State Electricity Regulatory Commission, Jharkhand | 11 | 0 | 4 | 0 | 0 |
| Jharkhand State Information Commission, Jharkhand | 5 | 0 | 2 | 0 | 0 |
| Khunti | 1 | 0 | 0 | 0 | 0 |
| Kuber Integrated Financial Management System, Jharkhand | 11 | 0 | 6 | 4 | 1 |
| Latehar | 3 | 0 | 0 | 0 | 0 |
| Lohardaga | 11 | 0 | 3 | 0 | 0 |
| Pakur | 2 | 0 | 0 | 0 | 0 |
| Palamu | 1 | 0 | 0 | 0 | 0 |
| Ramgarh | 5 | 0 | 0 | 0 | 0 |
| Ranchi | 7 | 0 | 2 | 0 | 0 |
| Road Construction Department, Jharkhand | 11 | 0 | 4 | 0 | 0 |
| Sahebganj | 2 | 0 | 0 | 0 | 0 |
| Saraikela Kharsawan | 1 | 0 | 1 | 0 | 0 |
| Simdega | 1 | 0 | 0 | 0 | 0 |
| Sports Authority of Jharkhand, Jharkhand | 11 | 0 | 1 | 0 | 0 |
| State Agricultural Management and Extension Training Institute (SAMETI), Jharkhand | 11 | 0 | 0 | 0 | 0 |
| Tourism Department, Jharkhand | 11 | 0 | 3 | 0 | 0 |
| UID - Aadhaar Portal, Jharkhand | 4 | 0 | 0 | 0 | 0 |
| Urban Development & Housing Department, Government of Jharkhand | 11 | 0 | 9 | 0 | 0 |
| West Singhbhum | 7 | 0 | 0 | 0 | 0 |
| e-Kalyan - Student Scholarships by Welfare Department, Jharkhand | 9 | 0 | 1 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Secretary, Building Construction Department, Jharkhand

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Personnel, Administrative Reforms & Rajbhasha Deptt., Jharkhand

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Secretary, Water Resources Deptt, Jharkhand

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Urban Development & Housing Department, Government of Jharkhand | Vishwas Bhajan | Secretary | 9 |  |
| Jharkhand State Electricity Regulatory Commission, Jharkhand | Rajendra Prasad Nayak | Secretary | 4 |  |
| Lohardaga | Rajasv-shakha | Secretary | 3 |  |
| Tourism Department, Jharkhand | Aseem Kumar Jha | Under Secretary to the Government of India | 3 |  |
| Urban Development & Housing Department, Government of Jharkhand | Arun Kumar Singh | Secretary | 3 |  |
| Finance Department, Jharkhand | Anil Kumar Yadav | Deputy Secretary / Secretary | 2 |  |
| Gumla | - Gumala | Commissioner | 2 |  |
| Gumla | Jila Shiksha Adhikshak | Commissioner | 2 |  |
| Kuber Integrated Financial Management System, Jharkhand | Sukhdev Singh | Additional Chief Secretary | 2 |  |
| Lohardaga | Svikrityadesh | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.