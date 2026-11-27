import re, subprocess, json, sys, urllib.parse, time
def get(url):
    return subprocess.run(["curl","-s","-A","Mozilla/5.0","--max-time","40",url],capture_output=True,text=True).stdout
def field(h,label):
    m=re.search(r'product-info-label[^>]*>\s*'+label+r'.*?</td>\s*<td class="product-info-data[^"]*">(.*?)</td>',h,re.S)
    return re.sub(r'<[^>]+>|\s+',' ',m.group(1)).strip() if m else None
cache={}
try: cache=json.load(open('./pcache.json'))
except: pass
def prod(s):
    if s in cache: return cache[s]
    for t in range(3):
        h=get("https://superhivemarket.com/products/"+s)
        if 'product-info-label' in h: break
        time.sleep(4)
    d={"slug":s,"sales":field(h,"Sales"),"pub":field(h,"Published"),"bver":field(h,"Blender Version")}
    m=re.search(r'productData = (\{.*?\})',h)
    if m:
        try: j=json.loads(m.group(1)); d["price"]=j.get("price"); d["title"]=j.get("title")
        except: pass
    m=re.search(r'(\d+) ratings?\s*</a>',h); d["ratings"]=int(m.group(1)) if m else 0
    m=re.search(r'star-ratings">(.*?)</div>',h,re.S); d["stars"]=(m.group(1).count('fa fa-star"')+0.5*m.group(1).count('half')) if m else None
    cache[s]=d; return d
for term in sys.argv[1:]:
    q=urllib.parse.quote_plus(term)
    h=get(f"https://superhivemarket.com/search?search%5Bq%5D={q}&search%5Bcategory_id%5D=6&sort_sales=desc")
    sl=[]
    for s in re.findall(r'href="/products/([^"?/]+)\?search_id',h):
        if s not in sl: sl.append(s)
    print(f"\n### {term} ({len(sl)} op pagina 1)")
    for s in sl[:10]:
        d=prod(s); time.sleep(0.4)
        print(f"  {s[:42]:42} ${(d.get('price') or 0)/100:<7} {d.get('sales') or '-':>7} r{d.get('ratings')}/{d.get('stars')} {d.get('pub')} | {d.get('bver')}")
json.dump(cache,open('./pcache.json','w'))
