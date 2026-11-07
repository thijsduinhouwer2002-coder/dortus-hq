# Vergelijkt het Forge-bereik van modules die wel en niet in de officiële Foundry-lijst staan.
# Gebruik: python3 foundry-lijst-analyse-script.py <forge-modules.json> <status.txt (id http-code)>
import json, sys, statistics as st, datetime as dt
x = json.load(open(sys.argv[1])); stat = dict(l.split() for l in open(sys.argv[2]) if l.strip())
N = 100 / 0.00136
def t(p): return (p.get("firstPublishAt") or p.get("created") or 0) / 1000
def soort(p):
    u = p.get("url") or ""
    if "patreon" in u or "foundryvtt.store" in u: return "premium"
    return "github" if ("github.com" in u or "gitlab.com" in u) else "ander"
def rapport(s, label):
    v = sorted(round((p["installs"] or 0) * N / 100) for p in s); n = len(v)
    if not n: print(label, "n=0"); return
    print(f"{label}: n={n} mediaan={st.median(v)} p75={v[int(n*.75)]} p90={v[int(n*.9)]} max={v[-1]} "
          f"10+={sum(i>=10 for i in v)/n:.0%} 50+={sum(i>=50 for i in v)/n:.0%} 100+={sum(i>=100 for i in v)/n:.0%} 0={sum(i==0 for i in v)/n:.0%}")
for a, b, lab in [((2026,5,1),(2026,9,1),"mei-aug 2026"), ((2025,5,1),(2026,5,1),"mei 2025-apr 2026")]:
    s = [p for p in x if dt.datetime(*a).timestamp() <= t(p) < dt.datetime(*b).timestamp() and p["id"] in stat]
    for k in ["github", "premium", "ander"]:
        for c, nm in [("200", "in lijst"), ("404", "NIET in lijst")]:
            rapport([p for p in s if soort(p) == k and stat[p["id"]] == c], f"{lab} {k} {nm}")
