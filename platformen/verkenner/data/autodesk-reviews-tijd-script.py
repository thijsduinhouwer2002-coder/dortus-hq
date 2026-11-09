# Gebruik: python3 -I autodesk-reviews-tijd-script.py autodesk-reviews-2026-11-09.jsonl (reviews per jaar en maand, top betaalde apps)
import json,collections as C,sys
sys.path=[p for p in sys.path if p]
A={json.loads(l)['url'].split('/')[-1]:json.loads(l) for l in open('/home/claude/dortus-hq/platformen/verkenner/data/autodesk-apps-2026-11-07.jsonl')}
def betaald(a):
    return any(p['type'] in('ONE_TIME','SUBSCRIPTION_MONTHLY','SUBSCRIPTION_ANNUAL') or any(float(b[0] or 0)>0 for b in p['bedragen']) for p in a.get('prijzen',[]))
rows=[json.loads(l) for l in open(sys.argv[1])]
fout=[r for r in rows if r.get('fout')]; rows=[r for r in rows if not r.get('fout')]
U={r['id']:r for r in rows}; rows=list(U.values())
print('reviews uniek',len(rows),'fouten',len(fout))
# reviews per jaar, betaald vs niet
j=C.Counter(); jb=C.Counter(); jv=C.Counter()
for r in rows:
    y=r['dateCreated'][:4]; j[y]+=1
    if betaald(A.get(r['appId'],{})): jb[y]+=1
    if r.get('isVerifiedDownload'): jv[y]+=1
for y in sorted(j): print(y,'alle',j[y],'op betaalde apps',jb[y],'geverifieerd',jv[y])
# per maand 2025-2026
m=C.Counter(r['dateCreated'][:7] for r in rows if r['dateCreated']>='2025-01')
mb=C.Counter(r['dateCreated'][:7] for r in rows if r['dateCreated']>='2025-01' and betaald(A.get(r['appId'],{})))
print([(k,m[k],mb[k]) for k in sorted(m)])
# laatste 12 maanden: betaalde apps met meeste reviews
L=[r for r in rows if r['dateCreated']>='2025-11-09']
c=C.Counter(r['appId'] for r in L if betaald(A.get(r['appId'],{})))
print('\nbetaald, reviews laatste 12 mnd, top 25:')
for k,v in c.most_common(25):
    a=A[k]; rs=[r for r in L if r['appId']==k]
    
    print(v,a.get('maker'),a.get('eerste','')[:10],a.get('producten',[])[:2],'geverif',sum(r.get('isVerifiedDownload',False) for r in rs),'gem',round(sum(r['rating'] for r in rs)/v,1),'dagen',len({r['dateCreated'][:10] for r in rs}),a['url'][-36:])
print('apps met 1+ review laatste 12 mnd: betaald',len(c),'alle',len({r['appId'] for r in L}))
