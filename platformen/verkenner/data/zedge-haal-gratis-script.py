import random,re,json,time,sys,subprocess,concurrent.futures as cf
random.seed(1114)
UA="Mozilla/5.0 (compatible; dortus-onderzoek)"
def get(u):
    r=subprocess.run(["curl","-sL","-m","30","-A",UA,u],capture_output=True)
    return r.stdout.decode("utf8","replace")
shards=["%03X"%i for i in range(4096)]
pick=random.sample(shards,50)
urls=[]
for s in pick:
    x=get("https://www.zedge.net/sitemap2/item/wallpaper/"+s)
    urls+=re.findall(r"<loc>([^<]+)</loc>",x); time.sleep(0.3)
print("urls",len(urls),flush=True)
random.shuffle(urls)
N=int(sys.argv[1])
urls=urls[:N]
out=open("/tmp/zd/items.jsonl","a")
def one(u):
    h=get(u); time.sleep(0.4)
    i=h.find('"initialData":{')
    if i<0:
        i=h.find('\\"initialData\\":{')
    seg=h[i:i+6000].replace('\\"','"')
    def f(k,pat=r'([^,}]*)'):
        m=re.search('"'+k+'":'+pat,seg); return m.group(1) if m else None
    return dict(url=u,title=f("title",r'"([^"]*)"'),licensed=f("licensed"),cat=f("category",r'"([^"]*)"'),
        up=f("dateUploaded"),dl=f("downloadCount"),pay=f("type",r'"([^"]*)"'),
        pm=(re.search(r'"paymentMethod":(\{[^}]*\})',seg) or [None,None])[1],
        prof=(re.search(r'"profile":\{"id":"([^"]*)","name":"([^"]*)"',seg).groups() if re.search(r'"profile":\{"id":"([^"]*)","name":"([^"]*)"',seg) else None),
        ai=("aiGenerated" in seg or "AI_GENERATED" in seg), ok=i>=0)
with cf.ThreadPoolExecutor(3) as ex:
    for k,r in enumerate(ex.map(one,urls)):
        out.write(json.dumps(r)+"\n"); out.flush()
        if k%200==0: print(k,flush=True)
