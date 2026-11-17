"""Schets Daan 17 nov: edelman tussen ridder, dief en held, om toets 1 en 2 uit ontwerp.md te proberen.

Geen eindmodel: lijf van de gewone held, jas herkleurd naar wijnrood met gouden bies, jabot, stok,
edelhoed uit proef.py. Draaien: <venv-met-bpy>/bin/python schets_edelman.py uit.png 1600 500 32
"""
import sys, os, math
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
import bpy
import gedeeld as g
import held
import hoeden as hd
import proef

R = math.radians


def edelman(plek):
    voor = set(bpy.data.objects)
    o = held.bouw("held", "rust", plek=plek, draai=30, kleur=0)
    nieuw = [x for x in bpy.data.objects if x not in voor]
    licht = g.mat("edel_jas", "a83a5a", rough=0.6, spec=0.35)   # fluweel
    donker = g.mat("edel_jas_d", "7a2444", rough=0.65, spec=0.3)
    for x in nieuw:
        if x.type == "MESH":
            for i, m in enumerate(x.data.materials):
                if m and m.name.startswith("kleed_d"):
                    x.data.materials[i] = donker
                elif m and m.name.startswith("kleed"):
                    x.data.materials[i] = licht
                elif m and (m.name.startswith("lantaarn") or m.name.startswith("vlam") or m.name.startswith("ijzer")
                            or m.name.startswith("leer")):
                    x.hide_render = True   # geen lantaarn en tas: hij draagt niets zelf
        if x.type == "LIGHT":
            x.hide_render = True
    wit = g.mat("jabot", "f6efe2", rough=0.8)
    goud = g.mat("edel_knoop", "goud", rough=0.25, metaal=0.9)
    px, py, pz = plek
    for i, z in enumerate((0.86, 0.77, 0.69)):   # jabot: drie bolletjes onder de kin
        hd._bol(o, (0.0, -0.3 + 0.01 * i, z), (0.11 - 0.015 * i, 0.06, 0.06), wit, segs=16)
    for z in (0.58, 0.48, 0.38):
        hd._bol(o, (0.02, -0.36, z), (0.035, 0.02, 0.035), goud, segs=10)
    # gouden bies: in de eerste schets een losse ring, zweefde als een hoepel om de benen; hoort in het echte model op de jasrand
    # stok rechts naast het lijf, gouden knop
    hd._kegel(o, (0.44, -0.12, 0.42), 0.025, 0.025, 0.84, g.mat("stok", "2a1a20", rough=0.4))
    hd._bol(o, (0.44, -0.12, 0.86), (0.06, 0.06, 0.06), goud, segs=16)
    proef.edelhoed((px, py, pz + 1.6), kantel=0)
    return o


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    g.leeg()
    held.bouw("ridder", "rust", plek=(-2.4, 0, 0), draai=30)
    held.bouw("dief", "rust", plek=(-0.8, 0, 0), draai=30)
    hd.bouw(5, (-0.8, 0, 1.6))
    edelman((0.8, 0, 0))
    held.bouw("held", "rust", plek=(2.4, 0, 0), draai=30, kleur=0)
    hd.bouw(7, (2.4, 0, 1.6))
    g.camera(hoogte_midden=1.1, schaal=6.4)
    g.licht()
    g.render(uit, W, H, S, doorzichtig=True)
    print("klaar", uit)
