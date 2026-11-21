"""Hoofdbeeld Click Joints Pro voor Superhive en Gumroad (Bram, 21 nov 2026, opdrachten hoofdchat 06:45 en 08:50 NL).

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


def draai_om(obs, p, a, graden, doel_kant, wie):
    """Draai hele delen om punt p en as a; kies het teken waarbij het verste punt naar doel_kant gaat."""
    p, a = Vector(p), Vector(a).normalized()
    ver = max((obs[0].matrix_world @ v.co for v in obs[0].data.vertices), key=lambda q: (q - p).length)
    beste = None
    for teken in (1, -1):
        m = Matrix.Translation(p) @ Matrix.Rotation(math.radians(teken * graden), 4, a) @ Matrix.Translation(-p)
        score = ((m @ ver) - ver).dot(Vector(doel_kant))
        if beste is None or score > beste[0]:
            beste = (score, m)
    for ob in obs:
        ob.matrix_world = beste[1] @ ob.matrix_world
    print(f"[hb] {wie}: {graden} graden")


def deel(n):
    return next(o for o in delen if o.get("cj_naam") == n and o.get("cj_deel") == "B")


def scharnier(n, graden, doel_kant, ook=()):
    """Scharnier: om de eigen as uit de add-on (cj_scharnier_punt, cj_scharnier_as), binnen cj_bereik_graden."""
    ob = deel(n)
    assert graden <= ob["cj_bereik_graden"], n
    draai_om([ob, *ook], ob["cj_scharnier_punt"], ob["cj_scharnier_as"], graden, doel_kant, f"{n} (bereik {ob['cj_bereik_graden']})")


def kogel(n, graden, as_, doel_kant, ook=()):
    """Kogel: om het kogelcentrum (cj_centrum), binnen cj_grens_graden."""
    ob = deel(n)
    assert graden <= ob["cj_grens_graden"], n
    draai_om([ob, *ook], ob["cj_centrum"], as_, graden, doel_kant, f"{n} (grens {ob['cj_grens_graden']})")


# Houding (21 nov, tweede versie): eerst de ellebogen en knieën, dan de kogels die het hele lid meenemen.
# Alles binnen het bereik dat Pro meldt: ellebogen 0-140, knieën 0-120, schouders en nek 20, heupen 25.
scharnier("Right elbow", 80, (0, -1, 1))
scharnier("Left elbow", 40, (0, -1, 1))
scharnier("Left knee", 60, (0, 1, 0.3))
kogel("Left shoulder", 18, (0, 1, 0), (1, 0, 1), ook=[deel("Left elbow")])
kogel("Right shoulder", 18, (1, 0, 0), (0, -1, 0.3), ook=[deel("Right elbow")])
kogel("Left hip", 20, (1, 0, 0), (0, -1, 0), ook=[deel("Left knee")])
kogel("Neck", 10, (0, 1, 0), (1, 0, 0))

# Kleuren als drie rollen filament: romp en hoofd licht, bovenarmen en dijen antraciet, onderarmen en
# onderbenen blauw. Zo heeft elk deel een andere kleur dan zijn buur en zie je alle 10 delen ook klein.
def mat(n, kleur, rough=0.42):
    m = bpy.data.materials.new(n)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = kleur
    b.inputs["Roughness"].default_value = rough
    return m

licht = mat("licht", (0.86, 0.85, 0.82, 1))
donker = mat("donker", (0.012, 0.014, 0.018, 1))
blauw = mat("blauw", (0.004, 0.05, 0.32, 1))
for o in delen:
    o.data.materials.clear()
    n, d_ = o.get("cj_naam"), o.get("cj_deel")
    if d_ == "A" or n == "Neck":
        m = licht
    elif n in ("Left shoulder", "Right shoulder", "Left hip", "Right hip"):
        m = donker
    else:
        m = blauw
    o.data.materials.append(m)
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
sc.view_settings.look = "AgX - Punchy"
sc.render.filepath = uit
bpy.ops.render.render(write_still=True)
print("[hb] KLAAR", uit)
