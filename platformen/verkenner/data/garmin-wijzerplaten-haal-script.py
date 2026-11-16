# Haalt wijzerplaten uit de open winkel-API van Garmin, nieuwste eerst, tot voorbij de grensdatum.
import json,subprocess,sys,time,gzip,concurrent.futures as cf
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"
GRENS=int(time.mktime((2025,11,1,0,0,0,0,0,0)))*1000
def get(s):
    for t in range(5):
        r=subprocess.run(["curl","-s","--max-time","40",f"{B}?startPageIndex={s}&pageSize=30&sortType=mostRecent&appType=watchface"],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if isinstance(d,list): return s,d
        except Exception: pass
        time.sleep(3+t*3)
    return s,None
def slim(a):
    loc=(a.get('appLocalizations') or [{}])
    en=next((l for l in loc if l.get('locale')=='en'),loc[0] if loc else {})
    p=a.get('pricing') or {}
    return dict(id=a['id'],naam=en.get('name'),beschrijving=en.get('description'),talen=[l.get('locale') for l in loc],
      maker=(a.get('developer') or {}).get('developerDisplayName'),makerId=a.get('developerId'),
      dl=a.get('downloadCount'),rating=a.get('averageRating'),reviews=a.get('reviewCount'),cat=a.get('categoryId'),
      pay=a.get('paymentModel'),prijs=((p.get('listPrice') or {}).get('price')),saleprijs=((p.get('salePrice') or {}).get('price')),
      valuta=((p.get('listPrice') or {}).get('currencyCode')),trial=a.get('hasTrialMode'),
      first=a.get('firstApprovalDate'),last=a.get('lastApprovalDate'),release=a.get('releaseDate'),creation=a.get('creationDate'),
      versie=a.get('latestExternalVersion'),ndev=len(a.get('compatibleDevicePartNumbers') or []),perm=a.get('permissions'),
      video=bool(a.get('videoUrl')),nscreens=len(a.get('screenshotFileIds') or []),extsub=a.get('requiringExternalSubscription'))
if __name__=='__main__':
    out={};fails=[];s=0;oud=0
    with cf.ThreadPoolExecutor(3) as ex:
        while oud<20 and s<60000:
            batch=list(range(s,s+90,30)); s+=90
            for st,d in ex.map(get,batch):
                if d is None: fails.append(st); continue
                for a in d: out[a['id']]=slim(a)
                if d and max((a.get('firstApprovalDate') or 0) for a in d)<GRENS: oud+=1
                else: oud=0
                if not d: oud=99
            time.sleep(1)
            if s%3000==0: print(s,len(out),len(fails),flush=True)
    json.dump(list(out.values()),gzip.open(sys.argv[1],'wt'))
    print("klaar pagina-start",s,"uniek",len(out),"mislukt",fails)
