#!/usr/bin/env python3
"""Telt de integraties op https://vercel.com/marketplace met hun goedkeuringsdatum (approvedAt).

Gebruik: python3 -I data/vercel-marketplace-meet.py
Schrijft data/vercel-marketplace-<datum>.json en drukt per jaar en per maand het aantal af.
Let op: approvedAt is de datum van de integratie, ook van oude koppelingen van voor de
native Marketplace (aug 2024). Tellingen van installs staan niet in de pagina.
"""
import datetime, json, re, subprocess, sys, collections, os

html = subprocess.run(["curl", "-sS", "-L", "https://vercel.com/marketplace"],
                      capture_output=True, text=True, check=True).stdout
s = html.replace('\\"', '"')
items = {}
for m in re.finditer(r'"approvedAt":(\d+)', s):
    seg = s[max(0, m.start() - 1500):m.start()]
    slug = re.findall(r'"slug":"([^"]{1,60})"', seg)
    name = re.findall(r'"name":"([^"]{1,60})"', seg)
    if not slug:
        continue
    d = datetime.datetime.fromtimestamp(int(m.group(1)) / 1000, datetime.timezone.utc).date()
    items.setdefault(slug[-1], {"slug": slug[-1], "naam": name[-1] if name else "", "goedgekeurd": d.isoformat()})

tags = collections.Counter(t for g in re.findall(r'"tagIds":\[([^\]]*)\]', s)
                           for t in g.replace('"', '').split(',') if t)
vandaag = datetime.date.today().isoformat()
uit = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"vercel-marketplace-{vandaag}.json")
json.dump({"datum": vandaag, "items": sorted(items.values(), key=lambda x: x["goedgekeurd"]),
           "tags": tags.most_common()}, open(uit, "w"), ensure_ascii=False, indent=1)

perjaar = collections.Counter(v["goedgekeurd"][:4] for v in items.values())
permaand = collections.Counter(v["goedgekeurd"][:7] for v in items.values() if v["goedgekeurd"] >= "2025-01")
print("totaal producten met approvedAt:", len(items))
print("per jaar:", dict(sorted(perjaar.items())))
print("per maand vanaf 2025:", dict(sorted(permaand.items())))
print("geschreven:", uit)
