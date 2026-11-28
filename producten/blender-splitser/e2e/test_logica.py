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
plat = importlib.import_module("split_joints.plat")
lijn = importlib.import_module("split_joints.lijn")

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
# #385: the default cube (2 m) on an A1 names its size and the way out, in plain numbers
m, regels = plan.te_veel_tekst("Cube", (2000.0, 2000.0, 2000.0), (246.0, 246.0, 251.0), 729)
stap("te veel: melding noemt maat, keer en uitweg (#385)", m.startswith("Cube is 2,000 x 2,000 x 2,000 mm, about 8 times")
     and "Scale it down (S)" in m and "bigger printer" in m and "e+" not in m, m)
stap("te veel: vier korte paneelregels (#385)", len(regels) == 4 and regels[0] == "Too big: 2,000 x 2,000 x 2,000 mm"
     and all(len(r) <= 34 for r in regels), str(regels))
# #386: sizes in plain numbers, never 3.985e+05
stap("maat in gewone getallen (#386)", plan.maat_tekst(398500.0) == "398,500 mm (about 400 m)"
     and plan.maat_tekst(120.0) == "120 mm" and plan.maat_tekst(0.3985) == "0.4 mm"
     and plan.maat_tekst(0.00004) == "0.00004 mm" and "e" not in plan.maat_tekst(4e9),
     f"{plan.maat_tekst(398500.0)} | {plan.maat_tekst(0.00004)} | {plan.maat_tekst(4e9)}")
m = plan.eenheid_tekst("aap_mm", 398500.0, 1.0, 0.001)
stap("eenheid fout: oorzaak en knop zoals in het paneel (#386)", m.startswith("aap_mm is 398,500 mm (about 400 m)")
     and "1,000 times too big: a mm model in a meter scene" in m and "press Convert to mm" in m, m)
m = plan.eenheid_tekst("klein", 0.45, 0.001, 1.0)
stap("eenheid fout: te klein (#386)", "1,000 times too small: a meter model in a mm scene" in m, m)
stap("eenheid fout: geen eenheid past (#386)", "Scale it yourself (S)" in plan.eenheid_tekst("x", 4e9, 1.0, None))
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

# 7b. magnets (issue #117): fixed size, clearance on the diameter, 1.2 mm wall at least, own message
mo = verbinders.magneet_opties("6x2", 0.2, 0.8)
stap("magneet 6x2: maat, halve speling per kant, diepte 2.3, wand minstens 1.2",
     mo["pen_d"] == 6.0 and abs(mo["speling"] - 0.1) < 1e-9 and abs(mo["diepte"] - 2.3) < 1e-9 and mo["wand"] == 1.2
     and not mo["auto"], str(mo))
stap("magneet: alle maten uit de lijst", [k for k, _d, _t in verbinders.MAGNETEN] == ["5x2", "6x2", "6x3", "8x3", "10x3"])
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, mo, lambda u, v_, r: True, "2-3")[0]
stap("magneet groot vlak: 2 tot 4 gaten van 6 mm", 2 <= len(res["pennen"]) <= 4
     and all(d == 6.0 for _, _, d in res["pennen"]), str(res["pennen"]))
mo10 = verbinders.magneet_opties("10x3", 0.2, 1.2)
smal = verbinders.melding_geen_pen(np.array([5.0, 6.0]), 10.0, mo10)
stap("magneet smal vlak: melding met breedte en wand", smal.startswith("too small for a magnet: the face is 12.0 mm across")
     and "12.6 mm with 1.2 mm wall" in smal, smal)
res = verbinders.plan_vlak(us, vs, binnen, kl, lab, n, mo10, lambda u, v_, r: False, "2-3")[0]
stap("magneet 3D-toets weigert: geen gat, melding over de wand", not res["pennen"]
     and res["melding"].startswith("no safe spot for a magnet"), res["melding"])

# 8. fit test: clearances, saved values per printer and material, block layout
stap("passing: 0,20 geeft 0,15 tot 0,30", passing.spelingen(0.2) == [0.15, 0.2, 0.25, 0.3], str(passing.spelingen(0.2)))
stap("passing: nooit onder 0", passing.spelingen(0.02) == [0.0, 0.05, 0.1, 0.15], str(passing.spelingen(0.02)))
stap("passing: nooit boven 1,0", passing.spelingen(1.0) == [0.85, 0.9, 0.95, 1.0], str(passing.spelingen(1.0)))
stap("passing: startspeling per materiaal (#227)", [passing.startspeling(k) for k in ("PLA", "PETG", "ABS", "TPU", "RESIN", "OTHER")]
     == [0.2, 0.25, 0.25, 0.3, 0.1, 0.2] and passing.startspeling("ONBEKEND") == 0.2)
