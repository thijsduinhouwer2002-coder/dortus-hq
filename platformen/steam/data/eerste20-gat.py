import sys, json, copy, statistics as S
sys.path.insert(0, "/home/claude/dortus-hq/producten/steam-hol/sim")
import sim
base = json.load(open("/home/claude/dortus-hq/producten/steam-hol/sim/voortgang-v3-eind-bram.json"))
sim.SPEL_ECONOMIE, sim.SOORTEN, sim.REEKS = True, True, True
def run(dr):
    spec = copy.deepcopy(base)
    for n in spec["sporen"][0]["niveaus"]:
        if n["niveau"] in dr: n["drempel"] = dr[n["niveau"]]
    gaten=[]; h5=[]; h3=[]; h6=[]
    for z in range(1, 17):
        st = sim.speel(0.6, z, spec)
        ev = [(a[0], a[1], a[2]) for a in st.get("ontgrendeld", [])]
        ev += [(a[0], "koop", i) for i, a in enumerate(st["aankopen"])]
        t = sorted(e[0] for e in ev if 30 < e[0] <= 1200) + [1200]
        g = max(b-a for a, b in zip([60]+t, t))/60
        gaten.append(g)
        hol = {a[2]: a[0]/60 for a in st.get("ontgrendeld", []) if a[1]=="hol-niveau"}
        h3.append(hol.get(3,99)); h5.append(hol.get(5,99)); h6.append(hol.get(6,99))
    return "langste gat min 1-20: mediaan %.1f ergste %.1f | hol3 %.1f hol5 %.1f hol6 %.1f (mediaan)" % (S.median(gaten), max(gaten), S.median(h3), S.median(h5), S.median(h6))
for naam, dr in [("nu 3/6/10/12/20", {}), ("3/4/8/12/17", {3:4,4:8,6:17}), ("2/4/8/12/17", {2:2,3:4,4:8,6:17})]:
    print(naam, "|", run(dr))
