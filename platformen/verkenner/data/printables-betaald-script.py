import sys,json,subprocess,time
out=sys.argv[1]; cur=None; n=0; old=0
F="id name price premium firstPublish datePublished created likesCount makesCount ratingCount ratingAvg aiGenerated user { id handle } category { name }"
with open(out,"w") as f:
    while True:
        a='limit: 30, paid: paid, ordering: "-first_publish"'+(', cursor: "%s"'%cur if cur else '')
        q="{ morePrints(%s){ cursor items { %s } } }"%(a,F)
        r=subprocess.run(["curl","-sS","-m","30","-A","Mozilla/5.0","-H","Content-Type: application/json","-d",json.dumps({"query":q}),"https://api.printables.com/graphql/"],capture_output=True,text=True).stdout
        try: d=json.loads(r)["data"]["morePrints"]
        except Exception: print("ERR",r[:200],flush=True); time.sleep(30); continue
        for it in d["items"]:
            f.write(json.dumps(it)+"\n"); n+=1
            if (it.get("firstPublish") or "9")<"2026-03-01": old+=1
        f.flush(); cur=d.get("cursor")
        print(n, d["items"][-1]["firstPublish"] if d["items"] else None, flush=True)
        if not d["items"] or not cur or old>300: break
        time.sleep(2.0)
