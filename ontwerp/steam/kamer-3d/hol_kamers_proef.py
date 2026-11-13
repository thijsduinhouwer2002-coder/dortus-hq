"""Het hol in 3D, stukje 1: de schatkamer met een gang (Mila, 13 nov 2026).

Draai:  <venv>/bin/python hol.py <uit.png> <breedte> <hoogte> <samples> [gloop_versie] [hoeden]
  Voorbeeld strook op ware grootte: hol.py strook.png 720 120 24 2 2
  Groot om te bekijken:             hol.py groot.png 1440 240 32 2 2

Wat erin zit: een doorsnede van de grond zoals een mierenbak. Bovenop gras met sprietjes,
daaronder pruim (geen bruin, zie ontwerp/steam/mila/stijl.md), uitgehold: links een gang,
in het midden de schatkamer met een gouden berg, een kist en twee fakkels die warm licht op de
pruim gooien. Gloop (Daans gloop.py, ongewijzigd) staat in de kamer.
Camera en licht komen uit gedeeld.py (regel 1 van 3d-stijl.md); de fakkels geven extra licht.
Schaal: 120 px hoog = 4,5 eenheden, dus 1 eenheid is ±27 px; Gloop is even groot als in Daans strook.
"""
import sys, os, math, random
HIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "producten", "steam-hol", "modellen")
sys.path.insert(0, HIER)
import bpy
from mathutils import Vector
import gedeeld as g

uit = sys.argv[1]
W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
GLOOP_V = int(sys.argv[5]) if len(sys.argv) > 5 else 2
HOEDEN = int(sys.argv[6]) if len(sys.argv) > 6 else 2
random.seed(7)

g.leeg()
sc = bpy.context.scene

HOOGTE = 4.5                      # wereld-eenheden op de hoogte van het plaatje
BREED = HOOGTE * W / H
ONDER = -0.55                     # onderkant van het beeld
# Rijen van hol.gd (Bram 13 nov): 40 spelpixels hoog, gras 0 tot 8, bovenste rij 8 tot 24, gang 24 tot 40,
# kolom 16 breed. Eén spelpixel is HOOGTE / 40 = 0,1125 eenheid. De camera kijkt 15 graden van boven, dus een
# hoogte z op de voorkant (y = 0) komt op spelpixel 40 * (2,25 - 0,966 * (z - CAM_MIDDEN)) / 4,5.
CAM_MIDDEN = 2.025                # vast, zodat de rijen niet verschuiven als er iets aan het hol verandert
MAAIVELD = 3.423                  # bovenkant van de aarde: voorrand op spelpixel 8
GANG_TOP = 1.559                  # plafond van de gang: spelpixel 24 (vloer z = 0 komt op 37,4, voeten op 37)
SPX = HOOGTE / 40                 # één spelpixel in eenheden
KOL = 16 * SPX                    # één kolom van hol.gd
LINKS = -BREED / 2                # x van spelpixel 0
TEGEL_X = LINKS + 13 * KOL        # kolom 13 en 14 (spelpixel 208 tot 240): rustig stuk voor herhalende tegels
TEGEL_LICHT = float(os.environ.get("HOL_TEGEL_LICHT", "300"))
X0, X1 = -BREED / 2 - 0.5, BREED / 2 + 0.5


def kies(o, m):
    o.data.materials.append(m)
    return o


