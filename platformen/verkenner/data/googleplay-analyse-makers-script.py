# Google Play: lichting mei-aug 2026 naar soort maker. Gebruik: python3 -I analyse2.py det.jsonl devs.json
import json,sys,statistics as st,collections,re
r=[json.loads(l) for l in open(sys.argv[1])]; dv=json.load(open(sys.argv[2]))
c=[a for a in r if 'err' not in a and a.get('released') and a['released'][-4:]=='2026' and a['released'][:3] in ('May','Jun','Jul','Aug')]
print('verdeling apps per makerpagina',collections.Counter(min(dv[a['developerId']],30)//5*5 for a in c).most_common())
corp=re.compile(r'\b(inc|llc|ltd|limited|gmbh|corp|co\.|company|s\.?a\.?|s\.?r\.?l|pvt|private|b\.?v|ag|oy|ab|technolog|studio|games|labs?|solutions|software|media|group|bank|pty|jsc|ltda|tech|apps|digital)\b',re.I)
def rep(lbl,x):
    ri=sorted(a['realInstalls'] or 0 for a in x); n=len(ri)
    if not n: return
    f=lambda k:100*sum(v>=k for v in ri)/n
    print(f"{lbl}: n={n} mediaan={st.median(ri):.0f} 100+={f(100):.1f}% 1000+={f(1000):.1f}% 10k+={f(10000):.1f}%")
rep('alle',c)
rep('maker met 1-3 apps',[a for a in c if dv[a['developerId']]<=3])
rep('maker met 1-3 apps, naam zonder bedrijfsvorm',[a for a in c if dv[a['developerId']]<=3 and not corp.search(a['developer'])])
rep('maker met 1-3 apps, spel',[a for a in c if dv[a['developerId']]<=3 and a['genreId'].startswith('GAME')])
rep('maker met 1-3 apps, IAP',[a for a in c if dv[a['developerId']]<=3 and a['offersIAP']])
rep('maker met 4-20 apps',[a for a in c if 4<=dv[a['developerId']]<=20])
rep('maker met 21+ apps',[a for a in c if dv[a['developerId']]>20])
rep('zonder winkels/bedrijf/bank (SHOPPING,BUSINESS,FINANCE,FOOD,TRAVEL,EVENTS) en 1-3 apps',[a for a in c if dv[a['developerId']]<=3 and a['genreId'] not in ('SHOPPING','BUSINESS','FINANCE','FOOD_AND_DRINK','TRAVEL_AND_LOCAL','EVENTS','MEDICAL','AUTO_AND_VEHICLES','HOUSE_AND_HOME')])
rep('alleen VS-rating heeft niet; inkomstenmodel: IAP of betaald, 1-3 apps, geen reclame',[a for a in c if dv[a['developerId']]<=3 and (a['offersIAP'] or not a['free']) and not a['containsAds']])
