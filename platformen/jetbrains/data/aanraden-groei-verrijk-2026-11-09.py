import csv,json,urllib.request,time,sys
rows=[r for r in csv.DictReader(open(sys.argv[1]),delimiter='\t') if r['groei'] not in ('None','') and int(r['groei'])>=30]
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=20))
        except Exception: time.sleep(2)
w=open(sys.argv[2],'w'); w.write("groei\tdownloads\tid\tnaam\tmaker\tmodel\tlaatste_versie\tlaatste_datum\tuntil\tsoorten\n")
for r in rows:
    d=get(f"https://plugins.jetbrains.com/api/plugins/{r['id']}") or {}
    u=get(f"https://plugins.jetbrains.com/api/plugins/{r['id']}/updates?size=1") or [{}]
    u=u[0] if u else {}
    v=(d.get('vendor') or {}).get('name','')
    m=d.get('pricingModel','')
    dt=time.strftime('%Y-%m-%d',time.gmtime(int(u.get('cdate') or 0)/1000)) if u.get('cdate') else ''
    w.write(f"{r['groei']}\t{r['downloads']}\t{r['id']}\t{r['naam']}\t{v}\t{m}\t{u.get('version','')}\t{dt}\t{u.get('until','')}\t{r['soorten']}\n")
    time.sleep(0.15)
w.close()
