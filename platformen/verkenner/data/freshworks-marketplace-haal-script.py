# Vera 16 nov 2026: leest alle apppagina's uit de sitemap van de Freshworks Marketplace (robots.txt staat alles toe)
# en haalt uit window.__NUXT__ (getAppDetails-<naam>) naam, extension_id (oplopend nummer, maat voor leeftijd), app_version, published_at (datum van de laatste versie), install_count, ratings, pricing, bron.
# Gebruik: python3 -I freshworks-marketplace-haal-script.py uit.jsonl   (4 tegelijk, rustig)
# Let op: het veld "developer" blijft leeg; de maker staat in "account" (ook via de open API https://www.freshworks.com/apps/api/app/<naam>). Er is geen aanmaakdatum; gebruik extension_id als leeftijdsmaat (loopt op met de tijd).
import re,sys,json,urllib.request,concurrent.futures as cf,time
UA={"User-Agent":"dortus-verkenner"}
def get(u):
    for _ in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read().decode('utf8','replace')
        except Exception as e: err=e; time.sleep(3)
    return ""
def parse(t):
    m=re.search(r'window\.__NUXT__=\(function\(([^)]*)\)\{',t)
    if not m: return None,None
    params=m.group(1).split(',');end=t.find('</script>',m.end());body=t[m.end():end]
    i=body.rfind('}(');args=body[i+2:].rstrip(';').rstrip(')');toks=[];j=0
    while j<len(args):
        c=args[j]
        if c in ', ': j+=1;continue
        if c=='"':
            k=j+1
            while args[k]!='"': k+=2 if args[k]=='\\' else 1
            toks.append(json.loads(args[j:k+1]));j=k+1
        else:
            k=j
            while k<len(args) and args[k]!=',': k+=1
            w=args[j:k].strip();v={'true':True,'false':False,'null':None,'void 0':None}.get(w,w)
            if isinstance(v,str):
                try: v=float(w) if '.' in w or 'e' in w else int(w)
                except: pass
            toks.append(v);j=k
    return dict(zip(params,toks)),body[:i]
def val(env,s):
    s=s.strip()
    if s.startswith('"'): return json.loads(s)
    return env.get(s,s)
def one(u):
    t=get(u if u.endswith('/') else u+'/')
    env,body=parse(t)
    if not body: return {"url":u,"fout":True}
    i=body.find('"getAppDetails-')
    if i<0: return {"url":u,"geen_app":True}
    seg=body[i:i+20000]
    r={"url":u}
    for k in ["name","display_name","extension_id","app_version","published_at","install_count","ratings_count","rating","pricing","subscription_type","type","uses_gen_ai"]:
        m=re.search(r'[{,]'+k+r':("(?:[^"\\]|\\.)*"|[^,}\]]+)',seg)
        r[k]=val(env,m.group(1)) if m else None
    m=re.search(r'listable:\{[^}]*source:("?[^,}"]+"?)',seg); r["source"]=val(env,m.group(1)) if m else None
    m=re.search(r'skus:\[([^\]]*)\]',seg); r["skus"]=[val(env,x) for x in m.group(1).split(',')] if m else None
    m=re.search(r'developer[a-z_]*:\{[^}]*?name:("(?:[^"\\]|\\.)*"|[^,}]+)',seg); r["developer"]=val(env,m.group(1)) if m else None
    return r
sm=get("https://www.freshworks.com/apps/sitemap.xml")
urls=[u for u in re.findall(r'<loc>([^<]+)',sm) if u.rstrip('/')!="https://www.freshworks.com/apps"]
if len(sys.argv)>2: urls=urls[:int(sys.argv[2])]
with open(sys.argv[1],"w") as f, cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(one,urls): f.write(json.dumps(r,ensure_ascii=False)+"\n")
print(len(urls),"pagina's")
