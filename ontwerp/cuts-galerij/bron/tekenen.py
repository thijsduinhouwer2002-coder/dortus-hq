"""Galerijbeeld Click Cuts 1.1 "Draw your own cut" (Beeldmaker, 27 nov 2026): het echte Blender-venster met Draw cut.

xvfb-run -s "-screen 0 2880x1620x24" blender --gpu-backend opengl <start.blend> --python tekenen.py -- \
    <click_cuts-1.1.zip> <modelmap horse_statue_01> <uitmap>

Installeert de echte add-on (zip van tak claude/click-cuts-1.1, versie 1.1.0), haalt het paard binnen (520 mm hoog),
drukt de echte knop Split to fit (Bambu Lab A1), zet het 3D-venster schermvullend met het tabblad Click Cuts open,
kiest een stuk, drukt de echte knop Draw cut en trekt met de muis (xdotool) een lijn over dat stuk, zoals een koper.
Daarna licht het deel dat eraf gaat wit op met de pijl "comes off"; dan de schermafbeelding. Niets nagetekend.

Model: Horse Statue 01 van Poly Haven (https://polyhaven.com/a/horse_statue_01), licentie CC0
(https://polyhaven.com/license). Geen AI-beeld. Het beeld is een schermafbeelding van Blender, geen foto van een print.

Omgeving: TK_STUK (nummer van het stuk; standaard het hoogste stuk), TK_LIJN (x1,y1,x2,y2 als deel van het kader
van dat stuk op het scherm, 0 tot 1, y omhoog), PN_* voor de camera zoals paneel.py. Schrijft <uitmap>/tekenen.json.
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
    print(f"[tk] {t}", flush=True)


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


def foto(naam):
    pad = os.path.join(UIT, naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    return os.path.exists(pad) and os.path.getsize(pad) > 20000


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


def stukken():
    return sorted((o for o in bpy.context.scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])


def klaarzetten():
    bpy.context.preferences.view.ui_scale = UI
    bpy.context.preferences.view.smooth_view = 0
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
    st = stukken()
    meta["split"] = list(r)
    meta["stukken"] = len(st)
    meta["status"] = [o.get("sj_status") for o in st]
    meta["printer"] = inst.printer
    meta["speling_mm"] = round(inst.speling_mm, 2)
    meta["midden_z"] = {o.name: round(sum((o.matrix_world @ Vector(c)).z for c in o.bound_box) / 8, 1) for o in st}
    meta["kleur"] = {o.name: [round(c, 2) for c in o.color[:3]] for o in st}
    log(f"split {r} {len(st)} stukken {meta['status']}")
    for o in s.objects:
        o.select_set(False)
        if "sj_as" in o or o.name.endswith("_watertight") or o.get("sj_pennen"):
            o.hide_set(True)
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
    r3 = sp.region_3d
    r3.view_perspective = "PERSP"
    sp.lens = float(os.environ.get("PN_LENS", "50"))
    st = stukken()
    pts = [o.matrix_world @ Vector(c) for o in st for c in o.bound_box]
    mn = Vector([min(p[i] for p in pts) for i in range(3)])
    mx = Vector([max(p[i] for p in pts) for i in range(3)])
    midden = (mn + mx) / 2
    r3.view_location = midden + Vector((float(os.environ.get("PN_DX", "0")), 0, float(os.environ.get("PN_DZ", "0"))))
    r3.view_rotation = (Matrix.Rotation(math.radians(float(os.environ.get("PN_DRAAI", "-32"))), 3, "Z")
                        @ Matrix.Rotation(math.radians(float(os.environ.get("PN_KANTEL", "74"))), 3, "X")).to_quaternion()
    r3.view_distance = (mx - mn).length * float(os.environ.get("PN_AFSTAND", "1.35"))


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


def start_tekenen():
    """Kies het stuk, druk Draw cut en reken de lijn uit (in schermpixels van het hele venster)."""
    from bpy_extras import view3d_utils
    import numpy as np
    st = stukken()
    keuze = os.environ.get("TK_STUK")
    if keuze:
        stuk = next(o for o in st if int(o["sj_stuk"]) == int(keuze))
    else:
        stuk = max(st, key=lambda o: meta["midden_z"][o.name])
    meta["stuk"] = stuk.name
    staat["aantal"] = len(st)
    for o in bpy.context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    stuk.select_set(True)
    bpy.context.view_layer.objects.active = stuk
    venster, gebied, ui, hoofd = gebied_3d()
    rv3d = gebied.spaces.active.region_3d
    mw = np.array(stuk.matrix_world)
    co = np.array([tuple(v.co) for v in stuk.data.vertices]) @ mw[:3, :3].T + mw[:3, 3]
    scherm = [view3d_utils.location_3d_to_region_2d(hoofd, rv3d, p) for p in co]
    scherm = np.array([tuple(p) for p in scherm if p is not None])
    lo, hi = scherm.min(axis=0), scherm.max(axis=0)
    meta["stuk_scherm"] = [round(float(v)) for v in (*lo, *hi)]
    f = [float(v) for v in os.environ.get("TK_LIJN", "0.5,-0.15,0.5,1.15").split(",")]
    p1 = (lo[0] + f[0] * (hi[0] - lo[0]), lo[1] + f[1] * (hi[1] - lo[1]))
    p2 = (lo[0] + f[2] * (hi[0] - lo[0]), lo[1] + f[3] * (hi[1] - lo[1]))
    with bpy.context.temp_override(window=venster, area=gebied, region=ui):  # als een klik in de zijbalk
        r = bpy.ops.split_joints.vrije_snede_tekenen("INVOKE_DEFAULT")
    log(f"tekenen: operator {r}, stuk {stuk.name}, lijn {p1} tot {p2}")

    def naar_scherm(x, y):
        return int(venster.x + hoofd.x + x), int(venster.y + venster.height - (hoofd.y + y))

    staat["lijn"] = (naar_scherm(*p1), naar_scherm(*p2))
    meta["lijn_regio"] = [round(float(v)) for v in (*p1, *p2)]


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
                kijk()  # een wielklik kan het venster bereiken: camera opnieuw
                staat["stap"] = 3
                return 2.0
            if staat["pogingen"] > 18:
                log("TEKENEN FOUT: tabblad Click Cuts niet actief")
                bpy.ops.wm.quit_blender()
                return None
            return 0.6
        if staat["stap"] == 3:
            foto("tekenen-voor.png")
            start_tekenen()
            staat["stap"] = 4
            return 0.6
        if staat["stap"] == 4:  # elke muisstap in een eigen timer, zodat Blender hem tussendoor verwerkt
            (x1, y1), (x2, y2) = staat["lijn"]
            k = staat.get("k", 0)
            n = 8
            if k == 0:
                xdo("mousemove", str(x1), str(y1))
            elif k == 1:
                xdo("mousedown", "1")
            else:
                t = (k - 1) / n
                xdo("mousemove", str(int(x1 + (x2 - x1) * t)), str(int(y1 + (y2 - y1) * t)))
            staat["k"] = k + 1
            if k + 1 > n + 1:
                staat["stap"] = 5
            return 0.3
        if staat["stap"] == 5:
            foto("tekenen-lijn.png")  # de lijn op het scherm, muis nog ingedrukt
            xdo("mouseup", "1")
            staat["stap"] = 6
            return 1.2
        if staat["stap"] == 6:
            import importlib
            vs = importlib.import_module("bl_ext.user_default.click_cuts.vrije_snede")
            st = vs.STAND
            snede = [o for o in bpy.context.scene.objects if o.get("sj_vrij") == meta["stuk"]]
            ok = bool(snede) and st["driehoeken"] > 0 and st["pijl"] is not None and st["fout"] is None
            meta["eraf"] = {"driehoeken": st["driehoeken"], "pijl": str(st["pijl"]), "fout": st["fout"]}
            meta["snedevlak"] = len(snede)
            xdo("mousemove", "10", "10")
            for w in bpy.context.window_manager.windows:
                for ar in w.screen.areas:
                    ar.tag_redraw()
            log(f"{'TEKENEN ERAF OK' if ok else 'TEKENEN ERAF FOUT'} {meta['eraf']}")
            staat["stap"] = 7
            return 1.0
        venster, gebied, ui, hoofd = gebied_3d()
        meta["zijbalk_px"] = [ui.x, ui.y, ui.width, ui.height]
        meta["venster_px"] = [venster.width, venster.height]
        meta["ui_scale"] = UI
        ok = foto("tekenen-scherm.png")
        with open(os.path.join(UIT, "tekenen.json"), "w") as f:
            json.dump(meta, f, indent=1)
        log(f"{'TEKENEN OK' if ok else 'TEKENEN FOUT'} {meta}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        log(f"TEKENEN FOUT {e!r}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=2.0)
