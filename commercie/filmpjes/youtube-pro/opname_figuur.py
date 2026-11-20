"""Opname 2 voor Click Joints Pro (Chris, 20 nov 2026, vraag Roep-Maker 19 nov 20:35 NL): "Figure from rig" en
Exploded view op een echte figuur, voor korte staande filmpjes en lange YouTube-video 2.
    CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python commercie/filmpjes/youtube-pro/opname_figuur.py -- <map> <betaalde zip>
Figuur, rig en tekenpop-uiterlijk komen ongewijzigd uit producten/blender-gewrichten/e2e/scherm_mens.py (plaatje 19,
gekeurd door Daan), de filmhulpjes (neem, deel, leeg_beeld) uit film_pro.py. Het script kleurt niets: bogen, groen
en getallen komen van de add-on. Het zet alleen de camera, drukt op de knop Figure from rig, sleept de Bend-schuif
van de rechterknie en zet Exploded view aan, zoals een gebruiker.
Delen: rig (figuur met rig, nog één stuk), knop (na de knop), buig (rechterknie 0 tot 60), uitelkaar (Exploded view
aan, rustig rond). Daarna export naar 3MF (alleen gemeten, niet gefilmd).
Uit: <map>/beelden/b00001.png ... en <map>/film.json. Regels "FIGUUR OK <deel>" eist de workflow."""
import glob
import importlib
import json
import math
import os
import sys

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
film["metingen"] = {}


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


def figuur_zonder_knop():
    """bouw() uit scherm_mens tot vlak voor de knop: figuur gesloten, tekenpop, rig met Limit Rotation."""
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

    # 0 rig: de figuur met zijn rig, nog één stuk, rustig rond
    deel("rig")
    yield from stuk(120, lambda t: cam(-60 + 25 * t))
    neem(30)
    log("FIGUUR OK rig")

    # 1 knop: Figure from rig, rig weg, bogen en kogels staan vanzelf aan
    uitslag = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    regels = [fig.regel(r) for r in lijst]
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = regels
    log(f"FIGUUR knop {uitslag} {len(lijst)} gewrichten regels={regels}")
    yield 1.5
    deel("knop")
    neem(30)
    yield from stuk(120, lambda t: cam(-35 + 10 * math.sin(math.pi * t)))
    neem(30)
    log(f"FIGUUR {'OK' if len(lijst) >= 4 else 'FOUT'} knop gewrichten={len(lijst)}")

    # 2 buig: de Bend-schuif van de rechterknie van 0 tot 60 graden
    delen = {o.get("cj_naam"): o for o in bpy.context.scene.objects
             if o.get("cj_deel") == "B" and o.get("cj_figuur") and o.get("cj_soort") == "SCHARNIER"}
    knie = delen.get("Right knee")
    deel("buig")
    if knie is not None:
        A["actief"](knie)
        wm.cj_scharnier_pose = 0.0
        yield 0.5
        yield from stuk(120, lambda t: setattr(wm, "cj_scharnier_pose", round(60.0 * t, 1)))
        neem(60)
        film["metingen"]["knie_pose"] = round(float(knie.get("cj_pose_graden", 0.0)), 1)
    log(f"FIGUUR {'OK' if knie is not None else 'FOUT'} buig knie={film['metingen'].get('knie_pose')} "
        f"scharnieren={sorted(k for k in delen if k)}")

    # 3 uitelkaar: Exploded view aan, rustig rond
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    los = [o.name for o in bpy.context.scene.objects if o.get("cj_deel") == "B" and o.delta_location.length > 1e-6]
    film["metingen"]["uit_elkaar_delen"] = len(los)
    yield 1.0
    deel("uitelkaar")
    yield from stuk(240, lambda t: cam(-35 + 70 * t, 80.0))
    neem(30)
    log(f"FIGUUR {'OK' if los else 'FOUT'} uitelkaar delen_los={len(los)}")
    deel("eind")

    # export naar 3MF (Exploded view telt niet mee: de export gebruikt de echte plek)
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    try:
        inst.exportmap = exportmap
        inst.formaat = "3MF"
    except Exception as fout:  # noqa: BLE001
        log(f"FIGUUR export instelling: {fout}")
    try:
        for o in bpy.context.view_layer.objects:
            o.select_set(bool(o.get("cj_deel")))
        e = bpy.ops.click_joints.exporteer()
    except Exception as fout:  # noqa: BLE001
        e = f"fout {fout}"
    bestanden = sorted(os.path.basename(p) for p in glob.glob(os.path.join(exportmap, "**", "*.*"), recursive=True))
    film["metingen"]["export"] = {"uitslag": str(e), "bestanden": bestanden}
    log(f"FIGUUR export {e} bestanden={bestanden}")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"FIGUUR klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
