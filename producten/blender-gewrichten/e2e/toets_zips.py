"""Draait met: python3 e2e/toets_zips.py <gratis zip> <betaalde zip>   (geen Blender nodig)
Twee builds uit één bron (ontwerp betaald v1.1, eis 7): de gratis zip bevat niets uit betaald/ en
noemt de betaalde versie nergens (hele woorden, zodat "Properties" niet telt); de gratis zip is precies
de map click_joints/ zonder betaald/ en __pycache__; de betaalde zip heeft betaald/ en de registratie."""
import os
import re
import sys
import zipfile

gratis, betaald = sys.argv[1], sys.argv[2]
hier = os.path.dirname(os.path.abspath(__file__))
bron = os.path.join(hier, "..", "click_joints")
fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[cj-zips] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


zg = zipfile.ZipFile(gratis)
namen = sorted(n for n in zg.namelist() if not n.endswith("/"))
stap("gratis zip zonder betaald/", not any(n.startswith("betaald/") for n in namen))
woorden = re.compile(r"\b(Hinge|hinge|Pro|Superhive|superhive|betaald|Betaald)\b")
treffers = []
for n in namen:
    tekst = zg.read(n).decode("utf-8", "replace")
    treffers += [f"{n}: {m.group(0)}" for m in woorden.finditer(tekst)]
stap("gratis code noemt de betaalde versie niet", not treffers, "; ".join(treffers[:5]))

verwacht = []
for wortel, mappen, bestanden in os.walk(bron):
    mappen[:] = [m for m in mappen if m not in ("__pycache__", "betaald")] if wortel == bron else \
        [m for m in mappen if m != "__pycache__"]
    for b in bestanden:
        verwacht.append(os.path.relpath(os.path.join(wortel, b), bron).replace(os.sep, "/"))
stap("gratis zip is precies de bronmap", namen == sorted(verwacht), f"{len(namen)} bestanden")
for n in namen:
    with open(os.path.join(bron, n), "rb") as f:
        if f.read() != zg.read(n):
            stap(f"gratis zip gelijk aan bron: {n}", False)

zb = zipfile.ZipFile(betaald)
nb = zb.namelist()
stap("betaalde zip heeft betaald/__init__.py", "betaald/__init__.py" in nb)
init_b = zb.read("__init__.py").decode()
stap("betaalde __init__ registreert betaald", "from . import betaald as _betaald" in init_b)
stap("betaalde __init__ begint met de gratis __init__", init_b.startswith(zg.read("__init__.py").decode()))
stap("betaalde zip zonder __pycache__", not any("__pycache__" in n for n in nb))
print(f"[cj-zips] klaar: {fout} FOUT")
sys.exit(1 if fout else 0)
