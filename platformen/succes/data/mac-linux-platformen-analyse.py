import json,csv,statistics as st,sys
r={x['appid']:x for x in csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv'))}
p={}
for l in open(sys.argv[1] if len(sys.argv)>1 else 'platforms.jsonl'):
    d=json.loads(l)
    if isinstance(d['platforms'],dict): p[d['appid']]=d['platforms']
print('met platformgegevens',len(p))
def band(n):
    return '1000+' if n>=1000 else '100-999' if n>=100 else '10-99' if n>=10 else '0-9'
rows=[]
for a,pl in p.items():
    x=r[a]; n=int(x['reviews_totaal'] or 0)
    rows.append(dict(appid=a,naam=x['naam'],reviews=n,band=band(n),jaar=x['releasedatum'][:4],gratis=x['gratis'],soort=x['soort_spel'],mac=pl.get('mac'),linux=pl.get('linux'),lijkt=x['lijkt_op_hats']))
spel=[z for z in rows if z['soort']!='programma of hulpmiddel']
for naam,grp in [('alle',rows),('spellen (geen hulpmiddel)',spel),('betaalde spellen',[z for z in spel if z['gratis']=='False']),('kerker/gevecht',[z for z in spel if z['soort']=='gevecht, kerker of RPG'])]:
    print('##',naam,len(grp),'mac',round(100*sum(z['mac'] for z in grp)/len(grp)),'% linux',round(100*sum(z['linux'] for z in grp)/len(grp)),'%')
    for b in ['1000+','100-999','10-99','0-9']:
        g=[z for z in grp if z['band']==b]
        if g: print('  ',b,len(g),'mac',round(100*sum(z['mac'] for z in g)/len(g)),'%','linux',round(100*sum(z['linux'] for z in g)/len(g)),'%')
b=[z for z in spel if z['gratis']=='False' and z['jaar'] in ('2024','2025','2026')]
for m in (True,False):
    g=[z['reviews'] for z in b if z['mac']==m]
    print('betaald 2024-26 mac' if m else 'betaald 2024-26 geen mac',len(g),'mediaan reviews',st.median(g) if g else None, '100+',round(100*sum(1 for v in g if v>=100)/len(g)) if g else None,'%')
for j in ('2022','2023','2024','2025','2026'):
    g=[z for z in spel if z['jaar']==j]
    if g: print(j,len(g),'mac',round(100*sum(z['mac'] for z in g)/len(g)),'%')
with open('platforms.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(sorted(rows,key=lambda z:-z['reviews']))
