# Google Play: details van app-id's ophalen met google-play-scraper (VS, Engels). Gebruik: python3 -I haal.py ids.json uit.jsonl
import json,sys,concurrent.futures as cf,time
from google_play_scraper import app
ids=json.load(open(sys.argv[1])); out=sys.argv[2]
done=set()
try:
    for l in open(out): done.add(json.loads(l)['appId'])
except FileNotFoundError: pass
K=['appId','title','minInstalls','realInstalls','released','price','free','offersIAP','containsAds','genreId','developer','developerId','developerEmail','ratings','reviews','score','updated','currency','contentRating']
def f(i):
    for t in range(3):
        try:
            d=app(i,lang='en',country='us'); return {k:d.get(k) for k in K}
        except Exception as e:
            if 'NotFound' in type(e).__name__ or 'not found' in str(e).lower(): return {'appId':i,'err':'404'}
            time.sleep(2)
    return {'appId':i,'err':'fail'}
todo=[i for i in ids if i not in done]
with open(out,'a') as w, cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(f,todo): w.write(json.dumps(r)+'\n'); w.flush()
