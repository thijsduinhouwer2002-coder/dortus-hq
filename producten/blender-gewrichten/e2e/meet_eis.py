"""Eis van de testset Figure from rig (Betrouwbaarheid, 23 nov 2026): haalt de figuur zijn ondergrens?

Gebruik: python3 meet_eis.py <uitslag.json> <blender-versie> <meet_drempel.json>
De drempel per figuur staat in meet_drempel.json ("alle": voor elke versie, of per versie "4.2"/"5.2"/"5.3").
Rood (code 1) als er minder gewrichten zijn, als een deel open is of als de meting niet afkwam.
"""
import json
import sys

pad, versie, drempel_pad = sys.argv[1], sys.argv[2], sys.argv[3]
kort = ".".join(versie.split(".")[:2])
try:
    d = json.load(open(pad))
except (OSError, ValueError) as e:
    print(f"EIS FOUT: geen uitslag ({e})")
    sys.exit(1)
eisen = json.load(open(drempel_pad))["figuren"].get(d["figuur"], {})
nodig = eisen.get(kort, eisen.get("alle", 0))
fouten = []
if d["gewrichten"] < nodig:
    fouten.append(f"{d['gewrichten']} gewrichten, nodig {nodig}; ontbreekt {d['ontbreekt']}: {d['overgeslagen']}")
if d["open_delen"]:
    fouten.append(f"open delen {d['open_delen']}")
slecht = [s for s in d.get("sneden", []) if not s.get("goed", True)]
print(f"EIS {d['figuur']} Blender {versie}: {d['gewrichten']} gewrichten (nodig {nodig}), "
      f"slechte sneden onderweg {len(slecht)}, knop {d.get('knop_s')} s")
for f in fouten:
    print(f"EIS FOUT: {f}")
sys.exit(1 if fouten else 0)
