#!/usr/bin/env python3
"""Haalt alle openbare apps uit de HighLevel App Marketplace (open API, geen login).
Gebruik: python3 -I data/highlevel-apps-meet.py [uitvoer.json]
Bron: https://backend.leadconnectorhq.com/marketplace/public/all?limit=..&skip=..
"""
import json, sys, time, urllib.request, datetime
B = "https://backend.leadconnectorhq.com/marketplace/public/all"
uit = sys.argv[1] if len(sys.argv) > 1 else f"data/highlevel-apps-{datetime.date.today()}.json"
apps, skip, stap = [], 0, 100
while True:
    req = urllib.request.Request(f"{B}?limit={stap}&skip={skip}", headers={"User-Agent": "Mozilla/5.0"})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    rij = d.get("integrations", [])
    apps += rij
    if len(rij) < stap:
        break
    skip += stap
    time.sleep(1)
json.dump({"gemeten": str(datetime.datetime.utcnow()), "totaal_api": d.get("total") or d.get("count"), "apps": apps}, open(uit, "w"), indent=0)
print(len(apps), "apps naar", uit)
