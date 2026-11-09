#!/usr/bin/env python3
"""Telt alle iCUE-widgets (Corsair XENEON EDGE en andere Corsair-schermen) in de Elgato Marketplace.
Openbare API, geen login. Haalt de lijst twee keer op: standaard (velden) en gesorteerd op downloads (alleen volgorde, geen getallen).
Gebruik: python3 -I data/xeneon-widgets-meet.py [uitvoer.json]
"""
import json, sys, time, urllib.request, datetime, collections, statistics as st
uit = sys.argv[1] if len(sys.argv) > 1 else f"data/xeneon-widgets-{datetime.date.today()}.json"
H = {"User-Agent": "Mozilla/5.0", "Origin": "https://marketplace.elgato.com", "Referer": "https://marketplace.elgato.com/"}
def alles(orde):
    u, rij = f"https://mp-gateway.elgato.com/products?extension=widgets&limit=100&ordering={orde}", []
    while u:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60)); rij += d["results"]; u = d["next"]; time.sleep(1)
    return rij
w = alles("-last_published"); rang = [x["id"] for x in alles("-download_count")]
json.dump({"gemeten": datetime.datetime.now(datetime.timezone.utc).isoformat(), "widgets": w, "rang_downloads": rang}, open(uit, "w"))
betaald = [x for x in w if not x["variants"][0]["is_free"]]
print("widgets", len(w), "betaald", len(betaald), "makers", len({x["org_name"] for x in w}))
print("nieuw per maand", sorted(collections.Counter(x["created_at"][:7] for x in w).items()))
print("betaald per maand", sorted(collections.Counter(x["created_at"][:7] for x in betaald).items()))
pr = [x["variants"][0]["price"]["unit_amount"] / 100 for x in betaald if x["variants"][0].get("price")]
print("prijs mediaan", st.median(pr) if pr else None)
eerste = {}
for x in sorted(w, key=lambda x: x["created_at"]): eerste.setdefault(x["org_name"], x["created_at"][:7])
print("nieuwe makers per maand", sorted(collections.Counter(eerste.values()).items()))
print("grootste makers", collections.Counter(x["org_name"] for x in w).most_common(10))
idx = {x["id"]: x for x in w}
print("top 40 op downloads (naam, maker, gratis?)", [(idx[i]["name"], idx[i]["org_name"], idx[i]["variants"][0]["is_free"]) for i in rang[:40] if i in idx])
