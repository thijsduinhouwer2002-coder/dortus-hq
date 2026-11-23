"""Opname tip-reeks 6 (Regisseur run 7, 23 nov 2026): "olifantsvoet". Echte Blender 5.3.0 op een X-scherm van
2160x1920, UI-schaal 2, geen add-on. Hulpcode gelijk aan ../regisseur-6/tip_opname.py.

Tip F "voet": een bakje (eigen model, 60 x 40 x 22 mm) met een scherpe onderrand. Tab, 3 (vlakselectie), View > Viewpoint >
Bottom (echte menu's), klik op het ondervlak, Ctrl B, 0.5 getypt, Enter: een schuine rand (chamfer) van 0,5 mm rondom de
onderkant. Gemeten: het ondervlak wordt 1 mm smaller en korter, de rand 0,5 mm hoog.

Een stap die niet raakte, doet het script daarna zelf (log "KORT vangnet").
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python tip_opname.py -- <uitmap>
Uit: <uitmap>/beelden/bNNNNN.png, film.json (delen, muis, metingen), log-regels "KORT OK <deel>"."""
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
    print(f"[tip8] {t}", flush=True)


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


def ocr(tekst, vak):
    pad = "/tmp/tip8_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", "60%",
                    "-negate", "/tmp/tip8_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip8_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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
                s = ws[i:i + len(doel)]
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



# ---------- modellen ----------

def draai_model(naam, prof, kleur, dicht_boven=True, seg=64):
    """Draaiprofiel (r, z) in mm. Begint op de as onderaan; met dicht_boven=False blijft de bovenkant open (vaas)."""
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    ringen = []
    for r, z in prof:
        if r == 0:
            ringen.append([bm.verts.new((0, 0, z))])
        else:
            ringen.append([bm.verts.new((r * math.cos(2 * math.pi * i / seg), r * math.sin(2 * math.pi * i / seg), z))
                           for i in range(seg)])
    for a, b in zip(ringen, ringen[1:]):
        for i in range(seg):
            j = (i + 1) % seg
            if len(a) == 1:
                bm.faces.new((a[0], b[j], b[i]))
            elif len(b) == 1:
                bm.faces.new((a[i], a[j], b[0]))
            else:
                bm.faces.new((a[i], a[j], b[j], b[i]))
    bm.normal_update()
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    m = bpy.data.materials.new(naam.lower())
    m.diffuse_color = kleur
    me.materials.append(m)
    return ob


def vaas():
    """Vaas van 140 mm hoog, één vlak dik (geen wanddikte), bovenkant open."""
    prof = [(0, 0), (26, 0), (30, 4), (35, 18), (40, 40), (41, 58), (37, 80), (28, 104), (22, 118), (22, 128),
            (25, 136), (29, 140)]
    return draai_model("Vase", prof, (0.20, 0.42, 0.88, 1), dicht_boven=False)


def ei():
    """Ei van 80 mm hoog met een ronde onderkant (staat op één punt)."""
    prof = [(0, 0)]
    for i in range(1, 24):
        t = math.pi * i / 24
        z = 40 * (1 - math.cos(t))
        r = 29 * math.sin(t) * (1 - 0.12 * (z / 80))
        prof.append((r, z))
    prof.append((0, 80))
    ob = draai_model("Egg", prof, (1.0, 0.58, 0.22, 1), seg=48)
    return ob


def wis_scene():
    for o in list(bpy.context.scene.objects):
        bpy.data.objects.remove(o, do_unlink=True)


