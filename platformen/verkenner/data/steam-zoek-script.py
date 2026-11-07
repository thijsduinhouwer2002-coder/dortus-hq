import json,re,sys,time,urllib.request,urllib.parse,html
tag=sys.argv[1]; out=sys.argv[2]; maxn=int(sys.argv[3])
res=[];start=0
while True:
    q=urllib.parse.urlencode({'start':start,'count':100,'tags':tag,'sort_by':'Released_DESC','infinite':1,'category1':'998','cc':'us','l':'english','ndl':1})
    d=json.load(urllib.request.urlopen(urllib.request.Request('https://store.steampowered.com/search/results/?'+q,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
    total=d['total_count']; blocks=d['results_html'].split('<a href=')[1:]
    if not blocks: break
    for b in blocks:
        a=re.search(r'data-ds-appid="([\d,]+)"',b); t=re.search(r'<span class="title">(.*?)</span>',b,re.S)
        r=re.search(r'search_released[^>]*>\s*(.*?)\s*</div>',b,re.S)
        rv=re.search(r'data-tooltip-html="([^"]*)"',b); n=None
        if rv:
            m=re.search(r'of the ([\d,]+) user reviews',html.unescape(rv.group(1)));n=int(m.group(1).replace(',','')) if m else None
        p=re.search(r'data-price-final="(\d+)"',b)
        res.append({'appid':int(a.group(1).split(',')[0]),'title':html.unescape(t.group(1)) if t else '','released':r.group(1) if r else '','reviews':n or 0,'price':int(p.group(1))/100 if p else None})
    start+=100
    if start>=min(total,maxn): break
    time.sleep(1)
json.dump(res,open(out,'w'));print(tag,total,len(res))
