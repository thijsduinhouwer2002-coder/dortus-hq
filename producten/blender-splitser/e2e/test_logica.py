"""Test of the pure logic (plan, cross-section, pins) without Blender: python3 -I e2e/test_logica.py
Loads the numpy modules of split_joints without its __init__ (which needs bpy). Exit 1 on any error."""
import math
import os
import sys
import types
import importlib

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
pak = types.ModuleType("split_joints")
pak.__path__ = [os.path.join(HIER, "..", "split_joints")]
sys.modules["split_joints"] = pak
printers = importlib.import_module("split_joints.printers")
plan = importlib.import_module("split_joints.plan")
doorsnede = importlib.import_module("split_joints.doorsnede")
verbinders = importlib.import_module("split_joints.verbinders")

fouten = []


def stap(naam, ok, extra=""):
    print(f"[sj-logica] {'OK ' if ok else 'FOUT'} {naam} {extra}", flush=True)
    if not ok:
        fouten.append(naam)


def doos(mn, mx):
    x0, y0, z0 = mn
    x1, y1, z1 = mx
    v = np.array([(x, y, z) for x in (x0, x1) for y in (y0, y1) for z in (z0, z1)], dtype=float)
    q = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
    f = [(a, b, c) for a, b, c, d in q] + [(a, c, d) for a, b, c, d in q]
    return v, np.array(f)


def ring(r_buiten, r_binnen, hoogte, n=96):
    """Tube (closed): outer wall, inner wall, top and bottom rings."""
    hoek = np.linspace(0, 2 * math.pi, n, endpoint=False)
    v = []
    for r in (r_buiten, r_binnen):
        for z in (0.0, hoogte):
            v += [(r * math.cos(a), r * math.sin(a), z) for a in hoek]
    v = np.array(v)
    ob, ot, ib, it = 0, n, 2 * n, 3 * n
    f = []
    for i in range(n):
        j = (i + 1) % n
        f += [(ob + i, ob + j, ot + j), (ob + i, ot + j, ot + i)]
        f += [(ib + i, it + j, ib + j), (ib + i, it + i, it + j)]
        f += [(ot + i, ot + j, it + j), (ot + i, it + j, it + i)]
        f += [(ob + i, ib + j, ob + j), (ob + i, ib + i, ib + j)]
    return v, np.array(f)


# 1. printers
stap("A1 mini 180 mm", printers.maat("A1MINI") == (180.0, 180.0, 180.0))
stap("eigen maat", printers.maat("CUSTOM", (100, 120, 130)) == (100.0, 120.0, 130.0))
stap("past gedraaid", printers.past((250, 100, 50), (100, 256, 256)))
stap("past niet", not printers.past((300, 10, 10), (256, 256, 256)))
stap("marge", printers.bruikbaar((180, 180, 180), 3) == (174.0, 174.0, 177.0))

# 2. plan: a 500 x 150 x 120 box on a 180 bed: 3 pieces along X
v, f = doos((0, 0, 0), (500, 150, 120))
dicht = np.concatenate([v, np.random.default_rng(1).uniform((0, 0, 0), (500, 150, 120), (2000, 3))])
p = plan.maak(dicht, (174, 174, 177))
stap("plan doos 3 stukken", p is not None and p["stukken"] == 3, str(p and (p["n"], p["stukken"])))
stap("plan doos snedes langs X", p is not None and all(a == 0 for a, _ in p["snedes"]), str(p and p["snedes"]))
stap("plan elke cel past", p is not None and printers.past(p["cel"], (174, 174, 177)), str(p and p["cel"]))
# a box that fits needs no cut
p = plan.maak(dicht * 0.3, (174, 174, 177))
stap("plan klein: 1 stuk", p is not None and p["stukken"] == 1 and not p["snedes"])
# L-shape: empty cells do not count
l_pts = np.concatenate([np.random.default_rng(2).uniform((0, 0, 0), (340, 60, 60), (3000, 3)),
                        np.random.default_rng(3).uniform((0, 0, 0), (60, 340, 60), (3000, 3))])
p = plan.maak(l_pts, (174, 174, 177))
stap("plan L-vorm 3 stukken (lege cel telt niet)", p is not None and p["stukken"] == 3, str(p and (p["n"], p["stukken"])))

