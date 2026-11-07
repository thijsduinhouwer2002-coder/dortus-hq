# Leest Gumroad-productpagina's (gewone curl) en haalt naam, prijs, sales_count (alleen als de maker hem toont), aantal ratings, maker
import subprocess,re,json,sys,html,random,concurrent.futures as cf
us=re.findall(r'<loc>([^<]*)</loc>',open(sys.argv[1]).read())
random.seed(7);us=random.sample(us,int(sys.argv[3]))
def g(u):
    s=subprocess.run(['curl','-sL','--max-time','25',u],capture_output=True,text=True).stdout
    m=re.search(r'data-page="([^"]*)"',s)
    if not m: return dict(url=u,ok=False)
    try: p=json.loads(html.unescape(m[1]))['props']['product']
    except Exception: return dict(url=u,ok=False)
    return dict(url=u,ok=True,name=p.get('name'),price=p.get('price_cents'),sales=p.get('sales_count'),ratings=(p.get('ratings') or {}).get('count'),seller=(p.get('seller') or {}).get('name'))
with cf.ThreadPoolExecutor(12) as ex: out=list(ex.map(g,us))
json.dump(out,open(sys.argv[2],'w'),indent=0);print(len(out),sum(x['ok'] for x in out))
