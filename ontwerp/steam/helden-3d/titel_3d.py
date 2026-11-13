"""Titel Hats of the Fallen in 3D, in de stijl van Gloop (Daan, 13 nov 2026).

Draai:  <venv>/bin/python titel_3d.py <uit.png> <breedte> <hoogte> <samples>
Het oude pixellogo (ontwerp/steam/winkelpagina/logo-1280.png) hoort bij de pixelrichting; sinds
Gloop 3D is, moet ook de titel speelgoed zijn: dik goud met een ronde rand, op elke letter van
HATS een hoed van een gevallen held (kroon, heksenhoed, pannetje, helm met pluim).
Letter: Lilita One (SIL Open Font License), in lettertype/.
"""
import sys, os, math
HIER = "/home/claude/dortus-hq/producten/steam-hol/modellen"
sys.path.insert(0, HIER)
import bpy
import gedeeld as g

uit = sys.argv[1]
W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lettertype", "LilitaOne.ttf")

g.leeg()
sc = bpy.context.scene
GOUD = g.mat("goud", "goud", rough=0.32, metaal=0.65, spec=0.6)
GOUD_D = g.mat("goud_d", "goud_d", rough=0.35, metaal=1.0)
MUNT = g.mat("munt", "munt", rough=0.35, spec=0.5, sss=0.15)
RAND = g.mat("rand", "1d1530", rough=0.6)
PAARS = g.mat("paars", "paars", rough=0.55)
STAAL = g.mat("staal", "staal", rough=0.3, metaal=1.0)
ROOD = g.mat("rood", "rood", rough=0.5)
font = bpy.data.fonts.load(FONT)


def tekst(s, x, z, grootte, m, diep=0.18, rand=0.05, achter=None):
    cu = bpy.data.curves.new(s, "FONT"); cu.body = s; cu.font = font
    cu.size = grootte; cu.extrude = diep; cu.bevel_depth = rand; cu.bevel_resolution = 4
    cu.align_x = "CENTER"; cu.align_y = "CENTER"; cu.space_character = 1.04
    o = bpy.data.objects.new(s, cu); sc.collection.objects.link(o)
    o.location = (x, 0, z); o.rotation_euler = (math.radians(90), 0, 0)
    o.data.materials.append(m)
    if achter:   # donkere dikke rand erachter, zoals de lijn om Gloop
        cu2 = cu.copy(); cu2.extrude = diep * 0.6; cu2.bevel_depth = rand + achter
        cu2.materials.clear(); cu2.materials.append(RAND)
        o2 = bpy.data.objects.new(s + "_rand", cu2); sc.collection.objects.link(o2)
        o2.location = (x, 0.12, z); o2.rotation_euler = o.rotation_euler
    return o


def letterpos(o, i):
    """Midden-boven van letter i, via de bounding box na het omzetten naar mesh."""
    bpy.context.view_layer.update()
    deps = bpy.context.evaluated_depsgraph_get()
    me = o.evaluated_get(deps).to_mesh()
    xs = [(o.matrix_world @ v.co) for v in me.vertices]
    o.evaluated_get(deps).to_mesh_clear()
    return min(p.x for p in xs), max(p.x for p in xs), max(p.z for p in xs)


hats = tekst("HATS", 0, 0.55, 2.3, GOUD, diep=0.22, rand=0.06, achter=0.07)
sub = tekst("OF THE FALLEN", 0, -0.75, 0.82, MUNT, diep=0.14, rand=0.035, achter=0.06)
x0, x1, top = letterpos(hats, 0)
stap = (x1 - x0) / 4


def cil(naam, loc, r, d, m, rot=(0, 0, 0), verts=32, r2=None):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r if r2 is None else r2, depth=d,
                                    location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); return o


def bol(naam, loc, s, m):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=loc, segments=32, ring_count=16)
    o = bpy.context.object; o.name = naam; o.scale = s; o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); return o


mid = [x0 + stap * (i + 0.5) for i in range(4)]
t = top + 0.02
# H: kroon (drie punten met bolletjes, rode steen)
cil("kroonband", (mid[0], -0.05, t + 0.14), 0.38, 0.28, GOUD, verts=40)
for k in (-1, 0, 1):
    cil("kroonpunt", (mid[0] + k * 0.24, -0.05, t + 0.42), 0.12, 0.34, GOUD, r2=0.0, verts=16)
    bol("kroonbol", (mid[0] + k * 0.24, -0.05, t + 0.62), (0.06, 0.06, 0.06), GOUD)
bol("kroonsteen", (mid[0], -0.42, t + 0.15), (0.08, 0.05, 0.08), ROOD)
# A: heksenhoed, schuin
hoed = cil("hoedrand", (mid[1], 0, t + 0.04), 0.5, 0.06, PAARS, verts=40)
cil("hoedpunt", (mid[1] + 0.08, 0, t + 0.6), 0.3, 1.15, PAARS, r2=0.015, rot=(0, math.radians(10), 0), verts=32)
cil("hoedband", (mid[1] + 0.01, 0, t + 0.14), 0.31, 0.1, GOUD_D, verts=32)
# T: pannetje (Gloops eerste helm)
bol("pan", (mid[2], 0, t + 0.02), (0.5, 0.42, 0.3), STAAL)
cil("panrand", (mid[2], 0, t + 0.0), 0.56, 0.05, STAAL, verts=40)
# S: ridderhelm met rode pluim
bol("helm", (mid[3], 0, t + 0.05), (0.4, 0.36, 0.36), STAAL)
for k in range(4):
    bol("pluim", (mid[3] - 0.05 + k * 0.04, 0, t + 0.42 + k * 0.08), (0.11, 0.11, 0.13), ROOD)
# helften onder de letters wegsnijden is niet nodig: de hoeden staan op de bovenrand

cam = g.camera(hoogte_midden=0.55, schaal=8.0)
g.licht()
for o in sc.objects:
    if o.type == "LIGHT":
        o.visible_camera = False
g.render(uit, W, H, SAMPLES, doorzichtig=True)
print("klaar", uit)
