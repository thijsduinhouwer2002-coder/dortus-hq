"""Galerijbeeld 3 Click Cuts (Beeldmaker, 25 nov 2026, issue #39): het echte Blender-venster met het tabblad Click Cuts.

xvfb-run -s "-screen 0 2880x1620x24" blender --gpu-backend opengl <start.blend> --python paneel.py -- \
    <click_cuts.zip> <modelmap horse_statue_01> <uitmap>

Installeert de echte add-on (zip van main), haalt het paard binnen (520 mm hoog), drukt de echte knop Split to fit
(printer Bambu Lab A1), zet het 3D-venster schermvullend met de zijbalk open op het tabblad Click Cuts
(Ctrl + muiswiel met xdotool, zoals de e2e) en maakt een schermafbeelding. Niets aan het paneel is nagemaakt.
Interface op schaal PN_UI (standaard 1.5), zodat de tekst in een galerijbeeld leest.

Model: Horse Statue 01 van Poly Haven (https://polyhaven.com/a/horse_statue_01), licentie CC0
(https://polyhaven.com/license). Geen AI-beeld. Het beeld is een schermafbeelding van Blender, geen foto van een print.
Logt PANEEL OK en schrijft <uitmap>/paneel.json met de uitslag van de add-on.
"""
import json
import math
import os
import subprocess
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

a = sys.argv[sys.argv.index("--") + 1:]
ZIP, MODEL, UIT = a[0], a[1], a[2]
os.makedirs(UIT, exist_ok=True)
DOEL = "Click Cuts"
UI = float(os.environ.get("PN_UI", "1.5"))
HOOGTE = float(os.environ.get("PN_HOOGTE", "520"))
staat = {"stap": 0, "pogingen": 0}
meta = {}


def log(t):
    print(f"[pn] {t}", flush=True)


def gebied_3d():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                ui = next(r for r in gebied.regions if r.type == "UI")
                hoofd = next(r for r in gebied.regions if r.type == "WINDOW")
                return venster, gebied, ui, hoofd
    return None, None, None, None


def xdo(*args):
    subprocess.run(["xdotool", *args], capture_output=True, text=True)


def laad_paard():
    s = bpy.context.scene
    naam = os.path.basename(MODEL.rstrip("/"))
    bpy.ops.import_scene.gltf(filepath=os.path.join(MODEL, f"{naam}_1k.gltf"))
    ob = [o for o in s.objects if o.type == "MESH"][0]
    for o in list(s.objects):
        if o is not ob:
            bpy.data.objects.remove(o)
    ob.name = "Horse"
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    zs = [v.co.z for v in ob.data.vertices]
    ob.data.transform(Matrix.Scale(HOOGTE / (max(zs) - min(zs)), 4))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.05)
    bm.to_mesh(ob.data)
    bm.free()
    ps = [v.co for v in ob.data.vertices]
    mn = Vector([min(p[i] for p in ps) for i in range(3)])
    mx = Vector([max(p[i] for p in ps) for i in range(3)])
    ob.data.transform(Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))))
    ob.data.materials.clear()
    for p in ob.data.polygons:
        p.use_smooth = True
    meta["model_mm"] = [round(v, 1) for v in (mx - mn)]
    return ob


def klaarzetten():
    prefs = bpy.context.preferences
    prefs.view.ui_scale = UI
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    s = bpy.context.scene
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    s.unit_settings.system, s.unit_settings.scale_length, s.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
    ob = laad_paard()
    for o in s.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    inst = s.split_joints
    inst.printer = os.environ.get("PN_PRINTER", "A1")
    r = bpy.ops.split_joints.split_to_fit()
    stukken = sorted((o for o in s.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])
    meta["split"] = list(r)
    meta["stukken"] = len(stukken)
    meta["status"] = [o.get("sj_status") for o in stukken]
    meta["printer"] = inst.printer
    meta["formaat"] = inst.formaat
    meta["pen_mm"] = round(inst.pen_mm, 2)
    meta["speling_mm"] = round(inst.speling_mm, 2)
    try:
        from importlib import import_module
        mod = import_module(next(m for m in sys.modules if m.endswith("split_joints.in_een_klik")))
        meta["uitslag"] = list(mod.uitslag_tekst(s) or [])
    except Exception as e:  # alleen voor het logboek
        meta["uitslag_fout"] = repr(e)
    log(f"split {r} {len(stukken)} stukken {meta['status']}")
    # stuk 1 actief, niets geselecteerd: geen oranje rand door het beeld
    for o in s.objects:
        o.select_set(False)
    if stukken:
        bpy.context.view_layer.objects.active = stukken[0]
    for o in s.objects:
        if "sj_as" in o or o.name.endswith("_watertight") or o.get("sj_pennen"):
            o.hide_set(True)  # pennenbak naast het model staat uit: hij leidt af (de pennen zelf telt het paneel)

    venster, gebied, ui, hoofd = gebied_3d()
    with bpy.context.temp_override(window=venster, area=gebied, region=hoofd):
        bpy.ops.screen.screen_full_area()


