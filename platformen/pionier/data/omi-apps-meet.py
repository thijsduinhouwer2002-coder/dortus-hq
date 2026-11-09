#!/usr/bin/env python3
"""Herhaalmeting Omi app store (Noor, 9 nov 2026).

Gebruik: python3 -I omi-apps-meet.py [uitvoer.json]
Haalt alle goedgekeurde apps op uit de open API van Omi en print:
totaal, nieuwe apps per maand, betaalde apps met installs, mediaan installs per jaargang.
Vergelijk met omi-apps-2026-11-09.json.
"""
import collections
import json
import statistics
import sys
import urllib.request

URL = "https://api.omi.me/v1/approved-apps?include_reviews=false"

with urllib.request.urlopen(URL, timeout=120) as r:
    apps = json.load(r)

if len(sys.argv) > 1:
    with open(sys.argv[1], "w") as f:
        json.dump(apps, f)

def datum(a):
    return (a.get("created_at") or "????")[:10]

print("totaal apps:", len(apps), "| zonder datum:", sum(1 for a in apps if not a.get("created_at")))
per_maand = collections.Counter(datum(a)[:7] for a in apps if a.get("created_at"))
print("nieuw per maand:", ", ".join(f"{k} {per_maand[k]}" for k in sorted(per_maand)))
print("installs totaal:", sum(a.get("installs", 0) for a in apps))
betaald = [a for a in apps if a.get("is_paid")]
print("betaald:", len(betaald), "| met 10+ installs:", sum(1 for a in betaald if a.get("installs", 0) >= 10))
for a in sorted(betaald, key=lambda a: -a.get("installs", 0))[:10]:
    print("  ", a.get("installs"), a.get("price"), a.get("payment_plan"), datum(a), a.get("name", "")[:50])
for jaar in ("2024", "2025", "2026"):
    s = [a.get("installs", 0) for a in apps if datum(a).startswith(jaar)]
    if s:
        print(f"jaargang {jaar}: {len(s)} apps, mediaan installs {statistics.median(s)}")