def blok(naam, loc, maat, m=None, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; o.scale = maat
    if m: kies(o, m)
    return o


def bol(naam, loc, schaal, m, segs=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=max(8, segs // 2), location=loc)
    o = bpy.context.object; o.name = naam; o.scale = schaal
    bpy.ops.object.shade_smooth(); return kies(o, m)


def cil(naam, loc, r, d, m, rot=(0, 0, 0), verts=32, r2=None):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); return kies(o, m)


def afronden(o, breedte=0.12, seg=3):
    b = o.modifiers.new("rond", "BEVEL"); b.width = breedte; b.segments = seg; b.limit_method = "NONE"


def uithollen(doel, gat):
    mod = doel.modifiers.new("hol", "BOOLEAN"); mod.operation = "DIFFERENCE"; mod.object = gat
    mod.solver = "EXACT"
    gat.hide_render = True; gat.display_type = "WIRE"


# ---------- materialen ----------
def aardemat(naam, donker, licht, schaal=1.6):
    """Pruim met lagen en vlekken (ruis), zodat de aarde op ware grootte niet als één vlak leest."""
    m = g.mat(naam, donker, rough=0.85, spec=0.15)
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    # Herhaalt precies elke kolom (16 spelpixels) in x: x gaat rond op een cirkel (cos, sin), z en y blijven.
    # Zo past elk stuk van 16 breed links en rechts op zichzelf (Bram 13 nov, vraag 3).
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    hoek = nt.nodes.new("ShaderNodeMath"); hoek.operation = "MULTIPLY"; hoek.inputs[1].default_value = 2 * math.pi / KOL
    co = nt.nodes.new("ShaderNodeMath"); co.operation = "COSINE"
    si = nt.nodes.new("ShaderNodeMath"); si.operation = "SINE"
    r = KOL / (2 * math.pi) * schaal * 0.7       # zelfde korrel als vroeger in x
    cr_ = nt.nodes.new("ShaderNodeMath"); cr_.operation = "MULTIPLY"; cr_.inputs[1].default_value = r
    sr_ = nt.nodes.new("ShaderNodeMath"); sr_.operation = "MULTIPLY"; sr_.inputs[1].default_value = r
    zz = nt.nodes.new("ShaderNodeMath"); zz.operation = "MULTIPLY"; zz.inputs[1].default_value = schaal * 2.6
    yy = nt.nodes.new("ShaderNodeMath"); yy.operation = "MULTIPLY"; yy.inputs[1].default_value = schaal
    mp = nt.nodes.new("ShaderNodeCombineXYZ")
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    nt.links.new(sep.outputs["X"], hoek.inputs[0])
    nt.links.new(hoek.outputs[0], co.inputs[0]); nt.links.new(hoek.outputs[0], si.inputs[0])
    nt.links.new(co.outputs[0], cr_.inputs[0]); nt.links.new(si.outputs[0], sr_.inputs[0])
    nt.links.new(sep.outputs["Z"], zz.inputs[0]); nt.links.new(sep.outputs["Y"], yy.inputs[0])
    nt.links.new(cr_.outputs[0], mp.inputs["X"]); nt.links.new(sr_.outputs[0], mp.inputs["Y"])
    nt.links.new(zz.outputs[0], mp.inputs["Z"])
    ns = nt.nodes.new("ShaderNodeTexNoise"); ns.noise_dimensions = "4D"
    nt.links.new(yy.outputs[0], ns.inputs["W"])
    ns.inputs["Scale"].default_value = 1.4; ns.inputs["Detail"].default_value = 3
    cr = nt.nodes.new("ShaderNodeValToRGB")
    cr.color_ramp.elements[0].position = 0.42; cr.color_ramp.elements[0].color = (*g.hex2(donker), 1)
    cr.color_ramp.elements[1].position = 0.62; cr.color_ramp.elements[1].color = (*g.hex2(licht), 1)
    bm = nt.nodes.new("ShaderNodeBump"); bm.inputs["Strength"].default_value = 0.25
    nt.links.new(mp.outputs["Vector"], ns.inputs["Vector"])
    nt.links.new(ns.outputs["Fac"], cr.inputs["Fac"])
    nt.links.new(cr.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(ns.outputs["Fac"], bm.inputs["Height"])
    nt.links.new(bm.outputs["Normal"], b.inputs["Normal"])
    return m


PRUIM = aardemat("pruim", "35203c", "4e3158")
PRUIM_L = g.mat("pruim_l", "5e3d68", rough=0.8, spec=0.2)
PRUIM_D = g.mat("pruim_d", "2a1832", rough=0.9, spec=0.1)
STEEN = g.mat("steen", "7a5d86", rough=0.6, spec=0.3)
GRAS = g.mat("gras", "5bbf4a", rough=0.95, spec=0.03)
GRAS_D = g.mat("gras_d", "3b8f3a", rough=0.95, spec=0.03)
GOUD = g.mat("goud", "goud", rough=0.18, spec=0.9, metaal=0.85, emis=0.06)
GOUD_D = g.mat("goud_d", "goud_d", rough=0.3, spec=0.7, metaal=0.8)
HOUT = g.mat("hout", "8a4b2a", rough=0.7, spec=0.2)
HOUT_D = g.mat("hout_d", "5a2e1c", rough=0.75)
VLAM = g.mat("vlam", "ffb347", emis=9.0)
VLAM_K = g.mat("vlamkern", "fff1b0", emis=14.0)
ROBIJN = g.mat("robijn", "rood", rough=0.08, spec=1.0, emis=0.4)
SAFIER = g.mat("safier", "4fa3ff", rough=0.08, spec=1.0, emis=0.4)
WORTEL = g.mat("wortel", "c9a27a", rough=0.8)
BLOEM = g.mat("bloem", "ffd84a", rough=0.5, emis=0.2)
BLOEM_R = g.mat("bloemr", "f08a9a", rough=0.5, emis=0.2)

# ---------- de aarde: een plaat met de voorkant op y = 0 ----------
aarde = blok("aarde", ((X0 + X1) / 2, 1.5, (ONDER - 1 + MAAIVELD) / 2), (X1 - X0, 3.0, MAAIVELD - ONDER + 1), PRUIM)

# schatkamer: boog (cilinder) plus vierkant onderstuk; achterwand blijft staan op y = 1.4
KX0, KX1, KVL, KTOP = -3.1, 3.1, 0.0, 2.75
kamer_b = blok("kamer_gat", (0, 0.2, (KVL + 1.4) / 2), (KX1 - KX0, 2.4, 1.4 - KVL))
uithollen(aarde, kamer_b)
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1.0, depth=2.4, location=(0, 0.2, 1.4), rotation=(math.radians(90), 0, 0))
boog = bpy.context.object; boog.scale = ((KX1 - KX0) / 2, (KTOP - 1.4), 1)
uithollen(aarde, boog)
# gang naar links, één rij hoog, met een schacht omhoog naar het gras
gang = blok("gang_gat", ((-11.8 + KX0) / 2, 0.2, GANG_TOP / 2), (KX0 - (-11.8) + 0.6, 2.4, GANG_TOP))
uithollen(aarde, gang)
schacht = blok("schacht_gat", (-11.0, 0.2, 2.0), (1.2, 2.4, 3.2))
uithollen(aarde, schacht)
# gang naar rechts, met een kleine voorraadkamer
# loopt door tot voorbij de rand: het rustige stuk (kolom 13 en 14) is een gang die herhaalt
gang_r = blok("gangr_gat", ((KX1 + X1 + 1) / 2, 0.2, GANG_TOP / 2), (X1 + 1 - KX1 + 0.6, 2.4, GANG_TOP))
uithollen(aarde, gang_r)
# twee kleine kamers boven de gang (in het spel: klik in de aarde boven de gang; later woont er iemand)
# Daan (proef 13 nov): een gegraven stuk van meer kolommen is EEN kamer. Kolom 2 tot 4 een brede kamer
# (begin, midden, eind), kolom 11 een losse kamer. Midden is recht, zodat hij naadloos herhaalt.
KZ = 2.25; KH = 0.62
BREDE = (LINKS + 2.5 * KOL, LINKS + 4.5 * KOL)      # middens van de ronde einden
LOS = LINKS + 11.5 * KOL
KAMERS = [(BREDE[0], KZ), (LINKS + 3.5 * KOL, KZ), (BREDE[1], KZ), (LOS, KZ)]   # voor kiezels en vloer
def ovaal(kx):
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=1.0, depth=2.4, location=(kx, 0.2, KZ), rotation=(math.radians(90), 0, 0))
    kg = bpy.context.object; kg.scale = (0.85, KH, 1)
    return kg
for kx in (BREDE[0], BREDE[1], LOS):
    uithollen(aarde, ovaal(kx))
# recht stuk tussen de twee einden: zelfde hoogte als het ovaal in zijn midden, licht afgerond plafond
mid = blok("kamer_mid", ((BREDE[0] + BREDE[1]) / 2, 0.2, KZ), (BREDE[1] - BREDE[0], 2.4, 2 * KH))
uithollen(aarde, mid)
for o in (aarde,):
    afronden(o, 0.18, 4)
    bpy.context.view_layer.objects.active = o

# achterwand donkerder dan de voorkant, zodat de kamer diepte heeft
blok("achterwand", (0, 1.35, 1.2), (X1 - X0, 0.1, 4.0), PRUIM_L)

# ---------- lagen en stenen in de voorkant ----------
for i in range(70):
    x = random.uniform(X0, X1); z = random.uniform(ONDER, MAAIVELD - 0.25)
    # niet in de gaten
    if x > TEGEL_X - 0.3:
        continue   # rustig stuk: daar liggen dezelfde kiezels in elke kolom (hieronder)
    if (KX0 - 1.4 < x < KX1 + 1.4 and z < KTOP + 0.45) or (z < 1.7 and x < 12.6 and x > -12.2) or (-11.8 < x < -10.2) or any(abs(x - kx) < 1.05 and abs(z - kz) < 0.8 for kx, kz in KAMERS) or (BREDE[0] < x < BREDE[1] and abs(z - KZ) < 0.8):
        continue
    r = random.uniform(0.07, 0.2)
    bol("kiezel", (x, -0.02, z), (r * 1.3, r * 0.6, r), random.choice([STEEN, PRUIM_L, PRUIM_L]), 12)
for k in range(-1, 3):   # kolom 12 (half, voor de naad) tot 14, plus één voorbij de rand
    x0 = TEGEL_X + k * KOL
    for (dx, z, r, m) in [(0.35, 2.35, 0.15, STEEN), (1.2, 2.9, 0.1, PRUIM_L), (0.9, 1.85, 0.08, PRUIM_L)]:
        if x0 + dx < LOS + 0.85 + 0.3:
            continue   # niet in de kamer rechts boven de gang
        bol("kiezel", (x0 + dx, -0.02, z), (r * 1.3, r * 0.6, r), m, 12)
# een strook lichtere aarde net onder het gras
blok("toplaag", ((X0 + X1) / 2, -0.01, MAAIVELD - 0.18), (X1 - X0, 0.04, 0.12), PRUIM_L)

# ---------- gras bovenop ----------
# loopt ver naar achteren door, zodat het gras de rij 0 tot 8 helemaal vult (geen donkere band erboven)
grasplak = blok("gras", ((X0 + X1) / 2, 1.4, MAAIVELD + 0.09), (X1 - X0, 2.9, 0.22), GRAS_D)
afronden(grasplak, 0.08, 3)
# gat in het gras boven de schacht
uithollen(grasplak, blok("graspgat", (-11.0, 0.5, MAAIVELD), (1.2, 1.6, 1.0)))  # alleen vooraan open
GRAS_PATROON = [(random.uniform(0, KOL), random.uniform(-0.05, 0.55), random.uniform(0.12, 0.32),
                 random.uniform(-0.3, 0.3), random.uniform(-0.35, 0.35), random.random() < 0.5) for i in range(11)]
for k in range(-1, 3):   # rustig stuk: elke kolom hetzelfde gras
    for (dx, y, h, rx, ry, licht) in GRAS_PATROON:
        cil("spriet", (TEGEL_X + k * KOL + dx, y, MAAIVELD + 0.18 + h / 2), 0.05, h, GRAS if licht else GRAS_D,
            rot=(rx, ry, 0), verts=4, r2=0.0)
    for dx in (0.2, 0.65, 1.1, 1.55):
        cil("rand", (TEGEL_X + k * KOL + dx, -0.05, MAAIVELD - 0.02), 0.07, 0.16, GRAS_D, rot=(math.radians(180), 0, 0), verts=4, r2=0.0)
for i in range(160):
    x = random.uniform(X0, X1)
    if -11.7 < x < -10.3 or x > TEGEL_X - KOL:
        continue
    y = random.uniform(-0.05, 0.55)
    h = random.uniform(0.12, 0.32)
    cil("spriet", (x, y, MAAIVELD + 0.18 + h / 2), 0.05, h, random.choice([GRAS, GRAS_D]),
        rot=(random.uniform(-0.3, 0.3), random.uniform(-0.35, 0.35), 0), verts=4, r2=0.0)
# gras hangt over de rand naar voren
for i in range(60):
    x = random.uniform(X0, X1)
    if -11.7 < x < -10.3 or x > TEGEL_X - KOL:
        continue
    cil("rand", (x, -0.05, MAAIVELD - 0.02), 0.07, 0.16, GRAS_D, rot=(math.radians(180), 0, 0), verts=4, r2=0.0)
for x, m in [(-6.3, BLOEM), (-4.1, BLOEM_R), (4.6, BLOEM), (7.9, BLOEM_R), (-8.4, BLOEM_R), (5.9, BLOEM)]:
    cil("steel", (x, 0.1, MAAIVELD + 0.38), 0.025, 0.4, GRAS_D, verts=6)
    bol("bloem", (x, 0.1, MAAIVELD + 0.6), (0.11, 0.11, 0.08), m, 12)
# wortels die door het plafond van de gang hangen
for x in (-8.6, -3.9, 6.2, 8.4):
    for k in range(3):
        cil("wortel", (x + k * 0.12 - 0.12, -0.05 + k * 0.1, GANG_TOP - 0.16 - k * 0.05), 0.035, 0.35 + 0.1 * k, WORTEL,
            rot=(0, random.uniform(-0.3, 0.3), 0), verts=6, r2=0.008)

# ---------- vloer van kamer en gangen ----------
VLOER = g.mat("vloer", "8a5a8e", rough=0.8, spec=0.2)
vloer = blok("vloer", ((X0 + X1) / 2, 0.7, -0.03), (X1 - X0, 1.5, 0.1), VLOER)

# ---------- de schat: een gouden berg rechts in de kamer ----------
mb = bpy.data.metaballs.new("berg"); mb.resolution = 0.06; mb.render_resolution = 0.03
berg = bpy.data.objects.new("berg", mb); sc.collection.objects.link(berg)
for (x, y, z, r) in [(1.5, 0.75, -0.25, 1.05), (2.25, 0.85, -0.3, 0.85), (0.4, 0.7, -0.45, 0.9), (1.7, 0.9, 0.1, 0.65)]:
    e = mb.elements.new(); e.co = (x, y, z); e.radius = r
berg.data.materials.append(GOUD_D)
# losse munten op en rond de berg
for i in range(90):
    a = random.uniform(0, math.pi); rr = random.uniform(0.2, 1.25)
    x = 1.55 + rr * math.cos(a) * 1.3; z = max(0.03, 0.75 - rr * 0.62 + random.uniform(-0.05, 0.05))
    y = random.uniform(0.25, 1.0)
    cil("munt", (x, y, z), 0.13, 0.035, GOUD, rot=(random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9), 0), verts=20)