stap("passing: elk materiaal heeft een startspeling", all(k in passing.STARTSPELING for k, _n, _o in passing.MATERIALEN))
stap("passing: hars test 0,05 tot 0,20 (SnapSplit 0,10 en Hubs 0,15 erin)", passing.spelingen(passing.startspeling("RESIN"))
     == [0.05, 0.1, 0.15, 0.2], str(passing.spelingen(0.1)))
stap("passing: TPU test 0,25 tot 0,40 (SnapSplit 0,35 erin)", passing.spelingen(passing.startspeling("TPU"))
     == [0.25, 0.3, 0.35, 0.4], str(passing.spelingen(0.3)))
stap("passing: PETG test 0,20 tot 0,35 (SnapSplit 0,30 erin)", passing.spelingen(passing.startspeling("PETG"))
     == [0.2, 0.25, 0.3, 0.35], str(passing.spelingen(0.25)))
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

# 10. Lay parts flat (1.0.0): the largest flat plane goes down, only if it is a real bottom and fits the bed
def doos_vlakken(x, y, z, gat=False):
    """Faces of a box 0..x, 0..y, 0..z as (normals, points, areas); gat: the +x face has a hole of 25%."""
    nrm, pts, opp = [], [], []
    for as_, maat_ in ((0, x), (1, y), (2, z)):
        rest = [m for i, m in enumerate((x, y, z)) if i != as_]
        for kant in (0.0, 1.0):
            n = [0.0, 0.0, 0.0]
            n[as_] = 1.0 if kant else -1.0
            p = [x / 2, y / 2, z / 2]
            p[as_] = maat_ * kant
            a = rest[0] * rest[1] * (0.75 if gat and as_ == 0 and kant else 1.0)
            nrm.append(n), pts.append(p), opp.append(a)
    return np.array(nrm), np.array(pts), np.array(opp)


def doos_hoeken(x, y, z):
    return np.array([(a, b, c) for a in (0, x) for b in (0, y) for c in (0, z)], dtype=float)


nrm, pts, opp = doos_vlakken(40.0, 100.0, 60.0)
n, a, d = plat.grootste_vlak(nrm, pts, opp)
stap("plat: grootste vlak van een doos 40 x 100 x 60 is 100 x 60", abs(a - 6000.0) < 1e-6 and abs(abs(n[0]) - 1) < 1e-9,
     f"{a:.0f} {n}")
# a cut face with pin holes, split in many small triangles, still counts as one plane
rng = np.random.default_rng(1)
stukjes = rng.uniform(10.0, 50.0, 400)  # together far more than the 6000 of the box
nrm2 = np.vstack([nrm, np.tile([1.0, 0.0, 0.0], (400, 1)) + rng.normal(0, 1e-5, (400, 3))])
pts2 = np.vstack([pts, np.column_stack([np.full(400, 200.0), rng.uniform(0, 50, 400), rng.uniform(0, 50, 400)])])
opp2 = np.concatenate([opp, stukjes])
n2, a2, d2 = plat.grootste_vlak(nrm2, pts2, opp2)
stap("plat: veel kleine driehoeken in één vlak tellen samen", abs(a2 - stukjes.sum()) < 1e-6 and abs(d2 - 200.0) < 0.02,
     f"{a2:.1f} van {stukjes.sum():.1f}")
for nv in ([0, 0, 1], [0, 0, -1], [1, 0, 0], [0.6, 0, 0.8], [0.3, -0.4, -0.866]):
    nv = np.array(nv, dtype=float) / np.linalg.norm(nv)
    r = plat.draai_naar_beneden(nv)
    stap(f"plat: draaiing zet {np.round(nv, 2).tolist()} naar beneden", np.allclose(r @ nv, [0, 0, -1], atol=1e-9)
         and np.allclose(r @ r.T, np.eye(3), atol=1e-9) and abs(np.linalg.det(r) - 1) < 1e-9)
