# Markdown corpus — Indian government orders, notifications, circulars and guidelines

40,708 PDFs from 70 union ministry/department sites and 36 state/UT government sites, converted to markdown
(547,273 pages, about 597 million characters). Produced by `scripts/shards_to_md.py` / `scripts/cloud_md_worker.py`.

## Layout
`md/<tree>/<tree>-NNN.md.zip` — one zip per shard of about 1,000 documents (centre) or 100–500 (states). `<tree>` is
`data__signatories__pdf` (union ministries) or `data__states__<ST>__pdf` (state code, e.g. `UP`, `TN`).
Each zip contains `<doc_id>.md` (one per document) and `index.jsonl` (one JSON line per document).

## A markdown file
```
---
doc_id: "22b783740c86ac0f"
source_url: "https://…/Order_JointInspection.pdf"
ministry: "Labour, Employment & Training Department, Andaman & Nicobar"
title: "Order for Joint Inspection under all Labour Acts"
date: ""
pages: 2
method: "tesseract:eng+hin"      # or "pdftotext" (text layer)
script: "LATIN"                  # dominant script of the text
needs_ocr: false                 # true = no text could be read (332 documents, 0.8%)
sha1: "923b9231f4f75df3"
---

<!-- page 1 -->
…text in reading order…
```
Scanned documents were read with Tesseract in the state's language(s) (up to 10 pages each); Hindi/Indic text is kept in its own script.

## Index
`../data/md_index.csv.gz` has one row per document: tree, shard, doc_id, source_url, ministry, title, date, pages, chars, bytes, sha1,
method, script, needs_ocr, error. Join it to `data/signatories/signatory_directory.csv`, `data/states/notification_signatories_all_states.csv`
and `data/policy_contacts_from_documents.csv` to go from a document to the officials who signed it.

## Read it
```python
import zipfile, json
z = zipfile.ZipFile("corpus/md/data__states__TN__pdf/data__states__TN__pdf-001.md.zip")
rows = [json.loads(l) for l in z.read("index.jsonl").decode().splitlines()]
text = z.read(rows[0]["doc_id"] + ".md").decode()
```

## Provenance and limits
Every document was downloaded from the public website named in `source_url`; the PDFs themselves are in the cloud archive (not in git).
OCR quality varies on poor scans; names and numbers should be checked against the source PDF before being relied on.
