"""Opname Regisseur run 15 (workflow regisseur-16): dezelfde opname als regisseur-14 (robot door Figure from rig van
Click Joints Pro 1.2.0), met één wijziging: de botnamen van de rig staan in beeld (armature "Names" aan) zolang de
robot nog één stuk is. De rig van de robot heeft Mixamo-botnamen (mixamorig:LeftForeArm enzovoort, uit
producten/blender-gewrichten/e2e/proef_mens.py maak_rig) en Limit Rotation op linker knie (120) en elleboog (140).
Script: week 48 nr. 6 (commercie/filmpjes/scripts/week-48-click-joints.md, hook 6B), Pro-lijst nr. 2.
    blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "regisseur-14", "opname.py"))
src = open(BRON, encoding="utf-8").read()
oud = '    arm.show_in_front = True\n'
assert src.count(oud) == 1, "regel show_in_front niet gevonden"
src = src.replace(oud, oud + '    arm.data.show_names = True\n    log("KORT namen aan: " + ", ".join(b.name for b in arm.data.bones)[:300])\n')
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
