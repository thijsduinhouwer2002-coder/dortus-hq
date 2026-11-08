#!/usr/bin/env python3
"""Analyse van een momentopname van highlevel-apps-meet.py. Gebruik: python3 -I data/highlevel-apps-analyse.py <bestand.json>"""
import json, sys, statistics as st, collections as C
apps = json.load(open(sys.argv[1]))["apps"]
def ins(a): return a.get("totalInstallations") or 0
def oid_jaar(a):  # datum uit de appId (Mongo ObjectId), echte aanmaakdatum van de app
    import datetime; return datetime.datetime.utcfromtimestamp(int(a["appId"][:8],16)).strftime("%Y-%m")
print("totaal", len(apps), "installs samen", sum(ins(a) for a in apps))
pm = C.Counter(oid_jaar(a) for a in apps)
print("nieuwe apps per maand (appId):", sorted(pm.items())[-26:])
pj = C.Counter(oid_jaar(a)[:4] for a in apps); print("per jaar", sorted(pj.items()))
paid = [a for a in apps if a.get("isPaidApp")]
print("betaald", len(paid), "freemium", sum(1 for a in apps if a.get("isFreemium")), "proef", sum(1 for a in apps if a.get("hasFreeTrial")))
pp = C.Counter(oid_jaar(a)[:4] for a in paid); print("betaald per jaar", sorted(pp.items()))
def q(xs):
    xs=sorted(xs); n=len(xs)
    return (n, xs[n//2] if n else 0, xs[int(n*.75)] if n else 0, xs[int(n*.9)] if n else 0, sum(1 for x in xs if x>=100), sum(1 for x in xs if x>=1000))
for naam, groep in [("alle", apps), ("betaald", paid)]:
    for per in ["2024","2025","2026"]:
        g=[ins(a) for a in groep if oid_jaar(a)[:4]==per]
        print(naam, per, "n, mediaan, p75, p90, >=100, >=1000:", q(g))
# betaalde apps van maart tot aug 2026 (2 tot 8 maanden oud)
g=[a for a in paid if "2026-03"<=oid_jaar(a)<="2026-08"]
print("betaald mrt-aug 2026", q([ins(a) for a in g]))
g=[a for a in apps if "2026-03"<=oid_jaar(a)<="2026-08"]
print("alle mrt-aug 2026", q([ins(a) for a in g]))
print("\ntop 25 installs:")
for a in sorted(apps,key=ins,reverse=True)[:25]:
    print(ins(a), a["name"][:40], "|", a.get("companyName","")[:25], "|", oid_jaar(a), "| betaald" if a.get("isPaidApp") else "", a.get("subcategory"))
print("\ntop 25 betaald:")
for a in sorted(paid,key=ins,reverse=True)[:25]:
    print(ins(a), a["name"][:40], "|", a.get("companyName","")[:25], "|", oid_jaar(a), a.get("averageRating"), a.get("totalReviews"), a.get("subcategory"))
cat=C.Counter(); ci=C.Counter(); cp=C.Counter()
for a in apps:
    for s in a.get("subcategory") or ["-"]:
        cat[s]+=1; ci[s]+=ins(a); cp[s]+= 1 if a.get("isPaidApp") else 0
print("\ncategorie: apps, betaald, installs")
for s,n in cat.most_common(): print(f"{s:30} {n:5} {cp[s]:4} {ci[s]:9}")
mk=C.Counter(a.get("companyName") for a in apps); print("\nmakers", len(mk), "grootste", mk.most_common(8))
