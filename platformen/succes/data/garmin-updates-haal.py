import json,gzip,subprocess,sys,time,concurrent.futures as cf
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/"
ids=[a['id'] for a in json.load(gzip.open(sys.argv[1]))]
def get(i):
    for t in range(4):
        r=subprocess.run(["curl","-s","--max-time","30",B+i],capture_output=True,text=True)
        try:
            a=json.loads(r.stdout)
            if isinstance(a,dict) and a.get('id'):
                return i,dict(dl=a.get('downloadCount'),reviews=a.get('reviewCount'),rating=a.get('averageRating'),
                  last=a.get('lastApprovalDate'),release=a.get('releaseDate'),changed=a.get('changedDate'),versie=a.get('latestExternalVersion'),
                  devs=a.get('compatibleDevicePartNumbers') or [],nieuw=a.get('markedAsNew'),video=bool(a.get('videoUrl')),nscr=len(a.get('screenshotFileIds') or []),
                  pay=a.get('paymentModel'))
            if isinstance(a,dict) and a.get('status')==404: return i,'weg'
        except Exception: pass
        time.sleep(2+2*t)
    return i,None
out={}
with cf.ThreadPoolExecutor(6) as ex:
    for n,(i,v) in enumerate(ex.map(get,ids)):
        out[i]=v
        if n%1000==0: print(n,flush=True)
json.dump(out,gzip.open(sys.argv[2],'wt'))
print('klaar',len(out),sum(v is None for v in out.values()),sum(v=='weg' for v in out.values()))
