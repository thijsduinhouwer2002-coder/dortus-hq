"""Draait met: python3 -I e2e/toets_direct_zip.py <gratis zip> <direct zip>   (geen Blender nodig)
Direct-zip (Pro-knoppen op slot, Afkijker 21 nov): de extensions-zip (gratis) noemt Pro nergens (grep op elk bestand,
hele woorden) en heeft geen direct.py; de direct-zip is precies de gratis zip plus direct.py, met __init__.py gelijk
aan de gratis __init__.py plus het fragment init_direct.py, zonder betaald/; alleen daar staan de Pro-teksten.
Regels met [cj-direct-zip]. Exit 1 bij elke fout."""
import os
import re
import sys
import zipfile

gratis, direct = sys.argv[1], sys.argv[2]
hier = os.path.dirname(os.path.abspath(__file__))
fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[cj-direct-zip] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


def lees(pad):
    with open(os.path.join(hier, "direct", pad), "rb") as f:
        return f.read()


zg, zd = zipfile.ZipFile(gratis), zipfile.ZipFile(direct)
ng = sorted(n for n in zg.namelist() if not n.endswith("/"))
nd = sorted(n for n in zd.namelist() if not n.endswith("/"))
woord = re.compile(r"\b(pro|dortus\.com/click-joints)\b", re.I)

treffers = [f"{n}: {m.group(0)}" for n in ng for m in woord.finditer(zg.read(n).decode("utf-8", "replace"))]
# Uitzondering: de website in de manifest is de gewone productpagina (staat zo op extensions.blender.org).
treffers = [t for t in treffers if not t.startswith("blender_manifest.toml: dortus.com/click-joints")]
stap("extensions-zip noemt Pro nergens", not treffers, "; ".join(treffers[:5]))
stap("extensions-zip heeft geen direct.py", "direct.py" not in ng)
stap("direct-zip = gratis zip plus direct.py", nd == sorted(ng + ["direct.py"]), f"{len(nd)} bestanden")
stap("direct-zip zonder betaald/", not any(n.startswith("betaald/") for n in nd))
for n in ng:
    if n == "__init__.py":
        continue
    if zg.read(n) != zd.read(n):
        stap(f"direct-zip gelijk aan gratis: {n}", False)
stap("direct.py is e2e/direct/direct.py", "direct.py" in nd and zd.read("direct.py") == lees("direct.py"))
stap("__init__.py = gratis plus fragment",
     zd.read("__init__.py") == zg.read("__init__.py") + lees("init_direct.py"))
tekst = zd.read("direct.py").decode("utf-8") if "direct.py" in nd else ""
for t in ("Figure from rig", "Hinge with end stop", "Body-part presets", "This is in Click Joints Pro",
          "See Click Joints Pro", "Upgrade to Pro", "https://dortus.com/click-joints/", "LOCKED"):
    stap(f"direct.py bevat {t!r}", t in tekst)
stap("geen prijs in de add-on", not re.search(r"[$€]\s?\d|\d+[.,]\d\d\s?(usd|eur)", tekst, re.I))
print(f"[cj-direct-zip] KLAAR {fout} FOUT")
sys.exit(1 if fout else 0)
