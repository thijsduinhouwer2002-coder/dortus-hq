"""Opname tip-reeks 10 (Regisseur run 11, 24 nov 2026): "piepklein in je slicer". Echte Blender 5.3.0 op een X-scherm
van 2160x1920, UI-schaal 2, geen add-on. Hulpcode gelijk aan ../regisseur-11/tip_opname.py.

Tip J "export": de scène staat op Unit Scale 1 met lengte in millimeter (Blender rekent dan in meter, toont mm). Een
label van 60 mm is intern 0,06. N: Dimensions zegt 60 mm. Een STL heeft geen eenheid: de gewone export schrijft 0,06.
File > Export > STL (echte muis, menu via OCR), in het venster Scale 1000, Export. Het script leest beide STL-bestanden
na (grootste maat, film.json metingen): zonder Scale en met Scale 1000.

Een stap die niet raakte, doet het script daarna zelf (log "KORT vangnet").
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python tip_opname.py -- <uitmap>"""
import json
import math
import os
import subprocess
import sys
import time

import bmesh
import bpy
from mathutils import Vector

uitmap = sys.argv[sys.argv.index("--") + 1]
beeldmap = os.path.join(uitmap, "beelden")
os.makedirs(beeldmap, exist_ok=True)
film = {"fps": 30, "delen": {}, "n": 0, "muis": [], "metingen": {}}
MUIS = {"x": 1500, "y": 1500, "klik": 0}
SNEL = int(os.environ.get("CJ_SNEL", "1"))     # proef: elk n-de beeld echt pakken


def log(t):
    print(f"[tip12] {t}", flush=True)


def xdo(*a):
    r = subprocess.run(["xdotool", *a], capture_output=True, text=True)
    if r.returncode:
        log(f"xdotool {' '.join(a)} faalde: {r.stderr.strip()}")


def neem(houd=1):
    film["n"] += 1
    pad = os.path.join(beeldmap, f"b{film['n']:05d}.png")
    if SNEL == 1 or film["n"] % SNEL == 0 or houd > 1:
        subprocess.run(["import", "-window", "root", pad], capture_output=True)
    film["muis"].append([MUIS["x"], MUIS["y"], MUIS["klik"]])
    MUIS["klik"] = 0
    for _ in range(houd - 1):
        film["n"] += 1
        kopie = os.path.join(beeldmap, f"b{film['n']:05d}.png")
        if os.path.exists(pad):
            os.link(pad, kopie)
        film["muis"].append([MUIS["x"], MUIS["y"], 0])


def deel(naam):
    film["delen"][naam] = film["n"] + 1
    log(f"deel {naam} vanaf beeld {film['n'] + 1}")


