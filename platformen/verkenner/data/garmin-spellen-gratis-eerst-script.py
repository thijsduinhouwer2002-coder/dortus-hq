# Vera 13 nov 2026: betaalde Garmin-spellen (categorie 206, prijs in 'pricing') met eerste goedkeuring jan t/m 15 aug 2026:
# lees alle reviews en tel klachten die erop wijzen dat het spel eerst gratis was.
# Gebruik: python3 -I garmin-spellen-gratis-eerst-script.py garmin-niet-wijzerplaten-2026-11-09.json.gz
import json,gzip,subprocess,time,re,datetime,sys
d=json.load(gzip.open(sys.argv[1]))
def dt(ms): return datetime.datetime.fromtimestamp(ms/1000,datetime.UTC).date().isoformat() if ms else '0'
P=lambda x:x['pricing']['listPrice']['price'] if x['pricing'] else 0
g=[x for x in d if x['cat']=='206' and P(x)>0 and '2026-01-01'<=dt(x['first'])<='2026-08-15']
pat=re.compile(r'was free|for free|used to be free|now (paid|charg)|have to pay|make us pay|pay for it|no longer free|not free anymore|kostenlos war|war gratis|era gratis|jadi berbayar|it was free|free before',re.I)
for x in sorted(g,key=lambda x:-x['dl']):
    rv=[]
    for off in range(0,600,30):
        r=subprocess.run(['curl','-s','--max-time','30',f"https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/{x['id']}/reviews?startPageIndex={off}&pageSize=30"],capture_output=True,text=True).stdout
        try: j=json.loads(r)
        except Exception: break
        if not j: break
        rv+=j; time.sleep(0.3)
        if len(j)<30: break
    k=[v for v in rv if pat.search(v.get('text') or '')]
    print(json.dumps({'naam':x['naam'],'maker':x['maker'],'dl':x['dl'],'prijs':P(x),'eerst':dt(x['first']),'reviews':len(rv),'gratis_klachten':len(k),'voorbeeld':(k[0]['text'][:120] if k else '')},ensure_ascii=False),flush=True)
