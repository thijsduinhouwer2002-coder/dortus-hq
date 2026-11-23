"""Proef per kandidaat (studio, 23 nov 2026): maakt Figure from rig (Pro 1.2.0) genoeg gewrichten zonder rare snedes?
Gebruik: blender -b --factory-startup --python proef_figuur.py -- <pro-zip> <model.glb|.blend|robot> <hoogte_mm> [weg,weg] [uitmap]
Met "robot" als model: de zelfgebouwde robot uit figuur_robot.py (studio-2, 23 nov).
Laatste regel: "PROEF <naam> hoogte=<mm> gewrichten=<n> delen=<n> stukken=<lijst>".
"""
import importlib
import json
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuur_laden as FL  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
zip_pad, pad, hoogte = args[0], args[1], float(args[2])
weg = tuple(w for w in (args[3] if len(args) > 3 else "").split(",") if w)
uit = args[4] if len(args) > 4 else None
naam_m = os.environ.get("CJ_NAAM") or os.path.splitext(os.path.basename(pad))[0]
if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
ARMEN = float(os.environ.get("CJ_ARMEN", "0"))
if pad == "robot":
    import figuur_robot as R
    arm, ob, _punten = R.laad_robot(hoogte)
elif pad.endswith(".obj"):
    arm, ob, _punten = FL.laad_mens_kleding(pad, hoogte)
else:
    arm, ob = FL.laad(pad, hoogte, weg, armen=ARMEN)
if os.environ.get("CJ_VOORPROEF"):   # snel plaatje van de invoer (Cycles), voor de knop
    FL.voorproef(os.environ["CJ_VOORPROEF"])
inst = bpy.context.scene.click_joints
inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
naam = ob.name
FL.actief(ob)
try:
    r = bpy.ops.click_joints.figuur_uit_rig()
except RuntimeError as e:
    r = f"fout {str(e).strip()[:300]}"
fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), None)
stukken = [FL.mesh_staat(o)["stukken"] for o in delen]
FL.log(f"FIGUUR {naam_m}: uitslag={r} gewrichten={len(alle)}")
regels = [fig.regel(x) for x in alle]
for x in regels:
    FL.log(f"  {x}")
FL.log(f"OVERGESLAGEN: {over}")
FL.log(f"DELEN: {len(delen)} {[o.name for o in delen]} stukken {stukken}")
if uit:
    os.makedirs(uit, exist_ok=True)
    json.dump({"model": naam_m, "hoogte_mm": hoogte, "gewrichten": len(alle), "regels": regels, "overgeslagen": str(over),
               "delen": len(delen), "stukken": stukken}, open(os.path.join(uit, f"{naam_m}-{int(hoogte)}.json"), "w"), indent=1)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, f"{naam_m}-{int(hoogte)}.blend"))
print(f"PROEF {naam_m} hoogte={int(hoogte)} gewrichten={len(alle)} delen={len(delen)} stukken={stukken}", flush=True)
