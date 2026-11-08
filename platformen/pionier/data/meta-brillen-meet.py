#!/usr/bin/env python3
"""Volgt de app-markt voor Meta-brillen.
1. Telt de apps in de community-catalogus glassapps.io.
2. Kijkt of de FAQ van Meta nog zegt dat indienen "soon" komt (of dat er een datum staat).
Schrijft een regel naar meta-brillen.csv. Gebruik: python3 data/meta-brillen-meet.py"""
import subprocess, re, html, csv, os, datetime
def get(u): return subprocess.run(["curl","-sL","--max-time","60",u],capture_output=True).stdout.decode(errors="ignore")
g=get("https://glassapps.io")
apps=len(set(re.findall(r'href="/apps?/[^"]+"',g)))
f=get("https://developers.meta.com/wearables/faq/")
t=html.unescape(re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",re.sub(r"<script.*?</script>|<style.*?</style>","",f,flags=re.S))))
m=re.search(r"When can I submit and publish my experience\?(.{0,300})",t)
antwoord=(m.group(1).strip() if m else "VRAAG NIET GEVONDEN, FAQ zelf lezen")[:200]
row={"datum":datetime.date.today().isoformat(),"glassapps":apps,"indienen_nog_soon":"soon" in antwoord.lower(),"faq_antwoord":antwoord}
print(row)
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),"meta-brillen.csv"); first=not os.path.exists(p)
with open(p,"a",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(row))
    if first: w.writeheader()
    w.writerow(row)
