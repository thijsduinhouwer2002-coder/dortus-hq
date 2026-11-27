"""Galerijbeeld "paneel 1.2.9" van Click Joints Pro (Beeldmaker, 27 nov 2026, issue #259).

Echte Blender met interface (Xvfb), echte Pro-add-on uit main (zip via e2e/maak_zip.sh betaald), de MakeHuman-figuur
met Mixamo-rig uit de e2e (proef_mens.py en scherm_mens.py: base.obj, CC0 1.0, github.com/makehumancommunity/makehuman,
makehuman/data/3dobjs/base.obj). Twee schermafbeeldingen in één run:
  rig-voor.png  de figuur met zijn rig in beeld, paneel met "Rig found" en Figure from rig bovenaan;
  rig-na.png    na een druk op die echte knop (ellebogen en knieën scharnier, heupen en nek kogel).
Niets aan het paneel of de figuur is nagetekend; tekst en kader komen er later bij (tekst_paneel_rig.py).

  cd producten/blender-gewrichten
  CJ_MENS_OBJ=<base.obj> xvfb-run -s "-screen 0 2880x1620x24" <blender> --factory-startup --python \
      ../../ontwerp/pro-galerij/bron/paneel_rig.py -- <uitmap> <click_joints_betaald.zip>
Logt PANEEL RIG OK en schrijft <uitmap>/paneel-rig.json.
"""
import json
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler, Vector

E2E = os.path.join(os.getcwd(), "e2e")
sys.path.insert(0, E2E)
UI = float(os.environ.get("PR_UI", "1.5"))
_src = open(os.path.join(E2E, "scherm_mens.py"), encoding="utf-8").read()
_src = _src[:_src.index("\ndef bouw(")]
S = {"__name__": "scherm_mens_deel", "__file__": os.path.join(E2E, "scherm_mens.py")}
exec(compile(_src, "scherm_mens.py", "exec"), S)
A, M = S["A"], S["M"]
from scherm_basis import uitmap, zip_pad, zijbalk, xdo  # noqa: E402

staat = {"n": 0, "pogingen": 0}
meta = {}


def log(t):
    print(f"[pr] {t}", flush=True)


def bouw():
    A["leeg"]()
    ob, punten = M["laad_mens"](os.environ["CJ_MENS_OBJ"])
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    S["etalagepop"](ob)
    ob.name = os.environ.get("PR_NAAM", "figure")
    arm = M["maak_rig"](punten)
    arm.data.display_type = os.environ.get("PR_BOT", "OCTAHEDRAL")
    arm.show_in_front = True
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    for o in bpy.context.scene.objects:
        o.select_set(False)
    A["actief"](ob)
    ob.select_set(False)  # actief, maar geen oranje rand
    staat["mesh"], staat["rig"] = ob.name, arm.name
    meta["rig"] = arm.name
    meta["botten"] = len(arm.data.bones)


def rustig():
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.screen.screen_full_area()
    venster, gebied, _ = zijbalk()
    sp = gebied.spaces.active
    sp.show_region_ui = True
    ov = sp.overlay
    for k in ("show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_text", "show_object_origins",
              "show_relationship_lines"):
        setattr(ov, k, False)
    ov.show_floor = True
    sh = sp.shading
    sh.type, sh.color_type, sh.light = "SOLID", "MATERIAL", "STUDIO"
    sh.show_cavity = True
    sh.cavity_type = "BOTH"
    sh.show_shadows = True
    sh.shadow_intensity = 0.3
    sp.clip_start, sp.clip_end = 0.1, 10000
    rv = sp.region_3d
    rv.view_perspective = "PERSP"
    sp.lens = float(os.environ.get("PR_LENS", "50"))
    rv.view_rotation = Euler((math.radians(float(os.environ.get("PR_KANTEL", "84"))), 0.0,
                              math.radians(float(os.environ.get("PR_DRAAI", "-24")))), "XYZ").to_quaternion()
    rv.view_location = (float(os.environ.get("PR_MIDX", "40")), 0.0, float(os.environ.get("PR_MIDZ", "112")))
    rv.view_distance = float(os.environ.get("PR_AFSTAND", "520"))


def tabblad():
    venster, gebied, ui = zijbalk()
    if ui.active_panel_category == "Click Joints":
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", "5" if staat["pogingen"] < 8 else "4")
    xdo("keyup", "ctrl")
    staat["pogingen"] += 1
    return False


def schiet(naam):
    pad = os.path.join(uitmap, naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    return os.path.exists(pad) and os.path.getsize(pad) > 20000


def stap():
    staat["n"] += 1
    try:
        if staat["n"] == 1:
            bpy.context.preferences.view.ui_scale = UI
            bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
            return 1.0
        if staat["n"] == 2:
            bouw()
            rustig()
            return 1.5
        if "tab" not in staat:
            if tabblad():
                staat["tab"] = True
                xdo("mousemove", "300", "1560")
                return 2.0
            if staat["pogingen"] > 18:
                log("PANEEL RIG FOUT: tabblad niet actief")
                bpy.ops.wm.quit_blender()
                return None
            return 0.6
        if "voor" not in staat:
            venster, gebied, ui = zijbalk()
            meta["zijbalk_px"] = [ui.x, ui.y, ui.width, ui.height]
            meta["venster_px"] = [venster.width, venster.height]
            staat["voor"] = schiet("rig-voor.png")
            ob = bpy.data.objects[staat["mesh"]]
            A["actief"](ob)
            ob.select_set(False)
            staat["knop"] = list(bpy.ops.click_joints.figuur_uit_rig())
            bpy.data.objects[staat["rig"]].hide_set(True)
            if os.environ.get("PR_BUIG", "1") == "1":
                S["buig"]()  # echte Bend-schuif van het paneel, zoals plaatje 19 (rechterknie 60), heupband uit
                meta["gebogen"] = S["staat"].get("gebogen")
            import importlib
            fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
            lijst = fig.figuur_gewrichten(bpy.context.scene.objects, staat["mesh"])
            meta["knop"] = staat["knop"]
            meta["regels"] = [fig.regel(r) for r in lijst]
            meta["samenvatting"] = fig.samenvatting(lijst)
            for o in bpy.context.scene.objects:
                o.select_set(False)
            return 2.0
        na = schiet("rig-na.png")
        meta["ui_scale"] = UI
        meta["blender"] = bpy.app.version_string
        with open(os.path.join(uitmap, "paneel-rig.json"), "w") as f:
            json.dump(meta, f, indent=1)
        ok = staat.get("voor") and na and staat["knop"] == ["FINISHED"]
        log(f"{'PANEEL RIG OK' if ok else 'PANEEL RIG FOUT'} {meta}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        log(f"PANEEL RIG FOUT {e!r}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=2.0)
