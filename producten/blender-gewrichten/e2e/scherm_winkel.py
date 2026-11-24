"""Winkelschermbeelden Pro (opdracht hoofdchat 24 nov, Thijs "die 1e"): drie echte schermbeelden van Blender.

Hele venster 1920x1080, interface op 1,5x (leesbaar in een kleine weergave), zijbalk breder getrokken.
Figuur: MakeHuman (CC0) met rig, zoals plaatje 19 (scherm_mens.py, hier ingeladen zonder zijn eigen volgorde).
  w1-figuur      Figure from rig net na de knop: alle gewrichten met hun graden (Labels: All), het hoofdpaneel
                 ingeklapt zodat Figure joints met de lijst in beeld staat
  w2-uitelkaar   zelfde figuur in Exploded view, hoofdpaneel open met stap 3 (Fit and export)
  w3-testkaart   Fit test strip (scharnier) met de vijf spelingen en hun nummers, figuur verborgen
Per beeld een regel "WINKEL beeld <naam> ..." en aan het eind "WINKEL OK" als alle drie er zijn.
    CJ_MENS_OBJ=<base.obj> blender --python e2e/scherm_winkel.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys
import time

import bpy
from mathutils import Euler, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
_src = open(os.path.join(HIER, "scherm_mens.py"), encoding="utf-8").read()
_START = "\nbpy.app.timers.register(stap, first_interval=3.0)\n"
assert _src.count(_START) == 1, "scherm_mens.py: de regel die de eigen volgorde start is veranderd"
_src = _src.replace(_START, "\n")
if os.environ.get("CJ_WINKEL_MEER", "1") == "1":  # More bones (ankles too), zodat de enkels in de lijst staan
    _KNOP = "bpy.ops.click_joints.figuur_uit_rig()"
    assert _src.count(_KNOP) == 1, "scherm_mens.py: de aanroep van Figure from rig is veranderd"
    _src = _src.replace(_KNOP, "bpy.ops.click_joints.figuur_uit_rig(meer=True)")
S = {"__name__": "scherm_mens_lib", "__file__": os.path.join(HIER, "scherm_mens.py")}
exec(compile(_src, "scherm_mens.py", "exec"), S)
from scherm_basis import klap_hoofdpaneel, log, open_paneel, toestand, uitmap, wiel_naar_tabblad, xdo, zijbalk, zip_pad  # noqa: E402

SCHAAL = float(os.environ.get("CJ_WINKEL_SCHAAL", "1.5"))
BREDER = int(os.environ.get("CJ_WINKEL_BREDER", "260"))  # zoveel pixels de zijbalk naar links trekken
# w2: bij 1,5x blijven Folder, STL/3MF en Export onder de rand, ook na scrollen tot het eind (run 45447006294,
# GEZIEN). 1,25x is nog steeds groter dan de standaard en laat het hele paneel tot de exportknop zien.
# Keuring Daan 24 nov (M2): bij 1,25x is stap 3 op 600 px niet te lezen. Nu 2x, hoofdpaneel tot onderaan gescrold,
# zodat stap 2 en 3 (Good fit, Export STL) groot in beeld staan; stap 1 mag boven de rand vallen.
SCHAAL_W2 = float(os.environ.get("CJ_WINKEL_SCHAAL_W2", "2.0"))
staat = {"beelden": [], "i": 0, "fase": "zet"}


def _mod(naam):
    return importlib.import_module(f"bl_ext.user_default.click_joints.{naam}")


def niets_gekozen():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None


def kies_romp():
    """Het grootste deel van het figuur actief (de romp), zodat Figure joints de lijst en de knoppen toont en stap 3
    de export van dit figuur. De oranje rand is uit (rustig)."""
    delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_deel") and o.visible_get()]
    if not delen:
        return None
    romp = max(delen, key=lambda o: len(o.data.vertices))
    niets_gekozen()
    for o in delen:
        o.select_set(True)
    bpy.context.view_layer.objects.active = romp
    return romp


def breder():
    venster, gebied, regio = zijbalk()
    if not regio:
        return False
    x = venster.x + regio.x + 2
    y = venster.y + venster.height - (regio.y + regio.height // 2)
    xdo("mousemove", str(x), str(y))
    time.sleep(0.2)
    xdo("mousedown", "1")
    for stap_x in range(1, 11):
        xdo("mousemove", str(x - BREDER * stap_x // 10), str(y))
        time.sleep(0.05)
    xdo("mouseup", "1")
    gebied.tag_redraw()
    return True


def labels_alle():
    wm = bpy.context.window_manager
    if hasattr(wm, "cj_labels"):
        wm.cj_labels = "ALL"


def kijk_figuur():
    S["kijk"]()
    _v, gebied, _r = zijbalk()
    rv = gebied.spaces.active.region_3d
    # Bredere zijbalk: het figuur iets naar links in het beeld schuiven (kijkpunt naar rechts).
    rv.view_location = Vector(rv.view_location) + rv.view_rotation @ Vector((float(os.environ.get("CJ_WINKEL_SCHUIF", "60")), 0, 0))


def testkaart():
    for o in list(bpy.context.scene.objects):
        if o.users_collection and all(c.name != "Fit test" for c in o.users_collection):
            o.hide_set(True)
    bpy.context.scene.click_joints.uit_elkaar = False
    uit = bpy.ops.click_joints.testkaart(soort="SCHARNIER")
    delen = [o for o in bpy.context.scene.objects if any(c.name == "Fit test" for c in o.users_collection)]
    log(f"WINKEL testkaart {uit} delen={len(delen)}")
    niets_gekozen()
    if not delen:
        return
    lo = Vector((min(min((o.matrix_world @ Vector(h))[i] for h in o.bound_box) for o in delen) for i in range(3)))
    hi = Vector((max(max((o.matrix_world @ Vector(h))[i] for h in o.bound_box) for o in delen) for i in range(3)))
    _v, gebied, _r = zijbalk()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "ORTHO"
    rv.view_rotation = Euler((math.radians(50), 0.0, math.radians(-20)), "XYZ").to_quaternion()
    midden = (lo + hi) / 2
    rv.view_location = midden + rv.view_rotation @ Vector((0.18 * (hi - lo).length, 0, 0))
    rv.view_distance = 1.05 * (hi - lo).length


def schiet(naam):
    pad = os.path.join(uitmap, f"{naam}.png")
    r = subprocess.run(["import", "-window", "root", pad], capture_output=True, text=True)
    _v, _g, regio = zijbalk()
    log(f"WINKEL beeld {naam} bestand={os.path.exists(pad)} zijbalk={regio.width if regio else None}px "
        f"schaal={bpy.context.preferences.view.ui_scale} {r.stderr.strip()}")
    if os.path.exists(pad):
        staat["beelden"].append(naam)


def schaal(waarde):
    bpy.context.preferences.view.ui_scale = waarde


def zijbalk_omlaag():
    """w2 (Daan M2): bij 2x staat stap 3 onder de rand. Het wiel (xdotool) en view2d.scroll_down(deltay=...) deden
    hier niets: deltay wordt genegeerd, de muis kwam niet aan (ronde 7, GEZIEN). Wat wel werkt (lokaal getest in 5.3.0
    onder Xvfb): view2d.scroll_down zonder argumenten met een volledige context (window, screen, area, region); elke
    aanroep is één vaste stap. Zoveel stappen dat "3  Fit and export" bovenaan staat en Export STL er nog onder past.
    Daarna de muis naar een leeg stuk van het beeld, anders staat er een hulpballon in het beeld."""
    venster, gebied, regio = zijbalk()
    if not regio:
        return
    with bpy.context.temp_override(window=venster, screen=venster.screen, area=gebied, region=regio):
        for _ in range(int(os.environ.get("CJ_WINKEL_STAPPEN", "9"))):
            bpy.ops.view2d.scroll_down("EXEC_DEFAULT")
    xdo("mousemove", str(venster.x + 1100), str(venster.y + 950))
    gebied.tag_redraw()
    log(f"WINKEL zijbalk omlaag view2d={regio.view2d.region_to_view(0, 0)} hoogte={regio.height}")


def gewone_naam():
    """Keuring Daan 24 nov (M1): na het snijden heet de romp "mens_A_A_A..." en dat leest in het paneel als een fout.
    Voor w2 krijgt het actieve deel (object en mesh) een gewone naam."""
    o = bpy.context.view_layer.objects.active
    if o is not None:
        o.name = o.data.name = os.environ.get("CJ_WINKEL_NAAM", "Human")
        log(f"WINKEL naam w2 {o.name}")


def ververs():
    _v, gebied, _r = zijbalk()
    if gebied:
        gebied.tag_redraw()


PLAN = [
    ("w1-figuur", lambda: (kies_romp(), labels_alle(), klap_hoofdpaneel(), kijk_figuur())),
    ("-schaal-w2", lambda: schaal(SCHAAL_W2)),  # eigen stap: eerst opnieuw tekenen, anders mist de klik op de kop
    ("w2-uitelkaar", lambda: (klap_hoofdpaneel(), setattr(bpy.context.scene.click_joints, "uit_elkaar", True),
                              kies_romp(), gewone_naam(), kijk_figuur()), zijbalk_omlaag),
    ("-schaal-w3", lambda: schaal(SCHAAL)),
    ("w3-testkaart", testkaart),
]


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.context.preferences.view.ui_scale = SCHAAL
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        S["bouw"]()
        S["rustig"]()
        open_paneel()
        kijk_figuur()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "breed" not in staat:
        staat["breed"] = breder()
        return 1.0
    i = staat["i"]
    if i >= len(PLAN):
        alles = all(p[0] in staat["beelden"] for p in PLAN if not p[0].startswith("-"))
        log(f"WINKEL {'OK' if alles else 'FOUT'} beelden={staat['beelden']} regels={S['staat'].get('regels')}")
        bpy.ops.wm.quit_blender()
        return None
    naam, zet = PLAN[i][:2]
    na = PLAN[i][2] if len(PLAN[i]) > 2 else None
    if staat["fase"] == "zet":
        try:
            zet()
        except Exception as fout:  # noqa: BLE001  een mislukt beeld mag de rest niet tegenhouden
            log(f"WINKEL zet {naam} fout: {fout}")
        ververs()
        staat["fase"] = "teken"
        return 2.0
    if staat["fase"] == "teken":
        if na:
            na()
        ververs()
        staat["fase"] = "schiet"
        return 1.5
    if not naam.startswith("-"):  # een stap met "-" zet alleen iets, zonder beeld
        schiet(naam)
    staat["i"] = i + 1
    staat["fase"] = "zet"
    return 0.3


bpy.app.timers.register(stap, first_interval=3.0)
