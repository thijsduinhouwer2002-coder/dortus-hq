# Haalt alle reviews (met datum, sterren, geverifieerde download) van apps met 1+ rating.
# Let op: limit mag maximaal 50. Gebruik: python3 -I autodesk-comments-script.py ratings.json uit.jsonl
import sys, json, time, subprocess
from concurrent.futures import ThreadPoolExecutor
R=json.load(open(sys.argv[1]))
ids=[k for k,v in R.items() if v.get('totalRatings',0)>0]
def haal(i):
    uit=[]; off=0
    while True:
        u=f'https://developer.api.autodesk.com/ngappapi/public/apps/{i}/comments?limit=50&offset={off}'
        d=None
        for p in range(3):
            r=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0',u],capture_output=True,text=True)
            try:
                d=json.loads(r.stdout)
                if 'results' in d: break
                d=None
            except Exception: pass
            time.sleep(3)
        if not d: uit.append({'appId':i,'fout':True}); break
        for c in d['results']:
            c.pop('content',None); fr=c.pop('firstReply',None); c['reply']=bool(fr); uit.append(c)
        tot=d.get('pagination',{}).get('totalResults',0); off+=50
        time.sleep(0.3)
        if off>=tot: break
    return uit
with open(sys.argv[2],'w') as f, ThreadPoolExecutor(4) as ex:
    for n,res in enumerate(ex.map(haal,ids)):
        for c in res: f.write(json.dumps(c)+'\n')
        if n%300==0: print(n,len(ids),flush=True)
