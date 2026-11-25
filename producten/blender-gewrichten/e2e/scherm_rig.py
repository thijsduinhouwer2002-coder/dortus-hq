"""Plaatje 16 (Pro 1.1 stap 2, Daan punt 1 en 2): de figuur na "Figure from rig" met een boog per gewricht.

Figuur en rig uit toetsen_rig.py (twee benen, knie links met Limit Rotation 0 tot 120 graden, rechts zonder).
Na de knop staan de bogen vanzelf aan (rig.py). Kijkrichting schuin van voren, zodat beide knieën een waaier
met getal tonen. Hele venster plus een uitsnede van de zijbalk (de lijst met `from rig` en, sinds spiegelen, `mirrored` op de rechterknie).
Regel "RIG BEELD OK" als minstens één boog van een figuur in de passingkleur met getal getekend is, de kopregel
hooguit één keer staat, en de lijst `from rig` bevat. Twee bogen in alle versies (ook 4.2, sinds de herkansing
met verschoven snijvlak).
    blender --python e2e/scherm_rig.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import toetsen_rig as tr  # noqa: E402
from scherm_basis import log, open_paneel, schiet, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

staat = {}


def bouw():
    tr.leeg()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    mesh = tr.figuur()
    arm = tr.rig(mesh)
    arm.data.display_type = "STICK"
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    mesh.select_set(True)
    bpy.context.view_layer.objects.active = mesh
    staat["mesh"] = mesh


def bouw_figuur():
    staat["knop"] = bpy.ops.click_joints.figuur_uit_rig()
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    staat["lijst"] = fig.figuur_gewrichten(bpy.context.scene.objects, "pop")
    staat["regels"] = [fig.regel(r) for r in staat["lijst"]]
    staat["samenvatting"] = fig.samenvatting(staat["lijst"])
    log(f"RIG knop {staat['knop']} regels={staat['regels']} samenvatting={staat['samenvatting']}")


def kijk():
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    rv = ruimte.region_3d
    rv.view_perspective = "ORTHO"
    # Schuin van voren en wat van opzij: de knieas ligt langs X, dus recht van voren zie je de waaier op zijn kant.
    rv.view_rotation = Euler((math.radians(80), 0.0, math.radians(-55)), "XYZ").to_quaternion()
    rv.view_location = (0.0, 0.0, 34.0)
    rv.view_distance = 115.0


def uitsnede(naam="16-figuur-rig"):
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, f"{naam}-x.png")
    doel = os.path.join(uitmap, f"{naam}-paneel.png")
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(doel)


def alle_labels():
    """Mooier overlay (23 nov): Pro toont bij een figuur standaard alleen het gekozen gewricht (Labels: Selected).
    Dit plaatje toetst de plek van alle getallen, dus hier de stand All. Oude code zonder schakelaar: niets doen."""
    wm = bpy.context.window_manager
    if hasattr(wm, "cj_labels"):
        wm.cj_labels = "ALL"


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        alle_labels()
        bouw()  # alleen figuur en rig; Figure from rig pas na het schermbeeld 16a
        open_paneel()
        kijk()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "boven" not in staat:  # 1.2.9 (issue 70): eerst het paneel vóór Figure from rig, met het vak Rig found bovenaan
        staat["boven"] = True
        zijbalk()[1].tag_redraw()
        return 1.0
    if "boven_geschoten" not in staat:
        staat["boven_geschoten"] = True
        schiet("16a-rig-boven.png")
        ok_boven = uitsnede("16a-rig-boven")
        rig = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
        arm = rig.zoek_armature(staat["mesh"])
        log(f"RIG BOVEN {'OK' if arm is not None and ok_boven else 'FOUT'} rig={arm.name if arm else None} uitsnede={ok_boven}")
        bouw_figuur()
        return 1.0
    if "geschoten" not in staat:
        staat["geschoten"] = True
        venster, gebied, regio = zijbalk()
        if regio:  # zijbalk omlaag tot het vak Figure joints met de lijst in beeld is
            x = venster.x + regio.x + regio.width // 2
            y = venster.y + venster.height - (regio.y + regio.height // 2)
            subprocess.run(["xdotool", "mousemove", str(x), str(y)])
            for _ in range(25):
                subprocess.run(["xdotool", "click", "5"])
        gebied.tag_redraw()
        return 1.5
    schiet("16-figuur-rig.png")
    ok_uit = uitsnede()
    boog = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_boog")
    bogen = [b for b in boog.laatst.get("bogen", []) if b.get("figuur")]
    koppen = [b for b in boog.laatst.get("bogen", []) if b.get("kop")]
    groen = all(b.get("kleur") != boog.WIT for b in bogen)
    getal = all(b.get("getal_getekend") for b in bogen)
    rig_regel = any("from rig" in r for r in staat.get("regels", []))
    act = bpy.context.view_layer.objects.active
    zichtbaar = act is not None and act.visible_get() and bool(act.get("cj_deel"))
    # BEKEND 4.2 (alleen Exact-solver): de gespiegelde rechterknie (120) mislukt soms; plan punt 3, status.md.
    genoeg = len(bogen) >= (1 if bpy.app.version < (4, 5, 0) else 2)
    ok = genoeg and groen and getal and len(koppen) <= 1 and rig_regel and zichtbaar and ok_uit
    log(f"RIG BEELD {'OK' if ok else 'FOUT'} bogen={[(b['naam'], b['getal'], b['kijkhoek']) for b in bogen]} "
        f"koppen={len(koppen)} actief={act.name if act else None} zichtbaar={zichtbaar} groen={groen} getal={getal} from_rig={rig_regel} uitsnede={ok_uit} "
        f"fout={boog.laatst.get('fout')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
