# Haalt per WooCommerce Marketplace-productpagina de openbare velden op (installaties, datum, prijs, reviews, maker).
# Gebruik: python3 -I woo-haal-script.py urls.txt uit.jsonl   (urls uit product-sitemap.xml en product-sitemap2.xml)
import sys, json, re, html, time, urllib.request
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
done=set()
try:
    for l in open(sys.argv[2]): done.add(json.loads(l)["url"])
except FileNotFoundError: pass
out=open(sys.argv[2],"a")
def veld(t,k):
    m=re.search(r'"%s":("(?:[^"\\]|\\.)*"|-?[0-9.]+|true|false|null)'%k,t)
    return json.loads(m.group(1)) if m else None
for u in urls:
    if u in done: continue
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (dortus-verkenner)"}),timeout=30)
        raw=r.read().decode("utf-8","replace")
    except Exception as e:
        out.write(json.dumps({"url":u,"fout":str(e)})+"\n"); out.flush(); time.sleep(1); continue
    rec={"url":u}
    m=re.search(r'decodeURIComponent\( "([^"]+)"',raw)
    if m:
        try:
            dl=json.loads(urllib.parse.unquote(m.group(1)))[0]
            rec["datum"]=dl.get("page_productDatePublished"); rec["type"]=dl.get("page_productType"); rec["prijs"]=dl.get("page_productPrice1")
        except Exception: pass
    m=re.search(r'wccom-comp-product-subscription-plan[^>]*data-props="([^"]+)"',raw)
    if m:
        t=html.unescape(m.group(1))
        for k in ["installations","numberOfReviews","rating","productName","vendorName","vendorId","developedByWoo","regularPrice","isFreemium","isSaaSProduct","hasExternalSubscription","isTheme","isPlugin","isRevShareProduct","versionDate","productCategory","isBusinessService"]:
            rec[k]=veld(t,k)
    out.write(json.dumps(rec)+"\n"); out.flush()
    time.sleep(0.3)
