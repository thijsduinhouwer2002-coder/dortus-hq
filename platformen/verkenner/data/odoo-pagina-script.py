#!/usr/bin/env python3
"""Odoo Apps Store: modulepagina's lezen voor ID (oplopend, maat voor leeftijd) en beschikbare versies.
Gebruik: python3 odoo-pagina-script.py lijst.json aantal uit.json [seed]"""
import sys, re, json, subprocess, random, concurrent.futures as cf, time
d=json.load(open(sys.argv[1])); n=int(sys.argv[2]); uit=sys.argv[3]
random.seed(int(sys.argv[4]) if len(sys.argv)>4 else 1)
kaarten=d['kaarten']; serie=d['serie']
keuze=random.sample(kaarten,min(n,len(kaarten)))
def get(u):
    for i in range(3):
        r=subprocess.run(["curl","-sL","--max-time","40",u],capture_output=True,text=True)
        if r.returncode==0 and len(r.stdout)>5000: return r.stdout
        time.sleep(2)
    return ""
def lees(k):
    h=get(f"https://apps.odoo.com/apps/modules/{serie}/{k['naam']}")
    m=re.search(r'js_module_id" type="hidden" value="(\d+)',h)
    blok=h.split('loempia_app_availability',1)[1][:6000] if 'loempia_app_availability' in h else ''
    vers=sorted(set(re.findall(r'href="/apps/modules/([0-9]+\.0)/'+re.escape(k['naam'])+'"',blok)),key=float)
    k=dict(k); k.update(id=int(m.group(1)) if m else None, versies=vers)
    return k
with cf.ThreadPoolExecutor(3) as ex: res=list(ex.map(lees,keuze))
json.dump(res,open(uit,'w')); print(len(res), sum(1 for r in res if r['id']))
