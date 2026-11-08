import json,statistics as st,collections as C,sys
d=[json.loads(l) for l in open(sys.argv[1])]
ok=[x for x in d if x['ok'] and x['created']]
print('ok',len(ok),'geen prijzen',sum(not x['prices'] for x in ok))
for x in ok:
    pr=[p for p in x['prices']] or [x.get('base') or 0]
    x['minp']=min([p for p in pr if p>0],default=0); x['free']=x['minp']==0
def stats(g,lab):
    L=sorted(x['likes'] or 0 for x in g)
    if not L: return
    n=len(L);print(lab,n,'med',st.median(L),'p75',L[int(n*.75)],'p90',L[int(n*.9)],'10+',round(sum(v>=10 for v in L)/n*100),'%','50+',round(sum(v>=50 for v in L)/n*100),'%','100+',round(sum(v>=100 for v in L)/n*100),'%','500+',round(sum(v>=500 for v in L)/n*100,1),'%')
lic=[x for x in ok if '2026-05'<=x['created'][:7]<='2026-08']
paid=[x for x in lic if not x['free'] and x['minp']>0]
print('lichting',len(lic),'betaald (alle varianten >0)',len(paid))
stats(lic,'mei-aug alle');stats(paid,'mei-aug betaald')
for c in ['avatars','clothing','materials','avatar-props','world-assets','shaders','scripts']:
    stats([x for x in paid if x['cat']==c],'  '+c)
print('mediaanprijs betaald $',st.median(x['minp'] for x in paid)/100)
for c in ['avatars','clothing']: 
    g=[x['minp'] for x in paid if x['cat']==c]; print(' prijs',c,st.median(g)/100 if g else None)
s=[x for x in ok if x['sales'] is not None]; print('sales zichtbaar',len(s),'van',len(ok))
print(' mei-aug sales',sorted((x['sales'],x['cat'],x['minp']) for x in s if x in lic))
print(' alle sales med',st.median(x['sales'] for x in s))
ai=[x for x in ok if x['ai']]; print('AI-melding ingevuld',len(ai),C.Counter(x['ai'][:40] for x in ai).most_common(5))
print('per maand 2026',sorted(C.Counter(x['created'][:7] for x in ok if x['created']>='2026').items()))
