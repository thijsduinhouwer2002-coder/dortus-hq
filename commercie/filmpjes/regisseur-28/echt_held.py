"""Echte schermopname voor sale-Short v2 in procesvorm (issue #159, Regisseur, 26 nov 2026).

Thijs 26 nov 09:00: "letterlijk zo'n filmpje exact namaken, maar dan met onze robot". Opbouw van het voorbeeld
(issue #159): seconde 0 al in Blender met een grijs model en beweging, dan elke ±0,7 tot 1 s een echte stap, dan
kleur met de node-editor eronder, dan de tijdlijn, dan de klik op Render > Render Animation, en als slot een mooi
eindbeeld dat ±6 s blijft staan.
Het scherm is staand (1080x1920) en is de hele Blender: menubalk bovenaan, 3D-weergave met het paneel van
Click Joints Pro 1.2.8 (wat kopers in de sale krijgen), de Shader Editor eronder en de tijdlijn onderaan. Niets
nagebouwd of erbij getekend; ffmpeg x11grab neemt het scherm op (neem_op.sh), glij.py beweegt de echte X-muis.
Knoppen vindt het script met tesseract; mist een echte klik, dan doet het script de stap en schrijft "KORT vangnet".
Na het scherm-deel rendert hetzelfde Blender het eindbeeld door de camera (Material Preview, zoals de heldenbeelden
van de studio) naar <map>/eind/; dat stuk van de opname valt buiten de montage.
    blender --gpu-backend opengl start.blend --python echt_held.py -- <map> <betaalde zip>"""
import importlib
import json
import math
import os
import subprocess
import sys
import time

import bpy
from mathutils import Quaternion, Vector

a = sys.argv[sys.argv.index("--") + 1:]
MAP, ZIP = a[0], a[1]
HIER = os.path.dirname(os.path.abspath(__file__))
GLIJ = os.path.join(HIER, "..", "regisseur-26", "glij.py")
STUDIO = os.path.abspath(os.path.join(HIER, "..", "studio"))
sys.path.insert(0, STUDIO)
import figuur_laden as FL  # noqa: E402
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402

UI = float(os.environ.get("CJ_UI", "1.5"))
BREED_ZIJBALK = int(os.environ.get("CJ_ZIJBALK", "470"))
EIND_BEELDEN = int(os.environ.get("CJ_EIND", "150"))
H = 220.0
film = {"delen": {}, "kliks": [], "metingen": {}, "echt": True}
MUIS = {"x": 300, "y": 700}
GRIJS = (0.62, 0.62, 0.64)

# tweede pose voor tijdlijn en eindbeeld: binnen het bereik dat de add-on meldt (kogels ±30, nek ±20)
POSE2 = {
    "Left hip": [((1, 0, 0), -22.0)], "Right hip": [((1, 0, 0), 10.0)],
    "Left knee": 55.0, "Right knee": 8.0,
    "Left shoulder": [((1, 0, 0), 18.0), ((0, 1, 0), 10.0)], "Left elbow": 70.0,
    "Right shoulder": [((1, 0, 0), -28.0), ((0, 1, 0), -10.0)], "Right elbow": 120.0,
    "Neck": [((0, 0, 1), 16.0), ((1, 0, 0), -4.0)],
}


def log(t):
    print(f"[held] {t}", flush=True)


def xdo(*args):
    subprocess.run(["xdotool", *args], capture_output=True, text=True)


def deel(naam):
    film["delen"][naam] = round(time.time(), 3)
    log(f"deel {naam} {time.time():.3f}")


def zacht(t):
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- scherm
def gebied(soort="VIEW_3D"):
    for venster in bpy.context.window_manager.windows:
        for g in venster.screen.areas:
            if g.type == soort:
                return venster, g
    return None, None


def rect(soort="UI", gebied_soort="VIEW_3D"):
    venster, g = gebied(gebied_soort)
    r = next(r for r in g.regions if r.type == soort)
    return [venster.x + r.x, venster.y + venster.height - (r.y + r.height), r.width, r.height]


def scherm_punt(p):
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, g = gebied()
    regio = next(r for r in g.regions if r.type == "WINDOW")
    q = location_3d_to_region_2d(regio, g.spaces.active.region_3d, Vector(p))
    if q is None:
        return None
    return int(venster.x + regio.x + q.x), int(venster.y + venster.height - (regio.y + q.y))


def herteken():
    for w in bpy.context.window_manager.windows:
        for ar in w.screen.areas:
            ar.tag_redraw()


