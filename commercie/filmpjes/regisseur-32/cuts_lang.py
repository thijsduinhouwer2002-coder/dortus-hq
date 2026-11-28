"""Zoekvideo Click Cuts 'split a model for 3D printing in Blender' (issue #332, Regisseur 28 nov 2026).

Echte Blender 5.3 met de gewone interface (bovenbalk, outliner, properties) onder Xvfb 1920x1080, Click Cuts 1.1.0
(main), het paard van het hoofdbeeld (Horse Statue 01, Poly Haven, CC0). Zelfde klok als cuts8.py (regisseur-31):
beeld voor beeld precies 1/30 s, echte X-muis en kliks (XTest), scherm met mss. Mist een klik, dan doet het script de
stap zelf en schrijft dat in film.json onder "vangnet". Uit: scherm-ruw.ts, muis.txt, film.json.
    blender --gpu-backend opengl -p 0 0 1920 1080 start.blend --python cuts_lang.py -- <map> <click_cuts.zip> <modelmap>"""
import json
import math
import os
import subprocess
import sys
import time

import bmesh
import bpy
from mathutils import Matrix, Quaternion, Vector

sys.path.insert(0, os.environ.get("CJ_PYLIB", "/tmp/pylib"))
import mss  # noqa: E402
from Xlib import X, XK  # noqa: E402
from Xlib import display as xdisplay  # noqa: E402
from Xlib.ext import xtest  # noqa: E402

a = sys.argv[sys.argv.index("--") + 1:]
MAP, ZIP, MODEL = a[0], a[1], a[2]
os.makedirs(MAP, exist_ok=True)
HOOGTE = 520.0
UI = float(os.environ.get("CC_UI", "1.25"))
PANEEL = int(os.environ.get("CC_PANEEL", "440"))
FPS = 30
film = {"fps": FPS, "delen": {}, "kliks": [], "metingen": {}, "vangnet": [], "echt": True}
D = xdisplay.Display()
MUIS = {"x": 300, "y": 1100}
K = {"n": 0, "rec": False, "haken": [], "ff": None, "sct": None, "muis": None}


def log(t):
    print(f"[lang] {t}", flush=True)


# ---------------------------------------------------------------- echte X-invoer
def xzet(x, y):
    xtest.fake_input(D, X.MotionNotify, x=int(round(x)), y=int(round(y)))
    D.sync()
    MUIS["x"], MUIS["y"] = int(round(x)), int(round(y))


def xknop(k, neer):
    xtest.fake_input(D, X.ButtonPress if neer else X.ButtonRelease, k)
    D.sync()


def xtoets(naam):
    code = D.keysym_to_keycode(XK.string_to_keysym(naam))
    xtest.fake_input(D, X.KeyPress, code)
    D.sync()
    xtest.fake_input(D, X.KeyRelease, code)
    D.sync()


# ---------------------------------------------------------------- klok, tekenen, vangen
def tijd():
    return K["n"] / FPS


def deel(naam):
    film["delen"][naam] = round(tijd(), 3)
    log(f"deel {naam} {tijd():.2f}")


def gebied_3d():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                return venster, gebied
    return None, None


def herteken():
    for w in bpy.context.window_manager.windows:
        for ar in w.screen.areas:
            ar.tag_redraw()


def teken():
    herteken()
    venster = bpy.context.window_manager.windows[0]
    try:
        with bpy.context.temp_override(window=venster, screen=venster.screen):
            bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)
    except Exception as f:  # noqa: BLE001
        log(f"KORT redraw {f}")


def begin_opname():
    K["sct"] = mss.mss()
    mon = K["sct"].monitors[0]
    K["mon"] = mon
    K["ff"] = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{mon['width']}x{mon['height']}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "12", "-pix_fmt", "yuv420p",
         "-f", "mpegts", os.path.join(MAP, "scherm-ruw.ts")], stdin=subprocess.PIPE)
    K["muis"] = open(os.path.join(MAP, "muis.txt"), "w", buffering=1)
    K["rec"] = True
    K["n"] = 0
    log(f"KORT opname begint, scherm {mon['width']}x{mon['height']}")


