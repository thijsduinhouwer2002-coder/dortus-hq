"""Wortels die van het gras de aarde in hangen (Mila, 16 nov 2026). Vult de bovenrand van de aardwand.
    <venv>/bin/python wortels.py <uit.png> <breedte> <hoogte> <samples> <zaad>
Doorzichtig, zelfde camera en licht (gedeeld.py). Bovenkant van het plaatje = onderkant van het gras.
"""
import sys, os, math, random
M = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../producten/steam-hol/modellen'))
sys.path.insert(0, M)
import bpy
from mathutils import Vector
import gedeeld as g

def buis(naam, punten, r0, mat):
    cu = bpy.data.curves.new(naam, 'CURVE'); cu.dimensions = '3D'
    cu.bevel_depth = r0; cu.bevel_resolution = 4
    sp = cu.splines.new('BEZIER'); sp.bezier_points.add(len(punten) - 1)
    for i, p in enumerate(punten):
        b = sp.bezier_points[i]; b.co = p; b.handle_left_type = b.handle_right_type = 'AUTO'
        b.radius = max(0.15, 1.0 - i / (len(punten) - 1))
    o = bpy.data.objects.new(naam, cu); bpy.context.scene.collection.objects.link(o)
    o.data.materials.append(mat); return o

def maak(zaad):
    random.seed(zaad)
    g.leeg(); g.camera(hoogte_midden=-0.6, schaal=3.0); g.licht()
    hout = g.mat("wortel", "b5835a", rough=0.8, spec=0.15)
    hout_d = g.mat("wortel_d", "7e5236", rough=0.85, spec=0.1)
    for k in range(random.randint(2, 3)):
        x = random.uniform(-1.0, 1.0); z = 0.4; pts = [Vector((x, 0, z))]
        n = random.randint(4, 6)
        for i in range(n):
            x += random.uniform(-0.25, 0.25); z -= random.uniform(0.25, 0.4); pts.append(Vector((x, -0.05 * i, z)))
        buis("w%d" % k, pts, random.uniform(0.06, 0.09), hout if k % 2 == 0 else hout_d)
        # zijworteltjes
        for j in range(2, n, 2):
            p = pts[j]; d = random.choice([-1, 1])
            buis("z%d%d" % (k, j), [p, p + Vector((d * 0.25, -0.05, -0.15)), p + Vector((d * 0.45, -0.08, -0.35))], 0.03, hout_d)

if __name__ == "__main__":
    uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    maak(int(sys.argv[5])); g.render(uit, W, H, S, doorzichtig=True)
