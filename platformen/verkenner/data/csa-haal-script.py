# Haalt alle materialen van CLIP STUDIO ASSETS per publicatiemaand via de open zoek-API (/en-us/search/ajax).
# Gebruik: python3 csa-haal-script.py 2026-05 2026-08 uit.jsonl [pay]
import json,sys,time,urllib.request,urllib.parse,calendar
van,tot,uit=sys.argv[1],sys.argv[2],sys.argv[3]
pay=sys.argv[4] if len(sys.argv)>4 else None
def maanden(a,b):
    y,m=map(int,a.split('-'));Y,M=map(int,b.split('-'))
    while (y,m)<=(Y,M):
        yield y,m; m+=1
        if m==13: y,m=y+1,1
def get(params):
    url="https://assets.clip-studio.com/en-us/search/ajax?"+urllib.parse.urlencode(params)
    for t in range(5):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; DortusVerkenner/1.0)"})
            return json.load(urllib.request.urlopen(req,timeout=30))
        except Exception as e:
            print("fout",e,file=sys.stderr); time.sleep(10*(t+1))
    raise SystemExit("opgegeven")
f=open(uit,'a')
for y,m in maanden(van,tot):
    last=calendar.monthrange(y,m)[1]
    base={"order":"new","published_from":f"{y}-{m:02d}-01T00:00:00.000Z","published_to":f"{y}-{m:02d}-{last}T23:59:59.999Z"}
    if pay: base["pay"]=pay
    cur=None;n=0
    while True:
        p=dict(base)
        if cur: p["cursor"]=cur
        d=get(p)["response_data"]
        for x in d["data"]:
            x["_maand"]=f"{y}-{m:02d}"; f.write(json.dumps(x,ensure_ascii=False)+"\n"); n+=1
        print(y,m,"found",d["found"],"n",n,"exceeded",d["hasExceeded"],file=sys.stderr,flush=True)
        cur=d.get("cursor")
        if not d["data"] or not cur: break
        time.sleep(1.0)
    f.flush()
