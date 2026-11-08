import json,urllib.request,time,urllib.parse
B="https://api.fortnite.com/ecosystem/v1/islands?size=1000"
out=open("/tmp/claude-0/fn/islands.jsonl","w");cur=None;n=0
while True:
    u=B+("&after="+urllib.parse.quote(cur) if cur else "")
    for t in range(5):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (compatible; DortusVerkenner/1.0)"}),timeout=30));break
        except Exception as e: print("err",e);time.sleep(5)
    for x in d["data"]: out.write(json.dumps(x,ensure_ascii=False)+"\n")
    n+=len(d["data"]); cur=d["meta"]["page"].get("nextCursor")
    if not cur or not d["data"]: break
    time.sleep(0.3)
print("klaar",n)
