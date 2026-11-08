#!/usr/bin/env python3
"""Telt de Grafana-plugincatalogus via de open API (grafana.com/api/plugins).
Schrijft een regel bij in grafana-plugins.csv: datum, totaal, betaald in de marketplace, per soort, nieuw dit jaar.
Gebruik: python3 grafana-plugins-meet.py"""
import json, urllib.request, collections, datetime, os
d=json.load(urllib.request.urlopen(urllib.request.Request("https://grafana.com/api/plugins",headers={"User-Agent":"dortus-meting"}),timeout=60))
it=d["items"]
mk=[x for x in it if x.get("versionDistributionType")=="marketplace"]
soort=collections.Counter(x["typeName"] for x in mk)
makers=collections.Counter(x["orgName"] for x in mk)
jaar=str(datetime.date.today().year)
nieuw=[x for x in it if x["createdAt"][:4]==jaar]
print("totaal",len(it),"marketplace",len(mk),dict(soort))
print("makers marketplace",makers.most_common())
print("nieuw dit jaar",len(nieuw))
f=os.path.join(os.path.dirname(os.path.abspath(__file__)),"grafana-plugins.csv")
n=not os.path.exists(f)
with open(f,"a") as o:
    if n: o.write("datum,totaal,marketplace,mk_datasource,mk_panel,mk_app,mk_makers,nieuw_dit_jaar\n")
    o.write("%s,%d,%d,%d,%d,%d,%d,%d\n"%(datetime.date.today(),len(it),len(mk),soort.get("Data Source",0),soort.get("Panel",0),soort.get("Application",0),len(makers),len(nieuw)))
