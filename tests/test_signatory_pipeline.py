"""Stages of scripts/signatory_matrix.py on synthetic documents (no network, no poppler/tesseract)."""
import json
import subprocess
import types

import pandas as pd
import pytest

from helpers import read, write_csv, write_gz_csv

DOC_COLS = ["ministry", "title", "group", "category", "url", "date", "source", "slug"]


@pytest.fixture
def S(load):
    m = load("signatory_matrix")
    m._WORDS = set()
    return m


@pytest.fixture
def docs(repo):
    rows = [
        dict(ministry="Ministry of Finance", title="Office Order on transfer of officers", group="g", category="c",
             url="https://fin.gov.in/a.pdf", date="2024-03-01", source="api,<t>"),
        dict(ministry="Ministry of Finance", title="Scheme guidelines for PLI", group="g", category="c",
             url="https://fin.gov.in/b.pdf", date="2024-05-01"),
        dict(ministry="Ministry of Finance", title="Scheme guidelines for PLI", group="g", category="c",
             url="https://fin.gov.in/b.pdf", date="2024-05-01"),                                  # duplicate url
        dict(ministry="Ministry of Finance", title="Press note", group="g", category="c", url="https://fin.gov.in/c.pdf", date="2024-01-01"),
        dict(ministry="Ministry of Finance", title="Circular", group="g", category="c", url="https://fin.gov.in/d.html", date="2024-01-01"),
        dict(ministry="Ministry of Other", title="Notification of rules", group="g", category="c", url="https://oth.gov.in/e.pdf", date="2023-01-01"),
        dict(ministry="Ministry of Other", title="Order two", group="g", category="c", url="https://oth.gov.in/f.pdf", date="2023-02-01"),
        dict(ministry="Ministry of Other", title="Order three", group="g", category="c", url="https://oth.gov.in/g.pdf", date="2023-03-01"),
    ]
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz", rows, DOC_COLS)
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry="Ministry of Finance", website="w", division="Policy Division", name="Amit Kumar", designation="Joint Secretary",
             room="1", phones="2", email="amit@gov.in", source_url="u"),
        dict(ministry="Ministry of Finance", website="w", division="", name="Bina Rao", designation="Director", room="", phones="", email="", source_url="u"),
    ])
    return rows


def test_select_filters_prioritises_and_dedups(S, docs, repo, capsys):
    S.select()
    c = read(repo / "data/signatories/candidates.csv")
    assert list(c.columns[:2]) == ["doc_id", "ministry"]
    # only ministries with a roster; only order-ish titles with .pdf urls; duplicate url dropped
    assert set(c.url) == {"https://fin.gov.in/a.pdf", "https://fin.gov.in/b.pdf"}
    # policy/incentive documents first
    assert list(c.url)[0] == "https://fin.gov.in/b.pdf"
    assert not ({"source", "slug"} & set(c.columns))
    assert (c.host == "fin.gov.in").all()
    assert c.doc_id.tolist() == [S.doc_id(u) for u in c.url]
    assert "select: 2 candidate PDFs across 1 ministries, 1 hosts" in capsys.readouterr().out


def test_select_keeps_earlier_selection_and_all_ministries_flag(S, docs, repo):
    S.select()
    # a later run with a new document keeps the earlier selection (dedup by url)
    write_gz_csv(repo / "ministry_documents/data/all_documents.csv.gz",
                 [dict(ministry="Ministry of Finance", title="Order new", group="", category="", url="https://fin.gov.in/new.pdf", date="2025-01-01")], DOC_COLS)
    S.select()
    assert set(read(repo / "data/signatories/candidates.csv").url) == {"https://fin.gov.in/a.pdf", "https://fin.gov.in/b.pdf", "https://fin.gov.in/new.pdf"}


def test_select_all_ministries_and_per_ministry_cap(S, docs, repo):
    S.ALL_MINISTRIES = True
    S.PER_MINISTRY_CAP = 1
    S.select()
    c = read(repo / "data/signatories/candidates.csv")
    # Finance (has a roster) keeps everything; 'Ministry of Other' is capped at its newest document
    assert set(c[c.ministry == "Ministry of Other"].url) == {"https://oth.gov.in/g.pdf"}
    assert len(c[c.ministry == "Ministry of Finance"]) == 2


