"""Opname tip-reeks deel 2 (Regisseur run 4, 23 nov 2026; tip-reeks naar het voorbeeld van Thijs, opdracht hoofdchat
17:45 NL). Echte Blender 5.3.0 op een X-scherm van 2160x1920, UI-schaal 2, alleen een 3D-weergave over het hele venster.
Geen add-on: de tips zijn gewoon Blender en hebben waarde zonder ons product. Hulpcode gelijk aan ../regisseur-3/.

Tip C "dikte": een vaas (eigen model) die maar één vlak dik is. Modifier-eigenschappen, Add Modifier > Generate >
Solidify met de echte muis (plekken via tesseract), Thickness 2 mm getypt, de rand is nu een echte wand.
Tip D "plat": een ei (eigen model) met een ronde onderkant. Edit Mode, puntselectie, vooraanzicht (numpad 1),
doorzicht (Alt Z), een kader om de onderste punten slepen, S Z 0 Enter: de onderkant is plat.

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
    print(f"[tip4] {t}", flush=True)


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
    pad = "/tmp/tip4_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", "60%",
                    "-negate", "/tmp/tip4_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip4_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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
    ob = draai_model("Egg", prof, (0.98, 0.72, 0.16, 1), seg=48)
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


def verloop():
    zet_scherm()
    yield 1.0
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)

    # ---------- tip C: wanddikte met Solidify ----------
    ob = vaas()
    selecteer(ob)
    herteken()
    yield 0.8
    film["metingen"]["c_maat_voor"] = eval_maat(ob)
    mid = Vector((0, 0, 70))
    rand = Vector((0, -29, 139))
    deel("c_heel")
    yield from stuk(70, lambda t: cam(160 + 70 * t, 62, 420, mid))
    log("KORT OK c_heel")
    deel("c_dun")
    yield from stuk(60, lambda t: cam(230 - 40 * t, 62 - 4 * t, 420 - 365 * t, mid.lerp(rand, t)))
    yield from houd(50)
    log("KORT OK c_dun")
    deel("c_mod")
    a.type = "PROPERTIES"
    sp = a.spaces.active
    try:
        sp.context = "MODIFIER"
    except Exception as f:  # noqa: BLE001
        log(f"context: {f}")
    herteken()
    yield 1.0
    neem(10)
    vak = regio_rect(a)
    film["metingen"]["c_props"] = vak
    via = yield from knop_menu("Add Modifier", "Generate", "Solidify", vak, "c")
    film["metingen"]["c_via_menu"] = via
    mods = [m for m in ob.modifiers if m.type == "SOLIDIFY"]
    if not mods:
        log("KORT vangnet c_mod: Solidify via script")
        mods = [ob.modifiers.new("Solidify", "SOLIDIFY")]
        herteken()
        yield 0.6
    sol = mods[0]
    neem(10)
    log(f"KORT OK c_mod via_menu {via}")
    deel("c_dik")
    yield 0.4
    th = yield from zoek("Thickness", vak)
    film["metingen"]["c_thickness"] = th
    if th:
        veld = (th[0] + 520, th[1])
        film["metingen"]["c_veld"] = veld
        yield from muis_naar(veld[0], veld[1], 14)
        neem(4)
        xdo("click", "--repeat", "2", "--delay", "80", "1")
        MUIS["klik"] = 1
        yield 0.5
        neem(6)
        toets("ctrl+a")
        yield 0.2
        neem(2)
        toets("2")
        yield 0.3
        neem(8)
        toets("Return")
        yield 0.6
        neem(6)
    film["metingen"]["c_dikte_ui"] = round(sol.thickness, 3)
    if abs(sol.thickness - 2.0) > 0.01:
        log(f"KORT vangnet c_dik: dikte {sol.thickness}, via script 2 mm")
        sol.thickness = 2.0
        herteken()
        yield 0.4
    yield from houd(40)
    log(f"KORT OK c_dik {sol.thickness}")
    a.type = "VIEW_3D"
    sp = a.spaces.active
    sp.show_region_ui = False
    cam(190, 58, 55, rand)
    herteken()
    yield 0.8
    deel("c_klaar")
    yield from houd(30)
    yield from stuk(70, lambda t: cam(190 + 50 * t, 58 + 4 * t, 55 + 365 * t, rand.lerp(mid, t)))
    film["metingen"]["c_maat_na"] = eval_maat(ob)
    film["metingen"]["c_offset"] = sol.offset
    yield from houd(30)
    log(f"KORT OK c_klaar maat {film['metingen']['c_maat_voor']} na {film['metingen']['c_maat_na']}")

    # ---------- tip D: platte onderkant ----------
    wis_scene()
    eg = ei()
    selecteer(eg)
    herteken()
    yield 0.8
    em = Vector((0, 0, 40))
    deel("d_heel")
    yield from stuk(70, lambda t: cam(150 + 60 * t, 86, 300, em))
    yield from houd(16)
    log("KORT OK d_heel")
    deel("d_edit")
    mx, my = zachte_muis_in_beeld()
    yield from muis_naar(mx, my, 10)
    toets("Tab")
    yield 0.6
    neem(10)
    toets("1")      # puntselectie
    yield 0.3
    neem(4)
    toets("alt+a")
    yield 0.3
    neem(4)
    toets("KP_1")
    yield 0.8
    neem(12)
    r3 = a.spaces.active.region_3d
    film["metingen"]["d_voor_ortho"] = r3.view_perspective
    if r3.view_perspective != "ORTHO":
        log("KORT vangnet d_edit: vooraanzicht via script")
        with bpy.context.temp_override(window=bpy.context.window_manager.windows[0], area=a,
                                       region=[r for r in a.regions if r.type == "WINDOW"][0]):
            bpy.ops.view3d.view_axis(type="FRONT")
        yield 0.6
    toets("alt+z")
    yield 0.6
    neem(10)
    film["metingen"]["d_xray"] = a.spaces.active.shading.show_xray
    if not a.spaces.active.shading.show_xray:
        log("KORT vangnet d_edit: X-ray via script")
        a.spaces.active.shading.show_xray = True
        herteken()
        yield 0.4
    # inzoomen zodat het ei groot staat (vooraanzicht blijft)
    with bpy.context.temp_override(window=bpy.context.window_manager.windows[0], area=a,
                                   region=[r for r in a.regions if r.type == "WINDOW"][0]):
        bpy.ops.view3d.view_selected()
    r3.view_location = Vector((0, 0, 40))
    r3.view_distance = 140
    herteken()
    yield 0.6
    neem(16)
    log(f"KORT {'OK' if eg.mode == 'EDIT' else 'FOUT'} d_edit")
    deel("d_kies")
    # schermplek van de onderste punten: projecteer z = 7 mm en z = -4 mm
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    reg = [r for r in a.regions if r.type == "WINDOW"][0]
    vr = regio_rect(a)
    p_hoog = location_3d_to_region_2d(reg, r3, Vector((-45, 0, 7.5)))
    p_laag = location_3d_to_region_2d(reg, r3, Vector((45, 0, -6)))
    x0, y0 = vr[0] + int(p_hoog.x), vr[1] + vr[3] - int(p_hoog.y)
    x1, y1 = vr[0] + int(p_laag.x), vr[1] + vr[3] - int(p_laag.y)
    film["metingen"]["d_box"] = [x0, y0, x1, y1]
    yield from muis_naar(x0, y0, 14)
    neem(4)
    xdo("mousedown", "1")
    MUIS["klik"] = 1
    yield 0.2
    yield from muis_naar(x1, y1, 24)
    neem(4)
    xdo("mouseup", "1")
    yield 0.6
    neem(10)
    bm = bmesh.from_edit_mesh(eg.data)
    gekozen = [v for v in bm.verts if v.select]
    film["metingen"]["d_gekozen"] = len(gekozen)
    if not gekozen or max(v.co.z for v in gekozen) > 9:
        log(f"KORT vangnet d_kies: {len(gekozen)} punten, kies via script z < 7,5 mm")
        for v in bm.verts:
            v.select_set(v.co.z < 7.5)
        bm.select_flush(True)
        bmesh.update_edit_mesh(eg.data)
        herteken()
        yield 0.4
        gekozen = [v for v in bm.verts if v.select]
    film["metingen"]["d_gekozen_na"] = len(gekozen)
    yield from houd(30)
    log(f"KORT OK d_kies {len(gekozen)}")
    deel("d_plat")
    mx2, my2 = vr[0] + int(vr[2] * 0.72), vr[1] + int(vr[3] * 0.40)
    yield from muis_naar(mx2, my2, 10)
    for k, n in (("s", 8), ("z", 8), ("0", 8)):
        toets(k)
        yield 0.3
        neem(n)
    toets("Return")
    yield 0.6
    neem(10)
    bm = bmesh.from_edit_mesh(eg.data)
    zs = [round(v.co.z, 2) for v in bm.verts if v.select]
    plat = max(zs) - min(zs) < 0.05 if zs else False
    if not plat:
        log("KORT vangnet d_plat: S Z 0 via script")
        gem = sum(v.co.z for v in bm.verts if v.select) / max(1, len(zs))
        for v in bm.verts:
            if v.select:
                v.co.z = gem
        bmesh.update_edit_mesh(eg.data)
        herteken()
        yield 0.4
    bm = bmesh.from_edit_mesh(eg.data)
    sel = [v for v in bm.verts if v.select]
    zvlak = sum(v.co.z for v in sel) / len(sel)
    breedte = max(v.co.x for v in sel) - min(v.co.x for v in sel)
    film["metingen"]["d_vlak_z"] = round(zvlak, 2)
    film["metingen"]["d_vlak_breed"] = round(breedte, 1)
    yield from houd(30)
    log(f"KORT OK d_plat z {zvlak:.2f} breed {breedte:.1f}")
    deel("d_klaar")
    toets("alt+z")
    yield 0.3
    a.spaces.active.shading.show_xray = False
    toets("Tab")
    yield 0.6
    eg.location.z = -zvlak     # op het bed zetten (de montage zegt dit niet als stap)
    film["metingen"]["d_hoogte_na"] = round(eg.dimensions.z, 1)
    herteken()
    neem(6)
    yield from stuk(80, lambda t: cam(0 + 40 * t, 90 + 14 * t, 160 + 60 * t, Vector((0, 0, 20 - 10 * t))))
    yield from houd(40)
    log("KORT OK d_klaar")
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