# box on an A1 mini (176 x 176 x 178): the 100 x 60 face down, height 40
r, a, rang, _snij = plat.kies_stand(nrm, pts, opp, doos_hoeken(40.0, 100.0, 60.0), (176.0, 176.0, 178.0), alleen_snijvlak=False)
w = doos_hoeken(40.0, 100.0, 60.0) @ r.T
stap("plat: doos ligt op zijn grootste kant", r is not None and rang == 0 and abs(np.ptp(w[:, 2]) - 40.0) < 1e-6,
     f"hoogte {np.ptp(w[:, 2]):.1f}")
# long thin piece on a low bed: the big face down would be fine, but a bed of 120 high and 90 wide
# does not take the 170 x 100 face lying down; the next plane that fits wins
nrm3, pts3, opp3 = doos_vlakken(170.0, 100.0, 30.0)
r3, a3, rang3, _snij = plat.kies_stand(nrm3, pts3, opp3, doos_hoeken(170.0, 100.0, 30.0), (120.0, 120.0, 180.0), alleen_snijvlak=False)
w3 = doos_hoeken(170.0, 100.0, 30.0) @ r3.T if r3 is not None else None
stap("plat: past het grootste vlak niet op het bed, dan het volgende dat past", r3 is not None and rang3 > 0
     and np.ptp(w3[:, 0]) <= 120.0 + 1e-6 and np.ptp(w3[:, 1]) <= 120.0 + 1e-6 and np.ptp(w3[:, 2]) <= 180.0 + 1e-6,
     f"rang {rang3}")
# turned around z to fit: a 140 x 10 strip on a 110 x 110 bed fits only diagonally (at 45 degrees 106 x 106)
nrm4, pts4, opp4 = doos_vlakken(140.0, 10.0, 5.0)
r4, a4, rang4, _snij = plat.kies_stand(nrm4, pts4, opp4, doos_hoeken(140.0, 10.0, 5.0), (110.0, 110.0, 50.0), alleen_snijvlak=False)
w4 = doos_hoeken(140.0, 10.0, 5.0) @ r4.T if r4 is not None else None
stap("plat: draait om z als het recht niet past", r4 is not None and rang4 == 0 and np.ptp(w4[:, 0]) <= 110.0 + 1e-6
     and np.ptp(w4[:, 1]) <= 110.0 + 1e-6)
# L-shape: the largest plane is a step in the middle, the rest sticks out past it: not a bottom
nrm5 = np.array([[0, 0, 1.0], [0, 0, -1.0], [0, 0, 1.0]])
pts5 = np.array([[50, 50, 10.0], [10, 50, 0.0], [10, 50, 40.0]])
opp5 = np.array([8000.0, 2000.0, 2000.0])
hoeken5 = np.array([[0, 0, 0], [100, 0, 0], [0, 100, 0], [100, 100, 0], [0, 0, 40], [20, 100, 40], [100, 100, 10.0]])
r5, a5, rang5, _snij = plat.kies_stand(nrm5, pts5, opp5, hoeken5, (176.0, 176.0, 178.0), alleen_snijvlak=False)
stap("plat: een vlak waar iets van het stuk voorbij steekt ligt niet onder", r5 is not None and abs(a5 - 2000.0) < 1e-6
     and np.allclose(r5 @ [0, 0, -1.0], [0, 0, -1.0]), f"vlak {a5:.0f}")
# cut faces first: a faceted side (8000 mm2) is larger than the cut face (2000 mm2) with a pin hole in it
nrm6 = np.array([[1.0, 0, 0], [0, 0, -1.0], [0, 0, 1.0]])
pts6 = np.array([[100, 50, 20.0], [50, 50, 0.0], [50, 50, 40.0]])
opp6 = np.array([8000.0, 2000.0, 2000.0])
hoeken6 = doos_hoeken(100.0, 100.0, 40.0)
r6, a6, _, snij6 = plat.kies_stand(nrm6, pts6, opp6, hoeken6, (176.0, 176.0, 178.0), snij=[((30.0, 40.0, 0.05), (0.0, 0.0, 1.0))])
stap("plat: een snijvlak (met pengat) gaat voor een groter plat vlak van het model", r6 is not None and abs(a6 - 2000.0) < 1e-6
     and snij6 and np.allclose(r6 @ [0, 0, -1.0], [0, 0, -1.0]), f"vlak {a6:.0f}")
