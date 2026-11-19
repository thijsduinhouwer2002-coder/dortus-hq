#!/usr/bin/env python3
"""Toets voor organisatie/loket/ophalen.py zonder netwerk: python3 organisatie/loket/toets_ophalen.py"""
import datetime
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ophalen  # noqa: E402

fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[loket] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


extra = ophalen.check_regels()
stap("patronen van check.py geladen", len(extra) >= 5, str(len(extra)))
s = ophalen.schoon
stap("mailadres weg", "@" not in s("Crash, mail me at jan.jansen@example.org please", extra))
nep_tel = "bel 0" + "6 1234" + "5678 of +3" + "1612345678"  # in stukken, anders houdt de pushcontrole dit bestand tegen
stap("telefoon weg", "1234" not in s(nep_tel, extra), s(nep_tel, extra))
stap("link weg", "http" not in s("see https://evil.example/x", extra))
stap("versienummers blijven", s("CLion 2025.2.3 (CL-252.27397.1) crash", extra) == "CLion 2025.2.3 (CL-252.27397.1) crash",
     s("CLion 2025.2.3 (CL-252.27397.1) crash", extra))
stap("gedachtestreepje weg", "—" not in s("a — b", extra))
stap("geen backticks of aanhalingstekens", not any(c in s('x `rm -rf` "y" <b>', extra) for c in '`"<>'))
stap("hoogstens 100 tekens", len(s("x" * 500, extra)) <= 100)
stap("lege titel", s("", extra) == "(zonder titel)")
stap("sleutel weg", "ghp_" not in s("token ghp_" + "a" * 36, extra))

# Keuring R5 moet 3: lastige titels, één toets per geval.
def schoon_van(naam, titel, verboden, moet=None):
    uit = s(titel, extra)
    ok = not any(v in uit for v in verboden) and (moet is None or moet in uit) and len(uit) <= 100
    stap(naam, ok, repr(uit))


schoon_van("ESC weg", "rood \x1b[31mtekst\x1b[0m", ["\x1b"], "rood")
schoon_van("C0-stuurtekens weg", "a\x00b\x07c\x08d\x7fe", ["\x00", "\x07", "\x08", "\x7f"], "abcde")
schoon_van("C1-stuurtekens weg", "a\x85b\x9bc\x9fd", ["\x85", "\x9b", "\x9f"])
schoon_van("bidi U+202A tot U+202E weg", "a\u202ab\u202bc\u202cd\u202de\u202ef", [chr(c) for c in range(0x202A, 0x202F)], "abcdef")
schoon_van("bidi U+2066 tot U+2069 weg", "a\u2066b\u2067c\u2068d\u2069e", [chr(c) for c in range(0x2066, 0x206A)], "abcde")
schoon_van("zero-width U+200B tot U+200F weg", "a\u200bb\u200cc\u200dd\u200ee\u200ff", [chr(c) for c in range(0x200B, 0x2010)], "abcdef")
schoon_van("BOM U+FEFF weg", "\ufeffCrash", ["\ufeff"], "Crash")
schoon_van("markdown-link zonder http", "zie [klik](evil.example/x) nu", ["evil", "](", "["], "klik")
schoon_van("markdown-link met http", "zie [klik](https://evil.example/x)", ["evil", "http", "["], "klik")
schoon_van("markdown-beeld met //", "![img](//evil.example/p.png) crash", ["evil", "![", "//"], "img")
schoon_van("markdown-beeld genest in link", "[![a](//e.example/p.png)](//e.example)", ["e.example", "[", "]("])
schoon_van("losse haken en uitroepteken", "![x] [y] ok", ["[", "]", "!"], "ok")
schoon_van("HTML-tags weg", "<img src=x onerror=alert(1)> <b>vet</b> <script>x</script>", ["<", ">", "img", "script"], "vet")
schoon_van("backticks weg", "```rm -rf``` en `x`", ["`"])
schoon_van("regeleinden weg", "regel1\nregel2\r\nregel3\u2028regel4\u2029regel5", ["\n", "\r", "\u2028", "\u2029"], "regel1 regel2 regel3 regel4 regel5")
schoon_van("lange titel hoogstens 100 tekens", "woord " * 60, [])

data = {
    "bison-flex": [{"number": 2, "title": "Folding breaks"}, {"number": 1, "title": "Crash in CLion", "user": {"login": "iemand"}}],
    "click-joints": [{"number": 5, "title": "Pin too tight", "body": "mail me at a@b.nl"}],
    "rollwright": [],
}
regels = ophalen.nieuw(data, {"bison-flex#1"}, extra)
stap("alleen nieuwe, oudste eerst", [k for k, _ in regels] == ["bison-flex#2", "click-joints#5"], str([k for k, _ in regels]))
tekst = "\n".join(r for _, r in regels)
stap("titel, link en product", '"Folding breaks" https://github.com/thijsduinhouwer2002-coder/bison-flex/issues/2' in tekst
     and "Click Joints #5" in tekst, tekst)
stap("geen naam of tekst van de melder", "iemand" not in tekst and "a@b.nl" not in tekst)
b = ophalen.bericht([r for _, r in regels], datetime.datetime(2026, 11, 19, 6, 17, tzinfo=datetime.timezone.utc))
stap("kop van het bericht", "## 19 nov 2026 ±06:17 UTC, van de workflow loket-meldingen" in b, b.splitlines()[1])
stap("curl-zin in het bericht", ophalen.CURL_ZIN in b)


class Antwoord(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


gezien = []


def nep(req, timeout):
    gezien.append(req)
    return Antwoord(json.dumps([{"number": 3, "title": "a"}, {"number": 4, "title": "pr", "pull_request": {}}]).encode())


lijst = ophalen.haal("bison-flex", "geheim", nep)
stap("pull requests eruit", [i["number"] for i in lijst] == [3])
stap("workflow-sleutel als kop", gezien[0].get_header("Authorization") == "Bearer geheim")
stap("juiste API-adres", gezien[0].full_url.startswith("https://api.github.com/repos/thijsduinhouwer2002-coder/bison-flex/issues?state=open"))
print(f"[loket] klaar: {fout} FOUT")
sys.exit(1 if fout else 0)
