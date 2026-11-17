import json,datetime as dt,statistics as st,collections
f=json.load(open('firstseen.json'));s=json.load(open('stats.json'));p=json.load(open('plugins.json'))
now=dt.datetime(2026,11,17).timestamp()
rows=[]
for x in p:
    i=x['id']
    if i not in f or i not in s: continue
    d=s[i]['downloads'];age=(now-f[i])/86400
    rows.append((i,f[i],d,age,x['name']))
open('obs_rows.csv','w').write('id,eerst_gezien,downloads,leeftijd_dagen,naam\n'+''.join(f'{r[0]},{dt.datetime.utcfromtimestamp(r[1]).date()},{r[2]},{r[3]:.0f},"{r[4]}"\n' for r in rows))
tot=sum(r[2] for r in rows)
rank=sorted(rows,key=lambda r:-r[2]);top100={r[0] for r in rank[:100]};top500={r[0] for r in rank[:500]}
def coh(t):
    d=dt.datetime.utcfromtimestamp(t)
    m=(d.year-2020)*12+d.month-10  # months since Oct 2020
    if m<3: return 'a 0-3 mnd (okt-dec 2020)'
    if m<12: return 'b 3-12 mnd (2021 t/m sep)'
    if m<24: return 'c jaar 2'
    if m<36: return 'd jaar 3'
    if m<48: return 'e jaar 4'
    if m<60: return 'f jaar 5'
    if m<67: return 'g okt 2025 tot apr 2026'
    return 'h vanaf mei 2026 (vloed)'
g=collections.defaultdict(list)
for r in rows: g[coh(r[1])].append(r)
print('cohort | n | mediaan dl | mediaan dl/dag | %>=10k | aandeel totaal | in top100 | in top500')
for k in sorted(g):
    L=g[k];n=len(L)
    print(k,n,int(st.median(r[2] for r in L)),round(st.median(r[2]/max(r[3],1) for r in L),2),
      f"{100*sum(r[2]>=10000 for r in L)/n:.0f}%",f"{100*sum(r[2] for r in L)/tot:.1f}%",sum(r[0] in top100 for r in L),sum(r[0] in top500 for r in L))
print('totaal',len(rows),tot)
