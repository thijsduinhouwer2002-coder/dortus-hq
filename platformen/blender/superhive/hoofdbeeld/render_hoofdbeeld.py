"""Hoofdbeeld Click Joints Pro voor Superhive (Bram, 21 nov 2026, opdracht hoofdchat 06:45 NL).

Rendert de echte delen die Pro 1.1 maakt na "Figure from rig" op de mensfiguur van de CI-toets
(e2e/toetsen_mens.py: MakeHuman base.obj CC0, 220 mm, 9 gewrichten, 10 delen). Niets nagetekend: het script
draait alleen hele delen om hun eigen scharnieras (cj_scharnier_punt, cj_scharnier_as van de add-on), binnen het
gemeten bereik, en geeft elk deel een kleur. Rendert met Cycles op een doorzichtige achtergrond met schaduw.
Tekst en achtergrondkleur komen er daarna bij in maak_hoofdbeeld.py.

    blender -b <mens.blend> --python render_hoofdbeeld.py -- <uit.png>
"""
import math
import sys

import bpy
from mathutils import Matrix, Vector

uit = sys.argv[sys.argv.index("--") + 1]
sc = bpy.context.scene
for o in list(sc.objects):
    if o.type != "MESH" or not o.visible_get():
        bpy.data.objects.remove(o, do_unlink=True)
delen = [o for o in sc.objects if o.type == "MESH"]
print("[hb] delen:", len(delen))


def draai(ob, graden, doel_kant):
    """Draai deel B om zijn scharnieras; kies het teken waarbij het verste punt naar doel_kant gaat."""
    p = Vector(ob["cj_scharnier_punt"])
    a = Vector(ob["cj_scharnier_as"]).normalized()
    ver = max((ob.matrix_world @ v.co for v in ob.data.vertices), key=lambda q: (q - p).length)
    beste = None
    for teken in (1, -1):
        m = Matrix.Translation(p) @ Matrix.Rotation(math.radians(teken * graden), 4, a) @ Matrix.Translation(-p)
        score = ((m @ ver) - ver).dot(Vector(doel_kant))
        if beste is None or score > beste[0]:
            beste = (score, m)
    ob.matrix_world = beste[1] @ ob.matrix_world
    print(f"[hb] {ob['cj_naam']}: {graden} graden (bereik {ob['cj_bereik_graden']})")


naam = {o.get("cj_naam"): o for o in delen if o.get("cj_soort") == "SCHARNIER"}
# Linkerknie 55 graden naar achter (voet naar +Y), rechterelleboog 70 graden naar voor en omhoog.
draai(naam["Left knee"], 55, (0, 1, 0.4))
draai(naam["Right elbow"], 70, (0, -1, 1))

# Kleuren als twee rollen filament: romp en hoofd licht, ledematen donker, zodat elke naad te zien is.
def mat(n, kleur, rough=0.42):
    m = bpy.data.materials.new(n)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = kleur
    b.inputs["Roughness"].default_value = rough
    return m

licht = mat("licht", (0.86, 0.85, 0.82, 1))
donker = mat("donker", (0.06, 0.065, 0.08, 1))
for o in delen:
    o.data.materials.clear()
    kogel_romp = o.get("cj_deel") == "A"  # het A-deel dat overblijft is romp met hoofd
    hoofd = o.get("cj_naam") == "Neck" and o.get("cj_deel") == "B"
    o.data.materials.append(licht if (kogel_romp or hoofd) else donker)
    for f in o.data.polygons:
        f.use_smooth = True

# Vloer die alleen schaduw vangt
bpy.ops.mesh.primitive_plane_add(size=2000, location=(0, 0, min((o.matrix_world @ v.co).z for o in delen for v in o.data.vertices)))
vloer = bpy.context.active_object
vloer.is_shadow_catcher = True

mid = Vector((0, 5, 112))
cam_d = bpy.data.cameras.new("cam")
cam_d.lens = 85
cam = bpy.data.objects.new("cam", cam_d)
sc.collection.objects.link(cam)
import os
cx, cy = (float(v) for v in os.environ.get("HB_CAM", "-620,-600").split(","))
cam.location = mid + Vector((cx, cy, 120))
cam.rotation_euler = (mid - cam.location).to_track_quat("-Z", "Y").to_euler()
cam_d.sensor_fit = "VERTICAL"
cam_d.sensor_height = 24 * 1.0
sc.camera = cam


def lamp(n, loc, energie, grootte, kleur=(1, 1, 1)):
    d = bpy.data.lights.new(n, "AREA")
    d.energy, d.size, d.color = energie, grootte, kleur
    o = bpy.data.objects.new(n, d)
    sc.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (mid - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

lamp("sleutel", (-350, -400, 420), 9e6, 300)
lamp("rand", (320, 300, 330), 7e6, 200, (1.0, 0.85, 0.7))
lamp("vul", (400, -500, 120), 2.5e6, 400)
sc.world = bpy.data.worlds.new("w")
sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs[0].default_value = (0.5, 0.5, 0.55, 1)
sc.world.node_tree.nodes["Background"].inputs[1].default_value = 0.35

sc.render.engine = "CYCLES"
sc.cycles.samples = int(__import__("os").environ.get("HB_SAMPLES", "96"))
sc.cycles.use_denoising = True
sc.render.film_transparent = True
sc.render.resolution_x, sc.render.resolution_y = 900, 1200
sc.render.resolution_percentage = 100
sc.view_settings.view_transform = "AgX"
sc.render.filepath = uit
bpy.ops.render.render(write_still=True)
print("[hb] KLAAR", uit)
