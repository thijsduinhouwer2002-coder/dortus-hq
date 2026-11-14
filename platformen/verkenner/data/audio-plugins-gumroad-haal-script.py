import json,urllib.request,urllib.parse,time,sys
out={}
for q in ["vst plugin","vst3","audio plugin","clap plugin","au plugin"]:
  i=0
  while True:
    u="https://gumroad.com/products/search?"+urllib.parse.urlencode({"query":q,"from":i,"sort":"newest"})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 dortus-meting"}),timeout=30))
    ps=d["products"]
    for p in ps: out[p["id"]]=dict(name=p["name"],seller=p["seller"]["name"],url=p["url"].split("?")[0],price=p["price_cents"],pwyw=p["is_pay_what_you_want"],ratings=p["ratings"]["count"],avg=p["ratings"]["average"],rec=p["recurrence"])
    i+=len(ps)
    if not ps or i>=d["total"] or i>=1200: break
    time.sleep(0.4)
  print(q,d["total"],len(out),file=sys.stderr)
json.dump(out,open(sys.argv[1],"w"))