def test_curl_success_and_failures(S, repo, monkeypatch):
    dest = repo / "x.pdf"

    def fake_run(cmd, capture_output, text):
        tmp = cmd[cmd.index("-o") + 1]
        assert "--max-filesize" in cmd and "-A" in cmd and cmd[-1] == "http://u"
        data = fake_run.data
        if data is not None:
            open(tmp, "wb").write(data)
        return types.SimpleNamespace(stdout=fake_run.out, stderr=fake_run.err)
    monkeypatch.setattr(S.subprocess, "run", fake_run)
    fake_run.data, fake_run.out, fake_run.err = b"%PDF-1.4 body", "200 application/pdf", ""
    assert S._curl("http://u", dest) == ("200", "application/pdf", True, "")
    assert dest.read_bytes().startswith(b"%PDF") and not dest.with_suffix(".part").exists()
    dest.unlink()
    fake_run.data = b"<html>not a pdf</html>"            # 200 but not a PDF
    code, ctype, ok, err = S._curl("http://u", dest)
    assert (code, ok) == ("200", False) and not dest.exists() and not dest.with_suffix(".part").exists()
    fake_run.data, fake_run.out, fake_run.err = b"%PDF", "404 text/html", "x" * 500
    code, ctype, ok, err = S._curl("http://u", dest)
    assert (code, ok, len(err)) == ("404", False, 200)
    fake_run.data, fake_run.out = b"", "200 application/pdf"      # empty body
    assert S._curl("http://u", dest)[2] is False
    fake_run.data = None                                          # curl wrote nothing
    assert S._curl("http://u", dest)[2] is False


def test_fetch_downloads_per_host_and_logs(S, docs, repo, monkeypatch, capsys):
    S.select()
    monkeypatch.setattr(S.time, "sleep", lambda s: None)
    calls = []

    def fake_curl(url, dest):
        calls.append(url)
        if url.endswith("a.pdf"):
            raise RuntimeError("boom")
        dest.write_bytes(b"%PDF")
        return "200", "application/pdf", True, ""
    monkeypatch.setattr(S, "_curl", fake_curl)
    S.fetch()
    log = read(repo / "data/signatories/fetch_log.csv")
    assert sorted(log.columns) == sorted(["doc_id", "url", "http", "content_type", "ok", "err", "ts"])
    by = log.set_index("url")
    assert by.loc["https://fin.gov.in/a.pdf", "http"] == "exc" and by.loc["https://fin.gov.in/a.pdf", "ok"] == 0
    assert "boom" in by.loc["https://fin.gov.in/a.pdf", "err"]
    assert by.loc["https://fin.gov.in/b.pdf", "ok"] == 1
    assert "fin.gov.in: 1 ok" in capsys.readouterr().out
    # second run: everything attempted or present is skipped; the header is not duplicated
    calls.clear()
    S.fetch()
    assert calls == []
    assert len(read(repo / "data/signatories/fetch_log.csv")) == 2


def test_fetch_splits_busy_hosts_in_two_workers(S, repo, monkeypatch):
    rows = [dict(doc_id=f"d{i:03d}", ministry="M", url=f"https://h.gov.in/{i}.pdf", host="h.gov.in") for i in range(101)]
    write_csv(repo / "data/signatories/candidates.csv", rows)
    monkeypatch.setattr(S.time, "sleep", lambda s: None)
    got = []
    monkeypatch.setattr(S, "_curl", lambda url, dest: (got.append(url), dest.write_bytes(b"%PDF"), ("200", "", True, ""))[2])
    S.fetch()
    assert sorted(got) == sorted(r["url"] for r in rows)


# ------------------------------------------------------------------ pdf text
def test_pdf_text_uses_and_writes_json_cache(S, repo, monkeypatch):
    pdf = repo / "data/signatories/pdf/abc.pdf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.write_bytes(b"%PDF")
    cache = repo / "data/signatories/text/abc.json"
    calls = []

    def fake_inner(path, pages_tail=2):
        calls.append(path)
        S.pdf_text.last_ocr = True
        return 4, "HEAD", "TAIL"
    monkeypatch.setattr(S, "_pdf_text", fake_inner)
    assert S.pdf_text(pdf) == (4, "HEAD", "TAIL")
    assert json.loads(cache.read_text()) == {"n": 4, "head": "HEAD", "tail": "TAIL", "ocr": True}
    S.pdf_text.last_ocr = False
    assert S.pdf_text(pdf) == (4, "HEAD", "TAIL") and len(calls) == 1 and S.pdf_text.last_ocr is True    # served from cache
    cache.write_text("{broken")                                                                          # corrupt cache -> recompute
    assert S.pdf_text(pdf) == (4, "HEAD", "TAIL") and len(calls) == 2


