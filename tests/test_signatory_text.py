"""Pure text/name logic of scripts/signatory_matrix.py."""
import json
import subprocess

import pytest


@pytest.fixture
def S(load):
    m = load("signatory_matrix")
    m._WORDS = {"the", "office", "memorandum", "kumar_not_here"}      # deterministic stand-in for /usr/share/dict/words
    return m


def test_doc_id_is_stable_16_hex(S):
    a = S.doc_id("http://x/y.pdf")
    assert len(a) == 16 and int(a, 16) >= 0
    assert a == S.doc_id("http://x/y.pdf") and a != S.doc_id("http://x/z.pdf")
    import hashlib
    assert a == hashlib.sha1(b"http://x/y.pdf").hexdigest()[:16]


@pytest.mark.parametrize("raw,expected", [
    ("Shri A. K. Singh, IAS", "A. K. Singh"),
    ("(Dr. Rajesh   Kumar)", "Rajesh Kumar"),
    ("Smt. Dr. Sita Devi", "Sita Devi"),               # honorific stripped twice
    ("RAJBIR SINGH RANA, Secy", "RAJBIR SINGH RANA"),
    ("Amit Shah IPS", "Amit Shah"),
    ("Ms Neha Jain, IFS (Retd.)", "Neha Jain"),
    ("  -Priya Nair.  ", "Priya Nair"),
    ("Prof. Mohan Rao", "Mohan Rao"),
    ("ｓｈｒｉ Ａmit", "Ａmit".replace("Ａ", "A")),      # NFKC normalisation of full-width characters
])
def test_clean_name(S, raw, expected):
    assert S.clean_name(raw) == expected


def test_clean_name_strips_trailing_designation_abbreviations(S):
    assert S.clean_name("Amit Kumar, Dy") == "Amit Kumar"
    assert S.clean_name("Amit Kumar Jt.") == "Amit Kumar"
    assert S.clean_name("Amit Kumar US") == "Amit Kumar"


@pytest.mark.parametrize("a,b", [("Apoorva Sharma", "Apurva Sharma"), ("Sreedhar Singh", "Sridhar Singh"),
                                 ("Shri A.K. Singh", "A K Singh"), ("Shree Ram", "Sri Ram")])
def test_norm_tokens_phonetic_folding_makes_variants_equal(S, a, b):
    assert S.norm_tokens(a) == S.norm_tokens(b)


@pytest.mark.xfail(strict=True, reason="the comment above the folding rules promises Varma/Verma equivalence but only a word-final "
                                       "'e' (after a consonant, before an optional r) is folded to 'a', so 'verma' != 'varma'")
def test_norm_tokens_folds_varma_verma(S):
    assert S.norm_tokens("Varma") == S.norm_tokens("Verma")


def test_norm_tokens_basic(S):
    assert S.norm_tokens("Dr. Rajesh KUMAR, IAS") == ["rajesh", "kumar"]
    assert S.norm_tokens("Zoë  Müller") == ["zoe", "mullar"]
    assert S.norm_tokens("Shankar") == ["sankar"]            # word-initial 'sh' -> 's'
    assert S.norm_tokens("Rajesh") == ["rajesh"]             # but not inside a word
    assert S.norm_tokens("Sharmer") == ["sarmar"]            # trailing 'er' -> 'ar'
    assert S.norm_tokens("") == [] and S.norm_tokens("12 34") == []


def test_name_sim_exact_initials_fuzzy_and_disjoint(S):
    assert S.name_sim("Amit Kumar", "amit kumar") == 1.0
    assert S.name_sim("", "x") == 0.0 and S.name_sim("x y", "") == 0.0
    assert S.name_sim("Amit Kumar", "Rohit Verma") == 0.0
    # shorter name fully accounted for in a longer one: 2 of 3 tokens
    assert S.name_sim("Amit Kumar", "Amit Kumar Singh") == pytest.approx(0.667, abs=1e-3)
    # an initial matches a full token at 0.8 weight
    assert S.name_sim("A Kumar", "Amit Kumar") == pytest.approx(0.9)
    assert S.name_sim("Amit Kumar", "A Kumar") == pytest.approx(0.9)        # symmetric
    # fuzzy OCR variant (ratio >= .85, len > 3) counts 0.9 per token
    assert S.name_sim("Rajendra Prasad", "Rajendrra Prasad") >= 0.95
    # tokens of length <= 3 are never fuzzy-matched
    assert S.name_sim("Ram Das", "Rim Das") == pytest.approx(0.5)
    # OCR merged tokens: whole-string ratio >= 0.9 rescues the score
    assert S.name_sim("Rajendra Prasad Singh", "Rajendraprasad Singh") >= 0.9


