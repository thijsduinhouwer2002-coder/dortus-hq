"""Plaatjes 11 en 12 (eis 8 van het scharnier, ontwerp betaald v1.1): betaalde build, staaf van 10 mm met een
scharnier, pose 60 (11-scharnier) en voorbij de eindstop met rode vlakken (12-scharnier-rood), hele venster
zoals de winkelschermen 8 en 9. Draait in een eigen stap met de betaalde zip, zodat de gratis schermtest
(schermen.py, plaatjes 1 tot 10) precies gelijk blijft:
    blender --python e2e/scherm_scharnier.py -- <map> <betaalde zip>
Regels "SCHARNIER OK pose" en "SCHARNIER OK rood" zijn wat de workflow eist; de rode pixels tellen we op het
X-scherm (r > 0,7, g en b < 0,3)."""
import importlib
import os
import sys

import bpy
import numpy as np
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
import scherm_basis  # noqa: E402
from scherm_basis import log, schiet, toestand, weergave, zijbalk, zip_pad  # noqa: E402

POSE = 60.0
staat = {}


def _mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


def rode_pixels(naam):
    pad = os.path.join(scherm_basis.uitmap, naam)
    if not os.path.exists(pad):
        return -1, None
    img = bpy.data.images.load(pad)
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    px = px.reshape(-1, 4)
    bpy.data.images.remove(img)
    rood = int(np.count_nonzero((px[:, 0] > 0.7) & (px[:, 1] < 0.3) & (px[:, 2] < 0.3)))
    return rood, (w, h)


def plaats_scharnier():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    staaf = figuren.staaf("staaf", 5.0)
    staaf.color = (0.8, 0.8, 0.8, 1.0)
    figuren.maak_actief(staaf)
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = 0.2, "CURSOR", False, False
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    staat["a"], staat["b"] = a, b
    log(f"SCHARNIER plaats: {uitslag}, A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    weergave()
    venster, gebied, _ = zijbalk()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.show_region_ui = ruimte.show_region_toolbar = ruimte.show_region_header = False
    ov = ruimte.overlay
    ov.show_text = ov.show_cursor = ov.show_axis_x = ov.show_axis_y = ov.show_floor = False
    if a is None:
        return
    rv3d = ruimte.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = Vector(a["cj_scharnier_as"]).normalized().to_track_quat("-Z", "Y")  # langs H: buigvlak
    rv3d.view_distance = 55.0
    rv3d.view_location = Vector(a["cj_scharnier_punt"]) + Vector((0, 0, 4.0))
    gebied.tag_redraw()


def zet(graden):
    a, b = staat.get("a"), staat.get("b")
    if a is None or b is None:
        log("SCHARNIER: geen delen")
        return 0
    beweeg = _mod("betaald.scharnier_beweeg")
    n = beweeg.pose(a, b, graden, _mod("kleur").materiaal("rood"))
    log(f"SCHARNIER pose={graden} rood_vlakken={n}")
    return n


def verslag(naam, graden, rood_vlakken, voorbij):
    rood, maat = rode_pixels(naam)
    a = staat.get("a")
    eisen = {
        "plaatje bestaat": rood >= 0,
        "maat 1920x1080": maat == (1920, 1080),
        "pose klopt": bool(a) and abs(staat["b"].get("cj_pose_graden", -1) - graden) < 1e-6,
        "voorbij de stop klopt": bool(a) and (graden > a["cj_bereik_graden"]) == voorbij,
        "rode vlakken alleen voorbij": (rood_vlakken > 0) == voorbij,
        "rode pixels": rood >= 500 if voorbij else rood < 50,
    }
    mis = [k for k, ok in eisen.items() if not ok]
    log(f"SCHARNIER {'OK' if not mis else 'FOUT'} {'rood' if voorbij else 'pose'} {naam} maat={maat} "
        f"rode_pixels={rood} rode_vlakken={rood_vlakken} pose={graden} "
        f"bereik={a.get('cj_bereik_graden') if a else None} mis={mis}")


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        plaats_scharnier()
        staat["rood11"] = zet(POSE)
        return 2.0
    if n == 3:
        schiet("11-scharnier.png")
        verslag("11-scharnier-x.png", POSE, staat["rood11"], voorbij=False)
        a = staat.get("a")
        staat["voorbij"] = round(float(a["cj_bereik_graden"]) + 8.0, 1) if a else 0.0
        staat["rood12"] = zet(staat["voorbij"])
        return 2.0
    if n == 4:
        schiet("12-scharnier-rood.png")
        verslag("12-scharnier-rood-x.png", staat["voorbij"], staat["rood12"], voorbij=True)
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