def zacht(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def herteken():
    for w in bpy.context.window_manager.windows:
        for a in w.screen.areas:
            a.tag_redraw()


def gebied(soort=None):
    w = bpy.context.window_manager.windows[0]
    for a in w.screen.areas:
        if soort is None or a.type == soort:
            return w, a
    return w, None


def regio_rect(a, soort="WINDOW"):
    w = bpy.context.window_manager.windows[0]
    for r in a.regions:
        if r.type == soort:
            return [w.x + r.x, w.y + w.height - (r.y + r.height), r.width, r.height]
    return None


def muis_naar(x, y, stappen=16):
    x0, y0 = MUIS["x"], MUIS["y"]
    for i in range(stappen):
        t = zacht((i + 1) / stappen)
        MUIS["x"], MUIS["y"] = int(x0 + (x - x0) * t), int(y0 + (y - y0) * t)
        xdo("mousemove", str(MUIS["x"]), str(MUIS["y"]))
        yield 0.03
        neem()


def klik():
    xdo("click", "1")
    MUIS["klik"] = 1


def toets(*k):
    xdo("key", *k)


def ocr(tekst, vak, drempel="60%", woord=None):
    pad = "/tmp/tip12_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", drempel,
                    "-negate", "/tmp/tip12_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip12_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
    regels = {}
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            regels.setdefault((d[2], d[3], d[4]), []).append(
                (d[11].strip().lower().strip(".,:;(){}[]'\"|"), int(d[6]), int(d[7]), int(d[8]), int(d[9])))
    doel = tekst.lower().split()
    for ws in regels.values():
        ws.sort(key=lambda w: w[1])
        for i in range(len(ws) - len(doel) + 1):
            if all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                s = ws[i:i + len(doel)] if woord is None else [ws[i + woord]]
                return (x0 + (min(w[1] for w in s) + max(w[1] + w[3] for w in s)) // 2,
                        y0 + (min(w[2] for w in s) + max(w[2] + w[4] for w in s)) // 2)
    alle = " ".join(w[0] for ws in regels.values() for w in ws)
    log(f"KORT ocr niet gevonden: {tekst!r} in: {alle[:300]}")
    return None


def zoek(tekst, vak, keer=4):
    for _ in range(keer):
        p = ocr(tekst, vak)
        if p:
            return p
        yield 0.4
    return None


def houd(n):
    for _ in range(max(1, n // 2)):
        yield 0.03
        neem(2)


# ---------- scherm ----------

def zet_scherm():
    p = bpy.context.preferences
    p.view.ui_scale = float(os.environ.get("CJ_UI", "2.0"))
    p.view.show_splash = False
    p.view.show_tooltips = False
    p.view.filebrowser_display_type = "SCREEN"   # run 12: los venster viel rechts buiten het X-scherm (geen WM)
    sc = bpy.context.scene
    for o in list(sc.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    sc.unit_settings.system = "METRIC"
    sc.unit_settings.scale_length = 0.001
    sc.unit_settings.length_unit = "MILLIMETERS"
    w = bpy.context.window_manager.windows[0]
    # alleen de 3D-weergave: maximaliseren (Ctrl+Spatie), kop blijft staan
    groot = [a for a in w.screen.areas if a.type == "VIEW_3D"][0]
    with bpy.context.temp_override(window=w, area=groot, region=[r for r in groot.regions if r.type == "WINDOW"][0]):
        bpy.ops.screen.screen_full_area()
    _, a = gebied("VIEW_3D")
    sp = a.spaces.active
    sp.shading.type = "SOLID"
    sp.shading.light = "STUDIO"
    sp.shading.color_type = "MATERIAL"
    sp.overlay.show_stats = False
    sp.overlay.show_cursor = False
    p.themes[0].view_3d.object_origin_size = 10   # Voorkeuren > Themes > 3D Viewport: grotere oorsprong-stip (leesbaar op een telefoon)
    sp.overlay.grid_scale = 0.001
    sp.clip_start, sp.clip_end = 1.0, 100000.0
    sp.show_region_toolbar = False
    sp.show_region_ui = False
    sp.show_gizmo_navigate = False
    log(f"KORT scherm {w.width}x{w.height} gebieden {len(w.screen.areas)}")


def cam(draai, kantel, afstand, punt):
    _, a = gebied("VIEW_3D")
    r3 = a.spaces.active.region_3d
    r3.view_perspective = "PERSP"
    from mathutils import Euler
    r3.view_rotation = Euler((math.radians(kantel), 0, math.radians(draai)), "XYZ").to_quaternion()
    r3.view_distance = afstand
    r3.view_location = Vector(punt)
    herteken()


def stuk(n, doe):
    for i in range(max(1, n // 2)):
        doe(zacht(i / max(1, n // 2 - 1)))
        yield 0.03
        neem(2)


def selecteer(ob):
    for o in bpy.context.scene.objects:
        o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def zachte_muis_in_beeld():
    _, a = gebied("VIEW_3D")
    v = regio_rect(a)
    return v[0] + int(v[2] * 0.78), v[1] + int(v[3] * 0.80)


def nonmanifold_tellen(ob):
    bm = bmesh.from_edit_mesh(ob.data)
    return sum(1 for e in bm.edges if e.select)





# ---------- tip "tekst": je naam op een print ----------

def wacht_ocr(tekst, vak, p, drempel="35%", woord=None):
    """Wacht tot een net geopend menu getekend is: tot 10 pogingen, muis een tikje bewegen (les run 7)."""
    q = None
    for i in range(10):
        yield 0.4
        xdo("mousemove", str(p[0] + (i % 2) * 2), str(p[1]))
        neem(2)
        q = ocr(tekst, vak, drempel, woord)
        if q:
            break
    return q


def kop_menu(kop, knop, knop_woord, sub, item, item_vak_dx, meet):
    """Menu in de kop (knop via OCR), submenu hoveren, item klikken. True als het zo ging."""
    p = ocr(knop, kop, woord=knop_woord)
    film["metingen"][meet + "_knop"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    q = yield from wacht_ocr(sub, [max(0, p[0] - 200), p[1], 700, 900], p)
    film["metingen"][meet + "_sub"] = q
    if not q:
        toets("Escape")
        return False
    yield from muis_naar(q[0], q[1], 14)
    r = yield from wacht_ocr(item, [q[0] + 100, max(0, q[1] - 200), item_vak_dx, 700], q)
    film["metingen"][meet + "_item"] = r
    if not r:
        toets("Escape")
        toets("Escape")
        return False
    yield from muis_naar(q[0] + 330, q[1], 6)
    yield from muis_naar(r[0], r[1], 12)
    neem(6)
    klik()
    yield 0.8
    neem(6)
    return True


def add_item(kop, item, meet):
    """Add-menu in de kop, één item zonder submenu klikken (Text)."""
    p = ocr("Add Object", kop, woord=0)
    film["metingen"][meet + "_knop"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    q = yield from wacht_ocr(item, [max(0, p[0] - 150), p[1] + 20, 700, 900], p)
    film["metingen"][meet + "_item"] = q
    if not q:
        toets("Escape")
        return False
    yield from muis_naar(q[0], q[1], 14)
    neem(6)
    klik()
    yield 0.8
    neem(6)
    return True


MAP = "/tmp/tip12"


def stl_maat(pad):
    """Grootste maat per as van een binair STL (zonder eenheid: de getallen zoals ze in het bestand staan)."""
    import struct
    with open(pad, "rb") as f:
        data = f.read()
    n = struct.unpack("<I", data[80:84])[0]
    lo, hi = [1e30] * 3, [-1e30] * 3
    for i in range(n):
        b = 84 + i * 50 + 12
        for k in range(3):
            p = struct.unpack("<3f", data[b + 12 * k:b + 12 * k + 12])
            for j in range(3):
                lo[j], hi[j] = min(lo[j], p[j]), max(hi[j], p[j])
    return [round(hi[j] - lo[j], 4) for j in range(3)]


def maat_mm(ob):
    d = ob.dimensions
    return [round(d.x * 1000, 1), round(d.y * 1000, 1), round(d.z * 1000, 1)]


def maak_label():
    """Label van 60 x 30 x 4 mm met afgeronde hoeken en een gat (intern 0,06 x 0,03 x 0,004)."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.002))
    ob = bpy.context.view_layer.objects.active
    ob.name = "Label"
    ob.scale = (0.06, 0.03, 0.004)
    bpy.ops.object.transform_apply(scale=True)
    bv = ob.modifiers.new("hoek", "BEVEL")
    bv.width, bv.segments, bv.affect = 0.006, 6, "EDGES"
    bv.limit_method = "ANGLE"
    bpy.ops.mesh.primitive_cylinder_add(radius=0.0045, depth=0.02, location=(-0.021, 0, 0.002), vertices=48)
    gat = bpy.context.view_layer.objects.active
    selecteer(ob)
    bo = ob.modifiers.new("gat", "BOOLEAN")
    bo.object, bo.operation = gat, "DIFFERENCE"
    with bpy.context.temp_override(object=ob, active_object=ob):
        bpy.ops.object.modifier_apply(modifier="hoek")
        bpy.ops.object.modifier_apply(modifier="gat")
    bpy.data.objects.remove(gat, do_unlink=True)
    selecteer(ob)
    try:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(35))
    except Exception as f:  # noqa: BLE001
        log(f"glad kleuren lukte niet: {f}")
    m = bpy.data.materials.new("label")
    m.diffuse_color = (0.96, 0.62, 0.18, 1)
    ob.data.materials.append(m)
    selecteer(ob)
    return ob


def exporteer_script(pad, schaal):
    try:
        bpy.ops.wm.stl_export(filepath=pad, global_scale=schaal, export_selected_objects=True)
    except TypeError:
        bpy.ops.wm.stl_export(filepath=pad, global_scale=schaal)


def verloop():
    zet_scherm()
    os.makedirs(MAP, exist_ok=True)
    sc = bpy.context.scene
    # de valkuil: Unit Scale 1 (Blender rekent in meter), lengte getoond in millimeter
    sc.unit_settings.system = "METRIC"
    sc.unit_settings.scale_length = 1.0
    sc.unit_settings.length_unit = "MILLIMETERS"
    _, a = gebied("VIEW_3D")
    sp = a.spaces.active
    sp.overlay.grid_scale = 1.0
    sp.clip_start, sp.clip_end = 0.0005, 50.0
    yield 1.0
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [x for x in a.regions if x.type == "WINDOW"][0]
    with bpy.context.temp_override(window=w, area=a, region=reg):
        ob = maak_label()
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(MAP, "label.blend"))
    film["metingen"]["j_maat_blender_mm"] = maat_mm(ob)
    film["metingen"]["j_unit_scale"] = sc.unit_settings.scale_length
    # wat de gewone export schrijft (Scale 1): onzichtbaar, alleen om na te meten
    exporteer_script(os.path.join(MAP, "zonder.stl"), 1.0)
    film["metingen"]["j_stl_zonder"] = stl_maat(os.path.join(MAP, "zonder.stl"))
    log(f"KORT meting blender {film['metingen']['j_maat_blender_mm']} mm, stl zonder schaal {film['metingen']['j_stl_zonder']}")
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    _, tb = gebied("TOPBAR")
    bovenbalk = regio_rect(tb, "HEADER") if tb else [0, 0, 2160, 60]
    film["metingen"]["kop"], film["metingen"]["bovenbalk"] = kop, bovenbalk
    mid = Vector((0, 0, 0.002))
    cam(25, 58, 0.16, mid)
    yield 0.5
    if os.environ.get("CJ_KIJK"):
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        bpy.ops.wm.quit_blender()
        return
    yield from muis_naar(*zachte_muis_in_beeld(), 4)

    deel("j_mooi")      # haakbeeld: label draait langzaam, dichtbij
    yield from stuk(120, lambda t: cam(25 + 40 * t, 58 - 6 * t, 0.16 - 0.03 * t, mid))
    log("KORT OK j_mooi")

    deel("j_maat")      # N: Dimensions 60 x 30 x 4 mm
    toets("n")
    yield 0.8
    if not sp.show_region_ui:
        log("KORT vangnet j_maat: zijbalk via script")
        sp.show_region_ui = True
        herteken()
        yield 0.5
    neem(6)
    zb = regio_rect(a, "UI")
    film["metingen"]["j_zijbalk"] = zb
    film["metingen"]["j_dim_scherm"] = ocr("Dimensions", zb, "35%") if zb else None
    yield from houd(100)
    toets("n")
    yield 0.5
    sp.show_region_ui = False
    yield from stuk(40, lambda t: cam(65 - 30 * t, 52 + 4 * t, 0.13 + 0.03 * t, mid))
    log("KORT OK j_maat")

    deel("j_menu")      # File > Export > STL
    neem(6)
    voor = len(bpy.context.window_manager.windows)
    p = ocr("File", bovenbalk)  # run 12: tesseract zet "edit" voor "file" (blender-logo), dus alleen "File"
    film["metingen"]["j_file"] = p
    q = r = None
    if p:
        yield from muis_naar(p[0], p[1], 16)
        neem(4)
        klik()
        q = yield from wacht_ocr("Export", [max(0, p[0] - 100), p[1], 800, 1300], p)
        film["metingen"]["j_export"] = q
        if q:
            yield from muis_naar(q[0], q[1], 14)
            r = yield from wacht_ocr("STL", [q[0] + 100, max(0, q[1] - 400), 1000, 1300], q)
            film["metingen"]["j_stl_item"] = r
            if r:
                yield from muis_naar(q[0] + 330, q[1], 6)
                yield from muis_naar(r[0], r[1], 12)
                neem(6)
                klik()
                yield 1.5
                neem(10)
    if not r:
        toets("Escape")
        toets("Escape")
        log("KORT vangnet j_menu: menu niet gevonden")
    yield 0.3
    film["metingen"]["j_venster_open"] = (len(bpy.context.window_manager.windows) > voor or any(
        a.type == "FILE_BROWSER" for w in bpy.context.window_manager.windows for a in w.screen.areas))
    log("KORT OK j_menu")

    deel("j_venster")   # Scale 1000, Export STL
    via_venster = False
    doel = os.path.join(MAP, "label.stl")
    if os.path.exists(doel):
        os.remove(doel)
    if r and film["metingen"]["j_venster_open"]:
        yield from houd(12)
        s = None
        for _ in range(6):
            s = ocr("Scale", [0, 0, 2160, 1920], "35%")
            if s:
                break
            yield 0.5
            neem(2)
        film["metingen"]["j_scale_label"] = s
        if s:
            veld = (s[0] + 260, s[1])
            yield from muis_naar(*veld, 16)
            neem(6)
            xdo("click", "--repeat", "2", "1")
            MUIS["klik"] = 1
            yield 0.4
            neem(6)
            toets("ctrl+a")
            for c in "1000":
                toets(c)
                yield 0.15
                neem(5)
            yield from houd(14)
            toets("Return")
            yield 0.4
            neem(10)
            # run 12: witte tekst op de blauwe knop leest tesseract slecht; onderste strook, drie drempels, dan Cancel + 280
            onder = [1000, 1700, 1160, 220]
            e = None
            for dr in ("35%", "60%", "75%"):
                e = ocr("Export STL", onder, dr)
                if e:
                    break
            if not e:
                c = ocr("Cancel", onder, "35%") or ocr("Cancel", onder, "60%")
                if c:
                    e = (c[0] + 280, c[1])
            film["metingen"]["j_knop"] = e
            if e:
                yield from muis_naar(e[0], e[1], 16)
                neem(6)
                klik()
                yield 1.0
                neem(4)
                if not os.path.exists(doel) and any(
                        a.type == "FILE_BROWSER" for a in bpy.context.window_manager.windows[0].screen.areas):
                    klik()      # eerste klik sloot alleen het tekstveld af
            yield 1.5
            neem(8)
    if os.path.exists(doel):
        film["metingen"]["j_stl_met"] = stl_maat(doel)
        via_venster = abs(film["metingen"]["j_stl_met"][0] - 60) < 0.5
    film["metingen"]["j_via_venster"] = via_venster
    if not via_venster:
        log(f"KORT vangnet j_venster: export via script (bestand {os.path.exists(doel)})")
        for _ in range(3):
            if len(bpy.context.window_manager.windows) > 1 or any(
                    a.type == "FILE_BROWSER" for a in bpy.context.window_manager.windows[0].screen.areas):
                toets("Escape")
                yield 0.4
        exporteer_script(doel, 1000.0)
        film["metingen"]["j_stl_met"] = stl_maat(doel)
    log(f"KORT meting stl met schaal 1000 {film['metingen']['j_stl_met']}")
    yield from houd(10)
    log("KORT OK j_venster")

    deel("j_klaar")     # rustig eindbeeld
    yield from muis_naar(*zachte_muis_in_beeld(), 8)
    yield from stuk(150, lambda t: cam(35 + 50 * t, 56 - 8 * t, 0.16 - 0.035 * t, mid))
    yield from houd(30)
    log("KORT OK j_klaar")
    deel("eind")
    with open(os.path.join(uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


def stap_maker():
    gang = verloop()

    def stap():
        try:
            return next(gang)
        except StopIteration:
            return None
        except Exception as f:  # noqa: BLE001
            import traceback
            log(f"KORT FOUT {f}\n{traceback.format_exc()}")
            with open(os.path.join(uitmap, "film.json"), "w") as fh:
                json.dump(film, fh, indent=1)
            bpy.ops.wm.quit_blender()
            return None
    return stap


bpy.app.timers.register(stap_maker(), first_interval=3.0)
