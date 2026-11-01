# PB — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (44 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 31 |
| PDFs with a detectable signature block | 31 |
| Signatures matched to a roster officer | 4 documents / 3 officers |
| Signatures not matched (person not in any roster, or moved) | 29 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture and Farmer Welfare Department, Punjab | 9 | 0 | 0 | 0 | 0 |
| Amritsar | 6 | 0 | 0 | 0 | 0 |
| Barnala | 1 | 0 | 0 | 0 | 0 |
| Bathinda | 2 | 0 | 1 | 0 | 0 |
| Board of Ayurvedic and Unani Systems of Medicine, Punjab | 9 | 0 | 4 | 0 | 0 |
| Civil Aviation Department, Punjab | 9 | 0 | 1 | 0 | 0 |
| Co-operative Department, Punjab | 9 | 0 | 2 | 0 | 0 |
| Department of School Education, Punjab | 9 | 0 | 1 | 0 | 0 |
| Department of Sports, Punjab | 9 | 0 | 0 | 0 | 0 |
| Director State Transport, Punjab | 2 | 0 | 0 | 0 | 0 |
| Directorate of Environment and Climate Change, Punjab | 9 | 0 | 3 | 0 | 0 |
| Directorate of Information & Public Relation, Punjab | 9 | 0 | 2 | 0 | 0 |
| Dr B.R. Ambedkar State Institute of Medical Sciences, Punjab | 7 | 0 | 1 | 0 | 0 |
| Employment Generation, Skill Development and Training Department, Punjab | 4 | 0 | 1 | 1 | 1 |
| Excise and Taxation Department, Punjab | 9 | 0 | 2 | 0 | 0 |
| Faridkot | 9 | 0 | 0 | 0 | 0 |
| Ferozepur | 1 | 0 | 0 | 0 | 0 |
| Finance Department, Punjab | 9 | 0 | 3 | 0 | 0 |
| Forests and Wildlife Preservation Department, Punjab | 9 | 0 | 0 | 0 | 0 |
| Greater Mohali Area Development Authority (GMADA), Mohali, Punjab | 9 | 0 | 0 | 0 | 0 |
| Guru Angad Dev Veterinary and Animal Sciences University (GADVASU), Ludhiana Punjab | 5 | 0 | 0 | 0 | 0 |
| Health and Family Welfare Department, Punjab | 5 | 0 | 0 | 0 | 0 |
| I. K. Gujral Punjab Technical University, Jalandhar, Punjab | 9 | 0 | 1 | 0 | 0 |
| Institute of Hotel Management Catering Technology and Applied Nutrition, Bathinda, Punjab | 9 | 0 | 0 | 0 | 0 |
| Kapurthala | 3 | 0 | 0 | 0 | 0 |
| Ludhiana | 2 | 0 | 0 | 0 | 0 |
| Mahatma Gandhi State Institute of Public Administration (MGSIPAP), Punjab | 5 | 0 | 0 | 0 | 0 |
| Malerkotla | 4 | 0 | 0 | 0 | 0 |
| Mansa | 2 | 0 | 0 | 0 | 0 |
| Medical Education and Research Department, Punjab | 9 | 0 | 1 | 0 | 0 |
| Moga | 3 | 0 | 0 | 0 | 0 |
| NRI Affairs Department, Punjab | 2 | 0 | 0 | 0 | 0 |
| Pepsu Road Transport Corporation, Patiala, Punjab | 9 | 0 | 0 | 0 | 0 |
| Punjab Agro Industries Corporation Limited (PAIC), Punjab | 9 | 0 | 1 | 0 | 0 |
| Punjab Pollution Control Board (PPCB), Punjab | 9 | 0 | 2 | 1 | 1 |
| Punjab Roads and Bridges Development Board (PRBDB), Punjab | 9 | 0 | 0 | 0 | 0 |
| Punjab State Agricultural Marketing Board (Punjab Mandi Board, PSAMB), Punjab | 8 | 0 | 1 | 0 | 0 |
| Punjab State Council for Science and Technology, Punjab | 9 | 0 | 2 | 2 | 1 |
| Punjab State Electricity Regulatory Commission (PSERC), Punjab | 9 | 0 | 0 | 0 | 0 |
| Punjab State Human Rights Commission | 9 | 0 | 0 | 0 | 0 |
| Punjab State Power Corporation Limited (PSPCL), Punjab | 9 | 0 | 0 | 0 | 0 |
| Punjab University, P.U. Swami Sarvanand Giri Regional Centre, Punjab | 9 | 0 | 2 | 0 | 0 |
| S.R.S Govt. Polytechnic College, Ludhiana, Punjab | 4 | 0 | 0 | 0 | 0 |
| Vigilance Bureau, Punjab | 9 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Principal Secretary, Food, Civil Supplies & Consumer Affairs

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |

### Principal Secretary, Health and Family Welfare

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Special Chief Secretary-cum-Director General, Govt of Punjab, Mahatma Gandhi State Instt. of Public Admin

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Environment and Climate Change, Punjab | RITESH KUMAR SINGH | Jt. Secy | 2 |  |
| Excise and Taxation Department, Punjab | A.VENU PRASAD | Secretary (Taxation) to | 2 |  |
| Punjab State Council for Science and Technology, Punjab | Chairman PPCB | Secretary PPCB. ; \\ | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.