def vang():
    raw = K["sct"].grab(K["mon"]).raw
    K["ff"].stdin.write(raw)
    p = D.screen().root.query_pointer()
    K["muis"].write(f"{tijd():.4f} {p.root_x} {p.root_y}\n")


def einde_opname():
    if K["ff"] is not None and not K["ff"].stdin.closed:
        K["ff"].stdin.close()
        K["ff"].wait()
        log(f"KORT opname klaar: {K['n']} beelden")


# ---------------------------------------------------------------- bewegingen (per beeld)
def zacht5(t):
    return t * t * t * (t * (6 * t - 15) + 10)


def glij(x, y, duur=None, boog=1.0):
    """Muis glijdt zoals een hand: versnellen, afremmen, kleine boog. Haak per beeld; geeft de duur terug."""
    x0, y0 = MUIS["x"], MUIS["y"]
    d = math.hypot(x - x0, y - y0)
    if duur is None:
        duur = max(0.22, min(0.6, 0.18 + d / 2600.0))   # snel, zoals iemand die het programma kent
    nx, ny = ((-(y - y0) / d, (x - x0) / d) if d > 0 else (0.0, 0.0))
    b = min(30.0, d * 0.06) * boog * (1 if int(x0 + y) % 2 else -1)
    n0, N = K["n"], max(1, int(round(duur * FPS)))

    def haak():
        t = min(1.0, (K["n"] - n0 + 1) / N)
        e = zacht5(t)
        s = math.sin(math.pi * e) * b
        xzet(x0 + (x - x0) * e + nx * s, y0 + (y - y0) * e + ny * s)
        return t < 1.0
    K["haken"].append(haak)
    return duur


def anim(duur, f):
    """Eigen haak: f(e) per beeld, e loopt zacht van 0 naar 1."""
    n0, N = K["n"], max(1, int(round(duur * FPS)))

    def haak():
        t = min(1.0, (K["n"] - n0 + 1) / N)
        f(zacht5(t))
        return t < 1.0
    K["haken"].append(haak)
    return duur


def naar(x, y, duur=None, boog=1.0):
    yield glij(x, y, duur, boog)


def klik(k=1):
    xknop(k, True)
    xknop(k, False)
    film["kliks"].append(round(tijd(), 3))


def wiel(omhoog, keer):
    for _ in range(keer):
        klik(4 if omhoog else 5)
        film["kliks"].pop()
        yield 1.0 / FPS * 2


def sleep_middel(dx, dy, duur):
    """Weergave draaien zoals een gebruiker: middelste muisknop vast, muis opzij, los."""
    xknop(2, True)
    yield 1.0 / FPS
    yield glij(MUIS["x"] + dx, MUIS["y"] + dy, duur, boog=0.25)
    xknop(2, False)
    yield 1.0 / FPS


# ---------------------------------------------------------------- scherm en scène
def rect(soort="UI"):
    venster, gebied = gebied_3d()
    r = next(r for r in gebied.regions if r.type == soort)
    return [venster.x + r.x, venster.y + venster.height - (r.y + r.height), r.width, r.height]


def scherm_punt(p):
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, gebied = gebied_3d()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    q = location_3d_to_region_2d(regio, gebied.spaces.active.region_3d, Vector(p))
    if q is None:
        return None
    return int(venster.x + regio.x + q.x), int(venster.y + venster.height - (regio.y + q.y))


