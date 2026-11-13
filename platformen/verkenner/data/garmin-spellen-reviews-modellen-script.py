# Vera 13 nov 2026: lees de reviews van alle Garmin-spellen (categorie 206) met 1.000+ downloads en tel welke horlogemodellen
# reviewers noemen (de review-API geeft geen toestel mee, dus dit is een benadering).
# Gebruik: python3 -I garmin-spellen-reviews-modellen-script.py garmin-niet-wijzerplaten-2026-11-09.json.gz uit.jsonl
import json,gzip,subprocess,time,sys
d=json.load(gzip.open(sys.argv[1]))
g=[x for x in d if x['cat']=='206' and x['dl']>=1000]
with open(sys.argv[2],'w') as f:
  for x in g:
    rv=[]
    for off in range(0,900,30):
      r=subprocess.run(['curl','-s','--max-time','30',f"https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/{x['id']}/reviews?startPageIndex={off}&pageSize=30"],capture_output=True,text=True).stdout
      try: j=json.loads(r)
      except Exception: break
      if not j: break
      rv+=j; time.sleep(0.25)
      if len(j)<30: break
    f.write(json.dumps({'id':x['id'],'naam':x['naam'],'maker':x['maker'],'prijs':(x['pricing']['listPrice']['price'] if x['pricing'] else 0),'pay':x['pay'],
      'reviews':[{'r':v.get('rating'),'t':v.get('text') or '','d':v.get('date')} for v in rv]},ensure_ascii=False)+'\n'); f.flush()
