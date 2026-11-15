# Analyse van Activities (vlag EMBEDDED) uit de App Directory.
# Gebruik: python3 -I discord-activities-analyse-script.py dir.json
import json, sys, datetime, statistics, collections
d = json.load(open(sys.argv[1]))
def m(i): return datetime.datetime.fromtimestamp(((int(i)>>22)+1420070400000)/1000, datetime.UTC).strftime("%Y-%m")
act = [a for a in d if a["embedded"]]
print("apps in directory:", len(d), "waarvan Activities (EMBEDDED):", len(act), f"({100*len(act)/len(d):.1f}%)")
per = collections.Counter(m(a["id"])[:7] for a in act)
print("Activities per aanmaakmaand 2025-2026:", {k:v for k,v in sorted(per.items()) if k>="2025-01"})
def stats(lst, label):
    g = [a["guild_count"] or 0 for a in lst]
    if not g: print(label, "geen"); return
    print(f"{label}: n={len(g)} mediaan={statistics.median(g)} 100+={100*sum(x>=100 for x in g)/len(g):.0f}% 1000+={100*sum(x>=1000 for x in g)/len(g):.0f}% 10000+={sum(x>=10000 for x in g)} betaalvlag={sum(bool(a['is_monetized']) for a in lst)} winkel={sum(bool(a['storefront']) for a in lst)} zonder_bot={sum(not a['bot'] for a in lst)}")
stats(act, "alle Activities")
stats([a for a in act if "2026-05"<=m(a["id"])<="2026-08"], "Activities aangemaakt mei-aug 2026 (3 tot 6 mnd)")
stats([a for a in act if "2026-05"<=m(a["id"])<="2026-08" and not a["bot"]], "  idem, zonder bot (pure Activity)")
stats([a for a in act if "2025-09"<=m(a["id"])<="2026-04"], "Activities aangemaakt sep 2025-apr 2026")
stats([a for a in d if not a["embedded"] and "2026-05"<=m(a["id"])<="2026-08"], "ter vergelijking: andere apps mei-aug 2026")
print("\nTop 40 Activities naar servers:")
for a in sorted(act, key=lambda a: -(a["guild_count"] or 0))[:40]:
    print(f"  {a['guild_count']:>9} {m(a['id'])} bot={int(a['bot'])} geld={int(bool(a['is_monetized']))} {a['name'][:40]}")
print("\nActivities sinds 2025-09 met 1000+ servers:")
for a in sorted([a for a in act if m(a["id"])>="2025-09" and (a["guild_count"] or 0)>=1000], key=lambda a:-(a["guild_count"] or 0)):
    print(f"  {a['guild_count']:>9} {m(a['id'])} bot={int(a['bot'])} geld={int(bool(a['is_monetized']))} {a['name'][:40]} | {(a['short'] or '')[:70]}")
