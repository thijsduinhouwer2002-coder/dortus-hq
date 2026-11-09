import json,urllib.request,time
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception as e: time.sleep(2+3*i)
    return {}
r=json.load(open('uac-makers.json'));out=[]
for x in r:
    if x['ctype']!='Group': continue
    g=get(f"https://groups.roblox.com/v1/groups/{x['cid']}"); own=(g.get('owner') or {}).get('userId')
    o={'id':x['id'],'owner':own,'owned_groups':None,'big_owned':0}
    if own:
        rl=get(f"https://groups.roblox.com/v1/users/{own}/groups/roles").get('data',[])
        owned=[q for q in rl if q['role']['rank']==255]
        o['owned_groups']=len(owned)
        o['big_owned']=sum(q['group']['memberCount']>=100000 for q in owned if q['group']['id']!=x['cid'])
    out.append(o); time.sleep(0.4)
json.dump(out,open('eigenaars.json','w'));print('klaar',len(out))