r7, a7, _, snij7 = plat.kies_stand(nrm6, pts6, opp6, hoeken6, (176.0, 176.0, 178.0), snij=[((30.0, 40.0, 3.0), (0.0, 0.0, 1.0))])
stap("plat: een pengat buiten het vlak maakt het geen snijvlak: eigen stand (M1 Daan)", r7 is None and not snij7, f"vlak {a7:.0f}")
r7b, a7b, _, snij7b = plat.kies_stand(nrm6, pts6, opp6, hoeken6, (176.0, 176.0, 178.0), snij=[((30.0, 40.0, 3.0), (0.0, 0.0, 1.0))],
                                      alleen_snijvlak=False)
stap("plat: zonder alleen_snijvlak wint dan het grotere vlak", abs(a7b - 8000.0) < 1e-6 and not snij7b, f"vlak {a7b:.0f}")
# M1 Daan: a thin curved shell (vase piece) has flat outer facets but its ring faces hold no pin or number;
# it must keep its own way up, not lie on a facet with the curve hanging over
hoek_ = np.radians(np.arange(0, 91, 15))
nrm8 = np.column_stack([np.cos(hoek_[:-1] + np.radians(7.5)), np.sin(hoek_[:-1] + np.radians(7.5)), np.zeros(6)])
pts8 = 60.0 * nrm8 + [0.0, 0.0, 40.0]
pts8[:, 2] = 40.0
nrm8 = np.vstack([nrm8, [[0, 0, -1.0], [0, 0, 1.0]]])
pts8 = np.vstack([pts8, [[40, 40, 0.0], [40, 40, 80.0]]])
opp8 = np.concatenate([np.full(6, 1250.0), [300.0, 300.0]])
hoeken8 = np.vstack([np.column_stack([r_ * np.cos(hoek_), r_ * np.sin(hoek_), np.full(7, z_)]) for r_ in (58.0, 62.0) for z_ in (0.0, 80.0)])
r8 = plat.kies_stand(nrm8, pts8, opp8, hoeken8, (176.0, 176.0, 178.0))
stap("plat: dunne schaal zonder herkend snijvlak houdt zijn eigen stand (vaas stuk 9 tot 16)", r8[0] is None and r8[2] == -1)
r8b = plat.kies_stand(nrm8, pts8, opp8, hoeken8, (176.0, 176.0, 178.0), snij=[((40.0, 40.0, 80.0), (0.0, 0.0, 1.0))])
stap("plat: dezelfde schaal met een pengat in de bovenring ligt op die ring", r8b[0] is not None and r8b[3]
     and np.allclose(r8b[0] @ [0, 0, 1.0], [0, 0, -1.0], atol=1e-9), f"vlak {r8b[1]:.0f}")
# K1 Daan: a piece scaled 3x after the split gives normals of length 1/3; they still count
n9, a9, _ = plat.grootste_vlak(nrm / 3.0, pts, opp)
stap("plat: korte normalen (geschaald stuk) tellen nog mee", n9 is not None and abs(a9 - 6000.0) < 1e-6, f"{a9:.0f}")
stap("plat: geen enkel plat vlak: stuk houdt zijn eigen stand", plat.kies_stand(np.zeros((0, 3)), np.zeros((0, 3)),
     np.zeros(0), hoeken5, (176.0, 176.0, 178.0))[0] is None)

# 11. Draw cut (issue #208): a line drawn over the arm of a torso, front view (looking along +Y)
torso_v, _ = doos((-20, -20, 0), (20, 20, 40))
arm_v, _ = doos((15, -8, 22), (80, 8, 38))
romp = np.vstack([torso_v, arm_v, [[x, y, z] for x in np.linspace(-20, 80, 21) for y in (-8, 8) for z in (22, 38)]])
for naam, p1, p2 in (("van onder naar boven", (50, -30, 15), (50, -30, 45)), ("van boven naar onder", (50, -30, 45), (50, -30, 15))):
    R, o, a, b = lijn.vlak_uit_lijn(p1, p2, (0, 1, 0), romp, marge=1.0)
    stap(f"tekenen {naam}: pijl naar het armeinde (+X)", np.allclose(R[:, 2], [1, 0, 0], atol=1e-9), f"{np.round(R[:, 2], 3)}")
    stap(f"tekenen {naam}: rechtshandig", abs(np.linalg.det(R) - 1.0) < 1e-9)
    stap(f"tekenen {naam}: vlak door de lijn op x = 50", abs(o[0] - 50.0) < 1e-9 and abs(o[2] - 30.0) < 1e-9, f"{np.round(o, 3)}")
    stap(f"tekenen {naam}: breed als de lijn plus 1 mm, diep als het stuk plus 1 mm", abs(a - 16.0) < 1e-9 and abs(b - 21.0) < 1e-9 and abs(o[1]) < 1e-9, f"a {a} b {b}")
