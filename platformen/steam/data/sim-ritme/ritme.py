"""Sanne 16 nov ±20:00 UTC: keuring 7 van Iris (62% van de tijd geen held in beeld). Welke ritmeknop?
Brams sim (producten/steam-hol/sim/sim.py), speeltestbuild zoals samenval.py deel 3 (graven gratis, upgrades 45/126/353,
drempels 3/5/7/12/17), 40 zaden. Vervangt in de bron alleen de tijd tussen helden en PLAT_S.
Meet: deel van de tijd met een held in beeld (held ±15 s in beeld), mediaan gat zonder held, deel 'geen held en Gloop plat',
langste gat zonder koop of hol-niveau (min 1 tot 20 en 1 tot 60), hol 6 en hol 12, en goud na 60 en 120 min.
Draai: python3 -I platformen/steam/data/sim-ritme/ritme.py"""
import os, sys, json, copy, statistics as S
SIM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../producten/steam-hol/sim")
src = open(os.path.join(SIM, "sim.py")).read().split('if __name__ == "__main__"')[0]
OUD_GAT = 'gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else (35, 45)\n            else:\n                gat = (40, 60)'
OUD_PLAT = 'v["plat_tot"] = t + PLAT_S * (2 / 3 if upg["slijm"] >= 2 else 1)'
assert OUD_GAT in src and OUD_PLAT in src and "PLAT_S = 60" in src
base = json.load(open(os.path.join(SIM, "voortgang-v3-eind-bram.json")))
IN_BEELD = 15.0

def spec_build():
    s = copy.deepcopy(base)
    for n in s["sporen"][0]["niveaus"]:
        n["drempel"] = {3: 5, 4: 7, 6: 17}.get(n["niveau"], n["drempel"])
    s["graven"] = False; s["upg_prijs"] = [45, 126, 353, 99999, 99999, 99999]
    return s

OUD_VOLGENDE = 'volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else rng.uniform(*gat) * (1.0 if stap else eff["gat"]))'
assert OUD_VOLGENDE in src

def maak(begin, later, vroeg_tot, plat, paar=0.0):
    # begin: gat na de vaste stappen 3 en verder; later: gat buiten het begin; vroeg_tot: tot die tijd 'begin'-gat ook buiten BEGIN
    nieuw = ('gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else %r\n            else:\n'
             '                gat = %r if t < %r else (40, 60)') % (begin, later, vroeg_tot)
    s = src.replace(OUD_GAT, nieuw).replace("PLAT_S = 60", "PLAT_S = %r" % plat)
    if paar:   # kans dat de volgende held al na 6 tot 10 s komt (niet tijdens BEGIN, niet tijdens het lied)
        s = s.replace(OUD_VOLGENDE, 'volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else (rng.uniform(6, 10) if (not stap and rng.random() < %r) else rng.uniform(*gat) * (1.0 if stap else eff["gat"])))' % paar)
    s = s.replace(OUD_PLAT, OUD_PLAT + '; st.setdefault("plat_log", []).append((t, v["plat_tot"]))')
    ns = {"__file__": os.path.join(SIM, "sim.py")}
    sys.path.insert(0, SIM)
    exec(s, ns)
    ns["SPEL_ECONOMIE"] = ns["SOORTEN"] = ns["REEKS"] = True
    return ns

def dekking(iv, a, b):
    iv = sorted((max(a, x), min(b, y)) for x, y in iv if y > a and x < b)
    tot, cur = 0.0, None
    for x, y in iv:
        if cur is None or x > cur[1]:
            if cur: tot += cur[1] - cur[0]
            cur = [x, y]
        else:
            cur[1] = max(cur[1], y)
    if cur: tot += cur[1] - cur[0]
    return tot

def meet(ns, eind=1200):
    r = {"beeld": [], "gatmed": [], "leeg": [], "g20": [], "g60": [], "h6": [], "h12": [], "goud60": [], "twee": []}
    for z in range(1, 41):
        st = ns["speel"](2.0, z, spec_build())
        komst = [x[0] for x in st["reeks"]]
        held = [(k, k + IN_BEELD) for k in komst]
        r["beeld"].append(dekking(held, 0, eind) / eind)
        k20 = [k for k in komst if k <= eind]
        gaten = [b - a - IN_BEELD for a, b in zip(k20, k20[1:]) if b - a > IN_BEELD]
        r["gatmed"].append(S.median(gaten) if gaten else 0)
        r["twee"].append(sum(1 for a, b in zip(k20, k20[1:]) if b - a < IN_BEELD) / max(1, len(k20)))
        plat = st.get("plat_log", [])
        # geen held en Gloop plat: plat-tijd min de stukken waarin een held in beeld is
        pt = dekking(plat, 0, eind)
        both = sum(dekking(held, max(0, x), min(eind, y)) for x, y in plat if x < eind)
        r["leeg"].append((pt - both) / eind)
        hol = {a[2]: a[0] / 60 for a in st.get("ontgrendeld", []) if a[1] == "hol-niveau"}
        r["h6"].append(hol.get(6, 999)); r["h12"].append(hol.get(12, 999))
        ev = sorted([a[0] for a in st.get("ontgrendeld", [])] + [a[0] for a in st["aankopen"]])
        for key, e in (("g20", 1200), ("g60", 3600)):
            t = [x for x in ev if 30 < x <= e] + [e]
            r[key].append(max(b - a for a, b in zip([60] + t, t)) / 60)
        r["goud60"].append(len([a for a in st["aankopen"] if a[0] <= 3600]))
    return r

VARIANTEN = [
    ("nu (35-45 / 40-60, plat 60)", (35, 45), (40, 60), 0, 60),
    ("b: plat 30", (35, 45), (40, 60), 0, 30),
    ("a1: 25-35 tot min 20", (25, 35), (25, 35), 1200, 60),
    ("a2: 20-30 tot min 20", (20, 30), (20, 30), 1200, 60),
    ("a3: 25-35 altijd", (25, 35), (25, 35), 1e9, 60),
    ("a4: 30-40 altijd", (30, 40), (30, 40), 1e9, 60),
    ("a1 + plat 30", (25, 35), (25, 35), 1200, 30),
    ("a4 + plat 30", (30, 40), (30, 40), 1e9, 30),
    ("a3 + plat 30", (25, 35), (25, 35), 1e9, 30),
    ("KEUS 28-38 + 15% paar, plat 30", (28, 38), (28, 38), 1e9, 30, 0.15),
]
if __name__ == "__main__":
    print("40 zaden, speeltestbuild, eerste 20 min (beeld/gat/leeg/twee), gaten koop-of-hol in min, hol 6/12 in min, kopen in uur 1 (mediaan)")
    print("%-28s %6s %6s %6s %6s | %5s %5s %5s %5s | %5s %6s | %4s" % ("variant", "beeld", "gat s", "leeg", "twee", "g20m", "g20e", "g60m", "g60e", "hol6", "hol12", "kop1"))
    for naam, b, l, vt, p, *pa in VARIANTEN:
        r = meet(maak(b, l, vt, p, *pa))
        m = S.median
        print("%-28s %5.0f%% %6.0f %5.0f%% %5.0f%% | %5.1f %5.1f %5.1f %5.1f | %5.1f %6.1f | %4.0f" % (
            naam, 100 * m(r["beeld"]), m(r["gatmed"]), 100 * m(r["leeg"]), 100 * m(r["twee"]), m(r["g20"]), max(r["g20"]),
            m(r["g60"]), max(r["g60"]), m(r["h6"]), m(r["h12"]), m(r["goud60"])))
