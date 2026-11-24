"""Opname tip-reeks 8 (Regisseur run 9, 24 nov 2026): "valt je print om?". Echte Blender 5.3.0 op een X-scherm van
2160x1920, UI-schaal 2, geen add-on. Hulpcode gelijk aan ../regisseur-9/tip_opname.py.

Tip H "val": een scheve toren (eigen model, 80 mm). Object > Set Origin > Origin to Center of Mass (Volume): de oranje
stip springt naar het zwaartepunt. View > Viewpoint > Front: de stip staat buiten de voet. Tab, 3, View > Viewpoint >
Bottom, klik op het ondervlak, S 3 Enter: voet drie keer zo breed. Tab, Front, opnieuw Set Origin: stip binnen de voet.
Gemeten: x van het zwaartepunt tegenover de voet, voor en na. Oorsprong-stip groter via Voorkeuren > Themes (object_origin_size).

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
    print(f"[tip10] {t}", flush=True)


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
    pad = "/tmp/tip10_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", drempel,
                    "-negate", "/tmp/tip10_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip10_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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





# ---------- tip "val": valt je print om? ----------

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
    """Menu in de kop van de 3D-weergave (knop via OCR), submenu hoveren, item klikken. True als het zo ging."""
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


def toren():
    """Scheve toren (eigen model): 16 rondom, 80 mm hoog, boven breder (r 12 naar 16 mm) en 0,45 mm opzij per mm hoogte.
    Onder en boven elk één vlak (ngon), zodat je het ondervlak in één klik kiest."""
    ringen = [(0, 12.0), (25, 12.5), (50, 14.0), (68, 16.0), (80, 15.0)]
    seg = 16
    me = bpy.data.meshes.new("Tower")
    bm = bmesh.new()
    rs = []
    for z, r in ringen:
        rs.append([bm.verts.new((r * math.cos(2 * math.pi * i / seg) + 0.45 * z, r * math.sin(2 * math.pi * i / seg), z))
                   for i in range(seg)])
    for a, b in zip(rs, rs[1:]):
        for i in range(seg):
            j = (i + 1) % seg
            bm.faces.new((a[i], a[j], b[j], b[i]))
    bm.faces.new(list(reversed(rs[0])))
    bm.faces.new(rs[-1])
    bm.normal_update()
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("Tower", me)
    bpy.context.scene.collection.objects.link(ob)
    m = bpy.data.materials.new("tower")
    m.diffuse_color = (0.96, 0.62, 0.18, 1)
    me.materials.append(m)
    return ob


def balans(ob):
    """Oorsprong (na Set Origin: het zwaartepunt) tegenover de voet: x van de stip, voet van x-min tot x-max (wereld, mm)."""
    mw = ob.matrix_world
    if ob.mode == "EDIT":
        vs = [mw @ v.co for v in bmesh.from_edit_mesh(ob.data).verts]
    else:
        vs = [mw @ v.co for v in ob.data.vertices]
    laag = [v for v in vs if v.z < 0.01]
    x0, x1 = min(v.x for v in laag), max(v.x for v in laag)
    c = ob.location
    return {"stip": [round(c.x, 1), round(c.y, 1), round(c.z, 1)], "voet_x": [round(x0, 1), round(x1, 1)],
            "binnen": bool(x0 <= c.x <= x1)}


def zwaartepunt_script(ob):
    with bpy.context.temp_override(selected_editable_objects=[ob], active_object=ob, object=ob):
        bpy.ops.object.origin_set(type="ORIGIN_CENTER_OF_VOLUME")


def view_punt(kop, punt, meet):
    p = ocr("View", kop)
    film["metingen"][meet + "_knop"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    q = yield from wacht_ocr("Viewpoint", [max(0, p[0] - 150), p[1], 900, 1000], p)
    film["metingen"][meet + "_viewpoint"] = q
    if not q:
        toets("Escape")
        return False
    yield from muis_naar(q[0], q[1], 14)
    r = yield from wacht_ocr(punt, [q[0] + 100, max(0, q[1] - 300), 900, 900], q)
    film["metingen"][meet + "_item"] = r
    if not r:
        toets("Escape")
        toets("Escape")
        return False
    yield from muis_naar(q[0] + 330, q[1], 6)
    yield from muis_naar(r[0], r[1], 10)
    neem(6)
    klik()
    yield 0.8
    neem(6)
    return True


def verloop():
    zet_scherm()
    yield 1.0
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [r for r in a.regions if r.type == "WINDOW"][0]
    sp = a.spaces.active
    r3 = sp.region_3d
    from bpy_extras.view3d_utils import location_3d_to_region_2d

    def scherm(pt):
        vr = regio_rect(a)
        q = location_3d_to_region_2d(reg, r3, Vector(pt))
        return [vr[0] + int(q.x), vr[1] + vr[3] - int(q.y)] if q else None

    ob = toren()
    selecteer(ob)
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    film["metingen"]["kop"] = kop
    film["metingen"]["v_voor"] = balans(ob)
    mid = Vector((14, 0, 38))
    if os.environ.get("CJ_KIJK"):
        cam(20, 72, 230, mid)
        yield 0.5
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        bpy.ops.wm.quit_blender()
        return

    deel("v_heel")      # de scheve toren draait rustig, dichterbij
    yield from stuk(100, lambda t: cam(-25 + 40 * t, 82 - 4 * t, 250 - 60 * t, mid))
    yield from houd(14)
    log("KORT OK v_heel")

    deel("v_origin")    # Object > Set Origin > Origin to Center of Mass (Volume)
    cam(15, 78, 190, mid)
    yield 0.3
    neem(6)
    via = yield from kop_menu(kop, "Add Object", 1, "Set Origin", "Mass Volume", 1100, "v_or")
    film["metingen"]["v_origin_menu"] = bool(via)
    na = balans(ob)
    if not via or na["stip"][2] < 5:
        log(f"KORT vangnet v_origin: {na}, zwaartepunt via script")
        zwaartepunt_script(ob)
        herteken()
        yield 0.5
    film["metingen"]["v_stip"] = balans(ob)
    yield from muis_naar(*zachte_muis_in_beeld(), 12)
    yield from houd(30)
    log(f"KORT OK v_origin {film['metingen']['v_stip']}")

    deel("v_front")     # View > Viewpoint > Front: stip buiten de voet
    via = yield from view_punt(kop, "Front", "v_fr")
    yield 0.8
    voor = r3.view_rotation.to_matrix().col[2]
    film["metingen"]["v_front_menu"] = bool(via and (voor - Vector((0, -1, 0))).length < 0.05)
    if not film["metingen"]["v_front_menu"]:
        log("KORT vangnet v_front: vooraanzicht via script")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.view3d.view_axis(type="FRONT")
        yield 0.6
    r3.view_location = Vector((14, 0, 40))
    r3.view_distance = 150
    herteken()
    yield 0.5
    yield from muis_naar(*zachte_muis_in_beeld(), 10)
    neem(4)
    film["metingen"]["v_stip_scherm"] = scherm(ob.location)
    b = balans(ob)
    film["metingen"]["v_rand_scherm"] = scherm((b["voet_x"][1], 0, 0))
    yield from houd(70)
    log("KORT OK v_front")

    deel("v_edit")
    toets("Tab")
    yield 0.6
    neem(10)
    toets("3")
    yield 0.4
    neem(8)
    toets("alt+a")
    yield 0.3
    neem(8)
    if ob.mode != "EDIT":
        log("KORT vangnet v_edit: Edit Mode via script")
        bpy.ops.object.mode_set(mode="EDIT")
        yield 0.4
    if not bpy.context.tool_settings.mesh_select_mode[2]:
        log("KORT vangnet v_edit: vlakselectie via script")
        bpy.context.tool_settings.mesh_select_mode = (False, False, True)
        yield 0.3
    yield from houd(8)
    log("KORT OK v_edit")

    deel("v_onder")
    via = yield from view_punt(kop, "Bottom", "v_on")
    yield 0.8
    onder = (r3.view_rotation.to_matrix().col[2] - Vector((0, 0, -1))).length < 0.05
    film["metingen"]["v_onder_menu"] = bool(via and onder)
    if not onder:
        log("KORT vangnet v_onder: onderaanzicht via script")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.view3d.view_axis(type="BOTTOM")
        yield 0.6
    r3.view_location = Vector((14, 0, 0))
    r3.view_distance = 150
    herteken()
    yield 0.5
    neem(8)
    k = scherm((-3, 4, 0))
    film["metingen"]["v_klik"] = k
    yield from muis_naar(k[0], k[1], 14)
    neem(6)
    klik()
    yield 0.6
    neem(10)
    bm = bmesh.from_edit_mesh(ob.data)
    gekozen = [f for f in bm.faces if f.select]
    goed = len(gekozen) == 1 and gekozen[0].normal.z < -0.9
    film["metingen"]["v_klik_goed"] = goed
    if not goed:
        log(f"KORT vangnet v_onder: {len(gekozen)} vlakken, ondervlak via script")
        for f in bm.faces:
            f.select_set(f.normal.z < -0.9)
        bm.select_flush_mode()
        bmesh.update_edit_mesh(ob.data)
        herteken()
        yield 0.4
    yield from houd(14)
    log("KORT OK v_onder")

    deel("v_schaal")    # S, 3, Enter
    vr = regio_rect(a)
    mx, my = vr[0] + int(vr[2] * 0.80), vr[1] + int(vr[3] * 0.25)
    yield from muis_naar(mx, my, 10)
    neem(4)
    toets("s")
    yield 0.5
    neem(6)
    yield from muis_naar(mx + 60, my - 40, 10)
    toets("3")
    yield 0.4
    neem(10)
    toets("Return")
    yield 0.6
    neem(8)
    b = balans(ob)
    breed = b["voet_x"][1] - b["voet_x"][0]
    film["metingen"]["v_voet_na_toets"] = round(breed, 1)
    if abs(breed - 72.0) > 0.5:
        log(f"KORT vangnet v_schaal: voet {breed}, via script")
        bpy.ops.ed.undo()
        yield 0.4
        bm = bmesh.from_edit_mesh(ob.data)
        vs = [v for v in bm.verts if v.co.z < 0.01]
        for v in vs:
            v.co.x *= 3
            v.co.y *= 3
        bmesh.update_edit_mesh(ob.data)
        herteken()
        yield 0.4
    yield from stuk(40, lambda t: cam(0 + 30 * t, 180 - 60 * t, 150 + 30 * t, Vector((14, 0, 20 * t))))
    yield from houd(14)
    log("KORT OK v_schaal")

    deel("v_terug")     # Tab, Front, opnieuw Set Origin: stip nu binnen de voet
    toets("Tab")
    yield 0.6
    if ob.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    neem(6)
    via = yield from view_punt(kop, "Front", "v_fr2")
    yield 0.8
    if (r3.view_rotation.to_matrix().col[2] - Vector((0, -1, 0))).length > 0.05:
        log("KORT vangnet v_terug: vooraanzicht via script")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.view3d.view_axis(type="FRONT")
        yield 0.6
    r3.view_location = Vector((14, 0, 40))
    r3.view_distance = 150
    herteken()
    yield 0.4
    neem(6)
    oud = ob.location.copy()
    via = yield from kop_menu(kop, "Add Object", 1, "Set Origin", "Mass Volume", 1100, "v_or2")
    film["metingen"]["v_origin2_menu"] = bool(via)
    if not via or (ob.location - oud).length < 0.5:
        log("KORT vangnet v_terug: zwaartepunt via script")
        zwaartepunt_script(ob)
        herteken()
        yield 0.5
    yield from muis_naar(*zachte_muis_in_beeld(), 10)
    film["metingen"]["v_na"] = balans(ob)
    film["metingen"]["v_stip2_scherm"] = scherm(ob.location)
    yield from houd(60)
    log(f"KORT OK v_terug {film['metingen']['v_na']}")

    deel("v_klaar")
    yield from stuk(120, lambda t: cam(0 + 50 * t, 90 - 14 * t, 150 + 60 * t, Vector((14, 0, 40 - 4 * t))))
    yield from houd(60)
    log("KORT OK v_klaar")
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
