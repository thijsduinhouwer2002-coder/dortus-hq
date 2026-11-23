"""Tabel uit een meting van de testset (tak betrouwbaar-uitslag, map <run>): gewrichten per figuur en versie.

Gebruik: python3 meet_tabel.py <map van de run> [<map van een tweede run>]
Per cel: gewrichten / slechte sneden onderweg / tijd van de knop in s. Met twee mappen: "oud -> nieuw".
"""
import glob
import json
import os
import sys

FIGUREN = ["robot-a", "robot-b", "robot-fijn", "kleding", "mens", "rigify", "armen"]
VERSIES = ["4.2.23", "5.2.3", "5.3.0"]


def lees(map_):
    uit = {}
    for f in glob.glob(os.path.join(map_, "*", "*.json")):
        try:
            d = json.load(open(f))
        except ValueError:
            continue
        v = os.path.basename(os.path.dirname(f))
        slecht = sum(1 for s in d.get("sneden", []) if not s.get("goed", True))
        uit[(d["figuur"], v)] = (d["gewrichten"], slecht, d.get("knop_s"), d.get("ontbreekt", []))
    return uit


def cel(x):
    return "geen uitslag" if x is None else f"{x[0]} / {x[1]} / {x[2]:.0f} s"


runs = [lees(m) for m in sys.argv[1:]]
print("| Figuur | " + " | ".join(VERSIES) + " |")
print("|---|" + "---|" * len(VERSIES))
for fig in FIGUREN:
    rij = []
    for v in VERSIES:
        rij.append(" -> ".join(cel(r.get((fig, v))) for r in runs))
    print(f"| {fig} | " + " | ".join(rij) + " |")
