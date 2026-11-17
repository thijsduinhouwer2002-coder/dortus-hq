import csv,json,time,urllib.request,os
r=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/succes/data/nextfest-tussenpoos-bureaublad-2026-11-17.csv')))
os.makedirs('h',exist_ok=True)
for x in r:
    a=x['appid']; f=f'h/{a}.json'
    if os.path.exists(f) or int(x['reviews_totaal'])<1: continue
    try:
        d=urllib.request.urlopen(f'https://store.steampowered.com/appreviewhistogram/{a}?l=english&review_score_preference=0',timeout=30).read()
        open(f,'wb').write(d)
    except Exception as e: print(a,e)
    time.sleep(0.6)
