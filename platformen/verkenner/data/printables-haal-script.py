import sys,json,subprocess,random,time,concurrent.futures as cf
lo,hi,n,out,seed=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5])
random.seed(seed); ids=random.sample(range(lo,hi),n)
Q='{ print(id: "%d") { id name datePublished firstPublish created downloadCount likesCount makesCount ratingCount price premium aiGenerated user { id handle } category { name } } }'
def get(i):
    time.sleep(1.5)
    r=subprocess.run(["curl","-sS","-m","25","-A","Mozilla/5.0","-H","Content-Type: application/json","-d",json.dumps({"query":Q%i}),"https://api.printables.com/graphql/"],capture_output=True,text=True).stdout
    try: d=json.loads(r)["data"]["print"]
    except Exception: return {"id":i,"err":r[:80]}
    if not d: return {"id":i,"none":True}
    return {"id":i,"t":d["firstPublish"],"tlast":d["datePublished"],"created":d["created"],"title":d["name"],"dl":d["downloadCount"],"like":d["likesCount"],"makes":d["makesCount"],"ratings":d["ratingCount"],
            "price":d["price"],"premium":d["premium"],"ai":d["aiGenerated"],"uid":(d.get("user") or {}).get("id"),"handle":(d.get("user") or {}).get("handle"),"cat":(d.get("category") or {}).get("name")}
with open(out,"w") as f, cf.ThreadPoolExecutor(1) as ex:
    for res in ex.map(get,ids): f.write(json.dumps(res)+"\n"); f.flush()
