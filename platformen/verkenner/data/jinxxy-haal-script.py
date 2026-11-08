# Jinxxy (VRChat-avatarwinkel): productpagina's uit de sitemap, haal created_at, like_count, sales_count, categorie, prijs.
# Gebruik: python3 jinxxy-haal-script.py urls UIT.txt   (alle product-URL's uit de sitemaps)
#          python3 jinxxy-haal-script.py haal URLS.txt UIT.jsonl N SEED   (willekeurige steekproef van N)
import sys,re,json,random,subprocess,time
from concurrent.futures import ThreadPoolExecutor
UA="DortusVerkenner/1.0 (+https://dortus.com)"
def get(u):
    r=subprocess.run(["curl","-sSL","-m","40","-A",UA,u],capture_output=True)
    return r.stdout.decode('utf-8','replace')
if sys.argv[1]=='urls':
    idx=get("https://jinxxy.com/sitemap.xml"); sms=re.findall(r'<loc>([^<]+)',idx); out=[]
    for s in sms:
        for u in re.findall(r'<loc>([^<]+)',get(s)):
            p=u.split('jinxxy.com/')[-1].split('?')[0].split('/')
            if len(p)==2 and p[0] not in('market','about','legal','help','blog') and p[1]: out.append(u)
        time.sleep(0.3)
    open(sys.argv[2],'w').write("\n".join(out)); print(len(sms),len(out))
else:
    urls=[u.strip().replace('&amp;','&') for u in open(sys.argv[2]).read().splitlines() if u.strip()]; random.seed(int(sys.argv[5])); smp=random.sample(urls,int(sys.argv[4]))
    def one(u):
        h=get(u).replace('\\"','"')
        def f(k,pat=r'("[^"]*"|[-0-9.]+|null)'):
            m=re.search('"'+k+'":'+pat,h); return json.loads(m.group(1)) if m else None
        return {'url':u,'ok':'created_at' in h,'created':f('created_at'),'likes':f('like_count'),'sales':f('sales_count'),
                'cat':f('category'),'base':f('base_price'),'cur':f('currency_code'),'ai':f('generative_ai_disclosure'),
                'prices':[int(x) for x in re.findall(r'"PublicProductVersion","id":"[0-9]+","name":"(?:[^"\\]|\\.)*","description":"(?:[^"\\]|\\.)*","price":([0-9]+)',h)]}
    with ThreadPoolExecutor(4) as ex, open(sys.argv[3],'a') as fo:
        for d in ex.map(one,smp): fo.write(json.dumps(d)+"\n"); fo.flush()
