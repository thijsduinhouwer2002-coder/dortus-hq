"""Het hol in 3D, stukje 1: de schatkamer met een gang (Mila, 13 nov 2026).

Draai:  <venv>/bin/python hol.py <uit.png> <breedte> <hoogte> <samples> [gloop_versie] [hoeden]
  Voorbeeld strook op ware grootte: hol.py strook.png 720 120 24 2 2
  Groot om te bekijken:             hol.py groot.png 1440 240 32 2 2

Wat erin zit: een doorsnede van de grond zoals een mierenbak. Bovenop gras met sprietjes,
daaronder warme oker-terracotta aarde (tot 15 nov pruim; kleur H, zie ontwerp/steam/kleur-warm/), uitgehold: links een gang,
in het midden de schatkamer met een gouden berg, een kist en twee fakkels die warm licht op de
pruim gooien. Gloop (Daans gloop.py, ongewijzigd) staat in de kamer.
Camera en licht komen uit gedeeld.py (regel 1 van 3d-stijl.md); de fakkels geven extra licht.
Schaal: 120 px hoog = 4,5 eenheden, dus 1 eenheid is ±27 px; Gloop is even groot als in Daans strook.
"""
import sys, os, math, random
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import bpy
from mathutils import Vector
import gedeeld as g

uit = sys.argv[1]
W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
GLOOP_V = int(sys.argv[5]) if len(sys.argv) > 5 else 2
HOEDEN = int(sys.argv[6]) if len(sys.argv) > 6 else 2
PUT_STAP = int(sys.argv[7]) if len(sys.argv) > 7 else 0   # Mila 14 nov: gekochte stap van de put (0 dicht, 1 Rusty Spikes, 2 Deep Pit)
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
SCHACHT_GLOED = float(os.environ.get("HOL_SCHACHT_GLOED", "0.35"))   # eigen licht van de schachtwanden (Bram 15 nov)
X0, X1 = -BREED / 2 - 0.5, BREED / 2 + 0.5
# Ronde 7 (Daan kan): de platen (aarde, achterwand, vloer, gras, gang rechts) lopen nu 6 eenheden voorbij de rand.
# Ze hielden 0,5 voorbij het beeld op, en door het open einde viel er licht in de gang: in kolom 14 liep de wand
# van 60 naar 62, en omdat het spel die tegel herhaalt kwam er elke 32 px een trede. X0 en X1 blijven voor de
# kiezels en sprieten (zelfde willekeurige reeks, dus verder hetzelfde beeld).
XP0, XP1 = -BREED / 2 - 6.0, BREED / 2 + 6.0


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


def rand_mat():
    """Donkere omtrek (Mila 26 nov, Iris #179: stut, houweel en ton lazen als wandkleur). Zelfde truc als beestjes.py:
    een omgekeerde schil, de voorkant doorzichtig, de binnenkant donker pruimbruin en zonder licht."""
    m = bpy.data.materials.get("omtrek")
    if m:
        return m
    m = bpy.data.materials.new("omtrek"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    uit_ = nt.nodes.new("ShaderNodeOutputMaterial"); geo = nt.nodes.new("ShaderNodeNewGeometry")
    mix = nt.nodes.new("ShaderNodeMixShader"); em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*g.hex2("2a1418"), 1); em.inputs["Strength"].default_value = 1.0
    door = nt.nodes.new("ShaderNodeBsdfTransparent")
    nt.links.new(geo.outputs["Backfacing"], mix.inputs["Fac"])
    nt.links.new(em.outputs["Emission"], mix.inputs[1]); nt.links.new(door.outputs["BSDF"], mix.inputs[2])
    nt.links.new(mix.outputs["Shader"], uit_.inputs["Surface"])
    return m


def omtrek(o, dikte=0.035):
    """Schil om o: kopie van het net, langs de normalen naar buiten, vlakken omgedraaid. Heet <naam>_rand, zodat de
    lagen van de pijplijn (HOL_ALLEEN, HOL_VERBERG op het begin van de naam) hem met het ding meenemen."""
    import bmesh
    bpy.ops.object.select_all(action="DESELECT")
    o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    me = o.data.copy(); bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * dikte
    bmesh.ops.reverse_faces(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()
    me.materials.clear(); me.materials.append(rand_mat())
    s = bpy.data.objects.new(o.name + "_rand", me); sc.collection.objects.link(s)
    s.parent = o; s.visible_shadow = False
    return o


def uithollen(doel, gat, eigen_mat=False):
    mod = doel.modifiers.new("hol", "BOOLEAN"); mod.operation = "DIFFERENCE"; mod.object = gat
    mod.solver = "EXACT"
    # Bram 15 nov: eigen_mat=True geeft de snijvlakken het materiaal van het gat (alleen de schacht gebruikt dit)
    if eigen_mat:
        mod.material_mode = "TRANSFER"
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
    # Ronde 6 (moet 1): x uit de wereldpositie. "Object" is de geschaalde blokruimte (x van -0,5 tot 0,5 over het
    # hele hol), dus de ruis ging niet rond per kolom maar liep als één trage golf van links (donker) naar het midden
    # (licht). Daardoor had elke kamer een eigen tint. Nu gaat x echt rond met een periode van één kolom.
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    sepw = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(geo.outputs["Position"], sepw.inputs[0])
    nt.links.new(sepw.outputs["X"], hoek.inputs[0])
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


# Mila 15 nov (punt 1 Thijs 13:30, voorstel H van Daan, ontwerp/steam/kleur-warm/): warme oker-terracotta aarde,
# lichter, in plaats van pruim. De namen PRUIM blijven, zodat de rest van de code niet verschuift.
# Mila 24 nov (issue 6, etalage-audit punt 10): FEL=1 geeft meer waardeverschil. De aarde zakt een trede (zelfde
# warme oker-terracotta van Thijs 15 nov), vloer en gras worden lichter en voller, en het beeld krijgt meer contrast.
# Zo staan gang, held, Gloop en goud los van de grond in plaats van bruin op bruin.
FEL = os.environ.get("HOL_FEL", "0") == "1"   # standaard uit tot Daan keurt; voor de tegels verandert er dan niets
PRUIM = aardemat("pruim", "552a1e", "7a4536") if FEL else aardemat("pruim", "684033", "8e5949")
PRUIM_L = g.mat("pruim_l", "a26a58", rough=0.8, spec=0.2)
PRUIM_D = g.mat("pruim_d", "5a3227", rough=0.9, spec=0.1)
STEEN = g.mat("steen", "c69383", rough=0.6, spec=0.3)
GRAS = g.mat("gras", "6fd84f" if FEL else "5bbf4a", rough=0.95, spec=0.03)
GRAS_D = g.mat("gras_d", "3b8f3a", rough=0.95, spec=0.03)
GOUD = g.mat("goud", "goud", rough=0.18, spec=0.9, metaal=0.85, emis=0.06)
GOUD_D = g.mat("goud_d", "goud_d", rough=0.3, spec=0.7, metaal=0.8)
HOUT = g.mat("hout", "8a4b2a", rough=0.7, spec=0.2)
HOUT_D = g.mat("hout_d", "5a2e1c", rough=0.75)
LADDER_SPORT = g.mat("ladder_sport", "7a4a2c", rough=0.75)   # Mila 15 nov: lichter dan HOUT_D, leest tegen kleur H
VLAM = g.mat("vlam", "ffb347", emis=9.0)
VLAM_K = g.mat("vlamkern", "fff1b0", emis=14.0)
# Daan 13 nov 23:40: vlam in drie lagen met lage emissie. Emissie 9 en 14 knipt met view transform Standard naar
# wit: de fakkel las als een wit ei op een stokje. Proef en vergelijking in ontwerp/steam/fakkel-3d/.
V_BUIT = g.mat("v_buit", "ff5a1f", emis=1.6)   # rood-oranje rand
V_MID = g.mat("v_mid", "ff9b2a", emis=2.4)     # oranje
V_HART = g.mat("v_hart", "ffe27a", emis=3.2)   # geel hart, net niet wit
HOUT_F = g.mat("hout_f", "6e4632", rough=0.75, spec=0.2)   # zelfde donkerder hout als de kamerstukken
DOEK = g.mat("doek", "3a2418", rough=0.9, spec=0.1)        # omwikkelde kop met pek
IJZER = g.mat("ijzer", "3b3640", rough=0.45, metaal=0.8)
ROBIJN = g.mat("robijn", "rood", rough=0.08, spec=1.0, emis=0.4)
SAFIER = g.mat("safier", "4fa3ff", rough=0.08, spec=1.0, emis=0.4)
WORTEL = g.mat("wortel", "c9a27a", rough=0.8)
BLOEM = g.mat("bloem", "ffd84a", rough=0.5, emis=0.2)
BLOEM_R = g.mat("bloemr", "f08a9a", rough=0.5, emis=0.2)

# ---------- de aarde: een plaat met de voorkant op y = 0 ----------
aarde = blok("aarde", ((XP0 + XP1) / 2, 1.5, (ONDER - 1 + MAAIVELD) / 2), (XP1 - XP0, 3.0, MAAIVELD - ONDER + 1), PRUIM)

# schatkamer: boog (cilinder) plus vierkant onderstuk; achterwand blijft staan op y = 1.4
# Ronde 5 (Bram 18:30): 48 breed, precies kolom 6 tot 9 (spelpixel 96 tot 144), zoals de schatkamer in het spel.
KX0, KX1, KVL, KTOP = LINKS + 6 * KOL + 0.08, LINKS + 9 * KOL - 0.08, 0.0, 2.75
kamer_b = blok("kamer_gat", (0, 0.2, (KVL + 1.4) / 2), (KX1 - KX0, 2.4, 1.4 - KVL))
uithollen(aarde, kamer_b)
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1.0, depth=2.4, location=(0, 0.2, 1.4), rotation=(math.radians(90), 0, 0))
boog = bpy.context.object; boog.scale = ((KX1 - KX0) / 2, (KTOP - 1.4), 1)
uithollen(aarde, boog)
# gang naar links, één rij hoog, met een schacht omhoog naar het gras
gang = blok("gang_gat", ((-11.8 + KX0) / 2, 0.2, GANG_TOP / 2), (KX0 - (-11.8) + 0.6, 2.4, GANG_TOP))
uithollen(aarde, gang)
# Bram 15 nov (moet Daan 00:50): de zijvlakken van de schacht, de inhammen en de ronde hoeken lagen in eigen schaduw en
# werden bijna zwart (lezen als gaten). Die snijvlakken krijgen nu een eigen wandkleur met een vleugje eigen licht,
# zodat ze de toon van de wand houden met wat schaduw, maar nooit zwart worden. De rest van de aarde blijft PRUIM.
SCHACHT_WAND = g.mat("schacht_wand", "8a5342", rough=0.9, spec=0.1, emis=SCHACHT_GLOED)
schacht = blok("schacht_gat", (-11.0, 0.2, 2.0), (1.2, 2.4, 3.2), SCHACHT_WAND)
uithollen(aarde, schacht, True)
# Bram 15 nov 00:30 (Daan 23:35: geen tanden): de schacht had harde rechte randen in de rots. Langs elke wand twee
# ondiepe ronde inhammen (bol die door de plaat steekt, hooguit 0,1 de wand in), zodat het een gegraven gat wordt zonder scherpe punten.
# Eigen random, zodat de rest van het hol gelijk blijft.
_rs = random.Random(11)
for _kant in (-1, 1):
    for _i in range(2):
        _z = GANG_TOP + 0.55 + _i * 0.85 + _rs.uniform(-0.1, 0.1) + (0.3 if _kant > 0 else 0.0)
        _r = _rs.uniform(0.15, 0.2)
        uithollen(aarde, bol("schacht_brok", (-11.0 + _kant * (0.6 - _r * 0.45), 0.2, _z), (_r, 1.3, _r * 2.2), SCHACHT_WAND, 24), True)
