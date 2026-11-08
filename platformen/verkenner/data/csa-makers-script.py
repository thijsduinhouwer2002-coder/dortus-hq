# Per maker in het GOLD-cohort mei t/m aug 2026: totaal GOLD-materialen en hoeveel daarvan voor 2026 en voor mei 2026.
import json,urllib.request,urllib.parse,time,sys
rows=[json.loads(l) for l in open('csa-gold-mrt-okt.jsonl')]
makers=sorted({r['clip_user_handle'] for r in rows if r['_maand'] in ('2026-05','2026-06','2026-07','2026-08')})
def found(p):
    for t in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request("https://assets.clip-studio.com/en-us/search/ajax?"+urllib.parse.urlencode(p),headers={"User-Agent":"Mozilla/5.0 (compatible; DortusVerkenner/1.0)"}),timeout=30))["response_data"]["found"]
        except Exception as e: print(e,file=sys.stderr);time.sleep(10)
out={}
for h in makers:
    a=found({"order":"new","pay":"gold","user":h});time.sleep(0.8)
    b=found({"order":"new","pay":"gold","user":h,"published_to":"2025-12-31T23:59:59.999Z"});time.sleep(0.8)
    c=found({"order":"new","pay":"gold","user":h,"published_to":"2026-04-30T23:59:59.999Z"});time.sleep(0.8)
    out[h]={"gold_totaal":a,"gold_voor_2026":b,"gold_voor_mei_2026":c}
    print(h,out[h],file=sys.stderr,flush=True)
json.dump(out,open('csa-makers.json','w'),ensure_ascii=False,indent=0)
