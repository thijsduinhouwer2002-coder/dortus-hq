"""Opname tip-reeks (Regisseur run 3, 23 nov 2026; opdracht hoofdchat 17:45 NL naar het voorbeeld van Thijs).
Echte Blender 5.3.0 op een X-scherm van 2160x1920, UI-schaal 2, alleen een 3D-weergave over het hele venster.
Geen add-on: de tips zijn gewoon Blender en hebben waarde zonder ons product.

Tip A "gat": een schaakpion (eigen model, gemaakt in dit script) met een gat in de kop. Edit Mode, randen, alles uit,
menu Select > Select All by Trait > Non Manifold (echte muis, plekken via tesseract), de rand van het gat licht op,
F vult het gat, opnieuw zoeken: niets licht op.
Tip B "maat": dezelfde pion op 31 cm hoog naast een doos van 220 x 220 x 250 mm (het printbed). Eenheden in mm
(Scene, Units), N-paneel met Dimensions, S 0.6 Enter, de pion past in de doos.

Elk filmbeeld is een schermafbeelding van het hele X-scherm (import -window root). De muis staat niet op een
X-schermafbeelding; per beeld komt de plek van de echte muis in film.json, de montage tekent het pijltje.
Een klik die niet raakte, doet het script daarna zelf (log "KORT vangnet").
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
    print(f"[tip] {t}", flush=True)


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
    pad = "/tmp/tip_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", "60%",
                    "-negate", "/tmp/tip_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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


# ---------- scène ----------

def pion(hoogte_mm=310.0, gat=True):
    """Schaakpion als draaiprofiel (r, z) in mm, dicht van onder tot boven. Met gat: vier vlakken in de kop weg."""
    prof = [(0, 0), (30, 0), (30, 6), (27, 10), (27, 14), (22, 20), (14, 34), (11, 52), (10, 66), (16, 70), (16, 74),
            (10, 77), (14, 84), (16.5, 92), (16, 100), (13.5, 107), (9, 112), (4, 114.5), (0, 115)]
    k = hoogte_mm / 115.0
    me = bpy.data.meshes.new("Pawn")
    bm = bmesh.new()
    seg = 48
    ringen = []
    for r, z in prof:
        if r == 0:
            ringen.append([bm.verts.new((0, 0, z * k))])
        else:
            ringen.append([bm.verts.new((r * k * math.cos(2 * math.pi * i / seg), r * k * math.sin(2 * math.pi * i / seg),
                                         z * k)) for i in range(seg)])
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
    if gat:
        # gat: acht vlakken in de kop (ringen 12 tot 14, segmenten 1 tot 5), rond 22,5 graden
        band = set(v for r in ringen[12:15] for v in r[1:6])
        weg = [f for f in bm.faces if all(v in band for v in f.verts)]
        bmesh.ops.delete(bm, geom=weg, context="FACES_ONLY")
        film["metingen"]["gat_vlakken"] = len(weg)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new("Pawn", me)
    bpy.context.scene.collection.objects.link(ob)
    m = bpy.data.materials.new("pawn")
    m.diffuse_color = (0.95, 0.42, 0.12, 1)
    me.materials.append(m)
    return ob


def bed():
    """Doos 220 x 220 x 250 mm, alleen draden: het printbed met zijn bouwhoogte."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 125))
    ob = bpy.context.active_object
    ob.name = "Print bed 220x220x250"
    ob.scale = (220, 220, 250)
    bpy.ops.object.transform_apply(scale=True)
    ob.display_type = "WIRE"
    ob.show_name = False
    ob.hide_select = True
    return ob


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


def menu_non_manifold(naam):
    """Select > Select All by Trait > Non Manifold met de echte muis. Geeft True als het via het menu ging."""
    _, a = gebied("VIEW_3D")
    kop = regio_rect(a, "HEADER")
    p = yield from zoek("Select", kop)
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 14)
    neem()
    klik()
    yield 0.6
    neem(4)
    vak = [kop[0], kop[1] + kop[3], 1300, 1400]
    q = yield from zoek("All by Trait", vak)
    if not q:
        toets("Escape")
        return False
    film["metingen"][naam + "_trait"] = q
    yield from muis_naar(q[0], q[1], 14)
    yield 0.6
    neem(8)
    vak2 = [q[0] - 100, q[1] - 300, 1400, 900]
    r = yield from zoek("Non Manifold", vak2)
    if not r:
        toets("Escape")
        toets("Escape")
        return False
    film["metingen"][naam + "_nm"] = r
    yield from muis_naar(q[0] + 260, q[1], 6)
    yield from muis_naar(r[0], r[1], 12)
    neem(6)
    klik()
    yield 0.6
    neem(2)
    return True


