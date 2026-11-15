# Vera 15 nov 2026: willekeurige steekproef uit de new-app-sitemaps van apps.apple.com,
# per app gegevens via de open iTunes lookup-API (land us). Gebruik: python3 haal.py ids.txt n uit.json
import sys,gzip,json,random,urllib.request,time
from concurrent.futures import ThreadPoolExecutor
ids=open(sys.argv[1]).read().split(); random.seed(1511); s=random.sample(ids,int(sys.argv[2]))
def look(chunk):
    for t in range(3):
        try:
            u='https://itunes.apple.com/lookup?country=us&id='+','.join(chunk)
            b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'curl/8'}),timeout=40).read()
            b=gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b
            return json.loads(b).get('results',[])
        except Exception as e: time.sleep(5)
    return []
chunks=[s[i:i+100] for i in range(0,len(s),100)]
res=[]
with ThreadPoolExecutor(3) as ex:
    for r in ex.map(look,chunks): res+=r
keep=['trackId','trackName','releaseDate','currentVersionReleaseDate','userRatingCount','averageUserRating','price','primaryGenreName','artistId','artistName','sellerName','kind','formattedPrice']
out=[{k:a.get(k) for k in keep} for a in res if a.get('kind')=='software']
json.dump({'steekproef':len(s),'gevonden_us':len(out),'apps':out},open(sys.argv[3],'w'))
print(len(s),len(out))
