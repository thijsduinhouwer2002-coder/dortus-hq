"""Plaatje 17 (Pro 1.1, Daan punt 1: "de hele figuur in één beeld met zijn bereiken"): hele figuur na "Figure from rig".

Figuur en rig uit toetsen_rig_armen.py (benen 90 mm, romp, armen; linkerelleboog Limit Rotation 0 tot 140).
Na de knop: vier scharnierbogen met getal (knieën, ellebogen) en vier kogelwaaiers (heupen, schouders).
Regel "ARMEN BEELD OK" als vier bogen van een figuur in de passingkleur met getal getekend zijn, de kopregel
hooguit één keer staat, de lijst `from rig` bevat en de samenvatting "8 joints" noemt (voor 4.5: 6 tot 8, zie
toetsen_rig_armen.py).
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
    oud = bpy.app.version < (4, 5, 0)  # bekende losse boolean-fout met alleen Exact (toetsen_rig_armen.py)
    # Run 20: zelfde eis als toetsen_rig_armen.py sinds run 19: in 4.2 minstens 4 van 8 gewrichten (de knieën
    # vallen daar eerlijk af met reden), dus minstens 2 scharnierbogen; in 5.x alle 8.
    genoeg = len(bogen) >= (2 if oud else 4)
    acht = staat.get("samenvatting", "").startswith(tuple(f"{n} joints" for n in range(4, 9)) if oud else "8 joints")
    # Daan 16 nov ±13:50: kogels van een figuur klein en groen met één getal ±N° (moet 1: nooit binnen 40 px van
    # een ander getal), en stap 3 zegt niet "No joint yet" naast de gewrichten (moet 2).
    ft = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur_teken")
    from mathutils import Vector
    kogels = list(ft.laatst.get("getekend", {}).values())
    schaal = bpy.context.preferences.system.ui_scale
    vakken = [k["vak"] for k in kogels if k.get("getal_getekend")]
    for b in bogen:
        if b.get("label_px"):
            vakken_s = ft.vak(Vector(b["label_px"]), b["getal"], int(boog.FIGUUR_PX * schaal))
            vakken.append(vakken_s)
    gaten = [ft.gat(k["vak"], o) for k in kogels for o in vakken if tuple(o) != tuple(k["vak"])]
    min_gat = round(min(gaten), 1) if gaten else None
    kogel_ok = (len(kogels) >= (2 if oud else 4) and all(k["getal"].startswith("\u00b1") for k in kogels)
                and all(k["kleur"] != boog.WIT for k in kogels) and all(k.get("getal_getekend") for k in kogels)
                and (min_gat is None or min_gat >= 40.0 * schaal - 0.5))
    stap3 = bool(act is not None and act.get("cj_passing"))
    log(f"ARMEN KOGELS {'OK' if kogel_ok else 'FOUT'} kogels={[(k['naam'], k['getal'], k['label_px']) for k in kogels]} "
        f"kleinste_gat_px={min_gat} stap3_passing={act.get('cj_passing') if act else None} fout={ft.laatst.get('fout')}")
    ok = genoeg and acht and groen and getal and len(koppen) <= 1 and rig_regel and zichtbaar and ok_uit and kogel_ok and stap3
    log(f"ARMEN BEELD {'OK' if ok else 'FOUT'} samenvatting={staat.get('samenvatting')} bogen={[(b['naam'], b['getal'], b['kijkhoek']) for b in bogen]} "
        f"koppen={len(koppen)} actief={act.name if act else None} zichtbaar={zichtbaar} groen={groen} getal={getal} from_rig={rig_regel} uitsnede={ok_uit} "
        f"fout={boog.laatst.get('fout')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
