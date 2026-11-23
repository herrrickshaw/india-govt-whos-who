"""scripts/policy_contact_linker.py"""
import pandas as pd
import pytest

from helpers import read, write_csv


@pytest.fixture
def K(load):
    m = load("policy_contact_linker")
    m.S._WORDS = set()
    return m


def _docs(rows):
    return pd.DataFrame(rows)


def test_instr_key_drops_stopwords_short_tokens(K):
    assert K.instr_key("The PM Kisan Samman Nidhi Scheme 2024") == "kisan samman nidhi"
    assert K.instr_key("A of to") == ""
    assert K.instr_key(None) == "none"                                    # str(None) is tokenised like any other word


def test_instruments_from_titles_needs_two_documents_and_picks_common_label(K):
    docs = _docs([
        dict(doc_id="1", title="Guidelines of Rooftop Solar Programme", subject=""),
        dict(doc_id="2", title="Amendment to Rooftop Solar Programme dated 1.1.2024", subject=""),
        dict(doc_id="3", title="Pradhan Mantri Kisan Sampada Yojana approved", subject=""),
        dict(doc_id="4", title="Other note on PM Dhan-Dhaanya Krishi Yojana", subject="http://x www.y 12345"),
        dict(doc_id="5", title="Production Linked Incentive Scheme for Textiles - revised", subject=""),
        dict(doc_id="6", title="Production Linked Incentive Scheme for Textiles - extended", subject=""),
        dict(doc_id="7", title="Tender notice only", subject=""),
    ])
    rows = K.instruments_from_titles(docs)
    keys = {r["key"]: r for r in rows}
    assert any("rooftop solar" in k for k in keys)
    solar = next(r for k, r in keys.items() if "rooftop solar" in k)
    assert solar["n_docs"] == 2 and solar["doc_ids"] == {"1", "2"} and solar["source"] == "documents"
    assert any("textiles" in k for k in keys)                             # PLI pattern found in two documents
    assert not any("sampada" in k for k in keys)                          # only one document -> dropped


def test_instruments_from_titles_ignores_urls_and_long_numbers(K):
    docs = _docs([dict(doc_id=str(i), title="See Scheme page http://x.in/Quick Start Scheme 123456", subject="") for i in range(3)])
    assert [r for r in K.instruments_from_titles(docs) if "http" in r["instrument"]] == []


def test_curated_instruments_merges_sources_and_dedups(K, repo):
    write_csv(repo / "data/policy_windows.csv", [
        dict(instrument="Production Linked Incentive (PLI) for Electronics", offering_entity="MeitY"),
        dict(instrument="Kerala Startup Mission", offering_entity="Kerala Department of Industries"),
        dict(instrument="XY", offering_entity=""),
    ])
    write_csv(repo / "data/policy_contacts.csv", [dict(instrument="Production Linked Incentive (PLI) for Electronics", offering_entity="MeitY"),
                                                 dict(instrument="Tamil Nadu Industrial Policy", offering_entity="tn")])
    write_csv(repo / "data/discovered_instruments.csv", [dict(instrument="Semicon India Programme", ministry="MeitY"),
                                                         dict(instrument="Kerala Startup Mission", ministry="x")])
    rows = K.curated_instruments()
    by = {r["instrument"]: r for r in rows}
    assert "XY" not in by                                                   # key shorter than 4 characters
    pli = by["Production Linked Incentive (PLI) for Electronics"]
    assert pli["source"] == "curated" and "PLI" in pli["acronyms"] and pli["state"] is None
    assert by["Kerala Startup Mission"]["state"] == "KL"                     # derived from the offering entity
    assert by["Kerala Startup Mission"]["source"] == "curated"               # curated wins over the discovered duplicate
    assert by["Tamil Nadu Industrial Policy"]["state"] == "TN"               # state taken from the instrument name
    assert by["Semicon India Programme"]["source"] == "pib/ministry-site" and by["Semicon India Programme"]["offering_entity"] == ["MeitY"]


def test_curated_instruments_no_files(K):
    assert K.curated_instruments() == []


def _ins(**kw):
    base = dict(instrument="X", key="solar rooftop", source="curated", acronyms=[], offering_entity=[], state=None)
    base.update(kw)
    return base


