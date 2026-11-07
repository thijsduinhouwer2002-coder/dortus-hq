# Haalt BOOTH-items op via de open JSON per item. Gebruik: python3 booth-haal-script.py UIT.jsonl ID1 ID2 ... of --range A B STAP of --random A B N SEED
import json,sys,time,subprocess,random
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 DortusVerkenner"
def get(i):
    r=subprocess.run(["curl","-sL","-m","30","-A",UA,f"https://booth.pm/ja/items/{i}.json"],capture_output=True)
    try: d=json.loads(r.stdout)
    except Exception: return {'id':i,'ok':False}
    c=d.get('category') or {}
    v=d.get('variations') or []
    return {'id':i,'ok':True,'published':d.get('published_at'),'price':d.get('price'),
      'cat':c.get('name'),'parent':(c.get('parent') or {}).get('name'),'likes':d.get('wish_lists_count'),
      'shop':(d.get('shop') or {}).get('subdomain'),'name':(d.get('name') or '')[:90],
      'digital':any(x.get('type')=='digital' for x in v),'prices':[x.get('price') for x in v],
      'tags':[t['name'] for t in d.get('tags') or []][:15]}
out=sys.argv[1]; a=sys.argv[2:]
if a[0]=='--range': ids=range(int(a[1]),int(a[2]),int(a[3]))
elif a[0]=='--random': random.seed(int(a[4])); ids=sorted(random.sample(range(int(a[1]),int(a[2])),int(a[3])))
else: ids=[int(x) for x in a]
with ThreadPoolExecutor(4) as ex, open(out,'a') as f:
    for d in ex.map(get,ids): f.write(json.dumps(d,ensure_ascii=False)+"\n"); f.flush()
