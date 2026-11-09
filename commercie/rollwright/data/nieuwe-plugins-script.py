# Chris run 25, 9 nov 2026. Momentopnamen: git clone -q --filter=blob:none --no-checkout https://github.com/obsidianmd/obsidian-releases.git or
# dan per week vanaf 1 dec 2025: c=$(git -C or log -1 --format=%h --before=<datum>T23:59 -- community-plugin-stats.json); git -C or show $c:community-plugin-stats.json > snap/s-<datum>.json
# plugins.json = community-plugins.json van HEAD. Deel 1 maakt nieuw.json, deel 2 de verdeling vanaf w0 (w0<100), deel 3 de tsv en de schone week. Controle van de controleur: nieuwe-plugins-controle.py.
import json,glob,datetime as dt,re,sys
files=sorted(glob.glob('snap/s-*.json'))
dates=[dt.date.fromisoformat(f[7:17]) for f in files]
S=[json.load(open(f)) for f in files]
P={p['id']:p for p in json.load(open('plugins.json'))}
first={}
for d,s in zip(dates,S):
    for k,v in s.items():
        if isinstance(v,dict) and k not in first: first[k]=d
start=dates[1]  # appeared after first snapshot = new
rows=[]
for k,f0 in first.items():
    if f0<=dates[0]: continue
    i=dates.index(f0)
    def at(w):
        j=i+w
        if j>=len(S): return None
        v=S[j].get(k); return v.get('downloads') if isinstance(v,dict) else None
    p=P.get(k,{})
    rows.append(dict(id=k,first=str(f0),w0=at(0),w2=at(2),w4=at(4),w6=at(6),now=S[-1].get(k,{}).get('downloads') if isinstance(S[-1].get(k),dict) else None,name=p.get('name',''),desc=p.get('description','')))
json.dump(rows,open('nieuw.json','w'))
print('nieuw sinds',dates[1],len(rows))
ok=[r for r in rows if r['w6'] is not None]
print('met 6 weken data',len(ok))
import statistics as st
for w in ['w2','w4','w6']:
    xs=sorted(r[w] for r in ok)
    n=len(xs); print(w,'mediaan',xs[n//2],'p75',xs[int(n*.75)],'p90',xs[int(n*.9)],'p99',xs[int(n*.99)],'>=1000',sum(x>=1000 for x in xs))
import json
rows=[r for r in json.load(open('nieuw.json')) if r['w0'] is not None]
def stats(sel,label):
    print('==',label,len(sel))
    for w in ['w2','w4','w6']:
        xs=sorted(r[w]-r['w0'] for r in sel if r[w] is not None)
        n=len(xs)
        if not n: continue
        print(f" {w} n={n} mediaan={xs[n//2]} p75={xs[int(n*.75)]} p90={xs[int(n*.9)]} p95={xs[int(n*.95)]} p99={xs[int(n*.99)]} >=1000:{sum(x>=1000 for x in xs)} ({100*sum(x>=1000 for x in xs)/n:.1f}%)")
import collections
print('w0 verdeling', collections.Counter(min(r['w0']//100*100,1000) for r in rows).most_common(6))
for a,b in [('2025-12-02','2026-05-01'),('2026-05-01','2026-08-01'),('2026-08-01','2026-09-28')]:
    stats([r for r in rows if a<=r['first']<b and r['w0']<100],f'w0<100, eerst gezien {a} tot {b}')

# Deel 3: tsv en de schone week (2 tot 9 nov), tabel 2b
import json,csv
a=json.load(open('snap/s-2026-11-02.json'));b=json.load(open('snap/s-2026-11-09.json'))
rows=[r for r in json.load(open('nieuw.json')) if r['w0'] is not None]
def g(k):
    x=(b.get(k) or {}).get('downloads');y=(a.get(k) or {}).get('downloads')
    return None if x is None or y is None else x-y
w=csv.writer(open('nieuwe-plugins-2026-11-09.tsv','w'),delimiter='\t')
w.writerow(['id','eerst_gezien','w0','w2','w4','w6','nu','week_2_9_nov','naam'])
for r in sorted(rows,key=lambda r:r['first']):
    v=g(r['id']); w.writerow([r['id'],r['first'],r['w0'],r['w2'],r['w4'],r['w6'],r['now'],'' if v is None else v,r['name']])
for lo,hi in [('2026-08-01','2026-09-01'),('2026-09-01','2026-10-01'),('2026-10-01','2026-10-27')]:
    for f in (lambda r:True, lambda r:r['w0']<100):
        xs=sorted(v for v in (g(r['id']) for r in rows if lo<=r['first']<hi and f(r)) if v is not None)
        n=len(xs);print(lo,n,xs[n//2],xs[int(.75*n)],xs[int(.9*n)],xs[int(.95*n)],sum(v>=168 for v in xs))
