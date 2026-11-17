"""De rolsteen (Mila, 17 nov 2026, ontwerp Daan in ontwerp/steam/rolsteen-edelman/ontwerp.md).

Een steen die je aan ziet dat hij gaat rollen: bultige bol (1 : 0,92), een ingekerfde groef rondom (donker
6e6860 met een lichte rand d8d0c0 erlangs) die je ziet draaien als hij rolt, twee platte afgeslagen vlakken
en een vlek mos bovenop. Klaar = op een houten wig met touwtje; niet klaar = zonder wig, gekanteld, mos opzij.

Daans proef (17 nov) las als bal of ei: glad, en de band als torus stak uit als een ring. Daarom hier:
ruis op de vorm, de groef als echte inkeping (vlakken bij het groefvlak naar binnen geduwd) en de kleur per
vlak, geen losse ring.

Draaien: <venv>/bin/python rolsteen.py <uit.png> <breedte> <hoogte> <samples> [stand] [draai]
  stand = klaar | niet_klaar | rol   (rol: alleen de steen, `draai` graden om de rolas: 12 beelden = 30 graden per stap)
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy, bmesh
from mathutils import Vector, noise
import gedeeld as g
import hoeden as hd

R = math.radians
STRAAL = 0.5
GROEF_AS = Vector((0.0, 0.42, 1.0)).normalized()   # normaal van het groefvlak: band loopt schuin, zichtbaar in elke stand


def steen(ouder, draai=0.0):
    steen_m = g.mat("rolsteen", "8e8a86", rough=0.95, spec=0.1)
    groef_m = g.mat("rolsteen_groef", "5e5850", rough=0.95, spec=0.05)
    rand_m = g.mat("rolsteen_rand", "d8d0c0", rough=0.85, spec=0.15)
    mos_m = g.mat("rolsteen_mos", "6f8f4a", rough=0.95)
    slag_m = g.mat("rolsteen_slag", "98938c", rough=0.8, spec=0.2)
    me = bpy.data.meshes.new("rolsteen")
    o = bpy.data.objects.new("rolsteen_bol", me)
    bpy.context.scene.collection.objects.link(o)
    bm = bmesh.new()
    # bol met zijn polen op de groefas: dan lopen de ringen evenwijdig aan de groef en is de band strak (ico gaf zaagtand)
    bmesh.ops.create_uvsphere(bm, u_segments=72, v_segments=56, radius=STRAAL)
    rot = Vector((0, 0, 1)).rotation_difference(GROEF_AS).to_matrix()
    for v in bm.verts:
        v.co = rot @ v.co
    for v in bm.verts:
        n = v.co.normalized()
        bult = noise.noise(n * 1.6 + Vector((3.1, 0.7, 1.9))) * 0.07 + noise.noise(n * 4.0) * 0.018
        d = n.dot(GROEF_AS)
        kerf = -0.045 * max(0.0, 1 - (abs(d) / 0.075) ** 2)          # de groef: een echte inkeping
        v.co = n * (STRAAL + bult + kerf)
        v.co.z *= 0.92
    # twee afgeslagen platte vlakken: alles voorbij het vlak terug op het vlak
    slagen = [(Vector((-0.55, -0.6, 0.45)).normalized(), 0.40), (Vector((0.7, -0.35, -0.2)).normalized(), 0.43)]
    for v in bm.verts:
        for n, afst in slagen:
            t = v.co.dot(n)
            if t > afst:
                v.co -= n * (t - afst)
    o.data.materials.append(steen_m)
    for m in (groef_m, rand_m, mos_m, slag_m):
        o.data.materials.append(m)
    mos_plek = Vector((0.2, -0.15, 1.0)).normalized()
    for f in bm.faces:
        c = f.calc_center_median()
        n = c.normalized()
        d = abs(Vector((c.x, c.y, c.z / 0.92)).normalized().dot(GROEF_AS))
        if d < 0.05:
            f.material_index = 1
        elif d < 0.075:
            f.material_index = 2
        elif any(c.dot(sn) > afst - 0.004 for sn, afst in slagen):
            f.material_index = 4
        elif n.dot(mos_plek) > 0.86 + noise.noise(n * 6) * 0.05:
            f.material_index = 3
    bm.to_mesh(me); bm.free()
    for p in me.polygons:
        p.use_smooth = True
    o.parent = ouder
    o.location = (0, 0, STRAAL * 0.92)
    o.rotation_euler = (R(draai), 0, 0)   # rolas = x (hij rolt naar links of rechts door de gang)
    return o


def bouw(stand="klaar", plek=(0, 0, 0), draai=0.0):
    ouder = bpy.data.objects.new("rolsteen", None)
    bpy.context.scene.collection.objects.link(ouder)
    if stand == "niet_klaar":
        o = steen(ouder, draai=0)
        o.rotation_euler = (0, R(-75), R(15))      # gekanteld tegen de wand: mos opzij
        o.location = (0, 0, STRAAL * 0.96)
    elif stand == "rol":
        o = steen(ouder, draai=0)
        o.rotation_euler = (0, R(-draai), 0)      # rolt langs de gang: om de as naar de camera
    else:
        steen(ouder)
        hout = g.mat("rolsteen_wig", "5e3b22", rough=0.75)   # Daan: oranje driehoekje, mag donkerder hout
        hd._kegel(ouder, (0.5, -0.02, 0.09), 0.2, 0.2, 0.5, hout, rot=(R(90), 0, R(0)), verts=3)
        bpy.ops.object.shade_flat()
        touw = g.mat("rolsteen_touw", "c8a870", rough=0.9)
        hd._kegel(ouder, (0.62, -0.28, 0.17), 0.014, 0.014, 0.34, touw, rot=(R(10), R(-25), 0), verts=8)
        hd._bol(ouder, (0.66, -0.25, 0.02), (0.05, 0.05, 0.03), touw, segs=12)
    ouder.location = plek
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    stand = sys.argv[5] if len(sys.argv) > 5 else "alle"
    draai = float(sys.argv[6]) if len(sys.argv) > 6 else 0
    g.leeg()
    if stand == "alle":
        bouw("klaar", (-1.4, 0, 0))
        bouw("niet_klaar", (0.0, 0, 0))
        bouw("rol", (1.4, 0, 0), draai=45)
        g.camera(hoogte_midden=0.45, schaal=4.4)
    else:
        bouw(stand, draai=draai)
        g.camera(hoogte_midden=0.45, schaal=1.7)
    g.licht()
    g.render(uit, W, H, S, doorzichtig=True)
    print("klaar", uit)
