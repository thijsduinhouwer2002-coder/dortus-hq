"""Opname 3 voor Click Joints Pro (20 nov 2026, opdracht hoofdchat 14:45 NL): lange YouTube-uitleg
"Rig to printable figure in Blender" en twee staande filmpjes, uit één opname in de echte Blender 5.3.0 met de
betaalde add-on 1.1.0.
    CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python commercie/filmpjes/youtube-pro-3/opname.py -- <map> <betaalde zip>
Bouwt voort op commercie/filmpjes/youtube-pro/opname_figuur.py (Chris): dezelfde figuur (MakeHuman base.obj, CC0, met
de rig uit e2e/proef_mens.py, linkerknie 120 en linkerelleboog 140 in Limit Rotation) en dezelfde filmhulpjes.
Het script kleurt niets: bogen, getallen, rood en de lijst komen van de add-on. Het zet alleen de camera, klapt
panelen in en uit met een klik, drukt op Figure from rig, zet de Bend-schuif van de rechterknie en zet Exploded view
aan en exporteert, zoals een gebruiker.
Delen (eerste beeld per deel in film.json):
  rig       figuur met rig, nog één stuk; paneel Figure joints met de knop in beeld
  druk      vlak voor de knop: stil, dan de knop
  lijst     na de knop: stil, de lijst met gewrichten in het paneel
  bogen     rustig rond met de bogen en getallen
  buig      Bend van de rechterknie 0 tot 120 (de stop)
  rood      120 tot 132: voorbij de stop wordt het rood
  terug     terug naar 60
  uitelkaar Exploded view aan, rustig rond
  export    paneel 3 Fit and export, 3MF, Export
Regels "LANG OK <deel>" eist de workflow."""
import glob
import importlib
import json
import math
import os
import subprocess
import sys
import time

import bpy
from mathutils import Euler

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
from scherm_basis import klap_hoofdpaneel, xdo  # noqa: E402
film["metingen"] = {}
STOP_VOORBIJ = 12.0   # graden voorbij de stop in deel rood


def cam(draai, kantel=82.0, afstand=335.0, midx=-12.0, midz=110.0):
    _, gebied, _ = zijbalk()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "ORTHO"
    rv.view_rotation = Euler((math.radians(kantel), 0.0, math.radians(draai)), "XYZ").to_quaternion()
    rv.view_location = (midx, 0.0, midz)
    rv.view_distance = afstand
    gebied.tag_redraw()


def stuk(stappen, doe):
    for i in range(stappen):
        doe(zacht(i / max(1, stappen - 1)))
        yield 0.05
        neem()


def zijbalk_rect():
    venster, _gebied, regio = zijbalk()
    if not regio:
        return None
    return [venster.x + regio.x, venster.y + venster.height - (regio.y + regio.height), regio.width, regio.height]


def klik_kop(y_boven):
    """Klik op een paneelkop in de zijbalk (y in px vanaf de bovenrand van de zijbalk), zoals een gebruiker."""
    venster, gebied, regio = zijbalk()
    if not regio:
        return False
    x = venster.x + regio.x + 60
    y = venster.y + venster.height - (regio.y + regio.height) + y_boven
    xdo("mousemove", str(x), str(y))
    time.sleep(0.2)
    xdo("click", "1")
    time.sleep(0.2)
    xdo("mousemove", "5", "600")   # muis uit de zijbalk, geen oplichtende knop
    gebied.tag_redraw()
    return True