for i in range(14):   # munten die over de vloer gerold zijn
    x = random.uniform(-2.6, 3.0); y = random.uniform(0.1, 0.9)
    cil("munt_vloer", (x, y, 0.02), 0.12, 0.03, GOUD, verts=20)
bol("robijn", (1.15, 0.35, 0.62), (0.12, 0.1, 0.14), ROBIJN, 8)
bol("safier", (2.3, 0.4, 0.5), (0.1, 0.08, 0.12), SAFIER, 8)
# een beker bovenop de berg
cil("beker_voet", (1.75, 0.7, 0.92), 0.12, 0.05, GOUD, verts=24)
cil("beker_steel", (1.75, 0.7, 1.02), 0.04, 0.18, GOUD, verts=16)
cil("beker_kom", (1.75, 0.7, 1.22), 0.1, 0.24, GOUD, verts=24, r2=0.2)

# achterwand van de schatkamer een trede lichter en warmer, met een gloed achter Gloop:
# hij moet het lichtste vlak van de strook zijn (frisse kijker ronde 1: "figuur te klein voor de drukke strook")
KAMERWAND = g.mat("kamerwand", "7a4a78", rough=0.8, spec=0.15)
blok("kamerwand", (0, 1.3, 1.3), (KX1 - KX0, 0.05, 2.9), KAMERWAND)
gg = bpy.data.lights.new("gloopgloed", "POINT"); gg.color = (1.0, 0.8, 0.55); gg.energy = 90; gg.shadow_soft_size = 1.0
ggo = bpy.data.objects.new("gloopgloed", gg); ggo.location = (-0.3, 1.15, 1.2); sc.collection.objects.link(ggo)

