import re,json,sys,urllib.request,concurrent.futures as cf,time
urls=open('/tmp/at/sample.txt').read().split()
def get(u):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'curl/8.5.0'})
        t=urllib.request.urlopen(req,timeout=40).read().decode('utf8','ignore')
        d=json.loads(re.search(r'<script[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>',t,re.S).group(1))
        R=lambda x:d[x] if isinstance(x,int) and not isinstance(x,bool) and x<len(d) else x
        pid=int(re.search(r'/project/(\d+)',u).group(1))
        proj=next(v for v in d if isinstance(v,dict) and R(v.get('id'))==pid and 'isAiMake' in v)
        cas=next(v for v in d if isinstance(v,dict) and 'combinedActionSum' in v)
        cs={k:R(x) for k,x in R(cas['combinedActionSum']).items()}
        cands=[v for v in d if isinstance(v,dict) and 'sales' in v and 'like' in v and R(v['view'])==cs['view']]
        st=cands[-1] if cands else {}
        st=dict(st); st['used']=cas.get('combinedUsedCount')
        o={k:R(proj.get(k)) for k in ['id','createdBy','publishedAt','forSale','origPrice','isExclusive','isAiMake','aiAssistance','source','newType','title']}
        o.update({'st_'+k:R(v) for k,v in st.items()})
        return o
    except Exception as e: return {'url':u,'err':str(e)[:80]}
out=[]
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(get,urls): out.append(r)
json.dump(out,open('/tmp/at/sample.json','w'))
print(len(out),sum('err' in r for r in out))