# Daans kan: waar de schacht op de gang uitkomt geen harde rechte hoek meer, maar een ronde overgang.
# Snijder = vierkantje in de hoek min een cilinder, dus de rots loopt in een boog de gang in.
for _kant in (-1, 1):
    _rr = 0.28
    _x = -11.0 + _kant * 0.6
    # Bram 15 nov: niet meer door de hele aarde snijden (tot y 0,6, niet 1,4): door een gat tot achteren keek je op de
    # achterwand in diepe schaduw, een zwart haakje. Nu kijk je in de hoek op een vlak dat naar de camera kijkt.
    _snij = blok("schacht_hoek", (_x + _kant * _rr / 2, -0.2, GANG_TOP + _rr / 2), (_rr, 1.6, _rr), SCHACHT_WAND)
    _cil = cil("schacht_hoek_rond", (_x + _kant * _rr, -0.2, GANG_TOP + _rr), _rr, 1.8, SCHACHT_WAND, rot=(math.radians(90), 0, 0), verts=32)
    uithollen(_snij, _cil, True)
    uithollen(aarde, _snij, True)
# gang naar rechts, met een kleine voorraadkamer
# loopt door tot voorbij de rand: het rustige stuk (kolom 13 en 14) is een gang die herhaalt
gang_r = blok("gangr_gat", ((KX1 + XP1 + 1) / 2, 0.2, GANG_TOP / 2), (XP1 + 1 - KX1 + 0.6, 2.4, GANG_TOP))
uithollen(aarde, gang_r)
# Kamers boven de gang (in het spel: klik in de aarde boven de gang). Ronde 5, voorstel Daan (moet 3):
# een gegraven stuk van meer kolommen is EEN kamer. Kolom 2 begin, 3 midden a, 4 midden b, 5 eind;
# kolom 11 een losse kamer. Het midden is recht en egaal belicht, zodat elk stuk naast elk ander past.
# Ovaal 0,78 breed (14 spelpixels, Bram 18:30): heel binnen zijn vak van 16.
KZ = 2.25; KH = 0.62; KR = 0.78
BREDE = (LINKS + 2.5 * KOL, LINKS + 5.5 * KOL)     # middens van de ronde einden (kolom 2 en 5)
LOS = LINKS + 11.5 * KOL
MID_A, MID_B = LINKS + 3.5 * KOL, LINKS + 4.5 * KOL
KAMERS = [(BREDE[0], KZ), (MID_A, KZ), (MID_B, KZ), (BREDE[1], KZ), (LOS, KZ)]   # voor de kiezels
def ovaal(kx):
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=1.0, depth=2.4, location=(kx, 0.2, KZ), rotation=(math.radians(90), 0, 0))
    kg = bpy.context.object; kg.scale = (KR, KH, 1)
    return kg
for kx in (BREDE[0], BREDE[1], LOS):
    uithollen(aarde, ovaal(kx))
uithollen(aarde, blok("kamer_mid", ((BREDE[0] + BREDE[1]) / 2, 0.2, KZ), (BREDE[1] - BREDE[0], 2.4, 2 * KH)))
for o in (aarde,):
    afronden(o, 0.18, 4)
    bpy.context.view_layer.objects.active = o

# achterwand donkerder dan de voorkant, zodat de kamer diepte heeft
blok("achterwand", (0, 1.35, 1.2), (XP1 - XP0, 0.1, 4.0), PRUIM_L)
# Bram 14 nov 23:30 (kan Daan): zachte donkere rand bovenin de schacht, op de achterwand onder het gras.
# Platte donkere bollen die naar beneden kleiner worden: het licht van boven komt er niet bij, dus een gegraven gat.
for _dx, _dz, _sx, _sz in [(-0.42, -0.22, 0.34, 0.26), (0.0, -0.18, 0.42, 0.24), (0.42, -0.22, 0.34, 0.26),
                           (-0.25, -0.5, 0.24, 0.16), (0.27, -0.48, 0.22, 0.15)]:
    bol("schacht_rand", (-11.0 + _dx, 1.29, MAAIVELD + _dz), (_sx, 0.03, _sz), PRUIM_D, 16)

