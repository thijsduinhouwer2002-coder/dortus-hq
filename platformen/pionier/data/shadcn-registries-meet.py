#!/usr/bin/env python3
"""Herhaalmeting shadcn-registry's (Noor, 8 nov 2026).
Haalt de officiële lijst (ui.shadcn.com/r/registries.json), telt registry's,
nieuwe per maand (health.firstObservedAt, monitoring begon aug 2026) en categorieën,
en npm-downloads van het pakket shadcn per maand.
Draai: python3 -I data/shadcn-registries-meet.py [vorig-bestand.json]"""
import collections, datetime, json, re, sys, urllib.request

def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read()

d = json.loads(get("https://ui.shadcn.com/r/registries.json"))
vandaag = datetime.date.today().isoformat()
open(f"data/shadcn-registries-{vandaag}.json", "w").write(json.dumps(d))
print("registry's:", len(d))
print("nieuw per maand:", sorted(collections.Counter((x.get("health") or {}).get("firstObservedAt", "?")[:7] for x in d).items()))
cats = {"animatie": r"animat|motion", "blocks/templates": r"block|template|landing", "ai/chat": r"\bai\b|chat|llm|agent",
        "grafiek/data": r"chart|graph|dashboard|table", "auth": r"auth|login|sign.?in", "billing": r"billing|stripe|pricing|payment|checkout",
        "e-commerce": r"commerce|shop|cart", "kalender": r"calendar|schedul", "betaald/premium": r"\b(pro|premium|paid|license|lifetime)\b"}
for k, r in cats.items():
    print(f"  {k}: {sum(1 for x in d if re.search(r, x['description'], re.I))}")
if len(sys.argv) > 1:
    oud = {x["name"] for x in json.load(open(sys.argv[1]))}
    nieuw = [x["name"] for x in d if x["name"] not in oud]
    print("nieuw sinds vorige meting:", len(nieuw))
eind = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
start = (eind - datetime.timedelta(days=365)).replace(day=1)
dl = json.loads(get(f"https://api.npmjs.org/downloads/range/{start}:{eind}/shadcn"))
c = collections.Counter()
for x in dl.get("downloads", []): c[x["day"][:7]] += x["downloads"]
print("npm shadcn per maand:", dict(sorted(c.items())))
