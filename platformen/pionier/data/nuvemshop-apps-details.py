import re,subprocess,time,json,html
apps=json.load(open('./nv_apps.json'))
out=[]
for i,(s,cats) in enumerate(apps.items()):
    t=subprocess.run(["curl","-sL","--max-time","25",f"https://www.nuvemshop.com.br/loja-aplicativos-nuvem/{s}"],capture_output=True,text=True).stdout
    rc=re.search(r'"reviewCount":(\d+)',t); rv=re.search(r'"ratingValue":([\d.]+)',t)
    x=' '.join(re.sub('<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)).split())
    x=html.unescape(x)
    m=re.search(r'Preços (.{0,40}?) Classifica',x) or re.search(r'Preços (.{0,40}?) (Instalar|Desenvolvedor)',x)
    d=re.search(r'Desenvolvedor (.{1,60}?) Forma de acesso',x)
    out.append(dict(slug=s,cats=cats,reviews=int(rc.group(1)) if rc else 0,rating=float(rv.group(1)) if rv else None,prijs=m.group(1) if m else None,maker=d.group(1) if d else None))
    time.sleep(0.3)
    if i%100==0: print(i,flush=True)
json.dump(out,open('./nv_details.json','w'),ensure_ascii=False)
print('klaar',len(out))
