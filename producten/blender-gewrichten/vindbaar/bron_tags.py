"""Bron voor de tags en categorie van de top 3 (Bram, issue #161). Leest met curl:
Superhive productpagina (tags uit /tags/..., hoofdcategorie uit 'in <a href="/categories/...">')
en Gumroad zoek-JSON (tags en taxonomy van het product). Schrijft bron-tags-<datum>.json."""
import re,json,subprocess,urllib.parse,datetime
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def get(u,json_=False):
    a=["curl","-sL","-A",UA]+(["-H","Accept: application/json"] if json_ else [])+[u]
    return subprocess.run(a,capture_output=True,text=True).stdout
sh=["click-joints-pro","cleave","catpin","split-3dprint","nb-figure-joints"]
gr={"click-joints-pro":"click joints pro","cleave":"cleave","catpin":"catpin"}
uit={"datum":datetime.datetime.now().isoformat(timespec="minutes"),"superhive":{},"gumroad":{}}
for s in sh:
    u="https://superhivemarket.com/products/"+s
    h=get(u)
    tags=[]
    for t in re.findall(r'href="/tags/([^"]+)"',h):
        if t not in tags: tags.append(t)
    cat=re.findall(r'in <a href="/categories/([^"]+)">',h)
    uit["superhive"][s]={"url":u,"tags":tags,"hoofdcategorie":cat}
for slug,q in gr.items():
    # Met taxonomy-filter blijft alleen het product zelf over; tags_data zijn dan zijn tags (max 9 zichtbaar).
    for tax in ["3d/3d-assets/blender",""]:
        u="https://gumroad.com/products/search?query="+urllib.parse.quote(q)+("&taxonomy="+tax if tax else "")
        try: d=json.loads(get(u,True))
        except Exception: d={"products":[],"total":None,"tags_data":[]}
        uit["gumroad"][slug+(" in "+tax if tax else " zonder filter")]={"zoek_url":u,"totaal":d.get("total"),
            "producten":[p["name"][:60]+" | "+p["url"].split("?")[0] for p in d.get("products",[])][:5],
            "tags_data":[t["key"] for t in d.get("tags_data",[])]}
naam="bron-tags-"+uit["datum"][:10]+".json"
json.dump(uit,open(naam,"w"),indent=1,ensure_ascii=False)
for k,v in uit["superhive"].items(): print("SH",k,v["hoofdcategorie"],len(v["tags"]),v["tags"])
for k,v in uit["gumroad"].items(): print("GR",k,v["totaal"],v["producten"][:2],v["tags_data"] if v["totaal"]==1 else "")
