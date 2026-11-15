# Vera 15 nov 2026: alle apps uit de open Salla-API, plus per app de oudste en nieuwste reviewdatum.
# Gebruik: python3 -I script.py uit.json   (rustig, alleen lezen, ±10 minuten)
import json,subprocess,sys,time,math
def get(u):
    for _ in range(3):
        try: return json.loads(subprocess.run(["curl","-s","-m","30",u],capture_output=True,text=True).stdout)
        except Exception: time.sleep(2)
    return {}
apps=[];p=1
while p:
    d=get(f"https://api.salla.dev/marketplace/v2/apps?page={p}")
    apps+=d.get('data',[]); p=(d.get('cursor') or {}).get('next'); time.sleep(0.3)
print('apps',len(apps),flush=True)
for i,a in enumerate(apps):
    n=a['reviews']['count']
    if n:
        last=math.ceil(n/10)
        r=get(f"https://api.salla.dev/marketplace/v2/apps/{a['id']}/reviews?page={last}").get('data',[])
        a['oudste']=min([x['date'] for x in r],default=None)
        r1=get(f"https://api.salla.dev/marketplace/v2/apps/{a['id']}/reviews?page=1").get('data',[])
        a['nieuwste']=max([x['date'] for x in r1],default=None)
        a['revdata1']=[x['date'] for x in r1]
        time.sleep(0.25)
    if i%100==0: print(i,flush=True)
json.dump(apps,open(sys.argv[1],'w'),ensure_ascii=False)
print('klaar')
