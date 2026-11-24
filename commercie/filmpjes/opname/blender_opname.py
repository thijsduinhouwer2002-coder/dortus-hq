"""Gedeelde hulpcode voor opnames in echte Blender (Olaf, 24 nov 2026).

Waarom: elke tip-opname van de Regisseur (regisseur-3 tot en met 12) had dezelfde 20 hulpfuncties gekopieerd (±300
regels). Een les uit één run (OCR-drempel, menu wacht, muis een tikje bewegen) kwam zo niet vanzelf in de volgende.
Dit bestand is die hulpcode, gelijk aan `../regisseur-12/tip_opname.py`, plus drie dingen die elke tip opnieuw schreef:
`menu_pad` (menu > submenu > item met de echte muis), `knop` (OCR met meerdere drempels) en `start` (de timer met
film.json bij een fout).

Gebruik in een nieuwe opname (zie LEESMIJ.md):

    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
    from blender_opname import *          # noqa: F401,F403
    zet_naam("tip13")

    def verloop():
        zet_scherm()
        ...
        deel("eind")
        einde()

    start(verloop)

Hash in de workflow: neem dit bestand mee in de sha van de opname, anders wordt een oude ruwe opname hergebruikt
na een wijziging hier.
"""
import json
import math
import os
import subprocess
import sys

import bmesh
import bpy
from mathutils import Euler, Vector

__all__ = ["bpy", "bmesh", "math", "os", "sys", "json", "subprocess", "Vector", "Euler",
           "uitmap", "beeldmap", "film", "MUIS", "SNEL",
           "zet_naam", "log", "xdo", "neem", "deel", "zacht", "herteken", "gebied", "regio_rect", "muis_naar", "klik",
           "dubbelklik", "toets", "typ", "ocr", "knop", "zoek", "houd", "zet_scherm", "cam", "stuk", "selecteer",
           "zachte_muis_in_beeld", "nonmanifold_tellen", "wacht_ocr", "kop_menu", "add_item", "menu_pad",
           "bovenbalk", "bewaar_film", "einde", "start", "stl_maat", "maat_mm", "exporteer_stl"]

uitmap = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "/tmp/opname"
beeldmap = os.path.join(uitmap, "beelden")
os.makedirs(beeldmap, exist_ok=True)
film = {"fps": 30, "delen": {}, "n": 0, "muis": [], "metingen": {}}
MUIS = {"x": 1500, "y": 1500, "klik": 0}
SNEL = int(os.environ.get("CJ_SNEL", "1"))     # proef: elk n-de beeld echt pakken
_NAAM = {"tag": "opname"}


def zet_naam(tag):
    """Naam voor de log-regels en de tijdelijke OCR-bestanden."""
    _NAAM["tag"] = tag


def log(t):
    print(f"[{_NAAM['tag']}] {t}", flush=True)


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
    """[x, y, breedte, hoogte] in schermpixels (y van boven) van een regio van gebied a."""
    w = bpy.context.window_manager.windows[0]
    for r in a.regions:
        if r.type == soort:
            return [w.x + r.x, w.y + w.height - (r.y + r.height), r.width, r.height]
    return None


def bovenbalk():
    """Vak van de bovenste menubalk (File, Edit, ...)."""
    _, tb = gebied("TOPBAR")
    return regio_rect(tb, "HEADER") if tb else [0, 0, 2160, 60]


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


def dubbelklik():
    xdo("click", "--repeat", "2", "1")
    MUIS["klik"] = 1


def toets(*k):
    xdo("key", *k)


def typ(tekst, beelden=5, pauze=0.15):
    """Tekens één voor één (zichtbaar typen). Alleen letters, cijfers en punt; spatie als 'space'."""
    for c in tekst:
        toets({" ": "space", ".": "period", "-": "minus"}.get(c, c))
        yield pauze
        neem(beelden)


def ocr(tekst, vak, drempel="60%", woord=None):
    """Midden (x, y) van `tekst` (een of meer woorden op één regel) in vak [x, y, b, h], of None.
    drempel: 60% voor witte tekst, 35% voor grijze (uitgezet vinkje, veldnaam). woord: alleen dat woord van de reeks."""
    tag = _NAAM["tag"]
    pad, vpad = f"/tmp/{tag}_ocr.png", f"/tmp/{tag}_ocr_v.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold", drempel,
                    "-negate", vpad], capture_output=True)
    r = subprocess.run(["tesseract", vpad, "stdout", "--psm", "11", "tsv"], capture_output=True, text=True)
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


def knop(tekst, vak, drempels=("35%", "60%", "75%")):
    """OCR met oplopende drempels (les run 12: witte tekst op een blauwe knop leest tesseract slecht bij één drempel)."""
    for dr in drempels:
        p = ocr(tekst, vak, dr)
        if p:
            return p
    return None


def zoek(tekst, vak, keer=4):
    for _ in range(keer):
        p = ocr(tekst, vak)
        if p:
            return p
        yield 0.4
    return None


