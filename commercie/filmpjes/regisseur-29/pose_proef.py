"""Proef voor de pose van v7b (issue #159, keuring Daan #217 M3): laadt de robot, draait Figure from rig van Click Joints
Pro, zet elke kandidaat-pose uit POSES, telt botsingen (zelfde toets als verloop7.py) en de rode vlakken van Pro, en
maakt per pose 3 kleine beelden (Workbench, Solid) van schuin links, voren en schuin rechts.
    xvfb-run blender -b --python pose_proef.py -- <uitmap> <betaalde zip> [namen,gescheiden,door,komma]"""
import json
import math
import os
import sys
import importlib

import bpy
from mathutils import Vector

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "studio"))
sys.path.insert(0, HIER)
import figuur_laden as FL  # noqa: E402
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402
from poses7 import POSES  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
UIT, ZIP = args[0], args[1]
KIES = args[2].split(",") if len(args) > 2 else list(POSES)
os.makedirs(UIT, exist_ok=True)

src = open(os.path.join(HIER, "verloop7.py"), encoding="utf-8").read()
exec(src[src.index("def maak_toets"):src.index("def schaal_pose")])  # noqa: S102 (eigen code)


def paar(naam):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam:
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def scharnier(n, g):
    a, b = paar(n)
    if b is None:
        return
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(g, 1)
    bpy.context.view_layer.update()


bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
arm, ob, _p = FL.laad_figuur("robot", 220.0)
inst = bpy.context.scene.click_joints
inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
for o in bpy.context.view_layer.objects:
    o.select_set(False)
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.ops.click_joints.figuur_uit_rig()
arm.hide_set(True)
arm.hide_render = True
delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH" and o.visible_get()]
print("DELEN", len(delen))
for o in bpy.context.scene.objects:
    if o.type == "MESH" and o not in delen:
        o.hide_render = True
for o in delen:
    o.rotation_mode = "QUATERNION"
R.kleur_herstel(delen)
S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)

sc = bpy.context.scene
sc.render.engine = "BLENDER_WORKBENCH"
sc.display.shading.light = "STUDIO"
sc.display.shading.color_type = "MATERIAL"
sc.display.shading.show_shadows = True
sc.display.shading.show_cavity = True
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 540, 960, 100
cam = S.camera()
sc.camera = cam

R.poseer(delen, {}, scharnier=scharnier)
toets = maak_toets(delen)
rust = toets()
onder = [x for x in (paar("Left elbow")[1], paar("Right elbow")[1]) if x is not None]
eigen = {x.name: (paar(x["cj_naam"])[0].name if paar(x["cj_naam"])[0] else "") for x in onder}
uitslag = {}
for naam in KIES:
    pose = POSES[naam]
    gebruikt = R.poseer(delen, pose, scharnier=scharnier)
    nu = toets()
    nieuw = sorted(nu - rust)
    arm_hits = sorted(pr for pr in nu if any(n in pr for n in eigen) and not any(set(pr) == {k, v} for k, v in eigen.items()))
    rood = sum(len(o.get("cj_rood_vlakken", [])) // 2 for o in delen)
    uitslag[naam] = {"nieuw": nieuw, "onderarm": arm_hits, "rood": rood, "gebruikt": gebruikt}
    print("POSE", naam, "botsing", len(nieuw) + len(arm_hits), "rood", rood, gebruikt, flush=True)
    for d in [int(x) for x in os.environ.get("CJ_HOEKEN", "-50,0,40").split(",")]:
        S.richt(cam, delen, "staand", draai=d, kantel=int(os.environ.get("CJ_KANTEL", "8")), vul=0.86, midden_y=0.5)
        sc.render.resolution_percentage = 50
        sc.render.filepath = os.path.join(UIT, f"{naam}_{d:+d}.png")
        bpy.ops.render.render(write_still=True)
with open(os.path.join(UIT, "uitslag.json"), "w") as f:
    json.dump(uitslag, f, indent=1)
print("KLAAR")
