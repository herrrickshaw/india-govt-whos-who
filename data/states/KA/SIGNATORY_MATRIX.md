# KA — who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-02 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (54 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 700 |
| PDFs fetched | 0 |
| PDFs with machine-readable text | 144 |
| PDFs with a detectable signature block | 144 |
| Signatures matched to a roster officer | 1 documents / 1 officers |
| Signatures not matched (person not in any roster, or moved) | 144 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| Agricultural Marketing Department, Karnataka | 20 | 0 | 2 | 0 | 0 |
| Agriculture Department, Karnataka | 15 | 0 | 1 | 0 | 0 |
| Agriculture Secretariat, Karnataka | 20 | 0 | 8 | 0 | 0 |
| Backward Classes Department, Karnataka | 20 | 0 | 1 | 0 | 0 |
| Bagalkote | 4 | 0 | 2 | 0 | 0 |
| Bangalore Metropolitan Transport Corporation (BMTC), Karnataka | 20 | 0 | 6 | 0 | 0 |
| Bengaluru Rural | 11 | 0 | 2 | 0 | 0 |
| Bengaluru South | 1 | 0 | 0 | 0 | 0 |
| Bidar | 1 | 0 | 0 | 0 | 0 |
| Chamarajanagar | 11 | 0 | 0 | 0 | 0 |
| Chamundeshwari Electricity Supply Corporation Limited Mysore, Karnataka | 20 | 0 | 1 | 0 | 0 |
| Chikkaballapura | 4 | 0 | 1 | 0 | 0 |
| Chikkamagaluru | 1 | 0 | 0 | 0 | 0 |
| Chitradurga | 8 | 0 | 0 | 0 | 0 |
| Commissionerate of Health & Family Welfare Service, Karnataka | 20 | 0 | 3 | 0 | 0 |
| Dakshina Kannada | 4 | 0 | 0 | 0 | 0 |
| Davanagere | 1 | 0 | 0 | 0 | 0 |
| Department of School Education & Literacy, Karnataka | 20 | 0 | 11 | 1 | 1 |
| Department of Technical Education | 20 | 0 | 1 | 0 | 0 |
| Directorates of Minorities, Karnataka | 20 | 0 | 5 | 0 | 0 |
| Drug Control Department, Karnataka | 20 | 0 | 10 | 0 | 0 |
| Ecology and Environment Department, Karnataka | 20 | 0 | 0 | 0 | 0 |
| Empowerment of Differently Abled and Senior Citizens Department, Karnataka | 20 | 0 | 6 | 0 | 0 |
| Energy Department, Karnataka | 17 | 0 | 6 | 0 | 0 |
| Handlooms and Textiles Department, Karnataka | 1 | 0 | 0 | 0 | 0 |
| Hassan | 2 | 0 | 1 | 0 | 0 |
| Haveri | 1 | 0 | 0 | 0 | 0 |
| Higher Education Department, Karnataka | 20 | 0 | 12 | 0 | 0 |
| Home Department, Karnataka | 20 | 0 | 11 | 0 | 0 |
| Industries and Commerce Department, Karnataka | 20 | 0 | 9 | 0 | 0 |
| International Institute of Information Technology Bangalore, Karnataka | 20 | 0 | 2 | 0 | 0 |
| Kalaburagi | 1 | 0 | 0 | 0 | 0 |
| Karnataka Housing Board, Karnataka | 20 | 0 | 2 | 0 | 0 |
| Karnataka Minorities Development Corporation Limited, Karnataka | 12 | 0 | 8 | 0 | 0 |
| Karnataka Power Transmission Corporation Limited, Karnataka | 20 | 0 | 9 | 0 | 0 |
| Karnataka Real Estate Regulatory Authority | 20 | 0 | 2 | 0 | 0 |
| Karnataka Rural Infrastructure Development Limited, Karnataka | 20 | 0 | 0 | 0 | 0 |
| Karnataka School Examination and Assessment Board, Karnataka | 20 | 0 | 7 | 0 | 0 |
| Karnataka State Diploma in Nursing Examination Board, Karnataka | 7 | 0 | 2 | 0 | 0 |
| Karnataka State Electronics Development Corporation Limited (KEONICS), Karnataka | 20 | 0 | 1 | 0 | 0 |
| Karnataka State Industrial and Infrastructure Development Corporation | 16 | 0 | 0 | 0 | 0 |
| Karnataka State Warehousing Corporation, Karnataka | 10 | 0 | 0 | 0 | 0 |
| Karnataka Veterinery, Animal and Fisheries Science University, Bidar, Karnataka | 2 | 0 | 0 | 0 | 0 |
| Kodagu | 2 | 0 | 0 | 0 | 0 |
| Kolar | 11 | 0 | 5 | 0 | 0 |
| Malnad College of Engineering, Hassan, Karnataka | 8 | 0 | 0 | 0 | 0 |
| Mandya | 1 | 0 | 0 | 0 | 0 |
| Mangalore Electricity Supply Company, Karnataka | 16 | 0 | 0 | 0 | 0 |
| Mangalore University, Konaje, Karnataka | 20 | 0 | 2 | 0 | 0 |
| National Law School of India University, Bengaluru,, Karnataka | 20 | 0 | 1 | 0 | 0 |
| Raichur | 1 | 0 | 1 | 0 | 0 |
| Rajiv Gandhi Housing Corporation Limited, Karnataka | 11 | 0 | 2 | 0 | 0 |
| Visveswaraiah Technological University, Belagaiv, Karnataka | 20 | 0 | 0 | 0 | 0 |
| e-Mapan, Legal Metrology Department, Karnataka | 20 | 0 | 1 | 0 | 0 |

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
| Higher Education Department, Karnataka | MAHESH R | Under Secretary to Government | 9 |  |
| Agriculture Secretariat, Karnataka | Prati | Director / Secretary | 5 |  |
| Bangalore Metropolitan Transport Corporation (BMTC), Karnataka | Public Relations | Officer | 5 |  |
| Drug Control Department, Karnataka | pratiyannu | Principal Secretary / Secretary | 5 |  |
| Karnataka Minorities Development Corporation Limited, Karnataka | Nagaraja | Under Secretary | 4 |  |
| Department of School Education & Literacy, Karnataka | Shubhamangala R.V | Under Secretary to Government (Planning | 3 |  |
| Drug Control Department, Karnataka | Karnataka Sarkara | Commissioner | 3 |  |
| Home Department, Karnataka | B.S. Nagarathnamma | Deputy Secretary to Government / Deputy Secretary to Government, | 3 |  |
| Karnataka School Examination and Assessment Board, Karnataka | Pratiyanu - | Commissioner / Principal Secretary | 3 |  |
| Directorates of Minorities, Karnataka | Prati Mahithigagi | Secretary | 2 |  |
| Empowerment of Differently Abled and Senior Citizens Department, Karnataka | -sahi- | Director / Under Secretary | 2 |  |
| Energy Department, Karnataka | SAMEER MADIMAN | Officer / Officer, | 2 |  |
| Higher Education Department, Karnataka | ivarage | Secretary | 2 |  |
| Home Department, Karnataka | G. Shyama Holla | Under Secretary to Government / Under Secretary to Government, | 2 |  |
| Home Department, Karnataka | T Krishnamurthy | Under Secretary to Government, | 2 |  |
| Industries and Commerce Department, Karnataka | ivarage | Commissioner / Director | 2 |  |
| Industries and Commerce Department, Karnataka | mattu avara hesarindalli | Under Secretary | 2 |  |
| Industries and Commerce Department, Karnataka | Prati Mahithigagi | Principal Secretary | 2 |  |
| Industries and Commerce Department, Karnataka | sevegalu mattu saman'haya | Director | 2 |  |
| Industries and Commerce Department, Karnataka | sevegalu mattu samanvaya | Commissioner | 2 |  |
| Karnataka Minorities Development Corporation Limited, Karnataka | mattu avara hesarindalli | Under Secretary | 2 |  |
| Karnataka Power Transmission Corporation Limited, Karnataka | Pratigalu Mahithigagi | Director / Principal Secretary | 2 |  |
| Karnataka State Diploma in Nursing Examination Board, Karnataka | Prati | Secretary | 2 |  |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.