def ocr(tekst, vak=None, niet=None, laatste=False):
    """Plek (x, y) op het X-scherm van `tekst` volgens tesseract (zoals regisseur-27), of None."""
    import numpy as np
    s = K["sct"] or mss.mss()
    g = s.grab(s.monitors[0])
    vak = vak or rect("UI")
    x0, y0, b, h = vak
    arr = np.frombuffer(g.raw, np.uint8).reshape(g.height, g.width, 4)[y0:y0 + h, x0:x0 + b, :3].mean(axis=2)
    pgm = np.where(arr > 165, 0, 255).astype(np.uint8)
    with open("/tmp/claude-0/w/ocr_v.pgm", "wb") as f_:
        f_.write(f"P5 {pgm.shape[1]} {pgm.shape[0]} 255\n".encode() + pgm.tobytes())
    r = subprocess.run(["tesseract", "/tmp/claude-0/w/ocr_v.pgm", "stdout", "--psm", "11", "tsv"], capture_output=True,
                       text=True)
    regels = {}
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            woord = d[11].strip().lower().strip(".,:;(){}[]'\"")
            woord = {"al": "a1", "ai": "a1", "a]": "a1"}.get(woord, woord)
            regels.setdefault((d[2], d[3], d[4]), []).append((woord, int(d[6]), int(d[7]), int(d[8]), int(d[9])))
    doel = tekst.lower().split()
    if laatste:
        regels = dict(sorted(regels.items(), key=lambda kv: -min(w[2] for w in kv[1])))
    for ws in regels.values():
        ws.sort(key=lambda w: w[1])
        for i in range(len(ws) - len(doel) + 1):
            if all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                if niet and i + len(doel) < len(ws) and ws[i + len(doel)][0] == niet:
                    continue
                s_ = ws[i:i + len(doel)]
                xa, xb = min(w[1] for w in s_), max(w[1] + w[3] for w in s_)
                ya, yb = min(w[2] for w in s_), max(w[2] + w[4] for w in s_)
                return x0 + (xa + xb) // 2, y0 + (ya + yb) // 2
    log(f"KORT ocr niet gevonden: {tekst!r} ({' '.join(w[0] for ws in regels.values() for w in ws)[:300]})")
    return None


def srgb(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) for x in c) + (1.0,)


def laad_paard():
    s = bpy.context.scene
    for o in list(s.objects):
        bpy.data.objects.remove(o)
    s.unit_settings.system, s.unit_settings.scale_length, s.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
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
    ob.color = srgb("E9DFCF")
    film["metingen"]["paard_mm"] = [round(v, 1) for v in (mx - mn)]
    # kader van het bed (256 mm, Bambu Lab A1): een draadkubus in de scène van de gebruiker, geen add-on-functie
    bpy.ops.mesh.primitive_cube_add(size=256.0, location=(0, 0, 128.0))
    bed = bpy.context.active_object
    bed.name = "A1 bed 256 mm"
    bed.display_type = "WIRE"
    bed.show_in_front = True
    bed.color = srgb("FFC94A")
    bed.hide_select = True
    for o in s.objects:
        o.select_set(False)
    s.view_layers[0].objects.active = None
    log(f"KORT paard {film['metingen']['paard_mm']} mm, {len(ob.data.polygons)} vlakken")
    return ob, bed


def zet_weergave(rot, midden, afstand):
    _, gebied = gebied_3d()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "PERSP"
    rv.view_rotation = rot
    rv.view_location = midden
    rv.view_distance = afstand


def tabblad():
    venster, gebied = gebied_3d()
    ui = next(r for r in gebied.regions if r.type == "UI")
    if ui.active_panel_category == "Click Cuts":
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xzet(x, y)
    code = D.keysym_to_keycode(XK.string_to_keysym("Control_L"))
    xtest.fake_input(D, X.KeyPress, code)
    D.sync()
    klik(5)
    film["kliks"].pop()
    xtest.fake_input(D, X.KeyRelease, code)
    D.sync()
    return False


def sleep_zijbalk(breed):
    for dx in (2, 5, 9, 14):
        z = rect("UI")
        if abs(z[2] - breed) < 25:
            break
        x, y = z[0] + dx, z[1] + 500
        xzet(x, y)
        yield 0.2
        xknop(1, True)
        yield 0.2
        doel = z[0] + z[2] - breed
        for i in range(1, 13):
            xzet(int(x + (doel - x) * i / 12), y)
            yield 0.05
        yield 0.2
        xknop(1, False)
        yield 0.3
        log(f"KORT zijbalk dx={dx}: {rect('UI')}")




