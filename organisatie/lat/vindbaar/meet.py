"""Afkijker #319: plek per zoekterm op Superhive, Gumroad Discover, Blender Extensions, Printables en YouTube.
Alleen lezen met curl. Gebruik: python3 meet.py > uitslag.json"""
import re,json,subprocess,urllib.parse,sys,time
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
TERMEN=["split model for 3d printing blender","ball joint blender addon","articulated figure blender","action figure blender",
"poseable figure 3d print","split model 3d print","3d print connectors blender","cut model into parts blender",
"blender 3d print addon","print in place joints"]
def curl(u,extra=()):
    return subprocess.run(["curl","-sL","--max-time","30","-A",UA,"-H","Accept-Language: en-US,en",*extra,u],capture_output=True,text=True).stdout
def superhive(t):
    lijst=[]
    for p in (1,2,3,4):
        h=curl("https://superhivemarket.com/search?search%5Bq%5D="+urllib.parse.quote_plus(t)+f"&page={p}")
        ids=[]
        for m in re.findall(r'href="/products/([^"?#]+)\?search_id=',h):
            if m not in ids: ids.append(m)
        if not ids: break
        lijst+=[i for i in ids if i not in lijst]
    return lijst
def gumroad(t):
    lijst=[];van=1;tot=None
    while van<=90:
        try: d=json.loads(curl("https://gumroad.com/products/search?query="+urllib.parse.quote(t)+f"&from={van}",("-H","Accept: application/json")))
        except Exception: break
        tot=d.get("total")
        if not d.get("products"): break
        for p in d["products"]: lijst.append(p["name"][:60]+" | "+p["seller"]["name"]+" | "+p["url"].split("?")[0])
        van+=len(d["products"])
    return lijst,tot
def extensions(t):
    h=curl("https://extensions.blender.org/search/?q="+urllib.parse.quote_plus(t))
    out=[]
    for m in re.findall(r'href="/add-ons/([^/"]+)/"',h):
        if m not in out: out.append(m)
    return out
def printables(t):
    q={"query":"query($q:String!){ searchPrints2(query:$q, limit:30, offset:0){ totalCount items{ id name downloadCount user{ publicUsername } } } }","variables":{"q":t}}
    r=subprocess.run(["curl","-s","--max-time","30","https://api.printables.com/graphql/","-H","Content-Type: application/json","-d",json.dumps(q)],capture_output=True,text=True).stdout
    try: d=json.loads(r)["data"]["searchPrints2"]
    except Exception: return [],None
    return [f'{i["name"][:60]} | {i["user"]["publicUsername"]} | {i["downloadCount"]} dl | printables.com/model/{i["id"]}' for i in d["items"]],d["totalCount"]
def youtube(t):
    h=curl("https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(t))
    m=re.search(r'ytInitialData = (\{.*?\});</script>',h)
    if not m: return []
    out=[]
    def loop(o):
        if isinstance(o,dict):
            if "videoRenderer" in o:
                v=o["videoRenderer"]
                titel="".join(r.get("text","") for r in v.get("title",{}).get("runs",[]))
                kanaal="".join(r.get("text","") for r in v.get("ownerText",{}).get("runs",[]))
                views=v.get("viewCountText",{}).get("simpleText","")
                out.append(f'{titel[:60]} | {kanaal} | {views} | youtu.be/{v.get("videoId")}')
            for x in o.values(): loop(x)
        elif isinstance(o,list):
            for x in o: loop(x)
    loop(json.loads(m.group(1)))
    return out
uit={"gemeten":time.strftime("%Y-%m-%d %H:%M UTC",time.gmtime()),"termen":{}}
for t in TERMEN:
    g,gt=gumroad(t); p,pt=printables(t)
    uit["termen"][t]={"superhive":superhive(t),"gumroad":g,"gumroad_totaal":gt,"extensions":extensions(t),"printables":p,"printables_totaal":pt,"youtube":youtube(t)}
    print(t,{k:len(v) for k,v in uit["termen"][t].items() if isinstance(v,list)},file=sys.stderr)
json.dump(uit,sys.stdout,indent=1,ensure_ascii=False)
