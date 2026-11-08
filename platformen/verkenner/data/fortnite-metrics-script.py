import json,urllib.request,time,random,sys
from concurrent.futures import ThreadPoolExecutor
isl=[json.loads(l) for l in open(sys.argv[1])]
random.seed(20261108); idx=sorted(random.sample(range(len(isl)),int(sys.argv[2])))
U="https://api.fortnite.com/ecosystem/v1/islands/%s/metrics/day?from=2026-11-01T00:00:00.000Z&to=2026-11-08T00:00:00.000Z"
def get(i):
    x=isl[i]
    for t in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(U%x["code"],headers={"User-Agent":"Mozilla/5.0 (compatible; DortusVerkenner/1.0)"}),timeout=30))
            return dict(pos=i,**x,m=d)
        except urllib.error.HTTPError as e:
            if e.code==404: return dict(pos=i,**x,m=None,err=404)
            time.sleep(3*(t+1))
        except Exception: time.sleep(3*(t+1))
    return dict(pos=i,**x,m=None,err="fail")
with open(sys.argv[3],"w") as f, ThreadPoolExecutor(4) as ex:
    for r in ex.map(get,idx): f.write(json.dumps(r,ensure_ascii=False)+"\n")
print("klaar")
