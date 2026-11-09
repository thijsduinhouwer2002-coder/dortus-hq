import json,urllib.request,urllib.parse,time,uuid,sys
S=str(uuid.uuid4())
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception as e: time.sleep(2+3*i)
    return {}
kw=['obby','tycoon','simulator','brainrot','tower defense','horror','clicker','incremental','idle','rng','anime','fishing','garden','pet','race','parkour','roleplay','survival','escape','shooter','fighting','merge','farm','story','difficulty chart']
U={}
for k in kw:
    tok=''
    for p in range(8):
        d=get(f"https://apis.roblox.com/search-api/omni-search?searchQuery={urllib.parse.quote(k)}&sessionId={S}&pageType=all&pageToken={tok}")
        for sr in d.get('searchResults',[]):
            for c in sr.get('contents',[]):
                if c.get('contentType')=='Game': U.setdefault(c['universeId'],{'kw':k,'rank':len(U)})
        tok=d.get('nextPageToken')
        if not tok: break
        time.sleep(0.4)
    print(k,len(U),flush=True)
ids=list(U);det={}
for i in range(0,len(ids),50):
    d=get("https://games.roblox.com/v1/games?universeIds="+",".join(map(str,ids[i:i+50])))
    for x in d.get('data',[]): det[x['id']]={k:x[k] for k in ['id','name','visits','playing','created','updated']}|{'ctype':x['creator']['type'],'cid':x['creator']['id'],'cname':x['creator']['name']}
    time.sleep(0.3)
json.dump(det,open('zoek.json','w'));print('klaar',len(det))
