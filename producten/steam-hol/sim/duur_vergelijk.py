"""Bram 16 nov ±19:30 UTC: klopt de sim met het echte spel? Windows-duurtest 43931188663 (main 07c48f9, 20 min gewoon spel,
niemand klikt, drempels 3/5/7/12/17) tegen de sim zonder kopen (40 zaden). Draai: python3 duur_vergelijk.py"""
import sys, os, json, copy, statistics as S
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim
HIER = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HIER, "voortgang-v3-eind-bram.json")))
sim.SPEL_ECONOMIE, sim.SOORTEN, sim.REEKS = True, True, True
DR = {2: 3, 3: 5, 4: 7, 5: 12, 6: 17}
SPEL = {2: 86.2, 3: 366.4, 4: 530.7, 5: 859.7, 6: 1137.3}   # HOL hol-niveau uit hol.log van run 43931188663
spec = copy.deepcopy(base); spec["graven"] = False; spec["upg_prijs"] = [99999] * 6
for n in spec["sporen"][0]["niveaus"]:
    if n["niveau"] in DR: n["drempel"] = DR[n["niveau"]]
tijden = {k: [] for k in DR}; vang20 = []; held20 = []
for z in range(1, 41):
    st = sim.speel(0.34, z, spec)
    assert not st["aankopen"], "sim kocht toch iets"
    for a in st.get("ontgrendeld", []):
        if a[1] == "hol-niveau" and a[2] in tijden: tijden[a[2]].append(a[0])
    r20 = [r for r in st["reeks"] if r[0] <= 1200]
    vang20.append(r20[-1][2] if r20 else 0); held20.append(len(r20))
def q(v, p): v = sorted(v); return v[min(len(v) - 1, int(p * len(v)))]
print("hol  drempel  spel(s)   sim mediaan  sim 10%-90%      in 20 min gehaald (sim)")
for k in sorted(DR):
    v = [t for t in tijden[k] if t <= 1200]
    print("%3d  %7d  %7.0f   %11s  %15s  %d/40" % (k, DR[k], SPEL[k], "%.0f" % S.median(v) if v else "-",
          "%.0f-%.0f" % (q(v, .1), q(v, .9)) if v else "-", len(v)))
print("helden in 20 min: spel 28 binnen, sim mediaan %d (%d-%d)" % (S.median(held20), min(held20), max(held20)))
print("vangsten in 20 min: spel 17+ (hol 6 op 1137 s), sim mediaan %d (%d-%d)" % (S.median(vang20), min(vang20), max(vang20)))