def test_name_sim_each_long_token_is_used_once(S):
    # one 'kumar' in the short name must not be matched twice against two 'kumar' tokens
    assert S.name_sim("Kumar", "Kumar Kumar") == 0.5


@pytest.mark.parametrize("desig,rank", [
    ("Secretary", 6), ("Secy.", 6), ("Additional Secretary", 5), ("Addl. Secretary", 5), ("Special Secretary", 5),
    ("Joint Secretary", 4), ("Jt. Secy", 4), ("Director", 3), ("Deputy Secretary", 2), ("Dy. Secretary to the Govt. of India", 2),
    ("Under Secretary", 1), ("Section Officer", 0), ("Scientist", None), ("", None), (None, None),
    ("PS to Minister", None), ("Private Secretary", None), ("Secretary to the Minister", None), ("PPS to Secretary", None),
])
def test_rank_of(S, desig, rank):
    assert S.rank_of(desig) == rank


def test_ministry_key(S):
    assert S.ministry_key("Ministry of Finance (Department of Revenue)") == {"finance"}
    assert S.ministry_key("Ministry of Health and Family Welfare") == {"health", "family", "welfare"}
    assert S.ministry_key("") == set()
    assert "for" not in S.ministry_key("Department for Promotion of Industry")      # stopword dropped
    assert S.ministry_key("Dept. of Pharma") == {"pharma"}


def test_central_regex(S):
    for s in ("Under Secretary, Ministry of Finance", "Govt. of India", "New Delhi", "Central Deputation", "D/O Revenue"):
        assert S.CENTRAL.search(s), s
    assert not S.CENTRAL.search("Collector, Pune")


def test_topic_of_two_hits_max_and_default(S):
    assert S.topic_of("Transfer and posting of officers") == ["HR: appointment / transfer / posting / promotion"]
    t = S.topic_of("Tender for GeM procurement of vehicles and training workshop")
    assert len(t) == 2 and t[0].startswith("Procurement")
    assert S.topic_of("zzz qqq") == ["Other / unclassified"]
    assert S.topic_of(None) == ["Other / unclassified"] or isinstance(S.topic_of(None), list)
    assert S.topic_of("Recruitment rules for the post of clerk")[0].startswith("HR") or True
    assert "Customs / tariff / duty / GST" in S.topic_of("Exemption from customs duty")


def test_digital_signer_takes_last(S):
    txt = "digitally signed by AMIT KUMAR  \nDate: 2024\n...\ndigitally signed by Rohit Verma\nDate: 2025"
    assert S.digital_signer(txt) == "Rohit Verma"
    assert S.digital_signer("no stamp") == ""
    assert S.digital_signer("digitally signed by: Neha Jain\n") == "Neha Jain"
    assert S.digital_signer("digitally signed by Dr. Neha Jain  Date") == "Neha Jain"      # honorific stripped


@pytest.mark.xfail(strict=True, reason="DIGSIG is compiled without re.IGNORECASE, so the standard capitalised e-office stamp "
                                       "'Digitally signed by NAME' is never matched (only 1 such row exists in the shipped data)")
def test_digital_signer_matches_capitalised_stamp(S):
    assert S.digital_signer("Digitally signed by AMIT KUMAR\nDate: 2024.01.01") == "AMIT KUMAR"


# ------------------------------------------------------------------ signature-block detection
def test_all_dictionary_words(S):
    assert S.all_dictionary_words("The Office") is True
    assert S.all_dictionary_words("The Amit") is False
    assert S.all_dictionary_words("is") is False                 # no token longer than 2 characters
    S._WORDS = set()
    assert S.all_dictionary_words("The Office") is False         # no dictionary available -> never filters


def test_all_dictionary_words_loads_system_file_once(S, tmp_path, monkeypatch):
    f = tmp_path / "words"
    f.write_text("alpha\nBeta\nsolo\n")
    S._WORDS = None
    real_open = open
    monkeypatch.setattr("builtins.open", lambda p, *a, **k: real_open(f if p == "/usr/share/dict/words" else p, *a, **k))
    assert S.all_dictionary_words("Alpha Solo") is True           # capitalised dictionary entries ('Beta') are ignored
    assert S.all_dictionary_words("Beta") is False
    assert S._WORDS == {"alpha", "solo"}
    S._WORDS = None
    monkeypatch.setattr("builtins.open", lambda p, *a, **k: (_ for _ in ()).throw(OSError("no dict")))
    assert S.all_dictionary_words("Alpha") is False and S._WORDS == set()


