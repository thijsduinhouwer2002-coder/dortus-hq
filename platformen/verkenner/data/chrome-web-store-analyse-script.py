import json,statistics,datetime as dt
D=__import__('sys').argv[1] if len(__import__('sys').argv)>1 else 'cws'
lo=dt.datetime(2026,5,16).timestamp(); hi=dt.datetime(2026,8,16).timestamp()
def rep(name,rows):
    n=len(rows)
    if not n: print(name,'0'); return
    u=sorted(rows); print(f"{name}: n={n} mediaan={statistics.median(u)} >=100: {sum(x>=100 for x in u)/n:.0%} >=1000: {sum(x>=1000 for x in u)/n:.0%} max={u[-1]}")
S=[json.loads(l) for l in open(D+'/cws_sample.jsonl')]
ok=[s for s in S if s['main']]
print('steekproef pagina\'s',len(S),'met data',len(ok))
ages=[int(s['main'][1]) for s in ok]
rep('alle (willekeurig, sitemap shard 0)',[int(s['main'][0]) for s in ok])
win=[s for s in ok if lo<=int(s['main'][1])<=hi]
rep('willekeurig, 3-6 mnd oud',[int(s['main'][0]) for s in win])
y26=[s for s in ok if int(s['main'][1])>=dt.datetime(2026,1,1).timestamp()]
rep('willekeurig, aangemaakt 2026',[int(s['main'][0]) for s in y26])
print('aandeel iap in steekproef',sum(s['iap'] for s in ok)/len(ok))
R={}
for l in open(D+'/cws_related.jsonl'):
    r=json.loads(l); R[(r['users'],r['ts'])]=r
rr=[int(u) for (u,t) in R if lo<=int(t)<=hi]
rep('gerelateerde items (scheef), 3-6 mnd oud',rr)
