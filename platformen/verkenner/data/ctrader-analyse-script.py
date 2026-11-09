# Analyse van de cTrader-steekproef. Gebruik: python3 -I ctrader-analyse-script.py steek*.jsonl
import json, sys, statistics as S, bisect
from datetime import datetime, timezone
recs = {}
for fn in sys.argv[1:]:
    for l in open(fn):
        r = json.loads(l)
        if "fout" not in r and r.get("soort"): recs[r["id"]] = r
R = sorted(recs.values(), key=lambda r: r["id"])
print("pagina's met data:", len(R))
def dt(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))
# id -> datum: producten op versie 1.0 geven hun startdatum (datum van versie 1.0)
pts = sorted((r["id"], dt(r["versiedatum"])) for r in R if r.get("versie") in ("1.0", "1", "1.0.0") and r.get("versiedatum"))
# maak monotoon: lopend minimum van achter naar voren (oude id kan niet later starten dan nieuwere)
ids = [p[0] for p in pts]; ds = [p[1] for p in pts]
for i in range(len(ds) - 2, -1, -1):
    if ds[i] > ds[i + 1]: ds[i] = ds[i + 1]
def schat(pid):
    i = bisect.bisect_left(ids, pid)
    if i >= len(ids): return ds[-1]
    return ds[i]  # eerste ijkpunt met id >= pid: bovengrens van de startdatum
nu = datetime(2026, 11, 9, tzinfo=timezone.utc)
for r in R:
    r["start"] = schat(r["id"]); r["maanden"] = (nu - r["start"]).days / 30.4
    r["betaald"] = (r.get("prijs") or 0) > 0 or (r.get("abo") or 0) > 0
print("ijkpunten (versie 1.0):", len(pts))
# per kwartaal: aantal in steekproef (x8 = hele winkel)
from collections import Counter, defaultdict
kw = Counter(f"{r['start'].year}-K{(r['start'].month-1)//3+1}" for r in R)
print("start per kwartaal (steekproef, x8 voor de winkel):", sorted(kw.items()))
mnd = Counter(r["start"].strftime("%Y-%m") for r in R if r["start"].year == 2026)
print("2026 per maand:", sorted(mnd.items()))
def stat(g, naam):
    if not g: print(naam, "leeg"); return
    u = [r.get("gebruikers") or 0 for r in g]
    print(f"{naam}: n={len(g)} mediaan gebruikers {S.median(u)}, 10+ {sum(x>=10 for x in u)/len(g):.0%}, 100+ {sum(x>=100 for x in u)/len(g):.0%}, 1000+ {sum(x>=1000 for x in u)/len(g):.0%}, met review {sum((r.get('reviews') or 0)>0 for r in g)/len(g):.0%}, actief {sum(r.get('status')=='Active' for r in g)/len(g):.0%}")
coh = [r for r in R if 3 <= r["maanden"] <= 9]
stat([r for r in coh if not r["betaald"]], "gratis, 3 tot 9 maanden")
stat([r for r in coh if r["betaald"]], "betaald, 3 tot 9 maanden")
stat([r for r in R if r["betaald"]], "betaald, alles")
stat([r for r in R if not r["betaald"]], "gratis, alles")
for s in ("cBot", "Indicator", "Plugin"):
    stat([r for r in coh if r["betaald"] and r.get("soort") == s], f"  betaald {s}, 3-9 mnd")
pr = [r["prijs"] for r in R if (r.get("prijs") or 0) > 0]
print("prijs betaald: mediaan", S.median(pr), "aandeel betaald", f"{sum(r['betaald'] for r in R)/len(R):.0%}", "abonnement", sum((r.get('abo') or 0)>0 for r in R))
# makers
mk = {}
for r in R:
    if r.get("maker_id"): mk[r["maker_id"]] = r
M = list(mk.values())
print("makers in steekproef:", len(M))
v = [m.get("maker_verkopen") or 0 for m in M]
print("verkopen per maker: mediaan", S.median(v), "0:", sum(x==0 for x in v), "10+:", sum(x>=10 for x in v), "50+:", sum(x>=50 for x in v), "100+:", sum(x>=100 for x in v), "500+:", sum(x>=500 for x in v))
nieuw = [m for m in M if m.get("maker_sinds") and dt(m["maker_sinds"]) >= datetime(2025, 7, 1, tzinfo=timezone.utc) and dt(m["maker_sinds"]) <= datetime(2026, 8, 1, tzinfo=timezone.utc)]
vn = [m.get("maker_verkopen") or 0 for m in nieuw]
if vn: print(f"makers lid jul 2025 t/m jul 2026: {len(nieuw)}, verkopen mediaan {S.median(vn)}, 10+ {sum(x>=10 for x in vn)}, 50+ {sum(x>=50 for x in vn)}, 100+ {sum(x>=100 for x in vn)}")
print("top makers op verkopen:")
for m in sorted(M, key=lambda m: -(m.get("maker_verkopen") or 0))[:15]:
    print("  ", m["maker"], m.get("maker_verkopen"), "gratis installs", m.get("maker_gratis_installs"), "lid", (m.get("maker_sinds") or "")[:10])
print("top producten op gebruikers (betaald):")
for r in sorted([r for r in R if r["betaald"]], key=lambda r: -(r.get("gebruikers") or 0))[:10]:
    print("  ", r["id"], r["titel"][:40], r["soort"], r["prijs"], r.get("abo"), "gebruikers", r["gebruikers"], "reviews", r["reviews"], "start", r["start"].date())
