# Telt nieuwe apps per maand, betaald of gratis, en makers. Gebruik: python3 autodesk-analyse-script.py <apps.jsonl>
import json, sys, collections as C, statistics as st
x = [json.loads(l) for l in open(sys.argv[1])]; x = [a for a in x if "fout" not in a]
# Echt betaald: eenmalig, maand- of jaarabonnement, of een bedrag boven 0. Alleen proef (UNLIMITED_TRIAL) of SUBSCRIPTION_ADSK telt niet.
def betaald(a): return any(p["type"] in ("ONE_TIME", "SUBSCRIPTION_MONTHLY", "SUBSCRIPTION_ANNUAL") or any(float(b[0] or 0) > 0 for b in p["bedragen"]) for p in a["prijzen"])
print("apps", len(x), "betaald", sum(map(betaald, x)))
print("prijstypes", C.Counter(p["type"] for a in x for p in a["prijzen"]).most_common())
jaar = C.Counter((a["eerste"] or "")[:4] for a in x); print("per jaar eerste uitgave", sorted(jaar.items()))
nieuw = [a for a in x if (a["eerste"] or "") >= "2025-11"]
maand = C.Counter(a["eerste"][:7] for a in x if (a["eerste"] or "") >= "2025-01"); print("per maand", sorted(maand.items()))
print("nieuw sinds nov 2025", len(nieuw), "betaald", sum(map(betaald, nieuw)))
print("makers nieuw", C.Counter(a["maker"] for a in nieuw).most_common(15))
print("producten nieuw", C.Counter(p for a in nieuw for p in a["producten"]).most_common(10))
for typ in ("ONE_TIME", "SUBSCRIPTION_MONTHLY", "SUBSCRIPTION_ANNUAL"):
    bed = [float(b[0]) for a in nieuw for p in a["prijzen"] if p["type"] == typ for b in p["bedragen"] if b[0] and float(b[0]) > 0 and b[1] == "USD"]
    if bed: print("mediaanprijs nieuw", typ, st.median(bed), "n", len(bed))
