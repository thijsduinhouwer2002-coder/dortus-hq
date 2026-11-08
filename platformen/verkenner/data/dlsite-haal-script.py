# Haalt productinfo van DLsite (alle leeftijden, /home) in groepen van 100 via /home/product/info/ajax, 10 s tussen verzoeken (Crawl-delay robots.txt).
# Gebruik: python3 dlsite-haal-script.py ids.txt uit.jsonl
import json,sys,time,urllib.request
ids=open(sys.argv[1]).read().split();f=open(sys.argv[2],'a')
keep=['maker_id','dl_count','wishlist_count','rate_count','review_count','price','price_without_tax','regist_date','work_type','work_name','is_free','is_ana','custom_genres','on_sale']
for i in range(0,len(ids),100):
    url="https://www.dlsite.com/home/product/info/ajax?product_id="+",".join(ids[i:i+100])
    for t in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; DortusVerkenner/1.0)"}),timeout=60));break
        except Exception as e: print(e,file=sys.stderr);time.sleep(30)
    else: continue
    if isinstance(d,dict):
        for k,v in d.items():
            r={x:v.get(x) for x in keep};r['id']=k;f.write(json.dumps(r,ensure_ascii=False)+"\n")
    f.flush();print(i,len(d),file=sys.stderr,flush=True);time.sleep(10)
