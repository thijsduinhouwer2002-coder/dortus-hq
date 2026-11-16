"""Plaatje 17 (Pro 1.1, Daan punt 1: "de hele figuur in één beeld met zijn bereiken"): hele figuur na "Figure from rig".

Figuur en rig uit toetsen_rig_armen.py (benen 90 mm, romp, armen; linkerelleboog Limit Rotation 0 tot 140).
Na de knop: vier scharnierbogen met getal (knieën, ellebogen) en vier kogelwaaiers (heupen, schouders).
Regel "ARMEN BEELD OK" als vier bogen van een figuur in de passingkleur met getal getekend zijn, de kopregel
hooguit één keer staat, de lijst `from rig` bevat en de samenvatting "8 joints" noemt.
    blender --python e2e/scherm_rig_armen.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import toetsen_rig_armen as tr  # noqa: E402
from scherm_basis import log, open_paneel, schiet, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

staat = {}


def bouw():
    mesh, arm = tr.figuur(90.0)
    arm.data.display_type = "STICK"
    staat["knop"] = bpy.ops.click_joints.figuur_uit_rig()
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    staat["lijst"] = fig.figuur_gewrichten(bpy.context.scene.objects, "held")
    staat["regels"] = [fig.regel(r) for r in staat["lijst"]]
    staat["samenvatting"] = fig.samenvatting(staat["lijst"])
    log(f"ARMEN knop {staat['knop']} regels={staat['regels']} samenvatting={staat['samenvatting']}")


def kijk():
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    rv = ruimte.region_3d
    rv.view_perspective = "ORTHO"
    # Schuin van voren: de knieas ligt langs X (waaier zichtbaar van opzij), de elleboogas niet (zichtbaar van voren).
    rv.view_rotation = Euler((math.radians(78), 0.0, math.radians(-38)), "XYZ").to_quaternion()
    rv.view_location = (0.0, 0.0, 80.0)
    rv.view_distance = 270.0


def uitsnede():
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, "17-figuur-heel-x.png")
    doel = os.path.join(uitmap, "17-figuur-heel-paneel.png")
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(doel)


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        bouw()
        open_paneel()
        kijk()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
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
    schiet("17-figuur-heel.png")
    ok_uit = uitsnede()
    boog = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_boog")
    bogen = [b for b in boog.laatst.get("bogen", []) if b.get("figuur")]
    koppen = [b for b in boog.laatst.get("bogen", []) if b.get("kop")]
    groen = all(b.get("kleur") != boog.WIT for b in bogen)
    getal = all(b.get("getal_getekend") for b in bogen)
    rig_regel = any("from rig" in r for r in staat.get("regels", []))
    act = bpy.context.view_layer.objects.active
    zichtbaar = act is not None and act.visible_get() and bool(act.get("cj_deel"))
    genoeg = len(bogen) >= 4
    acht = staat.get("samenvatting", "").startswith("8 joints")
    ok = genoeg and acht and groen and getal and len(koppen) <= 1 and rig_regel and zichtbaar and ok_uit
    log(f"ARMEN BEELD {'OK' if ok else 'FOUT'} samenvatting={staat.get('samenvatting')} bogen={[(b['naam'], b['getal'], b['kijkhoek']) for b in bogen]} "
        f"koppen={len(koppen)} actief={act.name if act else None} zichtbaar={zichtbaar} groen={groen} getal={getal} from_rig={rig_regel} uitsnede={ok_uit} "
        f"fout={boog.laatst.get('fout')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
