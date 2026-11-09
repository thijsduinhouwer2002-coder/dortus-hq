import json,glob,datetime as dt
files=sorted(glob.glob('snap/s-*.json'))
dates=[f[7:17] for f in files]
S=[json.load(open(f)) for f in files]
def dl(s,k):
    v=s.get(k); return v.get('downloads') if isinstance(v,dict) else None
for d,s in zip(dates,S):
    if d in('2026-04-06','2026-05-18','2026-08-10','2026-10-12','2026-11-02','2026-11-09'):
        print(d,sum(isinstance(v,dict) for v in s.values()))
first={}
for i,s in enumerate(S):
    for k,v in s.items():
        if isinstance(v,dict) and k not in first: first[k]=i
# gaps: plugins that disappear then reappear
gone=0
for k,i in first.items():
    pres=[isinstance(S[j].get(k),dict) for j in range(i,len(S))]
    if not all(pres): gone+=1
print('plugins met gat/verdwenen',gone)
print('nieuw',sum(1 for i in first.values() if i>0))
def q(xs,p): xs=sorted(xs); return xs[int(len(xs)*p)]
def pct(xs): 
    xs=sorted(xs);n=len(xs); return n, xs[n//2], xs[int(n*.9)], xs[int(n*.95)], sum(x>=1000 for x in xs), round(100*sum(x>=1000 for x in xs)/n,1)
for a,b in [('2026-05-01','2026-08-01'),('2026-08-01','2026-09-28')]:
    sel=[k for k,i in first.items() if i>0 and a<=dates[i]<b and i+6<len(S) and dl(S[i],k) is not None and dl(S[i],k)<100 and dl(S[i+6],k) is not None]
    print(a,b,pct([dl(S[first[k]+6],k)-dl(S[first[k]],k) for k in sel]))
    allsel=[k for k,i in first.items() if i>0 and a<=dates[i]<b and i+6<len(S) and dl(S[i+6],k) is not None and dl(S[i],k) is not None]
    print(' ook w0>=100:',pct([dl(S[first[k]+6],k)-dl(S[first[k]],k) for k in allsel]), ' totaal w6 (incl w0):',pct([dl(S[first[k]+6],k) for k in allsel]))
iN,iP=len(S)-1,len(S)-2
for a,b,l in [('2026-08-01','2026-09-01','aug'),('2026-09-01','2026-10-01','sep'),('2026-10-01','2026-11-01','okt')]:
    xs=[dl(S[iN],k)-dl(S[iP],k) for k,i in first.items() if a<=dates[i]<b and dl(S[iN],k) is not None and dl(S[iP],k) is not None]
    xs.sort();n=len(xs)
    print(l,n,xs[n//2],xs[int(n*.75)],xs[int(n*.9)],xs[int(n*.95)],sum(x>=168 for x in xs),round(100*sum(x>=168 for x in xs)/n,1), 'neg',sum(x<0 for x in xs))
for k in ['obsidian-dice-roller','atlas-vtt','sheetsmith','dice-rolls','onednd-character-sheet','fifth-edition-character-sheet','dice-tray','dice-table','perhaps','rollwright']:
    i=first.get(k)
    print(k, dates[i] if i is not None else None, dl(S[iN],k), dl(S[iP],k), [dl(s,k) for s in S[-8:]])
import collections
c=collections.Counter()
for k,i in first.items():
    pres=[isinstance(S[j].get(k),dict) for j in range(i,len(S))]
    if not all(pres):
        c['weg op 9 nov' if not pres[-1] else 'gat maar terug']+=1
print(c)
# total stats count over time drop?
print([ (dates[j],sum(isinstance(v,dict) for v in S[j].values())) for j in range(44,50)])
