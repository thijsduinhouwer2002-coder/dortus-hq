"""Steam-header v2 van Hats of the Fallen (Mila, 27 nov 2026, issue #30).

Draai:  <venv>/bin/python header_v2.py <uit.png> <breedte> <hoogte> <samples>
  daarna: python3 samenstellen.py  (lucht, heuvels, taakbalk en ondertitel eromheen)

Het idee (keuzes van Sanne in #30): de look van het spel zoals hij nu blind wint, niet de oude losse render.
Bovenaan een rustig bureaublad (lucht en heuvels, getekend in samenstellen.py), op de graslijn begint de
kelder: een doorsnede van de grond zoals in het spel. Rechts de schatkamer met metselwerk, Gloop met zijn
hoedentoren op het goud en zijn lichtring. Een held valt kop eerst door een gat in het gras de kamer in;
zijn rode pet vliegt los in de lucht. Links een gang met een fakkel en een held die nog niets weet.
Alles uit code in Blender, geen AI-beeld, geen gekocht pakket. Gloop en de helden komen uit Daans
gloop.py, held.py en hoeden.py (ingelezen, ongewijzigd). Titel in Lilita One (SIL OFL).

Beeld: 20 eenheden breed, 1 eenheid = 46 px op 920. Lucht boven z = MV is doorzichtig.
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
FONT = os.path.join(HIER, "..", "capsule-3d", "LilitaOne-Regular.ttf")
def E(n, d):
    return float(os.environ.get("HV2_" + n, d))
random.seed(5)
g.leeg()
sc = bpy.context.scene

BREED = 20.0
HOOG = BREED * H / W                 # 9,35
ZTOP = E("ZTOP", "8.35"); ZBOT = ZTOP - HOOG
MV = E("MV", "4.72")                 # graslijn (maaiveld)
KX0, KX1, KTOP = 1.0, 9.9, E("KTOP", "4.15")   # schatkamer
KRECHT = 2.4                          # tot hier recht, daarboven de boog
GX = E("GX", "6.55")                   # Gloop
SX0, SX1 = E("SX0", "1.25"), E("SX1", "3.05")   # gat waar de held door valt (v3: breder en donker, Daan #236 M2)
GANGTOP = E("GANGTOP", "2.45")   # v3: gang hoger, minder lege aarde links midden (Daan #236 kan)

# ---------- hulpjes ----------
def kies(o, m):
    o.data.materials.clear(); o.data.materials.append(m); return o
def blok(naam, loc, maat, m=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.name = naam; o.scale = maat
    bpy.ops.object.transform_apply(scale=True)
    if m: kies(o, m)
    return o
def bol(naam, loc, schaal, m, segs=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc)
    o = bpy.context.object; o.name = naam; o.scale = schaal; bpy.ops.object.shade_smooth(); return kies(o, m)
def cil(naam, loc, r, d, m, rot=(0, 0, 0), verts=32, r2=None):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); return kies(o, m)
def hol(doel, gat):
    md = doel.modifiers.new("gat", "BOOLEAN"); md.operation = "DIFFERENCE"; md.object = gat; md.solver = "EXACT"
    bpy.context.view_layer.objects.active = doel; bpy.ops.object.modifier_apply(modifier=md.name)
    bpy.data.objects.remove(gat, do_unlink=True)

# v4: het gat is geen rechthoek meer maar een rafelige trechter (Daan #243 kan 1). Eigen dobbelsteen,
# zodat de rest van het beeld (kiezels, sprieten) precies blijft zoals in v3.
RG = random.Random(11)
GAT_N = 22
def _gatrand(z0, z1):
    """Linker- en rechterkant van het gat van z0 tot z1: licht golvend, bovenaan rond uitlopend (geen hoeken)."""
    zs = [z0 + (z1 - z0) * i / GAT_N for i in range(GAT_N + 1)]
    links, rechts = [], []
    for z in zs:
        t = max(0.0, min(1.0, (z - (MV - 0.5)) / 0.7))
        flare = 0.38 * (1 - math.cos(t * math.pi / 2)) ** 0.8 if z < MV + 0.2 else 0.38
        links.append((SX0 - flare + RG.uniform(-0.07, 0.07) * (1 - t), z))
        rechts.append((SX1 + flare + RG.uniform(-0.07, 0.07) * (1 - t), z))
    return links, rechts
def boog_z(x):
    cx, hw = (KX0 + KX1) / 2, (KX1 - KX0) / 2
    u = min(1.0, abs(x - cx) / hw)
    return KRECHT + (KTOP - KRECHT) * math.sqrt(1 - u * u)
GAT_L, GAT_R = _gatrand(KRECHT, MV + 1.0)
def prisma(naam, omtrek, y0, y1, m=None):
    """Omtrek (x, z) als dicht blok van y0 tot y1 (manifold, voor de boolean)."""
    import bmesh
    me = bpy.data.meshes.new(naam); o = bpy.data.objects.new(naam, me); sc.collection.objects.link(o)
    bm = bmesh.new()
    voor = [bm.verts.new((x, y0, z)) for x, z in omtrek]
    f = bm.faces.new(voor)
    r = bmesh.ops.extrude_face_region(bm, geom=[f])
    for v in [e for e in r["geom"] if isinstance(e, bmesh.types.BMVert)]:
        v.co.y = y1
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bm.to_mesh(me); bm.free()
    if m: kies(o, m)
    return o
def gatomtrek(met_boog=False):
    """Omtrek tegen de klok: rechterkant omhoog, linkerkant omlaag. met_boog: onderkant volgt de boog van de kamer."""
    if not met_boog:
        return GAT_R + GAT_L[::-1]
    l = [(x, z) for x, z in GAT_L if z >= boog_z(x) + 0.05]
    r = [(x, z) for x, z in GAT_R if z >= boog_z(x) + 0.05]
    xa, xb = l[0][0], r[0][0]
    onder = [(xa + (xb - xa) * i / 12, boog_z(xa + (xb - xa) * i / 12) - 0.12) for i in range(1, 12)]
    return [(xa, boog_z(xa) - 0.12)] + onder + [(xb, boog_z(xb) - 0.12)] + r + l[::-1]

def aardemat(naam, donker, licht, schaal=0.9, bump=0.3):
    m = g.mat(naam, donker, rough=0.88, spec=0.12)
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    ns = nt.nodes.new("ShaderNodeTexNoise"); ns.inputs["Scale"].default_value = schaal; ns.inputs["Detail"].default_value = 4
    cr = nt.nodes.new("ShaderNodeValToRGB")
    cr.color_ramp.elements[0].position = 0.42; cr.color_ramp.elements[0].color = (*g.hex2(donker), 1)
    cr.color_ramp.elements[1].position = 0.62; cr.color_ramp.elements[1].color = (*g.hex2(licht), 1)
    bm = nt.nodes.new("ShaderNodeBump"); bm.inputs["Strength"].default_value = bump
    nt.links.new(ns.outputs["Fac"], cr.inputs["Fac"]); nt.links.new(cr.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(ns.outputs["Fac"], bm.inputs["Height"]); nt.links.new(bm.outputs["Normal"], b.inputs["Normal"])
    return m

def steenmat(naam, k1, k2, voeg, schaal=1.0, rij=0.5):
    """Metselwerk zoals de achterwand van de kamer in het spel: warme zandsteen met donkere voegen."""
    m = g.mat(naam, k1, rough=0.8, spec=0.15)
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    tc = nt.nodes.new("ShaderNodeTexCoord")
    br = nt.nodes.new("ShaderNodeTexBrick")
    br.inputs["Color1"].default_value = (*g.hex2(k1), 1); br.inputs["Color2"].default_value = (*g.hex2(k2), 1)
    br.inputs["Mortar"].default_value = (*g.hex2(voeg), 1)
    br.inputs["Scale"].default_value = schaal; br.inputs["Mortar Size"].default_value = 0.035
    br.inputs["Brick Width"].default_value = 1.0; br.inputs["Row Height"].default_value = rij
    br.inputs["Mortar Smooth"].default_value = 0.3; br.offset = 0.5
    mp = nt.nodes.new("ShaderNodeMapping"); mp.inputs["Rotation"].default_value = (math.radians(90), 0, 0)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"]); nt.links.new(mp.outputs["Vector"], br.inputs["Vector"])
    nt.links.new(br.outputs["Color"], b.inputs["Base Color"])
    bm = nt.nodes.new("ShaderNodeBump"); bm.inputs["Strength"].default_value = 0.5; bm.invert = True
    nt.links.new(br.outputs["Fac"], bm.inputs["Height"]); nt.links.new(bm.outputs["Normal"], b.inputs["Normal"])
    return m

# Kleuren: feller dan het spel en meer verschil (Mila-doel): aarde warm terracotta, kamer zandsteen, Gloop mint,
# helden blauw en rood, goud geel. Geen bruin-oranje met veel muur: de muur is licht metselwerk.
AARDE = aardemat("aarde", os.environ.get("C_AARDE1", "8c4c35"), os.environ.get("C_AARDE2", "a9674c"))
AARDE_SNIJ = g.mat("aarde_snij", "a5654a", rough=0.9, spec=0.1, emis=0.25)
KAMERWAND = steenmat("kamerwand", os.environ.get("C_STEEN1", "eab27c"), os.environ.get("C_STEEN2", "d99862"), "8a5640", 1.1)
GANGWAND = steenmat("gangwand", "c99a86", "b88a78", "6e4a44", 1.3)
VLOER = g.mat("vloer", "d9a27c", rough=0.8, spec=0.2)
STEEN = g.mat("steen", "e0b49a", rough=0.6, spec=0.3)
STEEN_D = g.mat("steen_d", "7d4a38", rough=0.8)
GRAS = g.mat("gras", "74dc52", rough=0.95, spec=0.03)
GRAS_D = g.mat("gras_d", "3e9a3c", rough=0.95, spec=0.03)
GOUD = g.mat("goud", "goud", rough=0.18, spec=0.9, metaal=0.85, emis=0.08)
GOUD_D = g.mat("goud_d", "goud_d", rough=0.3, spec=0.7, metaal=0.8)
HOUT = g.mat("hout", "8a4b2a", rough=0.7, spec=0.2)
DOEK = g.mat("doek", "3a2418", rough=0.9)
IJZER = g.mat("ijzer", "3b3640", rough=0.45, metaal=0.8)
WORTEL = g.mat("wortel", "6a3f2a", rough=0.8)
BOT = g.mat("bot", "f3e6cf", rough=0.5)
V_BUIT = g.mat("v_buit", "ff5a1f", emis=2.0); V_MID = g.mat("v_mid", "ff9b2a", emis=3.0); V_HART = g.mat("v_hart", "ffe27a", emis=4.0)
ROBIJN = g.mat("robijn", "rood", rough=0.08, spec=1.0, emis=0.4); SAFIER = g.mat("safier", "4fa3ff", rough=0.08, spec=1.0, emis=0.4)

# ---------- de grond: plaat met voorkant op y = 0 ----------
aarde = blok("aarde", (0, 1.5, (ZBOT - 1.5 + MV) / 2), (BREED + 8, 3.0, MV - ZBOT + 1.5), AARDE)
kamer = blok("kamer_gat", ((KX0 + KX1) / 2, 0.3, KRECHT / 2 - 0.5), (KX1 - KX0, 2.6, KRECHT + 1.0))
hol(aarde, kamer)
bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=1.0, depth=2.6, location=((KX0 + KX1) / 2, 0.3, KRECHT), rotation=(math.radians(90), 0, 0))
boog = bpy.context.object; boog.scale = ((KX1 - KX0) / 2, KTOP - KRECHT, 1); hol(aarde, boog)
gat = prisma("val_gat", gatomtrek(), -1.0, 1.6); hol(aarde, gat)
gang = blok("gang_gat", ((-12 + KX0 + 0.2) / 2, 0.3, GANGTOP / 2 - 0.5), (KX0 + 0.2 + 12, 2.6, GANGTOP + 1.0)); hol(aarde, gang)
bv = aarde.modifiers.new("rond", "BEVEL"); bv.width = 0.15; bv.segments = 4; bv.limit_method = "ANGLE"
# snijvlakken (binnenkant van de gaten) iets licht van zichzelf, zodat ze nooit zwart worden

# achterwanden: kamer licht metselwerk, gang koeler
w = blok("kamerwand", ((KX0 + KX1) / 2, 1.55, (KTOP + 0.2) / 2), (KX1 - KX0 + 0.4, 0.1, KTOP + 0.4), KAMERWAND)
blok("gangwand", ((-12 + KX0 + 0.4) / 2, 1.56, GANGTOP / 2), (KX0 + 12.4, 0.1, GANGTOP + 0.2), GANGWAND)
# v3: de schacht is donker van binnen, zodat je in één blik een gat ziet (Daan #236 M2)
SCHACHT = g.mat("schacht", "3a1c14", rough=0.95, spec=0.05)
# v4: de donkere achterkant volgt de rafelige rand en loopt onderaan mee met de boog (geen zwart vak, Daan #243 kan 1)
vw = [(x, z if z < MV + 0.06 else MV + 0.06) for x, z in gatomtrek(met_boog=True)]
prisma("valwand", vw, 1.40, 1.44, SCHACHT)
blok("vloer", (0, 0.8, -0.05), (BREED + 8, 1.6, 0.1), VLOER)

# stenen, botjes en wortels in de aarde (minder dingen dan v1: alleen in de lege aarde links onder de titel en tussen)
def vrij(x, z):
    if KX0 - 0.5 < x < KX1 + 0.5 and z < KTOP + 0.35: return False
    if SX0 - 0.4 < x < SX1 + 0.4: return False
    if z < GANGTOP + 0.35 and x < KX0 + 0.3: return False
    return z < MV - 0.35
for i in range(18):
    x = random.uniform(-9.8, 9.8); z = random.uniform(ZBOT + 0.2, MV - 0.3)
    if not vrij(x, z): continue
    r = random.uniform(0.09, 0.22)
    bol("kiezel", (x, -0.03, z), (r * 1.3, r * 0.6, r), random.choice([STEEN, STEEN, STEEN_D]), 12)
# een bot en een schedeltje in de aarde (er vielen er meer)
for x in (-7.8, -2.4, 0.2):
    for k in range(3):
        cil("wortel", (x + k * 0.12 - 0.12, -0.05 + k * 0.1, GANGTOP - 0.18 - k * 0.05), 0.04, 0.4 + 0.1 * k, WORTEL,
            rot=(0, random.uniform(-0.3, 0.3), 0), verts=6, r2=0.01)

# ---------- gras ----------
gp = blok("grasplak", (0, 1.4, MV + 0.1), (BREED + 8, 2.9, 0.24), GRAS_D)
hol(gp, prisma("gras_gat", gatomtrek(), -0.5, 1.45))
# v4: de verre rand van het gat is gras, met een paar sprieten: zo lees je een gat en geen zwart vak
for i in range(26):
    x = RG.uniform(SX0 - 0.3, SX1 + 0.3); h = RG.uniform(0.12, 0.26)
    cil("verspriet", (x, RG.uniform(1.5, 1.7), MV + 0.2 + h / 2), 0.055, h, RG.choice([GRAS, GRAS_D]),
        rot=(RG.uniform(-0.3, 0.3), RG.uniform(-0.35, 0.35), 0), verts=4, r2=0.0)
for i in range(14):   # en een paar die over de verre rand naar binnen hangen (rafelige bovenkant)
    x = RG.uniform(SX0 - 0.1, SX1 + 0.1); h = RG.uniform(0.12, 0.3)
    cil("hangachter", (x, 1.36, MV + 0.08 - h / 2), 0.05, h, RG.choice([GRAS, GRAS_D]),
        rot=(math.radians(180) + RG.uniform(-0.2, 0.2), RG.uniform(-0.4, 0.4), 0), verts=4, r2=0.0)
bl = gp.modifiers.new("rond", "BEVEL"); bl.width = 0.08; bl.segments = 3
for i in range(420):
    x = random.uniform(-10.5, 10.5)
    if SX0 - 0.36 < x < SX1 + 0.36: continue
    y = random.uniform(-0.08, 0.9); h = random.uniform(0.16, 0.4)
    cil("spriet", (x, y, MV + 0.2 + h / 2), 0.06, h, random.choice([GRAS, GRAS, GRAS_D]),
        rot=(random.uniform(-0.3, 0.3), random.uniform(-0.35, 0.35), 0), verts=4, r2=0.0)
for i in range(70):
    x = -10.4 + i * 0.3
    if SX0 - 0.42 < x < SX1 + 0.42: continue
    cil("rand", (x, -0.06, MV - 0.04), 0.09, 0.2, GRAS_D, rot=(math.radians(180), 0, 0), verts=4, r2=0.0)
# v3: rafelige graskant: sprieten hangen over de rand het gat in, en kluitjes vallen mee
for kant, xr in ((-1, SX0 - 0.3), (1, SX1 + 0.3)):   # v4: rand ligt verder naar buiten (trechter)
    for i in range(9):
        x = xr - kant * random.uniform(0.0, 0.3); h = random.uniform(0.2, 0.42)
        cil("hangspriet", (x, random.uniform(-0.15, 0.1), MV - h / 2 + 0.12), 0.05, h, random.choice([GRAS, GRAS_D]),
            rot=(math.radians(180) + random.uniform(-0.3, 0.3), kant * random.uniform(0.2, 0.6), 0), verts=4, r2=0.0)
    bol("graskant", (xr + kant * 0.05, -0.05, MV + 0.08), (0.2, 0.25, 0.12), GRAS_D, 14)
KLUIT = g.mat("kluit", "7a4430", rough=0.9); KLUIT_L = g.mat("kluit_l", "c07a50", rough=0.9)
# kluitjes vallen mee: licht op de donkere schacht, donker op het lichte metselwerk eronder
for (x, z, r, m, mg) in [(1.55, 4.3, 0.11, KLUIT_L, True), (2.8, 4.05, 0.09, KLUIT_L, False), (2.95, 3.75, 0.07, KLUIT_L, True),
                         (1.05, 3.05, 0.12, KLUIT, True), (3.35, 2.85, 0.1, KLUIT, False), (3.05, 2.2, 0.07, KLUIT, False),
                         (0.95, 2.3, 0.07, KLUIT, False)]:
    bol("kluit", (x, -0.6, z), (r * 1.25, r, r), m, 12)
    if mg:
        cil("kluitgras", (x + 0.03, -0.6, z + r + 0.05), 0.035, 0.16, GRAS, rot=(0.2, 0.35, 0), verts=4, r2=0.0)
# v4: rand van aarde en wortels binnen in het gat (Daan #243 kan 1): lichte kluiten langs beide wanden,
# zodat de rand rafelig is, en drie wortels die van boven het donker in hangen.
RAND_L = g.mat("rand_l", "b8704c", rough=0.9); RAND_D = g.mat("rand_d", "8e4e34", rough=0.9)
for kant, rand in ((-1, GAT_L), (1, GAT_R)):
    for x, z in rand:
        if z < boog_z(x) + 0.1 or z > MV - 0.05: continue
        r = RG.uniform(0.07, 0.13)
        bol("randkluit", (x - kant * RG.uniform(0.0, 0.06), RG.uniform(0.15, 0.9), z), (r * 1.1, r, r * 0.9),
            RG.choice([RAND_L, RAND_L, RAND_D]), 10)
WORTEL_L = g.mat("wortel_l", "b77a4e", rough=0.8)
for (x, l, sc_) in [(SX0 + 0.25, 0.55, 0.2), (SX0 + 1.05, 0.38, -0.25), (SX1 - 0.2, 0.62, -0.15)]:
    cil("gatwortel", (x, 0.2, MV - 0.05 - l / 2), 0.035, l, WORTEL_L, rot=(0, sc_, 0), verts=6, r2=0.008)
    cil("gatwortel2", (x + 0.08, 0.25, MV - 0.12 - l * 0.3), 0.02, l * 0.45, WORTEL_L, rot=(0, sc_ + 0.6, 0), verts=5, r2=0.005)
for x, k in [(-9.0, "ff6f91"), (-0.6, "ffd23a"), (4.2, "ff6f91"), (7.6, "ffffff"), (9.3, "ffd23a"), (3.4, "ffffff")]:
    cil("steel", (x, 0.15, MV + 0.45), 0.03, 0.5, GRAS_D, verts=6)
    bol("bloem", (x, 0.15, MV + 0.72), (0.14, 0.14, 0.1), g.mat("bl" + k, k, rough=0.6), 12)
    bol("hart", (x, 0.04, MV + 0.73), (0.06, 0.04, 0.05), g.mat("blh", "ffb020", rough=0.5), 10)

# ---------- fakkels ----------
def druppel(naam, loc, r, hoog, m, scheef=0.0):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=14, radius=1, location=(0, 0, 0))
    o = bpy.context.object; o.name = naam
    for v in o.data.vertices:
        if v.co.z > 0:
            t = v.co.z; k = (1 - t) ** 1.6
            v.co.x = v.co.x * k + scheef * t * t; v.co.y *= k; v.co.z = t * hoog
    o.scale = (r, r * 0.85, r); o.location = loc; o.visible_shadow = False
    bpy.ops.object.shade_smooth(); return kies(o, m)
def fakkel(x, z, y=1.4, kracht=220, groot=1.6):
    cil("steel", (x, y - 0.05, z - 0.2), 0.08, 0.6, HOUT, rot=(math.radians(-12), 0, 0), verts=10, r2=0.05)
    cil("kop", (x, y - 0.1, z + 0.12), 0.12 * groot / 1.2, 0.18, DOEK, verts=12, r2=0.14 * groot / 1.2)
    zv = z + 0.26
    druppel("vlam", (x, y - 0.12, zv + 0.12 * groot), 0.15 * groot, 2.3, V_BUIT, 0.05)
    druppel("vlammid", (x, y - 0.18, zv + 0.1 * groot), 0.11 * groot, 2.0, V_MID, 0.04)
    druppel("kern", (x, y - 0.24, zv + 0.06 * groot), 0.06 * groot, 1.7, V_HART, 0.02)
    d = bpy.data.lights.new("fakkellicht", "POINT"); d.color = (1.0, 0.62, 0.3); d.energy = kracht * E("FAKKEL", "1.0"); d.shadow_soft_size = 0.3
    l = bpy.data.objects.new("fakkellicht", d); l.location = (x, y - 0.7, zv + 0.5); sc.collection.objects.link(l)
fakkel(KX1 - 0.8, 2.2)
fakkel(-4.2, 1.45, kracht=190, groot=1.4)
# licht in het valgat, zodat de held en zijn laarzen niet in het donker hangen
lg_ = bpy.data.lights.new("gatlicht", "POINT"); lg_.color = (1.0, 0.92, 0.8); lg_.energy = E("GATLICHT", "260"); lg_.shadow_soft_size = 0.8
lgo_ = bpy.data.objects.new("gatlicht", lg_); lgo_.location = ((SX0 + SX1) / 2, -1.5, 3.9); sc.collection.objects.link(lgo_)

# ---------- schat ----------
bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=(GX + 0.4, 0.75, -0.35)); berg = bpy.context.object
berg.scale = (3.0, 0.75, 1.15); bpy.ops.object.shade_smooth(); kies(berg, GOUD_D)
def munt(loc, r=0.17, rx=None, ry=None):
    rx = random.uniform(-40, 40) if rx is None else rx; ry = random.uniform(-40, 40) if ry is None else ry
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=r, depth=0.05, location=loc,
                                        rotation=(math.radians(rx), math.radians(ry), random.uniform(0, 6)))
    o = bpy.context.object; o.name = "munt"; bpy.ops.object.shade_smooth(); kies(o, GOUD)
for i in range(260):
    a = random.uniform(0, 2 * math.pi); rr = math.sqrt(random.random())
    x = GX + 0.4 + 2.9 * rr * math.cos(a); y = 0.75 + 0.7 * rr * math.sin(a)
    hz = 1.15 * math.sqrt(max(0.0, 1 - ((x - GX - 0.4) / 3.0) ** 2 - ((y - 0.75) / 0.75) ** 2)) - 0.35
    if hz < 0.01: continue
    munt((x, y, hz + 0.02), random.uniform(0.13, 0.19))
for i in range(22):
    munt((random.uniform(KX0 + 0.5, KX1 - 0.3), random.uniform(-0.3, 0.4), 0.03), random.uniform(0.13, 0.18), random.uniform(-8, 8), random.uniform(-8, 8))
for (x, y, z, m) in [(GX - 2.0, 0.2, 0.2, ROBIJN), (GX + 2.6, 0.3, 0.3, SAFIER), (GX + 1.6, 0.5, 0.6, ROBIJN)]:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=0.17, location=(x, y, z)); e = bpy.context.object
    e.scale = (1, 1, 1.3); kies(e, m)
cil("beker", (GX + 2.3, 0.55, 0.62), 0.2, 0.42, GOUD, verts=32, r2=0.25)
cil("bekervoet", (GX + 2.3, 0.55, 0.32), 0.07, 0.3, GOUD, verts=16)

# ---------- Gloop (gloop.py, ongewijzigd ingelezen) ----------
voor = set(bpy.data.objects)
bron = open(os.path.join(MOD, "gloop.py"), encoding="utf-8").read()
begin = bron.index("# ---------- lijf"); eind = bron.index("# ---------- camera")
ns = {"bpy": bpy, "g": g, "math": math, "sc": sc, "VERSIE": 1, "HOEDEN": int(E("HOEDEN", "3")), "sys": sys, "os": os,
      "STAND": os.environ.get("GSTAND", "rust"), "PLUIM_KNAK": False}
exec(bron[bron.index("def bol("):begin], ns)
exec(bron[begin:eind], ns)
GS = E("GS", "2.2")
GZ = E("GZ", "0.72")
anker = bpy.data.objects.new("gloop_anker", None); sc.collection.objects.link(anker)
for o in [o for o in bpy.data.objects if o not in voor]:
    if getattr(o, "is_shadow_catcher", False) or o.name.startswith("Plane"):
        bpy.data.objects.remove(o, do_unlink=True); continue
    if o.parent is None and o is not anker:
        o.parent = anker
anker.location = (GX, 0.1, GZ); anker.scale = (GS, GS, GS)
anker.rotation_euler = (math.radians(E("GKANTEL", "-6")), 0, math.radians(E("GDRAAI", "-16")))
# v3: één mond; de losse tand las op 2x als een tweede mondje onder het oog (Daan #236 kan)
for o in list(anker.children_recursive):
    if o.material_slots and o.material_slots[0].material and o.material_slots[0].material.name.startswith("tand"):
        o.hide_render = True
# kroon minder munt (zoals capsule v1, Daan)
km = bpy.data.materials.get("kroon")
if km:
    b = km.node_tree.nodes["Principled BSDF"]; b.inputs["Roughness"].default_value = 0.38
# Gloop minder wit uitgeslagen in het felle licht: minder doorschijn, iets matter (alleen hier; gloop.py blijft gelijk)
lm = bpy.data.materials.get("lijf")
if lm:
    b = lm.node_tree.nodes["Principled BSDF"]
    for naam, w in (("Subsurface Weight", E("GSSS", "0.1")), ("Roughness", E("GRUW", "0.32"))):
        if naam in b.inputs: b.inputs[naam].default_value = w
# lichtring om zijn voet (gloopring.py: mint met wit hart), de kleur van Gloop op het goud
bpy.ops.mesh.primitive_torus_add(major_radius=1.55, minor_radius=0.07, location=(GX, 0.15, GZ + 0.05))
ring = bpy.context.object; ring.scale = (1.0, 0.42, 1.0); ring.visible_shadow = False
kies(ring, g.mat("ring", "b8ffd8", emis=E("RING", "5.0")))
lr = bpy.data.lights.new("ringlicht", "POINT"); lr.color = (0.55, 1.0, 0.75); lr.energy = E("RINGLICHT", "40"); lr.shadow_soft_size = 1.0
lo = bpy.data.objects.new("ringlicht", lr); lo.location = (GX, -0.6, GZ + 0.4); sc.collection.objects.link(lo)

# ---------- helden ----------
import held, hoeden
# 1. valt kop eerst door het gat de kamer in; zijn pet vliegt los
# v3 (Daan #236 M1): niet meer kop eerst (omgekeerd gezicht las als een los ei), maar voeten eerst met armen omhoog
# van schrik, iets schuin, gezicht rechtop: één silhouet. Hij zakt net uit het gat, de pet vliegt erboven.
HV = held.bouw("held", "schrik", plek=(E("HVX", "2.15"), -0.35, E("HVZ", "0.75")), draai=E("HVD", "-15"), schaal=E("HVS", "1.85"), kleur=int(E("HVKLEUR", "2")))
HV.rotation_mode = "ZYX"; HV.rotation_euler = (0, math.radians(E("HVKANTEL", "-14")), math.radians(15))   # paarse tuniek: los van de oranje stenen
for o in list(sc.objects):
    if o.name.startswith("hoed_") and o.parent is not None and o.parent == HV:
        o.hide_render = True
for o in list(HV.children_recursive):
    if o.name.startswith("hoed"):
        o.hide_render = True
hoeden.bouw(3, plek=(E("PETX", "3.1"), 0.0, E("PETZ", "5.75")), schaal=E("PETS", "1.6"), kantel=E("PETK", "15"), draai=E("PETD", "-30"))   # v5: koepel boven, klep opzij (v4 las als rode lippen)
# (bewegingsstreepjes weggelaten: op 2x lazen ze als stokjes door de held)
# 2. in de gang loopt een ridder nietsvermoedend naar de kamer
held.bouw("ridder", "stap2", plek=(E("RX", "-1.6"), 0.35, 0.0), draai=60, schaal=E("RS", "1.55"), gloed=40)

# ---------- titel ----------
def tekst(woord, loc, maat, kantel=0, rand=0.09, kleur="ffd23a"):
    cu = bpy.data.curves.new("titel", "FONT"); cu.body = woord
    cu.font = bpy.data.fonts.load(FONT); cu.size = maat; cu.align_x = "LEFT"; cu.align_y = "BOTTOM"
    cu.extrude = 0.09 * maat; cu.bevel_depth = 0.025 * maat; cu.bevel_resolution = 3
    o = bpy.data.objects.new("titel", cu); sc.collection.objects.link(o)
    o.location = loc; o.rotation_euler = (math.radians(90), math.radians(kantel), 0)
    o.data.materials.append(g.mat("titelgoud" + kleur, kleur, rough=0.3, spec=0.6, metaal=0.3, emis=0.25))
    cu2 = cu.copy(); cu2.extrude = 0.06 * maat; cu2.bevel_depth = rand * maat; cu2.bevel_resolution = 2
    o2 = bpy.data.objects.new("titelrand", cu2); sc.collection.objects.link(o2)
    o2.location = (loc[0], loc[1] + 0.16 * maat, loc[2]); o2.rotation_euler = o.rotation_euler
    cu2.materials.clear(); cu2.materials.append(g.mat("titelrand", "3a1a14", rough=0.6))
    return o
TX, TZ = E("TX", "-8.9"), E("TZ", "5.5")
tekst("HATS", (TX, -2.5, TZ), E("TH", "2.75"), kantel=E("TK", "3"))
tekst("OF THE FALLEN", (TX + 0.15, -2.5, TZ - 1.15), E("TO", "1.2"), kantel=E("TK", "3"), rand=0.12)

# ---------- licht ----------
def lamp(naam, soort, loc, kleur, kracht, grootte=1.0, doel=(0, 0, 1.0)):
    d = bpy.data.lights.new(naam, soort); d.color = kleur; d.energy = kracht
    if soort == "AREA": d.size = grootte
    o = bpy.data.objects.new(naam, d); o.location = loc; sc.collection.objects.link(o)
    o.rotation_euler = (Vector(doel) - Vector(loc)).to_track_quat("-Z", "Y").to_euler(); o.visible_camera = False
    return o
lamp("sleutel", "AREA", (3.0, -12.0, 10.0), (1.0, 0.9, 0.78), E("SLEUTEL", "3300"), E("SLEUTELMAAT", "18"), (2.0, 0.5, 2.0))
lamp("vul", "AREA", (-6.0, -12.0, 3.0), (0.8, 0.88, 1.0), E("VUL", "1500"), 10.0, (-3.0, 0.5, 2.5))
lamp("kamer", "AREA", (GX, -3.0, 3.6), (1.0, 0.82, 0.6), E("KAMERL", "350"), 4.0, (GX, 1.0, 1.4))
lamp("titellamp", "AREA", (-5.0, -8.0, 9.0), (1.0, 0.97, 0.9), E("TITELL", "1400"), 5.0, (-5.0, -2.5, 6.0))
lamp("zon", "SUN", (0, 0, 10), (1.0, 0.95, 0.85), E("ZON", "2.0"), 1.0, (1.0, 2.0, 0.0))
if os.environ.get("HV2_MAT", "0") == "1":
    # minder plastic: matter, minder glans, behalve goud, edelstenen en het oog
    for m in bpy.data.materials:
        if not m.use_nodes or m.name.startswith(("goud", "robijn", "safier", "kroon", "oog", "glim", "ring")): continue
        b = m.node_tree.nodes.get("Principled BSDF")
        if not b: continue
        if "Specular IOR Level" in b.inputs: b.inputs["Specular IOR Level"].default_value = min(b.inputs["Specular IOR Level"].default_value, E("GLANS", "0.25"))
        b.inputs["Roughness"].default_value = max(b.inputs["Roughness"].default_value, E("RUW", "0.55"))
    lamp("rand", "AREA", (4.0, 6.0, 7.0), (1.0, 0.85, 0.65), E("RANDL", "0"), 8.0, (4.0, 0.0, 1.5))
TOON = os.environ.get("HV2_TOON", "0") == "1"
if TOON:
    # v6 (Gemini 27 nov: "3D looks cheap and mobile-esque"): toon-schaduw zoals een getekend spel.
    # Elk materiaal wordt licht + vlakke schaduw: een harde Toon-lichtkant op de basiskleur, plus een vaste
    # schaduwtint (basiskleur, iets koeler en paarser) als emissie, zodat de schaduwkant een eigen vlakke kleur is
    # en niet zwart of glad. Glanzende dingen (oog, goud, kroon, stenen, helm) krijgen één harde witte glimvlek.
    ST = (E("STR", "0.78"), E("STG", "0.70"), E("STB", "1.0"))     # schaduwtint (koel en paars)
    SK = E("SCHADUW", "0.42")                                       # hoe licht de schaduwkant is
    GEENRAND = ("aarde", "gangwand", "kamerwand", "vloer", "steen", "gras", "kluit", "wortel", "rand_", "schacht", "titel", "hout", "mond", "hmond", "pupil", "hpupil", "brauw")
    GLIM = ("goud", "kroon", "hgoud", "gesp", "band")
    for m in bpy.data.materials:
        if not m.use_nodes: continue
        nt = m.node_tree; b = nt.nodes.get("Principled BSDF")
        if not b: continue
        if m.name.startswith("titelgoud"): b.inputs["Emission Strength"].default_value = 0.0   # titel ook getekend
        es = b.inputs["Emission Strength"].default_value if "Emission Strength" in b.inputs else 0.0
        if es > 0.0 or b.inputs["Emission Strength"].is_linked: continue
        uitn = next((n for n in nt.nodes if n.type == "OUTPUT_MATERIAL"), None)
        if not uitn: continue
        bc = b.inputs["Base Color"]
        src = bc.links[0].from_socket if bc.is_linked else None
        def kleur_naar(sock):
            if src is not None: nt.links.new(src, sock)
            else: sock.default_value = bc.default_value
        td = nt.nodes.new("ShaderNodeBsdfToon"); td.component = "DIFFUSE"
        td.inputs["Size"].default_value = E("TSIZE", "0.62"); td.inputs["Smooth"].default_value = E("TSMOOTH", "0.03")
        kleur_naar(td.inputs["Color"])
        mul = nt.nodes.new("ShaderNodeMix"); mul.data_type = "RGBA"; mul.blend_type = "MULTIPLY"
        mul.inputs[0].default_value = 1.0
        kleur_naar(mul.inputs[6]); mul.inputs[7].default_value = (ST[0], ST[1], ST[2], 1)
        em = nt.nodes.new("ShaderNodeEmission"); em.inputs["Strength"].default_value = E("TITELSCH", "0.8") if m.name.startswith("titelgoud") else SK
        nt.links.new(mul.outputs[2], em.inputs["Color"])
        add = nt.nodes.new("ShaderNodeAddShader")
        nt.links.new(td.outputs[0], add.inputs[0]); nt.links.new(em.outputs[0], add.inputs[1])
        laatst = add
        if not m.name.lower().startswith(GEENRAND) and E("RAND", "0.5") > 0:
            # randlicht: een smalle lichte rand langs de buitenkant van de figuren, zoals in getekende spellen
            lw = nt.nodes.new("ShaderNodeLayerWeight"); lw.inputs["Blend"].default_value = E("RANDBLEND", "0.35")
            cr = nt.nodes.new("ShaderNodeValToRGB"); cr.color_ramp.interpolation = "CONSTANT"
            cr.color_ramp.elements[0].position = 0.0; cr.color_ramp.elements[0].color = (0, 0, 0, 1)
            cr.color_ramp.elements[1].position = E("RANDPOS", "0.72"); cr.color_ramp.elements[1].color = (1, 1, 1, 1)
            nt.links.new(lw.outputs["Facing"], cr.inputs[0])
            mr = nt.nodes.new("ShaderNodeMix"); mr.data_type = "RGBA"; mr.blend_type = "SCREEN"; mr.inputs[0].default_value = 1.0
            kleur_naar(mr.inputs[6]); mr.inputs[7].default_value = (1.0, 0.86, 0.62, 1)
            mm = nt.nodes.new("ShaderNodeMix"); mm.data_type = "RGBA"; mm.blend_type = "MULTIPLY"; mm.inputs[0].default_value = 1.0
            nt.links.new(mr.outputs[2], mm.inputs[6]); nt.links.new(cr.outputs["Color"], mm.inputs[7])
            er = nt.nodes.new("ShaderNodeEmission"); er.inputs["Strength"].default_value = E("RAND", "0.5")
            nt.links.new(mm.outputs[2], er.inputs["Color"])
            a3 = nt.nodes.new("ShaderNodeAddShader")
            nt.links.new(add.outputs[0], a3.inputs[0]); nt.links.new(er.outputs[0], a3.inputs[1]); laatst = a3
        if m.name.lower().startswith(GLIM):
            tg = nt.nodes.new("ShaderNodeBsdfToon"); tg.component = "GLOSSY"
            tg.inputs["Size"].default_value = E("GSIZE", "0.08"); tg.inputs["Smooth"].default_value = 0.0
            g_ = E("GKLEUR", "0.45"); tg.inputs["Color"].default_value = (g_, g_ * 0.97, g_ * 0.9, 1)
            a2 = nt.nodes.new("ShaderNodeAddShader")
            nt.links.new(add.outputs[0], a2.inputs[0]); nt.links.new(tg.outputs[0], a2.inputs[1]); laatst = a2
        nt.links.new(laatst.outputs[0], uitn.inputs["Surface"])
    # minder lampen: één harde zon als lichtkant, de kamerlamp zacht; de rest uit (anders veel banden)
    for o in sc.objects:
        if o.type == "LIGHT" and o.name in ("vul", "titellamp", "sleutel"): o.data.energy = 0
        if o.type == "LIGHT" and o.name == "zon":
            o.data.energy = E("TZON", "3.2"); o.data.angle = math.radians(E("ZONHOEK", "4"))
            o.rotation_euler = (math.radians(E("ZONX", "52")), math.radians(E("ZONY", "-28")), math.radians(E("ZONZ", "-18")))
        if o.type == "LIGHT" and o.name == "kamer": o.data.energy = E("TKAMER", "0")
    for o in sc.objects:   # de titel werpt geen schaduw op de muur
        if o.name.split(".")[0].startswith("titel"): o.visible_shadow = False
sc.world = bpy.data.worlds.new("w"); sc.world.use_nodes = True
bg = sc.world.node_tree.nodes["Background"]; bg.inputs["Color"].default_value = (0.55, 0.72, 1.0, 1); bg.inputs["Strength"].default_value = E("WERELD", "0.0" if TOON else "0.2")

# ---------- camera ----------
cam = bpy.data.cameras.new("cam"); cam.sensor_fit = "HORIZONTAL"; cam.sensor_width = 36
D = 30.0; cam.lens = 36 * D / BREED
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
co.location = (0, -D, (ZTOP + ZBOT) / 2); co.rotation_euler = (math.radians(90), 0, 0)
sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.device = "CPU"; sc.cycles.use_denoising = True
sc.render.resolution_x = W; sc.render.resolution_y = H; sc.render.resolution_percentage = 100
sc.render.film_transparent = True
sc.view_settings.view_transform = "Standard"; sc.view_settings.look = "None"
# v6 (blinde test 27 nov 10:50, Gemini: "3D looks a bit cheap and mobile-esque, refine the lighting"):
# AgX met meer contrast in plaats van Standard, en een warme inktlijn om de vormen zoals bij een getekend spel.
if os.environ.get("HV2_AGX", "0") == "1":
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = os.environ.get("HV2_LOOK", "AgX - Punchy")
    sc.view_settings.exposure = E("BELICHT", "0.0")
if os.environ.get("HV2_LIJN", "0") == "1":
    geen = bpy.data.collections.new("geenlijn"); sc.collection.children.link(geen)
    for o in list(sc.objects):
        n = o.name.split(".")[0]
        if o.type != "MESH" and o.type != "CURVE": continue
        if n in ("spriet", "rand", "verspriet", "hangachter", "hangspriet", "kluitgras", "munt", "kiezel", "randkluit",
                 "gatwortel", "gatwortel2", "wortel", "aarde", "grasplak", "vloer", "kamerwand", "gangwand", "valwand",
                 "berg", "titel", "titelrand", "vlam", "vlammid", "kern", "bloem", "hart", "steel") or n.startswith("Sphere"):
            for c in list(o.users_collection): c.objects.unlink(o)
            geen.objects.link(o)
    sc.render.use_freestyle = True
    sc.render.line_thickness_mode = "ABSOLUTE"; sc.render.line_thickness = E("LIJNDIK", "2.6") * W / 1840
    fs = bpy.context.view_layer.freestyle_settings
    ls = fs.linesets[0] if fs.linesets else fs.linesets.new("lijn")
    ls.select_by_visibility = True; ls.select_by_edge_types = True
    ls.select_silhouette = True; ls.select_border = True; ls.select_crease = False; ls.select_external_contour = True
    ls.select_by_collection = True; ls.collection = geen; ls.collection_negation = "EXCLUSIVE"
    if ls.linestyle is None: ls.linestyle = bpy.data.linestyles.new("inkt")
    ls.linestyle.color = (0.16, 0.07, 0.05); ls.linestyle.thickness = 1.0; ls.linestyle.alpha = 0.85
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGBA"; sc.render.filepath = uit
bpy.ops.render.render(write_still=True)
print("klaar", uit)
