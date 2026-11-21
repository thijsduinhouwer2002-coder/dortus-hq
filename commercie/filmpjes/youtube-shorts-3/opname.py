"""Opname voor YouTube Shorts reeks 3 (recept v2, opdracht hoofdchat 22 nov 2026 ±00:05 NL).

Echte Blender 5.3.0 op een breed X-scherm (2160x1920): links de 3D-weergave, rechts de zijbalk van Click Joints Pro
1.1.0, breed gesleept. kort.py snijdt er staande Shorts uit: weergave boven, paneel onder.
    CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>
Figuur: MakeHuman base.obj (CC0 1.0) met de rig uit e2e/proef_mens.py (linkerknie 120 en linkerelleboog 140 in
Limit Rotation, rechts niets), geverfd als speelgoedpop (pak, handschoenen, laarzen, riem, hoofd): alleen invoer.
De muis is de echte muis van het X-scherm (xdotool): hij beweegt en klikt op de knoppen die tesseract op het scherm
vindt. Een X-schermafbeelding toont de muis niet; daarom schrijft het script per beeld de plek van de muis in
film.json, en kort.py tekent daar een pijltje. Knoppen die een echte klik niet raakte, drukt het script daarna zelf
in (staat in het log als "KORT vangnet"). Bogen, getallen, rood, lijst en export komen van de add-on zelf.
Delen (eerste beeld per deel in film.json): heel, kies, knop, lijst, knie, knie_rood, pose, uitelkaar, export, held.
Regels "KORT OK <deel>" eist de workflow."""
import glob
import importlib
import json
import math
import os
import subprocess
import sys
import time

import bpy
from mathutils import Euler, Vector

E2E = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                                   "producten", "blender-gewrichten", "e2e"))
sys.path.insert(0, E2E)
_film = open(os.path.join(E2E, "film_pro.py"), encoding="utf-8").read()
_film = _film[:_film.index("def verloop():")].replace(
    "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))", "")
exec(compile(_film, "film_pro_hulp", "exec"), globals())   # noqa: S102 (eigen code uit de repo)
_mens = open(os.path.join(E2E, "scherm_mens.py"), encoding="utf-8").read()
_mens = _mens.replace("bpy.app.timers.register(stap, first_interval=3.0)", "")
_mens = _mens.replace("HIER = os.path.dirname(os.path.abspath(__file__))", f"HIER = {E2E!r}")
SM = {"__name__": "scherm_mens_hulp", "__file__": os.path.join(E2E, "scherm_mens.py")}
exec(compile(_mens, "scherm_mens_hulp", "exec"), SM)   # noqa: S102
M, A = SM["M"], SM["A"]
from scherm_basis import xdo  # noqa: E402

PROEF = os.environ.get("CJ_PROEF", "")          # "laag": alleen de schermindeling, dan stoppen
BREED_ZIJBALK = int(os.environ.get("CJ_ZIJBALK", "1080"))
UI = float(os.environ.get("CJ_UI", "2.0"))
film["metingen"] = {}
film["muis"] = []          # per beeld [x, y, klik] in X-schermpunten
film["vlakken"] = {}       # per deel: zijbalk en weergave [x, y, b, h] voor de uitsnede in kort.py
film["paneel_y"] = {}      # per deel: X-schermhoogte van wat in het paneel te zien moet zijn
MUIS = {"x": 700, "y": 900, "klik": 0}
VOORBIJ = 12.0


def mengen(a, b, t):
    return [x + (y - x) * t for x, y in zip(a, b)]


