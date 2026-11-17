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
BASIS, SLAG, MOS = "6e6b67", "5d5a56", "3c5228"   # 17 nov 02:45: basis een tikje lichter (kan Daan)
GROOT = 1.07   # 17 nov 02:45 (kan Daan): in de gang op 1x was hij even groot en donker als een ton
GROEF_AS = Vector((0.0, 0.42, 1.0)).normalized()   # normaal van het groefvlak: band loopt schuin, zichtbaar in elke stand


# 17 nov 02:45 (kan Daan): groot leest de groef als een strak touw. Op twee plekken is hij weggesleten,
# dan is het een kerf in steen. heel(n) is 1 in de groef en zakt naar 0 bij de twee breuken.
_B2 = Vector((-0.5, -0.85, 0.36)).normalized()


def heel(n):
    """1 in de groef, 0 in één breuk. Eén, niet twee of drie: meer breuken lazen als stippellijn (stiksel), GEZIEN."""
    bp = (_B2 - GROEF_AS * _B2.dot(GROEF_AS)).normalized()
    t = (1 - n.dot(bp)) / 0.06                       # 0 midden in de breuk, 1 op ±20 graden
    return min(1.0, max(0.0, t))


def steen(ouder, draai=0.0):
    # Proef 2 (Daan 17 nov 01:30): onder het gedeelde licht werd 8e8a86 blauwig bbb9ca en de vlakken beige.
    # Daarom basis warmer en donkerder, zodat hij in beeld op 8e8a86 tot a8a39c uitkomt; vlakken dezelfde
    # tint een stap donkerder; geen lichte rand meer (gestippeld las als stiksel); mos donkerder en kleiner.
    steen_m = g.mat("rolsteen", BASIS, rough=0.95, spec=0.05)
    nt = steen_m.node_tree
    attr = nt.nodes.new("ShaderNodeVertexColor")
    attr.layer_name = "kleur"
    nt.links.new(attr.outputs["Color"], nt.nodes["Principled BSDF"].inputs["Base Color"])
    groef_m = g.mat("rolsteen_groef", "2e2a26", rough=1.0, spec=0.0)
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
        kerf = -0.016 * max(0.0, 1 - (abs(d) / 0.05) ** 2) * min(1.0, heel(n) * 1.5)  # ondiepe groef: geen twee opbollende helften
        v.co = n * (STRAAL + bult + kerf)
        v.co.z *= 0.92
    # twee afgeslagen platte vlakken: alles voorbij het vlak terug op het vlak
    slagen = [(Vector((-0.55, -0.6, 0.45)).normalized(), 0.43), (Vector((0.7, -0.35, -0.2)).normalized(), 0.45)]
    for v in bm.verts:
        for n, afst in slagen:
            t = v.co.dot(n)
            if t > afst:
                v.co -= n * (t - afst)
    o.data.materials.append(steen_m)
    o.data.materials.append(groef_m)
    # Kleur per hoekpunt (zacht verloop), niet per vlak: per vlak gaf kartelranden om vlakken en mos.
    mos_plek = Vector((0.2, -0.15, 1.0)).normalized()
    srgb = lambda h: tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))   # bytekleur wil sRGB
    basis, slag, mos = srgb(BASIS), srgb(SLAG), srgb(MOS)
    laag = bm.loops.layers.color.new("kleur")

    def glad(a, b, x):
        t = min(1.0, max(0.0, (x - a) / (b - a)))
        return t * t * (3 - 2 * t)

    kleur_v = {}
    for v in bm.verts:
        n = v.co.normalized()
        k = glad(-0.012, 0.0, max(v.co.dot(sn) - afst for sn, afst in slagen))
        m = glad(0.90, 0.94, n.dot(mos_plek) + noise.noise(n * 6) * 0.025)
        c = [basis[i] * (1 - k) + slag[i] * k for i in range(3)]
        c = [c[i] * (1 - m) + mos[i] * m for i in range(3)]
        kleur_v[v.index] = (*c, 1.0)
    for f in bm.faces:
        c = f.calc_center_median()
        d = abs(Vector((c.x, c.y, c.z / 0.92)).normalized().dot(GROEF_AS))
        if d < 0.042 and heel(Vector((c.x, c.y, c.z / 0.92)).normalized()) > 0.5:   # één breuk; breedte laten wisselen kan niet, de groef is één rij vlakken
            f.material_index = 1
        for lp in f.loops:
            lp[laag] = kleur_v[lp.vert.index]
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
        o.rotation_euler = (0, R(-32), R(25))      # proef 2: minder gekanteld (rechtop las als ei of walnoot), mos opzij, groef schuin
        o.location = (0, 0, STRAAL * 0.93)
    elif stand == "rol":
        o = steen(ouder, draai=0)
        o.rotation_euler = (0, R(-draai), 0)      # rolt langs de gang: om de as naar de camera
    else:
        steen(ouder)
        hout = g.mat("rolsteen_wig", "7a4a26", rough=0.75)   # proef 2: 5e3b22 viel weg in de bruine gangwand op spelmaat
        hd._kegel(ouder, (0.52, -0.02, 0.12), 0.26, 0.26, 0.55, hout, rot=(R(90), 0, R(0)), verts=3)
        bpy.ops.object.shade_flat()
        touw = g.mat("rolsteen_touw", "6a4e2c", rough=0.95)   # Daan: touwtje mag donkerder
        hd._kegel(ouder, (0.62, -0.28, 0.17), 0.014, 0.014, 0.34, touw, rot=(R(10), R(-25), 0), verts=8)
        hd._bol(ouder, (0.66, -0.25, 0.02), (0.05, 0.05, 0.03), touw, segs=12)
    ouder.location = plek
    ouder.scale = (GROOT, GROOT, GROOT)
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
