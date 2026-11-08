# Vera 8 nov 2026: echte leeftijd per plugin = datum van de oudste versie (/updates, pagina's van 100).
import json,sys,subprocess,concurrent.futures as cf
src,out=sys.argv[1],sys.argv[2]
ids=[json.loads(l)['id'] for l in open(src)]
def get(i):
    oud=None;n=0
    for p in range(1,30):
        t=subprocess.run(['curl','-s','--max-time','20',f'https://plugins.jetbrains.com/api/plugins/{i}/updates?page={p}&size=100'],capture_output=True,text=True).stdout
        try: d=json.loads(t)
        except Exception: return {'id':i,'fout':1}
        for u in d:
            c=int(u['cdate']); n+=1
            oud=c if oud is None else min(oud,c)
        if len(d)<100: break
    return {'id':i,'eerste':oud,'versies':n}
with cf.ThreadPoolExecutor(5) as ex, open(out,'w') as f:
    for r in ex.map(get,ids): f.write(json.dumps(r)+'\n')
