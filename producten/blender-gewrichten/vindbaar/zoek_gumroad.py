"""Plek per zoekterm op Gumroad Discover (JSON achter gumroad.com/discover). Bram, issue #161."""
import json,subprocess,urllib.parse,sys
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
termen=sys.argv[1:] or ["poseable figure","ball joint","articulated","3d print joints","action figure blender","print in place"]
def zoek(t,van):
    u="https://gumroad.com/products/search?query="+urllib.parse.quote(t)+f"&from={van}"
    return json.loads(subprocess.run(["curl","-sL","-A",UA,"-H","Accept: application/json",u],capture_output=True,text=True).stdout)
uit={}
for t in termen:
    lijst=[];tot=None
    van=1
    while van<=90:
        d=zoek(t,van);tot=d["total"]
        if not d["products"]: break
        for p in d["products"]:
            lijst.append((p["name"][:70],p["seller"]["name"],p["url"].split("?")[0],p["ratings"]["count"]))
        van+=len(d["products"])
    uit[t]={"total":tot,"lijst":lijst}
    print("==",t,"total",tot,"opgehaald",len(lijst))
    for i,(n,s,u,r) in enumerate(lijst,1):
        k=n.lower()+s.lower()+u
        if i<=5 or any(w in k for w in ["click joint","dortus","duinhouwer","cleave","catpin","split","joint","v4ss3ur","sokol"]):
            print(f"  {i:2} {n} | {s} | {u} | r{r}")
json.dump(uit,open("uitslag-gumroad-"+("eigen" if sys.argv[1:] else "zes")+".json","w"),indent=1)
