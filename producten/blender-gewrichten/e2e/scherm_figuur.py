"""Plaatje 15 (Pro 1.1 stap 1, voor Daan): het vak "Figure joints" met de zes presets en de lijst per figuur.

Staaf van 6 mm, Knee (scharnier 135) en Shoulder (kogel) via de presets, zijbalk op het tabblad Click Joints,
hele venster plus een uitsnede van de zijbalk. Regel "FIGUUR OK" als beide gewrichten in de lijst staan en de
iconen een icon_id hebben (met venster horen ze geladen te zijn).
    blender --python e2e/scherm_figuur.py -- <map> <betaalde zip>
"""
import importlib
import os
import subprocess
import sys

import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
from scherm_basis import log, open_paneel, schiet, toestand, uitmap, weergave, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

staat = {}


def cursor(x):
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):
        m.col[i][:3] = v
    m.col[3][:3] = (x, 0.013, 0.021)
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m


def bouw():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", True, True
    staaf = figuren.staaf("figure", 6.0, lengte=90.0)
    figuren.maak_actief(staaf)
    cursor(-20.0)
    r1 = bpy.ops.click_joints.plaats_preset(deel="KNEE")
    b = bpy.data.objects.get("figure_B")
    figuren.maak_actief(b)
    cursor(20.0)
    r2 = bpy.ops.click_joints.plaats_preset(deel="SHOULDER")
    log(f"FIGUUR plaats {r1} {r2}")
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    staat["lijst"] = fig.figuur_gewrichten(bpy.context.scene.objects, "figure")
    staat["iconen"] = [fig.icoon(p[0]) for p in fig.PRESETS]
    staat["regels"] = [fig.regel(r) for r in staat["lijst"]]


def uitsnede():
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, "15-figuur-x.png")
    doel = os.path.join(uitmap, "15-figuur-paneel.png")
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
        weergave()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "geschoten" not in staat:
        staat["geschoten"] = True
        for o in bpy.context.view_layer.objects:
            o.select_set(False)
        a = next((o for o in bpy.context.scene.objects if o.get("cj_naam") == "Shoulder"), None)
        if a:
            a.select_set(True)
            bpy.context.view_layer.objects.active = a
        # Hoofdpaneel inklappen? Nee: de koper ziet het zo. Wel de zijbalk omlaag scrollen tot het vak in beeld is.
        venster, gebied, regio = zijbalk()
        if regio:
            x = venster.x + regio.x + regio.width // 2
            y = venster.y + venster.height - (regio.y + regio.height // 2)
            subprocess.run(["xdotool", "mousemove", str(x), str(y)])
            for _ in range(25):
                subprocess.run(["xdotool", "click", "5"])
        return 1.5
    schiet("15-figuur.png")
    ok_uit = uitsnede()
    namen = [r["naam"] for r in staat.get("lijst", [])]
    ok = namen == ["Knee", "Shoulder"] and all(i > 0 for i in staat.get("iconen", [0])) and ok_uit
    log(f"FIGUUR {'OK' if ok else 'FOUT'} namen={namen} iconen={staat.get('iconen')} uitsnede={ok_uit} "
        f"regels={staat.get('regels')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
