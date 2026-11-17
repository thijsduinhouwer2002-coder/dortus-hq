"""Proef Daan 17 nov: de edelhoed naast koksmuts (nr 5) en hoge hoed (nr 7), en de rolsteen klaar en niet klaar.

Geen eindmodel: een schets in 3D om maat en kleur te toetsen voor Mila het echte model maakt
(zie ontwerp.md hiernaast). Draaien:
    <venv-met-bpy>/bin/python proef.py uit.png 1600 400 48
"""
import sys, os, math
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
import bpy
import gedeeld as g
import hoeden as hd

R = math.radians


def edelhoed(plek, kantel=0):
    ouder = bpy.data.objects.new("hoed_edel", None)
    bpy.context.scene.collection.objects.link(ouder)
    ivoor = g.mat("edel_ivoor", "f3ead6", rough=0.3, spec=0.6)
    goud = g.mat("edel_goud", "goud", rough=0.22, spec=0.9, metaal=0.9)
    # brede rand (proef 1 had opgekrulde flapjes opzij: GEZIEN, lazen als handvatten, weg)
    hd._kegel(ouder, (0, 0, 0.025), 0.55, 0.55, 0.05, ivoor)
    # koker 0,86 hoog en getailleerd: onder 0,31, midden 0,29, boven 0,34
    hd._kegel(ouder, (0, 0, 0.27), 0.31, 0.29, 0.43, ivoor)
    hd._kegel(ouder, (0, 0, 0.69), 0.29, 0.34, 0.43, ivoor)
    # brede gouden band (0,18) met een wijnrood rozetje vooraan
    hd._kegel(ouder, (0, 0, 0.15), 0.322, 0.317, 0.18, goud)
    roos = g.mat("edel_roos", "8e2a4a", rough=0.6)
    hd._bol(ouder, (0.0, -0.33, 0.15), (0.09, 0.05, 0.09), roos, segs=20)
    hd._bol(ouder, (0.0, -0.37, 0.15), (0.035, 0.02, 0.035), goud, segs=12)
    ouder.location = plek
    ouder.rotation_euler = (0, R(kantel), 0)
    return ouder


def rolsteen(plek, klaar=True):
    ouder = bpy.data.objects.new("rolsteen", None)
    bpy.context.scene.collection.objects.link(ouder)
    steen = g.mat("steen", "8e8a86", rough=0.95, spec=0.1)   # proef 1 a8a39c: leek onder de fakkel een ei
    groef = g.mat("groef", "6e6860", rough=0.9, spec=0.1)
    rand = g.mat("groefrand", "d8d0c0", rough=0.8)
    mos = g.mat("mos", "6f8f4a", rough=0.95)
    r = 0.5
    hd._bol(ouder, (0, 0, r * 0.92), (r, r, r * 0.92), steen, segs=40)
    # ingekerfde band rondom, schuin zodat je hem op elke stand ziet draaien
    for i, (rr, d, m) in enumerate([(r - 0.012, 0.03, rand), (r - 0.022, 0.035, groef)]):   # proef 2 stak de band uit als een touw; nu ligt hij erin
        bpy.ops.mesh.primitive_torus_add(major_radius=rr, minor_radius=d, location=(0, 0, r * 0.92),
                                         rotation=(0, R(90), R(40)))   # proef 1 stond de band naar de camera: een ring om de rand
        o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(m)
        o.scale = (1, 1, 0.92 if i else 0.95); o.parent = ouder
    hd._bol(ouder, (0.18, -0.12, r * 1.72), (0.2, 0.17, 0.06), mos, segs=20)     # mos bovenop
    # schilfers: proef 2 had bultjes (lazen als wratten); nu één platte donkere plek waar een stuk af is
    hd._bol(ouder, (-0.3, -0.36, r * 1.3), (0.12, 0.012, 0.09), groef, segs=16, rot=(R(-35), R(30), 0))
    if klaar:
        hout = g.mat("wig", "8a5a32", rough=0.7)
        # houten wig voor de steen, touwtje erlangs
        hd._kegel(ouder, (0.45, -0.05, 0.07), 0.16, 0.16, 0.14, hout, rot=(R(90), 0, 0), verts=3)
        touw = g.mat("touw", "c8a870", rough=0.9)
        hd._kegel(ouder, (0.48, -0.2, 0.2), 0.012, 0.012, 0.3, touw, rot=(0, R(20), 0), verts=8)
        ouder.location = plek
    else:
        ouder.location = plek
        ouder.rotation_euler = (0, R(70), 0)   # mos opzij: niet klaar
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    g.leeg()
    hd.bouw(5, (-3.0, 0, 0.0))
    hd.bouw(7, (-1.7, 0, 0.0))
    edelhoed((-0.4, 0, 0.0), kantel=5)
    rolsteen((1.4, 0, 0.0), klaar=True)
    rolsteen((3.0, 0, 0.0), klaar=False)
    g.camera(hoogte_midden=0.45, schaal=7.6)
    g.licht()
    g.render(uit, W, H, S, doorzichtig=True)
    print("klaar", uit)
