import random,re,json,time,subprocess,concurrent.futures as cf
random.seed(7)
UA="Mozilla/5.0 (compatible; dortus-onderzoek)"
def get(u):
    return subprocess.run(["curl","-sL","-m","30","-A",UA,u],capture_output=True).stdout.decode("utf8","replace")
idx=get("https://www.zedge.net/api/seo/sitemap/wallpapers")
subs=re.findall(r"<loc>([^<]+)</loc>",idx)
kws=[]
for s in random.sample(subs,min(6,len(subs))):
    kws+=re.findall(r"<loc>([^<]+)</loc>",get(s.replace("&amp;","&"))); time.sleep(0.5)
print("kw",len(kws),flush=True)
kws=random.sample(kws,160)
ids={}
for k in kws:
    h=get(k).replace('\\"','"'); time.sleep(0.5)
    for m in re.finditer(r'\{"id":"([0-9a-f-]{36})","licensed":(true|false),"title":"[^"]*","type":"WALLPAPER","origin":[^,]*,"paymentMethod":\{"type":"(\w+)","price":([^}]*)\}',h):
        if m.group(2)=="true": ids[m.group(1)]=(m.group(3),m.group(4),k)
print("licensed ids",len(ids),flush=True)
json.dump(ids,open("/tmp/zd/lic_ids.json","w"))
out=open("/tmp/zd/lic_items.jsonl","w")
def one(i):
    h=get("https://www.zedge.net/wallpaper/"+i).replace('\\"','"'); time.sleep(0.5)
    j=h.find('"initialData":{"id":"'+i)
    seg=h[j:j+5000]
    g=lambda p:(re.search(p,seg) or [None,None])[1]
    return dict(id=i,up=g(r'"dateUploaded":(\d+)'),dl=g(r'"downloadCount":(\d+)'),pay=g(r'"paymentMethod":\{"type":"(\w+)"'),price=g(r'"price":([^}]*)\}'),prof=g(r'"profile":\{"id":"[^"]*","name":"([^"]*)"'),cat=g(r'"category":"([^"]*)"'),kw=ids[i][2])
with cf.ThreadPoolExecutor(2) as ex:
    for r in ex.map(one,list(ids)):
        out.write(json.dumps(r)+"\n"); out.flush()
print("klaar",flush=True)