def test_pdf_text_tolerates_unwritable_cache(S, repo, monkeypatch):
    pdf = repo / "data/signatories/pdf/abc.pdf"
    monkeypatch.setattr(S, "_pdf_text", lambda p, t=2: (1, "h", "t"))
    S.pdf_text.last_ocr = False
    (repo / "data/signatories/text").write_text("a file, not a directory")     # mkdir/write_text will fail
    assert S.pdf_text(pdf) == (1, "h", "t")


def _fake_poppler(monkeypatch, S, pdfinfo="Pages: 5\n", texts=None, ocr=None):
    texts = texts or {}
    log = []

    def run(cmd, capture_output=True, text=True, timeout=None):
        log.append(cmd)
        if cmd[0] == "pdfinfo":
            if isinstance(pdfinfo, Exception):
                raise pdfinfo
            return types.SimpleNamespace(stdout=pdfinfo)
        if cmd[0] == "pdftotext":
            first = cmd[cmd.index("-f") + 1]
            return types.SimpleNamespace(stdout=texts.get(first, ""))
        raise AssertionError(cmd)
    monkeypatch.setattr(S.subprocess, "run", run)
    return log


def test__pdf_text_head_and_tail_pages(S, monkeypatch):
    log = _fake_poppler(monkeypatch, S, "Pages: 5\n", {"1": "H" * 100, "4": "T" * 100})
    n, head, tail = S._pdf_text("x.pdf")
    assert (n, head, tail) == (5, "H" * 100, "T" * 100) and S.pdf_text.last_ocr is False
    assert ["-f", "1", "-l", "2"] == log[1][2:6] and ["-f", "4", "-l", "5"] == log[2][2:6]


def test__pdf_text_short_documents_reuse_head_for_tail(S, monkeypatch):
    _fake_poppler(monkeypatch, S, "Pages: 2\n", {"1": "ZZ" * 60})
    n, head, tail = S._pdf_text("x.pdf")
    assert n == 2 and head == tail == "ZZ" * 60


def test__pdf_text_pdfinfo_failure_defaults_to_one_page_and_strips_zero_width(S, monkeypatch):
    _fake_poppler(monkeypatch, S, RuntimeError("no pdfinfo"), {"1": "ab‌‍cd " * 30})
    n, head, tail = S._pdf_text("x.pdf")
    assert n == 1 and "‌" not in head and "‍" not in tail
    _fake_poppler(monkeypatch, S, "garbage without pages", {"1": "x" * 100})
    assert S._pdf_text("x.pdf")[0] == 1


def test__pdf_text_ocr_fallback_for_scanned_pdfs(S, monkeypatch):
    _fake_poppler(monkeypatch, S, "Pages: 3\n", {})
    calls = []
    monkeypatch.setattr(S, "ocr_pages", lambda p, a, b: (calls.append((a, b)), f"ocr{a}-{b}")[1])
    n, head, tail = S._pdf_text("x.pdf")
    assert S.pdf_text.last_ocr is True and (head, tail) == ("ocr1-1", "ocr3-3") and calls == [(1, 1), (3, 3)]
    # single-page scan: the tail is the head; >60 pages are never OCRed
    _fake_poppler(monkeypatch, S, "Pages: 1\n", {})
    assert S._pdf_text("x.pdf")[1:] == ("ocr1-1", "ocr1-1")
    _fake_poppler(monkeypatch, S, "Pages: 61\n", {})
    S._pdf_text("x.pdf")
    assert S.pdf_text.last_ocr is False
    # OCR returning nothing keeps whatever poppler produced
    _fake_poppler(monkeypatch, S, "Pages: 3\n", {"1": "a", "2": "b"})
    monkeypatch.setattr(S, "ocr_pages", lambda p, a, b: "")
    assert S._pdf_text("x.pdf")[1:] == ("a", "b")


