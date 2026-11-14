"""Gloop in 3D (Daan, 13 nov 2026). Vanaf de proef van de hoofdchat (ontwerp/steam/proef-3d/gloop.py).

Draai:  <venv>/bin/python gloop.py <uit.png> <versie> <hoeden> <breedte> <hoogte> <samples>
  versie 1 = Speelgoed (rond, glanzend, groot oog, open lach)
  versie 2 = Muntje   (1 plus een gouden munt die half in zijn buik zit)
  versie 3 = Schatbuik (doorschijnend lijf met munten en belletjes erin)
  hoeden  = 0 tot 4 (helm, kroon, heksenhoed, rode muts), scheef op elkaar
  stand   = (optioneel, 7e woord) rust (standaard), knipper (oog dicht), blij (oog als boogje omhoog,
            grotere lach), hap (mond wijd open). Voor de pijplijn van Bram: elke stand een eigen beeld.

Lessen uit de pixelrondes (kijkers 1 tot 7): oog met veel wit en een ronde pupil met één glimstip,
een open lach (geen streepje), hoeden echt óp het hoofd, kroon zonder donkere binnenkant
(las als gezichtje), geen druppelvorm (las als breder lijf).
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g

uit = sys.argv[1]
VERSIE = int(sys.argv[2]); HOEDEN = int(sys.argv[3])
W, H, SAMPLES = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
STAND = sys.argv[7] if len(sys.argv) > 7 else "rust"

g.leeg()
sc = bpy.context.scene


def bol(naam, loc, schaal, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; o.scale = schaal
    bpy.ops.object.shade_smooth(); o.data.materials.append(m); return o


def kegel(naam, loc, r1, r2, h, m, kantel=0, verts=48):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2, depth=h, location=loc,
                                    rotation=(0, math.radians(kantel), 0))
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); o.data.materials.append(m); return o


# ---------- lijf ----------
mb = bpy.data.metaballs.new("lijf"); mb.resolution = 0.05; mb.render_resolution = 0.025; mb.threshold = 0.6
lijf = bpy.data.objects.new("lijf", mb); sc.collection.objects.link(lijf)
# breder dan hoog, iets scheef: rechts een tikje hoger (kijkt naar de schat)
for (x, y, z, r) in [(0, 0, 0.55, 1.2), (0.08, 0, 0.85, 0.8), (-0.65, 0, 0.3, 0.72),
                     (0.68, 0, 0.3, 0.68), (0, -0.2, 0.25, 0.95)]:
    e = mb.elements.new(); e.co = (x, y, z); e.radius = r
if VERSIE == 3:
    lijfmat = g.mat("lijf", "munt", rough=0.08, spec=0.7, glas=0.55, sss=0.15)
else:
    lijfmat = g.mat("lijf", "munt", rough=0.22, spec=0.6, sss=0.3)
lijf.data.materials.append(lijfmat)

# vloer die alleen schaduw vangt (doorzichtig plaatje, wel een contactschaduw)
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
vloer = bpy.context.object; vloer.is_shadow_catcher = True

# ---------- gezicht ----------
# Voorkant van het lijf ligt rond y = -1.05 op ooghoogte. Oog groot en iets rechts van het midden.
OX, OZ = 0.16, 0.98
_stand = globals().get("STAND", "rust")   # hol.py leest dit stuk in zonder STAND: dan rust
if _stand in ("knipper", "blij"):
    # oog dicht: een donker boogje op de plek van het oog (knipper hangt, blij staat omhoog als ^)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.3, minor_radius=0.065, location=(OX, -1.06, OZ + (0.1 if _stand == "knipper" else -0.12)),
                                     rotation=(math.radians(90), 0, 0))
    ooglid = bpy.context.object; ooglid.data.materials.append(g.mat("pupil", "pupil", rough=0.35, spec=0.2))
    bpy.ops.mesh.primitive_cube_add(size=1, location=(OX, -1.06, OZ + (0.4 if _stand == "knipper" else -0.42))); sn_o = bpy.context.object
    sn_o.scale = (1.0, 0.5, 0.6); sn_o.hide_render = True; sn_o.hide_viewport = True
    mo = ooglid.modifiers.new("snij", "BOOLEAN"); mo.object = sn_o; mo.operation = "DIFFERENCE"
    ooglid.scale = (1.0, 0.4 if _stand == "knipper" else 0.85, 1.0)   # lokaal y is na het kantelen de hoogte
else:
    bol("oogwit", (OX, -0.98, OZ), (0.44, 0.22, 0.46), g.mat("oogwit", "oogwit", rough=0.18, spec=0.5))
    bol("pupil", (OX + 0.07, -1.17, OZ - 0.02), (0.21, 0.07, 0.23), g.mat("pupil", "pupil", rough=0.35, spec=0.2))
    bol("glim", (OX + 0.15, -1.235, OZ + 0.09), (0.07, 0.03, 0.07), g.mat("glim", "oogwit", emis=4.0))
# open lach: halve schijf (mond), tong, één tand, scheef
bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=0.26, depth=0.12, location=(0.02, -1.0, 0.46),
                                    rotation=(math.radians(90), math.radians(-10), 0))
mond = bpy.context.object; mond.data.materials.append(g.mat("mond", "mond", rough=0.6))
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.02, -1.0, 0.62)); snij = bpy.context.object
snij.scale = (0.8, 0.5, 0.32); snij.rotation_euler = (0, math.radians(-10), 0); snij.hide_render = True; snij.hide_viewport = True
m1 = mond.modifiers.new("snij", "BOOLEAN"); m1.object = snij; m1.operation = "DIFFERENCE"
mond.scale = (1.15, 1.0, 0.85)
if _stand == "blij":
    mond.scale = (1.35, 1.0, 1.05)
if _stand == "hap":
    # Daan 13 nov 17:45: hap is een open O (ronde bovenkant), geen diepe lach. Halve schijf las als lach
    # (frisse kijker); nu een hele ovaal, lager, met de tand aan de bovenlip.
    mond.modifiers.remove(m1)
    mond.location = (0.04, -1.0, 0.24); mond.scale = (1.5, 1.0, 1.12)
bol("tong", (0.0, -1.03 if _stand != "hap" else -1.07, 0.37 if _stand != "hap" else 0.07), (0.15, 0.06, 0.07) if _stand != "hap" else (0.24, 0.07, 0.09), g.mat("tong", "tong", rough=0.4))
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.14, -1.12, 0.565) if _stand != "hap" else (0.10, -1.12, 0.49)); tand = bpy.context.object
tand.scale = (0.10, 0.05, 0.09); tand.rotation_euler = (0, math.radians(-10), 0)
bev = tand.modifiers.new("rond", "BEVEL"); bev.width = 0.02; bev.segments = 3
tand.data.materials.append(g.mat("tand", "tand", rough=0.3))
# blosjes
blos = g.mat("blos", "blos", rough=0.7)
bol("blos_l", (-0.48, -0.93, 0.62), (0.13, 0.04, 0.07), blos, rot=(0, 0, math.radians(-25)))
bol("blos_r", (0.70, -0.86, 0.62), (0.12, 0.04, 0.065), blos, rot=(0, 0, math.radians(30)))

# ---------- eigen trek ----------
goud = g.mat("goud", "goud", rough=0.18, spec=1.0, metaal=0.9, emis=0.12)


def munt(naam, loc, kantel_x, kantel_y, r=0.2):
    bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=r, depth=0.06, location=loc,
                                        rotation=(math.radians(kantel_x), math.radians(kantel_y), 0))
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth()
    bev = o.modifiers.new("rond", "BEVEL"); bev.width = 0.015; bev.segments = 2
    o.data.materials.append(goud)
    # ingeslagen streep, zodat het een munt is en geen knoop
    bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=r * 0.62, depth=0.075, location=loc,
                                        rotation=(math.radians(kantel_x), math.radians(kantel_y), 0))
    rim = bpy.context.object; rim.data.materials.append(g.mat(naam + "_d", "goud_d", rough=0.3, metaal=0.8))
    return o


if VERSIE == 2:
    # half in de buik gezakt, linksonder, schuin
    munt("munt", (-0.55, -0.92, 0.32), 72, 18, r=0.24)
if VERSIE == 3:
    munt("munt1", (-0.42, -0.35, 0.32), 80, 25, r=0.22)
    munt("munt2", (0.5, -0.3, 0.28), 70, -30, r=0.2)
    bel = g.mat("bel", "munt_l", rough=0.05, glas=0.9)
    for (x, z, r) in [(-0.15, 0.25, 0.06), (0.25, 0.65, 0.05), (-0.6, 0.7, 0.045), (0.75, 0.55, 0.04)]:
        bol("bel", (x, -0.5, z), (r, r, r), bel)

# ---------- Royal-stukken (Daan 14 nov): cape, zoom, ster ----------
# Stand cape, zoom of ster rendert alleen dat stuk, met dezelfde camera als rust (hoeden 0), zodat de pijplijn
# het als los frame op de plek van de oude pixels kan leggen (slijm.gd: cape vóór het lijf getekend, zoom en ster erna).
# Uitwerking in royal.py. hol.py leest dit stuk wel in, maar zonder STAND is het rust en gebeurt hier niets.
if _stand in ("cape", "zoom", "ster"):
    import royal
    royal.bouw(_stand, [o for o in sc.objects if o.type == "MESH" or o.type == "META"], vloer)
    _voor_toren = set(sc.objects)

# ---------- hoedentoren ----------
TOP = 1.52  # bovenkant van het lijf
z = TOP - 0.1
kantel = -7
x = 0.08
hoeden = []
# icoon (Daan 14 nov): GLOOP_ICOON=1 zet alleen de kroon op het hoofd, zonder helm eronder.
# Zonder die variabele verandert er niets voor het spel of de pijplijn.
ICOON = os.environ.get("GLOOP_ICOON") == "1"
if ICOON:
    HOEDEN = 2
    z = TOP - 0.24; kantel = 8
if HOEDEN >= 1 and not ICOON:   # helm van de ridder
    staal = g.mat("staal", "staal", rough=0.28, spec=0.8, metaal=0.85)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=(x, 0, z))
    helm = bpy.context.object; helm.scale = (0.58, 0.58, 0.68); helm.rotation_euler = (0, math.radians(kantel), 0)
    bpy.ops.object.shade_smooth(); helm.data.materials.append(staal)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0, z - 0.3)); sn = bpy.context.object
    sn.scale = (2, 2, 0.6); sn.hide_render = True; sn.hide_viewport = True
    bm = helm.modifiers.new("snij", "BOOLEAN"); bm.object = sn; bm.operation = "DIFFERENCE"
    kegel("helmrand", (x, 0, z + 0.01), 0.63, 0.63, 0.08, staal, kantel)
    if HOEDEN == 1:
        # ronde 3: rode pluim zoals op de helm van de ridder (held.py); alleen als de helm bovenop staat
        pl = g.mat("pluim", "rood", rough=0.7)
        for px, pz, ps in [(0.0, 0.74, 0.2), (0.13, 0.88, 0.18), (0.28, 0.95, 0.15), (0.42, 0.93, 0.12)]:
            bol("pluim", (x - 0.03 + px, 0, z + pz), (ps, ps * 0.8, ps), pl)
        PLUIM_TOP = z + 1.1   # voor de camera: de pluim mag niet uit beeld vallen
    else:
        kegel("helmpunt", (x - 0.03, 0, z + 0.6), 0.07, 0.0, 0.18, staal, kantel)
        if globals().get("PLUIM_KNAK", False):
            # capsule (Daan 14 nov): de rode pluim van de ridder hangt geknakt langs de helm,
            # zodat je ziet dat het dezelfde helm is als die van de ridder. Standaard uit (spel ongewijzigd).
            pl = g.mat("pluim", "rood", rough=0.7)
            for px, py, pz, ps in [(-0.28, -0.1, 0.5, 0.2), (-0.48, -0.13, 0.48, 0.18),
                                   (-0.64, -0.16, 0.36, 0.16), (-0.72, -0.18, 0.18, 0.14), (-0.74, -0.18, 0.01, 0.11)]:
                bol("pluim", (x + px, py, z + pz), (ps, ps * 0.85, ps), pl)
    # ronde 2: neusstuk weg, het las als een staafje dat in het oog prikt
    z += 0.5; x -= 0.03; kantel = 9
if HOEDEN >= 2:   # kroon van de koning: open, zonder donkere binnenkant
    kr = g.mat("kroon", "goud", rough=0.16, spec=1.0, metaal=0.9, emis=0.1)
    # ronde 2: drie grote gladde punten met een bolletje erop (las in ronde 1 als kluwen met vijf scherpe)
    kegel("kroonband", (x, 0, z + 0.12), 0.40, 0.42, 0.24, kr, kantel)
    for a_g in (215, 270, 325):
        a = math.radians(a_g)
        px, py = x + 0.36 * math.cos(a), 0.36 * math.sin(a)
        hoog = 0.42 if a_g == 270 else 0.34
        kegel("kroonpunt", (px, py, z + 0.24 + hoog / 2), 0.15, 0.0, hoog, kr, kantel, verts=24)
        # ronde 3: bolletje precies op de punt (zweefde erboven): de kegel kantelt om zijn midden
        k = math.radians(kantel)
        bol("kroonbol", (px + math.sin(k) * hoog / 2, py, z + 0.24 + hoog / 2 + math.cos(k) * hoog / 2 + 0.01), (0.06, 0.06, 0.06), kr)
    bol("steen", (x, -0.43, z + 0.12), (0.08, 0.04, 0.08), g.mat("robijn", "rood", rough=0.1, emis=0.3))
    z += 0.5; x += 0.05; kantel = -11   # ronde 3: 0,42 werd 0,5, de heksenhoed zakte over de kroonpunten
if HOEDEN >= 3:   # heksenhoed: breed en paars met een gouden band, punt knakt
    pa = g.mat("paars", "paars", rough=0.65)
    kegel("hoedrand", (x, 0, z + 0.04), 0.58, 0.58, 0.05, pa, kantel)
    kegel("hoedband", (x, 0, z + 0.11), 0.36, 0.34, 0.09, g.mat("band", "goud", rough=0.3, metaal=0.6), kantel)
    kegel("hoed", (x - 0.03, 0, z + 0.45), 0.35, 0.05, 0.7, pa, kantel)
    kegel("hoedpunt", (x - 0.16, 0, z + 0.86), 0.06, 0.0, 0.2, pa, kantel - 35)
    z += 0.82; x -= 0.14; kantel = 6
if HOEDEN >= 4:   # rood mutsje met pompon, bovenop de geknakte punt
    ro = g.mat("rood", "rood", rough=0.7)
    kegel("muts", (x, 0, z + 0.1), 0.17, 0.08, 0.2, ro, kantel)
    bol("pompon", (x - 0.01, 0, z + 0.26), (0.08, 0.08, 0.08), g.mat("wol", "oogwit", rough=0.95))
    z += 0.3

# ---------- camera en licht (gedeeld) ----------
if _stand in ("cape", "zoom", "ster"):   # hoeden alleen voor de camera (proefbeelden met toren), niet in de render
    for o in sc.objects:
        if o not in _voor_toren:
            o.hide_render = True
hoogste = max(TOP, z + 0.15, globals().get("PLUIM_TOP", 0))
midden = hoogste / 2 - 0.25
schaal = max(3.0, hoogste * 1.08 + 0.45)
g.camera(hoogte_midden=midden, schaal=schaal)
g.licht()
g.render(uit, W, H, SAMPLES, doorzichtig=True)
print("klaar", uit)
