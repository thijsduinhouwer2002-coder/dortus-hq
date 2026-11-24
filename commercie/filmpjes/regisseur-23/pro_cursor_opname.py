"""Opname clip 3 van de Click Joints Pro video guide (regisseur-23, Regisseur run 24, 24 nov 2026), opdracht Chris:
een gewricht op de 3D-cursor bij een model dat al in stukken is. Ook bron voor een Pro-Short ("Already split?").
Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, Pro-zip (e2e/maak_zip.sh betaald).
Verloop met de echte muis: eigen figuur in losse delen (romp, hoofd, armen, benen: elk een eigen object, zoals na
het splitsen in een ander programma), klik op het linkerbeen, Shift + rechtsklik op de knie (3D-cursor), zijbalk naar
Click Joints (Ctrl+wiel), klik "Knee" onder Figure joints, dan "Show bend range", camera naar de knie.
Geen vangnet: lukt een klik niet, dan KORT FOUT (eerlijk: wat in beeld staat is echt gebeurd).
Metingen in film.json: cursor-assen na Shift + rechtsklik, melding van Knee, passing, buigbereik, plekken (OCR).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python pro_cursor_opname.py -- <uitmap> <pro zip>"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
from bpy_extras import view3d_utils  # noqa: E402

zet_naam("pro23")
ZIP = sys.argv[sys.argv.index("--") + 2] if len(sys.argv) > sys.argv.index("--") + 2 else "/tmp/click_joints_betaald.zip"
M = film["metingen"]
KNIE = (-28.0, 0.0, 95.0)   # been r 22: r 15 en 16 gaf "Too thin here for a hinge" (proef run 24)


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


def zoek_scroll(tekst, richting="5", keer=10, drempels=("35%", "60%", "75%")):
    """OCR in de zijbalk; niet gevonden: met het muiswiel scrollen (echt) en opnieuw kijken."""
    vak = ui_vak()
    for _ in range(keer):
        p = knop(tekst, vak, drempels)
        if p:
            return p
        xdo("mousemove", str(vak[0] + vak[2] // 2), str(vak[1] + vak[3] // 2))
        MUIS["x"], MUIS["y"] = vak[0] + vak[2] // 2, vak[1] + vak[3] // 2
        for _k in range(3):
            xdo("click", richting)
            yield 0.05
            neem()
        yield 0.5
        neem(2)
    return None


def mat(naam, kleur):
    m = bpy.data.materials.new(naam)
    m.diffuse_color = kleur
    m.roughness = 0.5
    return m


def blok(naam, maak, kleur):
    maak()
    ob = bpy.context.active_object
    ob.name = naam
    for f in ob.data.polygons:
        f.use_smooth = True
    ob.data.materials.append(kleur)
    return ob


def maak_figuur():
    """Figuur van ±260 mm in losse delen. Elk deel is een eigen, waterdicht object (zoals na splitsen)."""
    oranje = mat("been", (0.95, 0.45, 0.12, 1))
    blauw = mat("romp", (0.16, 0.38, 0.85, 1))
    wit = mat("kop", (0.9, 0.9, 0.88, 1))
    delen = {}
    delen["Leg.L"] = blok("Leg.L", lambda: bpy.ops.mesh.primitive_cylinder_add(
        vertices=64, radius=22, depth=170, location=(KNIE[0], 0, 87)), oranje)
    delen["Leg.R"] = blok("Leg.R", lambda: bpy.ops.mesh.primitive_cylinder_add(
        vertices=64, radius=22, depth=170, location=(-KNIE[0], 0, 87)), oranje)
    delen["Body"] = blok("Body", lambda: bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 215)), blauw)
    delen["Body"].scale = (78, 40, 80)
    delen["Head"] = blok("Head", lambda: bpy.ops.mesh.primitive_uv_sphere_add(
        segments=48, ring_count=24, radius=24, location=(0, 0, 285)), wit)
    for kant, x in (("L", -52), ("R", 52)):
        delen["Arm." + kant] = blok("Arm." + kant, lambda x=x: bpy.ops.mesh.primitive_cylinder_add(
            vertices=48, radius=10, depth=110, location=(x, 0, 200)), oranje)
    bpy.ops.object.select_all(action="DESELECT")
    return delen


def delen_ab():
    return [o for o in bpy.context.scene.objects if o.get("cj_deel") in ("A", "B")]


def verloop():
    a3 = zet_scherm(mm=True)
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    d = maak_figuur()
    been = d["Leg.L"]
    sc.cursor.location = (0, 0, 0)
    sp = a3.spaces.active
    sp.overlay.show_cursor = True
    bpy.context.preferences.system.use_region_overlap = False
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    sp.show_region_ui = True
    sc.click_joints.uit_elkaar = False
    M["as_bron"] = sc.click_joints.as_bron
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Joints {ok}")
    xdo("mousemove", "400", "900")
    MUIS["x"], MUIS["y"] = 400, 900
    midden = (0.0, 0.0, 150.0)
    cam(-35, 78.0, 620.0, midden)
    yield 1.0

    deel("mooi")
    yield from stuk(60, lambda t: cam(-35 + 30 * t, 78.0 + 6 * t, 620.0 - 60 * t, midden))

    # klik op het linkerbeen (echte muis)
    deel("kies")
    p = scherm_punt((KNIE[0], -22, 50))
    yield from muis_naar(p[0], p[1], 22)
    klik()
    yield 0.4
    neem(6)
    M["kies_actief"] = bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None
    if M["kies_actief"] != been.name:
        log(f"KORT FOUT kies: actief is {M['kies_actief']}")
        einde()
        return
    log("KORT OK kies")
    yield from houd(16)

    # Shift + rechtsklik op de knie (echte muis): de 3D-cursor
    deel("cursor")
    p = scherm_punt((KNIE[0], -22, KNIE[2]))
    yield from muis_naar(p[0], p[1], 22)
    yield 0.3
    xdo("keydown", "shift")
    yield 0.2
    xdo("click", "3")
    MUIS["klik"] = 1
    yield 0.2
    xdo("keyup", "shift")
    yield 0.5
    neem(6)
    c = sc.cursor
    M["cursor_plek"] = [round(v, 2) for v in c.location]
    M["cursor_z"] = [round(v, 3) for v in c.matrix.col[2].xyz]
    log(f"KORT cursor {M['cursor_plek']} z-as {M['cursor_z']}")
    if abs(c.location.z - KNIE[2]) > 8:
        log("KORT FOUT cursor: niet op de knie")
        einde()
        return
    log("KORT OK cursor")
    yield from houd(30)

    # Knee onder Figure joints
    deel("knee")
    kn = yield from zoek_scroll("Knee")
    M["knee_ocr"] = kn
    if not kn:
        log("KORT FOUT knee: knop niet gevonden")
        einde()
        return
    yield 0.6
    kn = knop("Knee", ui_vak()) or kn   # na het scrollen opnieuw lezen (les run 19)
    yield from muis_naar(kn[0], kn[1], 22)
    neem(4)
    klik()
    yield 3.0
    neem(6)
    ab = delen_ab()
    M["delen"] = [o.name for o in ab]
    if len(ab) != 2:
        log(f"KORT FOUT knee: {len(ab)} delen, objecten {[o.name for o in sc.objects]}")
        einde()
        return
    a_deel = [o for o in ab if o.get("cj_deel") == "A"][0]
    M["passing"] = a_deel.get("cj_passing")
    M["melding"] = a_deel.get("cj_melding")
    M["stand"] = a_deel.get("cj_hoek")
    M["buig_graden"] = list(a_deel.get("cj_buig_graden", []))
    M["wand_mm"] = round(float(a_deel.get("cj_wand_mm", -1)), 3)
    log(f"KORT OK knee {M['passing']} {M['melding']} buig {M['buig_graden']} wand {M['wand_mm']}")
    yield from houd(40)
    for naam, tekst in (("fit_ocr", "fit"), ("bends_ocr", "Bends"), ("lijst_ocr", "Knee: hinge")):
        M[naam] = ocr(tekst, ui_vak(), "35%")

    # Show bend range
    deel("bereik")
    sb = yield from zoek_scroll("Show bend range", "4")
    M["bereik_ocr"] = sb
    if not sb:
        sb = yield from zoek_scroll("Show bend range", "5")
    if not sb:
        log("KORT FOUT bereik: knop niet gevonden")
        einde()
        return
    yield 0.6
    sb = knop("Show bend range", ui_vak()) or sb
    yield from muis_naar(sb[0], sb[1], 22)
    klik()
    yield 0.8
    neem(6)
    M["toon_bereik"] = bool(sc.click_joints.toon_bereik)
    if not M["toon_bereik"]:
        log("KORT FOUT bereik: niet aan")
        einde()
        return
    log("KORT OK bereik")
    xdo("mousemove", "300", "1700")
    MUIS["x"], MUIS["y"] = 300, 1700
    yield from houd(20)
    knie = Vector(KNIE)
    yield from stuk(110, lambda t: cam(-5 - 80 * t, 84.0 - 6 * t, 540.0 - 330 * t, Vector(midden).lerp(knie, t)))
    yield from houd(50)

    deel("eind")
    log("KORT OK alles")
    einde()


start(verloop)
