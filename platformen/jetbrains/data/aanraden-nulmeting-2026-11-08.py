import csv,json,time,urllib.request,urllib.parse,sys,datetime
src,out=sys.argv[1],sys.argv[2]
soorten=[r['soort'] for r in csv.DictReader(open(src),delimiter='\t')]
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=20))
        except Exception as e: time.sleep(2)
    return None
cache={}
w=open(out,'w'); w.write("tijd_utc\tsoort\txmlId\tid\tnaam\tdownloads\tbundled\n")
for s in soorten:
    lst=get("https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName="+urllib.parse.quote(s)) or []
    for p in lst:
        x=p['pluginId']
        if x not in cache:
            d=get("https://plugins.jetbrains.com/api/plugins/intellij/"+urllib.parse.quote(x)) or {}
            cache[x]=(d.get('id',''),d.get('name',p.get('pluginName','')),d.get('downloads',''))
            time.sleep(0.15)
        i,n,dl=cache[x]
        w.write(f"{datetime.datetime.utcnow():%Y-%m-%d %H:%M}\t{s}\t{x}\t{i}\t{n}\t{dl}\t{p.get('bundled')}\n")
    time.sleep(0.1)
w.close(); print(len(soorten),len(cache))
