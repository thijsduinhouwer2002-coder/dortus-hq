"""Schermen voor gidspagina 3 op dortus.com (beweegbare figuur uit een rig, Pro): het hele Blender-venster met de
zijbalk, zodat de lezer de echte knoppen ziet. Zelfde houten pop en rig als plaatje 19 (scherm_mens.py, MakeHuman
base.obj CC0 1.0), maar met een beeld vóór de knop erbij.
    CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python e2e/scherm_gids_figuur.py -- <map> <betaalde zip>
Plaatjes: f1-voor (pop met rig, vak Figure joints met de knop Figure from rig), f2-na (na de knop: bogen per
gewricht, rechterknie op 60 graden), plus van elk een uitsnede van de zijbalk (-paneel). Regels "GIDS OK <naam>" in
het log; een ontbrekend plaatje geeft "GIDS FOUT" en afsluitcode 1. Alleen voor de site."""
import importlib
import os
import subprocess
import sys

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
_src = open(os.path.join(HIER, "scherm_mens.py"), encoding="utf-8").read()
_src = _src.replace("\nbpy.app.timers.register(stap, first_interval=3.0)\n", "\n")
S = {"__name__": "scherm_mens_gids", "__file__": os.path.join(HIER, "scherm_mens.py")}
exec(compile(_src, "scherm_mens.py", "exec"), S)
M, A, staat = S["M"], S["A"], S["staat"]
from scherm_basis import klap_hoofdpaneel, log, open_paneel, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

fouten = []


def schiet(naam):
    pad = os.path.join(uitmap, naam + ".png")
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    ok = os.path.exists(pad)
    venster, _gebied, regio = zijbalk()
    if ok and regio:
        x = venster.x + regio.x
        y = venster.y + venster.height - (regio.y + regio.height)
        subprocess.run(["convert", pad, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage",
                        os.path.join(uitmap, naam + "-paneel.png")], capture_output=True)
    ok = ok and os.path.exists(os.path.join(uitmap, naam + "-paneel.png"))
    if not ok:
        fouten.append(naam)
    log(f"GIDS {'OK' if ok else 'FOUT'} {naam}")


def voor():
    """Pop en rig zoals bouw() in scherm_mens.py, tot vlak voor de knop."""
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
    S["etalagepop"](ob)
    arm = M["maak_rig"](punten)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    staat["ob"], staat["arm"] = ob.name, arm


def na():
    naam, arm = staat["ob"], staat["arm"]
    A["actief"](bpy.data.objects[naam])
    staat["knop"] = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    staat["regels"] = [fig.regel(r) for r in lijst]
    log(f"GIDS knop {staat['knop']} regels={staat['regels']} samenvatting={fig.samenvatting(lijst)}")
    S["buig"]()


def verloop():
    log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    voor()
    S["rustig"]()
    open_paneel()
    S["kijk"]()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    venster, _gebied, regio = zijbalk()
    if not (regio and regio.active_panel_category == "Click Joints"):
        fouten.append("tabblad")
        log("GIDS FOUT tabblad Click Joints niet actief")
    log(f"GIDS hoofdpaneel ingeklapt: {klap_hoofdpaneel()}")
    yield 2.0
    schiet("f1-voor")
    na()
    yield 2.5
    schiet("f2-na")
    log(f"GIDS KLAAR {len(fouten)} FOUT {fouten}")
    os._exit(1 if fouten else 0)


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None
    except Exception as e:  # noqa: BLE001  een fout in de timer mag Blender niet open laten hangen
        log(f"GIDS FOUT uitzondering {e!r}")
        os._exit(1)


bpy.app.timers.register(stap, first_interval=3.0)
