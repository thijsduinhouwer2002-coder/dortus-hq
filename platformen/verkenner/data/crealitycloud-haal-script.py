import re,json,urllib.request,time
out=[]
for u in open("/tmp/cc/sample.txt").read().split()[:110]:
    try:
        t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'curl/8.5.0'}),timeout=40).read().decode('utf8','ignore')
        d=json.loads(re.search(r'<script[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>',t,re.S).group(1))
        R=lambda x:d[x] if isinstance(x,int) and not isinstance(x,bool) and x<len(d) else x
        v=next(v for v in d if isinstance(v,dict) and 'downloadCount' in v and 'numOfPayment' in v)
        out.append({k:R(v.get(k)) for k in ['id','createTime','userId','groupName','isPay','totalPrice','numOfPayment','downloadCount','likeCount','pv','isOriginal','isExclusive','printCountTotal']})
    except Exception as e: out.append({'url':u,'err':str(e)[:60]})
    time.sleep(0.6)
    json.dump(out,open("/tmp/cc/sample.json","w"))
json.dump(out,open('/tmp/cc/sample.json','w')); print(len(out),sum('err' in r for r in out))
