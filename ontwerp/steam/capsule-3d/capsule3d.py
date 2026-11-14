"""Capsule (winkelafbeelding) van Hats of the Fallen in 3D (Mila, 14 nov 2026).

Draai:  <venv>/bin/python capsule3d.py <uit.png> <breedte> <hoogte> <samples> [variant]
  Header:  capsule3d.py header.png 920 430 64
  Klein:   capsule3d.py klein.png 462 174 64 klein

Het idee (de haak in één beeld): Gloop zit grijnzend op zijn goud met een toren van gestolen hoeden
(helm, kroon, heksenhoed, rode muts). Links staat een ridder die net binnenkomt en schrikt: onderaan de
toren draagt Gloop precies dezelfde helm als hij. Je snapt zonder tekst wat er met de vorige ridder
gebeurd is, en dat jij de volgende bent. Alles wat je ziet zit in het spel: Gloop, de hoedentoren, de
schat, de fakkels, de ridder met helm en pluim, de stand schrik.

Gloop en de ridder komen ongewijzigd uit Daans gloop.py en held.py (ingelezen, zoals in hol.py).
De titel is 3D-tekst in Lilita One (SIL Open Font License, Google Fonts), goud met een pruimen rand.
Camera: anders dan de strook een lichte perspectief (lange lens), want een capsule is een poster, geen tegel.
"""
import sys, os, math, random
HIER = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.normpath(os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
sys.path.insert(0, MOD)
import bpy
from mathutils import Vector
import gedeeld as g

uit = sys.argv[1]
W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
VARIANT = sys.argv[5] if len(sys.argv) > 5 else "header"
FONT = os.environ.get("CAPSULE_FONT", os.path.join(HIER, "LilitaOne-Regular.ttf"))
random.seed(11)

g.leeg()
sc = bpy.context.scene

# ---------- hulpjes ----------
def kies(o, m):
    o.data.materials.clear(); o.data.materials.append(m); return o

def bol(naam, loc, schaal, m, segs=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc)
    o = bpy.context.object; o.name = naam; o.scale = schaal; bpy.ops.object.shade_smooth(); return kies(o, m)

def cil(naam, loc, r, d, m, rot=(0, 0, 0), verts=32, r2=None):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); return kies(o, m)

def ruismat(naam, donker, licht, schaal=1.2, bump=0.35):
    m = g.mat(naam, donker, rough=0.85, spec=0.15)
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    ns = nt.nodes.new("ShaderNodeTexNoise"); ns.inputs["Scale"].default_value = schaal; ns.inputs["Detail"].default_value = 4
    cr = nt.nodes.new("ShaderNodeValToRGB")
    cr.color_ramp.elements[0].position = 0.4; cr.color_ramp.elements[0].color = (*g.hex2(donker), 1)
    cr.color_ramp.elements[1].position = 0.65; cr.color_ramp.elements[1].color = (*g.hex2(licht), 1)
    bm = nt.nodes.new("ShaderNodeBump"); bm.inputs["Strength"].default_value = bump
    nt.links.new(ns.outputs["Fac"], cr.inputs["Fac"]); nt.links.new(cr.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(ns.outputs["Fac"], bm.inputs["Height"]); nt.links.new(bm.outputs["Normal"], b.inputs["Normal"])
    return m

GOUD = g.mat("goud", "goud", rough=0.2, spec=0.9, metaal=0.85, emis=0.05)
GOUD_D = g.mat("goud_d", "goud_d", rough=0.3, spec=0.7, metaal=0.8)
WAND = ruismat("wand", "35203c", "5a3a66", 1.1)
VLOER = ruismat("vloer", "2c1a33", "4a2e52", 2.0, 0.2)
STEEN = g.mat("steen", "7a5d86", rough=0.6, spec=0.3)
HOUT_F = g.mat("hout_f", "6e4632", rough=0.75, spec=0.2)
DOEK = g.mat("doek", "3a2418", rough=0.9)
IJZER = g.mat("ijzer", "3b3640", rough=0.45, metaal=0.8)
V_BUIT = g.mat("v_buit", "ff5a1f", emis=2.0)
V_MID = g.mat("v_mid", "ff9b2a", emis=3.0)
V_HART = g.mat("v_hart", "ffe27a", emis=4.0)
ROBIJN = g.mat("robijn", "rood", rough=0.08, spec=1.0, emis=0.4)
SAFIER = g.mat("safier", "4fa3ff", rough=0.08, spec=1.0, emis=0.4)

KLEIN = VARIANT == "klein"
GX = 2.35 if not KLEIN else 3.4          # Gloop rechts van het midden
RX = -0.95 if not KLEIN else 0.2        # ridder

# ---------- achterwand met boog (de schatkamer) en vloer ----------
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 3.2, 3)); o = bpy.context.object
o.scale = (30, 14, 1); o.rotation_euler = (math.radians(90), 0, 0); kies(o, WAND)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0)); o = bpy.context.object
o.scale = (30, 14, 1); kies(o, VLOER)
# stenen boog achter Gloop: een ring van afgeronde blokken, half in de wand
for i in range(15):
    a = math.radians(180 * i / 14)
    x = GX + 3.4 * math.cos(a); z = 0.2 + 4.9 * math.sin(a)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 3.05, z)); s = bpy.context.object
    s.scale = (0.55, 0.4, 0.42); s.rotation_euler = (0, -a + math.pi / 2, 0)
    bv = s.modifiers.new("r", "BEVEL"); bv.width = 0.1; bv.segments = 3
    kies(s, STEEN if i % 2 == 0 else g.mat("steen_d", "65497a", rough=0.65))
