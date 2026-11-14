"""Proef fakkel in 3D (Daan, 13 nov 2026). Links de huidige fakkel uit hol.py, dan voorstel A en B.
Draai: <venv>/bin/python fakkel.py uit.png breedte hoogte samples [doorzichtig 0/1]
Waarom: in de deco-laag las de huidige vlam als een wit ei op een stokje (wattenstaafje). Oorzaak: emissie 9 en 14
met view transform Standard knipt alles naar wit. Een fakkel leest pas als fakkel met een oranje druppel met punt,
een geel hart, een donkere omwikkelde kop en een ijzeren beugel aan de muur.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../producten/steam-hol/modellen"))
import bpy
import gedeeld as g

uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
DOOR = (sys.argv[5] == "1") if len(sys.argv) > 5 else False
g.leeg()
sc = bpy.context.scene


def kies(o, m):
    o.data.materials.append(m); return o


def bol(naam, loc, schaal, m, segs=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=max(8, segs // 2), location=loc)
    o = bpy.context.object; o.name = naam; o.scale = schaal
    bpy.ops.object.shade_smooth(); return kies(o, m)


def cil(naam, loc, r, d, m, rot=(0, 0, 0), verts=24, r2=None):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; o.name = naam; bpy.ops.object.shade_smooth(); return kies(o, m)


def druppel(naam, loc, r, hoog, m, scheef=0.0):
    """Vlam als druppel: onderkant bol, boven een punt die iets opzij buigt (flakkert)."""
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=14, radius=1, location=(0, 0, 0))
    o = bpy.context.object; o.name = naam
    for v in o.data.vertices:
        z = v.co.z
        if z > 0:  # bovenhelft trekken tot een punt
            t = z
            k = (1 - t) ** 1.6
            v.co.x *= k; v.co.y *= k
            v.co.z = z * hoog
            v.co.x += scheef * t * t
    o.scale = (r, r * 0.85, r); o.location = loc
    o.visible_shadow = False  # een vlam geeft licht, geen schaduw
    bpy.ops.object.shade_smooth(); return kies(o, m)


# --- huidige (hol.py) ---
HOUT = g.mat("hout", "8a4b2a", rough=0.7, spec=0.2)
HOUT_D = g.mat("hout_d", "5a2e1c", rough=0.75)
VLAM = g.mat("vlam", "ffb347", emis=9.0)
VLAM_K = g.mat("vlamkern", "fff1b0", emis=14.0)


def huidig(x, z=1.0):
    cil("steel", (x, 1.0, z - 0.25), 0.05, 0.55, HOUT_D, rot=(math.radians(-18), 0, 0), verts=8)
    cil("kop", (x, 0.92, z + 0.05), 0.09, 0.12, HOUT, verts=10)
    bol("vlam", (x, 0.9, z + 0.24), (0.14, 0.11, 0.26), VLAM, 12).visible_shadow = False
    bol("vlamkern", (x, 0.85, z + 0.2), (0.06, 0.05, 0.1), VLAM_K, 10).visible_shadow = False


# --- nieuw ---
HOUT2 = g.mat("hout2", "6e4632", rough=0.75, spec=0.2)      # zelfde donkerder hout als de kamers (ronde 5)
DOEK = g.mat("doek", "3a2418", rough=0.9, spec=0.1)          # omwikkelde kop met pek
IJZER = g.mat("ijzer", "3b3640", rough=0.45, metaal=0.8)
V_BUIT = g.mat("v_buit", "ff5a1f", emis=1.6)                 # rood-oranje rand
V_MID = g.mat("v_mid", "ff9b2a", emis=2.4)                   # oranje
V_HART = g.mat("v_hart", "ffe27a", emis=3.2)                 # geel hart, net niet wit


def nieuw(x, z=1.0, beugel=True, groot=1.0):
    y = 1.0
    if beugel:  # ijzeren plaatje op de muur en een ring om de steel
        cil("beugelplaat", (x, y + 0.12, z - 0.18), 0.07, 0.03, IJZER, rot=(math.radians(90), 0, 0), verts=6)
        cil("beugelarm", (x, y + 0.04, z - 0.14), 0.018, 0.16, IJZER, rot=(math.radians(90), 0, 0), verts=8)
        cil("beugelring", (x, y - 0.03, z - 0.12), 0.07, 0.04, IJZER, verts=16)
    cil("steel", (x, y - 0.03, z - 0.25), 0.055, 0.6, HOUT2, rot=(math.radians(-12), 0, 0), verts=10, r2=0.035)
    cil("kop", (x, y - 0.06, z + 0.07), 0.085 * groot, 0.13, DOEK, verts=12, r2=0.1 * groot)
    zv = z + 0.16
    druppel("vlam_buit", (x, y - 0.08, zv + 0.10 * groot), 0.15 * groot, 2.3, V_BUIT, scheef=0.05)
    druppel("vlam_mid", (x, y - 0.13, zv + 0.08 * groot), 0.11 * groot, 2.0, V_MID, scheef=0.04)
    druppel("vlam_hart", (x, y - 0.18, zv + 0.05 * groot), 0.06 * groot, 1.7, V_HART, scheef=0.02)
    d = bpy.data.lights.new("fakkellicht", "POINT"); d.color = (1.0, 0.6, 0.28); d.energy = 25; d.shadow_soft_size = 0.15
    o = bpy.data.objects.new("fakkellicht", d); o.location = (x, y - 0.35, zv + 0.15); sc.collection.objects.link(o)


huidig(-0.8)
nieuw(0.0, groot=1.2)  # gekozen: met beugel, vlam 1,2
nieuw(0.8, beugel=False, groot=1.2)

# muur erachter (alleen als niet doorzichtig) zodat je de leesbaarheid op pruim ziet
if not DOOR:
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 1.4, 1.0), rotation=(math.radians(90), 0, 0))
    p = bpy.context.object; p.data.materials.append(g.mat("muur", "4a2e4f", rough=0.9))
g.camera(hoogte_midden=1.1, schaal=2.4)
g.licht()
g.render(uit, W, H, S, doorzichtig=DOOR)