def wiel(knop, keer):
    """Muiswiel boven de zijbalk (4 = omhoog, 5 = omlaag), zoals een gebruiker scrolt."""
    venster, gebied, regio = zijbalk()
    if not regio:
        return
    x = venster.x + regio.x + regio.width // 2
    y = venster.y + venster.height - (regio.y + regio.height // 2)
    xdo("mousemove", str(x), str(y))
    time.sleep(0.1)
    for _ in range(keer):
        xdo("click", knop)
        time.sleep(0.05)
    try:  # tweede weg, als het wiel onder Xvfb niets doet
        with bpy.context.temp_override(window=venster, area=gebied, region=regio):
            for _ in range(keer):
                if knop == "5":
                    bpy.ops.view2d.scroll_down(deltax=0, deltay=40)
                else:
                    bpy.ops.view2d.scroll_up(deltax=0, deltay=40)
    except Exception as fout:  # noqa: BLE001
        log(f"LANG scroll via view2d: {fout}")
    xdo("mousemove", "5", "600")
    gebied.tag_redraw()


def figuur_zonder_knop():
    """Zoals opname_figuur.py: figuur gesloten, tekenpop, rig met Limit Rotation, nog niet op de knop gedrukt."""
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
    arm = M["maak_rig"](punten)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    return ob, arm


def verloop():
    wm = bpy.context.window_manager
    log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    ob, arm = figuur_zonder_knop()
    naam = ob.name
    SM["rustig"]()
    leeg_beeld()
    SM["open_paneel"]()
    cam(-35)
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    yield 0.5
    # hoofdpaneel Click Joints dicht: paneel Figure joints met de knop staat dan bovenaan (zoals plaatje 19)
    log(f"LANG hoofdpaneel dicht: {klap_hoofdpaneel()}")
    xdo("mousemove", "5", "600")
    yield 1.0
    film["zijbalk"] = zijbalk_rect()
    log(f"LANG zijbalk {film['zijbalk']}")

    # rig: de figuur met zijn rig, nog één stuk, rustig rond
    deel("rig")
    yield from stuk(180, lambda t: cam(-70 + 35 * t))
    log("LANG OK rig")

    # druk: stil met de knop in beeld, dan de knop
    deel("druk")
    neem(45)
    uitslag = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    regels = [fig.regel(r) for r in lijst]
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = regels
    film["metingen"]["samenvatting"] = fig.samenvatting(lijst)
    log(f"LANG knop {uitslag} {len(lijst)} gewrichten regels={regels}")
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    # actief blijft een deel van de figuur, zodat het paneel de lijst toont
    delen_fig = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH"]
    if delen_fig:
        bpy.context.view_layer.objects.active = max(delen_fig, key=lambda o: len(o.data.vertices))
    yield 1.5
    log(f"LANG {'OK' if len(lijst) >= 4 else 'FOUT'} druk gewrichten={len(lijst)}")

    # lijst: stil, zodat de lijst te lezen is
    deel("lijst")
    neem(240)
    log("LANG OK lijst")

    # bogen: rustig rond met bogen en getallen
    deel("bogen")
    yield from stuk(300, lambda t: cam(-35 + 22 * math.sin(2 * math.pi * t)))
    log("LANG OK bogen")

    # buig: rechterknie kiezen, hoofdpaneel open en naar het blok Hinge met de Bend-schuif scrollen
    delen = {o.get("cj_naam"): o for o in bpy.context.scene.objects
             if o.get("cj_deel") == "B" and o.get("cj_figuur") and o.get("cj_soort") == "SCHARNIER"}
    knie = delen.get("Right knee")
    if knie is None:
        log("LANG FOUT buig: geen rechterknie")
        bpy.ops.wm.quit_blender()
        return
    A["actief"](knie)
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    wm.cj_scharnier_pose = 0.0
    a_knie = next((o for o in bpy.context.scene.objects if o.get("cj_soort") == "SCHARNIER"
                   and o.get("cj_deel") == "A" and o.get("cj_naam") == "Right knee"), None)
    stop = float(a_knie["cj_bereik_graden"]) if a_knie is not None else 120.0
    film["metingen"]["knie_stop"] = stop
    klik_kop(12)      # hoofdpaneel weer open
    yield 1.0
    wiel("5", 25)     # omlaag naar Hinge
    yield 1.0
    cam(-35, 82.0, 260.0, -12.0, 80.0)
    yield 0.5
    deel("buig")
    neem(20)
    yield from stuk(150, lambda t: setattr(wm, "cj_scharnier_pose", round(math.floor(stop * 10) / 10 * t, 1)))
    neem(60)
    film["metingen"]["knie_pose_stop"] = round(float(knie.get("cj_pose_graden", 0.0)), 1)
    log(f"LANG OK buig knie={film['metingen']['knie_pose_stop']} stop={stop}")

    # rood: voorbij de stop
    deel("rood")
    rood = [0]

    def voorbij(t):
        wm.cj_scharnier_pose = round(stop + STOP_VOORBIJ * t, 1)
        rood[0] = len(a_knie.get("cj_rood_vlakken", [])) // 2 if a_knie is not None else 0
    yield from stuk(45, voorbij)
    neem(105)
    film["metingen"]["knie_pose_rood"] = round(float(knie.get("cj_pose_graden", 0.0)), 1)
    film["metingen"]["rood_vlakken"] = rood[0]
    log(f"LANG {'OK' if rood[0] > 0 else 'FOUT'} rood pose={film['metingen']['knie_pose_rood']} rood_vlakken={rood[0]}")

    # terug: terug naar 60
    deel("terug")
    yield from stuk(60, lambda t: setattr(wm, "cj_scharnier_pose", round(stop + STOP_VOORBIJ - (stop + STOP_VOORBIJ - 60) * t, 1)))
    neem(45)
    rood_na = len(a_knie.get("cj_rood_vlakken", [])) // 2 if a_knie is not None else -1
    film["metingen"]["rood_na_terug"] = rood_na
    log(f"LANG OK terug rood_na={rood_na}")

    # uitelkaar: Exploded view aan, paneel terug naar boven, rustig rond
    wiel("4", 30)
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    los = [o.name for o in bpy.context.scene.objects if o.get("cj_deel") == "B" and o.delta_location.length > 1e-6]
    film["metingen"]["uit_elkaar_delen"] = len(los)
    yield 1.0
    deel("uitelkaar")
    yield from stuk(360, lambda t: cam(-35 + 80 * t, 80.0))
    log(f"LANG {'OK' if los else 'FOUT'} uitelkaar delen_los={len(los)}")

    # export: 3MF kiezen, alle delen kiezen, Export (de melding staat onderin de statusbalk)
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    try:
        inst.exportmap = exportmap
        inst.formaat = "3MF"
    except Exception as fout:  # noqa: BLE001
        log(f"LANG export instelling: {fout}")
    cam(10, 80.0)
    yield 1.0
    deel("export")
    neem(45)
    try:
        for o in bpy.context.view_layer.objects:
            o.select_set(bool(o.get("cj_deel")))
        e = bpy.ops.click_joints.exporteer()
    except Exception as fout:  # noqa: BLE001
        e = f"fout {fout}"
    yield 1.0
    neem(150)
    bestanden = sorted(os.path.basename(p) for p in glob.glob(os.path.join(exportmap, "**", "*.*"), recursive=True))
    film["metingen"]["export"] = {"uitslag": str(e), "bestanden": bestanden}
    log(f"LANG {'OK' if bestanden else 'FOUT'} export {e} bestanden={bestanden}")
    deel("eind")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"LANG klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
