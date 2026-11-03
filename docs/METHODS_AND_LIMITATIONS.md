# Methods and limitations

How each kind of fact in this repository was produced, how confident to be in it, and where it is weak. Read this before relying on a
specific row. Spot checks quoted below were made by hand against the source PDFs.

## 1. Rosters: who is listed where
Rosters are what each ministry or department **publishes about itself** (who's-who pages, officer directories, telephone-directory PDFs,
scheme "contact" pages) plus DoPT's civil lists for IAS/IPS officers. They are as accurate as those pages, which are updated irregularly.
- A name appears once per division: someone holding two charges can appear twice.
- Minister-office staff (PS, PPS, PA) and attached-office staff are included where the page lists them; the `designation` column says which.
- Ministries whose directory is not published, is behind a login, or needs a form, have no roster here (see `data/MINISTRY_PLAN.md`).

## 2. Reading signatures from documents
- **Selection.** Only order-type documents are read: orders, office memoranda, notifications, circulars, guidelines, rules, gazette notifications, tenders and similar, chosen by words in the title/category (English and, for states, regional languages such as आदेश, અધિસૂચના, அரசாணை, ഉത്തരവ്).
- **Where.** The last two pages. A signature block is a name line (often in brackets) followed within three lines by a designation line that matches a strict pattern (Secretary, Under Secretary, Director, Scientist, Commissioner…, with abbreviations such as `Jt. Secy`), or a one-line gazette form `NAME, Jt. Secy.`. A `Digitally signed by` stamp is used only when no other block exists and is marked as such.
- **Filters.** A candidate "name" is rejected if all its words are ordinary English words (a dictionary check), if it contains stop-words such as `Committee`, `Foundation`, `Guard File`, or if the designation line reads like prose. This removed most table headings and address lines.
- **Scans.** Documents with no text layer are OCR'd with Tesseract on the first and last page (for signature reading) and, for the markdown corpus, up to ten pages. State documents use the state's own Tesseract language packs plus English.
- **Indic scripts.** A name line in Devanagari, Tamil, Malayalam, Kannada, Telugu, Bengali, Gujarati, Gurmukhi or Odia followed by a designation word from a table of per-language Secretary/Director/Commissioner terms is accepted. The name is then romanised: first by a language model (cached), with a rule-based transliteration (`signatory_rule`) kept alongside for comparison.
- **What is not read.** Hindi-only signature blocks that OCR badly, signatures that are images only, and names printed outside the last two pages.

*Check:* for 40 randomly chosen high-confidence matches, the signer's name and a designation word were found in the last 4,000 characters of that document's converted markdown in all 40. This confirms the signature was read from the document; it does not prove the roster match is the right person (that is what the confidence labels and the ambiguity rule address). OCR errors in individual letters occur in some scanned documents (for example `Baldev SingnV` for Baldev Singh), which is why matching tolerates spelling noise.

## 3. Matching a signer to a roster officer
For each signature, every roster entry with a shared name token is scored:
1. **Name similarity (0–1).** Each token of the shorter name must be accounted for in the longer one: exact match = 1, OCR-near match = 0.9, initial match = 0.8; the sum is divided by the longer token count. Spelling variants common in Indian English (`oo/u`, `ee/i`, `w/v`, `th/t`, `Apoorva/Apurva`) are folded together first.
2. **Rank sanity.** A signature as Under Secretary cannot match a roster entry of Secretary rank (and vice versa); state-posted IAS officers are not candidates for union-ministry documents.
3. **Ministry.** Same ministry/department raises the score; a match that is name-only is capped at *low*.

Confidence labels in `confidence` / `match_confidence`:
| Label | Meaning |
|---|---|
| `high` | Name similarity ≥ 0.95, same ministry, ranks compatible |
| `medium` | Similarity ≥ 0.80 and same ministry |
| `low (name only, other ministry)` | Near-exact, 3+ name tokens, but a different ministry; plausible only for senior officers on deputation |
| `unmatched` / `rejected (…)` | No acceptable roster entry; the signer is real but not in any roster |

*Known failure mode:* very common two-word names (`Rajesh Kumar`, `Sunil Kumar`) can match the wrong person. For this reason the career layer applies an extra ambiguity rule (below), and `low` matches should never be used without checking.

