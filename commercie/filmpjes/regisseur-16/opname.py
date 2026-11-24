"""Opname Regisseur run 15 (workflow regisseur-16): dezelfde opname als regisseur-14 (robot door Figure from rig van
Click Joints Pro 1.2.0), met één wijziging: de botnamen van de rig staan in beeld (armature "Names" aan) zolang de
robot nog één stuk is. De rig van de robot heeft Mixamo-botnamen (mixamorig:LeftForeArm enzovoort, uit
producten/blender-gewrichten/e2e/proef_mens.py maak_rig) en Limit Rotation op linker knie (120) en elleboog (140).
Script: week 48 nr. 6 (commercie/filmpjes/scripts/week-48-click-joints.md, hook 6B), Pro-lijst nr. 2.

Run 16 (24 nov ±08:05 NL): de eerste opname liet geen enkele naam zien (GEZIEN, release regisseur-16). Oorzaak, zelf
getoetst in Blender 5.3.0: het rustige scherm (studio.rustig_scherm) zet overlay.show_text uit, en dat verbergt ook de
botnamen. Nu: show_text aan tijdens "heel" en "kies", weer uit (en namen uit) zodra "knop" begint, zodat de latere
delen rustig blijven.
    blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "regisseur-14", "opname.py"))
src = open(BRON, encoding="utf-8").read()
oud = '    arm.show_in_front = True\n'
assert src.count(oud) == 1, "regel show_in_front niet gevonden"
src = src.replace(oud, oud + '    arm.data.show_names = True\n    log("KORT namen aan: " + ", ".join(b.name for b in arm.data.bones)[:300])\n')

# extra vervangingen in de bron van reeks 4 (die regisseur-14 inleest): tekst-overlay aan en uit rond de namen
EXTRA = [
    ('    deel("heel")\n',
     '    deel("heel")\n    zijbalk()[1].spaces.active.overlay.show_text = True\n    log("KORT namen in beeld: show_text aan")\n'),
    ('    deel("knop")\n',
     '    deel("knop")\n    zijbalk()[1].spaces.active.overlay.show_text = False\n    arm.data.show_names = False\n'),
]
anker = '    ("gang = verloop()", FIGUUR'
assert src.count(anker) == 1, "vervang-lijst van regisseur-14 niet gevonden"
src = src.replace(anker, "".join(f"    ({o!r}, {n!r}),\n" for o, n in EXTRA) + anker)
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