# ---------- lagen en stenen in de voorkant ----------
for i in range(70):
    x = random.uniform(X0, X1); z = random.uniform(ONDER, MAAIVELD - 0.25)
    # niet in de gaten
    if x > TEGEL_X - 0.3:
        continue   # rustig stuk: daar liggen dezelfde kiezels in elke kolom (hieronder)
    if (KX0 - 1.4 < x < KX1 + 1.4 and z < KTOP + 0.45) or (z < 1.7 and x < 12.6 and x > -12.2) or (-11.8 < x < -10.2) or any(abs(x - kx) < 1.05 and abs(z - kz) < 0.8 for kx, kz in KAMERS) or (BREDE[0] - 1.0 < x < BREDE[1] + 1.0 and abs(z - KZ) < 0.8):
        continue
    r = random.uniform(0.07, 0.2)
    bol("kiezel", (x, -0.02, z), (r * 1.3, r * 0.6, r), random.choice([STEEN, PRUIM_L, PRUIM_L]), 12)
# Mila 26 nov (issue 96, Gemini "too basic"): het rustige stuk (de tegel die het spel herhaalt) heeft geen kiezels meer.
# Drie dezelfde kiezels elke 16 spelpixels lazen als een stippenpatroon. Nu legt het spel per kolom zelf stenen, botten,
# een helm of wortels uit versiering.py (deco-blad), elke kolom anders. De rest van het beeld houdt zijn kiezels.
# een strook lichtere aarde net onder het gras
blok("toplaag", ((XP0 + XP1) / 2, -0.01, MAAIVELD - 0.18), (XP1 - XP0, 0.04, 0.12), PRUIM_L)

# ---------- gras bovenop ----------
# loopt ver naar achteren door, zodat het gras de rij 0 tot 8 helemaal vult (geen donkere band erboven)
grasplak = blok("gras", ((XP0 + XP1) / 2, 1.4, MAAIVELD + 0.09), (XP1 - XP0, 2.9, 0.22), GRAS_D)
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
# Ronde 6: overal het patroon van het rustige stuk (4 per kolom), want losse plukjes wierpen een schaduw op de
# bovenste strook aarde die per kolom verschilde (moet 1). Trek de random toch even, zodat de rest gelijk blijft.
for i in range(60):
    random.uniform(X0, X1)
for k in range(-9, 0):
    for dx in (0.2, 0.65, 1.1, 1.55):
        x = TEGEL_X + k * KOL + dx
        if -11.7 < x < -10.3:
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
VLOER = g.mat("vloer", "e6a983" if FEL else "d0947c", rough=0.8, spec=0.2)
vloer = blok("vloer", ((XP0 + XP1) / 2, 0.7, -0.03), (XP1 - XP0, 1.5, 0.1), VLOER)

# ---------- de schat: een gouden berg rechts in de kamer ----------
mb = bpy.data.metaballs.new("berg"); mb.resolution = 0.06; mb.render_resolution = 0.03
berg = bpy.data.objects.new("berg", mb); sc.collection.objects.link(berg)
for (x, y, z, r) in [(1.35, 0.75, -0.25, 1.0), (1.95, 0.85, -0.3, 0.8), (0.4, 0.7, -0.45, 0.88), (1.5, 0.9, 0.1, 0.62)]:
    e = mb.elements.new(); e.co = (x, y, z); e.radius = r
berg.data.materials.append(GOUD_D)
# losse munten op en rond de berg
for i in range(90):
    a = random.uniform(0, math.pi); rr = random.uniform(0.2, 1.25)
    x = 1.35 + rr * math.cos(a) * 1.0; z = max(0.03, 0.75 - rr * 0.62 + random.uniform(-0.05, 0.05))
    y = random.uniform(0.25, 1.0)
    cil("munt", (x, y, z), 0.13, 0.035, GOUD, rot=(random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9), 0), verts=20)
for i in range(14):   # munten die over de vloer gerold zijn
    x = random.uniform(KX0 + 0.3, KX1 - 0.3); y = random.uniform(0.1, 0.9)
    cil("munt_vloer", (x, y, 0.02), 0.12, 0.03, GOUD, verts=20)
bol("robijn", (1.15, 0.35, 0.62), (0.12, 0.1, 0.14), ROBIJN, 8)
bol("safier", (2.0, 0.4, 0.5), (0.1, 0.08, 0.12), SAFIER, 8)
# een beker bovenop de berg
cil("beker_voet", (1.55, 0.7, 0.92), 0.12, 0.05, GOUD, verts=24)
cil("beker_steel", (1.55, 0.7, 1.02), 0.04, 0.18, GOUD, verts=16)
cil("beker_kom", (1.55, 0.7, 1.22), 0.1, 0.24, GOUD, verts=24, r2=0.2)

# achterwand van de schatkamer een trede lichter en warmer, met een gloed achter Gloop:
# hij moet het lichtste vlak van de strook zijn (frisse kijker ronde 1: "figuur te klein voor de drukke strook")
KAMERWAND = g.mat("kamerwand", "9e6a56", rough=0.8, spec=0.15)   # Mila 15 nov: H was b88168; een trede donkerder zodat goud en kroon eruit springen (blinde kijker 16 tegen 14)
blok("kamerwand", (0, 1.3, 1.3), (KX1 - KX0, 0.05, 2.9), KAMERWAND)
gg = bpy.data.lights.new("gloopgloed", "POINT"); gg.color = (1.0, 0.8, 0.55); gg.energy = 90; gg.shadow_soft_size = 1.0
ggo = bpy.data.objects.new("gloopgloed", gg); ggo.location = (-0.3, 1.15, 1.2); sc.collection.objects.link(ggo)

# de berg geeft zelf een warme gloed op de wand (dat is de sfeer: goud dat licht geeft)
gd = bpy.data.lights.new("goudgloed", "POINT"); gd.color = (1.0, 0.75, 0.3); gd.energy = 220; gd.shadow_soft_size = 0.8
go = bpy.data.objects.new("goudgloed", gd); go.location = (2.0, 0.2, 1.3); sc.collection.objects.link(go)

# ladder in de schacht naar het gras
for kant in (-0.35, 0.35):
    cil("ladder_paal", (-11.0 + kant, 0.6, 1.6), 0.05, 3.4, HOUT_F, verts=8)  # Daan 23:45: kamerhout, minder oranje
for k in range(8):
    # Mila 15 nov (kan 1 van Daan bij kleur H): sporten een trede lichter en geler, anders bruin op bruin
    cil("ladder_sport", (-11.0, 0.6, 0.25 + k * 0.4), 0.035, 0.7, LADDER_SPORT, rot=(0, math.radians(90), 0), verts=8)

# ---------- kist links in de kamer, open, goud puilt eruit ----------
kist = blok("kist", (-2.05, 0.75, 0.32), (0.85, 0.6, 0.62), HOUT); afronden(kist, 0.05, 2)
blok("kistband", (-2.05, 0.44, 0.32), (0.98, 0.03, 0.12), GOUD_D)
deksel = blok("deksel", (-2.05, 1.05, 0.88), (0.95, 0.12, 0.55), HOUT_D, rot=(math.radians(-25), 0, 0)); afronden(deksel, 0.04, 2)
for i in range(10):
    cil("kistmunt", (-2.05 + random.uniform(-0.38, 0.38), 0.7 + random.uniform(-0.15, 0.15), 0.66 + random.uniform(0, 0.08)),
        0.12, 0.03, GOUD, rot=(random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6), 0), verts=20)