def eval_maat(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    e = ob.evaluated_get(dg)
    pts = [e.matrix_world @ Vector(c) for c in e.bound_box]
    return [round(max(p[i] for p in pts) - min(p[i] for p in pts), 1) for i in range(3)]


def knop_menu(naam_knop, naam_sub, naam_item, vak, meet):
    """Klik op een knop (OCR), hover een submenu, klik een item. Geeft True als het via de echte menu's ging."""
    p = yield from zoek(naam_knop, vak)
    film["metingen"][meet + "_knop"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    yield 0.7
    neem(6)
    w = bpy.context.window_manager.windows[0]
    groot_vak = [0, 0, w.width, w.height]
    q = yield from zoek(naam_sub, groot_vak)
    film["metingen"][meet + "_sub"] = q
    if not q:
        toets("Escape")
        return False
    yield from muis_naar(q[0], q[1], 14)
    yield 0.7
    neem(10)
    r = yield from zoek(naam_item, groot_vak)
    film["metingen"][meet + "_item"] = r
    if not r:
        toets("Escape")
        toets("Escape")
        return False
    yield from muis_naar(q[0] + 200, q[1], 5)
    yield from muis_naar(r[0], r[1], 12)
    neem(6)
    klik()
    yield 0.8
    neem(4)
    return True


def bal():
    """Bal van 40 mm, laag-poly (12 rondom, 8 stappen van pool tot pool): 72 vierkanten en 24 driehoeken = 96 vlakken.
    Shade Smooth staat aan, dus in Blender lijkt hij rond."""
    prof = [(0, 0)]
    for i in range(1, 8):
        t = math.pi * i / 8
        prof.append((20 * math.sin(t), 20 * (1 - math.cos(t))))
    prof.append((0, 40))
    return draai_model("Ball", prof, (0.10, 0.70, 0.62, 1), seg=12)


def menu_klik(tekst, vak):
    p = yield from zoek(tekst, vak)
    if not p:
        return None
    yield from muis_naar(p[0], p[1], 12)
    neem(6)
    klik()
    yield 0.7
    neem(6)
    return p



def view_bottom(kop):
    """View-menu in de kop van de 3D-weergave > Viewpoint > Bottom, met de echte muis. Zoekt elk menu in een klein vak
    vlak onder of naast de knop, en wacht tot het menu echt getekend is (meerdere pogingen, muis een tikje bewegen)."""
    p = yield from zoek("View", kop)
    film["metingen"]["f_view_knop"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    q = None
    for i in range(10):
        yield 0.4
        xdo("mousemove", str(p[0] + (i % 2) * 2), str(p[1]))
        neem(2)
        q = ocr("Viewpoint", [max(0, p[0] - 150), p[1], 900, 1000])
        if q:
            break
    film["metingen"]["f_viewpoint"] = q
    if not q:
        toets("Escape")
        return False
    yield from muis_naar(q[0], q[1], 14)
    r = None
    for i in range(10):
        yield 0.4
        xdo("mousemove", str(q[0] + (i % 2) * 2), str(q[1]))
        neem(2)
        r = ocr("Bottom", [q[0] + 100, max(0, q[1] - 100), 900, 700])
        if r:
            break
    film["metingen"]["f_bottom"] = r
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


def bakje():
    """Bakje van 60 x 40 x 22 mm, wanden 3 mm, bak 18 mm diep. Vlakke kleur, scherpe randen."""
    me = bpy.data.meshes.new("Tray")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * 60, v.co.y * 40, (v.co.z + 0.5) * 22))
    boven = [f for f in bm.faces if f.normal.z > 0.9][0]
    r = bmesh.ops.inset_individual(bm, faces=[boven], thickness=3.0, depth=0.0)
    binnen = boven
    bmesh.ops.translate(bm, vec=(0, 0, -18), verts=list(binnen.verts))
    bm.normal_update()
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("Tray", me)
    bpy.context.scene.collection.objects.link(ob)
    m = bpy.data.materials.new("tray")
    m.diffuse_color = (0.95, 0.42, 0.22, 1)
    me.materials.append(m)
    return ob


def onder_maat(ob):
    """Breedte en diepte van het ondervlak (punten op z < 0,01) en de hoogte van de schuine rand."""
    me = ob.data
    if ob.mode == "EDIT":
        bm = bmesh.from_edit_mesh(me)
        vs = [v.co.copy() for v in bm.verts]
    else:
        vs = [v.co.copy() for v in me.vertices]
    laag = [v for v in vs if v.z < 0.01]
    bx = max(v.x for v in laag) - min(v.x for v in laag)
    by = max(v.y for v in laag) - min(v.y for v in laag)
    # rand: laagste punt op de volle breedte (x = 30)
    vol = [v.z for v in vs if abs(abs(v.x) - 30) < 0.01]
    return round(bx, 2), round(by, 2), round(min(vol), 2) if vol else None


def verloop():
    zet_scherm()
    yield 1.0
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [r for r in a.regions if r.type == "WINDOW"][0]
    from bpy_extras.view3d_utils import location_3d_to_region_2d

    ob = bakje()
    selecteer(ob)
    herteken()
    yield 0.8
    film["metingen"]["f_onder_voor"] = onder_maat(ob)
    film["metingen"]["f_vlakken_voor"] = len(ob.data.polygons)
    mid = Vector((0, 0, 9))
    hoek = Vector((30, -20, 0))

    deel("f_heel")
    yield from stuk(80, lambda t: cam(30 + 50 * t, 66 + 12 * t, 190 - 40 * t, mid))
    yield from houd(16)
    log("KORT OK f_heel")

    deel("f_rand")   # dichtbij de scherpe onderrand, van opzij
    yield from stuk(70, lambda t: cam(40 + 25 * t, 82, 150 - 30 * t, mid.lerp(hoek, 0.35 + 0.15 * t)))
    yield from houd(14)
    log("KORT OK f_rand")

    deel("f_edit")
    cam(60, 74, 170, mid)
    yield 0.4
    neem(6)
    mx, my = zachte_muis_in_beeld()
    yield from muis_naar(mx, my, 10)
    neem(4)
    toets("Tab")
    yield 0.6
    neem(10)
    toets("3")      # vlakselectie
    yield 0.4
    neem(8)
    toets("alt+a")
    yield 0.3
    neem(10)
    film["metingen"]["f_mode"] = ob.mode
    film["metingen"]["f_vlakmodus"] = tuple(bpy.context.tool_settings.mesh_select_mode)
    if ob.mode != "EDIT":
        log("KORT vangnet f_edit: Edit Mode via script")
        bpy.ops.object.mode_set(mode="EDIT")
        yield 0.4
    if not bpy.context.tool_settings.mesh_select_mode[2]:
        log("KORT vangnet f_edit: vlakselectie via script")
        bpy.context.tool_settings.mesh_select_mode = (False, False, True)
        yield 0.3
    yield from houd(12)
    log("KORT OK f_edit")

    deel("f_onder")
    kop = regio_rect(a, "HEADER")
    film["metingen"]["f_kop"] = kop
    via = yield from view_bottom(kop)
    yield 0.8     # het draaien naar het onderaanzicht duurt even (smooth view)
    r3 = a.spaces.active.region_3d
    film["metingen"]["f_onder_z"] = round(r3.view_rotation.to_matrix().col[2].z, 3)
    film["metingen"]["f_onder_menu"] = bool(via and (r3.view_rotation.to_matrix().col[2] - Vector((0, 0, -1))).length < 0.05)
    if not film["metingen"]["f_onder_menu"]:
        log("KORT vangnet f_onder: onderaanzicht via script")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.view3d.view_axis(type="BOTTOM")
        yield 0.6
    r3.view_location = Vector((0, 0, 0))
    r3.view_distance = 95
    herteken()
    yield 0.5
    neem(10)
    vr = regio_rect(a)
    p = location_3d_to_region_2d(reg, r3, Vector((-8, 6, 0)))
    kx, ky = vr[0] + int(p.x), vr[1] + vr[3] - int(p.y)
    film["metingen"]["f_klik"] = [kx, ky]
    yield from muis_naar(kx, ky, 14)
    neem(6)
    klik()
    yield 0.6
    neem(12)
    bm = bmesh.from_edit_mesh(ob.data)
    gekozen = [f for f in bm.faces if f.select]
    goed = len(gekozen) == 1 and gekozen[0].normal.z < -0.9
    film["metingen"]["f_klik_goed"] = goed
    if not goed:
        log(f"KORT vangnet f_onder: {len(gekozen)} vlakken, ondervlak via script")
        for f in bm.faces:
            f.select_set(f.normal.z < -0.9 and f.calc_center_median().z < 0.01)
        bm.select_flush_mode()
        bmesh.update_edit_mesh(ob.data)
        herteken()
        yield 0.4
    yield from houd(20)
    log("KORT OK f_onder")

    deel("f_bevel")
    mx2, my2 = vr[0] + int(vr[2] * 0.70), vr[1] + int(vr[3] * 0.30)
    yield from muis_naar(mx2, my2, 10)
    neem(4)
    toets("ctrl+b")
    yield 0.5
    neem(6)
    yield from muis_naar(mx2 - 60, my2 + 40, 10)   # even de live rand laten zien
    neem(4)
    for k in ("0", "period", "5"):
        toets(k)
        yield 0.3
        neem(6)
    neem(6)
    toets("Return")
    yield 0.7
    neem(10)
    m = onder_maat(ob)
    film["metingen"]["f_onder_na_toets"] = m
    goed = m[0] is not None and abs(m[0] - 59.0) < 0.05 and abs(m[1] - 39.0) < 0.05
    film["metingen"]["f_bevel_toets"] = goed
    if not goed:
        log(f"KORT vangnet f_bevel: maat {m}, opnieuw via script")
        bpy.ops.ed.undo()
        yield 0.5
        bm = bmesh.from_edit_mesh(ob.data)
        onder = [f for f in bm.faces if f.normal.z < -0.9 and f.calc_center_median().z < 0.01]
        randen = list(onder[0].edges) if onder else []
        bmesh.ops.bevel(bm, geom=randen, offset=0.5, segments=1, affect="EDGES")
        bmesh.update_edit_mesh(ob.data)
        herteken()
        yield 0.5
    m = onder_maat(ob)
    film["metingen"]["f_onder_na"] = m
    yield from houd(24)
    log(f"KORT OK f_bevel ondervlak {m}")

    deel("f_klaar")
    # eerst in Edit Mode: de nieuwe schuine vlakken zijn oranje gekozen; van onder naar een lage hoek
    bm = bmesh.from_edit_mesh(ob.data)
    for f in bm.faces:
        n = f.normal
        f.select_set(n.z < -0.2 and n.z > -0.9)
    bm.select_flush_mode()
    bmesh.update_edit_mesh(ob.data)
    herteken()
    yield 0.3
    neem(4)
    yield from stuk(90, lambda t: cam(0 + 40 * t, 180 - 72 * t, 95 + 15 * t, mid.lerp(hoek, 0.5 * t) * (1 - 0.5 * t)))
    yield from houd(24)
    toets("Tab")
    yield 0.6
    if ob.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    film["metingen"]["f_vlakken_na"] = len(ob.data.polygons)
    film["metingen"]["f_onder_eind"] = onder_maat(ob)
    neem(6)
    yield from stuk(80, lambda t: cam(40 + 30 * t, 108 - 38 * t, 110 + 60 * t, mid.lerp(hoek, 0.25 * (1 - t))))
    yield from houd(40)
    log(f"KORT OK f_klaar {film['metingen']['f_onder_voor']} naar {film['metingen']['f_onder_eind']}")
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
