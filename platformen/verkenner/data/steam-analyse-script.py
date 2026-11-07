import json,statistics as st,datetime as dt
def pd(s):
    for f in ('%b %d, %Y','%d %b, %Y'):
        try: return dt.datetime.strptime(s,f).date()
        except: pass
for f in ['companion2','idler2']:
    d=json.load(open('raw/'+f+'.json'))
    c=[x for x in d if pd(x['released']) and dt.date(2026,5,1)<=pd(x['released'])<=dt.date(2026,8,31)]
    for lab,g in [('alle',c),('betaald',[x for x in c if x['price']]),('gratis',[x for x in c if x['price']==0])]:
        r=sorted(x['reviews'] for x in g)
        if not r: continue
        n=len(r); q=lambda k: sum(1 for v in r if v>=k)
        print(f,lab,'n',n,'mediaan',st.median(r),'p75',r[int(n*.75)],'p90',r[int(n*.9)],'10+',round(100*q(10)/n),'%','50+',round(100*q(50)/n),'%','100+',round(100*q(100)/n),'%','500+',q(500))
    b=[x for x in c if x['price']]
    print(' mediaanprijs betaald',st.median(x['price'] for x in b))
    print(' top betaald',[(x['title'],x['reviews'],x['price'],x['released']) for x in sorted(b,key=lambda x:-x['reviews'])[:12]])
