import json,subprocess,time,concurrent.futures as cf
sel=json.load(open('sel.json'))
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/"
def get(s):
    grens=s['R']-60*86400000; rv=[]
    for off in range(0,900,30):
        j=None
        for t in range(3):
            r=subprocess.run(['curl','-s','--max-time','30',f"{B}{s['id']}/reviews?startPageIndex={off}&pageSize=30"],capture_output=True,text=True).stdout
            try: j=json.loads(r); break
            except Exception: time.sleep(2)
        if not isinstance(j,list) or not j: break
        rv+=[(v.get('date'),v.get('rating'),(v.get('text') or '')[:300]) for v in j]
        if len(j)<30 or min(v.get('date') or 0 for v in j)<grens: break
    s=dict(s); s['reviews']=rv; return s
out=[]
with cf.ThreadPoolExecutor(6) as ex:
    for n,s in enumerate(ex.map(get,sel)):
        out.append(s)
        if n%200==0: print(n,flush=True)
json.dump(out,open('rev.json','w')); print('klaar',len(out))
