import json,subprocess,sys,datetime,re
def get(u):
    return json.loads(subprocess.run(["curl","-sL","https://plugins.jetbrains.com"+u],capture_output=True,text=True).stdout)
def d(ms): return datetime.datetime.utcfromtimestamp(int(ms)/1000).date()
ids=[int(x) for x in sys.argv[1:]]
now=datetime.date(2026,11,6)
for pid in ids:
    p=get(f"/api/plugins/{pid}")
    ups=[]
    page=1
    while True:
        u=get(f"/api/plugins/{pid}/updates?page={page}&size=100")
        if not u: break
        ups+=u; page+=1
        if len(u)<100: break
    ups.sort(key=lambda x:int(x['cdate']))
    first=d(ups[0]['cdate']) if ups else None
    tot=sum(x['downloads'] for x in ups)
    last=ups[-1] if ups else None
    # downloads of versions released in last 90 days
    r90=sum(x['downloads'] for x in ups if (now-d(x['cdate'])).days<=90)
    # top version
    top=max(ups,key=lambda x:x['downloads']) if ups else None
    rat=get(f"/api/plugins/{pid}/rating")
    com=get(f"/api/plugins/{pid}/comments")
    pr=get(f"/api/marketplace/plugin/{pid}/prices?countryCode=US")
    try:
        pi=pr['pluginInfo']; price=f"pers {pi['personal']['annual']['firstYear']['price']} / comm {pi['commercial']['annual']['firstYear']['price']} {pr['currency']['iso']}"
    except Exception: price=str(pr)[:80]
    months=max(1,(now-first).days/30.4) if first else 1
    trial=(p.get('purchaseInfo') or {}).get('trialPeriod')
    print(f"{pid}\t{p['name']}\t{p.get('pricingModel')}\t{p['downloads']}\t{len(ups)}\t{first}\t{round(p['downloads']/months)}\t{last['version'] if last else ''}:{last['downloads'] if last else ''}\t{top['version']}:{top['downloads']}\t{r90}\t{len(com)}\t{rat.get('meanRating')}\t{rat.get('votes')}\t{trial}\t{price}")
