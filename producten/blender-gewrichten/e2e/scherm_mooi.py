"""Mooier overlay (23 nov 2026): voor- en na-beelden van Pro op de MakeHuman-figuur na Figure from rig.

Zelfde figuur, rig en kijkhoek als plaatje 19 (scherm_mens.py, die we hier inladen zonder zijn eigen volgorde).
Vijf beelden, hele venster 1920x1080, alleen echte uitkomst van de add-on:
  m1-heel        hele figuur, rechterknie gekozen en 60 graden gebogen (zoals een koper net klikte)
  m2-schoon      hele figuur, niets gekozen (het beeld voor een filmpje)
  m3-knie        rechterknie dichtbij van opzij, 60 graden
  m4-rood        rechterknie dichtbij, 12 graden voorbij de stop
  m5-uitelkaar   hele figuur in Exploded view, knie gekozen
  m6-paneel      uitsnede van de zijbalk bij m4
  m7-paneel      uitsnede van de zijbalk met het hoofdpaneel ingeklapt (Figure joints met de lijst)
Per beeld een regel "MOOI beeld <naam> getallen=<n> ..." (hoeveel getallen er getekend zijn) en aan het eind
"MOOI OK" als alle beelden er zijn. Werkt op de oude en de nieuwe code (voor/na in pro-mooier.yml).
    CJ_MENS_OBJ=<base.obj> blender --python e2e/scherm_mooi.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
_src = open(os.path.join(HIER, "scherm_mens.py"), encoding="utf-8").read()
_START = "\nbpy.app.timers.register(stap, first_interval=3.0)\n"
assert _src.count(_START) == 1, "scherm_mens.py: de regel die de eigen volgorde start is veranderd"
_src = _src.replace(_START, "\n")
S = {"__name__": "scherm_mens_lib", "__file__": os.path.join(HIER, "scherm_mens.py")}
exec(compile(_src, "scherm_mens.py", "exec"), S)
from scherm_basis import klap_hoofdpaneel, log, open_paneel, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

KNIE = os.environ.get("CJ_MOOI_KNIE", "Right knee")
staat = {"beelden": [], "getallen": []}


def _mod(naam):
    return importlib.import_module(f"bl_ext.user_default.click_joints.{naam}")


def knie_b():
    for o in bpy.context.scene.objects:
        if o.get("cj_deel") == "B" and o.get("cj_soort") == "SCHARNIER" and o.get("cj_naam") == KNIE:
            return o
    return None


def niets_gekozen():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None


def kies_knie():
    b = knie_b()
    if b is not None:
        S["A"]["actief"](b)
    return b


def pose(graden):
    b = kies_knie()
    if b is None:
        return None
    bpy.context.window_manager.cj_scharnier_pose = float(graden)
    return b


def kijk_heel():
    S["kijk"]()


def kijk_knie():
    b = knie_b()
    _v, gebied, _r = zijbalk()
    rv = gebied.spaces.active.region_3d
    p = Vector(b["cj_scharnier_punt"]) if b is not None else Vector((0, 0, 60))
    # Van rechts (de knieas ligt langs X, de rechterknie aan de kant -X), iets van voren.
    rv.view_rotation = Euler((math.radians(84), 0.0, math.radians(-65)), "XYZ").to_quaternion()
    rv.view_location = (p.x, p.y, p.z)
    rv.view_distance = float(os.environ.get("CJ_MOOI_KNIE_AFSTAND", "150"))


def getallen():
    """Hoeveel getallen en koppen er in de laatste tekenbeurt stonden (scharnierbogen en figuurkogels)."""
    sb = _mod("betaald.scharnier_boog")
    ft = _mod("betaald.figuur_teken")
    bogen = sb.laatst.get("bogen", [])
    n_s = sum(1 for b in bogen if b.get("getal_getekend"))
    n_k = sum(1 for k in ft.laatst.get("getekend", {}).values() if k.get("getal_getekend"))
    koppen = [b.get("kop") for b in bogen if b.get("kop")]
    rood = [b.get("voorbij_tekst") for b in bogen if b.get("voorbij_tekst")]
    return n_s + n_k, n_s, n_k, koppen, rood


def rood_vlakken():
    tel = 0
    for o in bpy.context.scene.objects:
        tel += len(o.get("cj_rood_vlakken", [])) // 2 + len(o.get("cj_rood_deel", [])) // 2
    return tel


def schiet(naam):
    pad = os.path.join(uitmap, f"{naam}.png")
    r = subprocess.run(["import", "-window", "root", pad], capture_output=True, text=True)
    n, n_s, n_k, koppen, rood = getallen()
    log(f"MOOI beeld {naam} getallen={n} scharnier={n_s} kogel={n_k} koppen={koppen} rood_tekst={rood} "
        f"rode_vlakken={rood_vlakken()} bestand={os.path.exists(pad)} {r.stderr.strip()}")
    if os.path.exists(pad):
        staat["beelden"].append(naam)
    staat["getallen"].append(n)
    teksten = [b.get("label_tekst") for b in _mod("betaald.scharnier_boog").laatst.get("bogen", [])
               if b.get("getal_getekend") and b.get("label_tekst")]
    staat.setdefault("per_beeld", {})[naam] = {"n": n, "koppen": koppen, "teksten": teksten, "rood": rood_vlakken()}
    return pad


def selected_ok():
    """Moet 1 keuring 23 nov: de standaardstand Labels: Selected, zoals een koper hem als eerste ziet.
    m1 en m3: precies 1 label, met de naam van het gekozen gewricht, geen kopregel. m2 (niets gekozen): 0 labels.
    m4 (voorbij de stop): het hele deel rood, dus veel meer dan een strook (voor: 17 vlakken)."""
    pb = staat.get("per_beeld", {})
    fout = []
    for nm in ("m1-heel", "m3-knie"):
        b = pb.get(nm, {})
        if b.get("n") != 1 or b.get("koppen") or not any(KNIE in t for t in b.get("teksten", [])):
            fout.append(f"{nm}={b}")
    if pb.get("m2-schoon", {}).get("n") != 0:
        fout.append(f"m2-schoon={pb.get('m2-schoon')}")
    if pb.get("m4-rood", {}).get("rood", 0) < 200:
        fout.append(f"m4-rood={pb.get('m4-rood')}")
    return not fout, fout


def uitsnede(bron, doel):
    venster, _gebied, regio = zijbalk()
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    ok = r.returncode == 0 and os.path.exists(doel)
    if ok:
        staat["beelden"].append(os.path.basename(doel)[:-4])
    return ok


def ververs():
    ft = _mod("betaald.figuur_teken")
    ft.laatst.clear()
    _v, gebied, _r = zijbalk()
    if gebied:
        gebied.tag_redraw()


# Elke stap zet iets klaar en geeft Blender een tel om te tekenen; de volgende stap schiet het beeld.
PLAN = [
    ("m1-heel", lambda: (pose(60.0), kijk_heel())),
    ("m2-schoon", lambda: (niets_gekozen(), kijk_heel())),
    ("m3-knie", lambda: (pose(60.0), kijk_knie())),
    ("m4-rood", lambda: (pose(float(_mod("betaald.scharnier_boog").grens(_paar_a())) + 12.0), kijk_knie())),
    ("m5-uitelkaar", lambda: (pose(0.0), setattr(bpy.context.scene.click_joints, "uit_elkaar", True), kies_knie(),
                              kijk_heel())),
]


def _paar_a():
    a, _b = _mod("betaald.scharnier_boog").paar(bpy.context.scene, knie_b())
    return a


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        S["bouw"]()
        S["rustig"]()
        open_paneel()
        kijk_heel()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "klaar_tab" not in staat:
        staat["klaar_tab"] = True
        staat["i"] = 0
        staat["fase"] = "zet"
        return 0.5
    i = staat["i"]
    if i == len(PLAN) and staat["fase"] == "zet":  # hoofdpaneel inklappen, zodat Figure joints in beeld staat
        log(f"MOOI hoofdpaneel ingeklapt: {klap_hoofdpaneel()}")
        staat["fase"] = "paneel"
        return 1.5
    if i == len(PLAN) and staat["fase"] == "paneel":
        pad = schiet("m7-heel-paneel")
        staat["ok_p7"] = uitsnede(pad, os.path.join(uitmap, "m7-paneel.png"))
        staat["i"] = i + 1
        return 0.3
    if i > len(PLAN):
        ok_p = uitsnede(os.path.join(uitmap, "m4-rood.png"), os.path.join(uitmap, "m6-paneel.png"))
        # Kan-punt auto-keurder: ergens moet een getal staan, anders bewijzen de beelden niets.
        alles = (all(os.path.exists(os.path.join(uitmap, f"{p[0]}.png")) for p in PLAN) and ok_p
                 and staat.get("ok_p7") and sum(staat["getallen"]) > 0)
        log(f"MOOI {'OK' if alles else 'FOUT'} beelden={staat['beelden']} fout_boog={_mod('betaald.scharnier_boog').laatst.get('fout')} "
            f"fout_kogel={_mod('betaald.figuur_teken').laatst.get('fout')}")
        sok, sfout = selected_ok()
        log(f"MOOI SELECTED {'OK' if sok else 'FOUT'} stand={getattr(bpy.context.window_manager, 'cj_labels', None)} {sfout}")
        bpy.ops.wm.quit_blender()
        return None
    naam, zet = PLAN[i]
    if staat["fase"] == "zet":
        try:
            zet()
        except Exception as fout:  # noqa: BLE001  een mislukt beeld mag de rest niet tegenhouden
            log(f"MOOI zet {naam} fout: {fout}")
        ververs()
        staat["fase"] = "teken"
        return 1.5
    if staat["fase"] == "teken":  # nog een tekenbeurt: de plekken van de getallen worden in de eerste berekend
        ververs()
        staat["fase"] = "schiet"
        return 1.0
    schiet(naam)
    staat["i"] = i + 1
    staat["fase"] = "zet"
    return 0.3


bpy.app.timers.register(stap, first_interval=3.0)
