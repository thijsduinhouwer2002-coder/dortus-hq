# Steekproef van de nieuwste Firefox-extensies via de open API van addons.mozilla.org (sort=created).
# De API geeft maximaal 600 pagina's van 50 (30.000 nieuwste). We nemen elke 5e pagina.
# Gebruik: python3 firefox-haal-script.py uit.json
import json,sys,subprocess,time
out=[]
for page in range(1,601,5):
    u=f'https://addons.mozilla.org/api/v5/addons/search/?app=firefox&type=extension&sort=created&page_size=50&page={page}'
    d=json.loads(subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout)
    for a in d.get('results',[]):
        out.append({'page':page,'slug':a['slug'],'created':a['created'],'adu':a['average_daily_users'],
                    'ratings':a['ratings']['count'],'requires_payment':a.get('requires_payment'),'promoted':a.get('promoted'),
                    'authors':[x.get('name') for x in a.get('authors',[])],'contributions_url':bool(a.get('contributions_url'))})
    time.sleep(0.2)
print(len(out), out[-1]['created'])
json.dump(out,open(sys.argv[1],'w'))