# de berg geeft zelf een warme gloed op de wand (dat is de sfeer: goud dat licht geeft)
gd = bpy.data.lights.new("goudgloed", "POINT"); gd.color = (1.0, 0.75, 0.3); gd.energy = 220; gd.shadow_soft_size = 0.8
go = bpy.data.objects.new("goudgloed", gd); go.location = (2.0, 0.2, 1.3); sc.collection.objects.link(go)

# ladder in de schacht naar het gras
for kant in (-0.35, 0.35):
    cil("ladderpaal", (-11.0 + kant, 0.6, 1.6), 0.05, 3.4, HOUT, verts=8)
for k in range(8):
    cil("sport", (-11.0, 0.6, 0.25 + k * 0.4), 0.035, 0.7, HOUT_D, rot=(0, math.radians(90), 0), verts=8)

# ---------- kist links in de kamer, open, goud puilt eruit ----------
kist = blok("kist", (-2.25, 0.75, 0.32), (0.95, 0.6, 0.62), HOUT); afronden(kist, 0.05, 2)
blok("kistband", (-2.25, 0.44, 0.32), (0.98, 0.03, 0.12), GOUD_D)
deksel = blok("deksel", (-2.25, 1.05, 0.88), (0.95, 0.12, 0.55), HOUT_D, rot=(math.radians(-25), 0, 0)); afronden(deksel, 0.04, 2)
for i in range(10):
    cil("kistmunt", (-2.25 + random.uniform(-0.38, 0.38), 0.7 + random.uniform(-0.15, 0.15), 0.66 + random.uniform(0, 0.08)),
        0.12, 0.03, GOUD, rot=(random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6), 0), verts=20)


