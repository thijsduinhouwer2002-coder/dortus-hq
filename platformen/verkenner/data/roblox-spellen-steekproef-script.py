import json,urllib.request,time,random,sys
random.seed(9)
def get(u):
    for i in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception as e: time.sleep(2+3*i)
    return {}
rows=[];asked=0
for b in range(200):
    ids=random.sample(range(10300000000,10500000000),50); asked+=50
    d=get("https://games.roblox.com/v1/games?universeIds="+",".join(map(str,ids)))
    for x in d.get('data',[]):
        if x['id']: rows.append({k:x[k] for k in ['id','name','visits','playing','created','updated']}|{'ctype':x['creator']['type']})
    time.sleep(0.3)
    if b%20==0: json.dump({'asked':asked,'rows':rows},open('steekproef.json','w'))
json.dump({'asked':asked,'rows':rows},open('steekproef.json','w'));print('klaar',asked,len(rows))