def test_ocr_pages_runs_tesseract_per_rendered_image(S, monkeypatch):
    seen = []

    def run(cmd, capture_output=True, text=True, timeout=None):
        seen.append(cmd)
        if cmd[0] == "pdftoppm":
            prefix = cmd[-1]
            for n in ("p-1.pgm", "p-2.pgm"):
                open(prefix.rsplit("/", 1)[0] + "/" + n, "wb").write(b"x")
            return types.SimpleNamespace(stdout="")
        return types.SimpleNamespace(stdout="text of " + cmd[1].rsplit("/", 1)[1])
    monkeypatch.setattr(S.subprocess, "run", run)
    S.OCR_LANG = "hin+eng"
    out = S.ocr_pages("x.pdf", 2, 3)
    assert out == "text of p-1.pgm\ntext of p-2.pgm"
    assert seen[0][:8] == ["pdftoppm", "-r", "200", "-gray", "-f", "2", "-l", "3"]
    assert seen[1][2:4] == ["-", "-l"] and seen[1][4] == "hin+eng"
    monkeypatch.setattr(S.subprocess, "run", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError("no tesseract")))
    assert S.ocr_pages("x.pdf", 1, 1) == ""


# ------------------------------------------------------------------ extract
SIGNED_TAIL = "Order text\nSd/-\n(Amit Kumar)\nUnder Secretary to the Government of India\nTel: 011-23012345 amit@gov.in\n"


@pytest.fixture
def extracted(S, docs, repo, monkeypatch):
    S.select()
    c = read(repo / "data/signatories/candidates.csv").set_index("url")
    a, b = c.loc["https://fin.gov.in/a.pdf", "doc_id"], c.loc["https://fin.gov.in/b.pdf", "doc_id"]
    pdfdir = repo / "data/signatories/pdf"
    pdfdir.mkdir(parents=True, exist_ok=True)
    for d in (a, b, "stranger"):
        (pdfdir / f"{d}.pdf").write_bytes(b"%PDF")
    texts = {
        a: (3, "No. F.12/34-AB/2024   dated 01.03.2024\nSubject: Transfer of officers\n\nSir,\n" + "body text " * 10, SIGNED_TAIL),
        b: (1, "digitally signed by Rohit Verma\nDate: 2024", "no block here"),
    }

    def fake_pdf_text(path, pages_tail=2):
        S.pdf_text.last_ocr = False
        return texts[path.stem]
    monkeypatch.setattr(S, "pdf_text", fake_pdf_text)
    fake_pdf_text.last_ocr = False
    S.pdf_text = fake_pdf_text
    S.extract()
    return a, b


def test_extract_rows(S, extracted, repo):
    a, b = extracted
    s = read(repo / "data/signatories/signatures.csv").set_index("doc_id")
    assert "stranger" not in s.index                                  # PDFs not in candidates are ignored
    ra = s.loc[a]
    assert (ra.sig_rank, ra.signatory, ra.sig_designation) == (1, "Amit Kumar", "Under Secretary to the Government of India")
    assert ra.sig_email == "amit@gov.in" and ra.sig_phone == "011-23012345" and ra.strength == 7
    assert ra.subject == "Transfer of officers" and ra.file_number.startswith("F.12/34-AB/2024")
    assert ra.pages == 3 and ra.scanned == 0 and ra.ocr == 0
    rb = s.loc[b]
    assert (rb.sig_rank, rb.signatory, rb.sig_designation, rb.strength) == (1, "Rohit Verma", "(digital signature only)", 2)
    assert rb.digital_signer == "Rohit Verma"


def test_extract_unsigned_document_gets_rank_zero_and_scanned_flag(S, docs, repo, monkeypatch):
    S.select()
    d = read(repo / "data/signatories/candidates.csv").doc_id.iloc[0]
    (repo / "data/signatories/pdf").mkdir(parents=True, exist_ok=True)
    (repo / f"data/signatories/pdf/{d}.pdf").write_bytes(b"%PDF")

    def fake(path, pages_tail=2):
        fake.last_ocr = False
        return 1, "  ", "nothing"
    monkeypatch.setattr(S, "pdf_text", fake)
    S.extract()
    r = read(repo / "data/signatories/signatures.csv").iloc[0]
    assert (r.sig_rank, r.scanned, r.ocr) == (0, 1, 0) and pd.isna(r.signatory)


def test_extract_is_incremental(S, extracted, repo, monkeypatch):
    a, b = extracted
    calls = []
    monkeypatch.setattr(S, "pdf_text", lambda path, pages_tail=2: calls.append(path) or (1, "", ""))
    S.pdf_text.last_ocr = False
    S.extract()
    assert calls == []                                # everything already done
    assert len(read(repo / "data/signatories/signatures.csv")) == 2