# ---------- fakkels met echt warm licht ----------
def druppel(naam, loc, r, hoog, m, scheef=0.0):
    """Vlam als druppel: onderkant bol, bovenhelft getrokken tot een punt die iets opzij buigt. Geen schaduw."""
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=14, radius=1, location=(0, 0, 0))
    o = bpy.context.object; o.name = naam
    for v in o.data.vertices:
        if v.co.z > 0:
            t = v.co.z; k = (1 - t) ** 1.6
            v.co.x = v.co.x * k + scheef * t * t; v.co.y *= k; v.co.z = t * hoog
    o.scale = (r, r * 0.85, r); o.location = loc; o.visible_shadow = False
    bpy.ops.object.shade_smooth(); return kies(o, m)


def vlam_fakkel(pre, x, y, z, beugel=True, groot=1.2):
    if beugel:
        cil(pre + "beugelplaat", (x, y + 0.12, z - 0.18), 0.07, 0.03, IJZER, rot=(math.radians(90), 0, 0), verts=6)
        cil(pre + "beugelarm", (x, y + 0.04, z - 0.14), 0.018, 0.16, IJZER, rot=(math.radians(90), 0, 0), verts=8)
    cil(pre + "steel", (x, y - 0.03, z - 0.16), 0.055, 0.42, HOUT_F, rot=(math.radians(-12), 0, 0), verts=10, r2=0.035)
    cil(pre + "kop", (x, y - 0.06, z + 0.07), 0.085 * groot, 0.13, DOEK, verts=12, r2=0.1 * groot)
    zv = z + 0.16
    druppel(pre + "vlam", (x, y - 0.08, zv + 0.10 * groot), 0.15 * groot, 2.3, V_BUIT, scheef=0.05)
    druppel(pre + "vlammid", (x, y - 0.13, zv + 0.08 * groot), 0.11 * groot, 2.0, V_MID, scheef=0.04)
    druppel(pre + "kern", (x, y - 0.18, zv + 0.05 * groot), 0.06 * groot, 1.7, V_HART, scheef=0.02)

FAKKEL_POEL = os.environ.get("HOL_FAKKEL_POEL", "0") == "1"
GANGFAKKELS = []   # lampen van de gangfakkels; zie onderaan (light linking)


def fakkel(x, z, kracht=160, gang=False):
    # namen beginnen met "fakkel" (Bram 13 nov 23:25): de pijplijn maakt er een losse laag van (HOL_ALLEEN ["fakkel"])
    # Daan 13 nov 23:40: ijzeren beugel, steel van kamerhout, donkere kop, vlam als druppel met punt (3 lagen).
    # Zelfde hoogte als de oude fakkel (van z - 0,52 tot z + 0,52), dus het vak in sprites.json blijft passen.
    vlam_fakkel("fakkel", x, 1.0, z - 0.17, beugel=True)
    d = bpy.data.lights.new("fakkellicht", "POINT"); d.color = (1.0, 0.6, 0.28); d.energy = kracht; d.shadow_soft_size = 0.15
    o = bpy.data.objects.new("fakkellicht", d); o.location = (x, 0.5, z + 0.35); sc.collection.objects.link(o)
    if gang:
        GANGFAKKELS.append(o)


fakkel(KX0 + 0.2, 1.65)
fakkel(KX1 - 0.2, 1.65)
fakkel(-7.2, 0.95, 90, gang=True)
fakkel(5.0, 0.95, 90, gang=True)   # verder van het rustige stuk rechts, zodat dat egaal licht krijgt
# Kamers (Daan, moet 3): geen fakkel hoog meer (die vlam las als pupil: drie kommen werden drie ogen).
# Begin: fakkel laag op de linkerwand. Midden a: stut met schoren. Midden b: houweel en tonnetje. Eind: kistje.
# Ronde 6 (Daan kan a): de vloer begint 0,2 achter de voorkant. Eerst stak hij tot y = 0 en voorbij de ronde
# einden door, en las de voorrand als een donker plankje onder de kamer.
blok("kamervloer", ((BREDE[0] + BREDE[1]) / 2, 0.8, KZ - 0.6), (BREDE[1] - BREDE[0], 1.2, 0.06), VLOER)
# Bram 15 nov (kan Daan 22:50): de vloer hield links en rechts op met een rechte lijn (een rechte plaat tegen de ronde
# wand, van boven gezien een lijn naar achteren, dus in beeld verticaal). Nu een halve schijf aan elk eind: midden
# diep loopt de vloer het verst door, voor en achter minder, zodat de rand meebuigt met de ronde kant.
for _ex in (BREDE[0], BREDE[1]):
    _vs = cil("kamervloer_eind", (_ex, 0.8, KZ - 0.606), 1.0, 0.06, VLOER, verts=48)   # net onder de plaat: geen dubbel vlak
    _vs.scale = (0.36, 0.6, 1)
    for _p in _vs.data.polygons:
        _p.use_smooth = False   # cil() zet glad; op een platte schijf geeft dat zwarte vlekken
blok("kamervloer", (LOS, 0.8, KZ - 0.6), (1.2, 1.2, 0.06), VLOER)
fakkel(BREDE[0] - 0.4, KZ - 0.3, 20)
STUT = g.mat("stut", "34180e", rough=0.75)       # Mila 15 nov kleur H: donkerder en roder (was 6e4632), anders verdwijnt het hout in de lichte warme kamerwand
BAND = g.mat("band", "d9a441", rough=0.4, spec=0.5)
# Mila 26 nov (Iris op #179, build 3fddb22: "wortels, haakjes en schappen zijn 4 tot 8 px en bijna wandkleur; liever
# minder maar groter en met een donkere rand, zoals vat en schedel"). Houweel en ton zijn nu groter, van lichter warm
# hout (STUT_L) en hebben een donkere omtrek, zodat ze op 120 px als ding voor de kamerwand staan.
STUT_L = g.mat("stut_l", "9a5a2e", rough=0.7, spec=0.2)
# De stut zelf blijft voorlopig zoals hij was: dikker met omtrek las hij bij een blinde lezer als tafel (twee keer, ook
# met schuine poten). Volgende stap: een vorm die als mijnraam leest, eerst blind testen.
for dx in (-0.55, 0.55):
    blok("stut", (MID_A + dx, 0.5, KZ - 0.05), (0.16, 0.16, 2 * KH - 0.1), STUT)
blok("stut", (MID_A, 0.5, KZ + KH - 0.12), (1.45, 0.18, 0.16), STUT)
for dx, a in ((-0.38, 45), (0.38, -45)):
    blok("stut", (MID_A + dx, 0.5, KZ + KH - 0.3), (0.42, 0.12, 0.1), STUT, rot=(0, math.radians(a), 0))
# houweel: dikke lichte steel schuin tegen de ton, een gebogen ijzeren kop met twee punten (las als wit streepje)
HOUWEEL = g.mat("houweel", "a9b0c2", rough=0.35, spec=0.6, metaal=0.6)
HOUWEEL_D = g.mat("houweel_d", "6c7388", rough=0.4, metaal=0.6)
_hx, _ha = MID_B - 0.3, math.radians(-20)   # voet van de steel, helling naar rechts
_sl = 0.95
omtrek(cil("houweelsteel", (_hx + math.sin(-_ha) * _sl / 2, 0.45, KZ - KH + 0.04 + math.cos(_ha) * _sl / 2), 0.055, _sl,
           STUT_L, rot=(0, -_ha, 0), verts=10))
_kx, _kz = _hx + math.sin(-_ha) * _sl * 0.96, KZ - KH + 0.04 + math.cos(_ha) * _sl * 0.96
for _kant in (-1, 1):   # twee helften van de kop, elk een kegel die naar buiten spits toeloopt en iets omlaag buigt
    # haaks op de steel (rechts: hoek 90 - helling), elke punt 14 graden terug naar de steel; de kegel wijst met z naar buiten
    _r = math.radians(90) - _ha + math.radians(14) if _kant > 0 else -math.radians(90) - _ha - math.radians(14)
    omtrek(cil("houweelkop", (_kx + _kant * 0.2 * math.cos(_ha), 0.4, _kz + _kant * 0.2 * math.sin(_ha) - 0.02), 0.075, 0.42,
               HOUWEEL, rot=(0, _r, 0), verts=12, r2=0.018))
