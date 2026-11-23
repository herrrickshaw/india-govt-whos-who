"""Script/transliteration/translation helpers of scripts/state_pipeline.py."""
import json
import sys
import types

import pytest


@pytest.fixture
def P(load):
    m = load("state_pipeline")
    m.S._WORDS = set()
    return m


DEVA = "आदेश"


def test_script_of_picks_dominant_script_and_threshold(P):
    assert P.script_of("Amit Kumar signed the order") == ("LATIN", 0, 23)
    hindi = "अमित कुमार सिंह " * 6                      # > 20 Devanagari characters
    scr, n, lat = P.script_of(hindi)
    assert scr == "DEVANAGARI" and n > 20 and lat == 0
    tamil = "அமித் குமார் " * 5
    assert P.script_of(tamil)[0] == "TAMIL"
    # not enough Indic characters (<= 20): falls back to LATIN even though they dominate
    assert P.script_of("अमित")[0] == "LATIN"
    # Latin text outweighs a small amount of Indic text (20 < n <= 0.3*latin)
    mixed = "अमित कुमार सिंह " * 3 + "x" * 400
    assert P.script_of(mixed)[0] == "LATIN"
    assert P.script_of("") == ("LATIN", 0, 0)
    # every configured script block is detected by its first code point
    for name, (a, b) in P.SCRIPT_RANGES.items():
        assert P.script_of(chr(a + 5) * 30)[0] == name


def test_indic_tokens(P):
    assert P.indic_tokens("अमित, कुमार; सिंह (IAS) x1", "DEVANAGARI") == ["अमित", "कुमार", "सिंह"]
    assert P.indic_tokens("अमित-कुमार ए.बी.", "DEVANAGARI") == ["अमित-कुमार", "ए.बी."]     # hyphen and '.' are allowed inside a token, Latin tokens are not
    assert P.indic_tokens("", "DEVANAGARI") == []
    assert P.indic_tokens("நாதன்", "DEVANAGARI") == []


def test_find_signatories_indic_name_then_designation(P):
    tail = "\n".join(["आदेश से", "श्री अमित कुमार", "संयुक्त सचिव", "", "कार्यालय"])
    out = P.find_signatories_indic(tail, "DEVANAGARI")
    assert out == [("अमित कुमार", "संयुक्त सचिव", "Joint Secretary", 3, 1)]
    # parentheses add 2 to the strength
    tail2 = "(अमित कुमार)\nउप सचिव"
    assert P.find_signatories_indic(tail2, "DEVANAGARI")[0][2:4] == ("Deputy Secretary", 5)
    # longest designation wins (additional chief secretary vs chief secretary vs secretary)
    tail3 = "रमेश चंद्र\nअपर मुख्य सचिव"
    assert P.find_signatories_indic(tail3, "DEVANAGARI")[0][2] == "Additional Chief Secretary"


def test_find_signatories_indic_rejections(P):
    assert P.find_signatories_indic("अमित\nसचिव", "LATIN") == []                         # unknown script
    assert P.find_signatories_indic("", "DEVANAGARI") == []
    assert P.find_signatories_indic("अमित कुमार\nकुछ और पाठ", "DEVANAGARI") == []          # no designation word
    assert P.find_signatories_indic("शासन विभाग\nसचिव", "DEVANAGARI") == []                # stop-word in the name line
    assert P.find_signatories_indic("अमित कुमार।\nसचिव", "DEVANAGARI") == []               # sentence-ending danda
    assert P.find_signatories_indic("अमित कुमार.\nसचिव", "DEVANAGARI") == []
    assert P.find_signatories_indic("अ\nसचिव", "DEVANAGARI") == []                         # name too short
    assert P.find_signatories_indic(("अमित " * 5) + "\nसचिव", "DEVANAGARI") == []          # > 4 tokens
    assert P.find_signatories_indic("अमित कुमार " + "x" * 80 + "\nसचिव", "DEVANAGARI") == []   # line longer than 70
    assert P.find_signatories_indic("अमित कुमार with latin words\nसचिव", "DEVANAGARI") == []   # name line not (almost) only the name
    # designation line must be within the next 3 non-empty lines and at most 90 chars
    far = "अमित कुमार\nx1\nx2\nx3\nसचिव"
    assert P.find_signatories_indic(far, "DEVANAGARI") == []
    long_desig = "अमित कुमार\nसचिव " + "क" * 90
    assert P.find_signatories_indic(long_desig, "DEVANAGARI") == []


