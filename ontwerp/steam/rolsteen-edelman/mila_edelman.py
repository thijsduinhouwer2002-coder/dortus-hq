"""Edelman als echt model (Mila 17 nov): held.bouw("edelman") uit held_soorten.py, edelhoed nr 10 op 0,9.
Strook: ridder, dief met koksmuts, edelman, held met hoge hoed nr 7 (zelfde opstelling als Daans schets).
<venv>/bin/python mila_edelman.py uit.png 1600 500 32 [stand]"""
import sys, os, math
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
import gedeeld as g
import held
import hoeden as hd

if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    stand = sys.argv[5] if len(sys.argv) > 5 else "rust"
    g.leeg()
    held.bouw("ridder", stand, plek=(-2.4, 0, 0), draai=30)
    held.bouw("dief", stand, plek=(-0.8, 0, 0), draai=30)
    hd.bouw(5, (-0.8, 0, 1.6))
    held.bouw("edelman", stand, plek=(0.8, 0, 0), draai=30)
    hd.bouw(10, (0.8, 0, 1.6), schaal=0.9, kantel=0, draai=30)
    held.bouw("held", stand, plek=(2.4, 0, 0), draai=30, kleur=0)
    hd.bouw(7, (2.4, 0, 1.6), draai=30)
    g.camera(hoogte_midden=1.1, schaal=6.4)
    g.licht()
    g.render(uit, W, H, S, doorzichtig=True)
    print("klaar", uit)
