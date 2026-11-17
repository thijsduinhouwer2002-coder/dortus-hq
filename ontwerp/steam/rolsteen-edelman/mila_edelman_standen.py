"""Edelman standen (Mila 17 nov): rust, wacht, wacht_tik, na_u, na_u2, tenen, stap1 naast elkaar, met edelhoed nr 10.
Bij na_u2 schuift de hoed mee met de buiging (ouder["hoed_voor"]).
<venv>/bin/python mila_edelman_standen.py uit.png 2100 420 32 [kok]   (kok: dief met koksmuts ernaast, toets witte hoeden)"""
import sys, os, math
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
import gedeeld as g
import held
import hoeden as hd

STANDEN = ["rust", "wacht", "wacht_tik", "na_u", "na_u2", "tenen", "stap1"]

if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    kok = len(sys.argv) > 5 and sys.argv[5] == "kok"
    g.leeg()
    rij = (["kok"] if kok else []) + STANDEN
    n = len(rij)
    for i, st in enumerate(rij):
        x = (i - (n - 1) / 2) * 1.5
        if st == "kok":
            o = held.bouw("dief", "rust", plek=(x, 0, 0), draai=30)
            hd.bouw(5, (x, 0, 1.6), draai=30)
            continue
        o = held.bouw("edelman", st, plek=(x, 0, 0), draai=30)
        voor = o.get("hoed_voor", 0.0)
        a = math.radians(30)
        # hoed volgt het hoofd: lokaal -y (naar voren) is na de draai van 30 graden (x, y) = (-sin, -cos) * voor ... rechts in beeld
        dx, dy = -voor * math.sin(a), -voor * math.cos(a)
        hz = 1.6 - (0.04 if voor else 0.0)
        hd.bouw(10, (x + dx, dy, hz), schaal=0.9, kantel=0, draai=30)
    g.camera(hoogte_midden=1.15, schaal=1.5 * n + 0.6)
    g.licht()
    g.render(uit, W, H, S, doorzichtig=True)
    print("klaar", uit)
