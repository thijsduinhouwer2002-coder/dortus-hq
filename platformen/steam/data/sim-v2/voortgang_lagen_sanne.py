"""Bram 16 nov: Sannes voortgang (platformen/steam/data/voortgang.json) met lagen en de volle economie, geijkt.
Gebruik: python3 voortgang_lagen.py [luik2,luik3,luik4] [upg1..upg6] [factor1..factor4]
1. doeluren = de tijden uit Sannes eigen uitkomst (sim zonder lagen, voortgang-uitkomst.txt);
2. lagen_spec: graven kost goud, upgrades 4/5/6 op hol 13/25/34, luik op hol 20/30/40, prijsfactor per laag,
   hoeden uit de lagen erboven tellen niet voor Gloops toren (wel voor de berg);
3. ijken: drempels van hol-niveau, laagsterren en bewoners zo dat ze weer op de doeluren vallen terwijl de gevangen
   helden van alle lagen meetellen; schrijft voortgang-lagen-bram.json naast dit script en toont het lagenrapport."""
import json, os, sys
import sim
hier = os.path.dirname(os.path.abspath(__file__))
pad = "/home/claude/dortus-hq/platformen/steam/data/voortgang.json"
a = sys.argv[1:]
luik = tuple(float(x) for x in a[0].split(",")) if a else (500, 1000, 1500)
upg = [float(x) for x in a[1].split(",")] if len(a) > 1 else [45, 126, 353, 600, 1000, 1600]
factor = [float(x) for x in a[2].split(",")] if len(a) > 2 else [1, 1, 1.5, 2]
# nieuwe dingen met een prijs: elk hol-niveau vanaf 13 dat een kamer, val of bewoner geeft (geen held, trek of
# hoedenpakket; die komen vanzelf), prijs ongeveer 1 uur goud van dat moment (Fenna punt 5: verhouding vlak)
DING_PRIJS = float(a[3]) if len(a) > 3 else 1.0
import ast
DINGEN_NIV = ast.literal_eval(os.environ["DINGEN"]) if os.environ.get("DINGEN") else {14: 1, 16: 1, 17: 1, 22: 2, 23: 2, 24: 2, 29: 2, 32: 3, 33: 3, 38: 3, 42: 4, 43: 4, 45: 4, 46: 4, 49: 4}
DECOR = ast.literal_eval(os.environ.get("DECOR","{}"))
GPU = dict(zip((1, 2, 3, 4), (float(x) for x in os.environ.get("GPU", "450,700,950,1200").split(","))))   # goud per uur per laag (sim, mediaan, zie rapport "goud/u")
dingen = {n: round(DING_PRIJS * GPU[l], -1) for n, l in DINGEN_NIV.items()}
dingen.update({n: round(1.25 * GPU[l], -1) for n, l in DECOR.items()})
orig = json.load(open(pad))
# doeluren uit Sannes ontwerp: zelfde sim zonder lagen (geeft de tijden in haar tabel)
sim.SPEL_ECONOMIE, sim.SOORTEN = True, True
plain = [sim.speel(100, z, orig) for z in range(1, 9)]
sim.SPEL_ECONOMIE, sim.SOORTEN = False, False
doel = {sp["naam"]: {n: (t / 3600 if t else None) for n, t in sim.niveau_tijden(plain, sp["naam"]).items()} for sp in orig["sporen"]}
spec = sim.lagen_spec(orig, luik, upg, False, factor, gloop_oud=False, dingen=dingen)
spec["oud_goud"] = float(os.environ.get("OUD_GOUD", "1"))
if os.environ.get("HOOG"): spec["laag_factor_hoog"] = [float(x) for x in os.environ["HOOG"].split(",")]
spec = sim.ijken(spec, doel)
spec["_uitleg"] = ("Bram 16 nov: Sannes voortgang.json versie 1 met lagen (luik %s op hol 20/30/40), graven kost goud, upgrades %s, "
                   "prijsfactor per laag %s, oude lagen geven %s x hun goud, drempels geijkt op haar doeluren terwijl helden uit alle lagen meetellen. "
                   "Gemaakt met producten/steam-hol/sim/voortgang_lagen.py." % ("/".join("%g" % x for x in luik), "/".join("%g" % x for x in upg), "/".join("%g" % x for x in factor), os.environ.get("OUD_GOUD", "1")))
uit = os.path.join(hier, "voortgang-lagen-sanne.json")
json.dump(spec, open(uit, "w"), indent=1, ensure_ascii=False)
alle = sim.lagen(uit, luik, upg, False, factor=factor, gloop_oud=False, spec=spec)
# drempels naast elkaar: Sanne (zonder lagen) en geijkt (met lagen)
o = {nv["niveau"]: nv["drempel"] for nv in orig["sporen"][0]["niveaus"]}
n = {nv["niveau"]: nv["drempel"] for nv in spec["sporen"][0]["niveaus"]}
print("  drempels hol-niveau (gevangen helden), Sanne -> geijkt met lagen:")
print("    " + "  ".join("%d: %d->%d" % (k, o[k], n[k]) for k in sorted(o) if k % 2 == 0 or k in (13, 25, 34)))
print("geschreven:", uit)
