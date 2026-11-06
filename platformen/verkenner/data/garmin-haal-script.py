import json,subprocess,sys,concurrent.futures as cf
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"
sort=sys.argv[2]; N=int(sys.argv[3])
keep=['id','developerId','typeId','downloadCount','averageRating','reviewCount','categoryId','paymentModel','pricing','hasTrialMode','requiringExternalSubscription','firstApprovalDate','releaseDate','creationDate','developer','trending','appLocalizations']
def get(s):
    for t in range(4):
        r=subprocess.run(["curl","-s","--max-time","40",f"{B}?startPageIndex={s}&pageSize=30&sortType={sort}"],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if isinstance(d,list): break
        except Exception: pass
    else: return s,None
    out=[]
    for a in d:
        b={k:a.get(k) for k in keep}
        b['naam']=(a.get('appLocalizations') or [{}])[0].get('name'); b.pop('appLocalizations')
        dv=a.get('developer') or {}; b['developer']=dv.get('developerDisplayName')
        out.append(b)
    return s,out
res={}
with cf.ThreadPoolExecutor(int(sys.argv[4])) as ex:
    for s,o in ex.map(get,range(0,N,30)):
        res[s]=o
fails=[s for s,o in res.items() if o is None]
allx=[a for s in sorted(res) for a in (res[s] or [])]
json.dump(allx,open(sys.argv[1],'w'))
print("rijen",len(allx),"uniek",len({a['id'] for a in allx}),"mislukt",len(fails))
