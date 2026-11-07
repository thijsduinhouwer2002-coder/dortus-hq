import json,time,urllib.request,datetime as dt
d=json.load(open('raw/companion2.json'))
def pd(s):
    try: return dt.datetime.strptime(s,'%b %d, %Y').date()
    except: return None
c=[x for x in d if pd(x['released']) and dt.date(2026,5,1)<=pd(x['released'])<=dt.date(2026,8,31)]
out={}
for x in c:
    for i in range(3):
        try:
            j=json.load(urllib.request.urlopen(f"https://store.steampowered.com/api/appdetails?appids={x['appid']}&cc=us",timeout=30))[str(x['appid'])]
            a=j.get('data',{}); po=a.get('price_overview') or {}
            out[x['appid']]={'title':x['title'],'released':x['released'],'zoek_reviews':x['reviews'],'totaal':(a.get('recommendations') or {}).get('total'),'lijstprijs':po.get('initial',0)/100 if po else 0.0,'gratis':a.get('is_free')}
            break
        except Exception as e: time.sleep(10)
    time.sleep(1.6)
json.dump(out,open('raw/companion-totaal.json','w'),indent=0);print(len(out))