def kijk():
    """Gewone Blender-indeling (bovenbalk, outliner, properties, tijdlijn): zoals iemands eigen pc."""
    venster, gebied = gebied_3d()
    sp = gebied.spaces.active
    sp.shading.type, sp.shading.light, sp.shading.color_type = "SOLID", "STUDIO", "OBJECT"
    sp.shading.show_cavity = True
    sp.shading.cavity_type = "WORLD"
    sp.shading.show_shadows = False
    sp.shading.wireframe_color_type = "OBJECT"
    sp.clip_start, sp.clip_end = 0.5, 100000
    ov = sp.overlay
    ov.show_floor, ov.show_axis_x, ov.show_axis_y, ov.show_cursor = True, True, True, False
    ov.show_stats = False
    sp.show_region_header = True
    sp.show_region_tool_header = True
    sp.show_region_toolbar = True
    sp.show_region_ui = True
    pr = bpy.context.preferences
    pr.view.ui_scale = UI
    pr.system.use_region_overlap = False
    pr.view.show_tooltips = False
    pr.view.smooth_view = 0
    pr.inputs.use_zoom_to_mouse = True


def stukken():
    return [o for o in bpy.context.scene.objects if o.get("sj_stuk") and o.visible_get()]


def kader(objs, duur=0.6, factor=1.0, rot=None):
    """Weergave schuift naar deze objecten, zoals een gebruiker met numpad . (View Selected) of het wiel."""
    _, gebied = gebied_3d()
    rv = gebied.spaces.active.region_3d
    pts = [o.matrix_world @ Vector(c) for o in objs for c in o.bound_box]
    if not pts:
        return 0.05
    mn = Vector([min(p[i] for p in pts) for i in range(3)])
    mx = Vector([max(p[i] for p in pts) for i in range(3)])
    mid = (mn + mx) / 2
    doel_d = max((mx - mn).length * 1.25 * factor, 40.0)
    van_loc, van_d, van_rot = rv.view_location.copy(), rv.view_distance, rv.view_rotation.copy()

    def f(e):
        rv.view_location = van_loc.lerp(mid, e)
        rv.view_distance = van_d + (doel_d - van_d) * e
        if rot is not None:
            rv.view_rotation = van_rot.slerp(rot, e)
    return anim(duur, f)