def test_find_signatories_indic_tamil_honorific(P):
    tail = "திரு குமார் ராஜன்\nசெயலாளர்"
    out = P.find_signatories_indic(tail, "TAMIL")
    assert out and out[0][0] == "குமார் ராஜன்" and out[0][2] == "Secretary"


# ------------------------------------------------------------------ romanise_rule
def _fake_indic(monkeypatch, mapping):
    sanscript = types.SimpleNamespace(DEVANAGARI="DEVANAGARI", TAMIL="TAMIL", ITRANS="ITRANS")
    mod = types.ModuleType("indic_transliteration")
    mod.sanscript = sanscript
    sub = types.ModuleType("indic_transliteration.sanscript")
    sub.DEVANAGARI, sub.ITRANS = "DEVANAGARI", "ITRANS"
    sub.transliterate = lambda name, src, dst: mapping[name]
    mod.sanscript = sub
    monkeypatch.setitem(sys.modules, "indic_transliteration", mod)
    monkeypatch.setitem(sys.modules, "indic_transliteration.sanscript", sub)


def test_romanise_rule_normalises_itrans(P, monkeypatch):
    _fake_indic(monkeypatch, {"n1": "amita kumAra", "n2": "shrIdhara", "n3": "rAjeesha|", "n4": "kRRishhNa .", "n5": "sooryaa", "n6": "ramMesh"})
    assert P.romanise_rule("n1", "DEVANAGARI") == "Amit Kumar"             # word-final schwa dropped, long A shortened
    assert P.romanise_rule("n2", "DEVANAGARI") == "Shridhar"
    assert P.romanise_rule("n3", "DEVANAGARI") == "Rajish"                 # 'ee' -> 'i', doubled 'h' collapsed, danda removed
    assert P.romanise_rule("n4", "DEVANAGARI") == "Krishn"                  # RRi -> ri, 'N' -> n, stray '.' removed
    assert P.romanise_rule("n5", "DEVANAGARI") == "Surya"                  # 'oo' -> 'u', doubled 'a' at the end dropped
    assert P.romanise_rule("n6", "DEVANAGARI") == "Ramnesh"                # anusvara 'M' -> 'n'


def test_romanise_rule_returns_empty_without_library_or_on_error(P, monkeypatch):
    monkeypatch.setitem(sys.modules, "indic_transliteration", None)        # import fails
    assert P.romanise_rule("x", "DEVANAGARI") == ""
    _fake_indic(monkeypatch, {})
    assert P.romanise_rule("missing", "DEVANAGARI") == ""                  # transliterate raised KeyError
    assert P.romanise_rule("x", "NOT_A_SCRIPT") == ""                      # getattr on the fake sanscript fails


# ------------------------------------------------------------------ Groq / cache
def test_groq_key_env_then_file(P, monkeypatch, tmp_path):
    monkeypatch.setenv("GROQ_API_KEY", "env-key")
    assert P._groq_key() == "env-key"
    monkeypatch.delenv("GROQ_API_KEY")
    monkeypatch.setattr(P.Path, "home", classmethod(lambda cls: tmp_path))
    assert P._groq_key() is None
    cfg = tmp_path / ".config/market-secrets"
    cfg.mkdir(parents=True)
    (cfg / "credentials.env").write_text('OTHER=1\nGROQ_API_KEY="file-key"\n')
    assert P._groq_key() == "file-key"
    (cfg / "credentials.env").write_text("OTHER=1\n")
    assert P._groq_key() is None


class _Resp:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self, *a):
        return json.dumps(self.payload).encode()


def test_groq_json_success_request_shape(P, monkeypatch):
    monkeypatch.setattr(P, "_groq_key", lambda: "k")
    seen = {}

    def fake_urlopen(req, timeout):
        seen["url"], seen["timeout"], seen["auth"] = req.full_url, timeout, req.get_header("Authorization")
        seen["body"] = json.loads(req.data)
        return _Resp({"choices": [{"message": {"content": json.dumps({"names": {"a": "b"}})}}]})
    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    assert P.groq_json("sys", "usr", max_tokens=77) == {"names": {"a": "b"}}
    assert seen["url"] == "https://api.groq.com/openai/v1/chat/completions" and seen["timeout"] == 90 and seen["auth"] == "Bearer k"
    b = seen["body"]
    assert b["max_completion_tokens"] == 77 and b["temperature"] == 0 and b["response_format"] == {"type": "json_object"}
    assert [m["role"] for m in b["messages"]] == ["system", "user"]


def test_groq_json_no_key_returns_none_without_network(P, monkeypatch):
    monkeypatch.setattr(P, "_groq_key", lambda: None)
    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", lambda *a, **k: pytest.fail("network used"))
    assert P.groq_json("s", "u") is None


