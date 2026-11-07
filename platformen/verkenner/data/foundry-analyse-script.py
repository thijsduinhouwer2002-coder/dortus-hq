# Bereik van nieuwe Foundry-modules, gemeten op de Forge. Gebruik: python3 foundry-analyse-script.py <bestand.json>
import json, sys, statistics as st, datetime as dt
x = json.load(open(sys.argv[1]))
N = 100 / 0.00136  # Forge-gebruikers in de noemer (kleinste stap = 1 gebruiker)
def t(p): return (p.get("firstPublishAt") or p.get("created") or 0) / 1000
def soort(p):
    u = p.get("url") or ""
    if "patreon" in u or "foundryvtt.store" in u: return "premium"
    return "github" if "github.com" in u else "ander"
def rapport(s, label):
    v = sorted(round((p["installs"] or 0) * N / 100) for p in s); n = len(v)
    if not n: return
    print(f"{label}: n={n} mediaan={st.median(v)} p75={v[int(n*.75)]} p90={v[int(n*.9)]} "
          f"10+={sum(i>=10 for i in v)/n:.0%} 50+={sum(i>=50 for i in v)/n:.0%} 100+={sum(i>=100 for i in v)/n:.0%} 0={sum(i==0 for i in v)/n:.0%}")
def tussen(a, b): return [p for p in x if dt.datetime(*a).timestamp() <= t(p) < dt.datetime(*b).timestamp()]
s = tussen((2026,5,1), (2026,9,1)); rapport(s, "mei-aug 2026")
for k in ["github", "premium", "ander"]: rapport([p for p in s if soort(p) == k], "  " + k)
rapport(tussen((2025,11,1), (2026,3,1)), "nov 2025-feb 2026")
rapport(tussen((2025,5,1), (2025,9,1)), "mei-aug 2025")