omtrek(bol("houweelkop", (_kx, 0.4, _kz), (0.1, 0.08, 0.1), HOUWEEL_D, 12))
cil("ton", (MID_B + 0.33, 0.5, KZ - KH + 0.29), 0.27, 0.55, STUT_L, verts=24)
omtrek(bpy.context.object)
for dz in (-0.16, 0.16):
    cil("tonband", (MID_B + 0.33, 0.5, KZ - KH + 0.29 + dz), 0.282, 0.06, BAND, verts=24)
blok("kistje", (BREDE[1] + 0.1, 0.45, KZ - 0.36), (0.5, 0.36, 0.38), STUT)
blok("kistje", (BREDE[1] + 0.1, 0.45, KZ - 0.2), (0.52, 0.38, 0.05), BAND)
# licht van binnen over de hele brede kamer, naar achteren gericht: licht de kamer, niet de voorkant van de aarde
kl = bpy.data.lights.new("kamerlicht", "AREA"); kl.shape = "RECTANGLE"; kl.size = BREDE[1] - BREDE[0] + 1.0; kl.size_y = 0.8
kl.color = (1.0, 0.78, 0.6); kl.energy = 90
klo = bpy.data.objects.new("kamerlicht", kl); klo.location = ((BREDE[0] + BREDE[1]) / 2, 0.05, KZ)
klo.rotation_euler = (math.radians(90), 0, 0); sc.collection.objects.link(klo)
# losse kamer: twee lichtgevende zwammetjes op de vloer, warm lila licht van binnen
for dx, s_ in ((-0.3, 1.0), (-0.08, 0.7)):
    cil("steel", (LOS + dx, 0.6, KZ - 0.48), 0.035 * s_, 0.18 * s_, g.mat("zsteel", "efe4d8", rough=0.6))
    bol("hoedje", (LOS + dx, 0.6, KZ - 0.39 + 0.05 * s_), (0.11 * s_, 0.11 * s_, 0.06 * s_), g.mat("zwam", "9ff0e0", rough=0.5, emis=2.0), 16)
ll = bpy.data.lights.new("loslicht", "AREA"); ll.size = 0.9; ll.color = (1.0, 0.8, 0.7); ll.energy = 25
llo = bpy.data.objects.new("loslicht", ll); llo.location = (LOS, 0.05, KZ); llo.rotation_euler = (math.radians(90), 0, 0); sc.collection.objects.link(llo)
zl = bpy.data.lights.new("zwamlicht", "POINT"); zl.color = (0.55, 1.0, 0.9); zl.energy = 40; zl.shadow_soft_size = 0.3
zlo = bpy.data.objects.new("zwamlicht", zl); zlo.location = (LOS - 0.2, 0.2, KZ - 0.2); sc.collection.objects.link(zlo)

# stekelput in de linker gang (zit in het spel: hol.gd, vallen = "stekelput")
PUT_X = LINKS + 4.5 * KOL   # midden van kolom 4 (spelpixel 64 tot 80), zoals hol.gd een put in één kolom tekent
# Mila 16 nov (moet Daan 13:58, Iris punt 3): de put moet op 120 px als GAT lezen, niet als rijtje naaldjes op de vloer.
# Zwarte schacht (snijvlakken zwart via eigen_mat), donkerrode gloed van onderen, botwitte stekels met donkere rand,
# een hoed op een stekel als grap en een schedeltje. PUT_OUD=1 = de put van vóór 16 nov.
PUT_OUD = os.environ.get("PUT_OUD") == "1"
PUT_ZWART = g.mat("put_zwart", "0a0608", rough=1.0, spec=0.0)
_gv = blok("put_gat_v", (PUT_X, 0.4, -0.2), (1.55, 2.0, 0.6)); _gv.data.materials.append(PUT_ZWART)
_ga = blok("put_gat_a", (PUT_X, 0.4, -0.25), (1.55, 2.0, 0.7)); _ga.data.materials.append(PUT_ZWART)
uithollen(vloer, _gv, eigen_mat=not PUT_OUD)
uithollen(aarde, _ga, eigen_mat=not PUT_OUD)
if PUT_OUD:
    blok("put_bodem", (PUT_X, 0.7, -0.52), (1.55, 1.5, 0.06), PRUIM_D)
else:
    # gloeiende bodem en rood licht van onderen: kleurt de stekels van onder en de gangmuur boven de put rood
    blok("put_bodem", (PUT_X, 0.7, -0.52), (1.55, 1.5, 0.06), g.mat("put_gloed", "a01a0a", rough=1.0, emis=1.4))
    rl = bpy.data.lights.new("putlicht", "POINT"); rl.color = (1.0, 0.16, 0.05); rl.energy = 18; rl.shadow_soft_size = 0.4
    rlo = bpy.data.objects.new("putlicht", rl); rlo.location = (PUT_X, 0.45, -0.38); sc.collection.objects.link(rlo)
    for dx in (-0.78, 0.78):   # donkere lip: de vloer houdt scherp op
        blok("put_lip", (PUT_X + dx, 0.5, 0.0), (0.03, 2.0, 0.04), PUT_ZWART)
STAAL = g.mat("staal", "staal", rough=0.25, spec=0.8, metaal=0.9)
# Ronde 4: de stekels steken boven de vloer uit (zoals hol.gd de put tekent: 8 spelpixels vanaf de vloer),
# want onder de vloer is maar 2,6 spelpixel beeld over. Lichter staal met een glimpje, zodat ze op 120 px lezen.
STAAL_L = g.mat("staal_l", "d8dce8", rough=0.2, spec=0.9, metaal=0.7, emis=0.15)
if PUT_STAP == 0 and not PUT_OUD:
    BOT = g.mat("put_bot", "f4eee2", rough=0.35, spec=0.6, emis=0.12)
    RAND_D = g.mat("put_randd", "1a0a0a", rough=1.0, spec=0.0)
    # voorste rij: 5 dikke botwitte stekels, wisselend hoog, met een donkere kegel er net achter als rand
    hoogtes = (0.62, 0.86, 0.7, 0.92, 0.66)
    for i, hoog in enumerate(hoogtes):
        x = PUT_X - 0.56 + i * 0.28
        cil("stekel", (x, 0.12, -0.3 + hoog / 2), 0.1, hoog, BOT, verts=10, r2=0.0)
        cil("stekelrand", (x, 0.2, -0.3 + (hoog + 0.08) / 2), 0.135, hoog + 0.08, RAND_D, verts=10, r2=0.0)
    # achterste rij lager en tussen de voorste in, alleen van onder rood aangelicht
    for i in range(4):
        x = PUT_X - 0.42 + i * 0.28
        cil("stekel", (x, 0.7, -0.3 + 0.28), 0.09, 0.56, BOT, verts=10, r2=0.0)
    # de grap: een blauwe puntmuts van een held die het niet haalde, doorgeprikt op de hoogste stekel
    HX = PUT_X - 0.56 + 3 * 0.28
    MUTS = g.mat("put_muts", "3d6fe0", rough=0.6)
    cil("puthoed_rand", (HX, 0.1, 0.38), 0.2, 0.035, MUTS, rot=(0, math.radians(-10), 0), verts=20)
    cil("puthoed", (HX + 0.02, 0.1, 0.5), 0.15, 0.26, MUTS, rot=(0, math.radians(-10), 0), verts=20, r2=0.0)
    cil("puthoed_band", (HX, 0.1, 0.41), 0.152, 0.04, g.mat("put_band", "f2c230", rough=0.5), rot=(0, math.radians(-10), 0), verts=20)
    # schedeltje vooraan op de bodem, half in het rood
    bol("putschedel", (PUT_X - 0.34, 0.02, -0.17), (0.13, 0.11, 0.12), BOT, 16)
    for ox in (-0.045, 0.045):
        bol("putschedel_oog", (PUT_X - 0.34 + ox, -0.09, -0.15), (0.03, 0.02, 0.035), PUT_ZWART, 10)
