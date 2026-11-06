# Analyse van Fab tools en plugins. Gebruik: python3 -I fab-analyse-script.py <tools-detail.json>
import json, sys, statistics as st, collections as C
d = [o for o in json.load(open(sys.argv[1])) if not o.get("fout") and o.get("eerst")]
print("n", len(d), "per maand eerste publicatie:", sorted(C.Counter(o["eerst"][:7] for o in d).items())[-14:])
mk = C.Counter(o["maker"] for o in d)
def rep(n, g):
    if not g: print(n, 0); return
    b = [o["beoordelingen"] or 0 for o in g]; k = len(g)
    p = [o["prijs"] for o in g if (o["prijs"] or 0) > 0]
    print(f"{n}: n={k} mediaan={st.median(b)} >=1:{sum(x>=1 for x in b)/k:.0%} >=5:{sum(x>=5 for x in b)/k:.0%} >=10:{sum(x>=10 for x in b)/k:.0%} >=25:{sum(x>=25 for x in b)/k:.0%} betaald:{len(p)/k:.0%} prijsmediaan:{st.median(p) if p else 0} max={max(b)}")
for n, a, z in [("2025 dec-2026 feb (8-11 mnd, onvolledig)", "2025-12", "2026-02"), ("2026 mrt-apr (6-8 mnd)", "2026-03", "2026-04"),
                ("2026 mei-aug (3-6 mnd)", "2026-05", "2026-08"), ("2026 sep-nov (0-2 mnd)", "2026-09", "2026-11")]:
    g = [o for o in d if a <= o["eerst"][:7] <= z]
    rep(n + " alles", g)
    rep(n + " betaald", [o for o in g if (o["prijs"] or 0) > 0])
    rep(n + " betaald, maker met 1 tot 3 tools", [o for o in g if (o["prijs"] or 0) > 0 and mk[o["maker"]] <= 3])
g = sorted([o for o in d if "2026-05" <= o["eerst"][:7] <= "2026-08"], key=lambda o: -(o["beoordelingen"] or 0))
print("top mei-aug:"); [print(" ", o["beoordelingen"], o["prijs"], o["eerst"][:10], (o["titel"] or "")[:50], "|", o["maker"], mk[o["maker"]]) for o in g[:12]]