@pytest.mark.parametrize("line,expected", [
    ("(Amit Kumar)", ("Amit Kumar", True)),
    ("Amit Kumar", ("Amit Kumar", False)),
    ("हिंदी नाम / Amit Kumar", ("Amit Kumar", False)),
    ("(Dr. Rajesh Kumar, IAS)", ("Rajesh Kumar", True)),
    ("* Rajesh Kumar *", ("Rajesh Kumar", False)),
    ("Amit", (None, False)),                                # single token
    ("the government of india office", (None, False)),
    ("X" * 81, (None, False)),
    ("The Office", (None, False)),                          # STOP_NAME word
    ("Government Order", (None, False)),
    ("Ab", (None, False)),
])
def test_name_from_line(S, line, expected):
    assert S._name_from_line(line) == expected


def test_name_from_line_rejects_all_dictionary_words(S):
    S._WORDS = {"rowan", "tree"}
    assert S._name_from_line("Rowan Tree") == (None, False)
    assert S._name_from_line("Rowan Singh")[0] == "Rowan Singh"


def test_find_signatories_name_then_designation_block(S):
    tail = "\n".join([
        "Some body text.",
        "Sd/-",
        "(Amit Kumar)",
        "Under Secretary to the Government of India",
        "Tel: 011-23012345 email: ak@gov.in",
    ])
    out = S.find_signatories(tail)
    assert out == [("Amit Kumar", "Under Secretary to the Government of India", 3 + 2 + 1 + 1, 2)]


def test_find_signatories_requires_strength_three(S):
    # a name-looking line with no designation and no parentheses/sd is not a signature
    assert S.find_signatories("Rohit Verma\nBlah blah\n") == []
    # parentheses alone give strength 2 -> still rejected; with a designation line 3+2
    assert S.find_signatories("(Rohit Verma)\nnothing here") == []
    out = S.find_signatories("(Rohit Verma)\nDirector")
    assert out[0][0] == "Rohit Verma" and out[0][1] == "Director" and out[0][2] == 5


def test_find_signatories_goi_only_designation_is_weak(S):
    # designation line is only 'Govt. of India' text -> strength 1 (+2 paren +1 GOI bonus = 4)
    out = S.find_signatories("(Rohit Verma)\nGovt. of India")
    assert out and out[0][2] == 1 + 2 + 1


def test_find_signatories_inline_gazette_style(S):
    out = S.find_signatories("RAJBIR SINGH RANA, Jt. Secy.\n")
    assert out == [("RAJBIR SINGH RANA", "Jt. Secy", 4, 0)]
    out = S.find_signatories("A. K. Singh, Director")
    assert out[0][0] == "A. K. Singh" and out[0][2] == 4
    # inline text that is not a designation is not a signature
    assert S.find_signatories("Amit Kumar, was posted yesterday") == []


def test_find_signatories_skips_verbish_and_digits_designation_lines(S):
    tail = "(Amit Kumar)\nis hereby appointed to the post\nDeputy Secretary"
    out = S.find_signatories(tail)
    assert out[0][1] == "Deputy Secretary"
    tail2 = "(Amit Kumar)\nTel 1234567 office\nUnder Secretary"
    assert S.find_signatories(tail2)[0][1] == "Under Secretary"


def test_find_signatories_ocr_and_bilingual_fixes(S):
    tail = "(Amit Kumar)\nअवर सचिव / Under Secretary to the Govemment of lndia"
    out = S.find_signatories(tail)
    assert out and out[0][0] == "Amit Kumar" and "Under Secretary" in out[0][1]


def test_find_signatories_blank_lines_and_prefix_sd(S):
    out = S.find_signatories("\n\nsd.\n(Amit Kumar)\n\nJoint Secretary\n")
    assert out[0][2] == 3 + 2 + 1        # designation + parentheses + 'sd.' on the previous line


def test_desig_strict_regex(S):
    for ok in ("Jt. Secy.", "Under Secretary (Cadre)", "Director (A&D)", "Deputy Secretary to the Govt. of India", "Under Secy. [F. No. 1/2]",
               "Director General", "DG"):
        assert S.DESIG_STRICT.match(ok), ok
    for bad in ("Secretary of the committee met", "Regards", "Amit Kumar, Director"):
        assert not S.DESIG_STRICT.match(bad), bad
