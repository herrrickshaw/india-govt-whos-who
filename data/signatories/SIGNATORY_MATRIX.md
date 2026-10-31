# Who signed what — officers ↔ orders / notifications matrix

_Built 2026-11-01 by `scripts/signatory_matrix.py`. Scope: ministries with a who's-who roster in `data/ministry_officials.csv` (70 ministries/departments)._

## Funnel

| Stage | Count |
|---|---|
| Candidate order/notification/circular/OM/gazette PDFs in the document index | 24577 |
| PDFs fetched | 589 |
| PDFs with machine-readable text | 23841 |
| PDFs with a detectable signature block | 8224 |
| Signatures matched to a roster officer | 2305 documents / 387 officers |
| Signatures not matched (person not in any roster, or moved) | 6105 |

## Per ministry

| Ministry | candidates | fetched | signature found | matched docs | officers linked |
|---|---|---|---|---|---|
| AYUSH (MoA) | 4 | 0 | 0 | 0 | 0 |
| Civil Aviation (MoCA) | 5 | 0 | 2 | 0 | 0 |
| Coal | 4 | 0 | 3 | 2 | 2 |
| Cooperation | 30 | 0 | 0 | 0 | 0 |
| Culture | 11 | 0 | 0 | 0 | 0 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | 2797 | 0 | 911 | 130 | 42 |
| Department of Administrative Reforms and Public Grievances (DARPG) | 182 | 0 | 45 | 0 | 0 |
| Department of Agriculture and Farmers Welfare (DoAFW) | 2 | 0 | 0 | 0 | 0 |
| Department of Animal Husbandry and Dairying (DoAHD) | 649 | 0 | 251 | 96 | 20 |
| Department of Atomic Energy | 6 | 0 | 0 | 0 | 0 |
| Department of Chemicals and Petro-Chemicals (DoCP) | 4 | 0 | 1 | 0 | 0 |
| Department of Consumer Affairs (DoCA) | 150 | 0 | 93 | 60 | 6 |
| Department of Drinking Water and Sanitation (DDWS) | 2 | 0 | 0 | 0 | 0 |
| Department of Economic Affairs (DEA) | 12 | 0 | 1 | 0 | 0 |
| Department of Empowerment of Persons with Disabilities (DEPWD) | 4 | 0 | 1 | 0 | 0 |
| Department of Ex-Servicemen Welfare (DESW) | 8 | 0 | 2 | 0 | 0 |
| Department of Expenditure (DoE) | 2 | 0 | 0 | 0 | 0 |
| Department of Fertilizers (DoFz) | 4 | 0 | 0 | 0 | 0 |
| Department of Financial Services (DoFS) | 247 | 0 | 128 | 11 | 4 |
| Department of Fisheries (DoF) | 454 | 0 | 136 | 66 | 12 |
| Department of Health Research (DHR) | 136 | 0 | 33 | 1 | 1 |
| Department of Health and Family Welfare (DoHFW) | 1875 | 0 | 580 | 183 | 40 |
| Department of Higher Education (DoHE) | 652 | 0 | 107 | 5 | 5 |
| Department of Justice (DoJ) | 671 | 0 | 469 | 1 | 1 |
| Department of Land Resources (DLR) | 160 | 0 | 51 | 2 | 1 |
| Department of Legal Affairs (DoLA) | 1367 | 0 | 975 | 48 | 8 |
| Department of Pension & Pensioner's Welfare (DoPPW) | 14 | 0 | 8 | 2 | 2 |
| Department of Personnel and Training (DoPT) | 381 | 0 | 123 | 3 | 2 |
| Department of Pharmaceuticals (DoPs) | 91 | 0 | 28 | 0 | 0 |
| Department of Public Enterprises (DPE) | 432 | 0 | 113 | 10 | 8 |
| Department of Revenue (DoR) | 9 | 0 | 3 | 1 | 1 |
| Department of Rural Development (DoRD) | 28 | 0 | 2 | 0 | 0 |
| Department of School Education and Literacy (DSEL) | 299 | 0 | 72 | 3 | 3 |
| Department of Science and Technology (DST) | 334 | 0 | 61 | 13 | 10 |
| Department of Scientific and Industrial Research (DSIR) | 161 | 0 | 26 | 2 | 2 |
| Department of Social Justice and Empowerment (DoSJE) | 414 | 0 | 90 | 13 | 3 |
| Department of Space | 376 | 0 | 1 | 0 | 0 |
| Department of Sports (DoS) | 9 | 0 | 1 | 0 | 0 |
| Department of Telecommunications (DoT) | 5407 | 589 | 1633 | 811 | 75 |
| Development of North Eastern Region (MDONER) | 101 | 0 | 36 | 18 | 5 |
| Earth Sciences (MoES) | 272 | 0 | 48 | 4 | 3 |
| Electronics and Information Technology (MeitY) | 145 | 0 | 70 | 60 | 15 |
| Environment, Forest and Climate Change (MoEFCC) | 935 | 0 | 423 | 188 | 3 |
| External Affairs (MEA) | 228 | 0 | 32 | 4 | 4 |
| Food Processing Industries (MoFPI) | 2 | 0 | 0 | 0 | 0 |
| Heavy Industries (MoHI) | 41 | 0 | 11 | 9 | 2 |
| Home Affairs (MHA) | 5 | 0 | 0 | 0 | 0 |
| Housing and Urban Affairs (MoHUA) | 1131 | 0 | 241 | 89 | 24 |
| Information and Broadcasting (MIB) | 39 | 0 | 21 | 3 | 3 |
| Labour and Employment (MoLE) | 695 | 0 | 338 | 76 | 18 |
| Legislative Department (LD) | 391 | 0 | 58 | 6 | 2 |
| Micro, Small & Medium Enterprises (MSME) | 64 | 0 | 15 | 1 | 1 |
| Mines (MoM) | 242 | 0 | 153 | 99 | 7 |
| Minority Affairs (MoMA) | 21 | 0 | 5 | 2 | 2 |
| New and Renewable Energy (MNRE) | 638 | 0 | 161 | 88 | 21 |
| Parliamentary Affairs (MPA) | 147 | 0 | 64 | 12 | 2 |
| Petroleum and Natural Gas (MoPNG) | 1 | 0 | 0 | 0 | 0 |
| Planning (MoP) | 90 | 0 | 16 | 0 | 0 |
| Ports, Shipping and Waterways (MoPSW) | 174 | 0 | 23 | 9 | 4 |
| Power | 830 | 0 | 275 | 91 | 10 |
| Railways (MoR) | 1 | 0 | 0 | 0 | 0 |
| Road Transport and Highways (MoRTH) | 125 | 0 | 54 | 43 | 11 |
| Rural Development (MoRD) | 32 | 0 | 6 | 1 | 1 |
| Skill Development and Entrepreneurship (MSDE) | 20 | 0 | 4 | 1 | 1 |
| Statistics and Programme Implementation (MoSPI) | 77 | 0 | 16 | 0 | 0 |
| Steel (MoS) | 123 | 0 | 70 | 5 | 3 |
| Textiles (MoT) | 209 | 0 | 56 | 6 | 4 |
| Tourism | 376 | 0 | 75 | 26 | 12 |
| Tribal Affairs (MoTA) | 26 | 0 | 3 | 1 | 1 |
| Women and Child Development (MoWCD) | 3 | 0 | 0 | 0 | 0 |

## Officer × topic matrix (documents signed)

Full pivot: `officer_topic_pivot.csv`; long form with example titles and URLs: `officer_topic_matrix.csv`; one row per signed document: `officer_documents.csv`.

| Officer | Designation (roster) | Ministry | Acts / commencement / legislation | Advisory / public notice / caution | Budget / sanction / release of funds / grants | Committees / meetings / minutes / constitution of | Customs / tariff / duty / GST | HR: appointment / transfer / posting / promotion | HR: leave / pay / allowances / service rules | Legal metrology / consumer protection rules | Licensing / approvals / standards / enlistment | Office administration / housekeeping | Other / unclassified | Parliament / VIP references / reports | Procurement / tenders / GeM | RTI / appellate authority / CPIO | Recruitment rules / RRs | Scheme guidelines / implementation | Statutory rules / gazette notifications (G.S.R. / S.O.) | Training / capacity building / workshops | Vigilance / disciplinary / court matters | TOTAL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shri Bijender Singh | Under Secretary (STG-I & II) | Department of Telecommunications (DoT) |  | 1 |  |  |  | 193 | 15 |  | 11 | 1 | 41 |  | 3 |  |  | 3 |  |  | 1 | 269 |
| Shri Prem Prakash Maurya | Deputy Secretary | Earth Sciences (MoES) |  |  |  |  |  | 110 | 36 |  |  | 76 |  |  | 2 |  | 2 | 4 |  | 2 |  | 232 |
| Shri Devendra Kumar Rai | Joint Secretary (Telecom) | Department of Telecommunications (DoT) | 28 |  |  | 1 | 6 | 3 | 6 |  | 2 | 2 | 8 |  |  |  |  |  | 81 |  |  | 137 |
| Sh. Anupam Mishra | Additional Secretary | Department of Consumer Affairs (DoCA) | 6 |  |  |  |  | 7 | 2 | 30 | 1 |  |  |  |  |  | 4 |  | 39 |  |  | 89 |
| Shri R K Soni | DDG (AS) | Department of Telecommunications (DoT) |  |  |  |  | 34 | 2 | 13 |  | 30 | 1 |  |  |  |  |  | 4 |  |  |  | 84 |
| Shri Sunil Kumar | Under Secretary (STG-III, SNG, TFS) | Department of Telecommunications (DoT) |  |  |  | 1 | 1 | 55 |  |  | 2 | 2 | 11 |  |  |  |  | 7 |  | 2 |  | 81 |
| Shri Ghanshyam Prasad | Chairperson | Power | 5 | 2 |  |  | 9 | 4 | 7 |  |  |  | 5 |  | 12 | 1 |  | 8 | 22 |  |  | 75 |
| Dr. Veena Kumari Dermal | ADDITIONAL SECRETARY | Mines (MoM) | 15 |  | 1 |  | 10 |  |  |  |  | 1 | 3 |  |  |  |  | 1 | 37 |  |  | 68 |
| Shri Abhishek Pandey | DD(A), RML | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 29 |  |  |  |  |  |  |  |  | 29 |  |  |  |  | 58 |
| Shri Pankaj Kumar Sinha | Under Secretary (Admin l/Cash Section) | Department of Animal Husbandry and Dairying (DoAHD) |  |  |  |  | 1 | 25 | 8 |  | 4 | 4 | 10 |  |  |  | 1 | 1 | 1 |  | 1 | 56 |
| Shri Sher Singh Meena | Under Secretary | Department for Promotion of Industry and Internal Trade (DPIIT) |  |  | 24 |  | 8 | 1 | 9 |  |  |  |  |  | 1 |  |  | 7 |  |  |  | 50 |
| Shri R.K Gupta | Vice Chairperson | Cooperation |  |  |  |  | 8 | 1 | 4 |  | 9 |  | 9 |  | 1 | 1 |  | 8 | 8 |  |  | 49 |
| Shri Sanjay Gorelal Karndhar | Scientist E | New and Renewable Energy (MNRE) |  | 4 |  | 2 | 1 |  |  |  | 30 |  |  |  |  |  |  | 7 |  |  |  | 44 |
| Shri Vijay Kumar Sharma | Under Secretary | Department of Expenditure (DoE) |  |  |  |  |  | 20 |  |  |  |  | 1 |  |  |  |  |  |  |  | 21 | 42 |
| Ms. Jyoti Negi | Under Secretary (SEA) | Department of Telecommunications (DoT) |  |  |  |  |  | 29 | 4 |  |  |  | 1 |  | 1 |  |  | 3 |  | 2 | 1 | 41 |
| Harshvardhan Singh Khangarot | Director | Steel (MoS) |  |  |  |  | 1 | 27 |  |  | 5 |  |  |  |  |  |  |  |  |  |  | 33 |
| Mr. Naresh Pal Gangwar | Secretary(AHD) | Department of Animal Husbandry and Dairying (DoAHD) |  |  |  |  |  |  |  |  |  |  | 1 |  |  |  |  |  | 32 |  |  | 33 |
| Shri Ganesh Kumar | Under Secretary(Dental Education, Nursing Division) | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 17 |  |  |  |  | 2 |  |  |  | 14 |  |  |  |  | 33 |
| Shri Kham Khan Suan | Under Secretary (Gen. I & III Protocol/R&I) | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 10 |  |  |  | 12 |  |  |  |  | 10 |  |  |  |  | 32 |
| Shri Kulveer Singh Yadav | Joint Secretary | Mines (MoM) |  |  |  |  | 4 |  |  |  |  |  | 2 |  |  |  |  |  | 25 |  |  | 31 |
| Shri Mahmood Ahmed | Additional Secretary | Road Transport and Highways (MoRTH) | 2 | 2 |  |  | 1 |  | 1 |  | 1 | 1 | 2 |  |  |  |  | 1 | 18 |  |  | 29 |
| Mr Jagbir Singh Rana | Under Secretary | Department of Telecommunications (DoT) |  |  |  | 2 |  | 21 |  |  |  | 4 | 1 |  |  |  |  |  |  |  |  | 28 |
| Shri Rajiv Mani | Secretary | Department of Legal Affairs | 12 |  |  | 1 |  | 3 |  |  |  |  |  |  |  |  |  |  | 8 |  | 2 | 26 |
| Shri Ajit Kumar | Joint Secretary | Electronics and Information Technology (MeitY) | 1 | 3 |  |  |  | 4 | 4 |  |  |  | 3 |  |  | 1 |  | 2 | 7 |  |  | 25 |
| Shri Manash Kumar Roy | Under Secretary | Department for Promotion of Industry and Internal Trade (DPIIT) |  |  | 15 |  |  |  | 1 |  |  |  |  |  |  |  |  | 9 |  |  |  | 25 |
| Shri Manish Kumar | Under Secretary (Vigilance) | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 12 |  |  |  |  |  |  |  |  | 9 |  |  |  | 3 | 24 |
| Shri Vaibhav Jain | Director (AS-I) | Department of Telecommunications (DoT) |  |  |  |  | 19 | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 21 |
| Shri Rishikesh Vaishnav | Scientist C | New and Renewable Energy (MNRE) |  | 4 |  |  |  |  |  |  | 3 |  | 2 |  |  |  |  | 11 |  |  |  | 20 |
| Shri Surendra Singh | Under Secretary | Department for Promotion of Industry and Internal Trade (DPIIT) |  |  |  |  |  | 4 | 1 |  | 11 |  | 1 |  | 1 |  |  | 1 |  |  |  | 19 |
| Shri. Darminder Singh | Deputy Secretary | Department of Agriculture and Farmers Welfare (DoAFW) |  | 2 |  |  |  | 9 |  |  |  |  |  |  |  |  | 6 |  | 2 |  |  | 19 |
| Shri V. Srinivasa Rao | Director | Department of Fisheries (DoF) |  |  |  |  |  |  |  |  |  | 9 | 3 |  | 5 |  |  | 2 |  |  |  | 19 |
| Shri Lalit Kumar | Principal Private Secretary to Joint Secretary | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 2 |  |  |  | 9 |  |  |  | 7 |  | 1 |  |  |  | 19 |
| Shri Khagesh Garg | DDG(I&DP) | Department of Telecommunications (DoT) |  |  |  |  |  | 13 | 4 |  |  |  | 1 |  |  |  |  |  |  |  |  | 18 |
| Ms. Deepika Kachhal | Joint Secretary | Labour and Employment (MoLE) | 6 |  |  |  |  | 5 |  |  |  |  | 2 |  |  | 1 |  | 1 | 3 |  |  | 18 |
| Shri S. K. Gupta | Regional P. F. Commissioner (Gr.I) (Pension) | Labour and Employment (MoLE) |  |  | 1 |  |  | 16 |  |  |  | 1 |  |  |  |  |  |  |  |  |  | 18 |
| Dr. Tejaswi S. Naik | Joint Secretary | Labour and Employment (MoLE) | 11 | 1 |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |  | 3 |  |  | 17 |
| Shri Krishan Pal | Under Secretary (Admin-II, General Coordination) | Department of Fisheries (DoF) |  |  |  |  |  | 8 | 2 |  |  |  | 1 |  |  |  | 6 |  |  |  |  | 17 |
| Dr. Kiran Kumar Karlapu | Director (PMSSY) | Department of Health and Family Welfare (DoHFW) |  |  |  |  |  | 7 |  |  |  |  |  |  |  |  | 9 |  |  |  |  | 16 |
| Shri Anil Kumar | Private Secretary | Housing and Urban Affairs (MoHUA) |  |  |  |  |  | 3 |  |  |  |  | 2 | 4 | 4 |  | 3 |  |  |  |  | 16 |
| Shri Awadhesh Kumar Singh | Director (Elect.) | Department of Telecommunications (DoT) |  |  |  |  |  | 8 | 2 |  |  | 1 | 4 |  |  |  |  |  | 1 |  |  | 16 |

## Contact person by topic

For each ministry and topic, the roster officers who signed the most documents on it (name, roster designation, email).

### Additional Chief Secretary to the Govt. of Assam, Revenue & DM Department and Additional Chief Secretary to the Govt. of Assam, Department of Tribal Affairs (Plain) and CEO, ASDMA (addl)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Recruitment rules / RRs |  |

### Additional Secretary to Govt. of India, Department of School Education and Literacy, Ministry of Education, New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Additional Secretary, Government of India, M/o Mines, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Additional Secretary, M/o Power, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Customs / tariff / duty / GST |  |
| HR: appointment / transfer / posting / promotion |  |
| HR: leave / pay / allowances / service rules |  |
| Licensing / approvals / standards / enlistment |  |
| Other / unclassified |  |
| Procurement / tenders / GeM |  |
| RTI / appellate authority / CPIO |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Additional Secretary, M/o Women and Child Development, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### CVO, AAI.M/o Civil Aviation

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |

### Coal

| Topic | Contact officers (docs signed) |
|---|---|
| Licensing / approvals / standards / enlistment | **Shri Himanshu Bhushan** — Deputy Coal Controller — himanshu.cco@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Himanshu Bhushan** — Deputy Coal Controller — himanshu.cco@gov.in (1); **Smt. Rupinder Brar** — Add. Secretary — rup.brar@nic.in (1) |

### Commerce and Industry (MoCI)

| Topic | Contact officers (docs signed) |
|---|---|
| Budget / sanction / release of funds / grants | **Hemant Kumar** — Deputy DGFT — hkzero.7@gov.in (1); **R Kumar** — Assistant DGFT — r.kumar68@nic.in (1) |
| HR: leave / pay / allowances / service rules | **Praveen Kumar** — Joint DGFT — praveen.kumar82@nic.in (1) |
| Other / unclassified | **R Kumar** — Assistant DGFT — r.kumar68@nic.in (1) |
| Scheme guidelines / implementation | **Hemant Kumar** — Deputy DGFT — hkzero.7@gov.in (1) |

### Cooperation

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (8) |
| HR: appointment / transfer / posting / promotion | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (4) |
| Licensing / approvals / standards / enlistment | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (9) |
| Other / unclassified | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (9) |
| Procurement / tenders / GeM | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (1) |
| RTI / appellate authority / CPIO | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (1) |
| Scheme guidelines / implementation | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (8) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri R.K Gupta** — Vice Chairperson — vc-cea@crcs.gov.in (8) |

### Department for Promotion of Industry and Internal Trade (DPIIT)

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution | **Shri Prashant Kumar** — Director — dirpmgs.dpiit@gov.in (1); **Shri Sanjay Kumar** — Under Secretary — sanjay-css@gov.in (1) |
| Budget / sanction / release of funds / grants | **Shri Sher Singh Meena** — Under Secretary — sher.meena@nic.in (24); **Shri Manash Kumar Roy** — Under Secretary — manash.roy@nic.in (15); **Shri Abhishek Dutt** — Under Secretary — dutt.abhishek@nic.in (6); **Shri Bikram Nath** — Joint Director — bikram.87@nic.in (6) |
| Committees / meetings / minutes / constitution of | **Dr. Ashish Kumar** — Senior Consultant — krashish@nic.in (1); **Shri Arvind Kumar** — Under Secretary — arvind.kumar198@nic.in (1); **Smt. Gurdeep Anand** — PPS — gurdeep.anand@nic.in (1); **Smt. Niharika Khatana** — Assistant Director — niharika.khatana@gov.in (1) |
| Customs / tariff / duty / GST | **Shri Sher Singh Meena** — Under Secretary — sher.meena@nic.in (8); **Shri Pritam Kumar** — Under Secretary — pritam.k@gov.in (1); **Shri Ravi Ranjan** — Under Secretary — rvranjan.edu@nic.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Surendra Singh** — Under Secretary — ssingh.dopt@nic.in (4); **Shri Sushil Kumar** — Deputy Secretary — sushil.dusyant@nic.in (4); **Shri Pritam Kumar** — Under Secretary — pritam.k@gov.in (2); **Shri Dheeraj Kumar Meena** — Under Secretary — dheeraj.meena17@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Sher Singh Meena** — Under Secretary — sher.meena@nic.in (9); **Shri Abhishek Dutt** — Under Secretary — dutt.abhishek@nic.in (3); **Shri Manash Kumar Roy** — Under Secretary — manash.roy@nic.in (1); **Shri Surendra Singh** — Under Secretary — ssingh.dopt@nic.in (1) |
| Licensing / approvals / standards / enlistment | **Shri Surendra Singh** — Under Secretary — ssingh.dopt@nic.in (11); **Smt. Himani Pande** — Additional Secretary — ashp.dpiit@gov.in (4); **Shri Dheeraj Kumar Meena** — Under Secretary — dheeraj.meena17@gov.in (1); **Shri Sushil Kumar** — Deputy Secretary — sushil.dusyant@nic.in (1) |
| Office administration / housekeeping | **Shri Binod Kumar** — Deputy Secretary — binod.kumar52@nic.in (1); **Shri Neelesh Mishra** — Senior Principal Private Secretary — neelesh.mishra65@gov.in (1); **Shri Subhash Chand** — Economic Officer — npcqci-dipp@nic.in (1) |
| Other / unclassified | **Dr. Jai Prakash Shivahare** — Joint Secretary — js-jps@gov.in (4); **Ms. Nidhi Kesarwani** — Joint Secretary — jointsecy-nk@gov.in (3); **Shri Sandeep S Kumbhar** — Technical Adviser (Boiler) & Secretary, Central Boilers Board (CBB) — sandeep.kumbhar7@gov.in (2); **Shri Arun Kumar Gupta** — Under Secretary (IPR-I Estt. (IPAB)) — ak.gupta38@nic.in (1) |
| Procurement / tenders / GeM | **Shri Sushil Kumar** — Deputy Secretary — sushil.dusyant@nic.in (8); **Shri Arvind Kumar** — Under Secretary — arvind.kumar198@nic.in (1); **Shri Jitender Juyal** — Deputy Secretary — jitender.juyal@nic.in (1); **Shri Prashant Kumar** — Director — dirpmgs.dpiit@gov.in (1) |
| Scheme guidelines / implementation | **Shri Manash Kumar Roy** — Under Secretary — manash.roy@nic.in (9); **Shri Sher Singh Meena** — Under Secretary — sher.meena@nic.in (7); **Shri Bikram Nath** — Joint Director — bikram.87@nic.in (6); **Shri Abhishek Dutt** — Under Secretary — dutt.abhishek@nic.in (3) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Smt. Himani Pande** — Additional Secretary — ashp.dpiit@gov.in (6); **Dr. Jai Prakash Shivahare** — Joint Secretary — js-jps@gov.in (1); **Ms. Gurneet Tej** — Joint Secretary — jsdpiit-gt@gov.in (1); **Shri Ateesh Kumar Singh** — Additional Secretary — as-aks@gov.in (1) |
| Vigilance / disciplinary / court matters | **Dr. Ashish Kumar** — Senior Consultant — krashish@nic.in (1); **Smt. Gurdeep Anand** — PPS — gurdeep.anand@nic.in (1) |

