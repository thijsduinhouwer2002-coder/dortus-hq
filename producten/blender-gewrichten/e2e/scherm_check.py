"""Plaatje 20 (issue 42): Check parts in stap 3, voor de keuring van Daan.

Een kogel op een dunne staaf (straal 4 mm, kogel 5 mm, zoals toetsen_check.py), Min wall net boven de gemeten wand,
dan Check parts en een klik op de regel van deel B: B staat in Edit Mode met de dunne vlakken van de kom gekozen.
Hele venster plus een uitsnede van de zijbalk, één keer zoals hij opent (20a) en één keer omlaag gescrold tot
stap 3 (20). Regel "CHECK BEELD OK" als de uitslag een dunne wand op B heeft, B in Edit Mode staat en beide
uitsneden er zijn.
    blender --python e2e/scherm_check.py -- <map> <betaalde zip>
"""
import json
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
from scherm_basis import log, open_paneel, schiet, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

staat = {}


def bouw():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    scene = bpy.context.scene
    inst = scene.click_joints
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron = 0.2, 5.0, "KOGEL", "CURSOR"
    inst.kogel_auto, inst.uit_elkaar = False, True
    staaf = figuren.staaf("Arm", 4.0)
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(staaf)
    staat["plaats"] = bpy.ops.click_joints.plaats()
    b = bpy.data.objects.get("Arm_B")
    wand = float(b.get("cj_wand_mm", 1.0)) if b else 1.0
    scene.cj_check_wand_mm = round(wand + 0.4, 1)
    staat["check"] = bpy.ops.click_joints.check_delen()
    staat["uitslag"] = json.loads(scene.get("cj_check", "[]"))
    staat["toon"] = bpy.ops.click_joints.check_toon(naam="Arm_B", soort="dun") if b else None
    log(f"CHECK plaats {staat['plaats']} wand {wand:.2f} uitslag {staat['uitslag']} toon {staat['toon']}")


def kijk():
    _venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    rv = ruimte.region_3d
    rv.view_perspective = "ORTHO"
    rv.view_rotation = Euler((math.radians(70), 0.0, math.radians(-35)), "XYZ").to_quaternion()
    rv.view_location = (0.0, 0.0, 0.0)
    rv.view_distance = 45.0


def uitsnede(naam):
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, f"{naam}-x.png")
    doel = os.path.join(uitmap, f"{naam}-paneel.png")
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(doel)


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        bouw()
        open_paneel()
        kijk()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "boven" not in staat:
        staat["boven"] = True
        zijbalk()[1].tag_redraw()
        return 1.0
    if "boven_geschoten" not in staat:
        staat["boven_geschoten"] = True
        schiet("20a-check-boven.png")
        staat["ok_boven"] = uitsnede("20a-check-boven")
        venster, gebied, regio = zijbalk()
        if regio:  # zijbalk omlaag tot stap 3 met Check parts in beeld is (zoals scherm_rig.py)
            x = venster.x + regio.x + regio.width // 2
            y = venster.y + venster.height - (regio.y + regio.height // 2)
            subprocess.run(["xdotool", "mousemove", str(x), str(y)])
            for _ in range(25):
                subprocess.run(["xdotool", "click", "5"])
        gebied.tag_redraw()
        return 1.5
    schiet("20-check.png")
    ok_uit = uitsnede("20-check")
    b = [d for d in staat.get("uitslag", []) if d.get("naam") == "Arm_B"]
    act = bpy.context.view_layer.objects.active
    ok = (bool(b) and b[0]["dun"] > 0 and staat.get("toon") == {"FINISHED"} and bpy.context.mode == "EDIT_MESH"
          and act is not None and act.name == "Arm_B" and ok_uit and staat.get("ok_boven"))
    log(f"CHECK BEELD {'OK' if ok else 'FOUT'} uitslag={staat.get('uitslag')} modus={bpy.context.mode} "
        f"actief={act.name if act else None} uitsnede={ok_uit} boven={staat.get('ok_boven')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
