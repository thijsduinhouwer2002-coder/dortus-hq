import csv,json,os,datetime as dt,statistics as st,collections
r=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/succes/data/nextfest-tussenpoos-bureaublad-2026-11-17.csv')))
tab=[];kruis=[]
for x in r:
    tot=int(x['reviews_totaal'])
    if x['releasedatum']>'2026-08-15': continue  # minstens 3 maanden oud
    f='h/'+x['appid']+'.json'
    if tot==0: tab.append((x,'geen review',None)); continue
    if not os.path.exists(f): continue
    try: d=json.load(open(f))['results']
    except Exception: continue
    if d.get('rollup_type')!='week': continue
    rel=int(dt.datetime.fromisoformat(x['releasedatum']).replace(tzinfo=dt.timezone.utc).timestamp())
    ws=sorted(d['rollups'],key=lambda w:w['date'])
    ws=[w for w in ws if w['date']>=rel-6*86400]
    n=[w['recommendations_up']+w['recommendations_down'] for w in ws]
    cum=0;i10=None
    for i,v in enumerate(n):
        cum+=v
        if cum>=10: i10=i;break
    if i10 is None: tab.append((x,'nooit (nog niet)',None)); continue
    g='week 1' if i10<=1 else 'week 2 tot 4' if i10<=4 else 'week 5 tot 13' if i10<=12 else 'later'
    tab.append((x,g,i10))
    if i10>=4 and len(n)>=i10+4:
        voor=n[i10-3:i10]; na=n[i10+1:i10+4]
        kruis.append((x['naam'],sum(voor)/3,sum(na)/3,i10))
c=collections.defaultdict(list)
for x,g,i in tab: c[g].append(int(x['reviews_totaal']))
print('spellen minstens 3 mnd oud met weekgrafiek of 0 reviews:',len(tab))
for g in ['week 1','week 2 tot 4','week 5 tot 13','later','nooit (nog niet)','geen review']:
    v=c[g]
    if v: print(g,len(v),'mediaan nu',st.median(v),'100+',sum(1 for y in v if y>=100))
print('kruising na week 3:',len(kruis))
hoger=sum(1 for k in kruis if k[2]>k[1]); lager=sum(1 for k in kruis if k[2]<k[1])
print('na hoger',hoger,'lager',lager,'gelijk',len(kruis)-hoger-lager)
print('mediaan voor',st.median([k[1] for k in kruis]),'na',st.median([k[2] for k in kruis]))
for k in sorted(kruis,key=lambda k:-k[2])[:8]: print(k)
json.dump([(x['appid'],x['naam'],g,i) for x,g,i in tab],open('anaC.json','w'))
json.dump(kruis,open('kruis.json','w'))
