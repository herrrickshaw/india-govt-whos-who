# MH — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (49 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 40 |
| PDFs with a detectable signature block | 40 |
| Signatures matched to a roster officer | 5 documents / 4 officers |
| Signatures not matched (person not in any roster, or moved) | 35 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Department, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Animal Husbandry Department, Maharashtra | 8 | 0 | 2 | 0 | 0 |
| Atomic Energy Central School-1, Mumbai, Maharashtra | 7 | 0 | 0 | 0 | 0 |
| COEP Technological University, Pune, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Charity Commissioner, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Co-operation, Marketing and Textiles Department, Maharashtra | 3 | 0 | 0 | 0 | 0 |
| Commissioner for Cooperation and Registrar, Cooperative Societies (CC and RCS), Pune, Maharashtra | 2 | 0 | 1 | 0 | 0 |
| Commissionerate of Skill Development, Employment & Entrepreneurship, Maharashtra | 4 | 0 | 0 | 0 | 0 |
| Crime Investigation Department, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Cultural Affairs Department, Maharashtra | 5 | 0 | 0 | 0 | 0 |
| Dairy Development Department, Maharashtra | 4 | 0 | 0 | 0 | 0 |
| Director General, Geology and Mining, Nagpur, Maharashtra | 8 | 0 | 1 | 0 | 0 |
| Directorate General of Information and Public Relations, Maharashtra | 5 | 0 | 1 | 0 | 0 |
| Directorate of Accounts and Treasuries, Maharashtra | 1 | 0 | 1 | 1 | 1 |
| Directorate of Higher Education, Maharashtra | 8 | 0 | 2 | 0 | 0 |
| Directorate of Information Technology, Maharashtra | 2 | 0 | 0 | 0 | 0 |
| Directorate of Medical Education & Research, Mumbai | 8 | 0 | 1 | 0 | 0 |
| Directorate of Silk, Maharashtra | 1 | 0 | 0 | 0 | 0 |
| Directorate of Technical Education, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Directorate of Vocational Education and Training, Maharashtra | 8 | 0 | 1 | 0 | 0 |
| Dr. Babasaheb Ambedkar Technological University, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Finance Department, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Fisheries Department, Maharashtra | 2 | 0 | 0 | 0 | 0 |
| Food and Drug Administration, Maharashtra | 5 | 0 | 0 | 0 | 0 |
| Food, Civil Supplies and Consumer Protection Department, Maharashtra | 1 | 0 | 0 | 0 | 0 |
| Forest Department, Maharashtra | 8 | 0 | 1 | 0 | 0 |
| General Administration Department, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Goods and Services Tax Department, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Government College of Engineering, Chhatrapati Sambhajinagar, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Government Medical College and Hospital Nagpur (MS), Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Government Ploytechnic, Karad, Maharashtra | 2 | 0 | 1 | 0 | 0 |
| Government Polytechnic, Ahmednagar, Maharashtra | 6 | 0 | 0 | 0 | 0 |
| Government Polytechnic, Amravati, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Government Polytechnic, Dharashiv, Maharashtra | 4 | 0 | 0 | 0 | 0 |
| Government Polytechnic, Mumbai, Maharashtra | 8 | 0 | 2 | 0 | 0 |
| Greater Mumbai Police, Maharashtra | 8 | 0 | 3 | 0 | 0 |
| Higher and Technical Education Department, Maharashtra | 8 | 0 | 1 | 0 | 0 |
| Home Department, Maharashtra | 8 | 0 | 4 | 0 | 0 |
| Labour Department, Maharashtra | 8 | 0 | 4 | 0 | 0 |
| Law and Judiciary Department, Maharashtra | 7 | 0 | 2 | 0 | 0 |
| Legal Metrology Organization, Maharashtra | 7 | 0 | 2 | 1 | 1 |
| Maharashtra Housing and Area Development Authority (MHADA), Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Maharashtra State Excise Duty, Maharashtra | 8 | 0 | 0 | 0 | 0 |
| Maharashtra State Police, Maharashtra | 8 | 0 | 2 | 0 | 0 |
| Medical Education and Drugs Department, Maharashtra | 3 | 0 | 1 | 0 | 0 |
| Minority Development Department, Maharashtra | 4 | 0 | 1 | 0 | 0 |
| Motor Vehicles Department ( R.T.O.), Maharashtra | 8 | 0 | 4 | 2 | 1 |
| Parliamentary Affairs Department, Maharashtra | 1 | 0 | 0 | 0 | 0 |
| Vaidhmapan, Legal Metrology Department, Maharashtra | 8 | 0 | 2 | 1 | 1 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Office administration / housekeeping | Other / unclassified | Statutory rules / gazette notifications (G.S.R. / S.O.) | TOTAL |
|---|---|---|---|---|---|---|
| Shri.Chetan B. Nikam | Deputy Secretary | Home Department, Maharashtra | 1 | 1 | 1 | 3 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Home Department, Maharashtra

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping | **Shri.Chetan B. Nikam** — Deputy Secretary — chetan.nikam@nic.in (1) |
| Other / unclassified | **Shri.Chetan B. Nikam** — Deputy Secretary — chetan.nikam@nic.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri.Chetan B. Nikam** — Deputy Secretary — chetan.nikam@nic.in (1) |

### Principal Secretary, School Education and Sports Department, Mantralaya, Mumbai

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Secretary (Animal Husbandry, Dairy and Fisheries), Agriculture and Animal Husbandry, Dairy and Fisheries Department, Mantralaya, Mumbai.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Recruitment rules / RRs |  |

### Secretary, Environment and Climate Change Department, Mantralaya, Mumbai.

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Greater Mumbai Police, Maharashtra | Sachin Badhe | Deputy Commissioner of Police (1 | 2 |  |
| Labour Department, Maharashtra | G. NARAYANA RAJU | Secretary to the Govt. of India. | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.