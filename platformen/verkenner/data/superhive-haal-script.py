# Haalt Superhive-productpagina's op (uit de sitemap) en schrijft per product: id, soort, verkopen, gepubliceerd, prijs.
# Gebruik: python3 -I superhive-haal-script.py urls.txt uit.jsonl  (hervat: slaat urls over die al in uit.jsonl staan)
import sys, re, json, html, subprocess, concurrent.futures as cf, os
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
out=sys.argv[2]
done=set()
if os.path.exists(out):
    for l in open(out):
        try:
            j=json.loads(l)
            if j['code']=='200': done.add(j['url'])
        except: pass
def get(u):
  import time
  for poging in range(6):
    d=get1(u)
    if d['code']!='429': return d
    time.sleep(5*(poging+1))
  return d
def get1(u):
    r=subprocess.run(['curl','-sL','--max-time','30','-A','Mozilla/5.0 (dortus-verkenner)','-w','\n%{http_code}',u],capture_output=True,text=True)
    s,code=r.stdout.rsplit('\n',1)
    d={'url':u,'code':code}
    if code!='200': return d
    def info(lbl):
        m=re.search(r'product-info-label[^>]*>\s*'+lbl+r'\s*</td>\s*<td class="product-info-data">(.*?)</td>',s,re.S)
        return html.unescape(re.sub(r'<[^>]+>','',m.group(1))).strip() if m else None
    d['sales']=info('Sales'); d['published']=info('Published')
    m=re.search(r'"mpn":"(\d+)"',s); d['id']=int(m.group(1)) if m else None
    m=re.search(r'"price":"([\d.]+)"',s); d['price']=float(m.group(1)) if m else None
    m=re.search(r'BLENDER [A-Z ]+(?:·[^<]*)?',s); d['soort']=html.unescape(m.group(0)).strip() if m else None
    m=re.search(r'"seller":\{"@type":"[A-Za-z]+","name":"([^"]*)"',s); d['maker']=m.group(1) if m else None
    c=re.findall(r'href="/categories/([^"]*)"',s)
    d['cat']=[x for x in set(c) if c.count(x)==1]
    m=re.search(r'"reviewCount":"?(\d+)',s); d['reviews']=int(m.group(1)) if m else 0
    return d
todo=[u for u in urls if u not in done]
with open(out,'a') as f, cf.ThreadPoolExecutor(3) as ex:
    for i,d in enumerate(ex.map(get,todo)):
        f.write(json.dumps(d)+'\n')
        if i%500==0: print(i,len(todo),flush=True); f.flush()
