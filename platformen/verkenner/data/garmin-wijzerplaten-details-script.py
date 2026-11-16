# Haalt details per id op voor betaalde wijzerplaten die de lijst MOST_RECENT niet gaf (ids uit de dataset van 6 nov).
import json,gzip,subprocess,time,sys,concurrent.futures as cf
sys.path.insert(0,'.')
from haal import slim  # noqa (haal.py draait niet opnieuw: guard hieronder)
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/"
def get(i):
    for t in range(4):
        r=subprocess.run(["curl","-s","--max-time","30",B+i],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if isinstance(d,dict) and d.get('id'): time.sleep(0.5); return i,slim(d)
            if isinstance(d,dict) and 'className' in d: return i,'weg'
        except Exception: pass
        time.sleep(3+3*t)
    return i,None
ids=json.load(open('mist.json')); out=[];weg=0;fout=0
with cf.ThreadPoolExecutor(4) as ex:
    for n,(i,d) in enumerate(ex.map(get,ids)):
        if d=='weg': weg+=1
        elif d is None: fout+=1
        else: out.append(d)
        if n%500==0: print(n,len(out),weg,fout,flush=True)
json.dump(out,gzip.open('details.json.gz','wt'))
print("klaar",len(out),"weg",weg,"fout",fout)
