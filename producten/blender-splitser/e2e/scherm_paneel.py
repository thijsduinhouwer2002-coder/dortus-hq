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
            # Daan #229 M1: scroll the sidebar down so the whole fit test box (both lines) can be seen
            venster, gebied, ui, hoofd = gebied_3d()
            xdo("mousemove", str(venster.x + ui.x + ui.width // 2),
                str(venster.y + venster.height - (ui.y + ui.height // 2)))
            for _ in range(12):
                xdo("click", "5")
            staat["stap"] = 30
            return 1.5
        if staat["stap"] == 30:
            pad = os.path.join(uitmap, "paneel-proef.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            ok = os.path.exists(pad) and os.path.getsize(pad) > 20000
            log(f"{'PANEEL PROEF OK' if ok else 'PANEEL PROEF FOUT'} {pad}")
            for _ in range(12):  # as many up as down, so a wheel that reaches the viewport ends where it began
                xdo("click", "4")
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
            staat["stap"] = 40
            return 0.5
        if staat["stap"] == 40:
            # issue #208: Draw cut for real, with the mouse. Start the modal operator on the largest piece and
            # drag a line with xdotool straight down over the middle of that piece, as a buyer would.
            from bpy_extras import view3d_utils
            import numpy as np
            inst = bpy.context.scene.split_joints
            inst.meldingen = ""
            stukken = [o for o in bpy.context.scene.objects if o.get("sj_stuk")]
            stuk = max(stukken, key=lambda o: len(o.data.vertices))
            staat["stuk"] = stuk.name
            staat["aantal"] = len(stukken)
            for o in bpy.context.view_layer.objects:
                if o is not None:
                    o.select_set(False)
            stuk.select_set(True)
            bpy.context.view_layer.objects.active = stuk
            venster, gebied, ui, hoofd = gebied_3d()
            # 1.1 (#238): the wheel clicks for the fit test picture can reach the viewport and zoom it, so the
            # piece fell off the screen. Put the view back as at the start before measuring the line.
            with bpy.context.temp_override(window=venster, area=gebied, region=hoofd):
                bpy.ops.view3d.view_axis(type="FRONT")
                bpy.ops.view3d.view_orbit(angle=0.5, type="ORBITUP")
                bpy.ops.view3d.view_orbit(angle=0.6, type="ORBITLEFT")
                bpy.ops.view3d.view_all()
            rv3d = gebied.spaces.active.region_3d
            mw = np.array(stuk.matrix_world)
            co = np.array([tuple(v.co) for v in stuk.data.vertices]) @ mw[:3, :3].T + mw[:3, 3]
            scherm = [view3d_utils.location_3d_to_region_2d(hoofd, rv3d, p) for p in co]
            scherm = np.array([tuple(p) for p in scherm if p is not None])
            mx, my = (scherm.min(axis=0) + scherm.max(axis=0)) / 2.0  # middle of the piece on the screen
            h = (scherm[:, 1].max() - scherm[:, 1].min()) * 0.5 + 25  # the line runs 25 px past both ends
            with bpy.context.temp_override(window=venster, area=gebied, region=ui):  # as a click in the sidebar
                r = bpy.ops.split_joints.vrije_snede_tekenen("INVOKE_DEFAULT")
            log(f"tekenen: operator {r}, stuk {stuk.name}, lijn x {mx:.0f}, y {my - h:.0f} tot {my + h:.0f}")

            def naar_scherm(x, y):
                return str(int(venster.x + hoofd.x + x)), str(int(venster.y + venster.height - (hoofd.y + y)))

            staat["lijn"] = (naar_scherm(mx, my + h), naar_scherm(mx, my - h))
            staat["lijn_regio"] = (mx, (my + h, my - h))
            staat["stap"] = 41
            return 0.5
        if staat["stap"] == 41:  # every mouse step in its own timer call, so Blender handles it in between
            (x1, y1), (x2, y2) = staat["lijn"]
            k = staat.get("k", 0)
            if k == 0:
                xdo("mousemove", x1, y1)
            elif k == 1:
                xdo("mousedown", "1")
            else:
                xdo("mousemove", x1, str(int(int(y1) + (int(y2) - int(y1)) * (k - 1) / 5)))
            staat["k"] = k + 1
            if k + 1 > 6:
                staat["stap"] = 42
            return 0.3
        if staat["stap"] == 42:
            pad = os.path.join(uitmap, "tekenen-lijn.png")  # the line on the screen, before the mouse goes up
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            xdo("mouseup", "1")
            staat["stap"] = 43
            return 1.0
        if staat["stap"] == 43:
            snede = [o for o in bpy.context.scene.objects if o.get("sj_vrij") == staat["stuk"]]
            import importlib
            vs = importlib.import_module("bl_ext.user_default.click_cuts.vrije_snede")
            log(f"tekenen: muis in de operator {vs.GEBEURD[-12:]}")
            log(f"{'TEKENEN OK' if snede else 'TEKENEN FOUT'}: {len(snede)} snedevlak voor {staat['stuk']}")
            if snede:  # the plane stands edge-on: on the screen it must lie on the drawn line
                from bpy_extras import view3d_utils
                venster, gebied, ui, hoofd = gebied_3d()
                rv3d = gebied.spaces.active.region_3d
                mw = snede[0].matrix_world
                hoeken = [view3d_utils.location_3d_to_region_2d(hoofd, rv3d, mw @ v.co) for v in snede[0].data.vertices]
                xs = [p.x for p in hoeken if p is not None]
                ys = [p.y for p in hoeken if p is not None]
                lx, (ly1, ly2) = staat["lijn_regio"]
                ok = xs and max(abs(x - lx) for x in xs) < 3 and min(ys) < min(ly1, ly2) + 3 and max(ys) > max(ly1, ly2) - 3
                log(f"{'TEKENEN PLEK OK' if ok else 'TEKENEN PLEK FOUT'}: vlak op het scherm x {min(xs):.0f} tot {max(xs):.0f}, "
                    f"y {min(ys):.0f} tot {max(ys):.0f}; lijn x {lx:.0f}, y {min(ly1, ly2):.0f} tot {max(ly1, ly2):.0f}")
            # keuring #212 M1: before Cut piece the part that comes off is lit, with an arrow "comes off"
            st = vs.STAND
            ok = st["driehoeken"] > 0 and st["pijl"] is not None and st["fout"] is None
            log(f"{'TEKENEN ERAF OK' if ok else 'TEKENEN ERAF FOUT'}: {st['driehoeken']} driehoeken licht op, pijl {st['pijl']}, fout {st['fout']}")
            pad = os.path.join(uitmap, "tekenen-vlak.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
            if snede:
                venster, gebied, ui, hoofd = gebied_3d()
                with bpy.context.temp_override(window=venster, area=gebied, region=hoofd):
                    try:
                        r = bpy.ops.split_joints.vrije_snede()
                    except RuntimeError as e:
                        r = str(e).strip()[:160]
                n = len([o for o in bpy.context.scene.objects if o.get("sj_stuk")])
                log(f"{'TEKENEN SNEDE OK' if n == staat['aantal'] + 1 else 'TEKENEN SNEDE FOUT'}: Cut piece {r}, "
                    f"{staat['aantal']} naar {n} stukken")
            staat["stap"] = 44
            return 1.5
        if staat["stap"] == 44:
            pad = os.path.join(uitmap, "tekenen-gesneden.png")
            subprocess.run(["import", "-window", "root", pad], capture_output=True)
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