# ---------- fakkels met echt warm licht ----------
def fakkel(x, z, kracht=160):
    cil("steel", (x, 1.0, z - 0.25), 0.05, 0.55, HOUT_D, rot=(math.radians(-18), 0, 0), verts=8)
    cil("kop", (x, 0.92, z + 0.05), 0.09, 0.12, HOUT, verts=10)
    bol("vlam", (x, 0.9, z + 0.24), (0.14, 0.11, 0.26), VLAM, 12)
    bol("vlamkern", (x, 0.85, z + 0.2), (0.06, 0.05, 0.1), VLAM_K, 10)
    d = bpy.data.lights.new("fakkellicht", "POINT"); d.color = (1.0, 0.6, 0.28); d.energy = kracht; d.shadow_soft_size = 0.15
    o = bpy.data.objects.new("fakkellicht", d); o.location = (x, 0.5, z + 0.35); sc.collection.objects.link(o)


fakkel(-2.9, 1.65)
fakkel(2.9, 1.65)
fakkel(-7.2, 0.95, 90)
fakkel(5.0, 0.95, 90)   # verder van het rustige stuk rechts, zodat dat egaal licht krijgt
# Daan: geen fakkel hoog in elke kamer meer (die vlam las als pupil: drie kommen werden drie ogen).
# Brede kamer: een fakkel laag op de linkerwand, een houten stut in elk middenstuk, een kistje in het eind.
blok("kamervloer", ((BREDE[0] + BREDE[1]) / 2, 0.7, KZ - 0.6), (BREDE[1] - BREDE[0] + 1.3, 1.4, 0.06), VLOER)
blok("kamervloer", (LOS, 0.7, KZ - 0.6), (1.3, 1.4, 0.06), VLOER)
fakkel(BREDE[0] - 0.45, KZ - 0.3, 25)
HOUT = g.mat("stut", "8a5a3c", rough=0.7)
xm = LINKS + 3.5 * KOL
MIDDEN = os.environ.get("HOL_MIDDEN", "a")   # a: stut met schoren, b: houweel en tonnetje (afwisselen in het spel)
if MIDDEN == "a":
    for dx in (-0.55, 0.55):
        blok("stut", (xm + dx, 0.5, KZ - 0.05), (0.16, 0.16, 2 * KH - 0.1), HOUT)
    blok("stut", (xm, 0.5, KZ + KH - 0.12), (1.45, 0.18, 0.16), HOUT)
    for dx, a in ((-0.38, 45), (0.38, -45)):
        blok("stut", (xm + dx, 0.5, KZ + KH - 0.3), (0.42, 0.12, 0.1), HOUT, rot=(0, math.radians(a), 0))