## 4. Topics
Each matched document is labelled with up to two of 18 keyword buckets applied to the subject line, title and site category:
HR appointment/transfer/posting/promotion · HR leave/pay/allowances/service rules · Recruitment rules · RTI/appellate/CPIO · Procurement/tenders/GeM ·
Budget/sanction/release of funds/grants · Statutory rules/gazette notifications · Acts/commencement/legislation · Customs/tariff/duty/GST ·
Scheme guidelines/implementation · Committees/meetings/minutes · Advisory/public notice/caution · Licensing/approvals/standards ·
Legal metrology/consumer protection rules · Office administration · Training/workshops · Vigilance/disciplinary/court matters · Parliament/VIP references/reports.
Buckets are regular expressions, not a classifier; documents that match none are `Other / unclassified`. "Officer X is the contact for topic Y" means *X signed N documents on topic Y*, not that X is the published point of contact.

## 5. Policy and incentive instruments
- **Curated list** (`policy_windows.csv`, `policy_contacts.csv`): open incentive instruments compiled earlier, each with its owning ministry.
- **Discovered from titles:** phrases ending in Scheme / Yojana / Mission / Programme / Fund / Abhiyan / Policy / Package / Challenge, "PM-…" names, "PLI …" and "Guidelines for …", kept when at least two documents carry the same normalised name. Duplicates and near-duplicates are possible.
- **Discovered from announcements:** PIB releases and ministry-site items since 4 Jul 2026 are shortlisted by keyword, classified by a language model (instrument or not, type, status, new or update) and checked against what the repository already knows. This step is where errors are most likely: reports of achievements can look like announcements, and the model sometimes names the programme loosely. Outlay and period are only filled when the release text states them (pattern extraction), so they are blank for most items.
- **Contacts** (`evidence` column): people who signed documents naming that instrument → roster divisions named after it → the ministry's most active signers → the igod minister/secretary. Only the first two are specific to the instrument; the last two are fallbacks, flagged as such.
- State instruments are matched only to documents from the same state; short generic acronyms (PPP, PLI, MSME) match only together with another distinctive word.

## 6. Where are they now (career layer)
Sources: DoPT ER sheets (`current_posting` and its effective date, authoritative for IAS) and appointment/transfer news (three sites). Events are extracted from titles/first paragraphs by pattern, with a language model for multi-officer reshuffle articles.
- A signer is linked to an event by name similarity, rank compatibility and recency.
- **Ambiguity rule:** if the same name maps to more than one distinct officer (different cadre/batch in the ER sheets), no move is claimed; `moved_since_signing = ambiguous name`.
- `moved_since_signing = yes` means a later event names a *different organisation*. After the ambiguity rule it remains a lead to verify: 83 centre signers carry it (94 more are marked `ambiguous name`), and a few that were inspected looked doubtful (a common name matched to a district post).

## 7. Markdown conversion
Text-layer PDFs: `pdftotext` in reading order, hyphenated line breaks joined, page markers kept. Scans: Tesseract (150 dpi, page-segmentation mode 6) in the document's language(s), up to ten pages, one thread per worker. Tables are not reconstructed — they come out as lines of text. 332 of 40,708 documents (0.8%) produced no text and are flagged. The first AWS test run revealed silent OCR failures caused by Tesseract's default multi-threading; after fixing it every previously empty scan in the test shard produced text.

## 8. Coverage limits
- **Roster coverage bounds match rate.** Centre: 2,305 signed documents matched of 8,224 with a signature (28%). States: 508 of 3,444 (15%), because most state-order signers are secretariat-service officers who are in no roster.
- **Selection caps.** Centre: every order-type PDF in the document index was selected (24,577) and 24,262 downloaded; PDFs that returned errors or were over 25 MB were skipped. States: at most 300 + 400 order PDFs per state were read (20,608 selected, 16,446 read), chosen from the pages the crawl reached, so states with thousands of orders are a sample.
- **Crawl reach.** 3,612 of 3,773 state department sites produced document links; the rest were unreachable or blocked. Sites that serve a CAPTCHA, WAF challenge or login were left alone, and a few JavaScript-only sites could not be listed.
- **Languages.** Names from Urdu, Manipuri (Meitei) and Mizo scripts are not handled; Hindi-only signature blocks that OCR poorly are missed.
- **Dates.** Many ministry documents have no reliable date; "last signed" can be blank or only a month.

## 9. Responsible use
All data come from public sources, but the compilation concentrates personal contact details of public servants (names, official phone numbers, email addresses, and, in the civil lists, cadre, batch and posting; date of birth and domicile are deliberately not included). Use the contact details for official enquiries about policy; do not use them for bulk marketing or profiling; verify the current post before contacting someone; open an issue to correct or remove an entry.
