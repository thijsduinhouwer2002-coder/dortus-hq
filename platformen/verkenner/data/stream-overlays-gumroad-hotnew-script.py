import json,urllib.request,urllib.parse,time,sys
out={}
for q in sys.argv[2:]:
  i=0
  while True:
    u="https://gumroad.com/products/search?"+urllib.parse.urlencode({"query":q,"from":i,"sort":"hot_and_new"})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 dortus-meting"}),timeout=30))
    ps=d["products"]
    for k,p in enumerate(ps): out.setdefault(p["id"],dict(rank=i+k,q=q,name=p["name"],seller=p["seller"]["name"],url=p["url"].split("?")[0],price=p["price_cents"],ratings=p["ratings"]["count"]))
    i+=len(ps)
    if not ps or i>=d["total"]: break
    time.sleep(0.4)
  print(q,d["total"],len(out),file=sys.stderr)
json.dump(out,open(sys.argv[1],"w"))
