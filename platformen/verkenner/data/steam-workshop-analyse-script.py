import sys,json,collections,datetime
for f in sys.argv[1:]:
    rows=[json.loads(l) for l in open(f)]
    rows=[r for r in rows if r["result"]==1 and r.get("time_created")]
    apps=collections.Counter(r["consumer_app_id"] for r in rows)
    yr=lambda r: datetime.datetime.utcfromtimestamp(r["time_created"]).year
    first={}
    for r in sorted(rows,key=lambda r:r["time_created"]):
        first.setdefault(r["creator"],yr(r))
    by=collections.Counter(yr(r) for r in rows)
    print(f,len(rows),dict(apps))
    for y in range(2019,2027):
        rs=[r for r in rows if yr(r)==y]
        cr=set(r["creator"] for r in rs)
        newc=[c for c in cr if first[c]==y]
        print(" ",y,"items",len(rs),"makers",len(cr),"nieuw (eerste geaccepteerde)",len(newc))
