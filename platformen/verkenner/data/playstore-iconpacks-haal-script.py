# Icon packs: zaad2.py (40 zoekopdrachten), daarna details.py en devs.py uit wearos-haal-script.py, daarna iklik.py (doorklikken vanaf kleine apps)
import re,subprocess,json,urllib.parse,time,sys
def get(u): return subprocess.run(["curl","-sL","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
ids=set()
qs=["icon pack","icon pack nova launcher","minimal icon pack","line icon pack","glyph icon pack","pastel icon pack","dark icon pack","white icon pack","black icon pack","neon icon pack","3d icon pack","flat icon pack","material you icon pack","outline icon pack","colorful icon pack","gradient icon pack","round icon pack","squircle icon pack","cute icon pack","retro icon pack","pixel icon pack","glass icon pack","gold icon pack","aesthetic icon pack","kawaii icon pack","hand drawn icon pack","sketch icon pack","duotone icon pack","monochrome icon pack","themed icons pack","new icon pack 2026","icon pack lawnchair","icon pack premium","adaptive icon pack","rounded icon pack","vintage icon pack","paper icon pack","candy icon pack","nature icon pack","futuristic icon pack"]
for q in qs:
    h=get("https://play.google.com/store/search?q="+urllib.parse.quote(q)+"&c=apps&hl=en&gl=US")
    ids|=set(re.findall(r'details\?id=([A-Za-z0-9._]+)',h)); time.sleep(0.3)
print(len(ids),file=sys.stderr); json.dump(sorted(ids),open(sys.argv[1],'w'))
import json,re,urllib.request,concurrent.futures as cf,datetime,random
random.seed(1)
r=[json.loads(l) for l in open('idet.jsonl')]
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
json.dump(sorted(found),open('iklik.json','w'))
