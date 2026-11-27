import re, subprocess, json, sys, html as H, concurrent.futures as cf
def get(url):
    return subprocess.run(["curl","-s","-A","Mozilla/5.0","--max-time","40",url],capture_output=True,text=True).stdout
def field(h,label):
    m=re.search(r'product-info-label[^>]*>\s*'+label+r'.*?</td>\s*<td class="product-info-data[^"]*">(.*?)</td>',h,re.S)
    return re.sub(r'<[^>]+>|\s+',' ',m.group(1)).strip() if m else None
def prod(s):
    h=get("https://superhivemarket.com/products/"+s)
    d={"slug":s}
    m=re.search(r'productData = (\{.*?\})',h)
    if m:
        try: d.update(json.loads(m.group(1)))
        except: pass
    d["sales"]=field(h,"Sales")
    d["published"]=field(h,"Published")
    d["bver"]=field(h,"Blender Version")
    m=re.search(r'star-ratings">(.*?)</div>\s*<a[^>]*>\s*(\d+) ratings?',h,re.S)
    if m:
        d["ratings"]=int(m.group(2)); d["stars_full"]=m.group(1).count('fa fa-star"')+0; d["stars_html"]=re.sub(r'\s','',m.group(1))[:300]
    cats=re.findall(r'href="/categories/([a-z0-9-]+)"',h)
    d["cats"]=sorted(set(cats))
    m=re.search(r'<meta name="description" content="([^"]*)"',h)
    d["desc"]=H.unescape(m.group(1))[:300] if m else None
    m=re.search(r'href="/creators/([^"]+)"',h); d["creator"]=m.group(1) if m else None
    return d
order=json.load(open(sys.argv[1]))
res=[]
with cf.ThreadPoolExecutor(1) as ex:
    for d in ex.map(prod,order): res.append(d)
with open(sys.argv[2],"w") as f:
    for d in res: f.write(json.dumps(d)+"\n")
print(len(res))
