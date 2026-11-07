# Verzamelt alle app-slugs uit de openbare function- en industry-pagina's van apps.xero.com, per regio, met ?page=N
import subprocess,re,json,sys,concurrent.futures as cf
base='https://apps.xero.com'
cats=[l.strip().replace(base+'/','') for l in open(sys.argv[1]) if '/function/' in l or '/industry/' in l]
regs=['au','uk','nz','us','ca','global','za','sg','ie','my','hk','ph','id']
def get(u): return subprocess.run(['curl','-sL','--max-time','40',u],capture_output=True,text=True).stdout
def slugs(s): return set(re.findall(r'href="/[a-z]{2,6}/app/([a-z0-9-]+)"',s))|set(re.findall(r'"/(?:[a-z]{2,6}/)?app/([a-z0-9-]+)"',s))|set(re.findall(r'/app/([a-z0-9-]+)',s))
def first(rc):
    r,c=rc; s=get(f'{base}/{r}/{c}')
    m=re.search(r'"pagination":\{"page":1,"pageSize":24,"pageCount":(\d+),"itemCount":(\d+)',s)
    return r,c,int(m[1]) if m else 1,int(m[2]) if m else 0,slugs(s)
jobs=[(r,c) for r in regs for c in cats]
res={};todo=[];counts={}
with cf.ThreadPoolExecutor(8) as ex:
    for r,c,pc,ic,sl in ex.map(first,jobs):
        counts[f'{r}/{c}']=ic; res.setdefault(r,set()).update(sl)
        todo+= [(r,c,p) for p in range(2,pc+1)]
    def more(x):
        r,c,p=x; return r,slugs(get(f'{base}/{r}/{c}?page={p}'))
    for r,sl in ex.map(more,todo): res[r].update(sl)
alls=set().union(*res.values())
json.dump(dict(per_regio={r:sorted(v) for r,v in res.items()},itemCount=counts,alle=sorted(alls)),open(sys.argv[2],'w'),indent=0)
print(len(alls),{r:len(v) for r,v in res.items()},len(todo))
