"""Screenshot of the real Blender window with the Click Cuts panel (under xvfb, with the interface).
blender --gpu-backend opengl /tmp/start.blend --python e2e/scherm_paneel.py -- <out dir> <zip> <suzanne.blend>
Installs the add-on, brings in the split Suzanne (pieces, pins, cuts), opens the sidebar on the tab
Click Cuts (Ctrl + mouse wheel with xdotool, as in the Click Joints screen test) and takes the picture.
Logs PANEEL OK when the tab was active and the picture exists."""
import os
import subprocess
import sys

import bpy

args = sys.argv[sys.argv.index("--") + 1:]
uitmap, zip_pad, blend = args[0], args[1], args[2]
os.makedirs(uitmap, exist_ok=True)
DOEL = "Click Cuts"
staat = {"stap": 0, "pogingen": 0}


def log(t):
    print(f"[sj-scherm] {t}", flush=True)


def gebied_3d():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                ui = next(r for r in gebied.regions if r.type == "UI")
                hoofd = next(r for r in gebied.regions if r.type == "WINDOW")
                return venster, gebied, ui, hoofd
    return None, None, None, None


def xdo(*a):
    subprocess.run(["xdotool", *a], capture_output=True, text=True)


def klaarzetten():
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    with bpy.data.libraries.load(blend, link=False) as (bron, doel):
        doel.objects = [n for n in bron.objects if n.startswith(("Piece", "Pins", "Cut")) or n.endswith("_watertight")]
    s = bpy.context.scene
    s.unit_settings.system, s.unit_settings.scale_length, s.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
    sneden = bpy.data.collections.new("Click Cuts cut planes")
    s.collection.children.link(sneden)
    for ob in doel.objects:
        (sneden if "sj_as" in ob else s.collection).objects.link(ob)
        if "sj_as" in ob or ob.name.endswith("_watertight"):
            ob.hide_set(True)
        if ob.name.endswith("_watertight"):
            s.split_joints.bron = ob.name
    s["sj_midden_mm"] = [0.0, 0.0, 0.0]
    s["sj_speling_bij_split"] = 0.2  # scene props do not come with the objects: Suzanne was cut at 0.20 (#227)
    s.split_joints.printer = "A1MINI"
    venster, gebied, ui, hoofd = gebied_3d()
    sp = gebied.spaces.active
    sp.show_region_ui = True
    sp.shading.type, sp.shading.color_type = "SOLID", "OBJECT"
    sp.clip_start, sp.clip_end = 0.5, 100000
    sp.overlay.show_floor = sp.overlay.show_axis_x = sp.overlay.show_axis_y = False
    for o in bpy.context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    stukken = [o for o in s.objects if o.get("sj_stuk")]
    if stukken:
        bpy.context.view_layer.objects.active = stukken[0]
    with bpy.context.temp_override(window=venster, area=gebied, region=hoofd):
        bpy.ops.view3d.view_axis(type="FRONT")
        bpy.ops.view3d.view_orbit(angle=0.5, type="ORBITUP")
        bpy.ops.view3d.view_orbit(angle=0.6, type="ORBITLEFT")
        bpy.ops.view3d.view_all()
    log(f"klaar: {len(stukken)} stukken, statussen {[o.get('sj_status') for o in stukken]}")


def tabblad():
    venster, gebied, ui, hoofd = gebied_3d()
    if ui.active_panel_category == DOEL:
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", "5" if staat["pogingen"] < 6 else "4")
    xdo("keyup", "ctrl")
    staat["pogingen"] += 1
    return False


def stap():
    try:
        if staat["stap"] == 0:
            klaarzetten()
            staat["stap"] = 1
            return 1.5
        if staat["stap"] == 1:
            if tabblad():
                log("TABBLAD OK")
                staat["stap"] = 2
                return 1.5
            if staat["pogingen"] > 14:
                log("PANEEL FOUT: tabblad Click Cuts niet actief")
                bpy.ops.wm.quit_blender()
                return None
            return 0.6
        if staat["stap"] == 2:
            pad = os.path.join(uitmap, "paneel-x.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
            log(f"{'PANEEL OK' if ok else 'PANEEL FOUT'} {pad}")
            # second picture with More settings open, so the cut positions (0.1 mm) can be seen (keuring K1)
            bpy.context.scene.split_joints.meer = True
            # issue #227: resin starts at 0.10 and the fit test box says it is a start value
            bpy.context.scene.split_joints.materiaal = "RESIN"
            log(f"hars: speling {bpy.context.scene.split_joints.speling_mm:.2f}")
            for w in bpy.context.window_manager.windows:
                for a in w.screen.areas:
                    a.tag_redraw()
            staat["stap"] = 3
            return 1.5
        if staat["stap"] == 3:
            pad = os.path.join(uitmap, "paneel-meer.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
            log(f"{'PANEEL MEER OK' if ok else 'PANEEL MEER FOUT'} {pad}")
            # third picture: More settings closed with notes, so the notes line can be seen whole (keuring
            # run 10, M1). Uses the notes of this Split; when there are none, two example notes (logged).
            inst = bpy.context.scene.split_joints
            if not inst.meldingen.strip():
                inst.meldingen = ("Piece 02: no room for the number on a part of this face\n"
                                  "Piece 03: piece only 2.1 mm thick here, a pin needs 4.0 mm: glue this joint")
                log("noten: voorbeeldnoten gezet (deze Split had geen noten)")
            inst.meer = False
            for w in bpy.context.window_manager.windows:
                for a in w.screen.areas:
                    a.tag_redraw()
            staat["stap"] = 4
            return 1.5
        if staat["stap"] == 4:
            pad = os.path.join(uitmap, "paneel-noten.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
            log(f"{'PANEEL NOTEN OK' if ok else 'PANEEL NOTEN FOUT'} {pad}")
            # issue #69: what a buyer sees first. A fresh scene: no pieces, the model selected, custom printer
            s = bpy.context.scene
            for ob in list(bpy.data.objects):
                bpy.data.objects.remove(ob)
            inst = s.split_joints
            inst.bron, inst.uitslag, inst.meldingen, inst.meer = "", "", "", False
            inst.printer = "CUSTOM"
            venster, gebied, ui, hoofd = gebied_3d()
            with bpy.context.temp_override(window=venster, area=gebied, region=hoofd):
                bpy.ops.mesh.primitive_monkey_add(size=300.0)
                model = bpy.context.view_layer.objects.active
                model.name = "Statue"
                model.select_set(True)
                bpy.ops.view3d.view_all()
            staat["stap"] = 5
            return 1.5
        if staat["stap"] == 5:
            pad = os.path.join(uitmap, "paneel-start.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
            log(f"{'PANEEL START OK' if ok else 'PANEEL START FOUT'} {pad}")
            # and with nothing selected: the panel says why Split to fit is grey
            for o in bpy.context.view_layer.objects:
                o.select_set(False)
            bpy.context.view_layer.objects.active = None
            for w in bpy.context.window_manager.windows:
                for a in w.screen.areas:
                    a.tag_redraw()
            staat["stap"] = 6
            return 1.5
        pad = os.path.join(uitmap, "paneel-leeg.png")
        subprocess.run(["import", "-window", "root", pad], capture_output=True)
        ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
        log(f"{'PANEEL LEEG OK' if ok else 'PANEEL LEEG FOUT'} {pad}")
    except Exception as e:
        log(f"PANEEL FOUT {e!r}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=2.0)
