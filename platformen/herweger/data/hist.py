import json,sys,time,urllib.request,datetime
src,out=sys.argv[1],sys.argv[2]
d=json.load(open(src))
def dt(s):
    for f in('%b %d, %Y','%d %b, %Y'):
        try: return datetime.datetime.strptime(s,f)
        except: pass
sel=[x for x in d if x['price'] and dt(x['released']) and datetime.datetime(2026,3,1)<=dt(x['released'])<=datetime.datetime(2026,10,12)]
res=[]
for x in sel:
    try:
        r=json.load(urllib.request.urlopen(f"https://store.steampowered.com/appreviewhistogram/{x['appid']}?l=english&review_score_preference=0",timeout=30))['results']
        x['hist']={'type':r.get('rollup_type'),'start':r.get('start_date'),'rollups':r.get('rollups',[])}
    except Exception as e: x['hist']={'err':str(e)}
    res.append(x); time.sleep(0.7)
json.dump(res,open(out,'w'));print(len(res))
