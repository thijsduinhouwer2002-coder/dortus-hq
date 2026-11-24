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
passing = importlib.import_module("split_joints.passing")
kleuren = importlib.import_module("split_joints.kleuren")

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

# 2. plan on bare meshes (only their own vertices: keuring A8, a box of 8 vertices gave 2 pieces)
BED = (174, 174, 177)
v, f = doos((0, 0, 0), (500, 150, 120))
p = plan.maak(v, BED, f)
stap("plan kale doos 500 x 150 x 120: 3 stukken", p is not None and p.get("stukken") == 3, str(p and (p.get("n"), p.get("stukken"))))
stap("plan doos snedes langs X", p is not None and all(a == 0 for a, _ in p.get("snedes", [(1, 0)])), str(p and p.get("snedes")))
stap("plan elke cel past", p is not None and "cel" in p and printers.past(p["cel"], BED), str(p and p.get("cel")))
vp, fp = doos((0, 0, 0), (600, 600, 30))
p = plan.maak(vp, BED, fp)
stap("plan kale plaat 600 x 600 x 30: 16 stukken", p is not None and p.get("stukken") == 16, str(p and (p.get("n"), p.get("stukken"))))
vk, fk = doos((0, 0, 0), (500, 500, 500))
p = plan.maak(vk, BED, fk)
stap("plan volle kubus 500: 27 stukken (ook de cel middenin zonder huid)", p is not None and p.get("stukken") == 27,
     str(p and (p.get("n"), p.get("stukken"))))
p = plan.maak(v * 0.3, BED, f)
stap("plan klein: 1 stuk", p is not None and p.get("stukken") == 1 and not p.get("snedes"))
# L-shape of two boxes: the empty corner cell does not count
va, fa = doos((0, 0, 0), (340, 60, 60))
vb, fb = doos((0, 60, 0), (60, 340, 60))
p = plan.maak(np.concatenate([va, vb]), BED, np.concatenate([fa, fb + len(va)]))
stap("plan L-vorm 3 stukken (lege cel telt niet)", p is not None and p.get("stukken") == 3, str(p and (p.get("n"), p.get("stukken"))))
# a model in mm read as meters (x1000): a clear refusal, fast, never thousands of cuts
import time  # noqa: E402
t0 = time.time()
p = plan.maak(v * 1000.0, BED, f)
duur = time.time() - t0
stap("plan 1000 keer te groot: weigert met te_veel", p is not None and p.get("fout") == "te_veel" and p["minimaal"] > plan.MAX_CELLEN,
     str(p and {k: p.get(k) for k in ("fout", "minimaal")}))
stap("plan 1000 keer te groot: binnen 2 s", duur < 2.0, f"{duur:.2f} s")
stap("aantal cellen zonder ze te maken", plan.aantal_cellen((0, 0, 0), (10, 10, 10), [(0, 3.0), (0, 6.0), (2, 5.0), (1, 20.0)]) == 6)

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

# 5b. tube with a 6 mm wall: the number follows the wall (no room for straight text)
v4, f4 = ring(50, 44, 100)
segs = doorsnede.snijlijnen(v4, f4, 0, 0.0137)
us, vs, binnen = doorsnede.raster(segs, (-60, -10, 60, 110), 0.5)
lab, n = doorsnede.eilanden(binnen)
kl = doorsnede.klaring(us, vs, binnen)
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, opties, lambda u, v_, r: True, "12-13")
for r in res:
    lb = r["label"]
    stap(f"buis 6 mm eiland {r['eiland']}: nummer langs de wand", lb is not None and lb[3] is not None and lb[2] >= 3.0,
         str(lb))
    if lb and lb[3]:
        stap("buis 6 mm: tekst loopt langs de wand (v-richting)", abs(lb[3][1]) > 0.95, str(lb[3]))

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
# wide face refused in 3D: the message must not show a width that looks big enough (Regisseur 24 nov)
stap("3D-toets weigert: melding noemt de echte reden", res["melding"].startswith("no safe spot for a pin")
     and "mm across" not in res["melding"] and res["melding"].endswith("Glue this joint"), res["melding"])
smal = verbinders.melding_geen_pen(np.array([0.5, 1.0]), 3.0, opties)
stap("smal vlak: melding noemt de breedte", smal.startswith("too small for a pin: the face is 2.0 mm across"), smal)

# 8. fit test: clearances, saved values per printer and material, block layout
stap("passing: 0,20 geeft 0,15 tot 0,30", passing.spelingen(0.2) == [0.15, 0.2, 0.25, 0.3], str(passing.spelingen(0.2)))
stap("passing: nooit onder 0", passing.spelingen(0.02) == [0.0, 0.05, 0.1, 0.15], str(passing.spelingen(0.02)))
stap("passing: nooit boven 1,0", passing.spelingen(1.0) == [0.85, 0.9, 0.95, 1.0], str(passing.spelingen(1.0)))
stap("passing: tekst met punt", passing.tekst(0.2) == "0.20" and passing.tekst(0.0) == "0.00")
j = passing.bewaar("", "A1MINI", "PLA", 0.25)
j = passing.bewaar(j, "A1MINI", "PETG", 0.3)
stap("passing: los bewaard per materiaal", passing.opgeslagen(j, "A1MINI", "PLA") == 0.25 and
     passing.opgeslagen(j, "A1MINI", "PETG") == 0.3 and passing.opgeslagen(j, "MK4", "PLA") is None, j)
