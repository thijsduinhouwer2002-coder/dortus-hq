import json,sys,urllib.request,time,concurrent.futures as cf
A=json.load(open(sys.argv[1]))
def get(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'dortus-verkenner'}),timeout=20) as r: return json.load(r)
    except Exception as e: return None
def one(a):
    p=a.get('package')
    if not p: return dict(a=a,stats=None,first=None)
    st=get(f'https://packagist.org/packages/{p}.json')
    first=None
    if st:
        vs=st['package'].get('versions',{})
        ts=[v.get('time') for k,v in vs.items() if v.get('time') and not k.startswith('dev-')]
        first=min(ts) if ts else None
        d=st['package'].get('downloads');t=st['package'].get('time')
        st=dict(downloads=d,created=t,favers=st['package'].get('favers'))
    return dict(slug=a['slug'],url=a['url'],seller=a['seller']['name'],package=p,price_range=a['price_range'],editions=a['editions'],stats=st,first=first)
with cf.ThreadPoolExecutor(8) as ex: R=list(ex.map(one,A))
json.dump(R,open(sys.argv[2],'w'))
print(len(R),sum(1 for r in R if r.get('stats')))
