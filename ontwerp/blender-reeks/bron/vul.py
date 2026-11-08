"""Vul het postersjabloon. Gebruik: python3 vul.py waarden.json uit.html
waarden.json: NAAM, ICOON, KOP (mag <em>woord</em> bevatten), ZIN, CHIPS (lijst van [soort w|g|r, label, tekst]), VOET, SCHERM."""
import json, sys
w = json.load(open(sys.argv[1])); t = open(__file__.replace("vul.py", "poster-sjabloon.html")).read()
w["CHIPS"] = "\n  ".join(f'<div class="chip"><b class="{s}">{l}</b>{x}</div>' for s, l, x in w["CHIPS"])
for k, v in w.items(): t = t.replace("{{" + k + "}}", v)
open(sys.argv[2], "w").write(t)
