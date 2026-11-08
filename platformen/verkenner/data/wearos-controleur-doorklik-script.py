import json,re,urllib.request,concurrent.futures as cf,datetime,random
random.seed(1)
r=[json.loads(l) for l in open('/home/claude/dortus-hq/platformen/verkenner/data/wearos-wijzerplaten-2026-11-08.jsonl')]
known={a['appId'] for a in r}
def get(i):
    try:
        req=urllib.request.Request("https://play.google.com/store/apps/details?id=%s&hl=en&gl=US"%i,headers={'User-Agent':'Mozilla/5.0'})
        h=urllib.request.urlopen(req,timeout=30).read().decode('utf8','ignore')
        return i,set(re.findall(r'details\?id=([A-Za-z0-9._]+)',h))-{i}
    except Exception: return i,set()
seeds=[a['appId'] for a in r if a.get('released') and a['released'].endswith('2026') and (a['realInstalls'] or 0)<100]
random.shuffle(seeds); seeds=seeds[:150]
seen=set(seeds); found=set()
front=seeds
for hop in range(2):
    nxt=set()
    with cf.ThreadPoolExecutor(4) as ex:
        for i,s in ex.map(get,front): nxt|=s
    new=nxt-seen; seen|=new; found|=(new-known)
    print('hop',hop,len(front),'links',len(nxt),'nieuw onbekend',len(new-known),flush=True)
    front=sorted(new-known)[:250]
json.dump(sorted(found),open('ids2.json','w'))