# rotsen langs de voet van de wand (geen harde lijn tussen vloer en wand)
for i in range(40):
    x = -7.5 + i * 0.4 + random.uniform(-0.1, 0.1)
    bol("voetrots", (x, 3.0, random.uniform(-0.05, 0.1)), (random.uniform(0.3, 0.5), 0.35, random.uniform(0.18, 0.4)),
        g.mat("vr", random.choice(["4e3158", "5a3a66", "432a4c"]), rough=0.8), 16)
# losse kiezels in de wand
for i in range(26):
    x = random.uniform(-7, 7); z = random.uniform(0.3, 6.5)
    if abs(x - GX) < 3.4 and z < 4.2:
        continue
    bol("kiezel", (x, 3.15, z), (random.uniform(0.08, 0.2), 0.1, random.uniform(0.06, 0.14)), g.mat("kz", "4e3158", rough=0.8), 12)

# ---------- fakkels aan de wand ----------
def druppel(naam, loc, r, hoog, m, scheef=0.0):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=14, radius=1, location=(0, 0, 0))
    o = bpy.context.object; o.name = naam
    for v in o.data.vertices:
        if v.co.z > 0:
            t = v.co.z; k = (1 - t) ** 1.6
            v.co.x = v.co.x * k + scheef * t * t; v.co.y *= k; v.co.z = t * hoog
    o.scale = (r, r * 0.85, r); o.location = loc; o.visible_shadow = False
    bpy.ops.object.shade_smooth(); return kies(o, m)

def fakkel(x, z, y=2.9, kracht=260, groot=1.6):
    cil("beugel", (x, y + 0.12, z - 0.25), 0.1, 0.04, IJZER, rot=(math.radians(90), 0, 0), verts=6)
    cil("steel", (x, y - 0.05, z - 0.2), 0.08, 0.6, HOUT_F, rot=(math.radians(-12), 0, 0), verts=10, r2=0.05)
    cil("kop", (x, y - 0.1, z + 0.12), 0.12 * groot / 1.2, 0.18, DOEK, verts=12, r2=0.14 * groot / 1.2)
    zv = z + 0.26
    druppel("vlam", (x, y - 0.12, zv + 0.12 * groot), 0.15 * groot, 2.3, V_BUIT, 0.05)
    druppel("vlammid", (x, y - 0.18, zv + 0.1 * groot), 0.11 * groot, 2.0, V_MID, 0.04)
    druppel("kern", (x, y - 0.24, zv + 0.06 * groot), 0.06 * groot, 1.7, V_HART, 0.02)
    d = bpy.data.lights.new("fakkellicht", "POINT"); d.color = (1.0, 0.6, 0.28); d.energy = kracht; d.shadow_soft_size = 0.3
    l = bpy.data.objects.new("fakkellicht", d); l.location = (x, y - 0.6, zv + 0.5); sc.collection.objects.link(l)

fakkel(GX - 3.4, 3.1)
fakkel(GX + 3.4, 3.1)

# ---------- de schat: een berg munten onder en rond Gloop ----------
bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=(GX, 0.5, -0.4)); berg = bpy.context.object
berg.scale = (3.3, 2.2, 1.25); bpy.ops.object.shade_smooth(); kies(berg, GOUD_D)

