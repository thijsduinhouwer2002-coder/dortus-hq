import csv,statistics as st,datetime as dt,collections
R0=[r for r in csv.DictReader(open('blender_vroeg.csv'))]
seen=set();R=[]
for r in R0:
    k=(r['naam'],r['gepubliceerd'],r['downloads'])
    if k in seen: continue
    seen.add(k)
    if r['gepubliceerd']=='2024-05-14': continue
    R.append(r)
print('na dubbel en zonder verhuisde add-ons van 14 mei 2024:',len(R),'van',len(R0))
for r in R: r['d']=dt.date.fromisoformat(r['gepubliceerd']); r['n']=int(r['downloads'])
now=dt.date(2026,11,17)
print('eerste',min(r['d'] for r in R));c=collections.Counter(r['d'].strftime('%Y-%m') for r in R);print(sorted(c.items()))
start=min(r['d'] for r in R)
def coh(d):
    m=(d.year-start.year)*12+d.month-start.month
    return ['a mnd 0-3','b mnd 3-6','c mnd 6-12','d jaar 2 eerste helft','e jaar 2 tweede helft','f jaar 3'][0 if m<3 else 1 if m<6 else 2 if m<12 else 3 if m<18 else 4 if m<24 else 5]
tot=sum(r['n'] for r in R);rk=sorted(R,key=lambda r:-r['n']);t100={r['id'] for r in rk[:100]}
g=collections.defaultdict(list)
for r in R: g[coh(r['d'])].append(r)
print('cohort n mediaan dl/dag %>=10k aandeel top100')
for k in sorted(g):
    L=g[k];n=len(L)
    print(k,n,int(st.median(r['n'] for r in L)),round(st.median(r['n']/max((now-r['d']).days,1) for r in L),1),f"{100*sum(r['n']>=10000 for r in L)/n:.0f}%",f"{100*sum(r['n'] for r in L)/tot:.1f}%",sum(r['id'] in t100 for r in L))
print(tot)
for r in rk[:20]: print(r['n'],r['naam'],r['d'])
