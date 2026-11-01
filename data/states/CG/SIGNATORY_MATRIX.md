# CG — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (41 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 300 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 38 |
| PDFs with a detectable signature block | 38 |
| Signatures matched to a roster officer | 2 documents / 1 officers |
| Signatures not matched (person not in any roster, or moved) | 36 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agriculture Development and Farmer Welfare and Bio-Technology Department, Chhattisgarh | 10 | 0 | 0 | 0 | 0 |
| Balodabazar-Bhatapara | 3 | 0 | 0 | 0 | 0 |
| Balrampur-Ramanujganj | 2 | 0 | 0 | 0 | 0 |
| Bemetara | 9 | 0 | 1 | 0 | 0 |
| Bilaspur | 2 | 0 | 0 | 0 | 0 |
| Chhattisgarh Ayush Counselling | 9 | 0 | 0 | 0 | 0 |
| Chhattisgarh Biofuel Development Authority (CBDA) | 10 | 0 | 0 | 0 | 0 |
| Chhattisgarh Board Of Secondary Education, Raipur | 10 | 0 | 2 | 0 | 0 |
| Chhattisgarh Directorate of Employment and Training | 1 | 0 | 0 | 0 | 0 |
| Chhattisgarh Housing Board, Raipur | 10 | 0 | 1 | 0 | 0 |
| Chhattisgarh Medical Counselling | 10 | 0 | 1 | 0 | 0 |
| Chhattisgarh Public Relations Directorate | 10 | 0 | 1 | 0 | 0 |
| Chhattisgarh State Beverages Corporation | 3 | 0 | 0 | 0 | 0 |
| Chhattisgarh State Industrial Development Corporation Limited (CSIDC) | 10 | 0 | 0 | 0 | 0 |
| Chhattisgarh State Minor Forest Produce (Trading & Development) Co-Operative Fedration Limited, Chhattisgarh | 10 | 0 | 3 | 0 | 0 |
| Chhattisgarh State Power Generation Co. Ltd. | 10 | 0 | 0 | 0 | 0 |
| Chhattisgarh Swami Vivekananda Technical University (CSVTU) | 1 | 0 | 0 | 0 | 0 |
| Chhattishgarh State Warehousing Corporation (CGSWC) | 10 | 0 | 1 | 0 | 0 |
| Dakshin Bastar Dantewada | 7 | 0 | 1 | 0 | 0 |
| Dhamtari | 4 | 0 | 0 | 0 | 0 |
| Directorate of Economics & Statistics, Raipur, Chhattisgarh | 10 | 0 | 4 | 0 | 0 |
| Directorate of Food, Chhattisgarh | 10 | 0 | 0 | 0 | 0 |
| Directorate of Technical Education, Chhattisgarh | 2 | 0 | 0 | 0 | 0 |
| Directorate of Town and Country Planning, Chhattisgarh | 10 | 0 | 0 | 0 | 0 |
| Finance Department, Chhattisgarh | 10 | 0 | 2 | 0 | 0 |
| Food, Civil Supplies and Consumer Protection Department, Chhattisgarh | 10 | 0 | 1 | 0 | 0 |
| Forest and Climate Change Department, Chhattisgarh | 9 | 0 | 0 | 0 | 0 |
| Gariyaband | 7 | 0 | 0 | 0 | 0 |
| General Administration Department (GAD), Chhattisgarh | 10 | 0 | 1 | 0 | 0 |
| Government College Kotri, Chhattisgarh | 3 | 0 | 0 | 0 | 0 |
| Govt. Dudhadhari Bajrang Girls Postgraduate College,Raipur, Chhattisgarh | 10 | 0 | 0 | 0 | 0 |
| Labour Department, Chhattisgarh | 8 | 0 | 1 | 0 | 0 |
| Law and Legislative Affairs Department, Chhattisgarh | 10 | 0 | 4 | 0 | 0 |
| Panchayat and Rural Development Department, Chhattisgarh | 7 | 0 | 2 | 2 | 1 |
| Pandit Sundarlal Sharma (Open) University (PSSOU) Chhattisgarh, Bilaspur | 4 | 0 | 1 | 0 | 0 |
| Public Relations Department, Chhattisgarh | 1 | 0 | 0 | 0 | 0 |
| Public Works Department, Chhattisgarh | 2 | 0 | 1 | 0 | 0 |
| Revenue and Disaster Department, Chhattisgarh | 10 | 0 | 1 | 0 | 0 |
| Sant Gahira Guru Vishwavidyalaya, Surguja, Ambikapur, Chhattisgarh | 6 | 0 | 1 | 0 | 0 |
| State Load Despatch Centre (SLDC), Chhattisgarh | 10 | 0 | 3 | 0 | 0 |
| e-MaapVigyan, Chhattisgarh | 10 | 0 | 5 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry |  | TOTAL |
|---|---|---|---|

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Secretary, D/o Panchayat and Rural Development

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Directorate of Economics & Statistics, Raipur, Chhattisgarh | Kusum Ekka | Secretary / Under Secretary | 3 |  |
| Chhattisgarh State Minor Forest Produce (Trading & Development) Co-Operative Fedration Limited, Chhattisgarh | PRANAY MISHRA | Joint Secretary | 2 |  |
| e-MaapVigyan, Chhattisgarh | ANUPAM MISHRA | Addl. Secy / Jt. Secy | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.