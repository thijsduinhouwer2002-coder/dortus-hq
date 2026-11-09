import json,subprocess,sys,time
ids=json.load(open(sys.argv[1]))
res={}
for game,aid in ids.items():
    p=subprocess.run(['curl','-s','-m','20',f'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={aid}'],capture_output=True,text=True).stdout
    n=subprocess.run(['curl','-s','-m','20',f'https://store.steampowered.com/api/appdetails?appids={aid}&filters=basic'],capture_output=True,text=True).stdout
    try: pc=json.loads(p)['response'].get('player_count')
    except Exception: pc=None
    try: nm=json.loads(n)[str(aid)]['data']['name']
    except Exception: nm=None
    res[game]={'appid':aid,'steamnaam':nm,'spelers_nu':pc}
    print(game,aid,nm,pc,flush=True); time.sleep(0.6)
json.dump(res,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