def kijk():
    venster, gebied, ui, hoofd = gebied_3d()
    sp = gebied.spaces.active
    sp.show_region_ui = True
    sp.show_region_toolbar = True
    sh = sp.shading
    sh.type, sh.color_type, sh.light = "SOLID", "OBJECT", "STUDIO"
    sh.show_cavity = True
    sh.cavity_type = "BOTH"
    sh.show_shadows = True
    sh.shadow_intensity = 0.35
    sh.show_specular_highlight = True
    sp.clip_start, sp.clip_end = 0.5, 100000
    ov = sp.overlay
    ov.show_floor = True
    ov.show_axis_x = ov.show_axis_y = False
    ov.show_relationship_lines = False
    ov.show_extras = False
    ov.show_text = True
    r3 = sp.region_3d
    r3.view_perspective = "PERSP"
    sp.lens = float(os.environ.get("PN_LENS", "50"))
    stukken = [o for o in bpy.context.scene.objects if o.get("sj_stuk")]
    pts = [o.matrix_world @ Vector(c) for o in stukken for c in o.bound_box]
    mn = Vector([min(p[i] for p in pts) for i in range(3)])
    mx = Vector([max(p[i] for p in pts) for i in range(3)])
    midden = (mn + mx) / 2
    r3.view_location = midden + Vector((float(os.environ.get("PN_DX", "0")), 0, float(os.environ.get("PN_DZ", "0"))))
    r3.view_rotation = (Matrix.Rotation(math.radians(float(os.environ.get("PN_DRAAI", "-32"))), 3, "Z")
                        @ Matrix.Rotation(math.radians(float(os.environ.get("PN_KANTEL", "74"))), 3, "X")).to_quaternion()
    r3.view_distance = (mx - mn).length * float(os.environ.get("PN_AFSTAND", "1.35"))
    meta["kader_mm"] = [round(v, 1) for v in (mx - mn)]


def tabblad():
    venster, gebied, ui, hoofd = gebied_3d()
    if ui.active_panel_category == DOEL:
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", "5" if staat["pogingen"] < 8 else "4")
    xdo("keyup", "ctrl")
    staat["pogingen"] += 1
    return False


def stap():
    try:
        if staat["stap"] == 0:
            klaarzetten()
            staat["stap"] = 1
            return 2.0
        if staat["stap"] == 1:
            kijk()
            staat["stap"] = 2
            return 1.5
        if staat["stap"] == 2:
            if tabblad():
                log("TABBLAD OK")
                xdo("mousemove", "10", "10")
                staat["stap"] = 3
                return 2.0
            if staat["pogingen"] > 18:
                log("PANEEL FOUT: tabblad Click Cuts niet actief")
                bpy.ops.wm.quit_blender()
                return None
            return 0.6
        venster, gebied, ui, hoofd = gebied_3d()
        meta["zijbalk_px"] = [ui.x, ui.y, ui.width, ui.height]
        meta["venster_px"] = [venster.width, venster.height]
        meta["ui_scale"] = UI
        pad = os.path.join(UIT, "paneel-scherm.png")
        subprocess.run(["import", "-window", "root", pad], capture_output=True)
        ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
        with open(os.path.join(UIT, "paneel.json"), "w") as f:
            json.dump(meta, f, indent=1)
        log(f"{'PANEEL OK' if ok else 'PANEEL FOUT'} {pad} {meta}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        log(f"PANEEL FOUT {e!r}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=2.0)