def test_groq_json_retries_with_backoff_then_gives_up(P, monkeypatch, capsys):
    monkeypatch.setattr(P, "_groq_key", lambda: "k")
    sleeps = []
    monkeypatch.setattr(P.time, "sleep", sleeps.append)
    import urllib.request
    n = {"c": 0}

    def flaky(req, timeout):
        n["c"] += 1
        raise OSError("HTTP Error 429: Too Many Requests" if n["c"] <= 2 else "connection reset")
    monkeypatch.setattr(urllib.request, "urlopen", flaky)
    assert P.groq_json("s", "u", retries=4) is None
    assert n["c"] == 4
    assert sleeps == [25, 50, 15, 20]            # 429 waits 25*(attempt+1), other errors 5*(attempt+1)
    assert "groq failed: connection reset" in capsys.readouterr().err


def test_groq_json_succeeds_after_retry(P, monkeypatch):
    monkeypatch.setattr(P, "_groq_key", lambda: "k")
    monkeypatch.setattr(P.time, "sleep", lambda s: None)
    import urllib.request
    n = {"c": 0}

    def flaky(req, timeout):
        n["c"] += 1
        if n["c"] == 1:
            raise OSError("boom")
        return _Resp({"choices": [{"message": {"content": "{\"ok\": 1}"}}]})
    monkeypatch.setattr(urllib.request, "urlopen", flaky)
    assert P.groq_json("s", "u") == {"ok": 1}


def test_cache_roundtrip(P, repo):
    (repo / "data/states").mkdir(parents=True, exist_ok=True)
    assert P.load_cache() == {"names": {}, "text": {}}
    P.save_cache({"names": {"अ": "A"}, "text": {}})
    assert json.loads((repo / "data/states/translations.json").read_text(encoding="utf-8")) == {"names": {"अ": "A"}, "text": {}}
    assert P.load_cache()["names"] == {"अ": "A"}


def test_translate_batch_chunks_dedups_and_filters(P, repo, monkeypatch):
    (repo / "data/states").mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(P.time, "sleep", lambda s: None)
    calls = []

    def fake_groq(system, user, **kw):
        req = json.loads(user)
        calls.append(req)
        return {"names": {**{n: n.upper() for n in req["names"]}, "stranger": "X"}, "text": {t: t + "!" for t in req["text"]}}
    monkeypatch.setattr(P, "groq_json", fake_groq)
    cache = {"names": {"known": "K"}, "text": {}}
    names = [f"n{i}" for i in range(13)] + ["n0", "known", ""]
    P.translate_batch(cache, names, ["t1", "t1", ""], "Hindi")
    assert [len(c["names"]) for c in calls] == [12, 1] and calls[0]["text"] == ["t1"] and calls[1]["text"] == []
    assert cache["names"]["n12"] == "N12" and cache["names"]["known"] == "K" and "stranger" not in cache["names"]
    assert cache["text"] == {"t1": "t1!"}
    assert json.loads((repo / "data/states/translations.json").read_text())["names"]["n3"] == "N3"
    # a failed call leaves the cache untouched and unsaved
    monkeypatch.setattr(P, "groq_json", lambda *a, **k: None)
    c2 = {"names": {}, "text": {}}
    P.translate_batch(c2, ["z"], [], "Hindi")
    assert c2 == {"names": {}, "text": {}}
    # nothing to do -> no calls
    monkeypatch.setattr(P, "groq_json", lambda *a, **k: pytest.fail("no call expected"))
    P.translate_batch({"names": {"a": "A"}, "text": {}}, ["a"], [], "Hindi")


def test_slug_for(P):
    assert P.slug_for("https://www.education.up.gov.in/home") == "st-education-up"
    assert P.slug_for("http://dept.nic.in") == "st-dept"
    assert P.slug_for("https://x.org.in") == "st-x"
    assert P.slug_for("https://Health.Kerala.GOV.IN/") == "st-health-kerala"
    assert P.slug_for("https://abc.com") == "st-abc-com"


def test_state_language_table_is_consistent(P):
    for st, (langs, scr, scheme, language) in P.STATE_LANG.items():
        assert scr == "LATIN" or scr in P.SCRIPT_RANGES, st
        assert "eng" in langs, st
    assert P.INDIC_DESIG == sorted(P.INDIC_DESIG, key=lambda x: -len(x[0]))        # longest first so 'Additional Chief Secretary' wins
    assert P.CADRE["KA"] == "KN" and P.CADRE["DL"] == "UT"
