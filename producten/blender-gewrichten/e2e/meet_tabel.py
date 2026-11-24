"""Tabel uit metingen van de testset (tak betrouwbaar-uitslag, map <run>/<code>/<versie>/<figuur>-<herhaling>.json).

Gebruik: python3 meet_tabel.py <map van een run of van een code daarbinnen> [<tweede map>]
Per cel: gewrichten per herhaling, slechte sneden onderweg (opgeteld), tijd van de knop (mediaan), en "1 vorm" als
alle herhalingen precies hetzelfde figuur gaven (zelfde regels met bereik en zelfde aantal punten per deel), anders
"N vormen". Met --verlies: het grootste verlies per kogelsnede (keuring A, M1). Oude mappen met één <figuur>.json per versie werken ook.
"""
import glob
import json
import os
import re
import statistics
import sys

FIGUREN = ["robot-a", "robot-b", "robot-fijn", "kleding", "mens", "rigify", "armen"]
VERSIES = ["4.2.23", "5.2.3", "5.3.0"]


def lees(map_, extra=""):
    uit = {}
    for f in sorted(glob.glob(os.path.join(map_, "*", "*.json"))):
        naam = os.path.basename(f)[:-5]
        m = re.match(r"^(.*?)(?:-(\d+))?(-t1)?$", naam)
        if m.group(3) != (extra or None) and not (extra == "" and m.group(3) is None):
            continue
        try:
            d = json.load(open(f))
        except ValueError:
            continue
        v = os.path.basename(os.path.dirname(f))
        uit.setdefault((d["figuur"], v), []).append(d)
    return uit


def cel_verlies(lijst):
    """Keuring A, M1: grootste verlies (verloren_diag, deel van de punten) over alle geslaagde kogelsneden, en hoeveel
    kogelsneden boven 6% kwamen."""
    if not lijst:
        return "geen uitslag"
    w = [p["verloren_diag"] for d in lijst for p in d.get("pogingen", []) if isinstance(p.get("verloren_diag"), float)]
    if not w:
        return "geen uitslag" if not lijst else "geen kogelsneden"
    return f"max {100 * max(w):.1f}% / {sum(1 for x in w if x > 0.06)} van {len(w)} boven 6%"


def cel(lijst):
    if VERLIES:
        return cel_verlies(lijst)
    if not lijst:
        return "geen uitslag"
    n = ",".join(str(d["gewrichten"]) for d in lijst)
    slecht = sum(sum(1 for s in d.get("sneden", []) if not s.get("goed", True)) for d in lijst)
    tijd = statistics.median(d.get("knop_s") or 0 for d in lijst)
    vormen = len({json.dumps(d.get("vinger"), sort_keys=True) for d in lijst}) if all("vinger" in d for d in lijst) else "?"
    return f"{n} / {slecht} / {tijd:.0f} s / {vormen} {'vorm' if vormen == 1 else 'vormen'}"


extra = "-t1" if "--t1" in sys.argv else ""
VERLIES = "--verlies" in sys.argv
runs = [lees(m, extra) for m in sys.argv[1:] if not m.startswith("--")]
print("| Figuur | " + " | ".join(VERSIES) + " |")
print("|---|" + "---|" * len(VERSIES))
for fig in FIGUREN:
    print(f"| {fig} | " + " | ".join(" -> ".join(cel(r.get((fig, v))) for r in runs) for v in VERSIES) + " |")
