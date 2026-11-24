"""Opname Regisseur run 16 (workflow regisseur-17): dezelfde opname als regisseur-14 (robot, Click Joints Pro 1.2.0,
echte muis en OCR), met één wijziging: de muis klikt op "More bones (ankles too)" in plaats van "Figure from rig", zodat
de enkels erbij komen. De rig van de robot heeft voetbotten (mixamorig:LeftFoot, uit proef_mens.py maak_rig).
Script: week 49 nr. 5 (commercie/filmpjes/scripts/week-49-click-joints.md, hook 5A), Pro-lijst nr. 13.
Bron: gumroad-1.1.md "Ankles via More bones"; de knop staat in 1.2.0 onder Figure from rig (GEZIEN, ruwe opname
regisseur-16 beeld 100).
    blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "regisseur-14", "opname.py"))
src = open(BRON, encoding="utf-8").read()

EXTRA = [
    ('    knop = yield from zoek("Figure from rig")\n',
     '    knop = yield from zoek("More bones")\n    log(f"KORT enkels knop More bones {knop}")\n'),
    ('        log("KORT vangnet knop: Figure from rig via script")\n        A["actief"](ob)\n        bpy.ops.click_joints.figuur_uit_rig()\n',
     '        log("KORT vangnet knop: More bones via script")\n        A["actief"](ob)\n        bpy.ops.click_joints.figuur_uit_rig(meer=True)\n'),
    ('    log(f"KORT knop {len(lijst)} gewrichten {film[\'metingen\'][\'regels\']}")\n',
     '    log(f"KORT knop {len(lijst)} gewrichten {film[\'metingen\'][\'regels\']}")\n'
     '    film["metingen"]["enkels"] = [r for r in film["metingen"]["regels"] if "nkle" in r]\n'
     '    log(f"KORT enkels in de lijst: {film[\'metingen\'][\'enkels\']}")\n'),
]
anker = '    ("gang = verloop()", FIGUUR'
assert src.count(anker) == 1, "vervang-lijst van regisseur-14 niet gevonden"
src = src.replace(anker, "".join(f"    ({o!r}, {n!r}),\n" for o, n in EXTRA) + anker)
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
