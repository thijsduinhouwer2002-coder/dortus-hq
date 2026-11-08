#!/usr/bin/env python3
"""Odoo Apps Store: systematische steekproef van lijstpagina's (betaalde modules, een serie).
Gebruik: python3 odoo-lijst-script.py 19.0 10 uit.json  (elke 10e pagina)
Respecteert robots.txt: alleen /page/N in het pad, geen ?order= of ?page=."""
import sys, re, json, subprocess, concurrent.futures as cf, time
serie, stap, uit = sys.argv[1], int(sys.argv[2]), sys.argv[3]
def get(u):
    for i in range(3):
        r = subprocess.run(["curl","-sL","--max-time","40",u],capture_output=True,text=True)
        if r.returncode==0 and len(r.stdout)>5000: return r.stdout
        time.sleep(2)
    return ""
first = get(f"https://apps.odoo.com/apps/modules/browse?price=Paid&series={serie}")
last = max(int(x) for x in re.findall(r'/page/(\d+)\?', first))
pages = list(range(1,last+1,stap))
kaart = re.compile(r'loempia_app_entry loempia_app_card.*?href="/apps/modules/([0-9.]+)/([a-z_0-9A-Z]+)"(.*?)(?=loempia_app_entry loempia_app_card|$)', re.S)
def parse(p):
    h = first if p==1 else get(f"https://apps.odoo.com/apps/modules/browse/page/{p}?price=Paid&series={serie}")
    out=[]
    for v,naam,rest in kaart.findall(h):
        rest=rest[:4000]
        a=re.search(r'loempia_panel_author">\s*<b>(.*?)</b>',rest,re.S)
        pr=re.search(r'oe_currency_value">([\d.,]+)<',rest)
        cur=re.search(r'<span>([^<\d]*)<span class="oe_currency_value',rest)
        tp=re.search(r'Total Purchases: (\d+), Last month: (\d+)',rest)
        vo=re.search(r'title="(\d+) votes"',rest)
        out.append(dict(pagina=p,versie=v,naam=naam,maker=a.group(1).strip() if a else None,
            prijs=float(pr.group(1).replace(',','')) if pr else None,valuta=(cur.group(1).strip() if cur else None),
            aankopen=int(tp.group(1)) if tp else 0,vorige_maand=int(tp.group(2)) if tp else 0,
            stemmen=int(vo.group(1)) if vo else 0))
    return out
res=[]
with cf.ThreadPoolExecutor(3) as ex:
    for r in ex.map(parse,pages): res+=r
json.dump(dict(serie=serie,laatste_pagina=last,stap=stap,kaarten=res),open(uit,'w'))
print(last,len(pages),len(res))