elif PUT_STAP == 1 and not PUT_OUD:
    # Mila 25 nov (issue #76, tempo-regel 4): Rusty Spikes las na de koop zwakker dan de put ervoor (dunne donkere
    # staafjes tegen de roodbruine vloer, hoed en schedel weg). Nu dezelfde opbouw als stap 0, maar meer en hoger:
    # 7 stekels voor in plaats van 5, ±15 procent hoger, met een wit puntje. Hoed en schedel blijven.
    # Ronde 2 (Daan #91, M1): op 100% las de oranje roest als donker tegen de roodbruine vloer. Nu is de bovenste
    # 70 procent fel wit staal (lichter dan het bot van stap 0), de roest alleen een gele okerkraag onderaan, en
    # de achterste rij licht staal met een okerkraag. Zo gaat het oog op ware grootte eerst naar deze put.
    STAAL_P = g.mat("put_staal", "f6f8ff", rough=0.22, spec=0.9, metaal=0.4, emis=0.32)
    ROEST_F = g.mat("put_roest", "e8a62a", rough=0.7, spec=0.3, metaal=0.2, emis=0.22)
    ROEST_D = g.mat("put_roestd", "c8801c", rough=0.8, spec=0.2, emis=0.15)
    RAND_D = g.mat("put_randd", "1a0a0a", rough=1.0, spec=0.0)
    rnd_r = random.Random(11)
    hoogtes = (0.74, 1.0, 0.82, 1.06, 0.86, 0.98, 0.76)
    for i, hoog in enumerate(hoogtes):
        x = PUT_X - 0.6 + i * 0.2
        r = 0.098
        kant = (0, math.radians(rnd_r.uniform(-6, 6)), 0)
        z0 = -0.3
        cil("stekel", (x, 0.12, z0 + hoog / 2), r, hoog, STAAL_P, rot=kant, verts=10, r2=0.0)
        k = 0.3   # okerkraag onderaan, net om de stekel heen
        cil("stekelroest", (x, 0.115, z0 + hoog * k / 2), r + 0.012, hoog * k, ROEST_F if i % 3 else ROEST_D,
            rot=kant, verts=10, r2=r * (1 - k) + 0.012)
        cil("stekelrand", (x, 0.2, z0 + (hoog + 0.08) / 2), r + 0.035, hoog + 0.08, RAND_D, rot=kant, verts=10, r2=0.0)
    for i in range(6):   # achterste rij: lager, licht staal met een okerkraag
        x = PUT_X - 0.5 + i * 0.2
        cil("stekel", (x, 0.7, -0.3 + 0.3), 0.08, 0.6, STAAL_L, verts=10, r2=0.0)
        cil("stekelroest", (x, 0.69, -0.3 + 0.09), 0.09, 0.18, ROEST_F, verts=10, r2=0.06)
    HX = PUT_X - 0.6 + 3 * 0.2
    MUTS = g.mat("put_muts", "3d6fe0", rough=0.6)
    cil("puthoed_rand", (HX, 0.1, 0.5), 0.2, 0.035, MUTS, rot=(0, math.radians(-10), 0), verts=20)
    cil("puthoed", (HX + 0.02, 0.1, 0.62), 0.15, 0.26, MUTS, rot=(0, math.radians(-10), 0), verts=20, r2=0.0)
    cil("puthoed_band", (HX, 0.1, 0.53), 0.152, 0.04, g.mat("put_band", "f2c230", rough=0.5), rot=(0, math.radians(-10), 0), verts=20)
    BOT = g.mat("put_bot", "f4eee2", rough=0.35, spec=0.6, emis=0.12)
    bol("putschedel", (PUT_X - 0.4, 0.02, -0.17), (0.13, 0.11, 0.12), BOT, 16)
    for ox in (-0.045, 0.045):
        bol("putschedel_oog", (PUT_X - 0.4 + ox, -0.09, -0.15), (0.03, 0.02, 0.035), PUT_ZWART, 10)
elif PUT_STAP == 2 and not PUT_OUD:
    # Mila 25 nov (issue #76): Deep Pit las na de koop als een stap terug (dunne grijze naaldjes op een zwarte strook,
    # hoed en schedel weg), net als Rusty Spikes ronde 1. Nu: de put van Rusty Spikes, maar nog een stap rijker.
    # Stekels ±25 procent hoger (zelfde wit staal), de kraag wordt glimmend goud, en de put krijgt een lijst: twee
    # houten palen met een gouden dop aan de rand. Twee hoeden op de stekels (blauwe muts en een rode punthoed):
    # er vallen er nu meer in. Schedel blijft. Op 120 px: hoger, meer goud, twee hoeden = zichtbaar beter.
    STAAL_P = g.mat("put_staal", "f6f8ff", rough=0.22, spec=0.9, metaal=0.4, emis=0.32)
    GOUD_K = g.mat("put_goudk", "ffcc33", rough=0.3, spec=0.8, metaal=0.6, emis=0.35)
    RAND_D = g.mat("put_randd", "1a0a0a", rough=1.0, spec=0.0)
    rnd_r = random.Random(13)
    hoogtes = (0.92, 1.24, 1.02, 1.3, 1.08, 1.2, 0.94)
    for i, hoog in enumerate(hoogtes):
        x = PUT_X - 0.6 + i * 0.2
        r = 0.1
        kant = (0, math.radians(rnd_r.uniform(-5, 5)), 0)
        z0 = -0.3
        cil("stekel", (x, 0.12, z0 + hoog / 2), r, hoog, STAAL_P, rot=kant, verts=10, r2=0.0)
        k = 0.24   # gouden kraag onderaan
        cil("stekelgoud", (x, 0.115, z0 + hoog * k / 2), r + 0.014, hoog * k, GOUD_K,
            rot=kant, verts=10, r2=r * (1 - k) + 0.014)
        cil("stekelrand", (x, 0.2, z0 + (hoog + 0.08) / 2), r + 0.035, hoog + 0.08, RAND_D, rot=kant, verts=10, r2=0.0)
    for i in range(6):   # achterste rij: ook hoger, licht staal met een gouden kraag
        x = PUT_X - 0.5 + i * 0.2
        cil("stekel", (x, 0.7, -0.3 + 0.38), 0.085, 0.76, STAAL_L, verts=10, r2=0.0)
        cil("stekelgoud", (x, 0.69, -0.3 + 0.09), 0.095, 0.18, GOUD_K, verts=10, r2=0.065)
    # lijst om de put: twee donkere houten palen met een gouden dop, net buiten de stekels
    PAAL = g.mat("put_paal", "4a2614", rough=0.75)
    for dx in (-0.8, 0.8):
        blok("put_paal", (PUT_X + dx, 0.05, 0.05), (0.13, 0.13, 0.7), PAAL)
        bol("put_dop", (PUT_X + dx, 0.03, 0.43), (0.1, 0.1, 0.08), GOUD_K, 12)
    # hoed 1: de blauwe muts van stap 0 en 1, nu hoger op de langste stekel
    HX = PUT_X - 0.6 + 3 * 0.2
    MUTS = g.mat("put_muts", "3d6fe0", rough=0.6)
    cil("puthoed_rand", (HX, 0.1, 0.74), 0.2, 0.035, MUTS, rot=(0, math.radians(-10), 0), verts=20)
    cil("puthoed", (HX + 0.02, 0.1, 0.86), 0.15, 0.26, MUTS, rot=(0, math.radians(-10), 0), verts=20, r2=0.0)
    cil("puthoed_band", (HX, 0.1, 0.77), 0.152, 0.04, g.mat("put_band", "f2c230", rough=0.5), rot=(0, math.radians(-10), 0), verts=20)
    # hoed 2: een rode punthoed scheef op de tweede stekel
    H2 = PUT_X - 0.6 + 1 * 0.2
    ROOD = g.mat("put_rood", "e0402a", rough=0.6)
    cil("puthoed2_rand", (H2, 0.08, 0.66), 0.17, 0.03, ROOD, rot=(0, math.radians(14), 0), verts=20)
    cil("puthoed2", (H2 - 0.03, 0.08, 0.8), 0.12, 0.3, ROOD, rot=(0, math.radians(14), 0), verts=20, r2=0.0)
    BOT = g.mat("put_bot", "f4eee2", rough=0.35, spec=0.6, emis=0.12)
    bol("putschedel", (PUT_X + 0.42, 0.02, -0.17), (0.13, 0.11, 0.12), BOT, 16)
    for ox in (-0.045, 0.045):
        bol("putschedel_oog", (PUT_X + 0.42 + ox, -0.09, -0.15), (0.03, 0.02, 0.035), PUT_ZWART, 10)