def test_extract_keeps_top3_signers_latest_first(S, docs, repo, monkeypatch):
    S.select()
    d = read(repo / "data/signatories/candidates.csv").doc_id.iloc[0]
    (repo / "data/signatories/pdf").mkdir(parents=True, exist_ok=True)
    (repo / f"data/signatories/pdf/{d}.pdf").write_bytes(b"%PDF")
    tail = "".join(f"(Person{c} Name{c})\nDirector\n\n" for c in "ABCD")

    def fake(path, pages_tail=2):
        fake.last_ocr = True
        return 2, "head text " * 20, tail
    monkeypatch.setattr(S, "pdf_text", fake)
    S.extract()
    s = read(repo / "data/signatories/signatures.csv")
    assert list(s.sig_rank) == [1, 2, 3] and list(s.signatory)[0].endswith("D") and list(s.signatory)[2].endswith("B")
    assert set(s.ocr) == {1}


# ------------------------------------------------------------------ directory / match / matrix
SIG_COLS = ["doc_id", "sig_rank", "signatory", "sig_designation", "subject", "file_number", "scanned", "sig_email", "sig_phone"]
CAND_COLS = ["doc_id", "ministry", "title", "group", "category", "date", "url", "host"]


@pytest.fixture
def matched_env(S, repo):
    """Candidates + signatures + rosters for three documents; rosters contain the signers (and decoys)."""
    write_csv(repo / "data/signatories/candidates.csv", [
        dict(doc_id="d1", ministry="Ministry of Finance", title="Transfer and posting order", group="g", category="c", date="2024-03-01", url="https://f/1.pdf", host="f"),
        dict(doc_id="d2", ministry="Ministry of Finance", title="Scheme guidelines for tender", group="g", category="c", date="2024-05-01", url="https://f/2.pdf", host="f"),
        dict(doc_id="d3", ministry="Ministry of Health", title="Order", group="g", category="c", date="2023-05-01", url="https://h/3.pdf", host="h"),
        dict(doc_id="d4", ministry="Ministry of Health", title="Order", group="g", category="c", date="2023-06-01", url="https://h/4.pdf", host="h"),
    ], CAND_COLS)
    write_csv(repo / "data/signatories/signatures.csv", [
        dict(doc_id="d1", sig_rank=1, signatory="Amit Kumar", sig_designation="Joint Secretary", subject="Transfer of officers", file_number="F1", scanned=0, sig_email="amit@gov.in", sig_phone="2301"),
        dict(doc_id="d2", sig_rank=1, signatory="Amit Kumar", sig_designation="Jt. Secy", subject="Tender", file_number="F2", scanned=0),
        dict(doc_id="d2", sig_rank=2, signatory="Zed Quill", sig_designation="Director", subject="Tender", file_number="F2", scanned=0),
        dict(doc_id="d3", sig_rank=1, signatory="Rohit Sharma", sig_designation="Under Secretary", subject="", file_number="", scanned=0),
        dict(doc_id="d4", sig_rank=0, signatory="", sig_designation="", subject="", file_number="", scanned=1),
    ], SIG_COLS)
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry="Ministry of Finance", website="w", division="Policy", name="Amit Kumar", designation="Joint Secretary", room="1", phones="2", email="amit@gov.in", source_url="u"),
        dict(ministry="Ministry of Finance", website="w", division="Policy", name="Zed Quill", designation="Secretary", room="1", phones="2", email="zq@gov.in", source_url="u"),
        dict(ministry="Ministry of Health", website="w", division="", name="Rohit Sharma", designation="Director", room="", phones="", email="", source_url="u"),
        dict(ministry="Ministry of Health", website="w", division="", name="vacant", designation="", room="", phones="", email="", source_url="u"),
    ])
    write_csv(repo / "data/officials.csv", [
        dict(org_name="Ministry of Health", name="Rohit Sharma", designation="Under Secretary", division="", phones="", email="rs@nic.in", igod_org_id="9"),
    ])
    write_csv(repo / "data/ias_officers.csv", [
        dict(name_en="Amit Kumar", current_posting="Joint Secretary, Ministry of Finance, New Delhi", er_sheet_url="http://er"),
        dict(name_en="Amit Kumar", current_posting="Collector, Pune", er_sheet_url="http://er2"),
    ])
    return repo


