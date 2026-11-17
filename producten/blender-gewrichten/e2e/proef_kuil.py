"""Proef (17 nov run 24, Ruben): hoeveel huid haalt een elleboogscharnier weg, en steekt er iets uit?

Aanleiding: Daan zag op plaatje 19 een "grijs blok" boven de elleboog. Deze proef zet op de MakeHuman-figuur alleen
de linkerelleboog (stop uit de rig, CJ_EL, standaard 140) en meet rond de elleboog (30 mm):
- huid weg: punten van het origineel die verder dan 0,3 mm van deel A en B liggen (diepte van de kuil);
- huid erbij: punten van A of B die meer dan 0,3 mm buiten het origineel liggen (een echt uitstekend blok).

Gebruik: CJ_HOOGTE=220 [CJ_EL=140] blender -b --factory-startup --python e2e/proef_kuil.py -- <betaalde zip> <base.obj>
Uitslag: regels [cj-kuil].
"""
import importlib
import os
import sys

import bmesh
import bpy
from mathutils.bvhtree import BVHTree

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
EL = int(os.environ.get("CJ_EL", "140"))
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
_src = _src.replace('("LeftForeArm", 140)', f'("LeftForeArm", {EL})')
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]


def log(t):
    print(f"[cj-kuil] {t}", flush=True)


def bvh(ob):
    b = bmesh.new()
    b.from_mesh(ob.data)
    b.transform(ob.matrix_world)
    return BVHTree.FromBMesh(b), b


def main():
    zip_pad, pad = sys.argv[sys.argv.index("--") + 1:][:2]
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    A["leeg"]()
    ob, punten = M["laad_mens"](pad)
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    naam = ob.name
    rig = M["maak_rig"](punten)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
    echt = rigm.gewrichten
    rigm.gewrichten = lambda a, meer=False: [x for x in echt(a, meer) if "left elbow" in x[2].lower()]
    r = bpy.ops.click_joints.figuur_uit_rig()
    log(f"rig-stop {EL}, uitslag {r}")
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    for x in fig.figuur_gewrichten(bpy.context.scene.objects, naam):
        log(f"lijst: {fig.regel(x)}")
    elleboog = rig.matrix_world @ next(b for b in rig.data.bones if b.name.endswith("LeftForeArm")).head_local
    oo, bo = bvh(bpy.data.objects[naam])
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    bd = [bvh(o) for o in delen]
    weg = []
    for v in bo.verts:
        if (v.co - elleboog).length < 30:
            d = min(t.find_nearest(v.co)[3] for t, _ in bd)
            if d > 0.3:
                weg.append((d, v.co.copy()))
    erbij = 0
    for t, b in bd:
        for v in b.verts:
            if (v.co - elleboog).length < 30:
                loc, n, _i, _d = oo.find_nearest(v.co)
                if (v.co - loc).dot(n) > 0.3:
                    erbij += 1
    diep = max((d for d, _ in weg), default=0.0)
    log(f"elleboog {tuple(round(c, 1) for c in elleboog)}, delen {len(delen)}")
    log(f"huid weg: {len(weg)} punten, diepste {diep:.2f} mm")
    if weg:
        d, p = max(weg, key=lambda x: x[0])
        rel = p - elleboog
        log(f"diepste punt t.o.v. elleboog: {tuple(round(c, 1) for c in rel)} mm")
    log(f"huid erbij (uitstekend > 0,3 mm): {erbij} punten")
    log("KLAAR")


main()
