"""Hoedenwand (Mila, 16 nov 2026): een hoed van een opgegeten held, scheef half begraven in de aardwand.
Rendert alleen holte + hoed + aardrand op een doorzichtige achtergrond, zodat het spel hem op de wand boven de gang legt.
Zelfde camera en licht als alle 3D (gedeeld.py). Hoeden uit producten/steam-hol/modellen/hoeden.py.
    <venv>/bin/python hoedenwand.py <uit.png> <breedte> <hoogte> <samples> <nr> <kantel>
"""
import sys, os, math
M = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../producten/steam-hol/modellen'))
sys.path.insert(0, M)
import bpy
import gedeeld as g
import hoeden

def bol(naam, loc, schaal, mat, segs=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc)
    o = bpy.context.active_object; o.name = naam; o.scale = schaal
    o.data.materials.append(mat); bpy.ops.object.shade_smooth()
    return o

def maak(nr, kantel):
    g.leeg()
    g.camera(hoogte_midden=0.3, schaal=2.7)
    g.licht()
    holte = g.mat("holte", "2e1712", rough=0.95, spec=0.05)
    aarde = g.mat("aarde", "684033", rough=0.9, spec=0.1)
    aarde_l = g.mat("aarde_l", "8e5949", rough=0.85, spec=0.15)
    steen = g.mat("steen", "c69383", rough=0.6, spec=0.3)
    # holte: donkere platte schaal net achter de hoed
    bol("holte", (0, 0.35, 0.28), (0.78, 0.12, 0.52), holte)
    # de hoed, scheef, een stuk naar achteren zodat hij IN de wand zit
    hoeden.bouw(nr, plek=(0, 0.05, 0.02), schaal=1.25, kantel=0, draai=0)
    h = bpy.data.objects["hoed_" + hoeden.NAMEN[nr % 10]]
    h.rotation_euler[1] = math.radians(kantel)   # zijwaarts om, zoals een hoed die viel en bleef steken
    # aardrand voor de onderkant: plat (dat is het wandvlak), met een kam van kluitjes langs de bovenrand en steentjes
    bol("rand", (0, -0.45, -0.22), (1.0, 0.08, 0.36), aarde)
    import random; random.seed(nr)
    for i in range(11):
        x = -0.85 + i * 0.17 + random.uniform(-0.03, 0.03)
        z = 0.1 - abs(x) * 0.18 + random.uniform(-0.03, 0.03)
        r = random.uniform(0.08, 0.12)
        bol("kluit", (x, -0.5, z), (r, r * 0.7, r * 0.8), aarde_l if i % 3 else aarde, segs=16)
    for x, z, r in [(-0.6, -0.15, 0.05), (0.5, -0.1, 0.045), (0.1, -0.3, 0.04)]:
        bol("steen", (x, -0.56, z), (r, r * 0.8, r * 0.85), steen, segs=16)

if __name__ == "__main__":
    uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    maak(int(sys.argv[5]), float(sys.argv[6]))
    g.render(uit, W, H, S, doorzichtig=True)
