"""Analyse van een meting van ctrader-store-meet.py. Gebruik: python3 -I data/ctrader-store-analyse.py data/ctrader-store-<datum>.json"""
import sys, json, statistics as st, collections as C
d = json.load(open(sys.argv[1])); P = [p for p in d["producten"] if p.get("status") == "Active"] ; S = d["verkopers"]
print("producten totaal", len(d["producten"]), "actief", len(P), "verkopers", len(S), "mislukt", len(d["mislukt"]))
print("per type", C.Counter(p["type"] for p in P))
betaald = [p for p in P if (p["price"] or 0) > 0 or p.get("minSubscriptionPrice")]
print("betaald", len(betaald), "gratis", len(P) - len(betaald), "met abonnement", sum(1 for p in P if p.get("minSubscriptionPrice")))
print("prijs mediaan betaald", st.median([p["price"] for p in betaald if p["price"]] or [0]))
# leeftijd via laatste versiedatum en id-banden
ids = sorted(p["productId"] for p in d["producten"])
print("id min/max", ids[0], ids[-1])
def band(p): return (p["productId"] // 1000) * 1000
print("gebruikers (userCount) per id-band, mediaan/aantal:")
for b, g in sorted(C.defaultdict(list, {}).items()): pass
grp = C.defaultdict(list)
for p in P: grp[(band(p), "betaald" if p in betaald else "gratis")].append(p["userCount"] or 0)
for k in sorted(grp): print(" ", k, len(grp[k]), "mediaan", st.median(grp[k]), "max", max(grp[k]))
# verkopers
sales = sorted(((v.get("totalSales") or 0), v.get("nickName"), v.get("joinAt", "")[:10], v.get("totalFreeInstalls")) for v in S.values())[::-1]
tot = sum(s[0] for s in sales)
print("totaal verkopen alle verkopers", tot, "verkopers met >=1 verkoop", sum(1 for s in sales if s[0] > 0), ">=10", sum(1 for s in sales if s[0] >= 10), ">=100", sum(1 for s in sales if s[0] >= 100))
print("top 15 verkopers op verkopen:"); [print("  ", s) for s in sales[:15]]
joins = C.Counter((v.get("joinAt") or "")[:7] for v in S.values())
print("verkopers per maand lid geworden:", sorted(joins.items()))
nieuw = [v for v in S.values() if (v.get("joinAt") or "") >= "2026-01"]
print("verkopers sinds 2026:", len(nieuw), "mediaan verkopen", st.median([v.get("totalSales") or 0 for v in nieuw] or [0]), "met >=10 verkopen", sum(1 for v in nieuw if (v.get("totalSales") or 0) >= 10))
# hulpmiddelen (geen strategie)
kw = {"risico/lotgrootte": ["risk", "lot size", "position size", "calculator"], "trade manager": ["trade manager", "break even", "breakeven", "trailing", "partial"],
      "prop-regels": ["prop", "daily loss", "drawdown", "equity protect", "challenge"], "copier": ["copier", "copy trade", "mirror"],
      "journaal": ["journal", "statistic", "analytics", "dashboard"], "alerts/telegram": ["telegram", "alert", "notification"], "nieuws": ["news", "calendar"], "sessie": ["session"]}
for k, ws in kw.items():
    g = [p for p in P if any(w in (p["title"] + " " + (p.get("shortDescription") or "") + " " + " ".join(p["tags"])).lower() for w in ws)]
    gb = [p for p in g if p in betaald]
    top = sorted(g, key=lambda p: -(p["userCount"] or 0))[:5]
    print(f"\n[{k}] {len(g)} producten, {len(gb)} betaald, typen {dict(C.Counter(p['type'] for p in g))}")
    for p in top: print("   ", p["productId"], p["type"], repr(p["title"][:45]), p["userNick"], "gebruikers", p["userCount"], "prijs", p["price"], "abo", p.get("minSubscriptionPrice"), "rev", p["reviews"])