# a line over the whole height of the torso: both sides lie fully inside the rectangle
R, o, a, b = lijn.vlak_uit_lijn((10, -30, 0), (10, -30, 50), (0, 1, 0), romp)
stap("tekenen: lijn over de hele hoogte: beide kanten binnen, de kant die minder ver doorloopt (-X, 30 tegen 70 mm)", R[:, 2][0] < -0.99, f"{np.round(R[:, 2], 3)}")
# slanted view: the plane still holds the view direction and the line
k = np.array([0.3, 1.0, -0.2])
R, o, a, b = lijn.vlak_uit_lijn((50, -30, 15), (50, -30, 45), k, romp)
stap("tekenen: schuine blik ligt in het vlak", abs(R[:, 2] @ (k / np.linalg.norm(k))) < 1e-9 and abs(R[:, 2] @ [0, 0, 1.0]) < 1e-9)
stap("tekenen: te korte lijn of lijn langs de blik geweigerd", lijn.vlak_uit_lijn((0, 0, 0), (0, 5, 0), (0, 1, 0), romp) is None
     and lijn.vlak_uit_lijn((0, 0, 0), (0, 0, 0), (0, 1, 0), romp) is None)
# keuring #212 M1: the part that comes off is lit before Cut piece; K1: Flip side turns it to the other part
R, o, a, b = lijn.vlak_uit_lijn((50, -30, 15), (50, -30, 45), (0, 1, 0), romp, marge=1.0)
proef = np.array([[60, 0, 30], [70, 0, 30], [65, 0, 35],  # arm end: comes off
                  [0, 0, 30], [10, 0, 30], [5, 0, 35],  # torso: stays
                  [60, 0, 60], [70, 0, 60], [65, 0, 65]])  # past the arm, outside the rectangle: stays
tri3 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
m = lijn.deel_eraf(proef, tri3, R, o, a, b)
stap("tekenen: alleen het armeinde licht op", m.tolist() == [True, False, False], f"{m.tolist()}")
R2 = lijn.omdraaien(R)
m2 = lijn.deel_eraf(proef, tri3, R2, o, a, b)
stap("tekenen: Flip side zet de pijl om en blijft rechtshandig", np.allclose(R2[:, 2], -R[:, 2]) and abs(np.linalg.det(R2) - 1.0) < 1e-9)
stap("tekenen: na Flip side licht de romp op, niet het armeinde", m2.tolist() == [False, True, False], f"{m2.tolist()}")
stap("tekenen: twee keer Flip side is terug bij af", np.allclose(lijn.omdraaien(R2), R))
stap("tekenen: leeg stuk geeft niets", lijn.deel_eraf(proef, np.zeros((0, 3)), R, o, a, b).shape == (0,))
# a triangle across the cut line is clipped at the plane: the light stops on the line (x = 50)
schuin = np.array([[40, 0, 30], [60, 0, 28], [60, 0, 32]])
h = lijn.eraf_hoeken(schuin, np.array([[0, 1, 2]]), R, o, a, b)
stap("tekenen: driehoek over de snede wordt op het vlak afgeknipt", len(h) >= 1 and h[:, :, 0].min() > 49.999 and h[:, :, 0].max() < 60.001,
     f"{len(h)} stukjes, x {h[:, :, 0].min():.3f} tot {h[:, :, 0].max():.3f}")
opp = sum(0.5 * np.linalg.norm(np.cross(t[1] - t[0], t[2] - t[0])) for t in h)
stap("tekenen: afgeknipt deel heeft driekwart van de oppervlakte (punt links valt weg)", abs(opp - 30.0) < 1e-6, f"{opp:.3f} mm2 (heel 40)")
h3 = lijn.eraf_hoeken(proef, tri3, R, o, a, b)
stap("tekenen: hele driehoeken blijven heel", len(h3) == 1 and np.allclose(h3[0], proef[:3]))

print(f"[sj-logica] KLAAR {len(fouten)} FOUT {fouten}")
sys.exit(1 if fouten else 0)
