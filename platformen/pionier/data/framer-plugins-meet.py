#!/usr/bin/env python3
"""Telt de plugins in de Framer Marketplace via de openbare sitemap.
Schrijft een regel naar framer-plugins.csv (datum, totaal, nieuw sinds vorige meting, weg sinds vorige meting)
en bewaart de lijst met namen in framer-plugins-namen.json voor de volgende vergelijking.
Gebruik: python3 data/framer-plugins-meet.py"""
import subprocess, re, json, os, csv, datetime
U="https://www.framer.com/marketplace/sitemap/resources-plugins.xml"
x=subprocess.run(["curl","-sL","--max-time","60",U],capture_output=True,check=True).stdout.decode()
namen=sorted(set(re.findall(r"/marketplace/plugins/([^/<]+)/",x)))
h=os.path.dirname(os.path.abspath(__file__))
pj=os.path.join(h,"framer-plugins-namen.json"); oud=set(json.load(open(pj))) if os.path.exists(pj) else set()
nieuw=[n for n in namen if n not in oud] if oud else []
weg=[n for n in oud if n not in set(namen)]
row={"datum":datetime.date.today().isoformat(),"totaal":len(namen),"nieuw":len(nieuw),"weg":len(weg)}
print(row); print("nieuw (eerste 30):",nieuw[:30])
json.dump(namen,open(pj,"w"))
pc=os.path.join(h,"framer-plugins.csv"); first=not os.path.exists(pc)
with open(pc,"a",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(row))
    if first: w.writeheader()
    w.writerow(row)
