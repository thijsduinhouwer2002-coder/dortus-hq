"""Plek per zoekterm op Superhive (Bram, issue #161). Gebruik: python3 zoek_superhive.py [termen...]"""
import re,subprocess,urllib.parse,json,sys
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
termen=sys.argv[1:] or ["poseable figure","ball joint","articulated","3d print joints","action figure blender","print in place"]
volg=["click-joints-pro","click-joints-lite","cleave","catpin","split-3dprint","nb-figure-joints","jointlab-","articulator---easy-figure-joint-generator","cut-flex"]
uit={}
for t in termen:
    lijst=[]
    for p in (1,2,3,4):
        u="https://superhivemarket.com/search?search%5Bq%5D="+urllib.parse.quote_plus(t)+f"&page={p}"
        h=subprocess.run(["curl","-sL","-A",UA,u],capture_output=True,text=True).stdout
        ids=[]
        for m in re.findall(r'href="/products/([^"?#]+)\?search_id=',h):
            if m not in ids: ids.append(m)
        if not ids: break
        lijst+= [i for i in ids if i not in lijst]
    uit[t]={"n":len(lijst),"top10":lijst[:10],"plek":{v:(lijst.index(v)+1 if v in lijst else None) for v in volg}}
    print(t,uit[t]["n"],uit[t]["plek"],file=sys.stderr)
json.dump(uit,open("uitslag-superhive.json","w"),indent=1)