elif PUT_STAP == 0:
    for i in range(6):
        for j in range(3):
            hoog = 0.62 if (i + j) % 2 == 0 else 0.5
            cil("stekel", (PUT_X - 0.6 + i * 0.24, 0.15 + j * 0.38, -0.25 + hoog / 2), 0.07, hoog, STAAL_L, verts=8, r2=0.0)
else:
    # Mila 14 nov: de put per gekochte stap, ontwerp van Daan (ontwerp/steam/put-3d/put_stappen.py ronde d), hier
    # overgenomen zodat de pijplijn put_1 en put_2 kan uitknippen (7e argument). Stap 0 blijft precies zoals hij was.
    rnd_put = random.Random(4)
    STAAL_D = g.mat("staal_d", "8c8a90", rough=0.55, spec=0.5, metaal=0.6)
    ROEST = g.mat("roest_d", "7a3a1a", rough=0.85, spec=0.2, metaal=0.2)
    for i in range(6):
        for j in range(3):
            x, y = PUT_X - 0.6 + i * 0.24, 0.15 + j * 0.38
            if PUT_STAP == 1:   # Rusty Spikes: grijs staal met roestbanden, een derde helemaal roest, iets scheef
                hoog = (0.6 if (i + j) % 2 == 0 else 0.48) + rnd_put.uniform(-0.05, 0.05)
                m = ROEST if (i + j) % 3 == 0 else STAAL_D
                kant = (math.radians(rnd_put.uniform(-14, 14)), math.radians(rnd_put.uniform(-14, 14)), 0)
                cil("stekel", (x, y, -0.25 + hoog / 2), 0.075, hoog, m, rot=kant, verts=8, r2=0.0)
                cil("stekelpunt", (x, y, -0.25 + hoog * 0.85), 0.075 * 0.3, hoog * 0.3, STAAL_L, rot=kant, verts=8, r2=0.0)
                for zb in (0.12, 0.3):
                    cil("roestband", (x, y, -0.25 + zb), 0.075 * (1 - zb / hoog) + 0.008, 0.06, ROEST, rot=kant, verts=8)
            else:               # Deep Pit: langere, dunnere stalen stekels met roestige voet
                hoog = 0.92 if (i + j) % 2 == 0 else 0.78
                cil("stekel", (x, y, -0.42 + 0.18 + hoog / 2), 0.07, hoog, STAAL_L, verts=8, r2=0.0)
                cil("stekelvoet", (x, y, -0.42 + 0.1), 0.08, 0.2, ROEST, verts=8)
    if PUT_STAP == 1:
        for dx in (-0.82, 0.8):
            blok("roestrand", (PUT_X + dx, 0.2, 0.0), (0.12, 0.35, 0.03), ROEST)
    else:   # zwart diep gat, donkere wanden, zwarte brede opening op vloerhoogte, donkere randen met rode band
        ZWART = g.mat("diep", "0b0610", rough=1.0, spec=0.0)
        for o in [o for o in sc.objects if o.name.split(".")[0] == "put_bodem"]:
            bpy.data.objects.remove(o, do_unlink=True)
        blok("put_diep", (PUT_X, 0.7, -0.66), (1.5, 1.5, 0.05), ZWART)
        for dx in (-0.76, 0.76):
            blok("put_wand", (PUT_X + dx, 0.6, -0.35), (0.04, 1.6, 0.62), ZWART)
        blok("put_wand", (PUT_X, 1.35, -0.35), (1.55, 0.04, 0.62), ZWART)
        blok("put_mond", (PUT_X, 0.45, 0.004), (1.72, 0.9, 0.01), ZWART)
        RAND_P = g.mat("putrand_d", "6e4e44", rough=0.85)
        BAND = g.mat("band", "c23a2a", rough=0.6, emis=0.1)
        for dx in (-0.84, 0.84):
            blok("putrand", (PUT_X + dx, 0.25, 0.08), (0.12, 0.5, 0.16), RAND_P)
            blok("putband", (PUT_X + dx, 0.0, 0.1), (0.125, 0.02, 0.05), BAND)
# buit van een gevallen held: een paar munten en zijn helm aan de rand
# Bram 14 nov: alles heet buit..., zodat de pijplijn de putstukken zonder buit knipt (HOL_VERBERG ["buit"]); in het spel
# staat het putstuk los in de gang en werden de halve munten en de helm losse goud- en grijze snippers (kan Daan).
for dx in (-0.85, -0.7, 0.75):
    cil("buit", (PUT_X + dx, 0.5, 0.04), 0.12, 0.03, GOUD, verts=20, rot=(0.2, 0.3, 0))
bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=(PUT_X + 0.95, 0.55, 0.0))
helm = bpy.context.object; helm.name = "buit_helm"; helm.scale = (0.24, 0.22, 0.2); bpy.ops.object.shade_smooth(); helm.data.materials.append(STAAL)
helm.rotation_euler = (0, math.radians(25), 0)

# ingang: fakkel op een paal naast de schacht, met een boogje van stenen
cil("ingangpaal", (-10.0, 0.35, MAAIVELD + 0.45), 0.05, 0.9, HOUT_D, verts=8)
# Daan 13 nov 23:40: zelfde vlam als de gangfakkels, kop bovenop de paal
cil("ingangkop", (-10.0, 0.35, MAAIVELD + 0.93), 0.085 * 1.2, 0.13, DOEK, verts=12, r2=0.1 * 1.2)
druppel("ingangvlam", (-10.0, 0.33, MAAIVELD + 1.03 + 0.12), 0.18, 2.3, V_BUIT, scheef=0.05)
druppel("ingangvlammid", (-10.0, 0.28, MAAIVELD + 1.03 + 0.10), 0.13, 2.0, V_MID, scheef=0.04)
druppel("ingangkern", (-10.0, 0.23, MAAIVELD + 1.03 + 0.06), 0.07, 1.7, V_HART, scheef=0.02)
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
# Ronde 5 (moet 1, Daan): deze lamp loopt nu over de hele breedte, zodat de aarde overal precies het licht van
# de aardtegel krijgt (het spel legt die tegel op elke dichte cel). Zelfde sterkte per vlak als eerst (300 op 10 breed).
TL_BREED = BREED + 40.0
tl = bpy.data.lights.new("tegellicht", "AREA"); tl.shape = "RECTANGLE"; tl.size = TL_BREED; tl.size_y = 3.0
tl.color = (1.0, 0.82, 0.86); tl.energy = TEGEL_LICHT * TL_BREED / 10.0
tlo = bpy.data.objects.new("tegellicht", tl); tlo.location = (0.0, -3.0, 4.6)
tlo.rotation_euler = (math.radians(52), 0, 0); sc.collection.objects.link(tlo)

