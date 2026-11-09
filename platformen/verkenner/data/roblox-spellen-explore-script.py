import json,urllib.request,uuid,time,sys
S=str(uuid.uuid4())
def get(u):
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception as e:
            time.sleep(2+i*3); err=e
    print('fout',u,err,file=sys.stderr); return {}
out={}
for sid in ['up-and-coming','top-trending','top-playing-now']:
    games=[];tok=''
    for p in range(15):
        d=get(f"https://apis.roblox.com/explore-api/v1/get-sort-content?sessionId={S}&sortId={sid}&device=computer&country=all&pageToken={tok}")
        games+=d.get('games',[]);tok=d.get('nextPageToken')
        if not tok:break
        time.sleep(0.5)
    out[sid]=games;print(sid,len(games))
ids=sorted({g['universeId'] for v in out.values() for g in v})
det={}
for i in range(0,len(ids),50):
    d=get("https://games.roblox.com/v1/games?universeIds="+",".join(map(str,ids[i:i+50])))
    for x in d.get('data',[]):det[x['id']]=x
    time.sleep(0.5)
json.dump({'sorts':out,'details':det},open('explore.json','w'))
print(len(det))
