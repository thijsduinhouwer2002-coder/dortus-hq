"""Opname tip-reeks 7 (Regisseur run 8, 23 nov 2026): "binnenstebuiten". Echte Blender 5.3.0 op een X-scherm van
2160x1920, UI-schaal 2, geen add-on. Hulpcode gelijk aan ../regisseur-8/tip_opname.py.

Tip G "binnen": een fles (eigen model, 90 mm hoog) waarvan een band vlakken naar binnen wijst. Overlays-menu (echte klik op
het pijltje naast de Overlays-knop) > Face Orientation aanvinken: de verkeerde vlakken worden rood. Tab, A, Shift N: alles
wijst naar buiten, geen rood meer. Gemeten: aantal vlakken met de normaal naar binnen, voor en na.

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
    print(f"[tip9] {t}", flush=True)


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


def ocr(tekst, vak, drempel="60%"):
    pad = "/tmp/tip9_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", drempel,
                    "-negate", "/tmp/tip9_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/tip9_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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



def fles():
    """Fles van 90 mm hoog, dicht, 32 rondom. Een band van de schouder (z 46 tot 74 mm) is binnenstebuiten gezet:
    die vlakken wijzen naar binnen, zoals na een slordige Extrude of Mirror."""
    prof = [(0, 0), (20, 0), (22, 2), (23, 8), (23, 30), (22.5, 42), (21, 50), (17, 58), (12, 64), (9, 70), (8.5, 78),
            (9.5, 82), (9.5, 88), (8, 90), (0, 90)]
    ob = draai_model("Bottle", prof, (0.10, 0.62, 0.66, 1), seg=32)
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    band = [f for f in bm.faces if 46 < f.calc_center_median().z < 74]
    bmesh.ops.reverse_faces(bm, faces=band)
    bm.normal_update()
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = False
    return ob


def binnen_tellen(ob):
    """Aantal vlakken waarvan de normaal naar de as van de fles wijst (dus naar binnen)."""
    if ob.mode == "EDIT":
        bm = bmesh.from_edit_mesh(ob.data)
        bm.normal_update()
        fs = [(f.normal.copy(), f.calc_center_median()) for f in bm.faces]
    else:
        fs = [(p.normal.copy(), p.center.copy()) for p in ob.data.polygons]
    n = 0
    for nor, c in fs:
        r = Vector((c.x, c.y, 0))
        if r.length < 0.5:      # bodem en dop: naar beneden of boven
            uit = Vector((0, 0, -1)) if c.z < 45 else Vector((0, 0, 1))
        else:
            uit = r.normalized()
        if nor.dot(uit) < -0.05:
            n += 1
    return n


def overlay_menu(kop):
    """Klik op het pijltje naast de Overlays-knop (rechts in de kop, plek uit CJ_OVL_DX vanaf de rechterrand), zoek
    "Face Orientation" in het menu en klik erop."""
    dx = int(os.environ.get("CJ_OVL_DX", "308"))
    px, py = kop[0] + kop[2] - dx, kop[1] + kop[3] // 2
    film["metingen"]["g_pijl"] = [px, py]
    yield from muis_naar(px, py, 18)
    neem(6)
    klik()
    q = None
    for i in range(10):
        yield 0.4
        xdo("mousemove", str(px + (i % 2) * 2), str(py))
        neem(2)
        q = ocr("Face Orientation", [max(0, px - 500), py + 600, 700, 500], "35%")
        if q:
            break
    film["metingen"]["g_face_or"] = q
    if not q:
        # reserve: plek gemeten in de proef van 23 nov (menu opent onder het pijltje, Face Orientation 190 links, 882 lager)
        q = (px - 190, py + 882)
        film["metingen"]["g_face_or_reserve"] = list(q)
        log("KORT ocr Face Orientation niet gevonden, reserveplek")
    yield from muis_naar(q[0], q[1], 16)
    neem(8)
    klik()
    yield 0.6
    neem(14)
    # menu dicht: muis naar links, dan Escape (proef 23 nov: een aangeklikt menu blijft open, ook als de muis weggaat)
    yield from muis_naar(380, 1350, 20)
    neem(4)
    toets("Escape")
    yield 0.6
    neem(6)
    w = bpy.context.window_manager.windows[0]
    film["metingen"]["g_menu_dicht"] = ocr("Viewport Overlays", [1100, 80, 1060, 300], "35%") is None
    return True


def verloop():
    zet_scherm()
    yield 1.0
    _, a = gebied("VIEW_3D")
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    sp = a.spaces.active
    ob = fles()
    selecteer(ob)
    mid = Vector((0, 0, 45))
    cam(35, 72, 260, mid)
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    film["metingen"]["kop"] = kop
    film["metingen"]["g_vlakken"] = len(ob.data.polygons)
    film["metingen"]["g_binnen_voor"] = binnen_tellen(ob)
    if os.environ.get("CJ_KIJK"):
        neem(1)
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        with open(os.path.join(uitmap, "film.json"), "w") as f:
            json.dump(film, f, indent=1)
        bpy.ops.wm.quit_blender()
        return

    deel("g_heel")      # de fles draait rustig rond, ziet er gewoon uit
    yield from stuk(90, lambda t: cam(20 + 70 * t, 70 + 8 * t, 250 - 50 * t, mid))
    yield from houd(14)
    log("KORT OK g_heel")

    deel("g_overlay")
    cam(60, 74, 230, mid)
    herteken()
    yield 0.3
    neem(6)
    via = yield from overlay_menu(kop)
    film["metingen"]["g_overlay_menu"] = bool(via and sp.overlay.show_face_orientation)
    if not sp.overlay.show_face_orientation:
        log("KORT vangnet g_overlay: Face Orientation via script")
        sp.overlay.show_face_orientation = True
        herteken()
        yield 0.5
    yield from houd(16)
    log("KORT OK g_overlay")

    deel("g_rood")      # dichterbij de rode band, langzaam rond
    yield from stuk(100, lambda t: cam(60 + 80 * t, 76 - 6 * t, 230 - 70 * t, mid + Vector((0, 0, 12 * t))))
    yield from houd(16)
    log("KORT OK g_rood")

    deel("g_edit")
    cam(140, 70, 190, mid + Vector((0, 0, 10)))
    yield 0.3
    neem(4)
    mx, my = zachte_muis_in_beeld()
    yield from muis_naar(mx, my, 10)
    neem(4)
    toets("Tab")
    yield 0.6
    neem(10)
    toets("a")
    yield 0.4
    neem(12)
    if ob.mode != "EDIT":
        log("KORT vangnet g_edit: Edit Mode via script")
        bpy.ops.object.mode_set(mode="EDIT")
        yield 0.4
    bm = bmesh.from_edit_mesh(ob.data)
    film["metingen"]["g_alles_toets"] = all(f.select for f in bm.faces)
    if not film["metingen"]["g_alles_toets"]:
        log("KORT vangnet g_edit: alles kiezen via script")
        bpy.ops.mesh.select_all(action="SELECT")
        yield 0.3
    yield from houd(14)
    log("KORT OK g_edit")

    deel("g_fix")
    toets("shift+n")
    yield 0.8
    neem(10)
    n = binnen_tellen(ob)
    film["metingen"]["g_binnen_na_toets"] = n
    if n:
        log(f"KORT vangnet g_fix: nog {n} naar binnen, Recalculate Outside via script")
        bpy.ops.mesh.normals_make_consistent(inside=False)
        yield 0.5
    yield from houd(20)
    log("KORT OK g_fix")

    deel("g_klaar")
    toets("Tab")
    yield 0.6
    if ob.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    film["metingen"]["g_binnen_na"] = binnen_tellen(ob)
    neem(6)
    yield from stuk(110, lambda t: cam(140 + 100 * t, 70 + 6 * t, 190 + 40 * t, mid + Vector((0, 0, 10 * (1 - t)))))
    yield from houd(30)
    sp.overlay.show_face_orientation = False      # voor de eindkaart en het slotbeeld: gewone kleur
    herteken()
    yield 0.4
    deel("g_slot")
    yield from stuk(90, lambda t: cam(240 + 60 * t, 74, 230 - 20 * t, mid))
    yield from houd(30)
    log(f"KORT OK g_klaar binnen {film['metingen']['g_binnen_voor']} naar {film['metingen']['g_binnen_na']}")
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
