# Vera, 7 nov 2026. Open VSX: alle extensies via de zoek-API, dan een steekproef met
# de datum van de eerste versie (oudste versie in allVersions).
# Gebruik: python3 openvsx-haal-script.py uitmap [steekproefgrootte]
import json, sys, random, subprocess, concurrent.futures as cf, os
out=sys.argv[1]; N=int(sys.argv[2]) if len(sys.argv)>2 else 2500
def j(url):
    for _ in range(3):
        t=subprocess.run(["curl","-s","-m","40",url],capture_output=True,text=True).stdout
        try: return json.loads(t)
        except Exception: pass
    return None
B="https://open-vsx.org/api"
tot=j(B+"/-/search?size=1")["totalSize"]
def page(o):
    d=j(B+"/-/search?size=100&offset=%d&sortBy=timestamp&sortOrder=desc"%o); return (d or {}).get("extensions",[])
alle={}
with cf.ThreadPoolExecutor(8) as ex:
    for res in ex.map(page,range(0,tot+100,100)):
        for e in res: alle["%s.%s"%(e["namespace"],e["name"])]=dict(ns=e["namespace"],naam=e["name"],dl=e.get("downloadCount",0),verified=e.get("verified"),laatst=e.get("timestamp"))
json.dump(alle,open(os.path.join(out,"openvsx-alle.json"),"w"))
print("totaal",tot,"opgehaald",len(alle))
ns_count={}
for e in alle.values(): ns_count[e["ns"]]=ns_count.get(e["ns"],0)+1
random.seed(11); keys=random.sample(sorted(alle),min(N,len(alle)))
def det(k):
    e=dict(alle[k]); d=j("%s/%s/%s"%(B,e["ns"],e["naam"]))
    if not d or "allVersions" not in d: return e
    vs=[v for v in d["allVersions"] if v!="latest" and v!="pre-release"]
    e["versies"]=len(vs); e["prijs_link"]=d.get("sponsorLink"); e["repo"]=d.get("repository")
    e["ns_ext"]=ns_count[e["ns"]]; e["maker"]=(d.get("publishedBy") or {}).get("loginName")
    if vs:
        f=j("%s/%s/%s/%s"%(B,e["ns"],e["naam"],vs[-1])); e["eerste"]=(f or {}).get("timestamp")
    return e
with open(os.path.join(out,"openvsx-steekproef.jsonl"),"w") as f, cf.ThreadPoolExecutor(12) as ex:
    for r in ex.map(det,keys): f.write(json.dumps(r)+"\n")