# 3. cross-section of a box at x = 100: a 150 x 120 rectangle
segs = doorsnede.snijlijnen(v, f, 0, 100.0)
stap("doorsnede doos heeft lijnen", len(segs) >= 4, str(len(segs)))
us, vs, binnen = doorsnede.raster(segs, (-10, -10, 160, 130), 1.0)
opp = binnen.sum() * (us[1] - us[0]) * (vs[1] - vs[0])
stap("oppervlak doos 150 x 120", abs(opp - 18000) < 400, f"{opp:.0f}")
kl = doorsnede.klaring(us, vs, binnen)
stap("klaring midden ~60 mm", 58 <= kl.max() <= 61, f"{kl.max():.2f}")
lab, n = doorsnede.eilanden(binnen)
stap("een eiland", n == 1)

# 4. tube cut through the middle (plane x = 0): two islands of 8 x 100 mm
v2, f2 = ring(50, 42, 100)
segs = doorsnede.snijlijnen(v2, f2, 0, 0.0137)
us, vs, binnen = doorsnede.raster(segs, (-60, -10, 60, 110), 0.5)
lab, n = doorsnede.eilanden(binnen)
stap("buis: twee eilanden", n == 2, str(n))
kl = doorsnede.klaring(us, vs, binnen)
stap("buis: klaring ~4 mm", 3.4 <= kl.max() <= 4.3, f"{kl.max():.2f}")

opties = {"pen_d": 5.0, "speling": 0.2, "wand": 1.2, "auto": True, "min_d": 3.0}
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, opties, lambda u, v_, r: True, "1-2")
stap("buis: per eiland een uitslag", len(res) == 2)
for r in res:
    pen = r["pennen"]
    ok = bool(pen) and pen[0][2] <= 5.0
    stap(f"buis eiland {r['eiland']}: pen kleiner gekozen", ok and pen[0][2] < 5.0, str(pen))
    for (u, w, d) in pen:
        rr = abs(u)  # plane x = 0: u is y, the wall runs from |y| 42 to 50
        stap("buis pen binnen de wand met marge", 42 + d / 2 + 0.2 + 1.2 - 0.6 <= rr <= 50 - d / 2 - 0.2 - 1.2 + 0.6,
             f"r={rr:.2f} d={d}")

# 5. thin tube: no pin, a clear message
v3, f3 = ring(50, 47, 100)
segs = doorsnede.snijlijnen(v3, f3, 0, 0.0137)
us, vs, binnen = doorsnede.raster(segs, (-60, -10, 60, 110), 0.5)
lab, n = doorsnede.eilanden(binnen)
kl = doorsnede.klaring(us, vs, binnen)
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, opties, lambda u, v_, r: True, "1-2")
stap("dunne buis: geen pen en een melding", all(not r["pennen"] and r["melding"] for r in res), res[0]["melding"])

# 6. big face: several pins, spread, label away from the holes
segs = doorsnede.snijlijnen(v, f, 0, 100.0)
us, vs, binnen = doorsnede.raster(segs, (-10, -10, 160, 130), 1.0)
kl = doorsnede.klaring(us, vs, binnen)
lab, n = doorsnede.eilanden(binnen)
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, opties, lambda u, v_, r: True, "2-3")[0]
pen = res["pennen"]
stap("groot vlak: 2 tot 4 pennen van 5 mm", 2 <= len(pen) <= 4 and all(d == 5.0 for _, _, d in pen), str(pen))
afst = min(math.hypot(a[0] - b[0], a[1] - b[1]) for i, a in enumerate(pen) for b in pen[i + 1:])
stap("pennen ver uit elkaar", afst >= 2 * (2.7 + 1.2), f"{afst:.1f}")
rand = min(min(u, 150 - u, w, 120 - w) for u, w, _ in pen)
stap("pennen niet te dicht bij de rand", rand >= 2.7 + 1.2 + 3.0 - 1.0, f"{rand:.1f}")
lb = res["label"]
stap("label gekozen", lb is not None, str(lb))
if lb:
    vrij = min(math.hypot(lb[0] - u, lb[1] - w) for u, w, _ in pen)
    stap("label niet op een gat", vrij >= 2.7 + lb[2] / 2, f"{vrij:.1f}")

# 7. 3D check that refuses everything: no pins, message
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, opties, lambda u, v_, r: False, "2-3")[0]
stap("3D-toets weigert: geen pen, wel melding", not res["pennen"] and res["melding"])

print(f"[sj-logica] KLAAR {len(fouten)} FOUT {fouten}")
sys.exit(1 if fouten else 0)