def srgb(h):
    c = tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    return tuple(((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


# Vrolijke speelgoedkleuren (invoer, zoals een koper zijn figuur een kleur geeft)
KLEUREN = {"pak": "FF9A3C", "hand": "2EC4B6", "laars": "2EC4B6", "hoofd": "F3C9A2"}


# ---------- muis ----------

def neem_m(houd=1):
    neem(houd)
    for i in range(houd):
        film["muis"].append([MUIS["x"], MUIS["y"], MUIS["klik"] if i == 0 else 0])
    MUIS["klik"] = 0


STAP = int(os.environ.get("CJ_STAP", "2"))   # elke stap STAP filmbeelden (15 opnames per seconde, sneller in CI)


def stuk(stappen, doe):
    n = max(1, stappen // STAP)
    for i in range(n):
        doe(zacht(i / max(1, n - 1)))
        yield 0.04
        neem_m(STAP)


def muis_naar(x, y, stappen=18, doe=None):
    """Echte muis in `stappen` beelden zacht naar (x, y); doe(t) mag tegelijk iets veranderen."""
    x0, y0 = MUIS["x"], MUIS["y"]
    stappen = max(1, stappen // STAP)
    for i in range(stappen):
        t = zacht((i + 1) / stappen)
        MUIS["x"], MUIS["y"] = int(x0 + (x - x0) * t), int(y0 + (y - y0) * t)
        xdo("mousemove", str(MUIS["x"]), str(MUIS["y"]))
        if doe is not None:
            doe(t)
        yield 0.04
        neem_m(STAP)


def klik():
    xdo("click", "1")
    MUIS["klik"] = 1


# ---------- scherm ----------

def rect(regio_type="UI"):
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                for r in gebied.regions:
                    if r.type == regio_type:
                        return [venster.x + r.x, venster.y + venster.height - (r.y + r.height), r.width, r.height]
    return None


def ocr(tekst, vak=None):
    """Plek (x, y) op het X-scherm van `tekst` (een of meer woorden) volgens tesseract, of None."""
    pad = "/tmp/cj_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    if vak is None:
        vak = rect("UI")
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", "65%",
                    "-negate", "/tmp/cj_ocr_v.png"], capture_output=True)   # lichte tekst op donker: zwart op wit
    r = subprocess.run(["tesseract", "/tmp/cj_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
    with open("/tmp/cj_ocr_laatst.tsv", "w") as f:
        f.write(r.stdout)
    woorden, regels = [], {}
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            w = (d[11].strip().lower().strip(".,:;(){}[]'\""), int(d[6]), int(d[7]), int(d[8]), int(d[9]))
            woorden.append(w)
            regels.setdefault((d[2], d[3], d[4]), []).append(w)
    doel = tekst.lower().split()
    for alleen_begin in (True, False):   # eerst regels die met `tekst` beginnen ("Bend" en niet "Flip bend")
        for ws in regels.values():
            ws.sort(key=lambda w: w[1])
            for i in ([0] if alleen_begin else range(len(ws) - len(doel) + 1)):
                if i + len(doel) <= len(ws) and all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                    stuk_ = ws[i:i + len(doel)]
                    xa, xb = min(w[1] for w in stuk_), max(w[1] + w[3] for w in stuk_)
                    ya, yb = min(w[2] for w in stuk_), max(w[2] + w[4] for w in stuk_)
                    return (x0 + (xa + xb) // 2, y0 + (ya + yb) // 2)
    log(f"KORT ocr niet gevonden: {tekst!r} ({len(woorden)} woorden: {' '.join(w[0] for w in woorden[:60])})")
    return None


def zoek(tekst, keer=5):
    """ocr() opnieuw na een korte pauze (panelen schuiven met een animatie open). Gebruik: r = yield from zoek(..)"""
    for _ in range(keer):
        r = ocr(tekst)
        if r:
            return r
        yield 0.6
    return None


def herteken():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            gebied.tag_redraw()


def sleep_zijbalk(breed):
    """Sleep de linkerrand van de zijbalk naar links tot hij `breed` punten breed is (echte muis). Probeert een paar
    plekken vlak bij de rand (de sleepzone is maar een paar punten breed) en geeft de nieuwe breedte."""
    for dx in (2, 6, 12, 18):
        z = rect("UI")
        if z[2] >= breed - 20:
            break
        x, y = z[0] + dx, z[1] + 300
        xdo("mousemove", str(x), str(y))
        yield 0.3
        xdo("mousedown", "1")
        yield 0.2
        doel = z[0] + z[2] - breed
        for i in range(1, 13):
            xdo("mousemove", str(int(x + (doel - x) * i / 12)), str(y))
            yield 0.05
        yield 0.2
        xdo("mouseup", "1")
        yield 0.4
        log(f"KORT zijbalk sleep dx={dx}: {rect('UI')}")


def wiel(knop, keer):
    z = rect("UI")
    for _ in range(keer):
        xdo("click", knop)
        time.sleep(0.03)
    return z


def kijk_breed():
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.shading.light = "STUDIO"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    ov = ruimte.overlay
    ov.show_cursor = False
    ov.show_stats = False
    ov.show_outline_selected = True
    ruimte.show_region_header = True
    ruimte.show_region_tool_header = False
    ruimte.show_region_toolbar = True


SCHAAL = {"k": None}          # punten per wereldeenheid x afstand (ortho), eenmaal gemeten
DOEL = {"x": 540, "y": 560}   # waar het richtpunt op het X-scherm moet staan (links, boven het paneel)


def cam(draai, kantel, afstand, punt, doel=None):
    """Ortho-camera die `punt` op X-schermpunt `doel` (standaard links boven) zet, niet in het midden: rechts staat
    de zijbalk over de weergave heen."""
    _, gebied, _ = zijbalk()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "ORTHO"
    q = Euler((math.radians(kantel), 0.0, math.radians(draai)), "XYZ").to_quaternion()
    rv.view_rotation = q
    rv.view_distance = afstand
    loc = Vector(punt)
    if SCHAAL["k"]:
        w = rect("WINDOW")
        cx, cy = w[0] + w[2] / 2, w[1] + w[3] / 2
        tx, ty = doel or (DOEL["x"], DOEL["y"])
        ppu = SCHAAL["k"] / afstand
        rechts, omhoog = q @ Vector((1.0, 0.0, 0.0)), q @ Vector((0.0, 1.0, 0.0))
        loc = loc + rechts * ((cx - tx) / ppu) - omhoog * ((cy - ty) / ppu)
    rv.view_location = loc
    gebied.tag_redraw()


def meet_schaal(punt, afstand):
    _, gebied, _ = zijbalk()
    q = gebied.spaces.active.region_3d.view_rotation
    a = scherm_punt(punt)
    b = scherm_punt(Vector(punt) + (q @ Vector((1.0, 0.0, 0.0))) * 20.0)
    if a and b:
        SCHAAL["k"] = abs(b[0] - a[0]) / 20.0 * afstand
    log(f"KORT schaal {SCHAAL['k']}")


def scherm_punt(p):
    """Wereldpunt naar X-schermpunt in de 3D-weergave."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    rv = gebied.spaces.active.region_3d
    q = location_3d_to_region_2d(regio, rv, Vector(p))
    if q is None:
        return None
    return int(venster.x + regio.x + q.x), int(venster.y + venster.height - (regio.y + q.y))


# ---------- figuur ----------

def verf(ob, p):
    """Speelgoedpop: elk vlak een kleur naar waar het zit (alleen invoer, voor de knop)."""
    mats = {}
    for k, h in KLEUREN.items():
        m = bpy.data.materials.new("toy_" + k)
        m.diffuse_color = srgb(h)
        m.roughness = 0.6
        mats[k] = m
    ob.data.materials.clear()
    volgorde = list(KLEUREN)
    for k in volgorde:
        ob.data.materials.append(mats[k])
    hz = (p["l-hand"].z + p["r-hand"].z) / 2
    hx = min(abs(p["l-hand"].x), abs(p["r-hand"].x))
    enkel = (p["l-ankle"].z + p["r-ankle"].z) / 2
    nek = p["neck"].z + (p["head"].z - p["neck"].z) * 0.35
    riem_lo, riem_hi = p["pelvis"].z + 2.0, p["pelvis"].z + 10.0
    for f in ob.data.polygons:
        c = f.center
        if c.z > nek:
            k = "hoofd"
        elif c.z < enkel + 9.0:
            k = "laars"
        elif abs(c.x) > hx - 4.0 and c.z < hz + 9.0:
            k = "hand"
        else:
            k = "pak"
        f.material_index = volgorde.index(k)
    ob.data.update()


def figuur():
    A["leeg"]()
    ob, punten = M["laad_mens"](os.environ["CJ_MENS_OBJ"])
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    SM["etalagepop"](ob)
    verf(ob, punten)
    arm = M["maak_rig"](punten)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    inst.exportmap = exportmap
    return ob, arm, punten


def geen_selectie():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


def paar(naam, soort="SCHARNIER"):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == soort:
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def buig(b, graden):
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(graden, 1)


def vlak(naam):
    film["vlakken"][naam] = {"zijbalk": rect("UI"), "weergave": rect("WINDOW")}


# ---------- verloop ----------

def verloop_pro():
    log(f"Blender {bpy.app.version_string}, zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    ob, arm, p = figuur()
    naam = ob.name
    SM["rustig"]()
    leeg_beeld()
    bpy.context.preferences.view.ui_scale = UI
    # zijbalk naast de weergave, niet erover: dan staat de tekst van de add-on midden in de linkerhelft
    bpy.context.preferences.system.use_region_overlap = False
    kijk_breed()
    _, gebied, _ = zijbalk()
    gebied.spaces.active.overlay.show_outline_selected = True
    SM["open_paneel"]()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    yield 0.5
    yield from sleep_zijbalk(BREED_ZIJBALK)
    yield 1.0
    xdo("mousemove", "400", "900")
    MUIS["x"], MUIS["y"] = 400, 900
    yield 0.5
    # hoofdpaneel inklappen: Figure joints met de knop komt bovenaan (klik op de kop, zoals een gebruiker)
    z = rect("UI")
    kop = ocr("Click Joints")
    log(f"KORT zijbalk {z} weergave {rect('WINDOW')} kop {kop}")
    if kop:
        xdo("mousemove", str(kop[0]), str(kop[1]))
        time.sleep(0.2)
        xdo("click", "1")
        time.sleep(0.2)
    yield 0.8
    xdo("mousemove", "400", "900")
    yield 0.5
    heel = (0.0, 0.0, 112.0)
    D_HEEL = 340.0
    cam(-25, 84.0, D_HEEL, heel)
    yield 0.8
    meet_schaal(heel, D_HEEL)
    cam(-25, 84.0, D_HEEL, heel)
    yield 0.5
    if PROEF == "laag":
        subprocess.run(["import", "-window", "root", os.path.join(scherm_basis.uitmap, "laag.png")])
        knop = ocr("Figure from rig")
        log(f"KORT laag knop {knop}")
        return

    # heel: figuur met rig, nog één stuk; de muis komt aanlopen
    vlak("heel")
    deel("heel")
    yield from stuk(40, lambda t: cam(-25 + 10 * t, 84.0, D_HEEL, heel))
    log("KORT OK heel")

    # kies: klik op de figuur (echte klik: Blender selecteert hem, oranje rand)
    deel("kies")
    arm.hide_select = True   # de klik moet de figuur raken, niet de botten ervoor
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    buik = scherm_punt((9.0, -8.0, 128.0))
    yield from muis_naar(buik[0], buik[1], 24)
    klik()
    for _ in range(5):
        yield 0.2
        if bpy.context.view_layer.objects.active == ob:
            break
    act = bpy.context.view_layer.objects.active
    log(f"KORT kies actief={act.name if act else None}")
    if act != ob:
        log("KORT vangnet kies: figuur via script actief")
        A["actief"](ob)
    yield 0.3
    neem_m(20)
    log("KORT OK kies")

    # knop: Figure from rig
    deel("knop")
    knop = yield from zoek("Figure from rig")
    film["metingen"]["knop_ocr"] = knop
    film["paneel_y"]["knop"] = knop[1] if knop else None
    if knop is None:
        knop = (rect("UI")[0] + rect("UI")[2] // 2, rect("UI")[1] + 160)
    yield from muis_naar(knop[0], knop[1], 26)
    neem_m(6)
    klik()
    yield 0.5
    t0 = time.time()
    while not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects) and time.time() - t0 < 60:
        yield 0.5
    if not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
        log("KORT vangnet knop: Figure from rig via script")
        A["actief"](ob)
        bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = [fig.regel(r) for r in lijst]
    film["metingen"]["samenvatting"] = fig.samenvatting(lijst)
    log(f"KORT knop {len(lijst)} gewrichten {film['metingen']['regels']}")
    geen_selectie()
    delen_fig = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH"]
    if delen_fig:   # actief blijft een deel van de figuur, zodat het paneel de lijst toont
        bpy.context.view_layer.objects.active = max(delen_fig, key=lambda o: len(o.data.vertices))
    yield 0.5
    neem_m(10)
    log(f"KORT {'OK' if len(lijst) >= 6 else 'FOUT'} knop")

    # lijst: de muis loopt langs de lijst met gewrichten en graden
    vlak("lijst")
    deel("lijst")
    eerste = yield from zoek(f"{len(lijst)} joints")
    film["paneel_y"]["lijst"] = eerste[1] if eerste else None
    film["metingen"]["lijst_ocr"] = eerste
    if eerste:
        yield from muis_naar(eerste[0] - 200, eerste[1], 20)
        yield from muis_naar(eerste[0] - 200, eerste[1] + 40 * max(1, len(lijst) - 1), 80)
    else:
        neem_m(100)
    yield from stuk(60, lambda t: cam(-15 + 25 * t, 84.0, D_HEEL, heel))
    log("KORT OK lijst")

    # knie: linkerknie kiezen (klik op het onderbeen), Bend-schuif tot de stop, voorbij de stop rood, terug
    a, b = paar("Left knee")
    if a is None or b is None:
        log("KORT FOUT knie: geen linkerknie")
        return
    stop = float(a["cj_bereik_graden"])
    film["metingen"]["knie_stop"] = stop
    film["metingen"]["knie_herkomst"] = a.get("cj_herkomst")
    k = p["l-knee"]
    blik = (k.x, k.y, k.z + 5.0)
    yield from stuk(30, lambda t: cam(10 + 60 * t, 84.0, D_HEEL + (165.0 - D_HEEL) * t, mengen(heel, blik, t)))
    deel("knie")
    onder = scherm_punt((p["l-knee"] + p["l-ankle"]) / 2)
    yield from muis_naar(onder[0], onder[1], 22)
    klik()
    yield 0.3
    if bpy.context.view_layer.objects.active is not b:
        log("KORT vangnet knie: onderbeen via script actief")
    geen_selectie()
    b.select_set(True)
    buig(b, 0.0)
    yield 0.5
    # hoofdpaneel weer open (klik op de kop): daar staat het blok Hinge met de Bend-schuif
    kop = ocr("Click Joints")
    if kop:
        yield from muis_naar(kop[0], kop[1], 20)
        klik()
        yield 0.5
        neem_m(4)
        yield 1.0
    vlak("knie")
    schuif = yield from zoek("Bend")
    film["metingen"]["bend_ocr"] = schuif
    film["paneel_y"]["knie"] = schuif[1] if schuif else None
    if schuif is None:
        schuif = (rect("UI")[0] + 300, rect("UI")[1] + 400)
    sx0 = schuif[0] - 60
    sx1 = rect("UI")[0] + rect("UI")[2] - 60
    yield from muis_naar(sx0, schuif[1], 22)
    s = math.floor(stop * 10) / 10
    neem_m(6)
    MUIS["klik"] = 1
    yield from muis_naar(sx0 + (sx1 - sx0) * 0.8, schuif[1], 100, doe=lambda t: buig(b, s * t))
    neem_m(40)
    film["metingen"]["knie_pose_stop"] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    deel("knie_rood")
    yield from muis_naar(sx1, schuif[1], 36, doe=lambda t: buig(b, stop + VOORBIJ * t))
    neem_m(60)
    film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
    yield from muis_naar(sx0 + (sx1 - sx0) * 0.45, schuif[1], 36,
                         doe=lambda t: buig(b, stop + VOORBIJ - (stop + VOORBIJ - 70.0) * t))
    neem_m(15)
    log(f"KORT {'OK' if film['metingen']['knie_rood_vlakken'] > 0 else 'FOUT'} knie {film['metingen']}")

    # pose: andere knie en ellebogen, terug naar de hele figuur
    deel("pose")
    standen = {"Left knee": 95.0, "Right knee": 25.0, "Left elbow": 130.0, "Right elbow": 75.0}
    paren = {n: paar(n) for n in standen}
    van = {n: float(pb.get("cj_pose_graden", 0.0)) if pb is not None else 0.0 for n, (pa, pb) in paren.items()}

    def zet_pose(t):
        for n, (pa, pb) in paren.items():
            if pb is not None:
                buig(pb, van[n] + (standen[n] - van[n]) * t)
        cam(70 - 95 * t, 84.0, 165.0 + (D_HEEL - 165.0) * t, mengen(blik, heel, t))
    yield from stuk(70, zet_pose)
    geen_selectie()
    bpy.context.view_layer.objects.active = b
    neem_m(20)
    log("KORT OK pose")

    # uitelkaar: Exploded view aan (echte klik), rustig rond
    vlak("uitelkaar")
    deel("uitelkaar")
    ex = yield from zoek("Exploded view")
    film["metingen"]["exploded_ocr"] = ex
    film["paneel_y"]["uitelkaar"] = ex[1] if ex else None
    inst = bpy.context.scene.click_joints
    if ex:
        yield from muis_naar(ex[0], ex[1], 22)
        klik()
        yield 0.5
    if not inst.uit_elkaar:
        log("KORT vangnet uitelkaar: Exploded view via script")
        inst.uit_elkaar = True
        herteken()
    bpy.context.view_layer.update()
    neem_m(6)
    yield from stuk(110, lambda t: cam(-25 + 70 * t, 84.0, D_HEEL, heel))
    los = [o.name for o in bpy.context.scene.objects if o.get("cj_deel") == "B" and o.delta_location.length > 1e-6]
    film["metingen"]["uit_elkaar_delen"] = len(los)
    log(f"KORT {'OK' if los else 'FOUT'} uitelkaar {len(los)}")

    # export: 3MF kiezen en Export (echte klikken), melding in de statusbalk
    exportmap = inst.exportmap
    herteken()
    yield 0.5
    vlak("export")
    deel("export")
    drie = yield from zoek("3MF")
    if drie:
        yield from muis_naar(drie[0], drie[1], 22)
        klik()
        yield 0.4
    if inst.formaat != "3MF":
        log("KORT vangnet export: 3MF via script")
        inst.formaat = "3MF"
        herteken()
        yield 0.6
    neem_m(6)
    for o in bpy.context.view_layer.objects:
        o.select_set(bool(o.get("cj_deel")))
    knop_e = yield from zoek("Export 3MF")
    film["metingen"]["export_ocr"] = knop_e
    film["paneel_y"]["export"] = knop_e[1] if knop_e else None
    if knop_e:
        yield from muis_naar(knop_e[0], knop_e[1], 22)
        klik()
        yield 1.5
    if not glob.glob(os.path.join(exportmap, "**", "*.3mf"), recursive=True):
        log("KORT vangnet export: Export via script")
        bpy.ops.click_joints.exporteer()
        yield 1.0
    neem_m(50)
    bestanden = sorted(os.path.basename(x) for x in glob.glob(os.path.join(exportmap, "**", "*.*"), recursive=True))
    film["metingen"]["export"] = bestanden
    log(f"KORT {'OK' if bestanden else 'FOUT'} export {len(bestanden)} {bestanden[:5]}")

    # held: dicht, figuur in pose (knie gebogen, arm omhoog), muis weg, rustig rond (eerste beeld van elke Short)
    inst.uit_elkaar = False
    geen_selectie()
    bpy.context.view_layer.update()
    yield from muis_naar(rect("WINDOW")[0] + 60, rect("WINDOW")[1] + rect("WINDOW")[3] - 80, 12)
    deel("held")
    yield from stuk(150, lambda t: cam(-40 + 80 * t, 84.0, D_HEEL - 20, heel))
    log("KORT OK held")


def verloop():
    try:
        yield from verloop_pro()
    except Exception as fout:  # noqa: BLE001
        import traceback
        log(f"KORT FOUT {fout}\n{traceback.format_exc()}")
    deel("eind")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
