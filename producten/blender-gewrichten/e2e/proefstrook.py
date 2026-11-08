"""Proefstrook geel (Daan, ontwerp): blender /tmp/start.blend --python e2e/proefstrook.py -- <map>
Zeven cilinders naast elkaar in de standaard Solid-weergave (kleur volgens Material, Studio-licht):
groen (huidig), vijf geeltinten, rood (huidig). Twee schermen: met de standaard kleurweergave van de scene
en met 'Standard', om te zien of de kleurweergave (AgX) het geel vaal maakt. Logt per cilinder de schermplek."""
import os
import subprocess
import sys
import bmesh
import bpy
from bpy_extras import view3d_utils
from mathutils import Vector

uitmap = sys.argv[sys.argv.index("--") + 1]
os.makedirs(uitmap, exist_ok=True)


def log(t):
    print(f"[cj-proef] {t}", flush=True)


def lin(hexkleur):
    def c(v):
        v = v / 255.0
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    h = hexkleur.lstrip("#")
    return (c(int(h[0:2], 16)), c(int(h[2:4], 16)), c(int(h[4:6], 16)), 1.0)


STALEN = [
    ("groen nu", (0.047, 0.716, 0.231, 1.0)),
    ("#FFD23F nu", lin("#FFD23F")),
    ("#FFE45C", lin("#FFE45C")),
    ("#FFF06A", lin("#FFF06A")),
    ("#FFC400", lin("#FFC400")),
    ("#FFEA00", lin("#FFEA00")),
    ("rood nu", (1.0, 0.074, 0.074, 1.0)),
]
toestand = {"n": 0}


def gebied3d():
    for v in bpy.context.window_manager.windows:
        for g in v.screen.areas:
            if g.type == "VIEW_3D":
                return v, g, next(r for r in g.regions if r.type == "WINDOW")
    return None, None, None


def bouw():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    for i, (naam, rgba) in enumerate(STALEN):
        me = bpy.data.meshes.new(f"staal{i}")
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, segments=64, radius1=5.0, radius2=5.0, depth=24.0)
        bm.to_mesh(me)
        bm.free()
        for p in me.polygons:
            p.use_smooth = True
        ob = bpy.data.objects.new(f"staal{i} {naam}", me)
        ob.location = (i * 14.0 - 42.0, 0, 0)
        mat = bpy.data.materials.new(f"proef {naam}")
        mat.diffuse_color = rgba
        mat.roughness = 0.6
        me.materials.append(mat)
        bpy.context.scene.collection.objects.link(ob)
    vs = bpy.context.scene.view_settings
    log(f"Blender {bpy.app.version_string}, kleurweergave scene: {vs.view_transform} / look {vs.look}")


def camera():
    v, g, r = gebied3d()
    ruimte = g.spaces.active
    ruimte.show_region_ui = False
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.overlay.show_overlays = False
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    log(f"licht {ruimte.shading.light} studio {ruimte.shading.studio_light}")
    rv3d = ruimte.region_3d
    rv3d.view_perspective = "PERSP"
    richting = Vector((0.0, 1.0, -0.35)).normalized()
    rv3d.view_rotation = richting.to_track_quat("-Z", "Y")
    rv3d.view_location = (0, 0, 0)
    rv3d.view_distance = 150.0
    g.tag_redraw()


def plekken():
    v, g, r = gebied3d()
    rv3d = g.spaces.active.region_3d
    for i, (naam, _) in enumerate(STALEN):
        uit = []
        for dx in (-3.5, 0.0, 3.5):
            p = view3d_utils.location_3d_to_region_2d(r, rv3d, Vector((i * 14.0 - 42.0 + dx, -4.5, 2.0)))
            if p is not None:
                uit.append((int(r.x + p.x), int(v.height - (r.y + p.y))))
        log(f"STAAL {i} {naam}: pixels links/midden/rechts {uit}")


def schiet(naam):
    pad = os.path.join(uitmap, naam)
    r = subprocess.run(["import", "-window", "root", pad], capture_output=True, text=True)
    log(f"scherm {pad} {os.path.exists(pad)} {r.stderr.strip()}")


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        bouw()
        camera()
        return 1.5
    if n == 2:
        plekken()
        schiet("proef-geel.png")
        bpy.context.scene.view_settings.view_transform = "Standard"
        return 1.0
    if n == 3:
        schiet("proef-geel-standard.png")
        return 0.3
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
