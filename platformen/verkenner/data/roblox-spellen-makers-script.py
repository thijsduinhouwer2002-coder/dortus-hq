import json,urllib.request,time,sys
def get(u):
    for i in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception as e: time.sleep(2+3*i); err=e
    print('fout',u,err,file=sys.stderr); return {}
d=json.load(open('explore.json'));det={int(k):v for k,v in d['details'].items()}
uac=[det[x['universeId']] for x in d['sorts']['up-and-coming'] if x['universeId'] in det]
res=[]
for r in uac:
    c=r['creator'];o={'id':r['id'],'name':r['name'],'playing':r['playing'],'visits':r['visits'],'created':r['created'][:10],'ctype':c['type'],'cname':c['name'],'cid':c['id'],'verified':c['hasVerifiedBadge']}
    if c['type']=='Group':
        g=get(f"https://groups.roblox.com/v1/groups/{c['id']}"); o['members']=g.get('memberCount')
        gl=get(f"https://games.roblox.com/v2/groups/{c['id']}/gamesV2?accessFilter=2&limit=50&sortOrder=Asc")
    else:
        gl=get(f"https://games.roblox.com/v2/users/{c['id']}/games?accessFilter=2&limit=50&sortOrder=Asc")
    games=gl.get('data',[])
    other=[x for x in games if x['id']!=r['id']]
    o['n_games']=len(games); o['other_visits_max']=max([x.get('placeVisits',0) for x in other],default=0)
    o['oldest_game']=min([x['created'][:10] for x in games],default=None)
    gp=get(f"https://apis.roblox.com/game-passes/v1/universes/{r['id']}/game-passes?passView=Full&pageSize=100")
    prices=[x.get('price') for x in gp.get("gamePasses",[])]
    o['passes']=len(prices); o['pass_prices']=prices
    res.append(o); time.sleep(0.4)
json.dump(res,open('uac-makers.json','w'),indent=0)
print(len(res))