stap("passing: kapotte tekst geeft niets", passing.lees("{kapot") == {} and passing.lees('[1]') == {} and
     passing.lees('{"a": "x", "b": 5}') == {})
m = passing.maten(5.0, 12.0, 1.2, 0.2, 0.3)
xs = [g["p"][0] for g in m["gaten"]]
tussen = min(b - a for a, b in zip(xs, xs[1:])) - 2 * (2.5 + 0.3)
stap("passing: wand tussen de gaten minstens 2 mm", tussen >= 2.0, f"{tussen:.2f}")
rand = min(xs[0] - m["mn"][0], m["mx"][0] - xs[-1], m["mx"][1]) - (2.5 + 0.3)
stap("passing: wand naar de rand minstens 2 mm", rand >= 2.0, f"{rand:.2f}")
vloer = m["mx"][2] - m["gaten"][0]["diepte"]
stap("passing: gat half de pen plus 0,3 en vloer eronder", abs(m["gaten"][0]["diepte"] - 6.3) < 1e-9 and vloer >= 2.0)
voor = min(nr["p"][1] - nr["h"] / 2 for nr in m["nummers"]) - m["mn"][1]
breed = (4 * 4 - 1) * passing.LETTER_MM / 5.0
gat_nr = min(b["p"][0] - a["p"][0] for a, b in zip(m["nummers"], m["nummers"][1:])) - breed
stap("passing: ruimte tussen twee nummers minstens 4 mm", gat_nr >= 4.0, f"{gat_nr:.2f}")
stap("passing: nummer binnen het blok en niet op het gat", voor >= 1.0 and
     all(g["p"][1] - (nr["p"][1] + nr["h"] / 2) >= g["r_gat"] + 1.0 for g, nr in zip(m["gaten"], m["nummers"])), f"{voor:.2f}")

# 9. color per piece: neighbors never share a color, colors spread, brand colors first
def rooster(n):
    return [(i, j, k) for k in range(n[2]) for j in range(n[1]) for i in range(n[0])]


for n in ((1, 1, 1), (3, 1, 1), (4, 4, 1), (3, 3, 3), (5, 4, 6)):
    cel = rooster(n)
    k = kleuren.verdeel(cel)
    botsing = [(a, b) for a in range(len(cel)) for b in range(a) if kleuren.buren(cel[a], cel[b]) and k[a] == k[b]]
    stap(f"kleur {n}: buren nooit gelijk", not botsing, f"{botsing[:3]}")
    stap(f"kleur {n}: zoveel kleuren als kan", len(set(k)) == min(len(cel), len(kleuren.PALET)), f"{len(set(k))}")
# gaps: empty cells drop out, the order stays the piece order
cel = [(0, 0, 0), (2, 0, 0), (1, 1, 0), (1, 0, 0)]
k = kleuren.verdeel(cel)
stap("kleur met lege cellen: buren verschillen", k[3] not in (k[0], k[1]) and k[2] != k[3], str(k))
stap("kleur: eerste drie stukken in de merkkleuren", kleuren.verdeel(rooster((3, 1, 1))) == [0, 1, 2])
stap("kleur: buren alleen via een vlak", kleuren.buren((0, 0, 0), (1, 0, 0)) and not kleuren.buren((0, 0, 0), (1, 1, 0))
     and not kleuren.buren((0, 0, 0), (0, 0, 0)))
lin = kleuren.lineair("FFFFFF")
stap("kleur: sRGB naar lineair", lin == (1.0, 1.0, 1.0, 1.0) and abs(kleuren.lineair("808080")[0] - 0.2159) < 1e-3)
afstand = min(sum((a - b) ** 2 for a, b in zip(kleuren.lineair(p)[:3], kleuren.lineair(kleuren.GOUD)[:3])) ** 0.5
              for p in kleuren.PALET)
stap("kleur: geen stuk lijkt op het goud van de pennen", afstand > 0.25, f"{afstand:.2f}")


def lab(hex_):
    r, g, b = kleuren.lineair(hex_)[:3]
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    t = [v ** (1 / 3) if v > 0.008856 else 7.787 * v + 16 / 116 for v in (x, y, z)]
    return (116 * t[1] - 16, 500 * (t[0] - t[1]), 200 * (t[1] - t[2]))


alle = list(kleuren.PALET) + [kleuren.GOUD]
dlab = min(math.dist(lab(a), lab(b)) for i, a in enumerate(alle) for b in alle[i + 1:])
stap("kleur: elk paar kleuren (ook het goud) minstens 25 uit elkaar in Lab", dlab >= 25.0, f"{dlab:.1f}")

print(f"[sj-logica] KLAAR {len(fouten)} FOUT {fouten}")
sys.exit(1 if fouten else 0)