# Ronde 6b (volgende ronde punt 2, frisse kijker 5b: "weinig contrast tussen gang en aarde"): de achterwand van de
# gang lag in de schaduw van het plafond en was donkerder dan de aarde (37 tegen 48). Een lange warme lamp in de
# gang, naar achteren gericht, alleen op achterwand en vloer (light linking). Even lang als de tegellamp, dus egaal
# in x: de gangtegel past nog steeds op zichzelf. HOL_GANG_LICHT = 0 zet hem uit.
GANG_LICHT = float(os.environ.get("HOL_GANG_LICHT", "60"))
if GANG_LICHT > 0:
    gl_ = bpy.data.lights.new("ganglicht", "AREA"); gl_.shape = "RECTANGLE"; gl_.size = TL_BREED; gl_.size_y = 0.5
    gl_.color = (1.0, 0.78, 0.66); gl_.energy = GANG_LICHT * TL_BREED / 10.0
    glo = bpy.data.objects.new("ganglicht", gl_); glo.location = (0.0, -0.3, GANG_TOP - 0.25)
    glo.rotation_euler = (math.radians(100), 0, 0); sc.collection.objects.link(glo)
    gangwand = bpy.data.collections.new("gangwand")
    for o in sc.objects:
        if o.name.split(".")[0] in ("achterwand", "vloer"):
            gangwand.objects.link(o)
    glo.light_linking.receiver_collection = gangwand

# ---------- Gloop van Daan erin (gloop.py ongewijzigd, alleen het model) ----------
voor = set(bpy.data.objects)
bron = open(os.path.join(HIER, "gloop.py"), encoding="utf-8").read()
begin = bron.index("# ---------- lijf")
eind = bron.index("# ---------- camera")
stuk = bron[begin:eind]
ns = {"bpy": bpy, "g": g, "math": math, "sc": sc, "VERSIE": GLOOP_V, "HOEDEN": HOEDEN, "sys": sys, "os": os}
# Ronde 5c: Gloop hapt naar de ridder (stand uit Daans gloop.py; in het spel bestaat hap ook, slijm.gd)
ns["STAND"] = os.environ.get("HOL_GLOOP_STAND", "hap")
# de hulpjes bol en kegel uit gloop.py
hulp = bron[bron.index("def bol("):begin]
exec(hulp, ns)
exec(stuk, ns)
nieuw = [o for o in bpy.data.objects if o not in voor]
GLOOP_X, GLOOP_Y, GLOOP_S, GLOOP_Z = -0.5, 0.6, 0.95, 0.18   # ronde 5: iets naar links, zodat de berg rechts van hem te zien is
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
    # Ronde 5, frisse kijker: "de helden staan ver van het monster, er gebeurt niets". De ridder staat nu bij de
    # kist en schrikt van Gloop (in het spel: helden lopen naar de schat en Gloop eet ze op).
    held.bouw("ridder", "schrik", plek=(KX0 + 0.75, 0.3, 0.0), draai=25, schaal=0.85, gloed=35, rand=40)
    voor_heks = set(bpy.data.objects)
    held.bouw("heks", "vallen", plek=(PUT_X - 0.25, 0.5, -0.05), draai=20, schaal=0.68, gloed=25, rand=40)
    # Ronde 6c (volgende ronde punt 3, Daan 21:45 kan c): de heks las niet als vallen. Haar hoed blijft los boven
    # de put hangen, zoals in het spel (Brams held_beeld.gd laat de hoed bij een val even hangen). Haar eigen hoed
    # gaat weg, de puntmuts uit hoeden.py hangt scheef boven de put. Naam held_..., dus de tegels hebben hem niet.
    # Ronde 7 (Daan 14 nov 00:40): hoed weer op haar hoofd. Zonder hoed is ze geen heks meer, en de losse hoed
    # viel op ware grootte weg tegen de paarse muur. Het wegvliegen tekent het spel zelf (held_beeld.gd).
    if os.environ.get("HOL_HOED_LOS", "0") == "1":
        for o in [o for o in bpy.data.objects if o not in voor_heks and "heksenhoed" in o.name]:
            bpy.data.objects.remove(o, do_unlink=True)
        import hoeden
        voor_hoed = set(bpy.data.objects)
        hoeden.bouw(1, plek=(PUT_X + 0.62, 0.45, 0.98), schaal=0.62, kantel=28, draai=20)
        for o in bpy.data.objects:
            if o not in voor_hoed:
                o.name = "held_los_" + o.name

# ---------- camera en licht (gedeeld) ----------
g.camera(hoogte_midden=CAM_MIDDEN, schaal=BREED)
g.licht()
# Het gedeelde licht is gezet voor Gloop alleen. In het hol zat "koel" in de achterwand en gaf
# "boven" een vlek op het gras. Zelfde richting en kleur, alleen verplaatst (Gloop krijgt evenveel licht).
for o in sc.objects:
    if o.name == "boven":
        o.location.z = 9.0; o.data.energy *= 2.25
    if o.name == "koel":
        o.location = (-1.6, 1.05, 2.2); o.data.size = 1.0; o.data.energy *= 0.6
for o in sc.objects:
    if o.type == "LIGHT":
        o.visible_camera = False   # de lampen zelf niet in beeld

# Ronde 6 (moet 1, Daan 21:45): de aarde was midden in het beeld 2 keer zo licht als aan de randen (gemeten 42
# links, 85 midden, 49 rechts), want de vier gedeelde lampen staan voor Gloop in het midden en vallen als een
# grote vlek op de voorkant van de aarde. Daardoor kreeg elke kamer een eigen tint en een trede op de celrand.
# Nu schijnen de gedeelde lampen en de lampjes van de helden alleen op Gloop, de helden en de schat
# (light linking in Cycles). De aarde krijgt alleen de lange egale tegellamp: overal hetzelfde licht.
FIGUUR = ("gloop_", "held_", "berg", "munt", "robijn", "safier", "beker", "kist", "deksel")
fig = bpy.data.collections.new("figuren")   # niet aan de scène gehangen: alleen een lijst voor het licht
for o in sc.objects:
    if o.type != "LIGHT" and o.name.startswith(FIGUUR):
        fig.objects.link(o)
for o in sc.objects:
    if o.type == "LIGHT" and o.name.split(".")[0] in ("fakkel", "koel", "boven", "vul", "heldgloed", "heldrand", "staflicht"):
        o.light_linking.receiver_collection = fig
# Ronde 7 (Daan 14 nov 00:40, moet): de achterwand van de put-cel was een lichter roze blok met een harde linkerrand
# (81 links, aflopend naar 64; gang 60 tot 63). Dat was de poel van de gangfakkel links (x -7,2, kolom 3): hij ligt
# vlak naast kolom 4, waar de pijplijn de put uitknipt. In het spel legt de put-tegel naast gangtegels zonder poel,
# dus de rand werd een blok. Het spel tekent zijn fakkels zelf, zonder poel op de muur. Daarom schijnen de twee
# gangfakkels nu alleen op de figuren, net als de gedeelde lampen. HOL_FAKKEL_POEL=1 geeft de poelen terug (alleen
# voor een sfeerplaatje, nooit voor de tegels).
if not FAKKEL_POEL:
    for o in GANGFAKKELS:
        o.light_linking.receiver_collection = fig
if FEL:
    # gedeeld zet de view transform op Standard vlak voor het renderen (en dat wist de look); daarom de look
    # erna, hier in hol.py, zodat de andere modellen niet veranderen. Deze look geeft diepere schaduw en voller licht.
    def _pre(scene, *_):
        scene.view_settings.look = "Medium High Contrast"
    bpy.app.handlers.render_pre.append(_pre)
g.render(uit, W, H, SAMPLES, doorzichtig=True)
print("klaar", uit)
