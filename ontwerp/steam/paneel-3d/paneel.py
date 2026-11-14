"""Voorstel paneel (kroniek en kaartje) in de 3D-stijl (Daan, 14 nov 2026). Vervangt kunst/paneel.png (12 x 12 pixels).
Een afgeronde plaat van donker pruimhout met een zachte gouden rand, zoals de schat en de tekens: mat, rond, geen lijnen.
Rendert een vierkante 9-slice-bron: rand = 1/3 van de breedte (bij 96 px dus 32 px = 4 spelpixels op 8 px per spelpixel).
    python3 paneel.py <uit.png> <px> <samples>
"""
import sys, math, bpy

def mat(naam, hexk, rough=0.5, metaal=0.0, spec=0.4):
    m = bpy.data.materials.new(naam); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    c = tuple(int(hexk[i:i + 2], 16) / 255 for i in (0, 2, 4))
    b.inputs["Base Color"].default_value = (*[x ** 2.2 for x in c], 1)
    b.inputs["Roughness"].default_value = rough; b.inputs["Metallic"].default_value = metaal
    return m

uit, PX, SAMPLES = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
# rand: afgeronde gouden rechthoek, binnenvlak: pruimhout iets lager
def plaat(naam, b, d, z, r, m):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, z))
    o = bpy.context.object; o.name = naam; o.scale = (b, b, d)
    bpy.ops.object.transform_apply(scale=True)
    mod = o.modifiers.new("rond", "BEVEL"); mod.width = r; mod.segments = 8; mod.limit_method = "NONE"
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o
goud = mat("rand", "e0a83a", rough=0.35, metaal=0.6)
hout = mat("binnen", "2b1b33", rough=0.8)
plaat("rand", 2.0, 0.3, 0.0, 0.14, goud)
plaat("binnen", 1.78, 0.3, 0.06, 0.1, hout)
cam = bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = 2.0
co = bpy.data.objects.new("cam", cam); co.location = (0, 0, 5); sc.collection.objects.link(co); sc.camera = co
for naam, loc, e, kleur in (("sleutel", (-3, 3, 6), 600, (1, 0.9, 0.8)), ("vul", (3, -2, 5), 150, (0.8, 0.8, 1))):
    l = bpy.data.lights.new(naam, "AREA"); l.size = 4; l.energy = e; l.color = kleur
    o = bpy.data.objects.new(naam, l); o.location = loc; sc.collection.objects.link(o)
    d = o.location; o.rotation_euler = (0, 0, 0)
    con = o.constraints.new("TRACK_TO"); con.target = bpy.data.objects["binnen"]
sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.device = "CPU"
sc.render.film_transparent = True; sc.render.resolution_x = sc.render.resolution_y = PX
sc.view_settings.view_transform = "Standard"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.25, 0.2, 0.3, 1); w.node_tree.nodes["Background"].inputs[1].default_value = 0.6
sc.render.filepath = uit; bpy.ops.render.render(write_still=True)
