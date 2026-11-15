import re,sys,subprocess,time,csv,random
def get(url):
    r=subprocess.run(['curl','-sS','-m','30','-A','Mozilla/5.0',url],capture_output=True,text=True,errors='ignore')
    return r.stdout
def parse(url,h):
    g=lambda p:(re.search(p,h,re.S).group(1).strip() if re.search(p,h,re.S) else '')
    return dict(url=url,sku=url.rsplit('/',1)[-1],
      datum=g(r'DC\.Date\.issued"[^>]*content="([^"]+)"'),
      soort=g(r'Product Type</dt>\s*<dd[^>]*>\s*([^<]+)'),
      reviews=g(r'"reviewCount":\s*"?(\d+)'),
      rating=g(r'"ratingValue":\s*"?([\d.]+)'),
      prijs=g(r'"price":\s*"([\d.]+)"'),
      uitgever=g(r'name="DC.Publisher" content="([^"]*)"') or g(r'"publisher":\s*\{\s*"@type":\s*"Organization",\s*"name":\s*"([^"]+)"'))
if __name__=='__main__':
    urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
    out=sys.argv[2]; w=None
    with open(out,'w',newline='') as f:
        for u in urls:
            d=parse(u,get(u))
            if w is None: w=csv.DictWriter(f,fieldnames=list(d)); w.writeheader()
            w.writerow(d); f.flush(); time.sleep(0.7)
