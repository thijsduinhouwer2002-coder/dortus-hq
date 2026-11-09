import re,sys,json,time,subprocess,concurrent.futures as cf
urls=[l.strip() for l in open(sys.argv[1])]
first={}
for u in urls:
    t=u.split('/')[4]
    first.setdefault(t,u)
M='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
def get(u):
    for i in range(3):
        r=subprocess.run(['curl','-sL','-A','Mozilla/5.0','--max-time','30',u],capture_output=True,text=True)
        if r.stdout and len(r.stdout)>5000: return r.stdout
        time.sleep(2)
    return ''
def dates(h):
    out=[]
    for m,d,y in re.findall(r'>\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}), (20\d\d)\s*<',h):
        out.append('%s-%02d-%02d'%(y,M.index(m)+1,int(d)))
    return out
def one(t):
    u=first[t]; h=get(u)
    d={'theme':t,'url':u}
    m=re.search(r'% positive\s*<[^>]*>\s*(?:<[^>]*>\s*)*(\d[\d,]*) reviews?',h) or re.search(r'(\d[\d,]*) reviews? for all presets',h); d['reviews']=int(m.group(1).replace(',','')) if m else 0
    m=re.search(r'(\d+)% positive',h); d['pos']=int(m.group(1)) if m else None
    m=re.search(r'Designed by ([^<]+)<',h); d['designer']=m.group(1).strip() if m else None
    m=re.search(r'Version ([\d.]+)',h); d['version']=m.group(1) if m else None
    m=re.search(r'\$(\d+) USD',h); d['price']=int(m.group(1)) if m else (0 if 'Free' in h[:60000] else None)
    ds=[]
    if d['reviews']>0:
        r1=get(u+'/reviews'); ds+=dates(r1)
        pages=[int(x) for x in re.findall(r'reviews\?page=(\d+)',r1)]
        if pages:
            ds+=dates(get(u+'/reviews?page=%d'%max(pages)))
    d['oldest_review']=min(ds) if ds else None
    d['newest_review']=max(ds) if ds else None
    return d
res=[]
with cf.ThreadPoolExecutor(4) as ex:
    for d in ex.map(one,sorted(first)):
        res.append(d); print(json.dumps(d),flush=True)