else:
    STAAL = g.mat("houweel", "b8b4c8", rough=0.35, spec=0.6, metaal=0.6)
    blok("houweelsteel", (xm - 0.25, 0.5, KZ - 0.2), (0.07, 0.07, 0.75), HOUT, rot=(0, math.radians(-18), 0))
    blok("houweelkop", (xm - 0.14, 0.5, KZ + 0.15), (0.5, 0.07, 0.08), STAAL, rot=(0, math.radians(-8), 0))
    cil("ton", (xm + 0.35, 0.5, KZ - 0.36), 0.2, 0.42, HOUT, verts=20)
    for dz in (-0.12, 0.12):
        cil("tonband", (xm + 0.35, 0.5, KZ - 0.36 + dz), 0.21, 0.04, g.mat("band", "d9a441", rough=0.4, spec=0.5), verts=20)
# zacht licht over de hele lengte van de brede kamer (licht hoort bij de kamer, niet bij een cel)
kl = bpy.data.lights.new("kamerlicht", "AREA"); kl.shape = "RECTANGLE"; kl.size = BREDE[1] - BREDE[0] + 3.0; kl.size_y = 1.0
kl.color = (1.0, 0.78, 0.6); kl.energy = 120
klo = bpy.data.objects.new("kamerlicht", kl); klo.location = ((BREDE[0] + BREDE[1]) / 2, 0.05, KZ)
klo.rotation_euler = (math.radians(90), 0, 0)   
sc.collection.objects.link(klo)   # kijkt naar achteren: licht de kamer, niet de voorkant van de aarde
blok("kistje", (BREDE[1] + 0.15, 0.45, KZ - 0.36), (0.5, 0.36, 0.38), HOUT)
blok("kistje", (BREDE[1] + 0.15, 0.45, KZ - 0.2), (0.52, 0.38, 0.05), g.mat("band", "d9a441", rough=0.4, spec=0.5))
# losse kamer: twee lichtgevende paddenstoeltjes op de vloer, zacht, laag (geen pupil)
for dx, s in ((-0.35, 1.0), (-0.12, 0.7)):
    cil("steel", (LOS + dx, 0.6, KZ - 0.48), 0.035 * s, 0.18 * s, g.mat("steel", "efe4d8", rough=0.6))
    bol("hoedje", (LOS + dx, 0.6, KZ - 0.39 + 0.05 * s), (0.11 * s, 0.11 * s, 0.06 * s), g.mat("zwam", "7fe3d0", rough=0.5, emis=1.2), 16)