def munt(loc, r=0.17, rx=None, ry=None):
    rx = random.uniform(-40, 40) if rx is None else rx; ry = random.uniform(-40, 40) if ry is None else ry
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=r, depth=0.05, location=loc,
                                        rotation=(math.radians(rx), math.radians(ry), random.uniform(0, 6)))
    o = bpy.context.object; o.name = "munt"; bpy.ops.object.shade_smooth()
    bv = o.modifiers.new("r", "BEVEL"); bv.width = 0.012; bv.segments = 2
    kies(o, GOUD)

for i in range(340):
    a = random.uniform(0, 2 * math.pi); rr = math.sqrt(random.random())
    x = GX + 3.2 * rr * math.cos(a); y = 0.5 + 2.1 * rr * math.sin(a)
    hz = 1.25 * math.sqrt(max(0.0, 1 - ((x - GX) / 3.3) ** 2 - ((y - 0.5) / 2.2) ** 2)) - 0.4
    if hz < 0.01:
        continue
    munt((x, y, hz + 0.02), random.uniform(0.13, 0.19))
# losse munten op de vloer, ook richting de ridder (de schat lokt)
for i in range(30):
    munt((random.uniform(GX - 4.5, GX + 4.0), random.uniform(-1.0, 1.2), 0.03), random.uniform(0.13, 0.18),
         random.uniform(-8, 8), random.uniform(-8, 8))
# een paar staande munten en edelstenen vooraan
for (x, y, rot) in [(GX - 2.1, -0.7, 75), (GX + 2.3, -0.5, 70), (GX - 3.4, -0.2, 80)]:
    munt((x, y, 0.17), 0.18, rot, random.uniform(-30, 30))
for (x, y, z, m) in [(GX - 1.5, -0.4, 0.18, ROBIJN), (GX + 1.7, -0.2, 0.25, SAFIER), (GX + 0.9, 0.2, 0.55, ROBIJN)]:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=0.16, location=(x, y, z)); e = bpy.context.object
    e.scale = (1, 1, 1.3); kies(e, m)
# beker
cil("beker", (GX + 2.15, 0.4, 0.5), 0.2, 0.42, GOUD, verts=32, r2=0.25)
cil("bekervoet", (GX + 2.15, 0.4, 0.22), 0.07, 0.3, GOUD, verts=16)
cil("bekerbodem", (GX + 2.15, 0.4, 0.06), 0.18, 0.05, GOUD, verts=24)

# ---------- Gloop van Daan (gloop.py ongewijzigd), met de hele hoedentoren ----------
voor = set(bpy.data.objects)
bron = open(os.path.join(MOD, "gloop.py"), encoding="utf-8").read()
begin = bron.index("# ---------- lijf"); eind = bron.index("# ---------- camera")
ns = {"bpy": bpy, "g": g, "math": math, "sc": sc, "VERSIE": 2, "HOEDEN": 4, "sys": sys, "os": os,
      "STAND": os.environ.get("CAPSULE_STAND", "rust")}
exec(bron[bron.index("def bol("):begin], ns)
exec(bron[begin:eind], ns)
GS = 1.95
for o in [o for o in bpy.data.objects if o not in voor]:
    if getattr(o, "is_shadow_catcher", False) or o.name.startswith("Plane"):
        bpy.data.objects.remove(o, do_unlink=True); continue
    o.name = "gloop_" + o.name
    if o.parent is None:
        o.location = Vector((o.location.x * GS + GX, o.location.y * GS - 0.9, o.location.z * GS + 0.45))
        o.scale = o.scale * GS
# Gloop kijkt een tikje naar de ridder: alles om zijn midden 12 graden draaien
anker = bpy.data.objects.new("gloop_anker", None); anker.location = (GX, -0.9, 0.45); sc.collection.objects.link(anker)
for o in list(sc.objects):
    if o.name.startswith("gloop_") and o.parent is None and o is not anker:
        mw = o.matrix_world.copy(); o.parent = anker; o.matrix_world = mw
anker.rotation_euler = (0, 0, math.radians(-12))

# ---------- de ridder: komt binnen en schrikt ----------
import held
held.bouw("ridder", "schrik", plek=(RX, -1.6, 0.0), draai=38, schaal=1.0, gloed=30, rand=60)

# ---------- de hoedenberg: in het spel draagt Gloop er 4, de rest ligt op de berg (toets_held.gd) ----------
import hoeden
for nr, x, y, z, k, d in [(6, GX - 2.15, -0.9, 0.38, -18, 20), (5, GX + 2.0, -0.6, 0.55, 22, -15),
                          (8, GX - 1.2, -1.75, 0.22, 12, 40), (3, GX + 1.25, -1.6, 0.32, -14, -30),
                          (9, GX + 2.75, 0.2, 0.55, 28, -20), (2, GX - 2.9, 0.1, 0.2, -25, 30),
                          (7, GX - 1.7, 0.35, 0.72, -10, 25)]:
    hoeden.bouw(nr, plek=(x, y, z), schaal=0.85, kantel=k, draai=d)

