import re,subprocess,time,json
cats="canais-de-vendas comunicacao dropshipping estatisticas gestao logistica marketing pagamentos recursos-extras seguranca".split()
apps={}
for c in cats:
    p=1; maxp=1
    while p<=maxp:
        u=f"https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/{c}?page={p}"
        t=subprocess.run(["curl","-sL","--max-time","30",u],capture_output=True,text=True).stdout
        ps=[int(x) for x in re.findall(rf'categorias/{c}\?page=(\d+)',t)]
        if ps: maxp=max(maxp,max(ps))
        for s in re.findall(r'href="/loja-aplicativos-nuvem/(?!categorias)([a-z0-9-]+)"',t):
            apps.setdefault(s,set()).add(c)
        p+=1; time.sleep(0.7)
    print(c,maxp,len(apps),flush=True)
json.dump({k:sorted(v) for k,v in apps.items()},open('./nv_apps.json','w'))