zl = bpy.data.lights.new("zwamlicht", "POINT"); zl.color = (0.55, 1.0, 0.9); zl.energy = 25; zl.shadow_soft_size = 0.3
ll = bpy.data.lights.new("loslicht", "AREA"); ll.size = 1.6; ll.color = (1.0, 0.8, 0.7); ll.energy = 30
llo = bpy.data.objects.new("loslicht", ll); llo.location = (LOS, 0.05, KZ); llo.rotation_euler = (math.radians(90), 0, 0); sc.collection.objects.link(llo)
zlo = bpy.data.objects.new("zwamlicht", zl); zlo.location = (LOS - 0.2, 0.2, KZ - 0.2); sc.collection.objects.link(zlo)

# stekelput in de linker gang (zit in het spel: hol.gd, vallen = "stekelput")
PUT_X = LINKS + 4.5 * KOL   # midden van kolom 4 (spelpixel 64 tot 80), zoals hol.gd een put in één kolom tekent
uithollen(vloer, blok("put_gat_v", (PUT_X, 0.4, -0.2), (1.55, 2.0, 0.6)))
uithollen(aarde, blok("put_gat_a", (PUT_X, 0.4, -0.25), (1.55, 2.0, 0.7)))
blok("put_bodem", (PUT_X, 0.7, -0.52), (1.55, 1.5, 0.06), PRUIM_D)
STAAL = g.mat("staal", "staal", rough=0.25, spec=0.8, metaal=0.9)
# Ronde 4: de stekels steken boven de vloer uit (zoals hol.gd de put tekent: 8 spelpixels vanaf de vloer),
# want onder de vloer is maar 2,6 spelpixel beeld over. Lichter staal met een glimpje, zodat ze op 120 px lezen.
STAAL_L = g.mat("staal_l", "d8dce8", rough=0.2, spec=0.9, metaal=0.7, emis=0.15)
for i in range(6):
    for j in range(3):
        hoog = 0.62 if (i + j) % 2 == 0 else 0.5
        cil("stekel", (PUT_X - 0.6 + i * 0.24, 0.15 + j * 0.38, -0.25 + hoog / 2), 0.07, hoog, STAAL_L, verts=8, r2=0.0)
# buit van een gevallen held: een paar munten en zijn helm aan de rand
for dx in (-0.85, -0.7, 0.75):
    cil("buit", (PUT_X + dx, 0.5, 0.04), 0.12, 0.03, GOUD, verts=20, rot=(0.2, 0.3, 0))
bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=(PUT_X + 0.95, 0.55, 0.0))
helm = bpy.context.object; helm.scale = (0.24, 0.22, 0.2); bpy.ops.object.shade_smooth(); helm.data.materials.append(STAAL)
helm.rotation_euler = (0, math.radians(25), 0)

# ingang: fakkel op een paal naast de schacht, met een boogje van stenen
cil("ingangpaal", (-10.0, 0.35, MAAIVELD + 0.45), 0.05, 0.9, HOUT_D, verts=8)
cil("ingangkop", (-10.0, 0.35, MAAIVELD + 0.93), 0.09, 0.12, HOUT, verts=10)
bol("ingangvlam", (-10.0, 0.33, MAAIVELD + 1.1), (0.14, 0.11, 0.26), VLAM, 12)
bol("ingangkern", (-10.0, 0.28, MAAIVELD + 1.06), (0.06, 0.05, 0.1), VLAM_K, 10)
il = bpy.data.lights.new("ingangslicht", "POINT"); il.color = (1.0, 0.6, 0.28); il.energy = 60; il.shadow_soft_size = 0.15
ilo = bpy.data.objects.new("ingangslicht", il); ilo.location = (-10.0, 0.0, MAAIVELD + 1.15); sc.collection.objects.link(ilo)
for k in range(9):
    a2 = math.radians(180 - k * 22.5)
    bol("boogsteen", (-11.0 + 0.78 * math.cos(a2), -0.02, MAAIVELD - 0.05 + 0.3 * math.sin(a2)), (0.16, 0.14, 0.13), STEEN, 10)

