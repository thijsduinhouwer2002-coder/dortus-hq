import json,glob,os,statistics as st,collections
rows=json.load(open('det_rows.json'))
N=123175
tot30=sum(r['u30'] for r in rows)/len(rows)*N
print('geschat totaal maandgebruikers (actor-paren) hele winkel',round(tot30))
s=sorted([r['u30'] for r in rows],reverse=True); T=sum(s)
print('aandeel top 1% / 10% actors in steekproef', round(sum(s[:30])/T,2), round(sum(s[:300])/T,2))
M=[]
for f in glob.glob('mk/*.json'):
    if f.endswith('.first.json'): continue
    u=os.path.basename(f)[:-5]
    try: it=json.load(open(f))['data']['items']
    except: continue
    if not it: continue
    try: first=json.load(open(f'mk/{u}.first.json'))['data']['createdAt'][:7]
    except: first=None
    u30=sum(i['stats'].get('totalUsers30Days',0) for i in it)
    paid=sum(1 for i in it if (i.get('currentPricingInfo') or {}).get('pricingModel') not in (None,'FREE'))
    M.append(dict(u=u,n=len(it),u30=u30,first=first,paid=paid,top=max(i['stats'].get('totalUsers30Days',0) for i in it)))
print('makers',len(M))
def show(nm,L):
    if not L: return
    x=[m['u30'] for m in L]
    print(nm,'n',len(L),'med actors',st.median([m['n'] for m in L]),'med maandgeb',st.median(x),
      '%50+',round(100*sum(v>=50 for v in x)/len(L)),'%200+',round(100*sum(v>=200 for v in x)/len(L)),'%1000+',round(100*sum(v>=1000 for v in x)/len(L)))
show('alle makers',M)
show('begonnen voor 2025',[m for m in M if m['first'] and m['first']<'2025'])
show('begonnen 2025',[m for m in M if m['first'] and '2025'<=m['first']<'2026'])
show('begonnen jan-apr 2026',[m for m in M if m['first'] and '2026-01'<=m['first']<='2026-04'])
show('begonnen mei-aug 2026',[m for m in M if m['first'] and '2026-05'<=m['first']<='2026-08'])
show('begonnen sep-nov 2026',[m for m in M if m['first'] and m['first']>='2026-09'])
print(collections.Counter((m['first'] or 'x')[:4] for m in M))
for m in sorted([m for m in M if m['first'] and m['first']>='2025-07'],key=lambda m:-m['u30'])[:12]: print(m)
json.dump(M,open('makers_rows.json','w'))
