import re,subprocess,json,time,html,sys
from concurrent.futures import ThreadPoolExecutor
A="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
urls=sorted({json.loads(l)['app-url'] for f in sys.argv[1:-1] for l in open(f)})
def get(u):
    time.sleep(0.4)
    h=subprocess.run(['curl','-s','-m','30','-A',A,'https://developers.reddit.com'+u],capture_output=True,text=True).stdout
    h=html.unescape(h)
    r={'url':u}
    m=re.search(r'installCount="(\d+)"',h); r['installs']=int(m.group(1)) if m else None
    m=re.search(r'"createdAt":"([^"]+)","owner":\{"id":"[^"]+","displayName":"([^"]+)"',h)
    if m: r['created'],r['owner']=m.group(1),m.group(2)
    up=re.findall(r'"uploadedAt":"([^"]+)"',h); r['laatste_upload']=max(up) if up else None
    r["cat"]=re.findall(r"\{\"id\":\d+,\"name\":\"([A-Z_]+)\"",h[h.find("categoriesV2"):h.find("categoriesV2")+600]) if "categoriesV2" in h else []
    r['payments']=('"payments"' in h) or ('products.json' in h)
    return r
with open(sys.argv[-1],'w') as out, ThreadPoolExecutor(3) as ex:
    for r in ex.map(get,urls): out.write(json.dumps(r)+'\n')
