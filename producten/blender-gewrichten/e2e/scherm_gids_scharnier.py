"""Schermen voor gidspagina 2 op dortus.com (scharnier met eindstop, Pro): het hele Blender-venster met de
zijbalk (tab Click Joints), zodat de lezer de echte knoppen ziet. Houten been uit scherm_pro.py, zoals de film.
    blender --gpu-backend opengl start.blend --python e2e/scherm_gids_scharnier.py -- <map> <betaalde zip>
Plaatjes: g1-voor (been heel, knoppen "Place hinge, bends up to:"), g2-pose (scharnier op 60 graden, vak Hinge
met de Bend-schuif, boog aan), g3-voorbij (3 graden voorbij de stop, rood). Regels "GIDS OK <naam>" in het log.
Alleen voor de site; de winkel- en e2e-plaatjes blijven ongemoeid."""
import math
import os
import subprocess
import sys

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
import scherm_basis  # noqa: E402
import scherm_pro as sp  # noqa: E402
from scherm_basis import log, toestand, weergave, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402


def ververs():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            gebied.tag_redraw()


def schiet(naam):
    pad = os.path.join(scherm_basis.uitmap, naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    log(f"GIDS {'OK' if os.path.exists(pad) else 'FOUT'} {naam}")


def camera(zij_lidas, hoogte, afstand, plek):
    h, buig, lidas = Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0))
    k = (h * math.cos(math.radians(zij_lidas)) + lidas * math.sin(math.radians(zij_lidas))).normalized()
    k = (k * math.cos(math.radians(hoogte)) + buig * math.sin(math.radians(hoogte))).normalized()
    _, gebied, _ = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = k.to_track_quat("-Z", "Y")
    rv3d.view_distance = afstand
    rv3d.view_location = plek
    gebied.tag_redraw()


def verloop():
    wm = bpy.context.window_manager
    log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    lid = sp.been()
    figuren.maak_actief(lid)
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    cm = c.matrix.copy()
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        cm.col[i][:3] = v
    cm.col[3][:3] = (0, 0, 0)
    c.matrix = cm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = sp.SPELING, "CURSOR", False, False
    weergave()
    venster, gebied, _ = zijbalk()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=False)  # alleen de 3D-weergave, menu en zijbalk blijven
    yield 1.0
    _, gebied, _ = zijbalk()
    gebied.spaces.active.show_region_ui = True
    ov = gebied.spaces.active.overlay
    ov.show_floor = ov.show_axis_x = ov.show_axis_y = False
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    plek = Vector((6.0, 0, 6.0))
    camera(25, 12, 110, plek)
    ververs()
    yield 2.5
    schiet("g1-voor.png")
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("been_A"), bpy.data.objects.get("been_B")
    log(f"GIDS plaats: {uitslag} A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    if a is None or b is None:
        bpy.ops.wm.quit_blender()
        return
    figuren.maak_actief(a)
    wm.cj_scharnier_boog = True
    wm.cj_scharnier_pose = 60.0
    camera(25, 12, 110, plek)
    ververs()
    yield 2.5
    schiet("g2-pose.png")
    voorbij = math.floor(float(a["cj_bereik_graden"])) + 3.0
    wm.cj_scharnier_pose = voorbij
    log(f"GIDS voorbij={voorbij} rood_vlakken={len(a.get('cj_rood_vlakken', [])) // 2}")
    ververs()
    yield 2.5
    schiet("g3-voorbij.png")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
