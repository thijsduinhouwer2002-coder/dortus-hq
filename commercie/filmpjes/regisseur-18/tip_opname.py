"""Opname tip-speling (regisseur-18, Regisseur run 17, 24 nov 2026): is je speling echt 0,2 mm? Gemeten na de snede.
Script: week 51 nr. 6 (commercie/filmpjes/scripts/week-51-click-joints.md, hook 6A), gratis Click Joints.
Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, gratis zip (e2e/maak_zip.sh).
Verloop met de echte muis: eigen cilinder van 80 mm (r 14 mm), 3D-cursor in het midden, zijbalk naar Click Joints
(Ctrl+wiel), klik op de cilinder, klik "Ball", klik "Place joint"; paneel toont "Good fit", "Wall: N mm" en
"Clearance: N mm (measured)"; klik "Exploded view", camera rond de kogel.
Metingen in film.json: speling ingesteld en gemeten, wand, passing (uit de delen zelf), plekken van de regels (OCR).
Lokale proef 24 nov zonder scherm: gemeten 0,1996 mm bij 0,2 ingesteld, wand 4,033 mm, groen (GEZIEN).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python tip_opname.py -- <uitmap> <gratis zip>"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
from bpy_extras import view3d_utils  # noqa: E402

zet_naam("tip18")
ZIP = sys.argv[sys.argv.index("--") + 2] if len(sys.argv) > sys.argv.index("--") + 2 else "/tmp/click_joints.zip"
M = film["metingen"]


def zijbalk():
    _, a = gebied("VIEW_3D")
    for r in a.regions:
        if r.type == "UI":
            return a, r
    return a, None


def ui_vak():
    _, a = gebied("VIEW_3D")
    return regio_rect(a, "UI")


def scherm_punt(p):
    _, a = gebied("VIEW_3D")
    r = [x for x in a.regions if x.type == "WINDOW"][0]
    q = view3d_utils.location_3d_to_region_2d(r, a.spaces.active.region_3d, Vector(p))
    v = regio_rect(a)
    return int(v[0] + q.x), int(v[1] + v[3] - q.y)


def naar_tabblad(doel="Click Joints"):
    w = bpy.context.window_manager.windows[0]
    for poging in range(16):
        a, r = zijbalk()
        if r.active_panel_category == doel:
            return True
        x = w.x + r.x + r.width - 8
        y = w.y + w.height - (r.y + r.height // 2)
        xdo("mousemove", str(x), str(y))
        xdo("keydown", "ctrl")
        xdo("click", "5" if poging < 7 else "4")
        xdo("keyup", "ctrl")
        yield 0.4
    return False


def maak_deel():
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=14, depth=80, location=(0, 0, 40))
    ob = bpy.context.active_object
    ob.name = "Arm"
    for f in ob.data.polygons:
        f.use_smooth = True
    m = bpy.data.materials.new("arm")
    m.diffuse_color = (0.95, 0.45, 0.12, 1)
    m.roughness = 0.5
    ob.data.materials.append(m)
    return ob


def delen():
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_deel") == "A":
            a = o
        elif o.get("cj_deel") == "B":
            b = o
    return a, b


def verloop():
    a3 = zet_scherm(mm=True)
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    ob = maak_deel()
    sc.cursor.location = (0, 0, 40)
    sp = a3.spaces.active
    sp.overlay.show_cursor = True
    bpy.context.preferences.system.use_region_overlap = False
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    sp.show_region_ui = True
    sc.click_joints.uit_elkaar = False   # staat standaard aan; de kijker zet hem later zelf aan
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Joints {ok}")
    xdo("mousemove", "400", "900")
    MUIS["x"], MUIS["y"] = 400, 900
    midden = (0.0, 0.0, 40.0)
    cam(-30, 72.0, 260.0, midden)
    yield 1.0

    deel("mooi")
    yield from stuk(50, lambda t: cam(-30 + 20 * t, 72.0, 260.0 - 30 * t, midden))

    # klik op de cilinder (echte muis)
    deel("kies")
    p = scherm_punt((0, -14, 52))
    yield from muis_naar(p[0], p[1], 22)
    klik()
    yield 0.4
    neem(6)
    if bpy.context.view_layer.objects.active is not ob:
        log("KORT vangnet kies: cilinder via script actief")
        selecteer(ob)
    yield from houd(20)

    # Ball kiezen en de speling laten zien
    deel("bal")
    vak = ui_vak()
    M["ui_vak"] = vak
    # Ball en Clearance staan op een blauwe knop of schuif: OCR leest ze niet (proef run 17). Plek vanaf Place joint
    # (grijs, wel leesbaar): Ball 187 px erboven, Clearance 71 px erboven (UI-schaal 2, GEZIEN in de proef).
    pj = knop("Place joint", vak)
    M["place_ocr"] = pj
    bal = (pj[0] - 135, pj[1] - 187) if pj else None
    M["bal_ocr"] = bal
    if bal:
        yield from muis_naar(bal[0], bal[1], 22)
        klik()
        yield 0.4
        neem(6)
    else:
        log("KORT vangnet bal: Ball via script")
    sc.click_joints.soort = "KOGEL"
    sc.click_joints.speling_mm = 0.2
    sc.click_joints.as_bron = "CURSOR"
    yield 0.4
    cl = (pj[0] - 130, pj[1] - 71) if pj else None
    M["clearance_veld_ocr"] = cl
    if cl:
        yield from muis_naar(cl[0] + 120, cl[1], 18)
    yield from houd(40)

    # Place joint
    deel("plaats")
    if pj:
        yield from muis_naar(pj[0], pj[1], 20)
        neem(4)
        klik()
        yield 2.0
        neem(6)
    a, b = delen()
    if a is None:
        log("KORT vangnet plaats: Place joint via script")
        selecteer(ob)
        bpy.ops.click_joints.plaats()
        yield 1.0
        a, b = delen()
    if a is None:
        log("KORT FOUT plaats: geen delen")
        einde()
        return
    M["passing"] = a.get("cj_passing")
    M["wand_mm"] = round(float(a.get("cj_wand_mm", -1)), 3)
    M["speling_ingesteld_mm"] = round(float(a.get("cj_speling_mm", -1)), 3)
    M["speling_gemeten_mm"] = round(float(a.get("cj_speling_gemeten_mm", -1)), 4)
    log(f"KORT plaats {M['passing']} wand {M['wand_mm']} speling {M['speling_ingesteld_mm']} gemeten {M['speling_gemeten_mm']}")
    xdo("mousemove", str(vak[0] + 60), str(vak[1] + vak[3] - 80))
    MUIS["x"], MUIS["y"] = vak[0] + 60, vak[1] + vak[3] - 80
    yield 0.8

    # de regels in het paneel
    deel("meet")
    yield from houd(10)
    for naam, tekst in (("fit_ocr", "Good fit"), ("wall_ocr", "Wall"), ("gemeten_ocr", "measured")):
        M[naam] = ocr(tekst, vak, "35%")
    yield from houd(70)

    # Exploded view: kogel uit de kom
    deel("uit")
    ex = (pj[0], pj[1] + 70) if pj else None   # knop direct onder Place joint
    M["exploded_ocr"] = ex
    if ex:
        yield from muis_naar(ex[0], ex[1], 20)
        klik()
        yield 0.6
        neem(6)
    if not sc.click_joints.uit_elkaar:
        log("KORT vangnet uit: Exploded view via script")
        sc.click_joints.uit_elkaar = True
    M["uit_elkaar"] = bool(sc.click_joints.uit_elkaar)
    xdo("mousemove", "300", "1700")
    MUIS["x"], MUIS["y"] = 300, 1700
    yield 0.6
    yield from stuk(120, lambda t: cam(-10 + 70 * t, 75.0 - 10 * t, 230.0 - 60 * t, midden))
    yield from houd(30)

    deel("eind")
    log("KORT OK alles")
    einde()


start(verloop)