def verloop():
    zet_scherm()
    yield 1.0
    ob = pion(310.0, gat=True)
    selecteer(ob)
    herteken()
    yield 0.8
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)
    film["metingen"]["kop"] = regio_rect(a, "HEADER")
    mid = Vector((0, 0, 160))
    gat_punt = Vector((41, 17, 262))   # vier vlakken rond 22,5 graden op de kop

    # ---------- tip A: gat zoeken en dichten ----------
    deel("a_heel")
    yield from stuk(70, lambda t: cam(150 + 60 * t, 74, 640, mid))
    log("KORT OK a_heel")
    deel("a_edit")
    mx, my = zachte_muis_in_beeld()
    yield from muis_naar(mx, my, 10)
    toets("Tab")
    yield 0.6
    neem(10)
    toets("2")
    yield 0.4
    neem(8)
    toets("alt+a")
    yield 0.5
    neem(14)
    log(f"KORT {'OK' if ob.mode == 'EDIT' else 'FOUT'} a_edit")
    deel("a_menu")
    via_menu = yield from menu_non_manifold("a")
    if not via_menu:
        log("KORT vangnet a_menu: sneltoets shift+ctrl+alt+m")
        yield from muis_naar(mx, my, 8)
        toets("shift+ctrl+alt+m")
        yield 0.6
        neem(10)
    film["metingen"]["a_via_menu"] = via_menu
    yield 0.4
    n = nonmanifold_tellen(ob)
    if n == 0:
        log("KORT vangnet a_menu: operator via script")
        with bpy.context.temp_override(window=bpy.context.window_manager.windows[0], area=a):
            bpy.ops.mesh.select_non_manifold()
        n = nonmanifold_tellen(ob)
    film["metingen"]["a_randen"] = n
    neem(6)
    log(f"KORT {'OK' if n > 0 else 'FOUT'} a_menu randen {n}")
    deel("a_licht")
    yield from muis_naar(mx, my, 8)
    yield from stuk(60, lambda t: cam(210 - 98 * t, 74 + 4 * t, 640 - 330 * t, mid.lerp(gat_punt, t)))
    yield from houd(40)
    log("KORT OK a_licht")
    deel("a_vul")
    toets("f")
    yield 0.6
    neem(16)
    bm = bmesh.from_edit_mesh(ob.data)
    film["metingen"]["a_vlakken_na_f"] = len(bm.faces)
    yield from houd(30)
    deel("a_weer")
    toets("alt+a")
    yield 0.4
    neem(6)
    toets("shift+ctrl+alt+m")
    yield 0.6
    neem(6)
    n2 = nonmanifold_tellen(ob)
    film["metingen"]["a_randen_na"] = n2
    yield from stuk(60, lambda t: cam(112 + 48 * t, 78 - 4 * t, 310 + 330 * t, gat_punt.lerp(mid, t)))
    log(f"KORT {'OK' if n2 == 0 else 'FOUT'} a_weer randen {n2}")
    toets("Tab")
    yield 0.6
    neem(20)

    # ---------- tip B: past het op je printer? ----------
    bed_ob = bed()
    selecteer(ob)
    bed_ob.select_set(False)
    herteken()
    yield 0.5
    deel("b_heel")
    big = Vector((0, 0, 170))
    yield from stuk(80, lambda t: cam(200 + 40 * t, 72, 820, big))
    log("KORT OK b_heel")
    # eenheden: het gebied even als Properties, tab Scene, paneel Units
    deel("b_units")
    a.type = "PROPERTIES"
    sp = a.spaces.active
    try:
        sp.context = "SCENE"
    except Exception as f:  # noqa: BLE001
        log(f"context: {f}")
    herteken()
    yield 0.8
    neem(4)
    vak = regio_rect(a)
    un = yield from zoek("Units", vak)
    film["metingen"]["b_units_kop"] = un
    if un:
        yield from muis_naar(un[0], un[1], 16)
        neem(4)
        klik()
        yield 0.6
        neem(6)
    u = yield from zoek("Unit Scale", vak)
    film["metingen"]["b_unitscale"] = u
    lu = yield from zoek("Length", vak)
    film["metingen"]["b_length"] = lu
    if u:
        yield from muis_naar(u[0] + 500, u[1], 16)
    yield from houd(50)
    log(f"KORT {'OK' if u else 'FOUT'} b_units")
    a.type = "VIEW_3D"
    herteken()
    yield 0.6
    sp = a.spaces.active
    sp.show_region_ui = True
    herteken()
    yield 0.8
    deel("b_maat")
    ui = regio_rect(a, "UI")
    film["metingen"]["b_ui"] = ui
    yield from stuk(30, lambda t: cam(240, 72, 820, big))
    d = yield from zoek("Dimensions", ui)
    film["metingen"]["b_dimensions"] = d
    z = yield from zoek("Z", [ui[0], (d[1] if d else ui[1]) + 10, ui[2], 300]) if d else None
    film["metingen"]["b_dim_z"] = z
    if d:
        yield from muis_naar(d[0] + 150, d[1] + 120, 16)
    film["metingen"]["b_hoogte_voor"] = round(ob.dimensions.z, 1)
    yield from houd(50)
    log(f"KORT {'OK' if d else 'FOUT'} b_maat hoogte {ob.dimensions.z:.1f}")
    deel("b_schaal")
    v = regio_rect(a)
    yield from muis_naar(v[0] + int(v[2] * 0.35), v[1] + int(v[3] * 0.45), 12)
    toets("s")
    yield 0.3
    neem(4)
    for k in ("0", "period", "7"):
        toets(k)
        yield 0.25
        neem(6)
    toets("Return")
    yield 0.6
    bpy.context.view_layer.update()
    neem(10)
    film["metingen"]["b_hoogte_na"] = round(ob.dimensions.z, 1)
    if abs(ob.dimensions.z - 217.0) > 2:
        log(f"KORT vangnet b_schaal: hoogte {ob.dimensions.z:.1f}, schaal via script")
        ob.scale = (0.7, 0.7, 0.7)
        bpy.context.view_layer.update()
        film["metingen"]["b_hoogte_na"] = round(ob.dimensions.z, 1)
    yield from houd(30)
    log(f"KORT OK b_schaal hoogte {ob.dimensions.z:.1f}")
    deel("b_past")
    yield from stuk(70, lambda t: cam(240 - 50 * t, 72 - 6 * t, 820 - 160 * t, big.lerp(Vector((0, 0, 125)), t)))
    yield from houd(30)
    log("KORT OK b_past")
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
