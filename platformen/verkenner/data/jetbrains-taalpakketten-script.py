import json,subprocess,sys,datetime
def get(u):
    o=subprocess.run(["curl","-sL","https://plugins.jetbrains.com"+u],capture_output=True,text=True).stdout
    try: return json.loads(o)
    except: return {}
def d(ms): return datetime.datetime.utcfromtimestamp(int(ms)/1000).date()
now=datetime.date(2026,11,8)
out=[]
for pid in sys.argv[1:]:
    p=get(f"/api/plugins/{pid}")
    ups=get(f"/api/plugins/{pid}/updates?page=1&size=100") or []
    ups.sort(key=lambda x:int(x['cdate']))
    first=d(ups[0]['cdate']) if ups else None
    r90=sum(x['downloads'] for x in ups if (now-d(x['cdate'])).days<=90)
    r365=sum(x['downloads'] for x in ups if (now-d(x['cdate'])).days<=365)
    rat=get(f"/api/plugins/{pid}/rating")
    votes=rat.get('votes') or {}
    n=sum(votes.values()); avg=round(sum(int(k)*v for k,v in votes.items())/n,2) if n else None
    com=get(f"/api/plugins/{pid}/comments") or []
    pr=get(f"/api/marketplace/plugin/{pid}/prices?countryCode=US")
    try:
        pi=pr['pluginInfo']; price=f"{pi['personal']['annual']['firstYear']['price']}/{pi['commercial']['annual']['firstYear']['price']}"
    except Exception: price='-'
    v=p.get('vendor'); v=v.get('name') if isinstance(v,dict) else v
    rec=dict(id=pid,naam=p.get('name'),maker=v,model=p.get('pricingModel'),dl=p.get('downloads'),eerste=str(first),versies=len(ups),laatste=str(d(ups[-1]['cdate'])) if ups else '',dl90=r90,dl365=r365,stemmen=n,gem=avg,votes=votes,prijs=price,comments=[dict(r=c.get('rating'),dt=str(d(c['cdate'])),t=c.get('comment','')[:400]) for c in com])
    out.append(rec)
    print(pid,rec['naam'][:40],v,rec['model'],rec['dl'],rec['eerste'],rec['laatste'],r90,r365,n,avg,price,len(com),sep='|',flush=True)
json.dump(out,open('taal-detail.json','w'),ensure_ascii=False,indent=1)