def ocr(tekst, vak=None, drempel="65%"):
    pad = "/tmp/cj_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    vak = vak or rect("UI")
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-resize", "200%",
                    "-threshold", drempel, "-negate", "/tmp/cj_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/cj_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True,
                       text=True)
    regels = {}
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            woord = d[11].strip().lower().strip(".,:;(){}[]'\"")
            regels.setdefault((d[2], d[3], d[4]), []).append(
                (woord, int(d[6]) // 2, int(d[7]) // 2, int(d[8]) // 2, int(d[9]) // 2))
    doel = tekst.lower().split()
    for ws in regels.values():
        ws.sort(key=lambda w: w[1])
        for i in range(len(ws) - len(doel) + 1):
            if all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                s = ws[i:i + len(doel)]
                xa, xb = min(w[1] for w in s), max(w[1] + w[3] for w in s)
                ya, yb = min(w[2] for w in s), max(w[2] + w[4] for w in s)
                return x0 + (xa + xb) // 2, y0 + (ya + yb) // 2
    alles = " ".join(w[0] for ws in regels.values() for w in ws)
    log(f"KORT ocr niet gevonden: {tekst!r} ({alles[:300]})")
    return None


def zoek(tekst, keer=4, vak=None):
    for _ in range(keer):
        r = ocr(tekst, vak)
        if r:
            return r
        yield 0.5
    return None


# ---------------------------------------------------------------- muis
def muis_naar(x, y, duur=None, boog=1.0):
    if duur is None:
        duur = max(0.3, min(0.9, 0.25 + math.hypot(x - MUIS["x"], y - MUIS["y"]) / 1800.0))
    p = subprocess.Popen(["python3", GLIJ, str(MUIS["x"]), str(MUIS["y"]), str(int(x)), str(int(y)),
                          f"{duur:.3f}", str(boog)])
    while p.poll() is None:
        yield 0.01
    MUIS["x"], MUIS["y"] = int(x), int(y)
    yield 0.08


def klik(knop="1"):
    xdo("click", knop)
    film["kliks"].append(round(time.time(), 3))


def wacht(s):
    t0 = time.time()
    while time.time() - t0 < s:
        yield 0.02


def zweef(s, r=45):
    t0 = time.time()
    x0, y0 = MUIS["x"], MUIS["y"]
    k = 0
    while True:
        rest = s - (time.time() - t0) - 0.1
        if rest < 0.3:
            break
        hoek = 2.1 * k + 0.6
        yield from muis_naar(x0 + r * math.cos(hoek), y0 + 0.6 * r * math.sin(hoek), duur=min(0.8, rest), boog=0.8)
        k += 1
    yield from wacht(max(0.0, s - (time.time() - t0)))


def sleep_knop(knop, dx, dy, duur, doe=None):
    """Echt slepen met een muisknop (2 = draaien in de weergave, 1 = tijdlijn), met een rustige hand."""
    xdo("mousedown", knop)
    film["kliks"].append(round(time.time(), 3))
    yield 0.08
    x0, y0 = MUIS["x"], MUIS["y"]
    p = subprocess.Popen(["python3", GLIJ, str(x0), str(y0), str(int(x0 + dx)), str(int(y0 + dy)), f"{duur:.3f}", "0.3"])
    t0 = time.time()
    while p.poll() is None:
        if doe:
            doe(min(1.0, (time.time() - t0) / duur))
        yield 0.01
    if doe:
        doe(1.0)
    MUIS["x"], MUIS["y"] = int(x0 + dx), int(y0 + dy)
    yield 0.1
    xdo("mouseup", knop)
    yield 0.15


# ---------------------------------------------------------------- figuur en houding
def paar(naam, soort="SCHARNIER"):
    pa = pb = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == soort:
            if o.get("cj_deel") == "A":
                pa = o
            elif o.get("cj_deel") == "B":
                pb = o
    return pa, pb


def buig(b, graden):
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(graden, 1)


def scharnier(n, g):
    _a, b = paar(n)
    if b is not None:
        buig(b, g)
        bpy.context.view_layer.update()


def meng_pose(pa, pb, t):
    uit = {}
    for n in set(pa) | set(pb):
        va, vb = pa.get(n), pb.get(n)
        if isinstance(va, list) or isinstance(vb, list):
            uit[n] = [(x, g * (1 - t)) for x, g in (va or [])] + [(x, g * t) for x, g in (vb or [])]
        else:
            uit[n] = (va or 0.0) * (1 - t) + (vb or 0.0) * t
    return uit


DELEN = []
ANIM = {"aan": False, "van": 1, "tot": 60}


def pose_op_beeld(sc, *_):
    if not ANIM["aan"] or not DELEN:
        return
    t = (sc.frame_current - ANIM["van"]) / max(1, ANIM["tot"] - ANIM["van"])
    t = zacht(max(0.0, min(1.0, t)))
    try:
        R.poseer(DELEN, meng_pose(R.HELD, POSE2, t), scharnier=scharnier)
        if ANIM.get("cam"):
            ANIM["cam"](t)
    except Exception as e:  # noqa: BLE001
        log(f"KORT pose fout {e!r}")


# ---------------------------------------------------------------- scherm opzetten
def opzet_scherm():
    pr = bpy.context.preferences
    pr.view.ui_scale = UI
    pr.system.use_region_overlap = False
    pr.view.show_tooltips = False
    pr.inputs.use_zoom_to_mouse = True
    venster = bpy.context.window_manager.windows[0]
    # outliner en eigenschappen dicht: in staand beeld gaat de breedte naar de weergave en het paneel
    for soort in ("OUTLINER", "PROPERTIES"):
        for _ in range(2):
            v, g = gebied(soort)
            if g is None:
                break
            try:
                with bpy.context.temp_override(window=v, area=g):
                    bpy.ops.screen.area_close()
            except Exception as e:  # noqa: BLE001
                log(f"KORT area_close {soort}: {e!r}")
    # weergave splitsen: onderaan de Shader Editor (zoals in het voorbeeld de node-editor onder de weergave)
    v, g = gebied()
    with bpy.context.temp_override(window=v, area=g):
        bpy.ops.screen.area_split(direction="HORIZONTAL", factor=0.3)
    gs = sorted([x for x in venster.screen.areas if x.type == "VIEW_3D"], key=lambda x: x.y)
    onder = gs[0]
    onder.type = "NODE_EDITOR"
    onder.ui_type = "ShaderNodeTree"
    v, g = gebied()
    sp = g.spaces.active
    sp.shading.type, sp.shading.light, sp.shading.color_type = "SOLID", "STUDIO", "SINGLE"
    sp.shading.single_color = GRIJS
    sp.shading.show_cavity = True
    sp.shading.cavity_type = "WORLD"
    sp.clip_start, sp.clip_end = 0.5, 100000
    ov = sp.overlay
    ov.show_floor, ov.show_axis_x, ov.show_axis_y, ov.show_cursor = True, True, True, False
    ov.show_stats = False
    sp.show_region_header = True
    sp.show_region_tool_header = False
    sp.show_region_toolbar = True
    sp.show_region_ui = True
    sc = bpy.context.scene
    sc.frame_start, sc.frame_end, sc.frame_current = 1, 60, 1
    film["metingen"]["gebieden"] = {x.type: [x.x, x.y, x.width, x.height] for x in venster.screen.areas}


def tabblad():
    venster, g = gebied()
    ui = next(r for r in g.regions if r.type == "UI")
    if ui.active_panel_category == "Click Joints":
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", "5")
    xdo("keyup", "ctrl")
    return False


def sleep_zijbalk(breed):
    for dx in (2, 6, 12):
        z = rect("UI")
        if abs(z[2] - breed) < 25:
            break
        x, y = z[0] + dx, z[1] + 200
        xdo("mousemove", str(x), str(y))
        yield 0.3
        xdo("mousedown", "1")
        yield 0.2
        doel = z[0] + z[2] - breed
        for i in range(1, 11):
            xdo("mousemove", str(int(x + (doel - x) * i / 10)), str(y))
            yield 0.05
        yield 0.2
        xdo("mouseup", "1")
        yield 0.4
    log(f"KORT zijbalk {rect('UI')}")


def zet_weergave(draai, kantel, afstand, punt):
    _, g = gebied()
    rv = g.spaces.active.region_3d
    rv.view_perspective = "PERSP"
    rv.view_rotation = Quaternion((0, 0, 1), math.radians(draai)) @ Quaternion((1, 0, 0), math.radians(kantel))
    rv.view_location = Vector(punt)
    rv.view_distance = afstand


# ---------------------------------------------------------------- verloop
def verloop():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    arm, ob, punten = FL.laad_figuur("robot", H)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    inst.exportmap = os.path.join(MAP, "export")
    os.makedirs(inst.exportmap, exist_ok=True)
    naam = ob.name
    for o in bpy.context.scene.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    opzet_scherm()
    herteken()
    yield 1.0
    for _ in range(14):
        if tabblad():
            break
        yield 0.5
    yield 0.5
    yield from sleep_zijbalk(BREED_ZIJBALK)
    midden = (0.0, 0.0, 112.0)
    zet_weergave(-50, 80, 560, midden)
    w = rect("WINDOW")
    xdo("mousemove", str(w[0] + w[2] // 2), str(w[1] + w[3] // 2 + 120))
    MUIS["x"], MUIS["y"] = w[0] + w[2] // 2, w[1] + w[3] // 2 + 120
    yield 1.5
    film["metingen"]["zijbalk"] = rect("UI")
    film["metingen"]["weergave"] = w

    # 1. seconde 0: grijze robot met rig, de hand draait de weergave rond (echte middelste muisknop)
    deel("begin")
    yield from sleep_knop("2", 260, -30, 2.4)
    yield from sleep_knop("2", -120, 20, 1.2)

    # 2. klik de robot
    arm.hide_select = True
    p = scherm_punt((9.0, -8.0, 128.0)) or (w[0] + w[2] // 2, w[1] + w[3] // 2)
    yield from muis_naar(*p)
    klik()
    deel("kies")
    yield 0.3
    if bpy.context.view_layer.objects.active != ob:
        log("KORT vangnet kies")
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob
    yield from wacht(0.3)

    # 3. Figure from rig
    q = yield from zoek("Figure from rig")
    film["metingen"]["knop_ocr"] = q
    if q:
        yield from muis_naar(*q)
    yield from wacht(0.2)
    deel("knop")
    klik()
    yield 0.5
    t0 = time.time()
    while not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects) and time.time() - t0 < 90:
        yield 0.5
    if not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
        log("KORT vangnet knop: Figure from rig via script")
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob
        bpy.ops.click_joints.figuur_uit_rig()
    film["metingen"]["knop_s"] = round(time.time() - t0, 1)
    arm.hide_set(True)
    herteken()
    deel("knop_klaar")
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH"]
    DELEN[:] = delen
    try:
        fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
        lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
        film["metingen"]["gewrichten"] = len(lijst)
        film["metingen"]["regels"] = [fig.regel(r) for r in lijst]
    except Exception as e:  # noqa: BLE001
        log(f"KORT lijst {e!r}")
    log(f"KORT figuur {len(delen)} delen, {film['metingen'].get('gewrichten')} gewrichten, {film['metingen']['knop_s']} s")
    yield from zweef(1.0, r=35)

    # 4. Exploded view aan (echte klik), weergave draait mee, weer uit
    q = yield from zoek("Exploded view")
    if q:
        yield from muis_naar(*q)
        yield from wacht(0.15)
        klik()
        yield 0.4
    if not inst.uit_elkaar:
        log("KORT vangnet uitelkaar")
        inst.uit_elkaar = True
    deel("uitelkaar")
    w = rect("WINDOW")
    yield from muis_naar(w[0] + w[2] // 2 + 60, w[1] + w[3] // 2 + 200, duur=0.5)
    yield from sleep_knop("2", -200, 0, 1.6)
    film["metingen"]["uit_elkaar_delen"] = sum(
        1 for o in bpy.context.scene.objects if o.get("cj_deel") == "B" and o.delta_location.length > 1e-6)
    if q:
        yield from muis_naar(*q)
        yield from wacht(0.1)
        klik()
        yield 0.4
    inst.uit_elkaar = False
    herteken()

    # 5. knie: klik het onderbeen, Bend typen tot voorbij de stop (rood), terug
    ka, kb = paar("Left knee")
    if ka is not None and kb is not None:
        stop = float(ka.get("cj_bereik_graden", 120.0))
        film["metingen"]["knie_stop"] = stop
        zet_weergave(-70, 84, 330, (punten["l-knee"].x, punten["l-knee"].y, punten["l-knee"].z + 10))
        yield 0.3
        q = scherm_punt((punten["l-knee"] + punten["l-ankle"]) / 2)
        if q:
            yield from muis_naar(*q)
            klik()
            yield 0.3
        for o in bpy.context.selected_objects:
            o.select_set(False)
        kb.select_set(True)
        buig(kb, 0.0)
        herteken()
        deel("knie")
        q = yield from zoek("Bend")
        film["metingen"]["bend_ocr"] = q
        z = rect("UI")
        midden_s = (z[0] + z[2] // 2, q[1]) if q else None
        if midden_s:
            yield from muis_naar(*midden_s)
            for doel in (round(stop), round(stop + 15)):
                klik()
                yield 0.4
                xdo("key", "ctrl+a")
                yield 0.1
                xdo("type", "--delay", "70", f"{doel:g}")
                yield 0.2
                xdo("key", "Return")
                yield 0.3
                if abs(float(bpy.context.window_manager.cj_scharnier_pose) - doel) > 1.0:
                    log(f"KORT vangnet bend {doel}")
                    buig(kb, doel)
                deel("knie_stop" if doel == round(stop) else "knie_rood")
                yield from wacht(0.7)
        else:
            log("KORT vangnet bend (geen schuif gevonden)")
            for doel in (round(stop), round(stop + 15)):
                buig(kb, doel)
                deel("knie_stop" if doel == round(stop) else "knie_rood")
                yield from wacht(0.9)
        film["metingen"]["knie_rood_vlakken"] = len(ka.get("cj_rood_vlakken", [])) // 2
        buig(kb, 0.0)
        bpy.context.window_manager.cj_scharnier_pose = 0.0
    else:
        log("KORT FOUT geen linkerknie")

    # 6. kleur: studio, plastic, Material Preview (echte klik op de knop in de kop), node-editor eronder
    for o in bpy.context.scene.objects:
        if o.type == "MESH" and not o.get("cj_figuur") and o.visible_get():
            o.hide_set(True)
            o.hide_render = True
    S.bouw(H)
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    R.poseer(delen, R.HELD, scharnier=scharnier)
    for o in bpy.context.selected_objects:
        o.select_set(False)
    romp = max(delen, key=lambda o: len(o.data.vertices))
    zet_weergave(-35, 82, 600, midden)
    yield 0.4
    v, g = gebied()
    kop = next(r for r in g.regions if r.type == "HEADER")
    knop = (v.x + kop.x + kop.width - int(52 * UI), v.y + v.height - (kop.y + kop.height // 2))
    yield from muis_naar(*knop)
    klik()
    yield 0.4
    if g.spaces.active.shading.type != "MATERIAL":
        log("KORT vangnet material preview")
        g.spaces.active.shading.type = "MATERIAL"
    g.spaces.active.shading.use_scene_world = True
    g.spaces.active.shading.use_scene_lights = True
    deel("kleur")
    q = scherm_punt(romp.matrix_world @ Vector(romp.get("cj_midden", (0, 0, 0))) if romp.get("cj_midden") else
                    (0.0, -10.0, 120.0))
    if q:
        yield from muis_naar(*q)
        klik()
        yield 0.3
    if bpy.context.view_layer.objects.active is None or not bpy.context.view_layer.objects.active.get("cj_figuur"):
        romp.select_set(True)
        bpy.context.view_layer.objects.active = romp
    vn, gn = gebied("NODE_EDITOR")
    if gn:
        with bpy.context.temp_override(window=vn, area=gn, region=next(r for r in gn.regions if r.type == "WINDOW")):
            try:
                bpy.ops.node.view_all()
            except Exception as e:  # noqa: BLE001
                log(f"KORT view_all {e!r}")
        nr = rect("WINDOW", "NODE_EDITOR")
        deel("nodes")
        yield from muis_naar(nr[0] + nr[2] * 0.35, nr[1] + nr[3] * 0.45, duur=0.6)
        yield from muis_naar(nr[0] + nr[2] * 0.6, nr[1] + nr[3] * 0.4, duur=0.6)
        yield from muis_naar(nr[0] + nr[2] * 0.45, nr[1] + nr[3] * 0.6, duur=0.5)
    w = rect("WINDOW")
    yield from muis_naar(w[0] + w[2] // 2, w[1] + w[3] // 2, duur=0.5)
    yield from sleep_knop("2", 160, 10, 1.4)

    # 7. tijdlijn: de robot gaat van de ene pose naar de andere (echte sleep van de afspeelkop)
    bpy.app.handlers.frame_change_post.append(pose_op_beeld)
    ANIM["aan"] = True
    for o in bpy.context.selected_objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    vt, gt = gebied("DOPESHEET_EDITOR")
    if gt is None:
        vt, gt = gebied("TIMELINE")
    if gt is not None:
        tr = rect("WINDOW", gt.type)
        zet_weergave(-20, 84, 640, midden)
        with bpy.context.temp_override(window=vt, area=gt, region=next(r for r in gt.regions if r.type == "WINDOW")):
            try:
                bpy.ops.action.view_all()
            except Exception:  # noqa: BLE001
                try:
                    bpy.ops.time.view_all()
                except Exception as e:  # noqa: BLE001
                    log(f"KORT tijdlijn view_all {e!r}")
        yield 0.3
        x1, x2 = tr[0] + int(tr[2] * 0.06), tr[0] + int(tr[2] * 0.92)
        yield from muis_naar(x1, tr[1] + tr[3] // 2)
        deel("tijdlijn")
        yield from sleep_knop("1", x2 - x1, 0, 2.6)
        yield from sleep_knop("1", -(x2 - x1) // 2, 0, 1.0)
        yield from sleep_knop("1", (x2 - x1) // 2, 0, 0.8)
        film["metingen"]["frame_na_sleep"] = bpy.context.scene.frame_current
    if bpy.context.scene.frame_current < 50:
        log("KORT vangnet tijdlijn")
        bpy.context.scene.frame_set(60)

    # 8. Render > Render Animation (echte klikken in de menubalk); na een tel Escape
    cam = S.camera()
    bpy.context.scene.camera = cam
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1080, 1920, 100
    vt2, gtop = gebied("TOPBAR")
    deel("render_menu")
    q = None
    if gtop:
        tb = rect("HEADER", "TOPBAR")
        q = ocr("Render", vak=[tb[0], tb[1], min(tb[2], 900), tb[3]], drempel="55%")
    if q:
        yield from muis_naar(*q)
        yield from wacht(0.15)
        klik()
        yield 0.6
        r2 = ocr("Render Animation", vak=[0, 0, 1080, 700], drempel="55%")
        film["metingen"]["render_menu"] = [q, r2]
        if r2:
            sc.render.filepath = os.path.join(MAP, "proef", "")
            sc.frame_end = 1
            yield from muis_naar(*r2, duur=0.4)
            yield from wacht(0.15)
            deel("render_klik")
            klik()
            yield from wacht(1.6)
            xdo("key", "Escape")
            yield 0.5
        else:
            xdo("key", "Escape")
    else:
        log("KORT render-menu niet gevonden")
    deel("eind_scherm")
    yield from wacht(1.0)
    # sluit een render-venster als dat nog open is
    for wv in list(bpy.context.window_manager.windows)[1:]:
        try:
            with bpy.context.temp_override(window=wv):
                bpy.ops.wm.window_close()
        except Exception:  # noqa: BLE001
            pass

    # 9. eindbeeld door de camera (valt buiten de opname-montage): robot van HELD naar POSE2, camera draait langzaam
    try:
        sc.frame_start, sc.frame_end = 1, EIND_BEELDEN
        ANIM["van"], ANIM["tot"] = 1, EIND_BEELDEN
        sc.eevee.taa_render_samples = int(os.environ.get("CJ_SAMPLES", "32"))
        sc.eevee.taa_samples = int(os.environ.get("CJ_SAMPLES", "32"))

        def cam_op(t):
            S.richt(cam, delen, "staand", draai=-38 + 26 * t, kantel=7 - 2 * t, vul=0.74 + 0.06 * t, midden_y=0.55)
        ANIM["cam"] = cam_op
        sc.frame_set(1)
        os.makedirs(os.path.join(MAP, "eind"), exist_ok=True)
        sc.render.filepath = os.path.join(MAP, "eind", "e_")
        sc.render.image_settings.file_format = "PNG"
        v, g = gebied()
        ruimte = g.spaces.active
        ruimte.region_3d.view_perspective = "CAMERA"
        ruimte.shading.type = "MATERIAL"
        ruimte.overlay.show_overlays = False
        regio = next(r for r in g.regions if r.type == "WINDOW")
        deel("eind_render")
        t0 = time.time()
        with bpy.context.temp_override(window=v, area=g, region=regio):
            bpy.ops.render.opengl(animation=True, view_context=True)
        film["metingen"]["eind_s"] = round(time.time() - t0, 1)
        log(f"KORT eindbeeld {EIND_BEELDEN} beelden in {film['metingen']['eind_s']} s")
    except Exception as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        log(f"KORT FOUT eindbeeld {e!r}")
    with open(os.path.join(MAP, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {json.dumps(film['metingen'])[:1500]}")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None
    except Exception as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        log(f"KORT FOUT {e!r}")
        with open(os.path.join(MAP, "film.json"), "w") as f:
            json.dump(film, f, indent=1)
        bpy.ops.wm.quit_blender()
        return None


bpy.app.timers.register(stap, first_interval=3.0)