def test_match_curated_token_conjunction_and_state_scope(K):
    docs = _docs([
        dict(doc_id="1", title="Rooftop Solar Scheme guidelines", subject=None, level="centre"),
        dict(doc_id="2", title="Solar pumps", subject=None, level="centre"),
        dict(doc_id="3", title="Rooftop Solar subsidy", subject="", level="KL"),
    ])
    assert K.match_curated(_ins(), docs) == {"1", "3"}
    assert K.match_curated(_ins(state="KL"), docs) == {"3"}
    assert K.match_curated(_ins(state="ZZ"), docs) == set()
    assert K.match_curated(_ins(key="solar"), docs) == set()               # one distinctive token, no acronym -> nothing


def test_match_curated_acronyms(K):
    docs = _docs([dict(doc_id=str(i), title=t, level="centre") for i, t in enumerate(
        ["SAMARTH portal live", "samarth.gov update", "PLI for textiles", "Notice about tex PLI mission", "NIDHI funding", "nid note"])])
    # long acronym (>= 4) stands alone, as a whole word
    assert K.match_curated(_ins(key="x", acronyms=["SAMARTH"]), docs) == {"0", "1"}      # \\b also splits at "samarth.gov"
    # generic acronym (PLI) needs another distinctive token from the name
    assert K.match_curated(_ins(key="textiles incentive", acronyms=["PLI"]), docs) == {"2"}
    assert K.match_curated(_ins(key="pli", acronyms=["PLI"]), docs) == set()
    # 3-letter non-generic acronym with no other tokens stands alone
    docs2 = _docs([dict(doc_id="a", title="the ABC cell", level="centre"), dict(doc_id="b", title="abcd", level="centre")])
    assert K.match_curated(_ins(key="abc", acronyms=["ABC"]), docs2) == {"a"}
    # ...but needs a companion token when the name has others
    assert K.match_curated(_ins(key="textiles abc", acronyms=["ABC"]), docs2) == set()
    assert K.match_curated(_ins(key="textiles", acronyms=["ABC"]), _docs([dict(doc_id="c", title="abc textiles", level="centre")])) == {"c"}


def test_match_curated_too_generic_is_dropped(K):
    docs = _docs([dict(doc_id=str(i), title="Rooftop Solar order", level="centre") for i in range(60)])
    assert K.match_curated(_ins(), docs) == set()                        # > max(40, 3%) hits
    assert len(K.match_curated(_ins(), docs.head(40))) == 40              # exactly 40 is still fine
    assert K.match_curated(_ins(), docs.iloc[0:0]) == set()


# ------------------------------------------------------------------ end to end
@pytest.fixture
def world(repo):
    sig = "data/signatories"
    write_csv(repo / f"{sig}/candidates.csv", [
        dict(doc_id="c1", ministry="Ministry of Power", title="Rooftop Solar Programme guidelines", url="https://p/1.pdf", date="2024-03-01"),
        dict(doc_id="c2", ministry="Ministry of Power", title="Amendment to Rooftop Solar Programme", url="https://p/2.pdf", date="2024-06-01"),
        dict(doc_id="c3", ministry="Ministry of Power", title="Rooftop Solar Programme notice", url="https://p/3.pdf", date="1980-01-01"),
    ])
    write_csv(repo / f"{sig}/signatures.csv", [
        dict(doc_id="c1", sig_rank=1, signatory="Amit Kumar", sig_designation="Joint Secretary", subject="Solar guidelines", sig_email="amit@gov.in", sig_phone="011-2301"),
        dict(doc_id="c2", sig_rank=1, signatory="Amit Kumar", sig_designation="Joint Secretary", subject="Amendment", sig_email="", sig_phone=""),
        dict(doc_id="c2", sig_rank=2, signatory="Bina Rao", sig_designation="Director", subject="Amendment"),
        dict(doc_id="c3", sig_rank=0, signatory="", sig_designation="", subject=""),
    ])
    write_csv(repo / f"{sig}/signatory_directory.csv", [
        dict(ministry="Ministry of Power", signatory="Amit Kumar", roster_match="Amit Kumar", roster_designation="JS", roster_email="amit.roster@gov.in",
             latest_posting="Secretary", latest_posting_date="2025-01-01", moved_since_signing="yes")])
    write_csv(repo / "data/states/UP/candidates.csv", [dict(doc_id="s1", ministry="UP Dept", title="UP Rooftop Solar Programme order", url="https://up/1.pdf", date="2024-01-01"),
                                                      dict(doc_id="s2", ministry="UP Dept", title="Rooftop Solar Programme circular", url="https://up/2.pdf", date="2024-02-01")])
    write_csv(repo / "data/states/UP/signatures.csv", [dict(doc_id="s1", sig_rank=1, signatory="Sita Devi", sig_designation="Secretary", subject="x", level="UP"),
                                                       dict(doc_id="s2", sig_rank=1, signatory="Sita Devi", sig_designation="Secretary", subject="y")])
    (repo / "data/states/NOT_A_STATE").mkdir(parents=True)
    write_csv(repo / "data/states/NOT_A_STATE/candidates.csv", [dict(doc_id="z", ministry="x", title="t", url="u", date="")])
    write_csv(repo / "data/ministry_officials.csv", [
        dict(ministry="Ministry of Power", division="Rooftop Solar Division", name="Div Head", designation="Director", email="dh@gov.in", phones="22"),
        dict(ministry="Ministry of Power", division="Other", name="Other Person", designation="Director", email="", phones="")])
    write_csv(repo / "data/policy_windows.csv", [dict(instrument="Rooftop Solar Programme", offering_entity="Ministry of Power")])
    return repo


