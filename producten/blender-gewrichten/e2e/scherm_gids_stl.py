"""Schermen voor gidspagina 'downloaded STL' op dortus.com (gratis Click Joints, voor printers die nooit Blender
openden): het hele Blender-venster met de zijbalk, zodat de lezer de echte knoppen ziet.
    blender --factory-startup --gpu-backend opengl --python e2e/scherm_gids_stl.py -- <map> <gratis zip> <stl>
De STL en gewrichten.json ernaast komen uit gids_stl_bron.py (Knight van Quaternius, CC0, 250 mm hoog). Plaatjes:
s1-import (STL net geladen in de standaardscene in meters, na Check mesh), s2-joint (na Convert to mm, Make watertight als
Check mesh dat vraagt, en Place joint in de linkerelleboog, as langs de bovenarm), s3-export (3MF gekozen en geschreven).
Regels "GIDS OK <naam>" in het log."""
import json
import os
import subprocess
import sys

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scherm_basis  # noqa: E402
from scherm_basis import log, toestand, weergave, wiel_naar_tabblad, zijbalk  # noqa: E402

stl = scherm_basis.args[2]
GEWRICHT = json.load(open(os.path.join(os.path.dirname(stl), "gewrichten.json")))["LowerArm.L"]
AS = Vector(GEWRICHT["richting"])  # Z van de 3D-cursor langs de bovenarm, dus het snijvlak dwars door de arm
# 12 mm boven de elleboog (naar de schouder): op de elleboog zelf is de arm te dun ("Too thin"), op -6 mm is de wand
# oranje (0,93 mm), op -12 mm groen (1,55 mm). GEZIEN 24 nov in Blender 5.3.0 met de gratis zip, speling 0,20.
ELLEBOOG = Vector(GEWRICHT["plek"]) - AS * 12.0


def ververs():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            gebied.tag_redraw()


def schiet(naam):
    pad = os.path.join(scherm_basis.uitmap, naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    log(f"GIDS {'OK' if os.path.exists(pad) else 'FOUT'} {naam}")


def kijk(afstand=None, plek=None):
    _, gebied, _ = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    from mathutils import Euler
    rv3d.view_rotation = Euler((1.30, 0.0, 0.55)).to_quaternion()
    if afstand:
        rv3d.view_distance = afstand
    if plek is not None:
        rv3d.view_location = plek
    gebied.tag_redraw()


def doe(op, **kw):
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        return op(**kw)


def verloop():
    log(f"Blender {bpy.app.version_string}, gratis zip {scherm_basis.zip_pad}, stl {stl}")
    bpy.ops.extensions.package_install_files(filepath=scherm_basis.zip_pad, repo="user_default",
                                             enable_on_install=True)
    yield 1.0
    for ob in list(bpy.data.objects):
        if ob.type == "MESH":
            bpy.data.objects.remove(ob)  # de standaardkubus weg, zoals de gids zegt
    bpy.ops.wm.stl_import(filepath=stl)
    ridder = bpy.context.active_object
    log(f"GIDS import {ridder.name} dims={tuple(round(d, 1) for d in ridder.dimensions)} "
        f"schaal={bpy.context.scene.unit_settings.scale_length}")
    venster, gebied, _ = zijbalk()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=False)
    yield 1.0
    _, gebied, _ = zijbalk()
    gebied.spaces.active.show_region_ui = True
    gebied.spaces.active.overlay.show_floor = False
    weergave()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    log(f"GIDS check: {doe(bpy.ops.click_joints.controleer)} gesloten={ridder.get('cj_gesloten')}")
    kijk(450, Vector((0, 0, 125)))
    ververs()
    yield 2.5
    schiet("s1-import.png")

    log(f"GIDS mm: {doe(bpy.ops.click_joints.zet_om_mm)} schaal={bpy.context.scene.unit_settings.scale_length}")
    if not ridder.get("cj_gesloten"):
        log(f"GIDS dicht: {doe(bpy.ops.click_joints.maak_gesloten)} actief={bpy.context.active_object.name}")
    c = bpy.context.scene.cursor
    c.location = ELLEBOOG
    c.rotation_mode = "QUATERNION"
    c.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(AS)
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.20, "CURSOR", True
    uitslag = doe(bpy.ops.click_joints.plaats)
    delen = [o for o in bpy.data.objects if o.get("cj_deel")]
    a = next((o for o in delen if o.get("cj_deel") == "A"), None)
    log(f"GIDS plaats: {uitslag} delen={[o.name for o in delen]} "
        f"melding={a.get('cj_melding') if a else None} passing={a.get('cj_passing') if a else None} wand={a.get('cj_wand_mm') if a else None}")
    kijk(160, ELLEBOOG)
    ververs()
    yield 2.5
    schiet("s2-joint.png")

    tmp = os.path.join(__import__("tempfile").gettempdir(), "click_joints")
    inst.formaat = "3MF"
    inst.exportmap = ""  # leeg: tijdelijke map, zo staat geen machinepad in beeld
    log(f"GIDS export: {doe(bpy.ops.click_joints.exporteer)} "
        f"bestanden={sorted(os.listdir(tmp)) if os.path.isdir(tmp) else 'geen map'}")
    ververs()
    yield 2.5
    schiet("s3-export.png")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
