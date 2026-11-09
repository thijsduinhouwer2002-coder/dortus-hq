# Vera 9 nov 2026: alle add-ons van Superhive van de laatste ±14 maanden (lijst op datum, nieuwste eerst),
# per product: titel, korte beschrijving, verkoopteller, publicatie, prijs, subcategorie, Blender-versie, reviews.
# Gebruik: python3 -I superhive-nieuwe-addons-script.py <paginas> uit.jsonl
import re,sys,json,subprocess,time,html,concurrent.futures as cf
P=int(sys.argv[1]); out=sys.argv[2]
UA='Mozilla/5.0 (dortus-verkenner)'
def curl(u):
    for poging in range(5):
        r=subprocess.run(['curl','-sL','--max-time','30','-A',UA,'-w','\n%{http_code}',u],capture_output=True,text=True)
        s,code=r.stdout.rsplit('\n',1) if '\n' in r.stdout else ('',r.stdout)
        if code!='429': return s,code
        time.sleep(5*(poging+1))
    return s,code
links=[]
for p in range(1,P+1):
    t,_=curl(f'https://superhivemarket.com/categories/addons/browse?sort_date=desc&page={p}')
    for l in re.findall(r'href="/products/([^"?/]+)"',t):
        if l not in links: links.append(l)
    time.sleep(0.3)
print('links',len(links),flush=True)
def txt(h): return re.sub(r'\s+',' ',re.sub('<[^>]+>','|',h))
def info(slug):
    t,code=curl('https://superhivemarket.com/products/'+slug)
    d={'slug':slug,'code':code}
    if code!='200': return d
    s=txt(t)
    def na(lbl,n=120):
        i=s.find('|'+lbl+'|')
        if i<0: return None
        return re.sub(r'\|+','|',s[i+len(lbl)+2:i+len(lbl)+2+n]).strip('| ').split('|')[0].strip()
    d['sales']=na('Sales',20); d['published']=na('Published',40); d['blender']=na('Blender Version',80)
    # let op: de pagina heeft eerst "price":1499 (centen) en later "price":"14.99" (dollars); hier de dollars
    m=re.search(r'"price"\s*:\s*"([\d.]+)"',t); d['prijs']=float(m.group(1)) if m else None
    m=re.search(r'<title>(.*?)</title>',t,re.S); d['titel']=html.unescape(m.group(1)).strip() if m else None
    m=re.search(r'<meta name="description" content="([^"]*)"',t); d['beschrijving']=html.unescape(m.group(1))[:300] if m else None
    m=re.search(r'"seller":\{"@type":"[A-Za-z]+","name":"([^"]*)"',t); d['maker']=m.group(1) if m else None
    c=re.findall(r'href="/categories/([^"]*)"',t); d['cat']=[x for x in set(c) if c.count(x)==1]
    m=re.search(r'"reviewCount":"?(\d+)',t); d['reviews']=int(m.group(1)) if m else 0
    return d
with cf.ThreadPoolExecutor(3) as ex, open(out,'w') as f:
    for i,r in enumerate(ex.map(info,links)):
        f.write(json.dumps(r)+'\n')
        if i%300==0: print(i,flush=True); f.flush()
