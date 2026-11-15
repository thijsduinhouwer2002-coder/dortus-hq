import json,urllib.request,urllib.parse,time,sys
out={}
for q in sys.argv[2:]:
  i=0
  while True:
    u="https://gumroad.com/products/search?"+urllib.parse.urlencode({"query":q,"from":i,"sort":"newest"})
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 dortus-meting"}),timeout=30))
    except Exception as e: print(q,i,e,file=sys.stderr); break
    ps=d["products"]
    for p in ps:
      o=out.setdefault(p["id"],dict(name=p["name"],seller=p["seller"]["name"],seller_url=p["seller"].get("profile_url"),url=p["url"].split("?")[0],price=p["price_cents"],pwyw=p["is_pay_what_you_want"],ratings=p["ratings"]["count"],avg=p["ratings"]["average"],rec=p["recurrence"],q=[]))
      o["q"].append(q)
    i+=len(ps)
    if not ps or i>=d["total"] or i>=1500: break
    time.sleep(0.4)
  print(q,d.get("total"),len(out),file=sys.stderr)
json.dump(out,open(sys.argv[1],"w"))
