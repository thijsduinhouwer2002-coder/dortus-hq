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


def zijbalk_omlaag():
    """w2: stap 3 met Export STL/3MF staat bij 1,5x onder de rand van het scherm (eigen keuring 24 nov). Het paneel
    is hier langer dan de zijbalk, dus scrollen met het wiel boven de zijbalk werkt (bij plaatje 19 paste alles en
    deed het wiel niets). Daarna nog view2d.scroll_down als vangnet; de log zegt hoe ver het kwam."""
    venster, gebied, regio = zijbalk()
    if not regio:
        return
    x = venster.x + regio.x + regio.width // 2
    y = venster.y + venster.height - (regio.y + regio.height // 2)
    xdo("mousemove", str(x), str(y))
    time.sleep(0.2)
    for _ in range(int(os.environ.get("CJ_WINKEL_WIEL", "25"))):
        xdo("click", "5")
        time.sleep(0.03)
    try:
        with bpy.context.temp_override(window=bpy.context.window_manager.windows[0], area=gebied, region=regio):
            bpy.ops.view2d.scroll_down(deltay=2000)
    except Exception as fout:  # noqa: BLE001
        log(f"WINKEL scroll_down fout: {fout}")
    gebied.tag_redraw()
    log(f"WINKEL zijbalk omlaag view2d={getattr(regio, 'view2d', None) and regio.view2d.region_to_view(0, 0)}")


def ververs():
    _v, gebied, _r = zijbalk()
    if gebied:
        gebied.tag_redraw()


PLAN = [
    ("w1-figuur", lambda: (kies_romp(), labels_alle(), klap_hoofdpaneel(), kijk_figuur())),
    ("w2-uitelkaar", lambda: (klap_hoofdpaneel(), setattr(bpy.context.scene.click_joints, "uit_elkaar", True),
                              kies_romp(), kijk_figuur()), zijbalk_omlaag),
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
        alles = all(p[0] in staat["beelden"] for p in PLAN)
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
    schiet(naam)
    staat["i"] = i + 1
    staat["fase"] = "zet"
    return 0.3


bpy.app.timers.register(stap, first_interval=3.0)
