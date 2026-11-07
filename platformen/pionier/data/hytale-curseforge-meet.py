#!/usr/bin/env python3
"""Telt alle Hytale-projecten op CurseForge via de open API-spiegel api.curse.tools (gameId 70216).
Schrijft een regel bij in hytale-curseforge.csv: datum, projecten, downloads, nieuw per maand.
Rustig: 1 verzoek per halve seconde. Gebruik: python3 hytale-curseforge-meet.py"""
import json, time, urllib.request, collections, datetime, os, sys
B="https://api.curse.tools/v1/cf/mods/search?gameId=70216&pageSize=50&sortField=2&sortOrder=desc&index=%d"
items=[];i=0
while True:
    req=urllib.request.Request(B%i,headers={"User-Agent":"dortus-meting"})
    d=json.load(urllib.request.urlopen(req,timeout=30))
    items+=d["data"]; tot=d["pagination"]["totalCount"]; i+=50
    if i>=tot or not d["data"] or i>=10000: break
    time.sleep(0.5)
seen={x["id"]:x for x in items}; items=list(seen.values())
dl=sorted((x["downloadCount"] for x in items),reverse=True)
pm=collections.Counter(x["dateCreated"][:7] for x in items)
cls=collections.Counter(x.get("classId") for x in items)
vandaag=datetime.date.today().isoformat()
print("totaal API",tot,"opgehaald",len(items),"downloads",sum(dl))
print("klassen",dict(cls))
print("nieuw per maand",dict(sorted(pm.items())))
print("plek 1/10/100/500:",[dl[k] for k in (0,9,99,499) if k<len(dl)], "mediaan",dl[len(dl)//2])
if len(sys.argv)>1:
    json.dump(items,open(sys.argv[1],"w"))
f=os.path.join(os.path.dirname(os.path.abspath(__file__)),"hytale-curseforge.csv")
nieuw=not os.path.exists(f)
with open(f,"a") as o:
    if nieuw: o.write("datum,projecten,downloads,mediaan_downloads,nieuw_per_maand\n")
    o.write("%s,%d,%d,%d,\"%s\"\n"%(vandaag,len(items),sum(dl),dl[len(dl)//2],";".join("%s:%d"%kv for kv in sorted(pm.items()))))
