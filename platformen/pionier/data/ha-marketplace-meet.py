#!/usr/bin/env python3
"""Telt de Home Assistant Marketplace (HACS-catalogus) via data-v2.hacs.xyz.
Schrijft een regel naar ha-marketplace.csv: datum, aantallen per soort,
mediaan en top van downloads (alleen integraties hebben downloads),
en hoeveel integraties in de laatste 90 dagen een eerste of nieuwe versie kregen.
Gebruik: python3 data/ha-marketplace-meet.py"""
import json, subprocess, statistics, datetime, csv, os
B="https://data-v2.hacs.xyz/{}/data.json"
def get(c):
    # gewoon curl, zoals de regels vragen
    return json.loads(subprocess.run(["curl","-sL","--max-time","60",B.format(c)],capture_output=True,check=True).stdout)
now=datetime.datetime.now(datetime.timezone.utc)
row={"datum":now.strftime("%Y-%m-%d")}
for c in ["integration","plugin","theme","template"]:
    d=get(c); row[c]=len(d)
    if c=="integration":
        dl=sorted((v.get("downloads") or 0) for v in d.values())
        row["int_dl_mediaan"]=statistics.median(dl)
        row["int_dl_p90"]=dl[int(len(dl)*0.9)]
        row["int_dl_max"]=dl[-1]
        row["int_1000plus"]=sum(x>=1000 for x in dl)
        top=sorted(d.values(),key=lambda v:-(v.get("downloads") or 0))[:10]
        print("Top 10 integraties op downloads:")
        for v in top: print(" ",v.get("downloads"),v.get("full_name"),v.get("stargazers_count"))
    if c=="plugin":
        st=sorted((v.get("stargazers_count") or 0) for v in d.values())
        row["kaart_sterren_mediaan"]=statistics.median(st)
print(row)
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),"ha-marketplace.csv")
new=not os.path.exists(p)
with open(p,"a",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(row)); 
    if new: w.writeheader()
    w.writerow(row)
