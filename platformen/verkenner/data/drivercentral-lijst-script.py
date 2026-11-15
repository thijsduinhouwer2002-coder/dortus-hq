import re,subprocess,time,sys,json
plats=['control4-drivers','crestron-drivers','rti-drivers','urc-drivers','nice-drivers']
out=open(sys.argv[1],'w'); seen=set()
def get(u):
    return subprocess.run(['curl','-s','--max-time','30',u],capture_output=True,text=True,errors='ignore').stdout
for p in plats:
    n=1; leeg=0
    while True:
        u=f'https://drivercentral.io/platforms/{p}/'+(f'page-{n}/' if n>1 else '')+'?sort_by=timestamp&sort_order=desc'
        h=get(u); time.sleep(1.2)
        links=set(re.findall(r'href="(https://drivercentral.io/platforms/'+p+r'/(?:[a-z0-9-]+/)?[a-z0-9-]+/)"',h))
        links={l for l in links if not re.search(r'/page-\d+/$',l)}
        nieuw=links-seen
        # categorie-links eruit: die eindigen op cat/ en hebben 1 niveau; producten soms ook 1 niveau, filter later
        for l in sorted(nieuw): out.write(json.dumps({'platform':p,'url':l,'pagina':n})+'\n'); seen.add(l)
        out.flush()
        print(p,n,len(links),len(nieuw),file=sys.stderr)
        if not nieuw: leeg+=1
        else: leeg=0
        if leeg>=2 or n>200: break
        n+=1
