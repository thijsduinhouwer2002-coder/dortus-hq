# Google Play: analyse van een willekeurige lichting uit de sitemaps. Gebruik: python3 -I analyse.py det.jsonl
import json,collections,datetime,statistics as st,sys
r=[json.loads(l) for l in open(sys.argv[1])]
ok=[a for a in r if 'err' not in a and a.get('released')]
for a in ok:
    try: a['d']=datetime.datetime.strptime(a['released'],'%b %d, %Y').date()
    except: a['d']=None
ok=[a for a in ok if a['d']]
print('opgehaald',len(r),'404',sum(a.get('err')=='404' for a in r),'met datum',len(ok))
dc=collections.Counter(a['developerId'] for a in ok)
def rep(lbl,c):
    if not c: print(lbl,'leeg'); return
    ri=sorted(a['realInstalls'] or 0 for a in c); n=len(ri)
    f=lambda k:100*sum(x>=k for x in ri)/n
    rt=[a['ratings'] or 0 for a in c]
    print(f"{lbl}: n={n} mediaan={st.median(ri):.0f} p75={ri[int(.75*n)]} p90={ri[int(.9*n)]} 100+={f(100):.1f}% 1000+={f(1000):.1f}% 10k+={f(10000):.1f}% 100k+={f(100000):.1f}% | ratings mediaan={st.median(rt):.0f} 10+={100*sum(x>=10 for x in rt)/n:.1f}%")
A,B=datetime.date(2026,5,1),datetime.date(2026,8,31)
c=[a for a in ok if A<=a['d']<=B]
rep('mei-aug 2026 alle',c)
rep('  spellen',[a for a in c if a['genreId'].startswith('GAME')])
rep('  apps',[a for a in c if not a['genreId'].startswith('GAME')])
rep('  betaald (prijs>0)',[a for a in c if not a['free']])
rep('  met in-app-aankopen',[a for a in c if a['offersIAP']])
rep('  met reclame',[a for a in c if a['containsAds']])
rep('  maker met 1 app in steekproef',[a for a in c if dc[a['developerId']]==1])
for m in range(5,9):
    rep(f'  maand {m}',[a for a in c if a['d'].month==m])
rep('2025 jan-jun alle',[a for a in ok if datetime.date(2025,1,1)<=a['d']<=datetime.date(2025,6,30)])
rep('sep-okt 2026',[a for a in ok if datetime.date(2026,9,1)<=a['d']<=datetime.date(2026,10,31)])
g=collections.Counter(a['genreId'] for a in c); print('genres',g.most_common(12))
print('betaald aandeel',round(100*sum(not a['free'] for a in c)/len(c),1),'IAP',round(100*sum(bool(a['offersIAP']) for a in c)/len(c),1),'ads',round(100*sum(bool(a['containsAds']) for a in c)/len(c),1))
c.sort(key=lambda a:-(a['realInstalls'] or 0))
for a in c[:15]: print(' ',a['realInstalls'],a['ratings'],a['released'],a['genreId'],a['developer'][:30],'|',a['title'][:45])