def test_load_rosters_unions_cleans_and_ids(S, matched_env):
    r = S.load_rosters()
    assert set(r.roster) == {"ministry_whoswho", "igod_officials", "ias_civil_list"}
    assert "vacant" not in set(r.name_clean.str.lower())                 # placeholder rows removed
    assert r.officer_id.is_unique and r.officer_id.str.len().eq(10).all()
    igod = r[r.roster == "igod_officials"].iloc[0]
    assert igod.source_url == "https://igod.gov.in/organization/9" and igod.ministry == "Ministry of Health"
    ias = r[r.roster == "ias_civil_list"]
    assert set(ias.ministry) == {"Joint Secretary, Ministry of Finance, New Delhi", "Collector, Pune"}
    # no ips file is fine
    assert r.index.tolist() == list(range(len(r)))


def test_match_confidence_levels_and_state_posted_ias_excluded(S, matched_env, repo, capsys):
    S.match()
    ns = read(repo / "data/signatories/notification_signatories.csv")
    assert (repo / "data/signatories/roster_union.csv").exists()
    d1 = ns[(ns.doc_id == "d1") & (ns.sig_rank == 1)].iloc[0]
    assert (d1.match_status, d1.confidence, d1.roster) == ("matched", "high", "ministry_whoswho")
    assert d1.same_ministry == 1 and d1.desig_match == 1 and d1.officer_email == "amit@gov.in"
    assert d1.subject == "Transfer of officers" and d1.title == "Transfer and posting order"
    # Zed Quill is a Secretary in the roster but signed as Director: |rank gap| = 3 >= 2 -> rejected, not matched
    zq = ns[ns.signatory == "Zed Quill"].iloc[0]
    assert zq.match_status == "unmatched" and pd.isna(zq.officer_id)
    # the IAS officer posted as a Collector in Pune is never matched to a union-ministry order
    assert "Collector, Pune" not in set(ns.officer_ministry.dropna())
    # name matches in another table row: Rohit Sharma matched in Health (igod roster + whoswho roster)
    rs = ns[ns.signatory == "Rohit Sharma"].iloc[0]
    assert rs.match_status == "matched" and rs.confidence in ("high", "medium") and rs.same_ministry == 1
    # sig_rank 0 rows are not part of the output
    assert "d4" not in set(ns.doc_id)
    out = capsys.readouterr().out
    assert "roster union" in out and "matched" in out


def test_match_unmatched_when_name_unknown_and_other_ministry_is_low(S, matched_env, repo):
    sig = read(repo / "data/signatories/signatures.csv")
    extra = pd.DataFrame([
        dict(doc_id="d1", sig_rank=2, signatory="Nobody Known", sig_designation="Director", subject="", file_number="", scanned=0),
        dict(doc_id="d3", sig_rank=2, signatory="Amit Kumar", sig_designation="", subject="", file_number="", scanned=0),
    ])
    pd.concat([sig, extra]).to_csv(repo / "data/signatories/signatures.csv", index=False)
    S.match()
    ns = read(repo / "data/signatories/notification_signatories.csv")
    nk = ns[ns.signatory == "Nobody Known"].iloc[0]
    assert nk.match_status == "unmatched" and nk.name_score == 0 and pd.isna(nk.confidence) or nk.confidence == ""
    other = ns[(ns.doc_id == "d3") & (ns.signatory == "Amit Kumar")].iloc[0]
    # two-token exact name in a different ministry: needs >= 3 tokens for 'low' -> rejected as weak
    assert other.match_status == "unmatched" and str(other.confidence).startswith("rejected (weak")


def test_directory_aggregates_signers_with_match_info(S, matched_env, repo, capsys):
    S.match()
    S.directory()
    d = read(repo / "data/signatories/signatory_directory.csv")
    amit = d[(d.ministry == "Ministry of Finance") & (d.signatory == "Amit Kumar")].iloc[0]
    assert amit.n_documents == 2 and amit.first_date == "2024-03-01" and amit.last_date == "2024-05-01"
    assert amit.email == "amit@gov.in" and str(amit.phone).startswith("2301")
    assert amit.roster_match == "Amit Kumar" and amit.match_confidence == "high"
    assert "Joint Secretary" in amit.designations
    assert "HR: appointment / transfer / posting / promotion" in amit.topics
    assert amit.example_titles.count("||") == 1 and amit.document_urls.split() == ["https://f/2.pdf", "https://f/1.pdf"]
    # signers are sorted by ministry then document count
    assert list(d.ministry) == sorted(d.ministry)
    out = capsys.readouterr().out
    assert "directory: " in out and "distinct signers" in out


