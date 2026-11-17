# Fenna verhaal 22: reviews (tekst, speeltijd bij review) per spel ophalen, hooguit 1000 per spel, rustig.
import json, time, sys, urllib.request, urllib.parse, os
IN, OUT = sys.argv[1], sys.argv[2]
apps=[json.loads(l)['appid'] for l in open(IN)]
done=set(os.listdir(OUT)) if os.path.isdir(OUT) else set(); os.makedirs(OUT,exist_ok=True)
for a in apps:
    if a+'.json' in done: continue
    cur='*'; revs=[]; summ=None
    for p in range(10):
        u=f'https://store.steampowered.com/appreviews/{a}?json=1&filter=recent&language=all&purchase_type=all&num_per_page=100&cursor='+urllib.parse.quote(cur)
        d=None
        for t in range(3):
            try: d=json.load(urllib.request.urlopen(u,timeout=30)); break
            except Exception: time.sleep(15)
        if not d or not d.get('success'): break
        if summ is None: summ=d.get('query_summary')
        rs=d.get('reviews',[])
        for r in rs:
            revs.append({'id':r['recommendationid'],'up':r['voted_up'],'taal':r['language'],'tijd':r['timestamp_created'],
              'speel_bij_review':r['author'].get('playtime_at_review'),'speel_totaal':r['author'].get('playtime_forever'),
              'tekst':r['review'][:1500],'nuttig':r.get('votes_up',0)})
        if not rs or d.get('cursor')==cur: break
        cur=d['cursor']; time.sleep(1.0)
    json.dump({'appid':a,'samenvatting':summ,'reviews':revs},open(f'{OUT}/{a}.json','w'))
    time.sleep(0.5)
