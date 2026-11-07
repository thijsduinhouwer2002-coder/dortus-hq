import json,time,urllib.request,datetime as dt,sys
d=json.load(open('raw/companion2.json'))
def pd(s):
    try: return dt.datetime.strptime(s,'%b %d, %Y').date()
    except: return None
c=[x for x in d if pd(x['released']) and dt.date(2026,5,1)<=pd(x['released'])<=dt.date(2026,8,31) and x['price']]
out={}
for x in c:
    try:
        j=json.load(urllib.request.urlopen(f"https://store.steampowered.com/api/appdetails?appids={x['appid']}&cc=us&l=english",timeout=30))[str(x['appid'])]
        if j['success']:
            a=j['data'];out[x['appid']]={'dev':a.get('developers'),'pub':a.get('publishers'),'type':a.get('type'),'genres':[g['description'] for g in a.get('genres',[])],'ai':bool(a.get('content_descriptors',{}).get('notes')) and 'AI' in (a.get('content_descriptors',{}).get('notes') or '')}
    except Exception as e: print('err',x['appid'],e)
    time.sleep(1.6)
json.dump(out,open('raw/companion-details.json','w'));print(len(out))
