import json,subprocess,sys,concurrent.futures as cf
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"
sort=sys.argv[2]; N=int(sys.argv[3])
def get(s):
    for t in range(4):
        r=subprocess.run(["curl","-s","--max-time","40",f"{B}?startPageIndex={s}&pageSize=30&sortType={sys.argv[5]}&appType={sort}"],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if isinstance(d,list): break
        except Exception: pass
    else: return s,None
    out=[]
    for a in d:
        dv=a.get('developer') or {}
        out.append(dict(id=a['id'],naam=(a.get('appLocalizations') or [{}])[0].get('name'),maker=dv.get('developerDisplayName'),makerId=a.get('developerId'),
          type=a.get('typeId'),cat=a.get('categoryId'),dl=a.get('downloadCount'),rating=a.get('averageRating'),reviews=a.get('reviewCount'),
          pay=a.get('paymentModel'),pricing=a.get('pricing'),trial=a.get('hasTrialMode'),extsub=a.get('requiringExternalSubscription'),
          first=a.get('firstApprovalDate'),last=a.get('lastApprovalDate'),release=a.get('releaseDate'),changed=a.get('changedDate'),
          versie=a.get('latestExternalVersion'),automig=a.get('latestVersionAutoMigrated'),devs=a.get('compatibleDeviceTypeIds') or [],
          web=a.get('websiteUrl'),beta=a.get('betaApp')))
    return s,out
res={}
with cf.ThreadPoolExecutor(int(sys.argv[4])) as ex:
    for s,o in ex.map(get,range(0,N,30)): res[s]=o
allx=[a for s in sorted(res) for a in (res[s] or [])]
json.dump(allx,open(sys.argv[1],'w'))
print("rijen",len(allx),"uniek",len({a['id'] for a in allx}),"mislukt",sum(o is None for o in res.values()))