def test_directory_without_match_file_and_short_names(S, repo):
    write_csv(repo / "data/signatories/candidates.csv", [
        dict(doc_id="d1", ministry="M", title="T", group="", category="", date="", url="u", host="h")], CAND_COLS)
    write_csv(repo / "data/signatories/signatures.csv", [
        dict(doc_id="d1", sig_rank=1, signatory="Al Bo", sig_designation="(digital signature only)", subject="", scanned=0),
        dict(doc_id="d1", sig_rank=1, signatory="X Y", sig_designation="", subject="", scanned=0)], SIG_COLS)
    S.directory()
    d = read(repo / "data/signatories/signatory_directory.csv")
    assert list(d.signatory) == ["Al Bo"]                  # 'X Y' -> name_key 'x y' (3 chars) is too short
    assert pd.isna(d.designations.iloc[0]) and pd.isna(d.roster_match.iloc[0])


def test_matrix_writes_outputs_and_report(S, matched_env, repo, capsys):
    S.match()
    S.matrix()
    mx = read(repo / "data/signatories/officer_topic_matrix.csv")
    assert {"officer_id", "officer_name", "topic", "n_documents", "doc_ids", "confidence"} <= set(mx.columns)
    amit = mx[mx.officer_name == "Amit Kumar"]
    assert set(amit.topic) >= {"HR: appointment / transfer / posting / promotion"}
    assert (amit.n_documents >= 1).all()
    piv = read(repo / "data/signatories/officer_topic_pivot.csv")
    assert "TOTAL" in piv.columns and piv.TOTAL.is_monotonic_decreasing
    docs = read(repo / "data/signatories/officer_documents.csv")
    assert "topics" in docs.columns and set(docs.match_status) == {"matched"}
    md = (repo / "data/signatories/SIGNATORY_MATRIX.md").read_text()
    for h in ("# Who signed what", "## Funnel", "## Per ministry", "## Officer × topic matrix", "## Contact person by topic",
              "## Signatories missing from the rosters", "## Caveats"):
        assert h in md
    assert "| Ministry of Finance |" in md and "**Amit Kumar**" in md
    assert "matrix: " in capsys.readouterr().out


def test_matrix_roster_gap_section_lists_repeat_unmatched_signers(S, matched_env, repo):
    sig = read(repo / "data/signatories/signatures.csv")
    gap = pd.DataFrame([dict(doc_id=d, sig_rank=2, signatory="Gap Person", sig_designation="Director", subject="", file_number="", scanned=0) for d in ("d1", "d2")] +
                       [dict(doc_id="d3", sig_rank=2, signatory="Once Only", sig_designation="Director", subject="", file_number="", scanned=0)])
    pd.concat([sig, gap]).to_csv(repo / "data/signatories/signatures.csv", index=False)
    S.match()
    S.matrix()
    md = (repo / "data/signatories/SIGNATORY_MATRIX.md").read_text()
    assert "| Ministry of Finance | Gap Person | Director | 2 |" in md
    assert "Once Only" not in md                                   # a single document is not a roster gap


def test_matrix_with_no_matches_writes_empty_outputs(S, repo, capsys):
    write_csv(repo / "data/signatories/notification_signatories.csv", [
        dict(doc_id="d1", sig_rank=1, signatory="Nobody", match_status="unmatched", officer_id="")])
    S.matrix()
    assert read(repo / "data/signatories/officer_topic_matrix.csv").empty
    assert list(read(repo / "data/signatories/officer_documents.csv").columns) == ["doc_id", "sig_rank", "signatory", "match_status", "officer_id"]
    assert "No signatory could be matched" in (repo / "data/signatories/SIGNATORY_MATRIX.md").read_text()
    assert "no matches" in capsys.readouterr().out


def test_main_dispatch_runs_named_stage(repo, matched_env):
    from conftest import run_script
    g = run_script("signatory_matrix", ["match"])
    assert (repo / "data/signatories/notification_signatories.csv").exists()
