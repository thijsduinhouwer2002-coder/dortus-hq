import sys,re,json,time,subprocess
def get(url):
    r=subprocess.run(['curl','-sL','-m','30',url],capture_output=True)
    s=r.stdout.decode('utf8','ignore')
    mid=url.rsplit('-',1)[1]
    out={'url':url,'id':mid}
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',s,re.S)
    if m:
        try:
            d=json.loads(m.group(1))
            fb=d['props']['pageProps'].get('fallback',{})
            for k,v in fb.items():
                if k.startswith('models/v2/'+mid) and isinstance(v,dict):
                    for f in ['name','isPaid','created','published','downloadCount','likesCount','viewCount','isAiGenerated','printSales','visibility','category','updatingUser']:
                        out[f]=v.get(f)
        except Exception as e: out['err']=str(e)
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
        try:
            d=json.loads(m.group(1))
            if d.get('@type')=='Product':
                out['price']=d.get('offers',{}).get('price'); out['ratingCount']=(d.get('aggregateRating') or {}).get('ratingCount'); out['brand']=(d.get('brand') or {}).get('name')
        except: pass
    return out
for line in sys.stdin:
    u=line.strip()
    if not u: continue
    print(json.dumps(get(u)),flush=True); time.sleep(0.7)
