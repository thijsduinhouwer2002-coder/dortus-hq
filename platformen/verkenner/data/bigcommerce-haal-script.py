import re,json,sys,urllib.request,concurrent.futures as cf,time
urls=re.findall(r'<loc>([^<]+)</loc>',open(sys.argv[1]).read())
F=['createdOn','appRegistryUpdatedAt','reviewCount','rating','unifiedBilling','upfrontPrice','monthlyPrice','pricing','pricingType','freeTrial']
def one(u):
    for t in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 dortus-verkenner'}),timeout=30).read().decode('utf8','replace');break
        except Exception as e: h=None; time.sleep(2)
    if not h: return dict(url=u,fout=True)
    r=dict(url=u)
    for f in F:
        m=re.search(r'"%s":("(?:[^"\\]|\\.)*"|[^,}]*)'%f,h)
        if m:
            try: r[f]=json.loads(m.group(1))
            except: r[f]=m.group(1)
    m=re.search(r'"appReviewCount":(\d+)',h); r['appReviewCount']=int(m.group(1)) if m else None
    m=re.search(r'<title[^>]*>([^<]*)',h); r['title']=m.group(1) if m else None
    return r
with cf.ThreadPoolExecutor(8) as ex: R=list(ex.map(one,urls))
with open(sys.argv[2],'w') as f:
    for r in R: f.write(json.dumps(r)+'\n')
print(len(R),sum(1 for r in R if r.get('fout')),sum(1 for r in R if r.get('createdOn')))