def test_load_centre_and_states(K, world):
    cand, sig, d = K.load_centre()
    assert set(cand.level) == {"centre"} and "subject" in cand.columns
    assert cand.set_index("doc_id").loc["c1", "subject"] == "Solar guidelines" and len(d) == 1
    c, s, dd = K.load_states()
    assert set(c.level) == {"UP"} and set(s.level) == {"UP"} and dd.empty           # 'NOT_A_STATE' directory is ignored
    assert set(c.doc_id) == {"s1", "s2"}


def test_load_without_optional_files(K, repo):
    write_csv(repo / "data/signatories/candidates.csv", [dict(doc_id="c1", ministry="M", title="t", url="u", date="")])
    cand, sig, d = K.load_centre()
    assert sig.empty and d.empty and "subject" in cand.columns
    assert [x.empty for x in K.load_states()] == [True, True, True]


def test_main_links_documents_signers_and_roster_divisions(K, world, repo, capsys):
    K.main()
    idx = read(repo / "data/policy_instruments_index.csv", keep_default_na=False)
    cur = idx[idx.instrument_source == "curated"]
    assert list(cur.instrument) == ["Rooftop Solar Programme"]
    r = cur.iloc[0]
    assert r.n_documents == 5 and r.ministry == "Ministry of Power" and r.n_contacts == 3
    assert r.first_date == "2024-01-01" and r.last_date == "2024-06-01"          # 1980 date is outside the accepted 1990-2029 window
    assert "Amit Kumar (Joint Secretary, amit@gov.in)" in r.top_contacts
    ci = read(repo / "data/policy_contacts_from_documents.csv", keep_default_na=False)
    amit = ci[(ci.contact == "Amit Kumar") & (ci.instrument == "Rooftop Solar Programme")].iloc[0]
    assert amit.n_documents_signed == 2 and amit.evidence == "signed documents" and amit.level == "centre"
    assert amit.email == "amit@gov.in" and amit.phone == "011-2301" and amit.last_signed == "2024-06-01"
    assert amit.roster_match == "Amit Kumar" and amit.latest_posting == "Secretary" and amit.moved_since_signing == "yes"
    assert set(amit.document_urls.split()) == {"https://p/1.pdf", "https://p/2.pdf"}      # order follows set iteration (hash-seed dependent)
    bina = ci[ci.contact.str.lower() == "bina rao"].iloc[0]
    assert bina.designation == "Director" and bina.email == ""
    div = ci[(ci.evidence == "roster division matches instrument") & (ci.instrument_source == "curated")]
    assert list(div.contact) == ["Div Head"] and div.iloc[0].email == "dh@gov.in"
    sita = ci[(ci.contact.str.lower() == "sita devi") & (ci.instrument_source == "curated")]
    assert len(sita) == 1 and (sita.level == "UP").all() and sita.iloc[0].n_documents_signed == 2
    md = (repo / "data/POLICY_CONTACTS.md").read_text()
    for h in ("# Policy & incentive contacts", "## Curated incentive instruments", "## Instruments discovered from document titles, by ministry", "## Caveats"):
        assert h in md
    assert "| Rooftop Solar Programme | Ministry of Power (centre) | 5 |" in md
    assert "linker: " in capsys.readouterr().out


def test_main_skips_instruments_without_matching_documents(K, world, repo):
    write_csv(repo / "data/policy_windows.csv", [dict(instrument="Zebra Crossing Initiative", offering_entity="x")])
    K.main()
    idx = read(repo / "data/policy_instruments_index.csv", keep_default_na=False)
    assert "Zebra Crossing Initiative" not in set(idx.instrument)
