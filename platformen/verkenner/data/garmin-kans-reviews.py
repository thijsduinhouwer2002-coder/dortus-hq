import json,subprocess,sys,datetime as D
A={a['naam']:a for a in json.load(open('alles.json'))}
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"
for n in sys.argv[1:]:
    a=A[n]; out=[]
    for s in range(0,90,30):
        r=subprocess.run(['curl','-s','--max-time','30',f"{B}/{a['id']}/reviews?startPageIndex={s}&pageSize=30"],capture_output=True,text=True).stdout
        try: d=json.loads(r)
        except Exception: break
        if not d: break
        out+=d
    if out: ks=[k for k in out[0] if 'date' in k.lower() or 'time' in k.lower() or 'version' in k.lower()]
    print('==',n,'|',a['maker'],a['dl'],a['rating'],a['reviews'],'B' if a['betaald'] else 'G','gelezen',len(out),ks)
    out.sort(key=lambda x:-(x.get(ks[0]) or 0) if ks else 0)
    for x in out[:int(12)]:
        t=x.get(ks[0]) if ks else None
        if isinstance(t,(int,float)): t=str(D.datetime.utcfromtimestamp(t/1000).date())
        print('  ',x['rating'],t,(x.get('text') or '')[:200].replace('\n',' '))