def kies(ob, dx=0, dy=0):
    """Echte klik op het object; vangnet als de klik mist."""
    mw = ob.matrix_world
    import numpy as np
    co = np.array([tuple(mw @ v.co) for v in list(ob.data.vertices)[::max(1, len(ob.data.vertices) // 400)]])
    mid = co.mean(axis=0)
    beste = min(co, key=lambda p: (Vector(p) - Vector(mid)).length)
    q = scherm_punt(tuple(beste))
    if q:
        yield from naar(q[0] + dx, q[1] + dy)
        yield 0.1
        klik()
        yield 0.15
    if not ob.select_get() or bpy.context.view_layer.objects.active is not ob:
        film["vangnet"].append(f"kies {ob.name}")
        for o in bpy.context.selected_objects:
            o.select_set(False)
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob


def knop(tekst, vak=None, niet=None, laatste=False, scrol=0):
    """Zoek de knop met OCR; scrol in het paneel als hij er (nog) niet staat. Geeft (x, y) of None."""
    teken()
    q = ocr(tekst, vak=vak, niet=niet, laatste=laatste)
    n = 0
    while q is None and n < abs(scrol):
        z = rect("UI")
        if abs(MUIS["x"] - (z[0] + z[2] // 2)) > 60 or not (z[1] < MUIS["y"] < z[1] + z[3]):
            yield from naar(z[0] + z[2] // 2, z[1] + int(z[3] * 0.5), 0.3)
        yield from wiel(scrol > 0, 2)
        yield 0.12
        teken()
        q = ocr(tekst, vak=vak, niet=niet, laatste=laatste)
        n += 2
    return q


def druk(tekst, **kw):
    q = yield from knop(tekst, **kw)
    if q:
        yield from naar(*q)
        yield 0.1
        klik()
        deel(f"knop {tekst}")
    return q


def tab_click_cuts():
    """Plek van het verticale tabblad "Click Cuts" in de zijbalk: strook draaien en lezen met tesseract."""
    import numpy as np
    venster, gebied = gebied_3d()
    ui = next(r for r in gebied.regions if r.type == "UI")
    s = K["sct"] or mss.mss()
    g = s.grab(s.monitors[0])
    x0 = venster.x + ui.x + ui.width - 34
    y0 = venster.y + venster.height - (ui.y + ui.height)
    arr = np.frombuffer(g.raw, np.uint8).reshape(g.height, g.width, 4)[y0:y0 + ui.height, x0:x0 + 34, :3].mean(axis=2)
    rot = np.rot90(arr, k=1)
    rot = np.repeat(np.repeat(rot, 2, axis=0), 2, axis=1)
    pgm = np.where(rot > 125, 0, 255).astype(np.uint8)
    with open("/tmp/claude-0/w/ocr_tab.pgm", "wb") as f_:
        f_.write(f"P5 {pgm.shape[1]} {pgm.shape[0]} 255\n".encode() + pgm.tobytes())
    r = subprocess.run(["tesseract", "/tmp/claude-0/w/ocr_tab.pgm", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
    ws = []
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            ws.append((d[11].strip().lower(), int(d[6]) // 2, int(d[7]) // 2, int(d[8]) // 2, int(d[9]) // 2))
    for i, w_ in enumerate(ws):
        if w_[0].startswith("click"):
            xr = w_[1] + w_[3] // 2 + 20   # midden van "Click Cuts" ligt iets voorbij "Click"
            yr = w_[2] + w_[4] // 2
            return x0 + 33 - yr, y0 + xr
    log(f"KORT tab niet gevonden: {[w_[0] for w_ in ws]}")
    return None


def opzet():
    """Niet opgenomen: add-on erin, paard laden, weergave klaarzetten, zijbalk op het tabblad Click Cuts."""
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 0.5
    paard, bed = laad_paard()
    kijk()
    yield 0.8
    for _ in range(14):
        if tabblad():
            break
        yield 0.4
    yield 0.4
    yield from sleep_zijbalk(PANEEL)
    inst = bpy.context.scene.split_joints
    inst.printer = "A1MINI"   # begin op de kleine A1 mini: de gebruiker kiest echt
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(MAP, "horse_statue.blend"))
    yield 0.5
    _, gebied = gebied_3d()
    gebied.spaces.active.show_region_ui = False   # de gebruiker drukt straks zelf op N
    yield 0.4
    film["metingen"]["weergave"] = rect("WINDOW")
    return paard, bed


def verloop():
    paard, bed = yield from opzet()
    w = rect("WINDOW")
    midden_x = w[0] + w[2] // 2
    rot0 = Quaternion((0, 0, 1), math.radians(28)) @ Quaternion((1, 0, 0), math.radians(74))
    zet_weergave(rot0, Vector((0, 0, 240.0)), float(os.environ.get("CC_AFSTAND", "880")))
    xzet(midden_x + 160, w[1] + int(w[3] * 0.6))
    yield 0.6
    teken()
    begin_opname()
    deel("start")
    # HOOFDSTUK 1: de vraag. Het paard steekt ver boven het gouden kader (bed) uit; de gebruiker draait er meteen omheen.
    yield from sleep_middel(-260, 0, 2.2)
    yield 0.3
    yield from sleep_middel(-200, 20, 2.0)
    yield 0.3
    yield from sleep_middel(-180, -10, 2.0)
    deel("antwoord")
    yield 0.6
    yield from sleep_middel(-160, 0, 1.8)
    yield 0.4
    # HOOFDSTUK 2: N, printer, model, Split to fit
    deel("h2")
    yield from naar(midden_x + 80, w[1] + int(w[3] * 0.45), 0.4)
    yield 0.2
    xtoets("n")
    deel("toets N")
    yield 0.7
    venster, gebied = gebied_3d()
    ui = next(r for r in gebied.regions if r.type == "UI")
    if ui.active_panel_category != "Click Cuts":
        q = tab_click_cuts()
        if q:
            yield from naar(*q, 0.5)
            yield 0.12
            klik()
            deel("tab Click Cuts")
            yield 0.5
        for _ in range(8):
            ui = next(r for r in gebied.regions if r.type == "UI")
            if ui.active_panel_category == "Click Cuts":
                break
            film["vangnet"].append("tab")
            tabblad()
            yield 0.2
    yield 0.4
    inst = bpy.context.scene.split_joints
    q = yield from druk("Bambu Lab A1 mini")
    if q:
        yield 0.4
        z = rect("UI")
        doel = ocr("Bambu Lab A1", vak=[max(0, z[0] - 420), 0, z[2] + 420, K["mon"]["height"]], niet="mini")
        if doel is None:
            doel = (q[0], q[1] + int(21 * UI))
        yield from naar(doel[0], doel[1], duur=0.4, boog=0.2)
        yield 0.2
        klik()
        yield 0.3
    if inst.printer != "A1":
        film["vangnet"].append(f"printer {inst.printer}")
        xtoets("Escape")
        inst.printer = "A1"
    yield 0.6
    yield from kies(paard, 10, 10)
    deel("paard gekozen")
    yield 0.8
    z = rect("UI")
    yield from naar(z[0] + z[2] // 2 - 40, z[1] + int(z[3] * 0.18), 0.4)   # de muis wijst naar "Horse: ... faces"
    yield 1.0
    q = yield from druk("Split to fit")
    t0 = time.time()
    yield 1.0 / FPS
    if not stukken():
        film["vangnet"].append("split")
        bpy.context.view_layer.objects.active = paard
        paard.select_set(True)
        bpy.ops.split_joints.split_to_fit()
    film["metingen"]["split_echte_s"] = round(time.time() - t0, 1)
    bed.hide_set(True)
    st = stukken()
    film["metingen"]["stukken"] = len(st)
    film["metingen"]["pennen"] = sum(int(o["sj_pennen"]) for o in bpy.context.scene.objects if o.get("sj_pennen"))
    film["metingen"]["groen"] = sum(1 for o in st if o.get("sj_status") == "groen")
    film["metingen"]["uitslag"] = inst.uitslag
    deel("gesplitst")
    yield 0.4
    if q:
        yield from naar(q[0] - 30, q[1] + int(52 * UI), 0.4)   # langs de uitslag
    yield 1.4
    yield from naar(midden_x, w[1] + int(w[3] * 0.55), 0.4)
    yield kader(st, 0.6)
    yield from sleep_middel(220, 0, 2.2)
    yield 0.3
    yield from sleep_middel(180, -20, 2.0)
    deel("h2 eind")
    # HOOFDSTUK 3: Draw cut op het bovenste stuk (hoofd en hals)
    deel("h3")
    kop = max(st, key=lambda o: Vector(o.get("sj_midden_mm", (0, 0, 0))).z)
    film["metingen"]["draw_stuk"] = kop.name
    _, gebied = gebied_3d()
    rv = gebied.spaces.active.region_3d
    zij = Quaternion((0, 0, 1), math.radians(20)) @ Quaternion((1, 0, 0), math.radians(84))
    yield from naar(midden_x - 100, w[1] + int(w[3] * 0.6), 0.35)
    yield kader([kop], 0.9, factor=1.25, rot=zij)
    yield 0.3
    yield from kies(kop)
    yield 0.4
    q = yield from druk("Draw cut")
    yield 0.5
    import numpy as np
    venster, gebied = gebied_3d()
    hoofd = next(r for r in gebied.regions if r.type == "WINDOW")
    from bpy_extras import view3d_utils
    mw = np.array(kop.matrix_world)
    co = np.array([tuple(v.co) for v in kop.data.vertices]) @ mw[:3, :3].T + mw[:3, 3]
    sc = [view3d_utils.location_3d_to_region_2d(hoofd, rv, p) for p in co]
    sc = np.array([tuple(p) for p in sc if p is not None])
    # lijn schuin over de hals: op 45 % van de hoogte van het stuk, 30 px voorbij beide kanten
    y_lijn = sc[:, 1].min() + (sc[:, 1].max() - sc[:, 1].min()) * float(os.environ.get("CC_LIJN", "0.42"))
    xa, xb = sc[:, 0].min() - 30, sc[:, 0].max() + 30
    kant = 0.12 * (xb - xa)

    def scherm(x, y):
        return int(venster.x + hoofd.x + x), int(venster.y + venster.height - (hoofd.y + y))
    p1, p2 = scherm(xa, y_lijn - kant), scherm(xb, y_lijn + kant)
    film["metingen"]["lijn"] = [p1, p2]
    yield from naar(*p1, 0.45)
    yield 0.25
    xknop(1, True)
    yield 2.0 / FPS
    yield glij(*p2, duur=1.1, boog=0.05)
    yield 0.2
    xknop(1, False)
    deel("lijn getrokken")
    yield 0.3
    snede = [o for o in bpy.context.scene.objects if o.get("sj_vrij") == kop.name]
    film["metingen"]["snedevlak"] = len(snede)
    yield 1.6
    q = yield from druk("Flip side")
    yield 1.3
    q = yield from druk("Flip side")
    yield 0.9
    n_voor = len(stukken())
    q = yield from druk("Cut piece")
    yield 1.0 / FPS
    film["metingen"]["draw_voor_na"] = [n_voor, len(stukken())]
    deel("gesneden")
    yield 0.6
    yield from naar(midden_x + 40, w[1] + int(w[3] * 0.55), 0.35)
    yield from sleep_middel(240, -40, 2.0)
    yield 0.3
    yield from sleep_middel(-120, 40, 1.6)
    deel("h3 eind")
    # HOOFDSTUK 4: Fit test
    deel("h4")
    q = yield from druk("More settings", laatste=True)
    yield 0.4
    if not inst.meer:
        film["vangnet"].append("meer")
        inst.meer = True
    q = yield from knop("Make fit test", scrol=-24)
    if q:
        yield from naar(q[0] - 60, q[1] - int(60 * UI), 0.4)   # langs "Fit test: print this first"
        yield 0.6
        yield from naar(*q, 0.35)
        yield 0.12
        klik()
        deel("knop Make fit test")
    yield 1.0 / FPS
    proef = [o for o in bpy.context.scene.objects if o.get("sj_passing")]
    if not proef:
        film["vangnet"].append("fit test")
        bpy.ops.split_joints.passing_maak()
        proef = [o for o in bpy.context.scene.objects if o.get("sj_passing")]
    film["metingen"]["proef"] = len(proef)
    yield 0.3
    yield from naar(midden_x, w[1] + int(w[3] * 0.55), 0.35)
    boven = Quaternion((0, 0, 1), math.radians(8)) @ Quaternion((1, 0, 0), math.radians(38))
    yield kader(proef, 1.1, factor=1.7, rot=boven)
    deel("proef dichtbij")
    yield 1.8
    yield from sleep_middel(120, 0, 1.6)
    q0 = yield from knop("Click the one that fits")
    if q0:
        z = rect("UI")
        q = ocr("0.20", vak=[z[0], q0[1] + 6, z[2], int(40 * UI)])
        if q:
            yield from naar(*q, 0.45)
            yield 0.15
            klik()
            deel("knop 0.20")
    yield 1.2
    film["metingen"]["speling"] = round(inst.speling_mm, 3)
    deel("h4 eind")
    # HOOFDSTUK 5: controleren en exporteren
    deel("h5")
    q = yield from druk("Exploded view", scrol=-24)
    yield 1.0 / FPS
    if not inst.uit_elkaar:
        film["vangnet"].append("exploded")
        inst.uit_elkaar = True
    yield 0.3
    z = rect("UI")
    yield from naar(z[0] + z[2] // 2, z[1] + int(z[3] * 0.62), 0.4)   # langs de lijst met groene stukken
    yield 1.4
    yield from naar(midden_x, w[1] + int(w[3] * 0.55), 0.4)
    rot5 = Quaternion((0, 0, 1), math.radians(35)) @ Quaternion((1, 0, 0), math.radians(70))
    yield kader(stukken(), 0.8, factor=0.95, rot=rot5)
    yield from sleep_middel(-220, 0, 2.2)
    q = yield from druk("Export parts", scrol=40)
    yield 1.0 / FPS
    bestanden = [f for f in os.listdir(os.path.join(MAP, "click_cuts"))] if os.path.isdir(os.path.join(MAP, "click_cuts")) else []
    film["metingen"]["export"] = sorted(bestanden)
    deel("geexporteerd")
    yield 1.5
    yield from naar(midden_x - 40, w[1] + int(w[3] * 0.5), 0.4)
    # HOOFDSTUK 6: eind, draaien om het paard in delen
    deel("h6")
    yield from sleep_middel(260, 0, 2.6)
    yield 0.2
    yield from sleep_middel(220, 0, 2.4)
    yield 0.2
    yield from sleep_middel(200, 0, 2.4)
    deel("eind")
    einde_opname()
    with open(os.path.join(MAP, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {json.dumps(film['metingen'])} vangnet {film['vangnet']}")
    bpy.ops.wm.quit_blender()
    yield None


gang = verloop()
RUST = {"rest": 0}



def stap():
    """Eén tik. Tijdens de opname: elke tik precies 1/30 s filmtijd, met tekenen en vangen. Daarvoor: echte tijd."""
    try:
        if not K["rec"]:
            d = next(gang)
            if d is None:
                return None
            if K["rec"]:
                RUST["rest"] = max(1, int(round(float(d) * FPS)))
                return 0.0
            for h in list(K["haken"]):
                if not h():
                    K["haken"].remove(h)
            return float(d)
        if RUST["rest"] <= 0:
            d = next(gang)
            if d is None:
                return None
            RUST["rest"] = max(1, int(round(float(d) * FPS)))
        for h in list(K["haken"]):
            if not h():
                K["haken"].remove(h)
        if K["haken"]:
            K["anker"] = None
        else:   # rust: de hand ligt nooit helemaal stil, de muis drijft een paar pixels (geen stilstaand beeld)
            if K.get("anker") is None:
                K["anker"] = (MUIS["x"], MUIS["y"], K["n"])
            ax, ay, n0 = K["anker"]
            u = (K["n"] - n0) / FPS
            xtest.fake_input(D, X.MotionNotify, x=int(round(ax + 7 * math.sin(5.0 * u))),
                             y=int(round(ay + 5 * math.sin(3.7 * u + 0.6) - 5 * math.sin(0.6))))
            D.sync()
        teken()
        vang()
        K["n"] += 1
        RUST["rest"] -= 1
        return 0.0
    except StopIteration:
        einde_opname()
        return None
    except Exception as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        log(f"KORT FOUT {e!r}")
        einde_opname()
        with open(os.path.join(MAP, "film.json"), "w") as f:
            json.dump(film, f, indent=1)
        bpy.ops.wm.quit_blender()
        return None


bpy.app.timers.register(stap, first_interval=2.0)
