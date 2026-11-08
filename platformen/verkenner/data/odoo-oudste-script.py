#!/usr/bin/env python3
"""Voor modules uit odoo-pagina-script: ID van de oudste versie ophalen (module-leeftijd = laagste ID).
Gebruik: python3 odoo-oudste-script.py in.json uit.json"""
import sys,re,json,subprocess,concurrent.futures as cf,time
r=json.load(open(sys.argv[1]))
def get(u):
    for i in range(3):
        p=subprocess.run(["curl","-sL","--max-time","40",u],capture_output=True,text=True)
        if p.returncode==0 and len(p.stdout)>5000: return p.stdout
        time.sleep(2)
    return ""
def f(x):
    x=dict(x); vs=[v for v in x['versies'] if float(v)<19]
    if not vs: x['oudste_versie']='19.0'; x['oudste_id']=x['id']; return x
    v=min(vs,key=float); h=get(f"https://apps.odoo.com/apps/modules/{v}/{x['naam']}")
    m=re.search(r'js_module_id" type="hidden" value="(\d+)',h)
    x['oudste_versie']=v; x['oudste_id']=int(m.group(1)) if m else None; return x
with cf.ThreadPoolExecutor(3) as ex: out=list(ex.map(f,r))
json.dump(out,open(sys.argv[2],'w')); print(len(out))
