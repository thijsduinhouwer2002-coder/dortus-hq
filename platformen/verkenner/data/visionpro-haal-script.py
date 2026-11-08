# Vera 8 nov 2026: steekproef nieuwe apps uit de new-app-sitemaps van apps.apple.com,
# daarna iTunes lookup (200 ids per keer) om visionOS-only apps te vinden.
# Gebruik: python3 visionpro-haal-script.py <aantal_sitemapbestanden> <uit.json>
import sys, re, gzip, json, time, random, urllib.request
N=int(sys.argv[1]); out=sys.argv[2]
UA={'User-Agent':'Mozilla/5.0'}
def get(u):
    for t in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
        except Exception as e:
            time.sleep(10*(t+1))
    return b''
idx=get('https://apps.apple.com/sitemaps_apps_index_new-app_1.xml').decode()
files=sorted(set(re.findall(r'https://apps.apple.com/sitemaps_apps_new-app_\d+_\d+\.xml\.gz',idx)))
random.seed(8); files=random.sample(files,min(N,len(files)))
ids=set()
for f in files:
    x=get(f)
    try: x=gzip.decompress(x)
    except Exception: pass
    ids|=set(re.findall(r'<loc>[^<]*/id(\d+)',x.decode('utf8','ignore')))
    time.sleep(1)
ids=sorted(ids); print('sitemaps',len(files),'ids',len(ids),file=sys.stderr)
res={}
for i in range(0,len(ids),150):
    chunk=ids[i:i+150]
    d=get('https://itunes.apple.com/lookup?country=us&id='+','.join(chunk))
    try: rs=json.loads(d)['results']
    except Exception: rs=[]
    for r in rs:
        sd=r.get('supportedDevices',[])
        res[str(r['trackId'])]={'naam':r.get('trackName'),'maker':r.get('artistName'),'prijs':r.get('price'),
          'release':r.get('releaseDate','')[:10],'genre':r.get('primaryGenreName'),'ratings':r.get('userRatingCount'),
          'vision':any('Vision' in s for s in sd),'iphone':any(s.startswith('iPhone') for s in sd),
          'ipad':any(s.startswith('iPad') for s in sd),'kind':r.get('kind')}
    time.sleep(1.5)
    if i%3000==0: print(i,len(res),file=sys.stderr)
json.dump({'sitemaps':files,'aantal_ids':len(ids),'apps':res},open(out,'w'))