### Department of Agriculture and Farmers Welfare (DoAFW)

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution | **Shri. Darminder Singh** — Deputy Secretary — s.darminder@nic.in (2) |
| HR: appointment / transfer / posting / promotion | **Shri. Darminder Singh** — Deputy Secretary — s.darminder@nic.in (9); **Shri Narender Kumar** — Deputy Commissioner (Superannuation) — narender.63@gov.in (1); **Shri. Anil Kumar Singh** — Section Officer National Bee Board — anilkumar.singh35@gov.in (1) |
| Other / unclassified | **Shri. Sunil Kumar** — Principal Private Secretary — aksahu@ias.nic.in (1) |
| Procurement / tenders / GeM | **Shri Parveen Kumar** — Under Secretary (Oilseeds) — praveen.kumar67@nic.in (1) |
| RTI / appellate authority / CPIO | **Manoj Kumar Singh** — Director (Costing Cell) — manoj..singh75@nic.in (1); **Shri Narender Kumar** — Deputy Commissioner (Superannuation) — narender.63@gov.in (1) |
| Recruitment rules / RRs | **Shri. Darminder Singh** — Deputy Secretary — s.darminder@nic.in (6) |
| Scheme guidelines / implementation | **Shri Chandan Kumar** — Under Secretary (Digital Agriculture) — us-it@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri. Darminder Singh** — Deputy Secretary — s.darminder@nic.in (2); **Manoj Kumar Singh** — Director (Costing Cell) — manoj..singh75@nic.in (1); **Shri. Anil Kumar Singh** — Section Officer National Bee Board — anilkumar.singh35@gov.in (1) |
| Vigilance / disciplinary / court matters | **Manoj Kumar Singh** — Director (Costing Cell) — manoj..singh75@nic.in (1) |

### Department of Animal Husbandry and Dairying (DoAHD)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Dr. Muthukumarasamy B.** — Joint Secretary (NLM/SD) — js-nlm@dahd.nic.in (1); **Shri Rama Shankar Sinha** — Additional Secretary (LH) — jslh-dadf@nic.in (1) |
| Advisory / public notice / caution | **Dr. Gagan Garg** — Joint Commissioner (RGM) — gagan.garg@nic.in (1); **Dr. Naveena. B.Maheswarappa** — Animal Husbandry Commissioner — ahc-dahd@nic.in (1) |
| Budget / sanction / release of funds / grants | **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (1); **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (1) |
| Committees / meetings / minutes / constitution of | **Dr. Muthukumarasamy B.** — Joint Secretary (NLM/SD) — js-nlm@dahd.nic.in (2); **Shri Bhuwan Chandra Mishra** — HOD & Sr. Director (IT) — bcmishra@nic.in (1) |
| Customs / tariff / duty / GST | **Shri Ajith Kumar K** — Deputy Commissioner (DD) — ajith.kk@gov.in (1); **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (25); **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (7); **Shri Rama Shankar Sinha** — Additional Secretary (LH) — jslh-dadf@nic.in (5); **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (3) |
| HR: leave / pay / allowances / service rules | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (8); **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (2); **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (2); **Shri Sanjib Bhattacharya** — Deputy Secretary (Admin l/ Admin ll/Cash Section) — sanjeeb.b@nic.in (1) |
| Licensing / approvals / standards / enlistment | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (4); **Dr. Gagan Garg** — Joint Commissioner (RGM) — gagan.garg@nic.in (2); **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (1) |
| Office administration / housekeeping | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (4); **Dr. Naveena. B.Maheswarappa** — Animal Husbandry Commissioner — ahc-dahd@nic.in (1); **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (1) |
| Other / unclassified | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (10); **Dr. Muthukumarasamy B.** — Joint Secretary (NLM/SD) — js-nlm@dahd.nic.in (2); **Shri Vikas Kumar Vikrosy** — Under Secretary (General & AQCS) — vk.vikrosy@gov.in (2); **Dr. Gagan Garg** — Joint Commissioner (RGM) — gagan.garg@nic.in (1) |
| Procurement / tenders / GeM | **Dr. Sujit K. Dutta** — Joint Commissioner (NLM) — sk.dutta@nic.in (4); **Shri C. Sen** — Joint Commissioner/GM (DMS) — chinmoyjit.sen@gov.in (2) |
| RTI / appellate authority / CPIO | **Shri S. Kamal Garg** — Under Secretary (GC/PC) — gargsk.edu@nic.in (3); **Shri Victor Bilung** — Under Secretary (Parl./Legal) — victor.bilung38@nic.in (3) |
| Recruitment rules / RRs | **Shri Rama Shankar Sinha** — Additional Secretary (LH) — jslh-dadf@nic.in (5); **Shri Sanjay Kumar** — Under Secretary (C&DD) — sanjay.kmr70@nic.in (2); **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (1); **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (1) |
| Scheme guidelines / implementation | **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Mr. Naresh Pal Gangwar** — Secretary(AHD) — secyahd@nic.in (32); **Dr. Muthukumarasamy B.** — Joint Secretary (NLM/SD) — js-nlm@dahd.nic.in (5); **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (2); **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (1) |
| Training / capacity building / workshops | **Smt. Anamika Nigam** — Under Secretary (NLM) — anamika.edu@nic.in (1) |
| Vigilance / disciplinary / court matters | **Dr. Gagan Garg** — Joint Commissioner (RGM) — gagan.garg@nic.in (1); **Shri Pankaj Kumar Sinha** — Under Secretary (Admin l/Cash Section) — pk.sinha88@gov.in (1) |

### Department of Consumer Affairs (DoCA)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (6); **Smt. Nidhi Khare** — Secretary (CA) — Secy-ca@nic.in (2) |
| Advisory / public notice / caution | **Sh. Ashutosh Agarwal** — Director (Legal Metrology) — ashutosh.agarwal13@nic.in, dirwm-ca@nic.in (2) |
| HR: appointment / transfer / posting / promotion | **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (7); **Shri Mukesh Kumar** — Section officer (BIS) — sobis-ca@nic.in (6) |
| HR: leave / pay / allowances / service rules | **Sh. Amit Kumar** — Under Secretary (P&C/O&M/ RTI/ E-GOV) — uspc-ca@gov.in (2); **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (2) |
| Legal metrology / consumer protection rules | **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (30); **Smt. Nidhi Khare** — Secretary (CA) — Secy-ca@nic.in (6); **Sh. Ashutosh Agarwal** — Director (Legal Metrology) — ashutosh.agarwal13@nic.in, dirwm-ca@nic.in (1) |
| Licensing / approvals / standards / enlistment | **Sh. Amit Kumar** — Under Secretary (P&C/O&M/ RTI/ E-GOV) — uspc-ca@gov.in (2); **Sh. Baldev Singh** — Under Secretary (BIS) — usbis-ca@gov.in (2); **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (1) |
| Office administration / housekeeping | **Sh. Ashutosh Agarwal** — Director (Legal Metrology) — ashutosh.agarwal13@nic.in, dirwm-ca@nic.in (1) |
| Procurement / tenders / GeM | **Shri Mukesh Kumar** — Section officer (BIS) — sobis-ca@nic.in (2); **Sh. Bal Krishna Thakur** — Under Secretary (Establishment and General Administration) — usestt-ca@nic.in (1); **Sh. Baldev Singh** — Under Secretary (BIS) — usbis-ca@gov.in (1) |
| Recruitment rules / RRs | **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (4) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Sh. Anupam Mishra** — Additional Secretary — as-ca1@gov.in (39); **Smt. Nidhi Khare** — Secretary (CA) — Secy-ca@nic.in (6); **Sh. Ashutosh Agarwal** — Director (Legal Metrology) — ashutosh.agarwal13@nic.in, dirwm-ca@nic.in (2) |

### Department of Expenditure (DoE)

| Topic | Contact officers (docs signed) |
|---|---|
| Budget / sanction / release of funds / grants | **Shri Prateek Kumar Singh** — Director — prateeks.98@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Vijay Kumar Sharma** — Under Secretary — vkumar.sharma@nic.in (20) |
| HR: leave / pay / allowances / service rules | **Shri Manoj Kumar Jain** — Under Secretary — mk.jain05@nic.in (2); **Shri Samir Kumar Das** — Deputy Secretary — samir.kumar70@nic.in (2) |
| Other / unclassified | **Shri Vijay Kumar Sharma** — Under Secretary — vkumar.sharma@nic.in (1) |
| Scheme guidelines / implementation | **Shri Prateek Kumar Singh** — Director — prateeks.98@gov.in (1) |
| Vigilance / disciplinary / court matters | **Shri Vijay Kumar Sharma** — Under Secretary — vkumar.sharma@nic.in (21) |

### Department of Fertilizers (DoFz)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Pradeep Kumar Singh** — Under Secretary (CPIO) — pk.singh34@gov.in (1) |

