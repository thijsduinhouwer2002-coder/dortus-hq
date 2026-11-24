"""Opname tip-reeks 9 (Regisseur run 10, 24 nov 2026): "je naam op een print". Echte Blender 5.3.0 op een X-scherm van
2160x1920, UI-schaal 2, geen add-on. Hulpcode gelijk aan ../regisseur-10/tip_opname.py.

Tip I "tekst": Add > Text (echte muis, menu via OCR). De tekst is 1 mm hoog (1 eenheid = 1 mm): S 20 Enter.
Tab, Backspace x4, typ HELLO, Tab. Van opzij: plat, dikte 0. Object > Convert > Mesh. Tab, A, E, 3, Enter, Tab:
letters 3 mm dik. N: Dimensions in de zijbalk. Gemeten: afmetingen voor en na (film.json metingen).

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
    print(f"[tip11] {t}", flush=True)


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
    pad = "/tmp/tip11_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", drempel,
                    "-negate", "/tmp/tip11_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip11_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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


def maat(ob):
    d = ob.dimensions
    return [round(d.x, 1), round(d.y, 1), round(d.z, 2)]


def verloop():
    zet_scherm()
    yield 1.0
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [r for r in a.regions if r.type == "WINDOW"][0]
    sp = a.spaces.active
    r3 = sp.region_3d
    sc = bpy.context.scene
    sc.cursor.location = (0, 0, 0)
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    film["metingen"]["kop"] = kop
    mid = Vector((30, 7, 0))
    cam(10, 50, 170, mid)
    yield 0.5
    if os.environ.get("CJ_KIJK"):
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        bpy.ops.wm.quit_blender()
        return

    deel("t_add")       # Add > Text
    neem(10)
    voor = set(sc.objects)
    via = yield from add_item(kop, "Text", "t_add")
    nieuw_ob = [o for o in sc.objects if o not in voor]
    film["metingen"]["t_add_menu"] = bool(via and nieuw_ob and nieuw_ob[0].type == "FONT")
    if not film["metingen"]["t_add_menu"]:
        log("KORT vangnet t_add: tekst via script")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.object.text_add(location=(0, 0, 0))
        yield 0.5
    ob = bpy.context.view_layer.objects.active
    m = bpy.data.materials.new("tekst")
    m.diffuse_color = (0.96, 0.62, 0.18, 1)
    ob.data.materials.append(m)
    herteken()
    film["metingen"]["t_maat_begin"] = maat(ob)
    yield from muis_naar(*zachte_muis_in_beeld(), 10)
    yield from houd(16)
    log("KORT OK t_add")

    deel("t_schaal")    # 1 mm hoog: S 20 Enter, camera zoomt mee
    yield from stuk(30, lambda t: cam(10, 50, 170 - 140 * t, Vector((1 + 0 * t, 0.3, 0))))
    neem(6)
    toets("s")
    yield 0.4
    neem(6)
    toets("2")
    toets("0")
    yield 0.4
    neem(10)
    toets("Return")
    yield 0.5
    neem(6)
    if abs(ob.scale.x - 20) > 0.1:
        log(f"KORT vangnet t_schaal: schaal {tuple(ob.scale)}, via script")
        ob.scale = (20, 20, 20)
        herteken()
        yield 0.4
    yield from stuk(40, lambda t: cam(10, 50, 30 + 140 * t, Vector((1 + 19 * t, 0.3 + 6.7 * t, 0))))
    film["metingen"]["t_maat_20"] = maat(ob)
    yield from houd(10)
    log("KORT OK t_schaal")

    deel("t_typ")       # Tab, Backspace x4, HELLO, Tab
    toets("Tab")
    yield 0.5
    neem(8)
    for _ in range(4):
        toets("BackSpace")
        yield 0.15
        neem(4)
    for c in "HELLO":
        toets("shift+" + c.lower())
        yield 0.15
        neem(5)
    yield 0.3
    neem(10)
    toets("Tab")
    yield 0.5
    if ob.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    film["metingen"]["t_body"] = ob.data.body
    if ob.data.body != "HELLO":
        log(f"KORT vangnet t_typ: tekst {ob.data.body!r}, via script")
        ob.data.body = "HELLO"
        herteken()
        yield 0.4
    bpy.context.view_layer.update()
    film["metingen"]["t_maat_hello"] = maat(ob)
    mid = Vector((ob.dimensions.x / 2, ob.dimensions.y / 2 - 1, 0))
    film["metingen"]["t_mid"] = list(mid)
    yield from stuk(24, lambda t: cam(10, 50, 170 - 30 * t, Vector((20, 7, 0)).lerp(mid, t)))
    yield from houd(10)
    log("KORT OK t_typ")

    deel("t_plat")      # van opzij: plat
    yield from stuk(70, lambda t: cam(10 + 10 * t, 50 + 39.5 * t, 140 - 30 * t, mid))
    yield from houd(40)
    yield from stuk(30, lambda t: cam(20 - 10 * t, 89.5 - 29.5 * t, 110 + 30 * t, mid))
    log("KORT OK t_plat")

    deel("t_conv")      # Object > Convert > Mesh
    neem(6)
    via = yield from kop_menu(kop, "Add Object", 1, "Convert", "Mesh", 900, "t_cv")
    film["metingen"]["t_conv_menu"] = bool(via and ob.type == "MESH")
    if ob.type != "MESH":
        log("KORT vangnet t_conv: omzetten via script")
        with bpy.context.temp_override(window=w, area=a, region=reg, selected_editable_objects=[ob], active_object=ob, object=ob):
            bpy.ops.object.convert(target="MESH")
        yield 0.5
    ob = bpy.context.view_layer.objects.active
    film["metingen"]["t_vlakken"] = len(ob.data.polygons)
    yield from muis_naar(*zachte_muis_in_beeld(), 10)
    yield from houd(24)
    log("KORT OK t_conv")

    deel("t_dik")       # Tab, A, E, 3, Enter, Tab
    toets("Tab")
    yield 0.5
    neem(8)
    toets("a")
    yield 0.4
    neem(8)
    vr = regio_rect(a)
    mx, my = vr[0] + int(vr[2] * 0.75), vr[1] + int(vr[3] * 0.30)
    yield from muis_naar(mx, my, 8)
    toets("e")
    yield 0.4
    neem(6)
    yield from muis_naar(mx + 30, my - 60, 8)
    toets("3")
    yield 0.4
    neem(12)
    toets("Return")
    yield 0.5
    neem(8)
    toets("Tab")
    yield 0.5
    if ob.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.context.view_layer.update()
    film["metingen"]["t_maat_dik_toets"] = maat(ob)
    if abs(ob.dimensions.z - 3.0) > 0.05:
        log(f"KORT vangnet t_dik: dikte {ob.dimensions.z}, via script")
        bm = bmesh.new()
        bm.from_mesh(ob.data)
        hoog = [v for v in bm.verts if abs(v.co.z) > 1e-5]
        if hoog:
            for v in hoog:
                v.co.z = 3.0 / ob.scale.z
        else:
            r = bmesh.ops.extrude_face_region(bm, geom=list(bm.faces))
            for v in [e for e in r["geom"] if isinstance(e, bmesh.types.BMVert)]:
                v.co.z += 3.0 / ob.scale.z
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(ob.data)
        bm.free()
        herteken()
        yield 0.4
    film["metingen"]["t_maat_dik"] = maat(ob)
    yield from stuk(60, lambda t: cam(10 + 25 * t, 60 + 8 * t, 140 - 20 * t, mid))
    yield from houd(16)
    log(f"KORT OK t_dik {film['metingen']['t_maat_dik']}")

    deel("t_maat")      # N: Dimensions in de zijbalk
    toets("n")
    yield 0.8
    if not sp.show_region_ui:
        log("KORT vangnet t_maat: zijbalk via script")
        sp.show_region_ui = True
        herteken()
        yield 0.5
    neem(6)
    zb = regio_rect(a, "UI")
    film["metingen"]["t_zijbalk"] = zb
    film["metingen"]["t_dim_scherm"] = ocr("Dimensions", zb, "35%") if zb else None
    yield from houd(90)
    toets("n")
    yield 0.5
    sp.show_region_ui = False
    log("KORT OK t_maat")

    deel("t_klaar")
    yield from stuk(140, lambda t: cam(35 - 50 * t, 68 - 6 * t, 120 + 10 * t, mid))
    yield from houd(40)
    log("KORT OK t_klaar")
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