# ---------- titel ----------
def tekst(woord, loc, maat, uitlijn="LEFT", kantel=0):
    cu = bpy.data.curves.new("titel", "FONT"); cu.body = woord
    cu.font = bpy.data.fonts.load(FONT); cu.size = maat; cu.align_x = uitlijn; cu.align_y = "BOTTOM"
    cu.extrude = 0.09 * maat; cu.bevel_depth = 0.025 * maat; cu.bevel_resolution = 3
    o = bpy.data.objects.new("titel", cu); sc.collection.objects.link(o)
    o.location = loc; o.rotation_euler = (math.radians(90 - 6), math.radians(kantel), 0)
    o.data.materials.append(g.mat("titelgoud", "ffc93a", rough=0.25, spec=0.8, metaal=0.6, emis=0.12))
    # rand: zelfde tekst, dikker (offset) en erachter, donker pruim
    cu2 = cu.copy(); cu2.offset = 0.0; cu2.extrude = 0.06 * maat; cu2.bevel_depth = 0.07 * maat; cu2.bevel_resolution = 2
    o2 = bpy.data.objects.new("titelrand", cu2); sc.collection.objects.link(o2)
    o2.location = (loc[0], loc[1] + 0.14 * maat, loc[2] - 0.02 * maat); o2.rotation_euler = o.rotation_euler
    cu2.materials.clear(); cu2.materials.append(g.mat("titelrand", "1d1026", rough=0.6))
    return o

if KLEIN:
    tekst("HATS", (-5.1, -0.6, 2.3), 2.3, kantel=-3)
    tekst("OF THE FALLEN", (-5.0, -0.6, 1.32), 0.9, kantel=-3)
else:
    tekst("HATS", (-5.0, -0.6, 3.0), 1.95, kantel=-3)
    tekst("OF THE FALLEN", (-4.9, -0.6, 2.1), 0.74, kantel=-3)

# ---------- licht ----------
def lamp(naam, soort, loc, kleur, kracht, grootte=1.0, doel=(0, 0, 1.0)):
    d = bpy.data.lights.new(naam, soort); d.color = kleur; d.energy = kracht
    if soort == "AREA":
        d.size = grootte
    o = bpy.data.objects.new(naam, d); o.location = loc; sc.collection.objects.link(o)
    o.rotation_euler = (Vector(doel) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    o.visible_camera = False
    return o

lamp("sleutel", "AREA", (GX + 3.5, -5.0, 6.0), (1.0, 0.82, 0.6), 1600, 4.0, (GX, 0.3, 1.5))
lamp("koel", "AREA", (-5.0, -1.0, 5.0), (0.55, 0.62, 1.0), 500, 3.0, (RX, -1.6, 1.0))
lamp("vul", "AREA", (-1.0, -8.0, 2.5), (0.85, 0.85, 1.0), 260, 6.0, (0, 0, 1.5))
lamp("titellamp", "AREA", (-3.0, -4.0, 4.5), (1.0, 0.95, 0.85), 500, 3.0, (-3.0, -0.6, 2.4))
lamp("schatgloed", "POINT", (GX, -1.8, 0.9), (1.0, 0.75, 0.35), 160)
lamp("wandgloed", "POINT", (GX, 2.2, 2.0), (1.0, 0.62, 0.3), 900)   # warme gloed op de muur achter Gloop
sc.world = bpy.data.worlds.new("w"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.03, 0.02, 0.045, 1)

# ---------- camera ----------
cam = bpy.data.cameras.new("cam"); cam.lens = 42; cam.sensor_fit = "HORIZONTAL"; cam.sensor_width = 36
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
doel = Vector((0.3, 0.6, 2.2)) if not KLEIN else Vector((0.45, 0.6, 2.1))
co.location = (0.3, -13.5, 3.6) if not KLEIN else (0.45, -13.5, 3.5)
co.rotation_euler = (doel - Vector(co.location)).to_track_quat("-Z", "Y").to_euler()
if KLEIN:
    cam.lens = 37

sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.device = "CPU"; sc.cycles.use_denoising = True
sc.render.resolution_x = W; sc.render.resolution_y = H; sc.render.resolution_percentage = 100
sc.render.film_transparent = False
sc.view_settings.view_transform = "Standard"; sc.view_settings.look = "None"
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = uit
bpy.ops.render.render(write_still=True)
print("klaar", uit)