### Department of Fisheries (DoF)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Dr. Ansy Mathew N.P.** — Assistant Commissioner (Fisheries) — ansy.mathew@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Subhash Chandra** — Director- Fisheries (IT & e-Governance Cell, Cyber Security & IT Infrastructure Unit, Media & Outreach, Data Protection Officer (DPO)) — it-director@dof.gov.in; [{'email':'soc.media-fy@dof.gov.in'}] (1) |
| HR: appointment / transfer / posting / promotion | **Shri Krishan Pal** — Under Secretary (Admin-II, General Coordination) — krishan.p13@nic.in (8); **Shri Umesh Shankar Prasad** — Under Secretary (Parliament, Training, RTI/PGMS, R&I & Cash) — us.prasad82@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Krishan Pal** — Under Secretary (Admin-II, General Coordination) — krishan.p13@nic.in (2) |
| Office administration / housekeeping | **Shri V. Srinivasa Rao** — Director — srveeragandham@ord.gov.in (9); **Dr. Sanjay Pandey** — Deputy Commissioner (Fisheries) — sanjay.rpandey@gov.in (1); **Dr. Tarun Kumar Singh** — Assistant Commissioner (Fisheries) — tarunkr.singh@gov.in (1); **Shri Rakesh Kumar** — Deputy Commissioner (Fisheries) — rakesh.kr38@gov.in (1) |
| Other / unclassified | **Shri V. Srinivasa Rao** — Director — srveeragandham@ord.gov.in (3); **Dr. Sanjay Pandey** — Deputy Commissioner (Fisheries) — sanjay.rpandey@gov.in (1); **Shri Krishan Pal** — Under Secretary (Admin-II, General Coordination) — krishan.p13@nic.in (1) |
| Procurement / tenders / GeM | **Shri V. Srinivasa Rao** — Director — srveeragandham@ord.gov.in (5); **Dr. Tarun Kumar Singh** — Assistant Commissioner (Fisheries) — tarunkr.singh@gov.in (1) |
| RTI / appellate authority / CPIO | **Dr. Ansy Mathew N.P.** — Assistant Commissioner (Fisheries) — ansy.mathew@gov.in (1); **Shri Pumzalal Pulamte** — Deputy Secretary(Training, General Coordination, RTI) — p.pulamte@nic.in (1) |
| Recruitment rules / RRs | **Shri Krishan Pal** — Under Secretary (Admin-II, General Coordination) — krishan.p13@nic.in (6); **Shri Umesh Shankar Prasad** — Under Secretary (Parliament, Training, RTI/PGMS, R&I & Cash) — us.prasad82@gov.in (4); **Shri Anil Singh Bhandari** — Under Secretary (Admin. I, V & Vigilance) — bhandari.anil@nic.in (1) |
| Scheme guidelines / implementation | **Shri V. Srinivasa Rao** — Director — srveeragandham@ord.gov.in (2); **Shri Subhash Chandra** — Director- Fisheries (IT & e-Governance Cell, Cyber Security & IT Infrastructure Unit, Media & Outreach, Data Protection Officer (DPO)) — it-director@dof.gov.in; [{'email':'soc.media-fy@dof.gov.in'}] (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Dr. Sanjay Pandey** — Deputy Commissioner (Fisheries) — sanjay.rpandey@gov.in (1) |

### Department of Food and Public Distribution (DFPD)

| Topic | Contact officers (docs signed) |
|---|---|
| RTI / appellate authority / CPIO |  |

### Department of Health and Family Welfare (DoHFW)

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution | **Shri Manoj Kumar Jha** — Section Officer(PMSSY - IV) — manoj@ndma.gov.in (3); **Shri Sukh lal Meena** — Director (Public Health, Vaccine Institute) — meena.sukh@nic.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Om Prakash** — Under Secretary(FP-I/RCH-CDN) — prakash.om26@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Abhishek Pandey** — DD(A), RML — abhishek.pandey86@gov.in (29); **Shri Ganesh Kumar** — Under Secretary(Dental Education, Nursing Division) — kumar.g@nic.in (17); **Shri Manish Kumar** — Under Secretary (Vigilance) — manishkumar.edu@nic.in (12); **Shri Kham Khan Suan** — Under Secretary (Gen. I & III Protocol/R&I) — kk.suan29@gov.in (10) |
| HR: leave / pay / allowances / service rules | **Shri Vijay Kumar** — SO (NCD-II) — ncd2mohfw@gmail.com; [{'email':'v.kumar85@nic.in'}] (2); **Shri Anurag Tewari** — Under Secretary (Hospital – II & Hospital – III Division) — anurag.tiwari86@gov.in (1); **Shri Manoj Kumar Jha** — Section Officer(PMSSY - IV) — manoj@ndma.gov.in (1) |
| Office administration / housekeeping | **Shri Kham Khan Suan** — Under Secretary (Gen. I & III Protocol/R&I) — kk.suan29@gov.in (12); **Shri Lalit Kumar** — Principal Private Secretary to Joint Secretary — jstraining-mohfw@gov.in (9) |
| Other / unclassified | **Ms. Aradhana Patnaik** — Additional Secretary and Mission Director (National Health Mission) and Director General (National Tuberculosis Elimination Programme) — asmd-mohfw@nic.in (4); **Shri Manoj Kumar Jha** — Section Officer(PMSSY - IV) — manoj@ndma.gov.in (3); **Shri Anurag Tewari** — Under Secretary (Hospital – II & Hospital – III Division) — anurag.tiwari86@gov.in (2); **Shri Ganesh Kumar** — Under Secretary(Dental Education, Nursing Division) — kumar.g@nic.in (2) |
| Procurement / tenders / GeM | **Shri R. K. Katiyar** — Additional Private Secretary to the Minister of State — mosap-mohfw@gov.in (1) |
| RTI / appellate authority / CPIO | **Shri Lalit Kumar** — Principal Private Secretary to Joint Secretary — jstraining-mohfw@gov.in (7); **Shri Dharm Bir Kumar Singh** — Under Secretary (PMSSY-V) — dharmbk.singh@nic.in (1); **Shri Nikhil Bhatnagar** — Under Secretary (CHS V & VI) — nikhil.bhatnagar@gov.in (1); **Shri Vijay Kumar** — SO (NCD-II) — ncd2mohfw@gmail.com; [{'email':'v.kumar85@nic.in'}] (1) |
| Recruitment rules / RRs | **Shri Abhishek Pandey** — DD(A), RML — abhishek.pandey86@gov.in (29); **Shri Ganesh Kumar** — Under Secretary(Dental Education, Nursing Division) — kumar.g@nic.in (14); **Shri Kham Khan Suan** — Under Secretary (Gen. I & III Protocol/R&I) — kk.suan29@gov.in (10); **Dr. Kiran Kumar Karlapu** — Director (PMSSY) — kiran.karlapu@gov.in (9) |
| Scheme guidelines / implementation | **Shri Lalit Kumar** — Principal Private Secretary to Joint Secretary — jstraining-mohfw@gov.in (1); **Shri Nikhil Bhatnagar** — Under Secretary (CHS V & VI) — nikhil.bhatnagar@gov.in (1); **Shri Ravinder Kumar** — SSO (Family Planning – II) — dhruva.rajyadav@nic.in (1); **Shri Vijay Kumar** — SO (NCD-II) — ncd2mohfw@gmail.com; [{'email':'v.kumar85@nic.in'}] (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Rakesh Kumar** — Director (Training Division, viz. Skill Development, Training, Mission Karmayogi, NIHFW, NIPHTR, Mumbai Gandhigram Institute of Rural Health and Family, General Administration ) — rk.singh67@nic.in (8); **Ms. Hemlata Singh** — Under Secretary(NCD-I) — hemlata.singh82@gov.in (5); **Ms. Sarita Nair** — DS (NCD - II, NPCDCS - All components excluding NHM Component) — sarita.nair@gov.in (1); **Shri Guite Elsy Thang Biak Lun** — Under Secretary(Coordination & Addl. Charge NUHM) — g.thangbiaklun15@nic.in (1) |
| Training / capacity building / workshops | **Shri D. Ramesh Babu** — Under Secretary (IC / IH and Addl. Charge G20 Secretariat) — dramesh.babu@nic.in (2) |
| Vigilance / disciplinary / court matters | **Shri Manish Kumar** — Under Secretary (Vigilance) — manishkumar.edu@nic.in (3) |

### Department of Land Resources (DLR)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Shri Sami Ahmad Khan** — Deputy Secretary — sa.khan15@gov.in (1) |
| Other / unclassified | **Shri Girnish Kumar** — Under Secretary — girnish.kumar@nic.in (2) |

### Department of Legal Affairs

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Rajiv Mani** — Secretary — secylaw-dla@nic.in (12); **Shri Arjun Ram Meghwal** — Minister of State (Independent Charge) — mljoffice@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Rajiv Mani** — Secretary — secylaw-dla@nic.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Rajiv Mani** — Secretary — secylaw-dla@nic.in (3) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Rajiv Mani** — Secretary — secylaw-dla@nic.in (8) |
| Vigilance / disciplinary / court matters | **Shri Rajiv Mani** — Secretary — secylaw-dla@nic.in (2) |

### Department of Public Enterprises (DPE)

| Topic | Contact officers (docs signed) |
|---|---|
| Budget / sanction / release of funds / grants | **Shri Kailash Bhandari** — Joint Director (Policy Division and C.S.R) — kailash.bhandari@nic.in (2); **Ms. Kranti E. Khobragade** — Director (Policy Division & HoD) — kranti.khobragade@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Ms. P. Songlianvung** — Under Secretary (Budget, Parliament, Coordination & IT Cell) — p.songlianvung12@nic.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Prafull Kumar Sinha** — Deputy Secretary (General Management and Capacity Building) — pk.sinha1966@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Dr. Sumantra Pal** — Economic Adviser (General Management and Capacity Building) — sumantra.pal@nic.in (1); **Shri Prafull Kumar Sinha** — Deputy Secretary (General Management and Capacity Building) — pk.sinha1966@gov.in (1) |
| Office administration / housekeeping | **Ms. Kranti E. Khobragade** — Director (Policy Division & HoD) — kranti.khobragade@gov.in (1); **Shri Kailash Bhandari** — Joint Director (Policy Division and C.S.R) — kailash.bhandari@nic.in (1) |
| Other / unclassified | **Shri Arun Kumar Sharma** — PPS to JS (Admn. & Coord.) — ak.sharma74@nic.in (1) |
| Scheme guidelines / implementation | **Dr. Sumantra Pal** — Economic Adviser (General Management and Capacity Building) — sumantra.pal@nic.in (1); **Shri Kailash Bhandari** — Joint Director (Policy Division and C.S.R) — kailash.bhandari@nic.in (1); **Shri Nitin Kumar** — Under Secretary (Administration, Establishment, Cash, Vigilance, Library) — nitin.kumar57@nic.in;[{'email':'us-admn-dpe@gov.in'}] (1); **Shri Prafull Kumar Sinha** — Deputy Secretary (General Management and Capacity Building) — pk.sinha1966@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Sh. Lucas L Kamsuan** — Joint Secretary (Admn. and Coord.) — js.admn-dpe@gov.in (3) |

### Department of Revenue (DoR)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Nimit Dhalia** — Assistant Director — nimit.dhalia2057@gov.in (1) |

### Department of Science and Technology (DST)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Ms. A. Dhanalakshmi** — Joint Secretary — a.dhanlakshmi@nic.in (1); **Shri Atin Singh Yadav** — Under Secretary — as.yadav78@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Dr. Charu Agarwal** — Scientist D — c.agarwal@gov.in (1) |
| Other / unclassified | **Dr Akhilesh Mishra** — Scientist ‘F’ — akhilesh.mishra@nic.in (1); **Dr Vandana Singh** — Scientist - F and Head — vandana.singh@nic.in (1); **Dr. Mrs Anita Aggarwal** — Scientist G & Head — anita.a@nic.in (1) |
| Recruitment rules / RRs | **Ms. A. Dhanalakshmi** — Joint Secretary — a.dhanlakshmi@nic.in (1) |
| Scheme guidelines / implementation | **Ms. A. Dhanalakshmi** — Joint Secretary — a.dhanlakshmi@nic.in (2); **Shri Atin Singh Yadav** — Under Secretary — as.yadav78@gov.in (2); **Dr Nisha Mendiratta** — Head — nisha67@nic.in (1); **Dr Vandana Singh** — Scientist - F and Head — vandana.singh@nic.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Ms. A. Dhanalakshmi** — Joint Secretary — a.dhanlakshmi@nic.in (2) |

### Department of Scientific and Industrial Research (DSIR)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Shri Surinder Pal Singh** — Joint Secretary — surinder.singh66@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Mahendra Kumar Gupta** — Joint Secretary — jsa-dsir@nic.in (1) |

### Department of Telecommunications (DoT)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (28); **Shri Venkata Praveen Pogiri** — Director (SEA&TF) — director.sea-dot@gov.in (1) |
| Advisory / public notice / caution | **Ms. Urvashi Sangwan** — Director (PHP) — urvashi.sangwan@nic.in (2); **Shankara Nand Mishra** — Director (LFA-III) — div.lfa3-dot@gov.in (1); **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (1); **Shri Devender Singh Rawat** — AWA (T) — awat.wpc-dot@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Ms. Urvashi Sangwan** — Director (PHP) — urvashi.sangwan@nic.in (3); **Mr Jagbir Singh Rana** — Under Secretary — jagbirsingh-upsc@gov.in (2); **Shri Devender Singh Rawat** — AWA (T) — awat.wpc-dot@gov.in (2); **Shri Sanjeev Kumar Balyan** — Director — dirtrg2-dot@gov.in (2) |
| Customs / tariff / duty / GST | **Shri R K Soni** — DDG (AS) — ddgas-dot@nic.in (34); **Shri Vaibhav Jain** — Director (AS-I) — dir.as-dot@gov.in (19); **Shri Prashant Verma** — Director (LPU) — diras2-dot@nic.in (7); **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (6) |
| HR: appointment / transfer / posting / promotion | **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (193); **Shri Sunil Kumar** — Under Secretary (STG-III, SNG, TFS) — usstg3-dot@gov.in (55); **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (29); **Mr Jagbir Singh Rana** — Under Secretary — jagbirsingh-upsc@gov.in (21) |
| HR: leave / pay / allowances / service rules | **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (15); **Shri R K Soni** — DDG (AS) — ddgas-dot@nic.in (13); **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (6); **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (4) |
| Licensing / approvals / standards / enlistment | **Shri R K Soni** — DDG (AS) — ddgas-dot@nic.in (30); **Shri Shashi Kumar** — Director (DS-II) — dirds2-dot@nic.in (12); **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (11); **Shri Ashok Kumar** — DDG (S.R.I.) — ddg.sri-dot@gov.in (5) |
| Office administration / housekeeping | **Mr Jagbir Singh Rana** — Under Secretary — jagbirsingh-upsc@gov.in (4); **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (2); **Shri Sh. Ashutosh Diwakar** — ADG (ABP Implementation -II & III) — adgabp2.dbn-dot@gov.in (2); **Shri Sunil Kumar** — Under Secretary (STG-III, SNG, TFS) — usstg3-dot@gov.in (2) |
| Other / unclassified | **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (41); **Shri Sunil Kumar** — Under Secretary (STG-III, SNG, TFS) — usstg3-dot@gov.in (11); **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (8); **Shri Venkata Praveen Pogiri** — Director (SEA&TF) — director.sea-dot@gov.in (6) |
| Procurement / tenders / GeM | **Shri Ashok Kumar Jain** — DDG (IP) — ddgic-dot@nic.in (4); **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (3); **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (1); **Shri PSM Tripathi** — Senior Deputy WA (IMT) — srdwaimt.wpc-dot@gov.in (1) |
| RTI / appellate authority / CPIO | **Shri Sudhir Kumar Sinha** — Deputy Secretary — dsadmin.2@gov.in (2) |
| Scheme guidelines / implementation | **Shri Sunil Kumar** — Under Secretary (STG-III, SNG, TFS) — usstg3-dot@gov.in (7); **Shri R K Soni** — DDG (AS) — ddgas-dot@nic.in (4); **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (3); **Shri Amit Kumar Singh** — AWA (National regulation) — awanr.wpc-dot@gov.in (3) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Devendra Kumar Rai** — Joint Secretary (Telecom) — jst-dot@gov.in (81); **Shri Sunil Kumar Singhal** — DDG (LP) — ddglp-dot@gov.in (4); **Mr Sidheshwar Chakrabarti** — Deputy Secretary (Coordination) — dscord1-dot@gov.in (1); **Shri Awadhesh Kumar Singh** — Director (Elect.) — direlect-dot@nic.in (1) |
| Training / capacity building / workshops | **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (2); **Shri Sunil Kumar** — Under Secretary (STG-III, SNG, TFS) — usstg3-dot@gov.in (2) |
| Vigilance / disciplinary / court matters | **Ms. Jyoti Negi** — Under Secretary (SEA) — ussea-dot@gov.in ; [{'email':'adgsea1.hq-dot@nic.in'}] (1); **Shri Bijender Singh** — Under Secretary (STG-I & II) — us.sgt-dothq@gov.in (1); **Shri Sudhir Kumar Sinha** — Deputy Secretary — dsadmin.2@gov.in (1) |

### Deputy Secretary (GOI) M/o Minority Affairs New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Deputy Secretary, Department of School Education & Literacy, M/o Education, Govt. of India, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Advisory / public notice / caution |  |

### Deputy Secretary, Ministry of Tourism, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion |  |
| Recruitment rules / RRs |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Development of North Eastern Region (MDONER)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Ms. Parna Sahana** — Under Secretary — parna.sahana@nic.in (3) |
| Budget / sanction / release of funds / grants | **Shri Silabhadra Das** — Deputy Secretary — silabhadra.das@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Ms. Parna Sahana** — Under Secretary — parna.sahana@nic.in (3) |
| Other / unclassified | **Shri Rajesh Kumar** — Section Officer — rajesh.kmr07@gov.in (1) |
| Scheme guidelines / implementation | **Shri Silabhadra Das** — Deputy Secretary — silabhadra.das@gov.in (4); **Shri Mahipal Yadav** — Under Secretary — mahipal.yadav@gov.in (1); **Shri Vijay Kumar Goel** — Director — goelvijay.17@gov.in (1) |

### Earth Sciences (MoES)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (110); **Shri Sreenivasa Rao Gangi Reddy** — Joint Secretary — js@moes.gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (36) |
| Office administration / housekeeping | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (76) |
| Procurement / tenders / GeM | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (2); **Dr. N Khare** — Scientist G — neloy.khare@nic.in (1) |
| Recruitment rules / RRs | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (2); **Shri Sreenivasa Rao Gangi Reddy** — Joint Secretary — js@moes.gov.in (1) |
| Scheme guidelines / implementation | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (4) |
| Training / capacity building / workshops | **Shri Prem Prakash Maurya** — Deputy Secretary — premp.maurya@nic.in (2) |

### Electronics and Information Technology (MeitY)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Notan Roy** — Scientist E — notan.roy@meity.gov.in (5); **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (2); **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (1); **Shri Neeraj Kumar** — Junior Secretariat Assistant — neeraj.kumar82@meity.gov.in (1) |
| Advisory / public notice / caution | **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (3); **Shri Navneet Kumar** — OSD to Hon'ble Minister — moeit@gov.in ; [{'email':'osd.meity@meity.gov.in'},{'email':'navneet.k12@gov.in'}] (1); **Shri Saurabh Ranjan** — Scientist E — saurabh.ranjan@meity.gov.in (1); **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Ajay Kumar** — Scientist D — ajay.dhiman@meity.gov.in (1) |
| Customs / tariff / duty / GST |  |
| HR: appointment / transfer / posting / promotion | **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (4); **Shri. Amitesh Kumar Sinha** — Additional Secretary, MeitY & CEO, ISM — ceo@ism.gov.in ; amitesh.iras@gov.in (3); **Shri Manish Kumar** — Scientist C — manish.bishnoi@meity.gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (4) |
| Licensing / approvals / standards / enlistment | **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (2); **Shri Ritesh Kumar Sahu** — Scientist D — ritesh.s@meity.gov.in (1) |
| Office administration / housekeeping | **Shri Krishan Kumar Singh** — Joint Secretary — js.kksingh@meity.gov.in (1) |
| Other / unclassified | **Shri. Amitesh Kumar Sinha** — Additional Secretary, MeitY & CEO, ISM — ceo@ism.gov.in ; amitesh.iras@gov.in (4); **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (3); **Shri Shobhendra Bahadur** — Director — shobhendra.b@meity.gov.in (1); **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (1) |
| Procurement / tenders / GeM | **Shri Saurabh Ranjan** — Scientist E — saurabh.ranjan@meity.gov.in (2); **Dr. Kshitij Kushagra** — Scientist F — kshitij.kushagra@meity.gov.in (1) |
| RTI / appellate authority / CPIO | **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (1) |
| Recruitment rules / RRs | **Shri. Amitesh Kumar Sinha** — Additional Secretary, MeitY & CEO, ISM — ceo@ism.gov.in ; amitesh.iras@gov.in (3); **Shri Neeraj Kumar** — Junior Secretariat Assistant — neeraj.kumar82@meity.gov.in (1) |
| Scheme guidelines / implementation | **Shri Ajay Kumar** — Scientist D — ajay.dhiman@meity.gov.in (4); **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (4); **Dr. Kshitij Kushagra** — Scientist F — kshitij.kushagra@meity.gov.in (3); **Shri Saurabh Ranjan** — Scientist E — saurabh.ranjan@meity.gov.in (3) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Ajit Kumar** — Joint Secretary — js-akumar@meity.gov.in (7); **Shri Sushil Pal** — Joint Secretary — spal.1999@meity.gov.in (5); **Shri Notan Roy** — Scientist E — notan.roy@meity.gov.in (4); **Shri Saurabh Ranjan** — Scientist E — saurabh.ranjan@meity.gov.in (1) |
| Vigilance / disciplinary / court matters | **Shri Manish Kumar** — Scientist C — manish.bishnoi@meity.gov.in (1); **Shri Navneet Kumar** — OSD to Hon'ble Minister — moeit@gov.in ; [{'email':'osd.meity@meity.gov.in'},{'email':'navneet.k12@gov.in'}] (1); **Shri Ritesh Kumar Sahu** — Scientist D — ritesh.s@meity.gov.in (1) |

### External Affairs (MEA)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules | **Krishna K.** — Director (IC) — - (5) |
| Scheme guidelines / implementation | **Krishna K.** — Director (IC) — - (1) |
| Vigilance / disciplinary / court matters | **Krishna K.** — Director (IC) — - (5) |

### Heavy Industries (MoHI)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified | **Sh. Vijay Mittal** — Joint Secretary — vijay.mittal@nic.in (3) |
| Scheme guidelines / implementation | **Dr. Hanif Qureshi, IPS** — Additional Secretary — hanif.qureshi@gov.in (4); **Sh. Vijay Mittal** — Joint Secretary — vijay.mittal@nic.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Dr. Hanif Qureshi, IPS** — Additional Secretary — hanif.qureshi@gov.in (1) |

### Housing and Urban Affairs (MoHUA)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Ravi Kumar Arora** — Joint Secretary — jsle-mohua@gov.in (3); **SHRI PRAVEER KUMAR** — Joint Secretary — jsnudm-mohua@gov.in (2); **Shri Surya Narayan Jha** — Deputy Secretary — jha.sn@gov.in (2); **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (1) |
| Budget / sanction / release of funds / grants | **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (3); **Shri Sanjeev Kumar Sharma** — Under Secretary — sk.sanjeev@nic.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Nitin Gupta** — Section Officer — nitin.gupta20@gov.in (1); **Shri Sanjay Kumar** — Under Secretary — sanjaykumar55@nic.in (1); **Shri Sibbo Ram Meena** — Assistant Director of Estates — sibbo.meena@gov.in (1); **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (4); **Shri Amit Kumar Sinha** — Additional Private Secretary to Hon'ble MoS — sahu.tokhan@gov.in (3); **Shri Anil Kumar** — Private Secretary — anil.binjola@gov.in (3); **Shri Binay Kumar Malangia** — Under Secretary — binayk.malangia@nic.in (2) |
| Licensing / approvals / standards / enlistment | **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (2); **Shri Ashok Kumar.** — Dy Director Admin — cgewho@nic.in (1); **Shri Jitender Kumar** — Principal Private Secretary — jitender.kumar73@gov.in (1) |
| Office administration / housekeeping | **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (3); **Shri Jitender Kumar** — Principal Private Secretary — jitender.kumar73@gov.in (2); **Shri Amit Kumar Sinha** — Additional Private Secretary to Hon'ble MoS — sahu.tokhan@gov.in (1); **Shri Rajesh Kumar Sahu** — Director — rajesh.sahu@nic.in (1) |
| Other / unclassified | **Shri Anil Kumar** — Private Secretary — anil.binjola@gov.in (2); **Shri Rajesh Kumar Sahu** — Director — rajesh.sahu@nic.in (1); **Shri Sunil Kumar** — Deputy Secretary — sunilkumar.1970@gov.in (1); **Shri Surya Narayan Jha** — Deputy Secretary — jha.sn@gov.in (1) |
| Parliament / VIP references / reports | **Shri Anil Kumar** — Private Secretary — anil.binjola@gov.in (4) |
| Procurement / tenders / GeM | **Shri Anil Kumar** — Private Secretary — anil.binjola@gov.in (4); **Shri Rajesh Kumar Sahu** — Director — rajesh.sahu@nic.in (4) |
| RTI / appellate authority / CPIO | **Smt. Shivani Chauhan** — Assistant Director — chauhan.shivani@gov.in (1) |
| Recruitment rules / RRs | **Shri Anil Kumar** — Private Secretary — anil.binjola@gov.in (3); **Shri Binay Kumar Malangia** — Under Secretary — binayk.malangia@nic.in (1); **Shri Jitender Kumar** — Principal Private Secretary — jitender.kumar73@gov.in (1) |
| Scheme guidelines / implementation | **Shri Rajesh Kumar Sahu** — Director — rajesh.sahu@nic.in (2); **Shri Surya Narayan Jha** — Deputy Secretary — jha.sn@gov.in (1); **Shri Yogesh Antil** — Director — yogesh.antil@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Surya Narayan Jha** — Deputy Secretary — jha.sn@gov.in (6); **Shri Ravi Kumar Arora** — Joint Secretary — jsle-mohua@gov.in (5); **Shri Upendra Kumar Tiwari** — Under Secretary — uk.tiwari@nic.in (4); **SHRI PRAVEER KUMAR** — Joint Secretary — jsnudm-mohua@gov.in (3) |
| Vigilance / disciplinary / court matters | **Shri Ashok Kumar.** — Dy Director Admin — cgewho@nic.in (1) |

### Joint Secretary, Department of Financial Services, M/o Finance, Govt. of India, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Joint Secretary, Dept. of Fisheries, GoI, M/o Fisheres, Animal Husbandry and Dairying

| Topic | Contact officers (docs signed) |
|---|---|
| Licensing / approvals / standards / enlistment |  |
| Scheme guidelines / implementation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Joint Secretary, GOI, D/o Financial Services, M/o Finance, New Delhi.

| Topic | Contact officers (docs signed) |
|---|---|
| HR: leave / pay / allowances / service rules |  |
| Scheme guidelines / implementation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Joint Secretary, M/o Earth Sciences, New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| HR: appointment / transfer / posting / promotion |  |
| Recruitment rules / RRs |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Joint Secretary, M/o Health & Family Welfare, Govt. of India (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Joint Secretary, M/o Housing & Urban Affairs, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Labour and Employment (MoLE)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Dr. Tejaswi S. Naik** — Joint Secretary — js-socialsecurity@gov.in (11); **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (6); **Shri Ashutosh A.T.Pednekar** — Joint Secretary — ashutosh.pednekar@gov.in (4); **Shri Ajoy Sharma** — Additional Secretary — asajoy-mole@gov.in (3) |
| Advisory / public notice / caution | **Dr. Tejaswi S. Naik** — Joint Secretary — js-socialsecurity@gov.in (1) |
| Budget / sanction / release of funds / grants | **Shri Ashutosh A.T.Pednekar** — Joint Secretary — ashutosh.pednekar@gov.in (1); **Shri S. K. Gupta** — Regional P. F. Commissioner (Gr.I) (Pension) — 24345236rc.pension@epfindia.gov.in (1) |
| Committees / meetings / minutes / constitution of | **Anil Kumar Sahu** — Insurance Commissioner — ic-northeastzone@esic.gov.in (1); **Dr. Tejaswi S. Naik** — Joint Secretary — js-socialsecurity@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri S. K. Gupta** — Regional P. F. Commissioner (Gr.I) (Pension) — 24345236rc.pension@epfindia.gov.in (16); **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (5); **Shri Barajesh Kumar** — Under Secretary — barajesh.kumar@nic.in (2); **Dr. Mahendra Kumar** — Joint Secretary — jsadmin-mole@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Supriya Ranjan Datta** — Director — sr.datta@nic.in (1) |
| Office administration / housekeeping | **Shri Ajoy Sharma** — Additional Secretary — asajoy-mole@gov.in (2); **Dr. Mahendra Kumar** — Joint Secretary — jsadmin-mole@gov.in (1); **Shri Ravi Shankar Nirala** — Under Secretary — ravis.nirala@nic.in (1); **Shri S. K. Gupta** — Regional P. F. Commissioner (Gr.I) (Pension) — 24345236rc.pension@epfindia.gov.in (1) |
| Other / unclassified | **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (2); **Shri P. K. Tiwari** — Regional P. F. Commissioner (Gr.I) (CSD) — 24345222rc.csd@epfindia.gov.in (2); **Dr. Mahendra Kumar** — Joint Secretary — jsadmin-mole@gov.in (1); **Dr. Tejaswi S. Naik** — Joint Secretary — js-socialsecurity@gov.in (1) |
| Procurement / tenders / GeM | **Shri Manish Kumar Diwaker** — Under Secretary — mk.diwaker@nic.in (1) |
| RTI / appellate authority / CPIO | **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (1); **Shri Santosh Kumar** — Assistant Director (Vigilance) — vcc.vig@epfindia.gov.in (1) |
| Recruitment rules / RRs | **Shri Dhiraj Kumar** — Assistant P. F. Commissioner — 286084198655408288dhiraj.kumar@epfindia.gov.in (1) |
| Scheme guidelines / implementation | **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (1); **Shri P. K. Tiwari** — Regional P. F. Commissioner (Gr.I) (CSD) — 24345222rc.csd@epfindia.gov.in (1); **Shri Rahul Sinha** — Under Secretary — rahul.sinha81@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Dr. Tejaswi S. Naik** — Joint Secretary — js-socialsecurity@gov.in (3); **Ms. Deepika Kachhal** — Joint Secretary — js-osh@gov.in (3); **Shri Ajoy Sharma** — Additional Secretary — asajoy-mole@gov.in (3); **Shri P. K. Tiwari** — Regional P. F. Commissioner (Gr.I) (CSD) — 24345222rc.csd@epfindia.gov.in (2) |

### Legislative Department

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Rajiv Mani** — Secretary — secyoffice-ld@gov.in (2) |
| Committees / meetings / minutes / constitution of | **Shri Rajiv Mani** — Secretary — secyoffice-ld@gov.in (1) |
| Other / unclassified | **Shri Rajiv Mani** — Secretary — secyoffice-ld@gov.in (2) |

### Managing Director, Solar Energy Corporation of India, M/o New & Renewable Energy, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Other / unclassified |  |

### Micro, Small & Medium Enterprises (MSME)

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST | **Sh.Charanjeet Singh** — Assistant Director Gr-I — charan@dcmsme.gov.in (1) |
| Scheme guidelines / implementation | **Sh.Charanjeet Singh** — Assistant Director Gr-I — charan@dcmsme.gov.in (1) |

### Mines (MoM)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (15); **Shri Vivek Kumar Bajpai** — JOINT SECRETARY — vivek.bajpai@gov.in (3); **Shri Hanuman Prasad Nishad** — UNDER SECRETARY/ DEPUTY DIRECTOR — hp.nishad@nic.in (1) |
| Budget / sanction / release of funds / grants | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (1) |
| Committees / meetings / minutes / constitution of | **Shri Kaustubh Rajput** — Assistant Director — kaustubh.rajput@gov.in (1) |
| Customs / tariff / duty / GST | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (10); **Shri Kulveer Singh Yadav** — Joint Secretary — jspolicy-mines@gov.in (4) |
| HR: appointment / transfer / posting / promotion | **Shri Hanuman Prasad Nishad** — UNDER SECRETARY/ DEPUTY DIRECTOR — hp.nishad@nic.in (2) |
| Licensing / approvals / standards / enlistment | **Shri Vivek Kumar Bajpai** — JOINT SECRETARY — vivek.bajpai@gov.in (2); **Shri Kaustubh Rajput** — Assistant Director — kaustubh.rajput@gov.in (1) |
| Office administration / housekeeping | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (1) |
| Other / unclassified | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (3); **Shri Kulveer Singh Yadav** — Joint Secretary — jspolicy-mines@gov.in (2) |
| RTI / appellate authority / CPIO | **Shri Hanuman Prasad Nishad** — UNDER SECRETARY/ DEPUTY DIRECTOR — hp.nishad@nic.in (1) |
| Scheme guidelines / implementation | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Dr. Veena Kumari Dermal** — ADDITIONAL SECRETARY — veena.kumarid@gov.in (37); **Shri Kulveer Singh Yadav** — Joint Secretary — jspolicy-mines@gov.in (25); **Shri Vivek Kumar Bajpai** — JOINT SECRETARY — vivek.bajpai@gov.in (2); **Shri Hanuman Prasad Nishad** — UNDER SECRETARY/ DEPUTY DIRECTOR — hp.nishad@nic.in (1) |

### New and Renewable Energy (MNRE)

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution | **Shri Rishikesh Vaishnav** — Scientist C — rishikesh.mnre@gov.in (4); **Shri Sanjay Gorelal Karndhar** — Scientist E — karndhar.sg@nic.in (4); **Shri Aravindh Madhavankutty Ambika** — Scientist D — aravindh.mnre@gov.in (1); **Shri Jeevan Kumar Jethani** — Scientist F — jethani.jk@nic.in (1) |
| Committees / meetings / minutes / constitution of | **Shri J. Rajesh Kumar** — Economic Adviser — jrajesh.kumar@nic.in (2); **Shri Sanjay Gorelal Karndhar** — Scientist E — karndhar.sg@nic.in (2); **Shri Pankaj Saxena** — Scientist G — spankaj@nic.in (1); **Shri Shobhit Srivastava** — Scientist E — shobhit.srivastava@nic.in (1) |
| Customs / tariff / duty / GST | **Shri Mohd. Azmal Mansoori** — Scientist C — azmal.mnre@gov.in (1); **Shri Sachin Meena** — Scientist C — sachin.mnre@gov.in (1); **Shri Sanjay Gorelal Karndhar** — Scientist E — karndhar.sg@nic.in (1) |
| HR: appointment / transfer / posting / promotion | **Sunita Dhewal** — Under Secretary (officer authorised to receive PIDPI complaints) — sunitadhewal.mnre@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Pillarisetty Venkata Tarun Saketh** — Scientist C — tarunsaketh.mnre@gov.in (1) |
| Licensing / approvals / standards / enlistment | **Shri Sanjay Gorelal Karndhar** — Scientist E — karndhar.sg@nic.in (30); **Shri Rishikesh Vaishnav** — Scientist C — rishikesh.mnre@gov.in (3); **Shri Sujit Pillai** — Scientist F — sujit.pillai@gov.in (1) |
| Other / unclassified | **Shri Vikram Dhaka** — Scientist D — vikram.mnre@gov.in (4); **Shri Sujit Pillai** — Scientist F — sujit.pillai@gov.in (3); **Shri Rishikesh Vaishnav** — Scientist C — rishikesh.mnre@gov.in (2); **Shri Sanjay Kumar Shahi** — Scientist E — sk.shahi@nic.in (2) |
| Procurement / tenders / GeM | **Shri Anubhav Uppal** — Scientist D — anubhav.mnre@gov.in (1); **Shri Aravindh Madhavankutty Ambika** — Scientist D — aravindh.mnre@gov.in (1); **Shri Mohd. Azmal Mansoori** — Scientist C — azmal.mnre@gov.in (1) |
| Scheme guidelines / implementation | **Shri Rishikesh Vaishnav** — Scientist C — rishikesh.mnre@gov.in (11); **Shri Sanjay Gorelal Karndhar** — Scientist E — karndhar.sg@nic.in (7); **Shri Jeevan Kumar Jethani** — Scientist F — jethani.jk@nic.in (4); **Shri Rajesh Kulhari** — Joint Secretary — rkjs.mnre@gov.in (3) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri J. Rajesh Kumar** — Economic Adviser — jrajesh.kumar@nic.in (2); **Shri Rajesh Kulhari** — Joint Secretary — rkjs.mnre@gov.in (2); **Shri Pankaj Saxena** — Scientist G — spankaj@nic.in (1) |

### Panchayati Raj (MoPR)

| Topic | Contact officers (docs signed) |
|---|---|
| Training / capacity building / workshops | **Shri Kumar Shyamal Parthsarathi** — Under Secretary — shymal.pr@nic.in (3) |

### Ports, Shipping and Waterways (MoPSW)

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of | **Sh. Sachin Kumar** — SO — sofin-psw@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Sh. Uttam Kumar Mishra** — US (SU) — ussu-psw@gov.in (3); **Sh. Sandeep Gupta** — JS (PHRD, Establishment, Coord. & Parl) — jsadmin-psw@gov.injscord-psw@gov.in (2) |
| HR: leave / pay / allowances / service rules | **Sh. Uttam Kumar Mishra** — US (SU) — ussu-psw@gov.in (2) |
| Recruitment rules / RRs | **Sh. Sandeep Gupta** — JS (PHRD, Establishment, Coord. & Parl) — jsadmin-psw@gov.injscord-psw@gov.in (1) |
| Training / capacity building / workshops | **Sh. Sachin Kumar** — SO — sofin-psw@gov.in (1) |

### Power

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (5); **Shri Hemant Kumar Pandey** — Chief Engineer — hpandey@nic.in (2); **Shri Manish Mishra** — Director, Ministry of Power (WIM) — manish.mishra87@gov.in (2) |
| Advisory / public notice / caution | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (2) |
| Customs / tariff / duty / GST | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (9) |
| HR: appointment / transfer / posting / promotion | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (4); **Shri Ravi Prakash Pradhan** — Chief Information Security Officer, Ministry of Power — ciso-mop@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (7); **Shri Naorem Indrakumar Singh** — Under Secretary — indra.kumar39@nic.in (1) |
| Other / unclassified | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (5); **Shri Sanjeev Prasad** — Under Secretary — rcmdivision-mop@gov.in (1) |
| Procurement / tenders / GeM | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (12) |
| RTI / appellate authority / CPIO | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (1) |
| Scheme guidelines / implementation | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (8); **Shri Hemant Kumar Pandey** — Chief Engineer — hpandey@nic.in (4); **Shri Naorem Indrakumar Singh** — Under Secretary — indra.kumar39@nic.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Ghanshyam Prasad** — Chairperson — cea-cear@nic.in (22) |

### Railways (MoR)

| Topic | Contact officers (docs signed) |
|---|---|
| Customs / tariff / duty / GST |  |
| HR: appointment / transfer / posting / promotion |  |
| HR: leave / pay / allowances / service rules |  |
| Licensing / approvals / standards / enlistment |  |
| Office administration / housekeeping |  |
| Other / unclassified |  |
| RTI / appellate authority / CPIO |  |
| Recruitment rules / RRs |  |
| Scheme guidelines / implementation |  |
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Registrar General and Census Commissioner, India (RG & CCI), New Delhi

| Topic | Contact officers (docs signed) |
|---|---|
| Office administration / housekeeping |  |

### Road Transport and Highways (MoRTH)

| Topic | Contact officers (docs signed) |
|---|---|
| Acts / commencement / legislation | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (2) |
| Advisory / public notice / caution | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (2); **Shri Alok Kumar Verma** — DDG (TRW) — alokkumar.verma@nic.in (1); **Shri Ganesh B. Shelar** — EE (BP&SP) & HA — ganesh.bshelar@gov.in (1) |
| Budget / sanction / release of funds / grants | **Shri Shashi Bhoosan Kumar** — Under Secretary (Parl.,W&A ) — shashi.bhushan.mcd@mcd.nic.in (10) |
| Committees / meetings / minutes / constitution of | **Shri Alok Kumar Verma** — DDG (TRW) — alokkumar.verma@nic.in (1) |
| Customs / tariff / duty / GST | **Shri Akil Ahmad** — Superintending Engineer (S&R) — akil.ahmad@nic.in (1); **Shri Ganesh B. Shelar** — EE (BP&SP) & HA — ganesh.bshelar@gov.in (1); **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (1) |
| HR: appointment / transfer / posting / promotion | **Shri R. V. C. Sridhar** — Under Secretary (E-II, E-II-B) — rvcsridhar66@nic.in (1) |
| HR: leave / pay / allowances / service rules | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (1) |
| Licensing / approvals / standards / enlistment | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (1) |
| Office administration / housekeeping | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (1); **Shri Parveen kumar** — US (Transport) — parveen.kumar25@nic.in (1); **Shri R. V. C. Sridhar** — Under Secretary (E-II, E-II-B) — rvcsridhar66@nic.in (1) |
| Other / unclassified | **Shri Akil Ahmad** — Superintending Engineer (S&R) — akil.ahmad@nic.in (2); **Shri Bidur Kant Jha** — Director (New Technology) — bidurkant.jha@gov.in (2); **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (2); **Shri Bijender kumar** — Under Secretary (Gen./O&M/RTI & Coordination) — bijender.rathree@nic.in (1) |
| Procurement / tenders / GeM | **Shri Akil Ahmad** — Superintending Engineer (S&R) — akil.ahmad@nic.in (1) |
| Scheme guidelines / implementation | **Shri Shashi Bhoosan Kumar** — Under Secretary (Parl.,W&A ) — shashi.bhushan.mcd@mcd.nic.in (3); **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (1); **Shri Parveen kumar** — US (Transport) — parveen.kumar25@nic.in (1); **Shri Tulsa Ram** — AEE [S&R(P&B)] — ram.tulsa@gov.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Mahmood Ahmed** — Additional Secretary — as-transport-morth@gov.in,mahmood.ahmed@nic.in (18); **Shri C.N. Singh** — Joint Secretary (RTI and Grievance) — js.morth@gov.in (1) |

### Secretary, D/o Higher Education, M/o Education, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Advisory / public notice / caution |  |
| Committees / meetings / minutes / constitution of |  |

### Secretary, M/o Environment, Forests & Climate Change, Govt. of India, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

### Secretary, National Commission for Scheduled Tribes, M/o Tribal Affairs, GoI, New Delhi (On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Budget / sanction / release of funds / grants |  |

### Skill Development and Entrepreneurship (MSDE)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Shri Akhilesh Kumar Roy** — Under Secretary — akhileshroy-upsc@gov.in (1) |
| HR: leave / pay / allowances / service rules | **Shri V. S. Arvind** — Director — vs.arvind@gov.in (1) |
| RTI / appellate authority / CPIO | **Shri Akhilesh Kumar Roy** — Under Secretary — akhileshroy-upsc@gov.in (1) |

### Steel (MoS)

| Topic | Contact officers (docs signed) |
|---|---|
| Committees / meetings / minutes / constitution of |  |
| Customs / tariff / duty / GST | **Harshvardhan Singh Khangarot** — Director — harshvardhan.singh86@gov.in (1) |
| HR: appointment / transfer / posting / promotion | **Harshvardhan Singh Khangarot** — Director — harshvardhan.singh86@gov.in (27) |
| Licensing / approvals / standards / enlistment | **Harshvardhan Singh Khangarot** — Director — harshvardhan.singh86@gov.in (5) |
| Other / unclassified |  |

### Textiles (MoT)

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Shri Sachin Dev Varma** — Deputy Secretary — sachindev-cwc@gov.in (1) |
| Licensing / approvals / standards / enlistment | **Ms. Padmini Singla** — Joint Secretary — singla.padmini@gov.in (1) |
| Other / unclassified | **Ms. Padmini Singla** — Joint Secretary — singla.padmini@gov.in (1) |
| Procurement / tenders / GeM | **Shri Sachin Dev Varma** — Deputy Secretary — sachindev-cwc@gov.in (1) |
| Scheme guidelines / implementation | **Ms. Padmini Singla** — Joint Secretary — singla.padmini@gov.in (1); **Shri Akhilesh Kumar** — Deputy Director General, Ministry of Textiles — akhilesh.kumar99@gov.in (1); **Shri Hari Kishore** — Deputy Secretary — h.kishore@nic.in (1) |
| Statutory rules / gazette notifications (G.S.R. / S.O.) | **Shri Akhilesh Kumar** — Deputy Director General, Ministry of Textiles — akhilesh.kumar99@gov.in (1); **Shri Hari Kishore** — Deputy Secretary — h.kishore@nic.in (1) |

### Tourism

| Topic | Contact officers (docs signed) |
|---|---|
| HR: appointment / transfer / posting / promotion | **Mr Sayak Nandi** — Assistant Director — sayak.nandi@gov.in (3); **Ms. Seema Jain, IES (2011)** — Director — seema.jain74@nic.in (3); **Mr Praveen Kumar Singh** — Under Secretary — praveensingh-upsc@gov.in (2); **Mr Arun Srivastava** — Joint Director General — srivastava.arun@gov.in (1) |
| Procurement / tenders / GeM | **Ms. Seema Jain, IES (2011)** — Director — seema.jain74@nic.in (4); **Mr Ajit Pal Singh** — Assistant Director General — ajit.pal1@gov.in (2); **Mr Arun Srivastava** — Joint Director General — srivastava.arun@gov.in (2); **Mr Uttank Joshi** — Deputy Director General — uttank.joshi@nic.in (2) |
| Recruitment rules / RRs | **Mr Om Prakash** — Under Secretary — prakash.om50@nic.in (1); **Mr Praveen Kumar Singh** — Under Secretary — praveensingh-upsc@gov.in (1) |
| Scheme guidelines / implementation | **Mr Uttank Joshi** — Deputy Director General — uttank.joshi@nic.in (3) |

### Vice Chairman, Delhi Development Authority, M/o Housing & Urban Affairs, GoI, New Delhi(On Central Deputation)

| Topic | Contact officers (docs signed) |
|---|---|
| Statutory rules / gazette notifications (G.S.R. / S.O.) |  |

## Signatories missing from the rosters (roster gaps)

People who sign orders for a ministry but are not on its who's-who page / igod / civil lists — candidates to add to the yellow pages.

| Ministry | Signatory (as printed) | Signed as | Documents | Latest |
|---|---|---|---|---|
| Department of Justice (DoJ) | Prem Chand | Under Secretary (Appointments-! / Under Secretary (Appointments-1 | 228 | 2026-10-13 |
| Department of Legal Affairs (DoLA) | Kumar Gaurva | Officer / Officer (Judicial | 151 | 2026-07-02 |
| Department of Legal Affairs (DoLA) | D. Srinivas | Officer / Officer (J udicial | 147 | 2025-10-07 |
| Department of Legal Affairs (DoLA) | S. R. Mishra | Additional Secreta ry / Additional Secretary | 130 | 2024-08-16 |
| Department of Legal Affairs (DoLA) | R. K. Srivastava | Adviser / Adviser (Judi | 118 | 2026-08-20 |
| Department of Justice (DoJ) | Anant Kumar | Under Secretary (Appointments-II / Under Secretary (Appointments-IT | 113 | 2026-10-09 |
| Department of Telecommunications (DoT) | CMD BSNL | Additional Secretary, DOR-CUM-Member Secretary, / Assistant Director (Homoeo), Central Council for Research in | 89 | 2025-07-28 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ANIL AGRAWAL | Additional Secretary / Additional Secretary to the Government of India | 81 | 2025-08-13 |
| Department of Justice (DoJ) | Rajinder Kashyap | Additional Secretary to the Government of India / Special Secretary to the Government of India | 80 | 2023-11-23 |
| Department of Legal Affairs (DoLA) | Ramesh Kairamkonda | Officer / Officer (Judicial | 78 | 2026-10-16 |
| Department of Telecommunications (DoT) | Trilok Chandra | Director (AS-D / Director (AS-H1 | 64 | 2025-02-13 |
| Department of Legal Affairs (DoLA) | Inder Kumar | Additional Secretary / Additional Secretary | | 60 | 2018-10-17 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | GANESH H. NIKHARE | Under Secntary / Under SecretarYours faithfully, | 58 | 2025-07-14 |
| Department of Legal Affairs (DoLA) | Kumar Gaurav | Officer / Officer (Judicial | 51 | 2026-10-09 |
| Environment, Forest and Climate Change (MoEFCC) | Phalguni Banerjee | Under Secretary to the Government of India / Under Secretary to the Government of India. | 46 |  |
| Department of Legal Affairs (DoLA) | Manindra Choudhary | Adviser / Adviser (J | 42 | 2026-10-16 |
| Department of Legal Affairs (DoLA) | Lakka Muneswara Rao | Officer (Judicial | 39 | 2026-05-27 |
| Department of Health and Family Welfare (DoHFW) | D V K Rao | Under Secretary to the Govt of India / Under Secretary to the Govt. of India | 37 | 2025-12-04 |
| Department of Legal Affairs (DoLA) | C. Dabaria | Adviser / Adviser (Judichl | 37 | 2026-08-20 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SANDHYA BHULLAR | Joint Secretary to the Government of India / Jt. Secy | 36 | 2026-09-22 |
| Labour and Employment (MoLE) | Satish Chander | Deputy Secretary to the Government of India / Under Secretary | 36 | 2025-06-24 |
| Mines (MoM) | DINESH MAHUR | Joint Secretary / Joint Secretary to the Government of India | 33 |  |
| Department of Legal Affairs (DoLA) | B. S. Sharma | Adviser / Adviser (Judicial | 31 | 2025-01-06 |
| Steel (MoS) | Parmjeet Singh | Adviser / Advisor | 31 | 2025-04 |
| Department of Telecommunications (DoT) | Anil Kumar Gehlot | Director (AS-I / Director (AS-I} | 29 | 2023-08-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | GOPAL KRISHNA | Joint Secretary to the Government of India / Joint Secretary to the Government of India. | 28 | 2025-08-08 |
| Power | Ajay Shankar | Additional Secretary / Additional Secretary to the Government of India | 28 | 2025-07-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ASHOK KUMAR | JOINT SECRETARY / JOINT SECRETARY TO THE GOVERNMENT OF INDIA | 27 | 2025-07-02 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RAJEEV SINGH THAKUR | Additional Secy / Addl. Secy | 27 | 2026-09-24 |
| Department of Legal Affairs (DoLA) | Vijay Kumar Sharma | Joint Secretary & Legal Adviser | 27 | 2024-07-08 |
| Labour and Employment (MoLE) | RAJEEV ARORA | Jt. SecY / Jt. Secy | 27 | 2025-07-05 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Umesh Kumar | Joint / Joint Secretary | 26 | 2025-07-22 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SHAILENDRA SINGH | Additional / Additional Secretary to the Government of India | 25 | 2025-07-20 |
| Department of Administrative Reforms and Public Grievances (DARPG) | Vandana Nangia | I                             to the Government of India / Under Secretary to the Government of India | 25 | 2024-05-30 |
| Department of Health and Family Welfare (DoHFW) | Bikash R. Mahato | Under Secretary to the Go^veir^enfof / Under Secretary to the Government of India | 25 | 2024-04-24 |
| Department of Telecommunications (DoT) | Narayan Ram | Officer (AS-17 / Officer (AS-ID | 25 | 2022-08-29 |
| Labour and Employment (MoLE) | MANISH KUMAR GUPTA | Jt. Secy | 25 | 2025-06-26 |
| Department of Legal Affairs (DoLA) | Suresh Chandra | Joint Secretary & Lega! Adviser to the Govt. of India / Joint Secretary & Legal Adviser | 24 | 2025-10-07 |
| Department of Telecommunications (DoT) | Sanchit Kumar Garg | Assistant Director General (AS-III / Assistant Director General (AS-IIT | 24 | 2024-12-04 |
| Labour and Employment (MoLE) | Dhananjay Sharma | Under Secretary to the Government of Ind ia / Under Secretary to the Government of India | 24 | 2025-06-23 |
| Department of Legal Affairs (DoLA) | V.S. Chauhan | Under Secretary / Under Secretary to the Government of India | 23 | 2025-07-10 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | VANDANA KUMAR | JS / Jt. Secy | 22 | 2025-08-13 |
| Department of Justice (DoJ) | Jagannat Srinivasan | Joint Secretary to the Government of India | 22 | 2025-10-14 |
| Department of Land Resources (DLR) | Th. Lianboi | Under SecretarY (Admn / Under Secretary (Admn. | 21 | 2026-03-16 |
| Department of Telecommunications (DoT) | Subhash Chandra Kesarwani | Assistant Director General (AS-IID / Assistant Director General (AS-III | 21 | 2024-01-08 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | NITI Aayog | Comptroller / Comptroller and Auditor General of India | 20 | 2025-11-24 |
| Department of Justice (DoJ) | Jaganna Srinivasan | Joint Secretary to the Government of India / Joint Secretary to the Government ofIndia | 20 | 2025-08-29 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SUMITA DAWRA | Addl. Secy / Joint | 19 | 2026-06-03 |
| Labour and Employment (MoLE) | KALPANA RAJSINGHOT | Joint Secretary to the Government of India / Jt. Secy | 19 | 2025-07-04 |
| Environment, Forest and Climate Change (MoEFCC) | Shravan Kumar | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 18 |  |
| Department of Justice (DoJ) | Jagann Srinivasan | Joint Secretary to the Governinent of India / Joint Secretary to the Government of India | 16 | 2026-06-01 |
| Department of Legal Affairs (DoLA) | R. S. Verma | Additional Secretary / Secretary | 16 | 2024-08-02 |
| Department of Telecommunications (DoT) | Addl. CGCA | Advisor(F), DoT Hq. / CVO DoT HQ. | 16 | 2026-02-02 |
| Housing and Urban Affairs (MoHUA) | RAJIV RANJAN MISHRA | Jt. Secy | 16 | 2017-04-19 |
| Power | Madhukar Sood | Under Secretary to Government of India / Under Secretary to the Government of India | 16 | 2025-06-28 |
| Textiles (MoT) | RAJEEV SAXENA | Joint Secretary to the Government of India / Jt. Secy | 16 | 2025-01-02 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SHAMBHU DATT SATI | UNDER SECRETARY TO THE GOVERNMENT OF INDIA / Under Secretary | 15 | 2026-07-03 |
| Department of Health and Family Welfare (DoHFW) | G.P. Samanta | Under Secretary / Under Secretary (Hospital | 15 | 2019-11-20 |
| Department of Telecommunications (DoT) | Officers Concerned | Director (BD & F), HRIDC, Chandigarh. / Director (PA- Admin), DoP HQ. | 15 | 2026-07-07 |
| Power | AJAY TEWARI | Addl. Secy / Secy | 15 | 2025-07-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | S. JAGADEESAN | It. Secy / JT. SECY | 14 | 2025-07-04 |
| Department of Financial Services (DoFS) | Vinod Kumar | Director (Coordination and RTI Cell / Director (Coordination, DA and RT| Cell | 14 | 2026-10 |
| Department of Health and Family Welfare (DoHFW) | Baidyanath Prasad | Secretary to the Covemment of India / Secretary to the Covernment ofIndia | 14 | 2025-07-02 |
| Department of Health and Family Welfare (DoHFW) | Sanjay Pant | Under Secretary / Under Secretary fo the Government of India | 14 | 2025-09-10 |
| Environment, Forest and Climate Change (MoEFCC) | CEO CAMPA | Director, GA, MoEF&CC, New Delhi. / Principal Secretary (Forests), Government of Bihar, Paina. | 14 |  |
| Environment, Forest and Climate Change (MoEFCC) | Pradip Kumar | Under Secretary to the Government of India / Under Secretary to the Government of india | 14 |  |
| Labour and Employment (MoLE) | Ajay Malik | Under Secretary to Government of India / Under Secretary to the Government of India | 14 | 2018-12-28 |
| Power | SRIKANT NAGULAPALLI | Additional Secretary to the Govt. of India / Addl. Secy | 14 | 2025-09-19 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Atul Chaturvedi | Additional Secretary / Joint | 13 | 2025-07-20 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | MANMEET K. NANDA | It. Secy / Jt. Secy | 13 | 2025-08-13 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | P. Dasgupta | Director | 13 | 2025-06-25 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RAJIV AGGARWAL | Joint Secretary / Joint Secretary to the Government of India | 13 | 2025-07-20 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RENU SHARMA | Joint Secretary to the Govt. of India / Jt. Secy | 13 | 2026-06-03 |
| Department of Animal Husbandry and Dairying (DoAHD) | Rohit Tewari | Secretary to the Government of India / Under Secretary to the Government of India | 13 | 2025-07-15 |
| Department of Health and Family Welfare (DoHFW) | D VK Rao | Under Secretary to the Govt. of India | 13 | 2025-11-04 |
| Department of Health and Family Welfare (DoHFW) | Ram Naresh | Under Secretary to tJ:e Government of India. / Under Secretary to the Government of India | 13 | 2024-08-11 |
| Department of Legal Affairs (DoLA) | G. S. Yadav | Joint Secretary & Legal Adviser / Joint Secretary & Legal Adviser to the Government of India | 13 | 2017-09-04 |
| Department of Social Justice and Empowerment (DoSJE) | AINDRI ANURAG | Jt. Secy | 13 |  |
| Department of Telecommunications (DoT) | Saroj Kujur | Under Secretary to the Gov t. of India / Under Secretary to the Govt. of India | 13 | 2021-03-10 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | M.S. SRINIVASAN | Joint Secretary / Joint Secretary to the Government of India | 12 | 2025-07-02 |
| Department of Legal Affairs (DoLA) | Sher Singh Dagar | Joint Secretary & Legal Adviser / Joint Secretary and Legal Advisor | 12 | 2024-08-12 |
| Department of Telecommunications (DoT) | CMD MTNU CMD BSNL | Commissioner and Inspector General, Registration and / Commissioner of Food Safety, Food & Drugs Control | 12 | 2023-07-10 |
| Department of Telecommunications (DoT) | Pradeep Kumar | Director (CS-111 / Director (CS-III | 12 | 2022-11-10 |
| Environment, Forest and Climate Change (MoEFCC) | VED PRAKASH MISHRA | Director / Jt. Secy | 12 | 2021-12 |
| Labour and Employment (MoLE) | Babu Cherian | Deputy Secretary to the Government of India / Deputy Secretary to the Government of Indian | 12 | 2025-07-05 |
| Labour and Employment (MoLE) | G. NARAYANA RAJU | Secretary to the Govt. of India. | 12 | 2025-07-05 |
| Department of Health and Family Welfare (DoHFW) | Prem Narain | Under Secrctary to the Government of / Under Secretary (H-l | 11 | 2023-05-19 |
| Department of Higher Education (DoHE) | Purnendu Kishore Banerjee | Joint Secretary to the Government of India / Jt. Secy | 11 | 2026-07-09 |
| Department of Justice (DoJ) | Rajinder ICashyap | Additional Secretary to the Government of India / Special Secretary to the Government of India | 11 | 2023-11-02 |
| Department of Telecommunications (DoT) | Rajeev Prakash | Director (TF / Director (WF | 11 | 2013-02-05 |
| Legislative Department (LD) | G. NARAYANA RAJU | Secretary to the Govt. of India / Secretary to the Govt. of India. | 11 | 2020-03-18 |
| Parliamentary Affairs (MPA) | Satya Prakash | Additional Secretary / Additional Secretary to the Govt. of India | 11 | 2025-04-15 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Professional Services | Secretary C. & 1. / Under Demand No.11 for the year 2024-25 | 10 | 2026-06-23 |
| Department of Animal Husbandry and Dairying (DoAHD) | Dharm Prakash | Under Secretary (RTI / Under Secretary (RTT | 10 | 2025-07-15 |
| Department of Financial Services (DoFS) | Jasmine James | Deputy Secretary (Coord. / Under Secretary (Coordination | 10 | 2026-01 |
| Department of Health and Family Welfare (DoHFW) | LAV AGARWAL | Jt. SecY / Jt. Secy | 10 | 2025-12-08 |
| Department of Land Resources (DLR) | Rajeev Bahal | Under Secretary to the Government of India | 10 | 2022-03-17 |
| Department of Legal Affairs (DoLA) | Jaspal Singh Dhanju | Adviser (Judicial | 10 | 2025-08-05 |
| Department of Legal Affairs (DoLA) | Main Sectt | Registrar, CAT (PB) New oelhi. / Registrar, Delhi High Court, New Delhi. | 10 | 2024-02-28 |
| Department of Scientific and Industrial Research (DSIR) | Kuldip Kumar | Under Secretary to the Government of India / Under Secretary to the Govt' of India | 10 | 2025-12-05 |
| Labour and Employment (MoLE) | MANISH GUPTA | Jt. Secy | 10 | 2025-06-26 |
| Power | JYOTI ARORA | Jt. Secy | 10 | 2025-06-28 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | DAYANIDHI JOSHI | Under / Under Secretary to the Govt. | 9 | 2025-12-31 |
| Department of Animal Husbandry and Dairying (DoAHD) | UPAMANYU BASU | Jt. Secy | 9 | 2025-06-30 |
| Department of Financial Services (DoFS) | Abdul Gufran | Under Secretary to Government of India / Under Secretary to the Government of India | 9 | 2026-10 |
| Department of Health Research (DHR) | Tushar Karmarkar | Deputy Secretary / Deputy Secretary, DHR | 9 | 2026-10-08 |
| Department of Justice (DoJ) | Giridhar G Pai | Director | 9 | 2021-11-22 |
| Department of Justice (DoJ) | Yashasvi Kumar | Deputy Secretary to Government of India / Deputy Secretary to the Government of India | 9 | 2028-08-04 |
| Department of Legal Affairs (DoLA) | L. C. Dabaria | Adviser / Adviser (Judicial | 9 | 2025-02-10 |
| Department of Legal Affairs (DoLA) | Niranjan Prasad | Officer (Judicial | 9 | 2026-10-05 |
| Department of Telecommunications (DoT) | Prabha Ji | Director (AS-III / Director (AS-IIT | 9 | 2025-01-09 |
| Department of Telecommunications (DoT) | SHASHI RANJAN KUMAR | Joint Secretary (T)DoT / Jt. Secy | 9 | 2022-08-25 |
| Earth Sciences (MoES) | Rishi Kumar | DEPUTY SECRETARY (GA / Deputy Secretary | 9 | 2025-07-02 |
| Parliamentary Affairs (MPA) | Rameshwar Prasad | Under Secretary to the Government of India / Under Secretary to the Govt. Of India | 9 | 2025-08-01 |
| Power | Debranjan Chattopadhyay | Deputy Secretary to Government of India / Deputy Secretary to the Govt. of India | 9 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | N. N. PRASAD | Joint Secretary to the Government of India / Jt. Secy | 8 | 2025-08-03 |
| Department of Animal Husbandry and Dairying (DoAHD) | Deepak Sethi | Under Secretary / Under Secretary to the Government of India | 8 | 2025-06-27 |
| Department of Animal Husbandry and Dairying (DoAHD) | GIRJA NAND SINGH | Joint Secretary to the Government of India / Jt. Secy | 8 | 2026-03-27 |
| Department of Consumer Affairs (DoCA) | AMIT MEHTA | Jt. Secy | 8 |  |
| Department of Financial Services (DoFS) | SAURABH MISHRA | Jt. Secy | 8 | 2026-10 |
| Department of Higher Education (DoHE) | Gajraj Singh | Deputy Director / Deputy Director (OL | 8 | 2016-08-17 |
| Department of Legal Affairs (DoLA) | Kishore Kumar | Officer / Officer (Judicial | 8 | 2016-10-05 |
| Department of Personnel and Training (DoPT) | ARCHANA VARMA | It. Secy / Jt. Secy | 8 | 2014-10-27 |
| Department of Pharmaceuticals (DoPs) | Uma Magesh | Under Secretary to Government of India / Under Secretary to the Government of India | 8 |  |
| Department of Telecommunications (DoT) | Govind Singhal | Director (BS-III / Director (BS.III | 8 | 2007-03-07 |
| Department of Telecommunications (DoT) | Mahesh Kumar | Secretary / Secretary, Telecom, New’Delhi-1. | 8 | 2026-08-04 |
| Department of Telecommunications (DoT) | Mathias Tuti | Under Secretary (CWG / Under Secretary to Govt. India | 8 | 2026-06-30 |
| Environment, Forest and Climate Change (MoEFCC) | ARUN KUMAR MEHTA | Addl. Secy | 8 | 2018-03 |
| Labour and Employment (MoLE) | C.S. Rao | Under Secretary / Under Secretary to the Government of India | 8 | 2020-01-06 |
| Parliamentary Affairs (MPA) | Kiran Kumar | Under Secretary (Admn. / Under Secretary to the Govt. of India | 8 | 2024-07-23 |
| Power | Satinder Kaur | Under Secretary to the Government of India | 8 | 2025-06-28 |
| Statistics and Programme Implementation (MoSPI) | Neelam Arora | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 8 | 2026-10-22 |
| Steel (MoS) | RUCHIKA CHAUDHRY GOVIL | Joint Secretary to the Government of India / Jt. Secy | 8 | 2025-04 |
| Tourism | R K Bhati | . Director General / Asstt. Director General | 8 | 2024-01-30 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ADITI S RAY | DIRECTOR / Director | 7 | 2025-07-02 |
| Department of Animal Husbandry and Dairying (DoAHD) | S. C. Srivastav | Deputy Secretary to the Government of India / Deputy Secretary to the Govt. of India | 7 | 2025-10-19 |
| Department of Financial Services (DoFS) | SANJAY KUMAR MISHRA | Under Secy | 7 |  |
| Department of Financial Services (DoFS) | SHEKHAR AGARW AL | Director | 7 | 2026-01 |
| Department of Fisheries (DoF) | Yoginder Kumar | Under Secretary to the Government of India / Under Secy | 7 | 2025-12-08 |
| Department of Health Research (DHR) | GEETA NARAYAN | Jt. Secy | 7 | 2022-05-19 |
| Department of Health and Family Welfare (DoHFW) | Pamposh Pokhriyal | Deputy Director | 7 | 2026-05-12 |
| Department of Health and Family Welfare (DoHFW) | PATIBANDLA ASHOK BABU | Jt. Secy | 7 | 2026-05-21 |
| Department of Legal Affairs (DoLA) | M.A. Khan Yusufi | Joint Secretary & Govt. Counsel to the Government ofIndia / Joint Secretary & Legal Adviser to the Government of India | 7 | 2021-12-10 |
| Department of Legal Affairs (DoLA) | MADHAB CHARAN PRUSTY | Additional Secretary / Addl. Secy | 7 | 2026-07-23 |
| Department of Legal Affairs (DoLA) | Poonam Suri | ADVISER & / Advisor | 7 | 2018-01-09 |
| Department of Personnel and Training (DoPT) | Uma Magesh | Under Secretary to Government of India / Under Secretary to the Government of India | 7 | 2026-06-05 |
| Department of Public Enterprises (DPE) | Rakesh Bhartiya | Director | 7 | 2011-11-01 |
| Department of Public Enterprises (DPE) | Samsul Haque | Under Secretary / Under Secretary to the Government of India | 7 | 2025-07-11 |
| Department of Social Justice and Empowerment (DoSJE) | SANJEEV KUMAR | Joint Secretary to Government of India / Jt. Secy | 7 |  |
| Department of Telecommunications (DoT) | DG NICF | Executive Director, C-DoT / Sr.DDG | 7 | 2024-11-19 |
| Department of Telecommunications (DoT) | International Long Distance Submarine Cables | Jt. Secy. | 7 | 2025-12-24 |
| Department of Telecommunications (DoT) | N Janardhan | Director (SAS-III | 7 | 2025-02-24 |
| Department of Telecommunications (DoT) | Raj K. Kataria | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 7 | 2009-03-16 |
| Department of Telecommunications (DoT) | Raj Kumar Jha | Assistant Director General (Satellite-I1 / Assistant Director General (Satellite-ID | 7 | 2022-01-24 |
| Department of Telecommunications (DoT) | UMESH KHEMNANI | Director (DS / Director (DS-1 | 7 | 2023-11-09 |
| Environment, Forest and Climate Change (MoEFCC) | NARESH PAL GANGAWAR | Addl. Secy / Jt. Secy | 7 |  |
| Housing and Urban Affairs (MoHUA) | COUNTERSIGNED BY | Principal Secretary (MAHUD), / Principal Secretary (MAHUD}, | 7 | 2021-03-27 |
| New and Renewable Energy (MNRE) | GHANSHYAM PRASAD | Joint Secretary to the Govt. of India / Jt. Secy | 7 | 2022-12-01 |
| New and Renewable Energy (MNRE) | Rahul Rawat | Scientist 'C' / Scientist - C | 7 | 2024-08-23 |
| New and Renewable Energy (MNRE) | Rohit Thakwani | Scientist C / Scientist ‘C’ | 7 | 2023-02-15 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | G. NARAYANA RAJU | Secretary to the Govt. of India. | 6 | 2025-07-15 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Reetu Jain | Director / Director, | 6 | 2025-08-15 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SHUBHRA SINGH | Jt. Secy / Secy | 6 | 2025-09-01 |
| Department of Animal Husbandry and Dairying (DoAHD) | SAGAR MEHRA | Jt. Secy | 6 | 2021-12-17 |
| Department of Consumer Affairs (DoCA) | D. K. SONKER | Deputy Director (NTH / Director | 6 |  |
| Department of Health and Family Welfare (DoHFW) | D.D. Maheshwari | Under Secretary to Govt. of India / Under Secretary to the Govt. of India | 6 | 2018-04-04 |
| Department of Health and Family Welfare (DoHFW) | GAYATRI MISHRA | Jt. Secy | 6 | 2019-06-12 |
| Department of Health and Family Welfare (DoHFW) | Health Services | Chairman; / Chairperson; | 6 | 2025-01-31 |
| Department of Health and Family Welfare (DoHFW) | RAJIV WADHAWAN | Adviser / Adviser (Cost) | 6 | 2025-11-06 |
| Department of Legal Affairs (DoLA) | Asstt. Legal | Adviser (Judicial) | 6 | 2018-06-07 |
| Department of Legal Affairs (DoLA) | Devanshu Kumar | Under Secretary / Under Secretary to the Govt. of India | 6 | 2026-01-23 |
| Department of Legal Affairs (DoLA) | Radhe Shyam Singh | Under Secretary (Notary / Under Secretary to the Govt. of India | 6 | 2025-12-23 |
| Department of Legal Affairs (DoLA) | Ram Kumar | Officer (Judicial / Officer (Judl. | 6 | 2018-10-16 |
| Department of Legal Affairs (DoLA) | S. Yadav | Joint Secretary & Legal Adviser to the Government of India / Joint Secretary & Legal Adviser to the Govt. of India | 6 | 2017-07-22 |
| Department of Personnel and Training (DoPT) | JISHNU BARUA | Jt. Secy | 6 | 2016-06-20 |
| Department of School Education and Literacy (DSEL) | ANITA KARWAL | Addl. Secy / Jt. Secy | 6 | 2025-12-31 |
| Department of School Education and Literacy (DSEL) | Maneesh Garg | Director, Samagra Shiksha Department of School Education & Literacy, Govt. of India / Joint Secretary, Samagra Shiksha | 6 | 2025-12-31 |
| Department of School Education and Literacy (DSEL) | VRINDA SARUP | Addl. Secy / Secy | 6 | 2014-09-11 |
| Department of Science and Technology (DST) | Soumitra Basu | Under Secretary to the Govt of India | 6 | 2017-08-23 |
| Department of Telecommunications (DoT) | Assistant Chief Accounts | Officer / Officer (SEA-III & TF) | 6 | 2026-06-30 |
| Department of Telecommunications (DoT) | D. S. Parmar | Director (Elect. / Director (Electrical | 6 | 2019-02-24 |
| Department of Telecommunications (DoT) | HARI RANJAN RAO | Jt. Secy / Jt.Secy | 6 | 2022-08-25 |
| Department of Telecommunications (DoT) | Kuldeep Kumar | Under Secretary to / Under Secretary to the Govt. of India | 6 | 2024-11-19 |
| Department of Telecommunications (DoT) | OR Chittoor Chittoor ANDHRA | Director EXTENDED LAL DORA, KH- | 6 | 2024-03-20 |
| Department of Telecommunications (DoT) | S. K. Khare | Director (E lectrical / Director (Elect | 6 | 2020-11-27 |
| Department of Telecommunications (DoT) | Vinai Kumar Kanaujia | Director (IT-II / Director (IT-V | 6 | 2018-11-12 |
| Environment, Forest and Climate Change (MoEFCC) | GEETA MENON | Jt. Secy | 6 | 2017-08 |
| Environment, Forest and Climate Change (MoEFCC) | NARESH PAL GANGWAR | Jt. Secy | 6 | 2021-11 |
| Environment, Forest and Climate Change (MoEFCC) | SURJIT SINGH | Jt. Secy | 6 | 2018-03 |
| Housing and Urban Affairs (MoHUA) | Archana Mittal | Director (UPA / Director, UPA-I | 6 | 2016-06-15 |
| Housing and Urban Affairs (MoHUA) | K. Appeals | officer in the / officer in the year: | 6 | 2020-10-08 |
| Housing and Urban Affairs (MoHUA) | S.K. Lohia | Director (Urban Transport) / Director(UT | 6 | 2025-10-15 |
| Parliamentary Affairs (MPA) | Sharad Dwivedi | Under Secretary (Admn. / Under Secretary to the Govt. of India | 6 | 2025-08-01 |
| Planning (MoP) | Harinder Singh | Under Secretary (RT! / Under Secretary (RTD | 6 | 2026-06 |
| Power | Hausuanthang Guite | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 6 | 2025-06-28 |
| Steel (MoS) | ABHIJIT NARENDRA | Joint Secretary to the Government of India / Jt. Secy | 6 | 2026-06 |
| Steel (MoS) | Addl. Industrial | Adviser | 6 | 2025-04 |
| Tourism | RAJESH KUMAR | Under Secretary to the Government of India / Under Secy | 6 | 2025-08-07 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | D. V. PRASAD | Jt Secy / Jt. Secy | 5 | 2025-07-04 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RAVNEET KAUR | Joint Secretary / Jt. Secy | 5 | 2025-07-04 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SHRUTI SINGH | Director (Startup / Director (Startups | 5 | 2025-07-14 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | T. S. G. NARAYANNEN | Secretary, Central Boilers Board / Secy | 5 | 2025-08-11 |
| Department of Financial Services (DoFS) | Mohamed Ashraf J.S | Deputy Secretary / Deputy Secretary (Coord. | 5 | 2026-10 |
| Department of Fisheries (DoF) | Shankar L | Joint / Joint Commissioner (Fisheries-APL | 5 | 2025-12-08 |
| Department of Health and Family Welfare (DoHFW) | Vangara Prasad | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 5 | 2025-07-01 |
| Department of Higher Education (DoHE) | Rajnish Jain | Secretary / Secy | 5 | 2023-02-28 |
| Department of Higher Education (DoHE) | Sanjay Kumar Sinha | Director / Director (ICR | 5 | 2019-09-30 |
| Department of Justice (DoJ) | Arun Kumar Aggarwal | Officer (Appointments | 5 | 2023-02-06 |
| Department of Justice (DoJ) | C.K. Reejonia | Deputy Secretary to the Government of India / Director | 5 | 2021-11-22 |
| Department of Legal Affairs (DoLA) | M.K. Sharma | Adviser (Admn.} / Joint Secretary & Legal Adviser (Admn. | 5 | 2016-10-04 |
| Department of Legal Affairs (DoLA) | Sunita Anand | Addl. Secy / Joint Secretary & Legal Adviser | 5 | 2025-05-23 |
| Department of Legal Affairs (DoLA) | Shweta Kamboj | Officer (Judicial / Under Secretary to Govt. of India | 5 | 2026-06-09 |
| Department of Personnel and Training (DoPT) | Sangeeta Singh | Director(S / Director(Services | 5 | 2004-06-03 |
| Department of Pharmaceuticals (DoPs) | NAVDEEP RINWA | Jt. Secy | 5 |  |
| Department of Public Enterprises (DPE) | Umesh Dongre | Director | 5 | 2014-11-20 |
| Department of School Education and Literacy (DSEL) | Gajraj Singh | Deputy Director (OL / Deputy Director (Ol | 5 | 2016-05-19 |
| Department of School Education and Literacy (DSEL) | RINA RAY | Addl. Secy | 5 | 2017-03-02 |
| Department of Science and Technology (DST) | ANJU BHALLA | Joint Secretary / Joint Secretary (Admn. | 5 | 2020-11-25 |
| Department of Telecommunications (DoT) | AMIT YADAV | Jt. Secy / Secy | 5 | 2018-10-29 |
| Department of Telecommunications (DoT) | CMD MTNIJ CMD BSNL | Executive Officer, CSC e-Oovemance Services / Executive Officer, National Health | 5 | 2023-07-10 |
| Department of Telecommunications (DoT) | CVO DoT HQ | DDG (C&A). / Director (PA-Admin), DoP HQ. | 5 | 2025-01-10 |
| Department of Telecommunications (DoT) | D. C. Madan | Deputy Secretary to the Govt. of India / Under Secretarv (Abs. Cell | 5 | 2013-03-11 |
| Department of Telecommunications (DoT) | Ritu Pande | Assistant Director General (LR-I / Director General (LR-I | 5 | 2004-01-19 |
| Department of Telecommunications (DoT) | S.K. JASSAL | Officer (PHP | 5 | 2014-03-04 |
| Development of North Eastern Region (MDONER) | Vikramaditya Singh Dev | officer | 5 | 2026-08-27 |
| Housing and Urban Affairs (MoHUA) | SAILESH JOGIANI | Under Secretary (Housing / Under Secy | 5 | 2025-11-07 |
| Labour and Employment (MoLE) | RAJIT PUNHANI | Director General Labour Welfare / Joint Secret ary t o t he Government of India. | 5 | 2018-02-19 |
| Labour and Employment (MoLE) | VIBHA BHALLA | Jt. Secy | 5 | 2021-04-01 |
| Legislative Department (LD) | SUBHASH C. JAIN | Secy. to the Govt. of India. / Secy.to the Govt. of India. | 5 | 2025-10-30 |
| New and Renewable Energy (MNRE) | PIYUSH SINGH | Joint Secretary to the Government of India / Jt. Secy | 5 | 2023-05-23 |
| Parliamentary Affairs (MPA) | Mukesh Kumar | Deputy Secretary / Deputy Secretary (Admn. | 5 | 2026-07-22 |
| Ports, Shipping and Waterways (MoPSW) | MUMBAI PORT TRUST | Officer (im full (5 SRE NPL Et ae / Officer (in fail a oe es ee | 5 |  |
| Power | Alok Kumar | Director / Director (R&R | 5 | 2021-05-03 |
| Power | MRITUNJAY KUMAR NARAYAN | Jt. Secy | 5 | 2025-07-03 |
| Statistics and Programme Implementation (MoSPI) | Mukesh Kumar | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 5 | 2026-06-16 |
| Steel (MoS) | RASIKA CHAUBE | Additional Secretary to the Government of India / Addl. Secy | 5 | 2025-04 |
| Steel (MoS) | SUNIL BARTHWAL | Jt. Secy / Secy | 5 | 2025-04 |
| Tourism | RK Bhati | . Director General | 5 | 2023-10-09 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ANJALI PRASAD | Joint Secretary to the Government of India / Jt. Secy | 4 | 2025-09-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ANOOP KUMAR | Under Secretary to the Government of India / Under Secretary to the Govt. of India. | 4 | 2025-08-18 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Archana Gupta | Under Secretary to the Govt. of India | 4 | 2025-07-14 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | D.S. Parihar | Secretary, DIPP, No.271-A, Udyog / Under | 4 | 2025-06-30 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RAJENDRA RATNOO | Jt. Secy | 4 | 2025-08-12 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | TALLEEN KUMAR | Jt. Secy | 4 | 2025-08-13 |
| Department of Animal Husbandry and Dairying (DoAHD) | Bhushan Tyagi | Deputy Commissioner (RGM) - / Joint Commissioner | 4 | 2025-06-27 |
| Department of Animal Husbandry and Dairying (DoAHD) | KPJ Gerald | Deputy Secretary to Govt of India / Deputy Secretary to the Govt of India | 4 | 2020-06-04 |
| Department of Animal Husbandry and Dairying (DoAHD) | Madhusudanan V. K | Under Secretary (RTI / Under Secretary to the Government of India | 4 | 2025-06-27 |
| Department of Consumer Affairs (DoCA) | P. V. RAMA SASTRY | Jt. Secy / Secy | 4 |  |
| Department of Consumer Affairs (DoCA) | RAKESH KACKER | Addl. Secy / Spl. Secy | 4 |  |
| Department of Financial Services (DoFS) | Sanjay Kumar | Deputy Secretary / Deputy Secretary to the Government of India | 4 | 2026-01 |
| Department of Financial Services (DoFS) | Subhashchandra Amin | Under Secretary to the Go'rt. of India / Under Secretary to the Govt. of India | 4 |  |
| Department of Health and Family Welfare (DoHFW) | A. D. Bawari | Under Secretary | 4 | 2020-02-12 |
| Department of Health and Family Welfare (DoHFW) | BHAVANI THYAGARAIAN | It Secy | 4 | 2025-12-08 |
| Department of Health and Family Welfare (DoHFW) | Manoj Kumar Upadhyay | Under Secretary to the Government of India / Under Secretary to the Government of India. | 4 | 2023-01-05 |
| Department of Health and Family Welfare (DoHFW) | MH II | Under Secretary to the Govcrlrment ofIndia / Under Secretary to the Government of India | 4 | 2020-09-06 |
| Department of Health and Family Welfare (DoHFW) | Sriobit GuPta | Under Secretary to the Govt. Ol India | 4 | 2025-10-15 |
| Department of Health and Family Welfare (DoHFW) | Swamendu Singha | Under Secretary to the Government of India | 4 | 2025-10-15 |
| Department of Health and Family Welfare (DoHFW) | Swarnendu Singha | Under Secretary to the Government of India | 4 | 2023-08-31 |
| Department of Higher Education (DoHE) | AMIT KHARE | Joint Secretary (P / Joint Secretary (Policy | 4 | 2012-12-17 |
| Department of Justice (DoJ) | Naray Prasad | Deputy Secretary to the Gove nt of India / Deputy Secretary to the Governiènt of India | 4 | 2024-02-02 |
| Department of Legal Affairs (DoLA) | Asst. Legal | Adviser / Adviser (J) | 4 | 2026-06-03 |
| Department of Legal Affairs (DoLA) | D. Sfinivas | Officer (Judicial / Officer (Judicial Section | 4 | 2018-09-12 |
| Department of Legal Affairs (DoLA) | Krishna Mohan Arya | Adviser / Advisor | 4 | 2026-02-16 |
| Department of Legal Affairs (DoLA) | Legal Affairs | Registrar, Supreme Court of India, New Delhi. | 4 | 2025-12-15 |
| Department of Legal Affairs (DoLA) | PRAVEEN SRIVASTAVA | Addl Secy / Addl. Secy | 4 | 2026-10-08 |
| Department of Legal Affairs (DoLA) | Rajeev Kumar | Deputy SecretarY / Deputy Secretary to the Govt. of India | 4 | 2025-03-27 |
| Department of Legal Affairs (DoLA) | Solicitors General | Registrar, High Court of Andhra Pradesh. / Registrar, Supreme Court of India' New Delhi' | 4 | 2023-07-05 |
| Department of Personnel and Training (DoPT) | Pratibha Mohan | Director | 4 | 2004-07-23 |
| Department of Public Enterprises (DPE) | Naresh Kumar | Under Secretary / Under Secretary to the Govt. of India | 4 | 2023-09-13 |
| Department of Public Enterprises (DPE) | Rajesh Puri | Deputy Director | 4 | 2025-09-15 |
| Department of Science and Technology (DST) | Himanshu Gandhi | Under Secretary to Govt. of India / Under Secretary to the Govt of India | 4 | 2019-04-05 |
| Department of Science and Technology (DST) | Ravi Kumar | Officer / Officer (Pension). | 4 | 2018-09-04 |
| Department of Social Justice and Empowerment (DoSJE) | Asokan P K | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 4 |  |
| Department of Social Justice and Empowerment (DoSJE) | D.P. Majhi | Director | 4 |  |
| Department of Telecommunications (DoT) | A. S. Verma | Director (AS-IV / Director (VAS-II | 4 | 2016-09-26 |
| Department of Telecommunications (DoT) | Alok Ranjan | Director (IP | 4 | 2025-06-13 |
| Department of Telecommunications (DoT) | Ashish Kumar | Director (Satellite / Director (Satellite-l | 4 | 2022-07-12 |
| Department of Telecommunications (DoT) | B.L. Panwar | Secretary, TRAI, New Delhi | 4 | 2009-02-20 |
| Department of Telecommunications (DoT) | CMD. MTNL | Director (TERM-I), DoT (HQ). / Secretary, St2.te G~vt. ofChh2ttisgarh. | 4 | 2016-12-01 |
| Department of Telecommunications (DoT) | Dhananjay Kumar Ranjan | Director (AS- Ill / Director (AS-III | 4 | 2017-09-07 |
| Department of Telecommunications (DoT) | Devendra Singh | Director (DS-1 / Director (DS-I), DoT | 4 | 2010-08-25 |
| Department of Telecommunications (DoT) | Mohit Bansal | Assistant Di rector General (csJm / Assistant Director General (CS-ID | 4 | 2022-07-12 |
| Department of Telecommunications (DoT) | Rajesh Kumar Pathak | Deputy Director General (IC / Deputy Director General (International Cooperation | 4 | 2022-06-20 |
| Department of Telecommunications (DoT) | Rajesh Sharma | Executive Director & Principal Advisor / Under Secretary to the Government of India | 4 | 2025-04-15 |
| Department of Telecommunications (DoT) | ROSHNI SOHNI | DDG(Estt.) / Dy. Director General (Establishment) | 4 | 2025-06-10 |
| Department of Telecommunications (DoT) | Shashi Mohan | Director (AS-IV / Director(AS-IV | 4 | 2009-12-10 |
| Department of Telecommunications (DoT) | Vineet Malik | DS / Director (Radio-II), TEC & | 4 | 2026-01-10 |
| Department of Telecommunications (DoT) | VISHAL VISHAL SRIVASTAVA | Director (AS-II / Director (AS-III | 4 | 2026-01-21 |
| Development of North Eastern Region (MDONER) | Haradhan Das | Under Secretary to the Govt. of India | 4 | 2016-12-14 |
| Earth Sciences (MoES) | Ashok Saha | Scientist -C / Scientist-C, | 4 | 2025-07-04 |
| Earth Sciences (MoES) | P.G. Dastidar | Scientist | 4 | 2025-06-18 |
| Earth Sciences (MoES) | Tarun Sood | Officer (General / Officer (Genl. | 4 | 2025-06-20 |
| Environment, Forest and Climate Change (MoEFCC) | BISHWANATH SINHA | Jt. Secy | 4 |  |
| Environment, Forest and Climate Change (MoEFCC) | G. V. Subrahmanyam | Adviser / Scientist ‘G’ | 4 | 2021-08 |
| Environment, Forest and Climate Change (MoEFCC) | Lalit Kapur | Adviser | 4 | 2021-08 |
| Environment, Forest and Climate Change (MoEFCC) | Prem Maurya | Under Secretary to the Government of India / Under Secretary to the government of India | 4 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Prakash Mautya | Deputy Secretary / Under Secretary to the Government of india | 4 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prent Prakash Maurya | Under Secretary to the Government of India / Under Secretary to the Government of India ; | 4 |  |
| Environment, Forest and Climate Change (MoEFCC) | RITESH KUMAR SINGH | Jt. Secy | 4 |  |
| Housing and Urban Affairs (MoHUA) | DEEN DAYAL | US(MRTS-Coord) / Under Secretary to the Govt. of India | 4 | 2025-10-15 |
| Housing and Urban Affairs (MoHUA) | SUJATA CHATURVEDI | Director / Director (Delhi Division) | 4 | 2009-08-20 |
| Housing and Urban Affairs (MoHUA) | Th. Harikumar Singh | Director, PMAY (U / Director, PMAY(U | 4 | 2021-03-27 |
| Legislative Department (LD) | SANJAY SINGH | Secretary to the Govt. of India. | 4 | 2015-05-28 |
| Legislative Department (LD) | Sr. Accounts | Officer (A) / Officer(Admn) | 4 | 2015-12-07 |
| Power | GIREESH B. PRADHAN | Joint Secretary to the Government of India / Jt. Secy | 4 | 2025-06-28 |
| Power | RITVIK PANDEY | Jt. Secy | 4 | 2022-10-12 |
| Power | U.N Panjiar | Additional Secretary to the Government of India | 4 | 2025-06-28 |
| Textiles (MoT) | PRAJAKTA VERMA | Jt. Secy | 4 | 2024-07-03 |
| Tourism | Pankaj Kumar Devrani | Under Secretary (IT / Under Secretary to the Government of India | 4 | 2022-04-22 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | A E. AHMAD | JOINT SECRETARY TO THE GOVT. OF INDIA / Jt. Secy | 3 | 2025-06-30 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | A.C. DUGGAL | DIRECTOR / Director | 3 | 2000-09-08 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ANESH H. NIKHARE | Under SecretaW / Under Secretary | 3 | 2025-07-14 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Arun Kumar | Under / Under Secretary | 3 | 2025-07-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Deepak Narain | Director | 3 | 2025-07-22 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | GOPAL KRsAN'A | Joint Secretary to / Joint Secretary to the Government of India | 3 | 2025-07-22 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Indian Standards | Joint Secretary, / ds (BIS). | 3 | 2025-08-25 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | N. N. I'RASAD | it. Secy | 3 | 2025-06-24 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Rajesh Gupta | Director | 3 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Reetu Jarn | Director | 3 | 2025-08-06 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Saurabh Gaur | Joint / Joint Secretary to Government of India | 3 | 2025-07-14 |
| Department of Administrative Reforms and Public Grievances (DARPG) | Kaikam Doungel | Under Secretary to the Govt of India | 3 | 2023-03-23 |
| Department of Animal Husbandry and Dairying (DoAHD) | K. GURUMURTHY | Jt. Secy | 3 | 2026-07-10 |
| Department of Financial Services (DoFS) | Chandragupta Shaurya | Under Secretary to the Govt. of India | 3 |  |
| Department of Financial Services (DoFS) | TARUN BAJAJ | It. Secy | 3 | 2026-01 |
| Department of Fisheries (DoF) | Meenakshi Sankar | Under Secretary to the Govt. of India | 3 | 2024-09-02 |
| Department of Health Research (DHR) | REETA VASISHTA | Secretary to the Govt. of India. | 3 | 2022-04-18 |
| Department of Health and Family Welfare (DoHFW) | ARB Aa | Director | 3 | 2025-11-06 |
| Department of Health and Family Welfare (DoHFW) | ARUN K. PANDA | Jt. Secy | 3 | 2026-05-21 |
| Department of Health and Family Welfare (DoHFW) | G.A. Raghuvanshi | Secretary to the Government of india / Under Secretary to the Government of India | 3 | 2019-04-15 |
| Department of Health and Family Welfare (DoHFW) | G. NARAYANARAJU | Secretary to the Govt. of India. | 3 | 2025-12-08 |
| Department of Health and Family Welfare (DoHFW) | HAULIANKAP SUANTAH | Deputy Director (EPI | 3 | 2024-02-17 |
| Department of Health and Family Welfare (DoHFW) | M. K. Aggarwal | Deputy Commissioner (UIP), | 3 | 2025-12-02 |
| Department of Health and Family Welfare (DoHFW) | NIPUN VINAYAK | Jt. Secy | 3 | 2025-12-08 |
| Department of Health and Family Welfare (DoHFW) | REETA VASISHTA | Secretary to the Govt. of India. | 3 | 2023-10-27 |
| Department of Health and Family Welfare (DoHFW) | Roli Singh | Additional Secretary / Addl. Secy | 3 | 2024-02-16 |
| Department of Health and Family Welfare (DoHFW) | Shambhu Kumar | Under Secretary io the Govt. Of India / Under Secretary to the Govt. Of India | 3 | 2025-12-06 |
| Department of Health and Family Welfare (DoHFW) | Siba Sankar Sahoo | Officer | 3 | 2025-04-18 |
| Department of Health and Family Welfare (DoHFW) | SUNDEEP KUMAR NAYAK | Jt. Secy | 3 | 2025-12-08 |
| Department of Health and Family Welfare (DoHFW) | Tarsem Chand | Director | 3 | 2025-11-06 |
| Department of Higher Education (DoHE) | ISHITA ROY | Jt. Secy | 3 | 2023-05-11 |
| Department of Higher Education (DoHE) | Manish R. Joshi | Secretary / Secretary, | 3 | 2023-08-31 |
| Department of Higher Education (DoHE) | PSto HRM | Secretary, Deptt. of Higher Education | 3 | 2016-06-02 |
| Department of Higher Education (DoHE) | SUKHBIR SINGH SANDHU | Addl. Secy / Joint Secretary to the Government ofIndia | 3 | 2019-07-12 |
| Department of Justice (DoJ) | Gaurav Masaldan | Joint Secretary to the Government of India | 3 | 2024-03-21 |
| Department of Legal Affairs (DoLA) | ASHUTOSH MISHRA | Addl. Secy | 3 | 2025-10-17 |
| Department of Legal Affairs (DoLA) | Branch Secretariats | Officer, Department of Legal Affairs. | 3 | 2025-03-27 |
| Department of Legal Affairs (DoLA) | C.O. Rajan | Deputy Secretary (Admn.} / Deputy Secretary to the Government of India | 3 | 2010-04-05 |
| Department of Legal Affairs (DoLA) | D.R. Meena | Joint Secretary & Legal Adviser / Joint Secretary & Legal Adviser to the Government of India | 3 | 2005-07-18 |
| Department of Legal Affairs (DoLA) | G. NARAYANA RAJU | Secretary to the Govt. of India. / Secretary, | 3 | 2022-06-06 |
| Department of Legal Affairs (DoLA) | J.S. Mishra | Adviser | 3 | 2017-06-28 |
| Department of Legal Affairs (DoLA) | KuFnar Gaurva | Officer (Judicial | 3 | 2025-06-27 |
| Department of Legal Affairs (DoLA) | Rajiv Mani | Joint Secretary & Legal Adviser / Joint Secretary and Legal Adviser | 3 | 2020-03-31 |
| Department of Legal Affairs (DoLA) | Sandeep Saxena | Officer | 3 | 2016-10-04 |
| Department of Legal Affairs (DoLA) | Sr. Accounts | Officer / Officer (A) | 3 | 2016-05-25 |
| Department of Legal Affairs (DoLA) | Vijay Kumar Sharm | Senior Adviser | 3 | 2024-02-15 |
| Department of Legal Affairs (DoLA) | ZOYA HADKE | JOINT SECRETARY & LEGAL ADVISER TO THE GOVT.OF INDIA / Joint Secretary & Legal Adviser | 3 | 2015-01-16 |
| Department of Personnel and Training (DoPT) | S. G. Mulchandaney | Under Secretary | 3 | 2025-08-06 |
| Department of Personnel and Training (DoPT) | SUJATA CHATURVEDI | Addl. Secy | 3 | 2020-11-25 |
| Department of Public Enterprises (DPE) | Arun Kumar Sinha | Joint Secretary to the Government of India | 3 | 2011-12-29 |
| Department of Public Enterprises (DPE) | Kalyani Mishra | Director | 3 | 2020-08-05 |
| Department of Public Enterprises (DPE) | Lokesh Bajpai | Director / Director, DPE | 3 | 2025-07-07 |
| Department of Public Enterprises (DPE) | M. Subbarayan | Director / Joint Secretary | 3 | 2025-07-10 |
| Department of Public Enterprises (DPE) | Planning Commission | Commissioner for Disabilities, Room No. 120, / Commissioner for Persons with Disabilities, Sarojini House, | 3 | 2025-07-14 |
| Department of School Education and Literacy (DSEL) | J.P Pandey | Director, Samagra Shiksha Department of School Education & Literacy, Govt. of India | 3 | 2025-12-31 |
| Department of Scientific and Industrial Research (DSIR) | SRINIBAS PRADHAN | UNDER SECRETARY TO THE GOVT.OF INDIA / Under Secretary to the Govt.of India | 3 | 2025-10-30 |
| Department of Social Justice and Empowerment (DoSJE) | K. V. K. SUNDARAM | Secretary,, / Secretary. | 3 |  |
| Department of Social Justice and Empowerment (DoSJE) | N.S. Venkateshwaran | Under Secretary to the Government of India / Under Secretary to the Government of India. | 3 |  |
| Department of Telecommunications (DoT) | ANAND SINGH | Jt. Secy | 3 | 2023-04-21 |
| Department of Telecommunications (DoT) | D.S.S. Srinivasa Rao | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 3 | 2015-07-22 |
| Department of Telecommunications (DoT) | Dinesh Sharma | Director (Electrical | 3 | 2022-06-14 |
| Department of Telecommunications (DoT) | H. Atheli | Director | 3 | 2019-02-22 |
| Department of Telecommunications (DoT) | Malay Shrivastava | Joint Secretary (T / Joint Secretary to Government of India | 3 | 2012-10-05 |
| Department of Telecommunications (DoT) | Mandar Deshpande | Director (LFP-11 / Director (LFP-I): | 3 | 2019-11-06 |
| Department of Telecommunications (DoT) | MISHA BAJPAI | Assistant Director General (PHP | 3 | 2009-09-23 |
| Department of Telecommunications (DoT) | Narayan Rayn | Officer (AS-IIT | 3 | 2013-05-02 |
| Department of Telecommunications (DoT) | Sakshi Mittal | Director (SM | 3 | 2026-04-21 |
| Department of Telecommunications (DoT) | Shishir Kansal | Director (AS - IV / Director (AS-IV | 3 | 2016-07-05 |
| Department of Telecommunications (DoT) | Subhash Chandra Kesarwam | Assistant Director General (CS-III | 3 | 2016-04-18 |
| Department of Telecommunications (DoT) | Sukhbir Singh | Director (BS-II / Director (BS.III | 3 | 2004-11-09 |
| Department of Telecommunications (DoT) | Vijay Agrawal | Director (UDS | 3 | 2022-12-02 |
| Department of Telecommunications (DoT) | VINOD VAISH | Secretary to the Government of India | 3 | 2000-09-30 |
| Department of Telecommunications (DoT) | Yashwant Gupta | Director | 3 | 2024-09-12 |
| Earth Sciences (MoES) | Meena Gopinath | Under Secretary to the Govt. of India | 3 | 2026-08-05 |
| Electronics and Information Technology (MeitY) | RAJIV MANI | Secretary to the Govt. of India. | 3 | 2025-08-29 |
| Housing and Urban Affairs (MoHUA) | CREDAI P | Director | 3 | 2022-12-02 |
| Housing and Urban Affairs (MoHUA) | M. Ramachandran | Secretary | 3 | 2025-11-03 |
| Housing and Urban Affairs (MoHUA) | N. NAMASIVAYAM | Dy. Secy | 3 | 2001-05-19 |
| Housing and Urban Affairs (MoHUA) | NIRAJ KUMAR | Dy. Secy | 3 | 2001-09-04 |
| Housing and Urban Affairs (MoHUA) | Ramesh Chand | Deputy Secretary to the Govt. of India | 3 | 2026-02-26 |
| Housing and Urban Affairs (MoHUA) | S.K. Gupta | SecretarY (Admin / Secretary (Admn | 3 | 2025-10-31 |
| Housing and Urban Affairs (MoHUA) | Sushant Mishra VC | Additional Secretary, Govern | 3 | 2023-05-02 |
| Information and Broadcasting (MIB) | Santosh Kumar Maurya | Under Secretary | 3 | 2026-10 |
| Information and Broadcasting (MIB) | Shiv Ram Meena | Under Secrctary to the Govemmont of India / Under Secretary to the Governmenl of India | 3 | 2025-11 |
| Labour and Employment (MoLE) | Akhi Bharatiya Beedi Mazdoor Mahasangh | Secretary, INTUC, New Delhi Member | 3 | 2025-07-05 |
| Labour and Employment (MoLE) | D. CHAUDHURI | Dy. Director General | 3 | 2017-02-28 |
| Labour and Employment (MoLE) | SK Srivastwa | Under Secretary to the Government of India | 3 | 2019-11-07 |
| Labour and Employment (MoLE) | Tuglakabad Institutional Area | Director | 3 | 2025-07-05 |
| Legislative Department (LD) | T.K. VISWANATHAN | Secy. to the Govt. of India. / Secy. to the Govt. of india. | 3 | 2025-10-30 |
| Mines (MoM) | R. SRIDHARAN | Addl. Secy | 3 |  |
| Mines (MoM) | RAJIV MANI | Secretary to the Govt. of India. | 3 |  |
| Mines (MoM) | REETA VASISHTA | Secretary to the Govt. of India. | 3 |  |
| Mines (MoM) | Shakil Alam | Advisor / Advisor (Mines | 3 |  |
| New and Renewable Energy (MNRE) | AJAY JAIN | PRINCIPAL SECRETARY TO GOVERNMENT | 3 | 2019-01-03 |
| New and Renewable Energy (MNRE) | Sanjay G. Kamdhar | Scientist-E | 3 | 2023-08-23 |
| Power | K.D. Yadav | Under Secretary (OM | 3 | 2012-03-03 |
| Textiles (MoT) | Jayashree Sivakumar | Under Secretary to the Govt. of India | 3 | 2025-01-06 |
| Textiles (MoT) | Ravi Shankar Shukla | Deputy Secretary (AdmIn / Deputy Secretary to the Govt. of India | 3 | 2024-03-11 |
| Tourism | RAJA KAR | Under Secretary to the Govt. of India / Under Secy | 3 | 2025-08-07 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Andhra Pradesh | Commissioner of Labour, Paturi’s Pride, / Director Assam | 2 | 2025-07-04 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | ANITA PRAVEEN | Jt. Secy | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Asha Nangia | Scientist G and Group Coordinator | 2 | 2025-10-16 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Auditor Superintendent Gazetted | Officer | 2 | 2026-06-23 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | BABU LAL | Director | 2 | 2025-07-02 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | CEO. INSA | Secretary 2) PS to | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Chandandeep Singh | Officer / Officer (MS | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Dashrath Prasad | Director | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | DBA-I I | Director, North Eastern Development Finance Corporation | 2 | 2025-06-25 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Gauri Singh | Director | 2 | 2025-07-16 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | GOPAL KRISHAN | Jt. Secy | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | GOPAL KRisHRA | Joint Secretary to / Joint Secretary to the Government of India | 2 | 2025-07-22 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | JPAROEEPKUMAR KHER | UnderSecretary | 2 | 2025-08-13 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Kamala Hareesh | Officer | 2 | 2025-07-17 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | L. K. SHARMA | Under Secy | 2 | 2025-07-02 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Medium Enterprises | Secretary, / Secretary, Ministry | 2 | 2025-11-24 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | N. Ganapathi | Deputy Secretary to the Govt. of India | 2 | 2000-03-14 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Prita Kumar | Secretary to Government | 2 | 2025-07-03 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | R.S. JULANIYA | Director | 2 | 2003-11-28 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | RACHNA SHAH | Jt. Secy | 2 | 2025-07-14 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | REETA VASISHTA | Secretary to the Govt. of India. | 2 | 2025-06-30 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Surabhi Sharma | Deputy Secretary to the Government of India / Dy. Secretary to the Govt. of India | 2 | 2025-07-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Sushil K. Satpute | Director | 2 | 2025-07-02 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | SYED RAVISH ALI | Under Secy | 2 | 2025-08-13 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | T. Hanumantha Rao | Under Secretary to the Govt. of India, | 2 | 2025-07-01 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Tamil Nadu | Chief General Manger (FED), / Principal Scientist, | 2 | 2025-08-08 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | Urban Affairs | Secretary, | 2 | 2025-11-24 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | V Bhaskar | Joint Secretary to the Government of India / Jt. Secy | 2 | 2025-07-04 |
| Department for Promotion of Industry and Internal Trade (DPIIT) | YOGESH GUPTA | Dy. Secretary / Under Secretary | 2 | 2025-07-01 |
| Department of Administrative Reforms and Public Grievances (DARPG) | Bhuvnendra Singh | Under Secretary to the Govt. of India | 2 | 2025-10-29 |
| Department of Animal Husbandry and Dairying (DoAHD) | C. L.Gautam | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 2 | 2025-06-30 |
| Department of Animal Husbandry and Dairying (DoAHD) | DHARMENDRA DEO | Secy | 2 | 2026-06-05 |
| Department of Animal Husbandry and Dairying (DoAHD) | K. P. J. Gerald | Deputy Secretary to the Government of India | 2 | 2020-05-28 |
| Department of Animal Husbandry and Dairying (DoAHD) | LALIT GROVER | Under Secretary to the Govt. of India / Under Secy | 2 | 2026-04-16 |
| Department of Animal Husbandry and Dairying (DoAHD) | Narender Kumar | Under Secretary to the Government of India | 2 | 2021-01-13 |
| Department of Animal Husbandry and Dairying (DoAHD) | O. P. CHAUDHARY | Joint Secretary to the Government of India / Jt. Secy | 2 | 2026-06-05 |
| Department of Animal Husbandry and Dairying (DoAHD) | Pankaj Sinha | Under Secretary to the Government of India | 2 | 2025-06-30 |
| Department of Animal Husbandry and Dairying (DoAHD) | Personal Files | Secretary, AHD. | 2 | 2025-06-27 |
| Department of Animal Husbandry and Dairying (DoAHD) | R. P. Sinha | Under Secretary (RTI / Under Secretary to the Government of India | 2 | 2025-06-27 |
| Department of Animal Husbandry and Dairying (DoAHD) | RACHNA SHAH | Secy | 2 | 2026-10-23 |
| Department of Animal Husbandry and Dairying (DoAHD) | RAJBIR SINGH RANA | Jt. Secy / it. Secy | 2 | 2026-10-16 |
| Department of Animal Husbandry and Dairying (DoAHD) | RAJIV MANI | Secretary to the Govt. of India. | 2 | 2026-07-10 |
| Department of Animal Husbandry and Dairying (DoAHD) | RAVI S. PRASAD | Jt. Secy | 2 | 2026-06-05 |
| Department of Consumer Affairs (DoCA) | Consumer Disputes | Joint Registrar, | 2 |  |
| Department of Consumer Affairs (DoCA) | Disputes Redressal | Jt. Secy. | 2 |  |
| Department of Consumer Affairs (DoCA) | RAJIV AGARWAL | Secy | 2 |  |
| Department of Ex-Servicemen Welfare (DESW) | PRAVIN AGRAWAL | Jt. Secy | 2 | 2026-10 |
| Department of Financial Services (DoFS) | ANUP WADHAWAN | It. Secy / Jt. Secy | 2 | 2026-01 |
| Department of Financial Services (DoFS) | Arvind Gaur AK Thakur CASH | Under Secretary Director | 2 | 2026-01 |
| Department of Financial Services (DoFS) | Arvind Gaur Surender Singh CASH | Under Secretary Director | 2 | 2026-01 |
| Department of Financial Services (DoFS) | Aut Couto | Under Secretary to the Government of India | 2 | 2026-10 |
| Department of Financial Services (DoFS) | DEBASISH PRUSTY | Addl. Secy | 2 | 2026-07 |
| Department of Financial Services (DoFS) | GIC Re | Joint Secretary, DFS | 2 |  |
| Department of Financial Services (DoFS) | JNANATOSH ROY | Under Secy | 2 |  |
| Department of Financial Services (DoFS) | N. RAMAN | Executive Director | 2 | 2026-01 |
| Department of Financial Services (DoFS) | P.K. MALHOTRA | Secy. to the Govt. of India. / Secy. to the Govt. of india. | 2 | 2026-01 |
| Department of Financial Services (DoFS) | PANKAJ SHARMA | Jt. Secy | 2 | 2026-01 |
| Department of Financial Services (DoFS) | RAJENDER SINGH | Under Secy | 2 |  |
| Department of Financial Services (DoFS) | VINOD KLTMAR | Under Secy | 2 |  |
| Department of Fisheries (DoF) | Dibakar Misilra | Secretary to thefihmrrftEnt ol.India | 2 | 2021-03-30 |
| Department of Fisheries (DoF) | G.R.K. Rao | Assistant Commissioner (Fisheries | 2 | 2026-04-01 |
| Department of Fisheries (DoF) | Harbans Lal | Under Secretary to the Government of India | 2 | 2017-03-04 |
| Department of Fisheries (DoF) | LALIT GROVER | Under Secy | 2 | 2015-05-20 |
| Department of Fisheries (DoF) | S. Reshmi | Assistant Director (OL | 2 | 2022-06-09 |
| Department of Fisheries (DoF) | SAGAR MEHRA | Jt. Secy | 2 | 2023-05-09 |
| Department of Fisheries (DoF) | TARUN SHRIDHAR | Jt. Secy | 2 | 2012-04-01 |
| Department of Fisheries (DoF) | WEST BENGAL | Assistant Director , adfmarine.south24pgs@gm / Director of | 2 | 2026-04-01 |
| Department of Health Research (DHR) | Bhavani Shankara Bagepally | Scientist E, ICMR-NIE, Chennai | 2 | 2026-02-01 |
| Department of Health Research (DHR) | DHR-ICMR SECRETARIAT | Scientist F, DHR-ICMR | 2 | 2026-02-01 |
| Department of Health Research (DHR) | Priya Parmar | Director | 2 | 2026-02-01 |
| Department of Health Research (DHR) | Research Units | Director level person of | 2 | 2025-09-02 |
| Department of Health Research (DHR) | RICHA KHODA | Jt. Secy | 2 | 2026-06-23 |
| Department of Health and Family Welfare (DoHFW) | Adverse Events Following Immunization | Advisor, Department of Biotechnology, GoI | 2 | 2016-04-16 |
| Department of Health and Family Welfare (DoHFW) | Ali R. Rizvi | Joint Secretary, Medical Education | 2 | 2025-12-03 |
| Department of Health and Family Welfare (DoHFW) | B. BandYoPadhYaY | Deputy Secretary to the Govt. of India | 2 | 2017-10-13 |
| Department of Health and Family Welfare (DoHFW) | B L Meena | Under Secretary to the Government of India / Under Secretary(Co-ord | 2 | 2017-09-20 |
| Department of Health and Family Welfare (DoHFW) | Chief Admn | Officer - | 2 | 2017-11-18 |
| Department of Health and Family Welfare (DoHFW) | DNB Courses | Officer. : = | | 2 | 2012-11-02 |
| Department of Health and Family Welfare (DoHFW) | DV K Rao | Under Secretary to the Govt. of India / Under Secretary to the Govt. of India‘ | 2 | 2017-08-11 |
| Department of Health and Family Welfare (DoHFW) | DVK Rao | Under Secretary to the Govt. of India | 2 | 2018-02-06 |
| Department of Health and Family Welfare (DoHFW) | Dy Directo | Director, | 2 | 2022-03-31 |
| Department of Health and Family Welfare (DoHFW) | Educational Qualifications | Officer. | 2 | 2026-01-23 |
| Department of Health and Family Welfare (DoHFW) | G K Pillai | Under Secretary to the Government of India | 2 | 2021-09-07 |
| Department of Health and Family Welfare (DoHFW) | G. NARAYANA RAJU | Secretary to the Govt, of India. / Secretary to the Govt. of India. | 2 | 2026-05-21 |
| Department of Health and Family Welfare (DoHFW) | GP Samanta | Under Secretary to the Covemment of India / Under Secretary to the Governmcnt ofIndia | 2 | 2019-12-19 |
| Department of Health and Family Welfare (DoHFW) | I Assistrnl | Director | 2 | 2020-07-02 |
| Department of Health and Family Welfare (DoHFW) | IC Venkatesan | Under Secretary to the Government of India | 2 | 2020-02-11 |
| Department of Health and Family Welfare (DoHFW) | Lok Sabha Secretariat | Registrar, Supreme Court of India | 2 | 2025-09-10 |
| Department of Health and Family Welfare (DoHFW) | Manish Rai | Under Secretary to the Govt. of India | 2 | 2022-06-16 |
| Department of Health and Family Welfare (DoHFW) | Md Reyazuddin | Under Secretary of Governrnenl ol India / Under Secretary to the Govt' of India | 2 | 2026-10-08 |
| Department of Health and Family Welfare (DoHFW) | P. SH | UNDER SECRETARY TO THE GOVT. OF INDIA. | 2 | 2015-03-03 |
| Department of Health and Family Welfare (DoHFW) | Pradip Kumar Pal | Under Secretary to the Government of India / Under Secretary to the Government of India of India | 2 | 2016-06-08 |
| Department of Health and Family Welfare (DoHFW) | R.K. THAPAR | Under Secretary to Govt. of India | 2 | 2025-12-04 |
| Department of Health and Family Welfare (DoHFW) | R. RAVI | DEPUTY SECRETARY TO THE GOVERNMENT OF INDIA. / Deputy Secretary to the Government of India | 2 | 2025-09-10 |
| Department of Health and Family Welfare (DoHFW) | Rajeev Attri | Under Secretary to the Government of India / Under Secretary to the Government of India | | 2 | 2019-04-16 |
| Department of Health and Family Welfare (DoHFW) | S. Promotion Service Benchmark | OFFICER (GDMO) SUB-CADRE | 2 | 2015-03-03 |
| Department of Health and Family Welfare (DoHFW) | Sandeep Dhanda | Officer, Government of India | 2 | 2024-11-13 |
| Department of Health and Family Welfare (DoHFW) | Sitansu Mollan RorrtraY | Under Secretary to the Covernment of India | 2 | 2018-11-22 |
| Department of Health and Family Welfare (DoHFW) | Swarnendu Singhaf | Under Secretary to the Government of India | 2 | 2022-09-15 |
| Department of Health and Family Welfare (DoHFW) | Swarnendu Sinqha | Under Secretary lo the Government of Indih | 2 | 2024-04-02 |
| Department of Health and Family Welfare (DoHFW) | Vandana Chaudhary | Under Secretary to the Government of India | 2 | 2019-04-16 |
| Department of Health and Family Welfare (DoHFW) | VIKAS SHEEL | Jt. Secy | 2 | 2018-03-28 |
| Department of Health and Family Welfare (DoHFW) | Vilay Kumar | Under Secretary to Govt of India | 2 | 2023-06-21 |
| Department of Higher Education (DoHE) | Achint Kumar | Under Secretary (TS VI I / Under Secretary to the Government of India | 2 | 2019-09-09 |
| Department of Higher Education (DoHE) | Harpreet Singh | Director (U Policy | 2 | 2015-01-07 |
| Department of Higher Education (DoHE) | K.N. Channa | Secretary to the Government of India. / Secretary to the Govt. of India. | 2 | 1975-08-13 |
| Department of Higher Education (DoHE) | M. L. Soni | Officer | 2 | 2022-11-03 |
| Department of Higher Education (DoHE) | Nishant Upadhyaya | Under Secretary to the Governmenl of India / Under Secretary to the Govt.-of India | 2 | 2026-06-17 |
| Department of Higher Education (DoHE) | Praveen Kumar | Joint Secretary to the Government of India | 2 | 2017-05-17 |
| Department of Higher Education (DoHE) | Rajani Saini | Officer | 2 | 2026-06-19 |
| Department of Higher Education (DoHE) | Rajive Kumar | SecretarY / Secretary | 2 | 2023-08-24 |
| Department of Higher Education (DoHE) | RAKESH RANJAN | Joint Secretary (P / Jt. Secy | 2 | 2016-08-23 |
| Department of Higher Education (DoHE) | SHASHI PRAKASH GOYAL | Joint Secretary (TEL | 2 | 2015-07-25 |
| Department of Higher Education (DoHE) | SUNIL KUMAR | Joint Secretary to the Government of India / Jt. Secy | 2 | 2005-10-15 |
| Department of Higher Education (DoHE) | V. K. BHASIN | Secretary to the Govt. of India. / Secretary to the Govt~ ofIndia~ | 2 | 2012-06-21 |
| Department of Justice (DoJ) | Amarjeet Sroa | Under Secretary to Government of India | 2 | 2024-07-18 |
| Department of Justice (DoJ) | Ashok Kumar | Deputy Secretary to the Government of India / Deputy Secretary to the Government of india | 2 | 2021-03-17 |
| Department of Justice (DoJ) | Jaganna I Srinivasan | Joint Secretary to the Government of India | 2 | 2025-07-28 |
| Department of Justice (DoJ) | Jagannath Shinivasan | Joint Secretary to the Government of India | 2 | 2025-09-20 |
| Department of Justice (DoJ) | JagannatI Srinivasan | Joint Secretary to the Government of India | 2 | 2025-07-22 |
| Department of Justice (DoJ) | Jagannth Srinivasan | Joint Secretary to the Government of India | 2 | 2024-10-09 |
| Department of Justice (DoJ) | Preni Chand | Under Secretary (Appointments-I / Under Secretary(Appointments-I | 2 | 2024-07-03 |
| Department of Land Resources (DLR) | Sushil Kumar Daila | Director (WM / Director(WM | 2 | 2023-01-24 |
| Department of Land Resources (DLR) | Th Lianbol | Under Secretary to the Government of:ndia / under sec「 eta:γ to the Government ofIndia | 2 | 2022-08-29 |
| Department of Legal Affairs (DoLA) | Addl. Legal | Adviser | 2 | 2026-03-11 |
| Department of Legal Affairs (DoLA) | AJAY KUMAR ARORA | Jt. Secy | 2 | 2024-06-13 |
| Department of Legal Affairs (DoLA) | D. Sfinivasf | Officer (Judicial | 2 | 2024-09-19 |
| Department of Legal Affairs (DoLA) | D. Siinivas | Officer (Judicial | 2 | 2021-04-08 |
| Department of Legal Affairs (DoLA) | D. Srinivasy | Officer (Judicial / Officer (Judicial Section | 2 | 2019-04-16 |
| Department of Legal Affairs (DoLA) | D. STinivas | Officer (Judicial | 2 | 2018-03-23 |
| Department of Legal Affairs (DoLA) | DB. Srinivas | Officer (Judicial Section | 2 | 2016-11-07 |
| Department of Legal Affairs (DoLA) | Jay Prakash Dubey | Advisor / Advisor (Judicial | 2 | 2025-02-28 |
| Department of Legal Affairs (DoLA) | K. Srivastava | Adviser | 2 | 2017-03-20 |
| Department of Legal Affairs (DoLA) | Kumar Sharma | Adviser / JS&LA are relieved with | 2 | 2025-04-16 |
| Department of Legal Affairs (DoLA) | Lal Chand Dabaria | Adviser / Adviser (Judicial | 2 | 2022-02-01 |
| Department of Legal Affairs (DoLA) | Mahendra Khandelwal | JS&LA in the Main / Joint Secretary of | 2 | 2022-07-19 |
| Department of Legal Affairs (DoLA) | Main Sectl | Registrar, High Court ofJammu & Kashmir at Jammu. | 2 | 2024-12-26 |
| Department of Legal Affairs (DoLA) | Ramayan Yadav | Additional Secretary | 2 | 2018-10-04 |
| Department of Legal Affairs (DoLA) | SS Se | Officer (Judicial | 2 | 2024-09-19 |
| Department of Legal Affairs (DoLA) | Sunil Kumar Sah | Officer (Judicial | 2 | 2018-01-25 |
| Department of Legal Affairs (DoLA) | Shweta Kambo | Under Secretary | 2 | 2025-08-11 |
| Department of Pension & Pensioner's Welfare (DoPPW) | D.K. Solanki | Under Secretary to the Government of India | 2 | 2014-05-07 |
| Department of Pension & Pensioner's Welfare (DoPPW) | Dhrubajyoti Sengupta | Joint Secretary to Government of India | 2 | 2026-01-09 |
| Department of Personnel and Training (DoPT) | Ajay Kumar Sinha | Under Secretary to the Government of India | 2 | 2026-09-15 |
| Department of Personnel and Training (DoPT) | BHASKAR KHULBE | Addl. Secy | 2 | 2014-09-08 |
| Department of Personnel and Training (DoPT) | George D. Toppo | Under Secretary to the Government of India | 2 | 2022-06-24 |
| Department of Personnel and Training (DoPT) | Harish Chandra | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 2 | 1968-07-05 |
| Department of Personnel and Training (DoPT) | Indira Murthy | Deputy Secretary to the Govt. of India | 2 | 2007-09-27 |
| Department of Personnel and Training (DoPT) | Krishna Menon | Deputy Secretary to the Government of India | 2 | 1995-08-02 |
| Department of Personnel and Training (DoPT) | LaLt Kumar | Under Secretary to the Government of India | 2 | 2025-08-06 |
| Department of Personnel and Training (DoPT) | LOK RANJAN | Additional Secretary to the Government of India / Addl. Secy | 2 | 2019-10-24 |
| Department of Personnel and Training (DoPT) | Miss S. Trikha | Under Secretary to the Government of India / Under Secretary to the Govt. of India. | 2 | 1979-10-10 |
| Department of Personnel and Training (DoPT) | Mukta Goel | Director (E.! / Director (E.!). | 2 | 2025-08-06 |
| Department of Personnel and Training (DoPT) | N.R. Ranganathan | Secretary (P | 2 | 1993-04-29 |
| Department of Personnel and Training (DoPT) | R.C. Gupta | Deputy Secretary to the Government of India | 2 | 1979-03-21 |
| Department of Personnel and Training (DoPT) | RASHMI CHOWDHARY | Addl. Secy / Addl.Secy | 2 | 2021-01-05 |
| Department of Personnel and Training (DoPT) | RITVIK PANDEY | Jt. Secy | 2 | 2023-06-16 |
| Department of Personnel and Training (DoPT) | S. Radha Chauhan | Secretary (P | 2 | 2023-05-04 |
| Department of Personnel and Training (DoPT) | S. Trikha | Deputy Secretary to the Govt. of India. | 2 | 1984-05-01 |
| Department of Personnel and Training (DoPT) | SARITA PRASAD | It. Secy / Jt. Secy | 2 | 1996-01-22 |
| Department of Personnel and Training (DoPT) | SRINIVAS R. KATIKITHALA | Addl. Secy | 2 | 2020-03-02 |
| Department of Personnel and Training (DoPT) | Y.G. Parande | Director / Director. | 2 | 1996-10-07 |
| Department of Pharmaceuticals (DoPs) | Arvind Kumar | Under Secretary to the Govt. of India | 2 |  |
| Department of Public Enterprises (DPE) | A.K. Gautam | Director | 2 | 2011-04-18 |
| Department of Public Enterprises (DPE) | B.N. Mishra | Director | 2 | 2019-05-29 |
| Department of Public Enterprises (DPE) | CONCOR Shri Anurag Mathur | Executive Director (CSR) | 2 | 2018-12-10 |
| Department of Public Enterprises (DPE) | G. Ramachandran | Director | 2 | 2008-10-16 |
| Department of Public Enterprises (DPE) | Insurance Companies | Secretary, Department of Public Enterprises, CGO | 2 | 2023-01-17 |
| Department of Public Enterprises (DPE) | JYOTI MATHUR | Under Secy | 2 | 2014-11-11 |
| Department of Public Enterprises (DPE) | K. C. GUPTA | Jt SecY | 2 | 2020-01-08 |
| Department of Public Enterprises (DPE) | K.D. Tripathi | Joint Secretary to the Government of India | 2 | 2009-02-04 |
| Department of Public Enterprises (DPE) | Madhukar Gupta | Additional Secretary | 2 | 2016-08-10 |
| Department of Public Enterprises (DPE) | Pavanesh Kr Sharma | Deputy Secretary to the Government of India / Dy. Secretary to Govt of India | 2 | 2020-07-15 |
| Department of School Education and Literacy (DSEL) | Alok Jawahar | Under Secretary to the Government of India / Under Secretary to the Govt. of India | 2 | 2019-07-24 |
| Department of School Education and Literacy (DSEL) | Amarjit Singh | Additional Secretary(EE.1 / Additional Secretary(EE.| | 2 | 2014-10-09 |
| Department of School Education and Literacy (DSEL) | ANITA KAUL | Addl. Secy | 2 | 2011-09-12 |
| Department of School Education and Literacy (DSEL) | KS. Mahajan | Under Secretary (Public Greivance) - . | 2 | 2016-10-25 |
| Department of School Education and Literacy (DSEL) | Kuldeep Meem | Under Secretary to the Go\,,t. of India | 2 | 2022-11-09 |
| Department of School Education and Literacy (DSEL) | MLC. Worthing | Deputy Secretary to the Government of India | 2 | 2019-03-01 |
| Department of School Education and Literacy (DSEL) | PRABHAT KUMAR MISHRA | Joint Secretary to Government of India | 2 | 2023-12-27 |
| Department of School Education and Literacy (DSEL) | PSto HRM | Secretary, Deptt. of Higher Education | 2 | 2016-05-19 |
| Department of School Education and Literacy (DSEL) | Vikram Sahay | Director / Director, | 2 | 2016-06-08 |
| Department of Science and Technology (DST) | Anil Sharma | Under Secretary to the Government of India / Under Secretary to the Government of India | | 2 | 2014-09-19 |
| Department of Science and Technology (DST) | Annie G. Mathew | Additional Secretary to Government of India j / Joint Secretary to the Government of India | 2 | 2020-03-23 |
| Department of Science and Technology (DST) | N. Radhakrishnan | Director (E. Coord / Director(E.Coord | 2 | 2016-01-25 |
| Department of Scientific and Industrial Research (DSIR) | Nitin Gupta | Under Secretary to the Govt of India : / Under Secretary to the Govt of India H | 2 | 2025-10-09 |
| Department of Social Justice and Empowerment (DoSJE) | Akash Patil | Director / Director, DAIC | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | Atul Dev Sarmah | Director | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | Ghazala Meenai | Joint Secretary to the Government of India | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | Kishan Chand | Under Secretary to the Govt. of India | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | P. L. Negi | Director (SCD | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | Prabhudas Xalxo | Deputy Secretary to Govt. of India | 2 |  |
| Department of Social Justice and Empowerment (DoSJE) | Vikas Trivedi | Director | 2 |  |
| Department of Telecommunications (DoT) | Academic Qualifications | officer | 2 | 2025-01-21 |
| Department of Telecommunications (DoT) | AJAY GULATI | JOINT REGISTRAR / JOINT REGISTRAR (JUDICIAL | 2 | 2025-12-24 |
| Department of Telecommunications (DoT) | Ajay Kumar Nema | Director (Staff | 2 | 2022-05-02 |
| Department of Telecommunications (DoT) | AJEET SINGH | DIRECTOR(PHP / Director (PHP | 2 | 2009-05-15 |
| Department of Telecommunications (DoT) | AK Tripathi | Director(IT-ID | 2 | 2018-10-31 |
| Department of Telecommunications (DoT) | Balbir Singh | Advisor (HRD / Engineer (COP | 2 | 2026-06-01 |
| Department of Telecommunications (DoT) | Balvinder Singh | Director (AS-Ill | 2 | 2009-12-03 |
| Department of Telecommunications (DoT) | Bhartendu Kumar Singh | Director(E . llA | 2 | 2019-02-22 |
| Department of Telecommunications (DoT) | BRAJESH MISHRA | Director(PSU-I | 2 | 2011-04-01 |
| Department of Telecommunications (DoT) | C. P. Kushwaha | Under Secretary to the Govt. of India / Under Secretary, E.II(A | 2 | 2024-05-22 |
| Department of Telecommunications (DoT) | Chandan Kumar | Officer (STG-I1D / Officer (STG-III | 2 | 2018-11-29 |
| Department of Telecommunications (DoT) | CM D BSNL | officer / officer to implement the helpline. The Nodal | 2 | 2018-10-03 |
| Department of Telecommunications (DoT) | Communications Commission | Officer to Member (Personnel), Postal Services Board | 2 | 2026-07-01 |
| Department of Telecommunications (DoT) | Concerned Officers | Director (EW), DoT Hgq. for uploading / Director (IT) for uploading this order on DoT website. | 2 | 2024-02-13 |
| Department of Telecommunications (DoT) | DG Telecom | Advisor(F / Advisor(T | 2 | 2018-08-13 |
| Department of Telecommunications (DoT) | Durgendra Singh Jadaun | Officer (A&P), | 2 | 2026-09-24 |
| Department of Telecommunications (DoT) | Ek Dass | Under Secretary to the Govt. of India | 2 | 2022-08-04 |
| Department of Telecommunications (DoT) | EURUS NETWORK SERVICES | Director | 2 | 2023-10-31 |
| Department of Telecommunications (DoT) | GURDIP SINGH | Jt. Secy | 2 | 1999-03-20 |
| Department of Telecommunications (DoT) | HARISH KUMAR | Advisor 8037 / Director (Restg.) | 2 | 2021-04-15 |
| Department of Telecommunications (DoT) | Hoshiar Singh | Director (UDS | 2 | 2018-01-31 |
| Department of Telecommunications (DoT) | Information TechnologyDepartment | Principal Secretary | 2 | 2019-06-22 |
| Department of Telecommunications (DoT) | K. A. Sathia Sulochana | Under Secretary to the Govt. of India / Under Secretary to the Govt. ofIndia | 2 | 2014-01-02 |
| Department of Telecommunications (DoT) | KUMAR KANAUJIA | Director (IT-II / Director(IT | 2 | 2018-11-12 |
| Department of Telecommunications (DoT) | Lalit Kumar | Under Secretary | 2 | 2025-09-10 |
| Department of Telecommunications (DoT) | Madhu Mankotia | Under Secretary to the Government ofIndia | 2 | 2024-10-22 |
| Department of Telecommunications (DoT) | Managing Karimapatta | Director Cross Road, | 2 | 2019-09-30 |
| Department of Telecommunications (DoT) | Mukesh Meena | Director (Staff-Ill | 2 | 2022-04-01 |
| Department of Telecommunications (DoT) | MUKTA GOEL | Director (Establishment) | 2 | 2019-02-25 |
| Department of Telecommunications (DoT) | Narayah Ram | Officer (AS-II} | 2 | 2024-12-03 |
| Department of Telecommunications (DoT) | Narayan Bam | Officer (AS-IIL | 2 | 2016-10-04 |
| Department of Telecommunications (DoT) | P.C. Sharma | Director (AS-11 / Director (AS-II | 2 | 2014-12-29 |
| Department of Telecommunications (DoT) | Prashant Verma | Secretary, TRAI, New Delhi. | 2 | 2017-09-22 |
| Department of Telecommunications (DoT) | PRITINDER SINGH | Deptt. of Tetecom, Govt. of India / Officer | 2 | 2026-09-30 |
| Department of Telecommunications (DoT) | Raj Kulnar Jha | Assistant Director General (Satellite-II | 2 | 2021-03-11 |
| Department of Telecommunications (DoT) | Rajvir Sharma | Director (CS-1 / Director (CS-I | 2 | 2007-08-23 |
| Department of Telecommunications (DoT) | Rakesh Garg | Secretary, ] | 2 | 2015-03-04 |
| Department of Telecommunications (DoT) | S.P. Cianguly | Officer (AS-III | 2 | 2012-12-03 |
| Department of Telecommunications (DoT) | S.P. Mahapatra | Director (Civil | 2 | 2017-07-25 |
| Department of Telecommunications (DoT) | S. S. Pandey | Director (PR), NCA-T / Director (Policy Research | 2 | 2026-06-19 |
| Department of Telecommunications (DoT) | Sanjeev Kumar Arya | Director (CA), TEC | 2 | 2025-03-05 |
| Department of Telecommunications (DoT) | SHASHT RANJAN KUMAR | Jt. Secy | 2 | 2019-06-22 |
| Department of Telecommunications (DoT) | Shrigopal Agrawal | Director (AS-I | 2 | 2019-05-21 |
| Department of Telecommunications (DoT) | Subhash Chandra Kesanvani | Assistant Director General (AS-III / Assistant Director General (CS-Ill | 2 | 2015-03-23 |
| Department of Telecommunications (DoT) | Subodh Saxena | Deputy Director General (IC), DoT / Director(DS-II | 2 | 2023-12-19 |
| Department of Telecommunications (DoT) | Sujit Kumar | Secretary, TRAI | 2 | 2018-09-14 |
| Department of Telecommunications (DoT) | Suresh Kumar | Assistant Director General (AS-II / Member(F | 2 | 2021-04-16 |
| Department of Telecommunications (DoT) | TEC. TTPRIT. TCF | Director (IT), DoT for uploading the circular in DoT website / Director(IT), DoT for uploading the circular in DoT website. | 2 | 2023-08-29 |
| Department of Telecommunications (DoT) | UTs Chief Secretaries | Secretary, TRAI | 2 | 2018-07-06 |
| Department of Telecommunications (DoT) | ValbRay Sain | Director (AS-III | 2 | 2025-04-02 |
| Department of Telecommunications (DoT) | VANDANA SETHI | Director (Establishment) | 2 | 2024-01-18 |
| Department of Telecommunications (DoT) | West Bengal Principal SeCfetary | Principal Secretary | 2 | 2019-06-22 |
| Department of Telecommunications (DoT) | Vineeth Mathew | Adviser | 2 | 2025-05-20 |
| Department of Telecommunications (DoT) | Vivek Dwivedi | Under Secretary to the Government of India | 2 | 2024-06-13 |
| Department of Telecommunications (DoT) | Vivek Srivastava | Director (AS-II | 2 | 2019-05-30 |
| Department of Telecommunications (DoT) | VKPH Toppo | Under Secretary to the Govt. of India / Under Secretary(CWG | 2 | 2023-01-16 |
| Development of North Eastern Region (MDONER) | Harmeet Singh | Director | 2 | 2017-05-12 |
| Development of North Eastern Region (MDONER) | Rajesh Kumar | Director | 2 | 2012-07-02 |
| Earth Sciences (MoES) | Kailash Chand | Under Secretary to the Govt. of India | 2 | 2018-01-24 |
| Earth Sciences (MoES) | REETA VASISHTA | Secretary to the Govt. of India. | 2 | 2025-06-16 |
| Electronics and Information Technology (MeitY) | RAJENDRA KUMAR | Addl. Secy | 2 | 2025-10-23 |
| Electronics and Information Technology (MeitY) | Saurabh Gaur | Joint Secretary to the Government of India / Jt. Secy | 2 | 2021-12-30 |
| Environment, Forest and Climate Change (MoEFCC) | AJAY TYAGI | Jt. Secy | 2 | 2021-10 |
| Environment, Forest and Climate Change (MoEFCC) | APAR GRADING PROFORMA | officer | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | ARUN KUMAR MEH IA | Addl. Secy | 2 | 2017-11 |
| Environment, Forest and Climate Change (MoEFCC) | ARUN KUMAR MEHTA J | Secy | 2 | 2018-03 |
| Environment, Forest and Climate Change (MoEFCC) | ATUL KAUSHIK | Jt. Secy | 2 | 2018-03 |
| Environment, Forest and Climate Change (MoEFCC) | BRE Gur | Secretary | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | BHUPINDER PAL SINGH | Under Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | G. SUNDARAM | Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Kharibam Hitler Singh | Deputy Secretary | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | KAVITA CHAUHAN | Under Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Lalit Bakolia | Director | 2 | 2021-08 |
| Environment, Forest and Climate Change (MoEFCC) | NAMEETA PRASAD | Jt. Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | NEELESH KUMAR SAH | Jt.Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | OK WS | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | PrafiPiaRash Maurya | Under Secretary to the Government of India. | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Preity Prakash Misa | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Mautyay | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem P Marys | Under Secretary to the Government of India ! | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem P Maurya | Under Secretary to the Government of India | | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Prak Mautya | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Praka' Maurya | Under Secretary to the Govt. of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Prakash Many | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Prakash MauryS | Under Secretary to the Government of India : | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem PraRast Maurya | Under Secretary to the Government of India : | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prem Pri Maurya | Under Secretary to the Govt. of India ; | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | PrenrPrakash Maurya | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prern P Maurya | Under Secretary to the Govt. of India | | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Prexg Prakash Maurya | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | R. RAJAMANI | Secy | 2 | 2018-03 |
| Environment, Forest and Climate Change (MoEFCC) | Rajasekhar Ratti | Scientist ‘D’ | 2 | 2022-02 |
| Environment, Forest and Climate Change (MoEFCC) | RAJESH KUMAR YADAV | Under Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | Satish C. Garkoti | Scientist ‘G' | 2 | 2021-08 |
| Environment, Forest and Climate Change (MoEFCC) | SURJlT SINGH | Jt. Secy | 2 | 2018-03 |
| Environment, Forest and Climate Change (MoEFCC) | UDAY CHAUDHARI | Jt. Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | We WS | Under Secretary to the Government of India | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | VUAT SHARMA | Jt. Secy | 2 |  |
| Environment, Forest and Climate Change (MoEFCC) | YASHVIR SINGH. Economic | Advisor | 2 | 2017-06 |
| External Affairs (MEA) | Kartik Pande | Director (ADP | 2 |  |
| External Affairs (MEA) | Krishan Kumar | Deputy Secretary to the Govt. of India | 2 |  |
| External Affairs (MEA) | Vipra Pandey | Under Secretary (Cadre) | 2 |  |
| Housing and Urban Affairs (MoHUA) | ARs Wyre | Under Secretary to the Government of India | 2 | 2016-01-18 |
| Housing and Urban Affairs (MoHUA) | Avanish Kumar Mishra | Deputy Secretary to the Government of India | 2 | 2013-09-24 |
| Housing and Urban Affairs (MoHUA) | BISHWANATH SINHA | Jt. Secy | 2 | 2016-04-28 |
| Housing and Urban Affairs (MoHUA) | C. K. KHAITAN | Joint Secretary (Urban Transport / Jt. Secy | 2 | 2025-10-14 |
| Housing and Urban Affairs (MoHUA) | G. NARAYANA RAJU | Secretary to the Govt. of India. | 2 | 2021-03-12 |
| Housing and Urban Affairs (MoHUA) | Gasleen Kaur | Under Secretary to the Government of India | 2 | 2016-01-18 |
| Housing and Urban Affairs (MoHUA) | Gaurav Physically | Secretary, CREDAI | 2 | 2025-09-04 |
| Housing and Urban Affairs (MoHUA) | Lalit Kumar | Officer ( Admn.IV / Officer (Admn-IV | 2 | 2025-10-31 |
| Housing and Urban Affairs (MoHUA) | Manisha Nanda | Secretary (UD) to the | 2 | 2016-12-05 |
| Housing and Urban Affairs (MoHUA) | MEHAR SINGH | Deputy Secretary to the Government of india / Under Secy | 2 | 2007-01-03 |
| Housing and Urban Affairs (MoHUA) | PRAVEEN KUMAR SRIVASTAVA | Jt. Secy | 2 | 2017-05-03 |
| Housing and Urban Affairs (MoHUA) | R.R. Sharma | Under Secretary | 2 | 1966-05-30 |
| Housing and Urban Affairs (MoHUA) | R. Sathyanarayanan | Under Secretary to the Government of India | 2 | 2025-11-03 |
| Housing and Urban Affairs (MoHUA) | S.K. Guita | Under Secretary to Govt. of India | 2 | 2013-02-11 |
| Housing and Urban Affairs (MoHUA) | SIDDIQ PasHa | Under Secretary to Government | 2 | 2016-05-13 |
| Information and Broadcasting (MIB) | Deepak Negi | Under Secretary (11S | 2 | 2026-05 |
| Information and Broadcasting (MIB) | Kshitij Aggarwal | Deputy Director / Deputy Director (DM | 2 | 2025-11 |
| Information and Broadcasting (MIB) | SANJIV SHANKAR | Jt. Secy / Jt.Secy | 2 | 2025-01 |
| Information and Broadcasting (MIB) | Santosh Kumar Ma | Under Secretary to the Govt. of India | 2 | 2026-10 |
| Labour and Employment (MoLE) | ALOK MISHRA | Jt. Secy | 2 | 2025-12-30 |
| Labour and Employment (MoLE) | Anita Tripathi | Deputy Secretary to the Government of India / Deputy Secretary to the Govt. of India | 2 | 2016-09-16 |
| Labour and Employment (MoLE) | ANURADHA PRASAD | Addl. Secy / Special Secy | 2 | 2021-06-03 |
| Labour and Employment (MoLE) | H.L. Meena | Director {SS / Director, Govt. of India | 2 | 2017-11-27 |
| Labour and Employment (MoLE) | HEERALAL SAMARIYA | Addl. Secy | 2 | 2025-06-25 |
| Labour and Employment (MoLE) | N. K. SANTOSHI | Dy. Director General | 2 | 2017-08-29 |
| Legislative Department (LD) | REETA VASISHTA | Secretary to the Govt. of India. | 2 | 2023-09-28 |
| Legislative Department (LD) | V.K. BHASIN | Secy. to the Govt. of India. | 2 | 2012-01-12 |
| Micro, Small & Medium Enterprises (MSME) | Ajay Kumar | Deputy Secretary (LC | 2 | 2024-12-31 |
| Micro, Small & Medium Enterprises (MSME) | Bhaskar KaIra | Under Secretary to the Govt. of India | 2 | 2018-04-06 |
| Micro, Small & Medium Enterprises (MSME) | M AGAN LA L | Under Secretary | 2 | 2025-06-23 |
| Micro, Small & Medium Enterprises (MSME) | MAGAN LAL | Under Secretary | 2 | 2025-06-23 |
| Mines (MoM) | Dheeraj Kumar | Dy. Secretary to the Government of India | 2 |  |
| Mines (MoM) | EXPLORATION LICENCE | Director, | 2 |  |
| Mines (MoM) | NIRANJAN KUMAR SINGH | Jt. Secy | 2 |  |
| Minority Affairs (MoMA) | SHERSHA C SHAIK MOHIDDIN | Jt. Secy | 2 |  |
| New and Renewable Energy (MNRE) | ANKUR GUPTA | Principal Secretary to Government Haryana, / Principal Secretary to Govt. Haryana, | 2 | 2018-03-09 |
| New and Renewable Energy (MNRE) | DILIP NIGAM | Adviser (NSM / Director | 2 | 2017-06-19 |
| New and Renewable Energy (MNRE) | Divisional Heads | Officer, MNRE, New Delhi. | 2 | 2022-10-13 |
| New and Renewable Energy (MNRE) | JK Jethani | Scientist ‘F’ | 2 | 2024-11-28 |
| New and Renewable Energy (MNRE) | Monitoring Framework | Secretary, MNRE and other | 2 | 2024-07-04 |
| New and Renewable Energy (MNRE) | Regulatory Commissions | Secretary, MNRE, CGO Complex, New Delhi | 2 | 2023-04-10 |
| New and Renewable Energy (MNRE) | Ye Jha | Deputy Secretary to Govt. of India | 2 | 2025-02-13 |
| Parliamentary Affairs (MPA) | A Lana | Director to the Govt. of India | 2 | 2021-03-17 |
| Parliamentary Affairs (MPA) | Mukesh Bitton | Under Secretary to the Govt. of India | 2 | 2021-02-08 |
| Planning (MoP) | Aseem Kumar Jha | Secretary | 2 | 2026-06 |
| Planning (MoP) | Deo Nath Sah | Director | 2 | 2026-05 |
| Ports, Shipping and Waterways (MoPSW) | Dashrath Prasad | Director | 2 |  |
| Power | Ajit Kumar | Under Secretary to the Govt. of India | 2 | 2014-01-16 |
| Power | Bihari Lal | Under Secretary flrans / Under Secretary to the Govt. of India | 2 | 2025-07-03 |
| Power | D. Chattopadhyay | Under Secretary to the Govt of India / Under Secretary to the Govt. of India | 2 | 2020-04-21 |
| Power | G. NARAYANA RAJU | Secretary to the Govt. of India. | 2 | 2021-05-29 |
| Power | Goutam Ghosh | Director / Director (Trans | 2 | 2021-07-23 |
| Power | I. C. P. KESHARI | Joint Secretary to the Government of India / Jt. Secy | 2 | 2010-03-19 |
| Power | N. Sriraman | Under Secretary to the Government of India | 2 | 2025-06-28 |
| Power | Narender Singh | Under Secretary to the Govt of India | 2 | 2020-10-08 |
| Power | S. Majumdar | Under Secretary to the Govt. of India | 2 | 2021-06-08 |
| Road Transport and Highways (MoRTH) | Naveen. S | Director | 2 |  |
| Steel (MoS) | Addi. Industrial | Adviser | 2 | 2025-04 |
| Steel (MoS) | DALIP SINGH | Jt. Secy | 2 | 2025-04 |
| Steel (MoS) | SUDERSHAN MENDIRATTA | Jt. Secy | 2 | 2026-06 |
| Textiles (MoT) | Nitin Gupta | Under Secretary to the Govt of India | 2 | 2017-11-01 |
| Textiles (MoT) | Sr. Accounts | Officer(Admn) | 2 | 2024-06-10 |
| Tourism | Aqsa Ilahi | Deputy Director (MRD / Deputy Director, MRD | 2 | 2022-06-01 |
| Tourism | Bharti Sharma | Deputy Director General | 2 | 2026-01-30 |
| Tourism | Manju Maan | Under Secretary (HRD | 2 | 2025-08-05 |
| Tourism | Satarupa Datta | Assistant Director | 2 | 2022-09-08 |

## Caveats

- A signature block is read heuristically from the last two pages of each PDF: a name line (often in parentheses) followed by a designation line. Scanned PDFs and Hindi-only signature blocks are not read (counted above).
- Matching is by name similarity with a bonus for the same ministry and a matching designation; `confidence` is `high` (near-exact name, same ministry), `medium`, or `low (name only, other ministry)`. Rosters are a snapshot (who's-who pages, igod, DoPT civil lists), so an officer who signed in 2022 may have moved since.
- 'Contact person for a topic' means *signed documents on that topic*, not a published point of contact. Topics are keyword buckets over subject line + title + site category; a document can fall in two buckets.
- Rows with `match_status=unmatched` in `notification_signatories.csv` are real signatories who are not in any roster — a useful list of people to add to the yellow pages.