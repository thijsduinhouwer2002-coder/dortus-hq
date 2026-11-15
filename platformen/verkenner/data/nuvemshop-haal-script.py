# Vera 15 nov 2026: alle apps uit sitemap-apps.xml van nuvemshop.com.br, per app de app-gegevens
# (id, createdAt, maker, reviews, prijs) en de getoonde reviews met datum. Gebruik: python3 -I script.py sitemap.xml uit.jsonl
import re,subprocess,sys,json,time
sm=open(sys.argv[1]).read()
urls=[u for u in re.findall(r'<loc>([^<]*)</loc>',sm) if '/loja-aplicativos-nuvem/' in u and '/categorias/' not in u]
seen=set()
try:
    for l in open(sys.argv[2]): seen.add(json.loads(l)['url'])
except FileNotFoundError: pass
out=open(sys.argv[2],'a')
def grab(t,key):
    i=t.find(key)
    if i<0: return None
    j=t.find('{',i); d=0
    for k in range(j,len(t)):
        if t[k]=='{': d+=1
        elif t[k]=='}':
            d-=1
            if d==0: return t[j:k+1]
for n,u in enumerate(urls):
    if u in seen: continue
    t=subprocess.run(["curl","-sL","--max-time","30",u],capture_output=True,text=True).stdout
    t=t.replace('\\"','"').replace('\\\\','\\')
    r={'url':u}
    a=grab(t,'{"app":{"id"')
    if a:
        a=a[len('{"app":'):] if a.startswith('{"app":') else a
    m=re.search(r'\{"app":(\{"id":\d+,"slug".*?"analytics":\{[^}]*\}\})',t)
    try:
        app=json.loads(m.group(1)); 
        for k in ['id','slug','name','developer','pricing','rating','installCount','createdAt','updatedAt','isNew','isFeatured','isPopular']: r[k]=app.get(k)
    except Exception as e: r['fout']=str(e)[:80]
    rv=re.search(r'"reviews":\{"reviews":(\[.*?\]),"total":(\d+)\}',t)
    if rv:
        try:
            lst=json.loads(rv.group(1)); r['rev_total']=int(rv.group(2))
            r['revs']=[(x.get('createdAt'),x.get('rating'),x.get('storeId')) for x in lst]
        except Exception as e: r['revfout']=str(e)[:80]
    out.write(json.dumps(r,ensure_ascii=False)+'\n'); out.flush()
    time.sleep(0.4)
    if n%50==0: print(n,flush=True)
print('klaar')
