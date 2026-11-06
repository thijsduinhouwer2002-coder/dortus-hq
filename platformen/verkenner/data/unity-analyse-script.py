# Analyse van unity-tools-2026-11-06.json. Gebruik: python3 -I unity-analyse-script.py <json>
import json, sys, statistics as st, collections as C
d = [o for o in json.load(open(sys.argv[1])) if not o.get("fout")]
def groep(naam, g):
    if not g: return
    b = [o["beoordelingen"] or 0 for o in g]; r = [o["reviews"] or 0 for o in g]
    n = len(g)
    print(f"{naam}: n={n} mediaan beoord={st.median(b)} gem={sum(b)/n:.1f} >=1:{sum(x>=1 for x in b)/n:.0%} >=5:{sum(x>=5 for x in b)/n:.0%} >=10:{sum(x>=10 for x in b)/n:.0%} >=25:{sum(x>=25 for x in b)/n:.0%} | reviews>=1:{sum(x>=1 for x in r)/n:.0%} max={max(b)}")
cohorten = {"2025 jan-jun (16-22 mnd)": ("2025-01","2025-06"), "2025 jul-dec (10-16 mnd)": ("2025-07","2025-12"),
            "2026 jan-apr (6-10 mnd)": ("2026-01","2026-04"), "2026 mei-aug (3-6 mnd)": ("2026-05","2026-08"),
            "2026 sep-nov (0-2 mnd)": ("2026-09","2026-11")}
for naam,(a,z) in cohorten.items():
    g = [o for o in d if a <= (o["eerst"] or "")[:7] <= z]
    groep(naam+" alles", g)
    groep(naam+" betaald", [o for o in g if not o["vrij"]])
    groep(naam+" gratis", [o for o in g if o["vrij"]])
    p = [float(o["prijs"]) for o in g if not o["vrij"] and o["prijs"]]
    if p: print("   prijsmediaan betaald", st.median(p), "aandeel betaald", f"{len(p)/len(g):.0%}")

# Zonder vervolgversies (Unity neemt beoordelingen van de vorige versie soms mee, zie PlayMaker 2)
import re
VERV = re.compile(r"(\b(v|ver\.?|version)\s?\d+(\.\d+)?\b|\b[2-9]\b|\b(19|20)\d\d\b|\bpro edition\b)", re.I)
pc = C.Counter(o["uitgever_id"] for o in d)
print("\n== zonder vervolgversies (naam met versienummer of jaartal eruit) ==")
for naam,(a,z) in cohorten.items():
    g = [o for o in d if a <= (o["eerst"] or "")[:7] <= z and not VERV.search(o["naam"] or "")]
    groep(naam+" betaald", [o for o in g if not o["vrij"]])
    groep(naam+" betaald, uitgever met 1 tot 3 tools sinds eind 2024", [o for o in g if not o["vrij"] and pc[o["uitgever_id"]] <= 3])
print("uitgevers per cohort mei-aug 2026:", len({o["uitgever_id"] for o in d if "2026-05" <= (o["eerst"] or "")[:7] <= "2026-08"}))