# spinrag in de rechter gang (plat, bovenin, zoals in stijl.md)
WEB = g.mat("web", "e8e0f0", rough=0.6, emis=0.3)
for k in range(5):
    a = math.radians(-90 + k * 22)
    cil("draad", (8.9 + 0.25 * math.cos(a), 0.4, GANG_TOP - 0.18 + 0.25 * math.sin(a) * 0.6), 0.008, 0.55, WEB,
        rot=(0, a + math.pi / 2, 0), verts=4)
bol("spin", (8.9, 0.4, GANG_TOP - 0.56), (0.07, 0.06, 0.07), PRUIM_D, 10)

# egaal licht op het rustige stuk rechts (kolom 13 en 14): een lange lamp die voorbij beide randen loopt, zodat
# het licht daar niet verloopt in x en de tegels naadloos naast elkaar passen. De fakkels vallen er zwak op.
tl = bpy.data.lights.new("tegellicht", "AREA"); tl.shape = "RECTANGLE"; tl.size = 10.0; tl.size_y = 3.0
tl.color = (1.0, 0.82, 0.86); tl.energy = TEGEL_LICHT
tlo = bpy.data.objects.new("tegellicht", tl); tlo.location = (TEGEL_X + KOL + 1.0, -3.0, 4.6)
tlo.rotation_euler = (math.radians(52), 0, 0); sc.collection.objects.link(tlo)

# ---------- Gloop van Daan erin (gloop.py ongewijzigd, alleen het model) ----------
voor = set(bpy.data.objects)
bron = open(os.path.join(HIER, "gloop.py"), encoding="utf-8").read()
begin = bron.index("# ---------- lijf")
eind = bron.index("# ---------- camera")
stuk = bron[begin:eind]
ns = {"bpy": bpy, "g": g, "math": math, "sc": sc, "VERSIE": GLOOP_V, "HOEDEN": HOEDEN, "sys": sys, "os": os}
# de hulpjes bol en kegel uit gloop.py
hulp = bron[bron.index("def bol("):begin]
exec(hulp, ns)
exec(stuk, ns)
nieuw = [o for o in bpy.data.objects if o not in voor]
GLOOP_X, GLOOP_Y, GLOOP_S, GLOOP_Z = -0.25, 0.6, 0.95, 0.18
for o in nieuw:
    if getattr(o, "is_shadow_catcher", False) or o.name.startswith("Plane"):
        bpy.data.objects.remove(o, do_unlink=True)
        continue
    o.name = "gloop_" + o.name   # zodat de pijplijn een laag zonder Gloop kan maken (HOL_VERBERG ["gloop"])
    if o.parent is None:
        o.location = Vector((o.location.x * GLOOP_S + GLOOP_X, o.location.y * GLOOP_S + GLOOP_Y, o.location.z * GLOOP_S + GLOOP_Z))
        o.scale = o.scale * GLOOP_S

# ---------- helden van Daan (held.py): het verhaal in beeld ----------
# Frisse kijker ronde 2: "er gebeurt niets". Het spel is: helden komen binnen en vallen in de put. Een ridder
# loopt vanaf de ladder naar de put, een heks valt er net in. Alles heet held_..., dus HOL_VERBERG ["held"]
# geeft het hol zonder helden (het spel tekent ze zelf).
if os.environ.get("HOL_HELDEN", "1") == "1":
    import held
    held.bouw("ridder", "stap1", plek=(LINKS + 2.5 * KOL, 0.45, 0.0), draai=40, schaal=0.78, gloed=25, rand=40)
    held.bouw("heks", "vallen", plek=(PUT_X - 0.25, 0.5, -0.05), draai=20, schaal=0.68, gloed=25, rand=40)

# ---------- camera en licht (gedeeld) ----------
g.camera(hoogte_midden=CAM_MIDDEN, schaal=BREED)
g.licht()
# Het gedeelde licht is gezet voor Gloop alleen. In het hol zat "koel" in de achterwand en gaf
# "boven" een vlek op het gras. Zelfde richting en kleur, alleen verplaatst (Gloop krijgt evenveel licht).
for o in sc.objects:
    if o.name == "boven":
        o.location.z = 9.0; o.data.energy *= 2.25
    if o.name == "koel":
        o.location = (-2.6, 1.05, 2.3); o.data.size = 1.2; o.data.energy *= 0.6
for o in sc.objects:
    if o.type == "LIGHT":
        o.visible_camera = False   # de lampen zelf niet in beeld
g.render(uit, W, H, SAMPLES, doorzichtig=True)
print("klaar", uit)
