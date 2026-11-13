"""Proef: Gloop als 3D-model in Blender, gerenderd tot een groot plaatje en tot pixelart.
Draai: /home/claude/bpyenv/bin/python gloop.py <uitmap> <breedte> <hoogte> <samples>
"""
import sys, math
import bpy
from mathutils import Vector

uit, W, H, SAMPLES = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

def mat(naam, kleur, rough=0.5, emis=0.0, spec=0.3, sss=0.0):
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*kleur, 1)
    b.inputs["Roughness"].default_value = rough
    if "Specular IOR Level" in b.inputs:
        b.inputs["Specular IOR Level"].default_value = spec
    if emis:
        b.inputs["Emission Color"].default_value = (*kleur, 1)
        b.inputs["Emission Strength"].default_value = emis
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
        b.inputs["Subsurface Radius"].default_value = (0.4, 0.9, 0.5)
    return m

def hex2(h):
    h = h.lstrip("#")
    c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(x ** 2.2 for x in c)  # sRGB naar lineair

MUNT = hex2("5fd6a4"); MUNT_D = hex2("2f9c78"); OOGWIT = hex2("f4f1e8"); PUPIL = hex2("1d1530")
PRUIM = hex2("3a2440"); PRUIM_L = hex2("5a3a63"); GOUD = hex2("f2b632"); ROOD = hex2("c8423b")
PAARS = hex2("6b4fbf"); STAAL = hex2("aab4c4"); MOND = hex2("3b1830"); TAND = hex2("fbf6e4")

# Lijf: metaballen, onderaan plat, een beetje peervormig en scheef (levendig, niet perfect)
mb = bpy.data.metaballs.new("lijf"); mb.resolution = 0.04; mb.render_resolution = 0.03
lijf = bpy.data.objects.new("lijf", mb); sc.collection.objects.link(lijf)
for (x, y, z, r) in [(0, 0, 0.55, 1.0), (0.15, 0, 0.95, 0.75), (-0.55, 0, 0.35, 0.6), (0.6, 0, 0.3, 0.55), (0, 0.1, 0.25, 0.8)]:
    e = mb.elements.new(); e.co = (x, y, z); e.radius = r
lijf.data.materials.append(mat("munt", MUNT, rough=0.25, spec=0.6, sss=0.25))
# platte onderkant: een vloer die het lijf afsnijdt
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
vloer = bpy.context.object; vloer.data.materials.append(mat("vloer", PRUIM_L, rough=0.9))

# Eén groot oog, iets naar rechts (kijkt naar de schat)
def bol(naam, loc, schaal, m):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=loc)
    o = bpy.context.object; o.name = naam; o.scale = schaal
    bpy.ops.object.shade_smooth(); o.data.materials.append(m); return o
bol("oogwit", (0.28, -0.72, 1.05), (0.42, 0.25, 0.46), mat("wit", OOGWIT, rough=0.2, spec=0.5))
bol("pupil", (0.40, -0.93, 1.02), (0.2, 0.08, 0.24), mat("pupil", PUPIL, rough=0.1, spec=0.9))
bol("glim", (0.47, -1.0, 1.13), (0.06, 0.03, 0.06), mat("glim", OOGWIT, emis=3.0))

# Scheve grijns met één tand
bpy.ops.mesh.primitive_torus_add(major_radius=0.32, minor_radius=0.07, location=(0.05, -0.86, 0.55), rotation=(math.radians(90), 0, math.radians(-12)))
grijns = bpy.context.object; grijns.data.materials.append(mat("mond", MOND, rough=0.6))
# alleen de onderste helft van de torus laten zien: boven wegsnijden met een boolean
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.05, -0.86, 0.78)); snij = bpy.context.object; snij.scale = (1.2, 0.6, 0.45)
mod = grijns.modifiers.new("snij", "BOOLEAN"); mod.object = snij; mod.operation = "DIFFERENCE"; snij.hide_render = True
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.2, -0.93, 0.47)); tand = bpy.context.object; tand.scale = (0.11, 0.06, 0.13)
tand.data.materials.append(mat("tand", TAND, rough=0.3))

# Hoedentoren: een helm, een puntmuts, een kroon, scheef om en om
def kegel(naam, loc, r1, r2, h, m, rot=0):
    bpy.ops.mesh.primitive_cone_add(vertices=40, radius1=r1, radius2=r2, depth=h, location=loc, rotation=(0, math.radians(rot), 0))
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); o.data.materials.append(m); return o
top = 1.36
kegel("helm", (0.08, 0, top + 0.12), 0.55, 0.45, 0.28, mat("staal", STAAL, rough=0.3, spec=0.8), rot=-6)
kegel("helmrand", (0.08, 0, top - 0.02), 0.66, 0.66, 0.06, mat("staal2", STAAL, rough=0.3, spec=0.8), rot=-6)
kegel("mutsrand", (0.0, 0, top + 0.33), 0.5, 0.5, 0.06, mat("paars", PAARS, rough=0.7), rot=8)
kegel("muts", (-0.05, 0, top + 0.72), 0.36, 0.02, 0.8, mat("paars2", PAARS, rough=0.7), rot=10)
kroon = kegel("kroon", (-0.16, 0, top + 1.18), 0.16, 0.2, 0.16, mat("goud", GOUD, rough=0.2, spec=1.0, emis=0.15), rot=14)
bol("ster", (-0.04, -0.33, top + 0.62), (0.07, 0.03, 0.07), mat("ster", GOUD, emis=1.5))

# Achtergrond: pruim wand
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 4, 5), rotation=(math.radians(90), 0, 0))
bpy.context.object.data.materials.append(mat("wand", PRUIM_L, rough=1.0))

# Licht: warm fakkellicht van rechts, koel licht van links, zacht van boven
def licht(naam, soort, loc, kleur, kracht, grootte=1.0):
    d = bpy.data.lights.new(naam, soort); d.color = kleur; d.energy = kracht
    if soort == "AREA": d.size = grootte
    o = bpy.data.objects.new(naam, d); o.location = loc; sc.collection.objects.link(o)
    o.rotation_euler = (Vector((0, 0, 1.0)) - Vector(loc)).to_track_quat("-Z", "Y").to_euler(); return o
licht("fakkel", "POINT", (2.6, -2.2, 1.6), (1.0, 0.62, 0.3), 900)
licht("koel", "AREA", (-3.0, -3.0, 3.0), (0.55, 0.6, 1.0), 400, 3.0)
licht("boven", "AREA", (0, -1.5, 5.0), (1, 0.95, 0.9), 250, 4.0)
sc.world = bpy.data.worlds.new("w"); sc.world.color = (0.02, 0.01, 0.03)

# Camera: orthografisch van voren, licht van boven
cam = bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = 4.6
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
co.location = (0.0, -10, 4.2); co.rotation_euler = (math.radians(75), 0, 0)

sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.device = "CPU"
sc.render.resolution_x = W; sc.render.resolution_y = H; sc.render.resolution_percentage = 100
sc.render.film_transparent = False
sc.view_settings.view_transform = "Standard"
sc.render.filepath = uit
bpy.ops.render.render(write_still=True)
print("klaar", uit)