def houd(n):
    """Stilstaand beeld van ±n beelden (elke schermfoto telt twee keer)."""
    for _ in range(max(1, n // 2)):
        yield 0.03
        neem(2)


# ---------- scherm ----------

def zet_scherm(mm=True):
    """UI-schaal 2, lege scène, alleen de 3D-weergave groot, geen werkbalk, zijbalk of navigatie.
    mm=True: Unit Scale 0,001 met millimeter (1 Blender-eenheid is 1 mm)."""
    p = bpy.context.preferences
    p.view.ui_scale = float(os.environ.get("CJ_UI", "2.0"))
    p.view.show_splash = False
    p.view.show_tooltips = False
    p.view.filebrowser_display_type = "SCREEN"   # run 12: los venster viel rechts buiten het X-scherm (geen WM)
    sc = bpy.context.scene
    for o in list(sc.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    if mm:
        sc.unit_settings.system = "METRIC"
        sc.unit_settings.scale_length = 0.001
        sc.unit_settings.length_unit = "MILLIMETERS"
    w = bpy.context.window_manager.windows[0]
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
    p.themes[0].view_3d.object_origin_size = 10   # grotere oorsprong-stip (leesbaar op een telefoon)
    sp.overlay.grid_scale = 0.001 if mm else 1.0
    sp.clip_start, sp.clip_end = 1.0, 100000.0
    sp.show_region_toolbar = False
    sp.show_region_ui = False
    sp.show_gizmo_navigate = False
    log(f"KORT scherm {w.width}x{w.height} gebieden {len(w.screen.areas)}")
    return a


def cam(draai, kantel, afstand, punt):
    _, a = gebied("VIEW_3D")
    r3 = a.spaces.active.region_3d
    r3.view_perspective = "PERSP"
    r3.view_rotation = Euler((math.radians(kantel), 0, math.radians(draai)), "XYZ").to_quaternion()
    r3.view_distance = afstand
    r3.view_location = Vector(punt)
    herteken()


def stuk(n, doe):
    """±n beelden waarin doe(t) met t van 0 naar 1 (zacht) loopt, bijvoorbeeld een camerabeweging."""
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


# ---------- menu's met de echte muis ----------

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


def menu_pad(vak, pad, meet, knop_woord=None, klik_wacht=1.0):
    """Klik een menu langs `pad` met de echte muis, bijvoorbeeld menu_pad(bovenbalk(), ["File", "Export", "STL"], "j").
    Eerste stap: knop in vak (OCR, 60%). Elke volgende stap: wacht tot hij getekend is in een vak onder of rechts van
    de vorige. Tussenstappen hoveren (submenu), de laatste klikken. Metingen in film["metingen"][meet + "_1"] enz.
    Geeft True als alles raakte; anders twee keer Escape en False (doe dan een vangnet in je script)."""
    p = ocr(pad[0], vak, woord=knop_woord)
    film["metingen"][f"{meet}_1"] = p
    if not p:
        return False
    yield from muis_naar(p[0], p[1], 16)
    neem(4)
    klik()
    vorige = p
    for i, naam in enumerate(pad[1:], start=2):
        if i == 2:      # menu valt open onder de knop
            zoekvak = [max(0, p[0] - 200), p[1], 900, 1300]
        else:           # submenu klapt rechts uit, kan hoger beginnen
            zoekvak = [vorige[0] + 100, max(0, vorige[1] - 400), 1000, 1300]
        q = yield from wacht_ocr(naam, zoekvak, vorige)
        film["metingen"][f"{meet}_{i}"] = q
        if not q:
            toets("Escape")
            toets("Escape")
            return False
        if i > 2:       # eerst horizontaal het submenu in, dan pas omhoog of omlaag (anders sluit het submenu)
            yield from muis_naar(vorige[0] + 330, vorige[1], 6)
        yield from muis_naar(q[0], q[1], 14 if i < len(pad) else 12)
        vorige = q
    neem(6)
    klik()
    yield klik_wacht
    neem(6)
    return True


def kop_menu(kop, knop_tekst, knop_woord, sub, item, item_vak_dx, meet):
    """Menu in de kop (knop via OCR), submenu hoveren, item klikken. True als het zo ging. (vorm van regisseur-11/12)"""
    p = ocr(knop_tekst, kop, woord=knop_woord)
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


# ---------- meten ----------

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
            q = struct.unpack("<3f", data[b + 12 * k:b + 12 * k + 12])
            for j in range(3):
                lo[j], hi[j] = min(lo[j], q[j]), max(hi[j], q[j])
    return [round(hi[j] - lo[j], 4) for j in range(3)]


def maat_mm(ob, per_eenheid=1000):
    """Afmetingen in mm. per_eenheid 1000 bij Unit Scale 1 (meter), 1 bij zet_scherm(mm=True)."""
    d = ob.dimensions
    return [round(d.x * per_eenheid, 1), round(d.y * per_eenheid, 1), round(d.z * per_eenheid, 1)]


def exporteer_stl(pad, schaal=1.0):
    try:
        bpy.ops.wm.stl_export(filepath=pad, global_scale=schaal, export_selected_objects=True)
    except TypeError:
        bpy.ops.wm.stl_export(filepath=pad, global_scale=schaal)


# ---------- begin en einde ----------

def bewaar_film():
    with open(os.path.join(uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)


def einde():
    """Aan het eind van verloop(): film.json schrijven, KORT klaar loggen, Blender sluiten."""
    bewaar_film()
    log(f"KORT klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


def start(verloop, eerste=3.0):
    """Laat verloop() (een generator die seconden yieldt) lopen op Blenders timer. Een fout geeft 'KORT FOUT' met de
    traceback in de log, schrijft film.json (voor de diagnose) en sluit Blender."""
    gang = verloop()

    def stap():
        try:
            return next(gang)
        except StopIteration:
            return None
        except Exception as f:  # noqa: BLE001
            import traceback
            log(f"KORT FOUT {f}\n{traceback.format_exc()}")
            bewaar_film()
            bpy.ops.wm.quit_blender()
            return None
    bpy.app.timers.register(stap, first_interval=eerste)
