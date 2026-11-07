# Vera, 7 nov 2026. Haalt per add-on de vermelding op: gebruikers, aantal reviews,
# "Listing updated", prijsvorm, werkt met, en de datums van de reviews die op de pagina staan.
# Gebruik: python3 gwm-haal-script.py zoek.jsonl detail.jsonl
import re, sys, json, subprocess, concurrent.futures as cf, html
M="January February March April May June July August September October November December".split()
DT=r'((?:%s) \d{1,2}, 20\d\d)'%"|".join(M)
def iso(s):
    m,d,y=re.match(r'(\w+) (\d+), (\d+)',s).groups(); return "%s-%02d-%02d"%(y,M.index(m)+1,int(d))
def get(a):
    url="https://workspace.google.com/marketplace/app/%s/%s"%(a["slug"],a["id"])
    t=subprocess.run(["curl","-sL","-m","60",url],capture_output=True,text=True,errors="ignore").stdout
    t=re.sub(r'<style.*?</style>','',t,flags=re.S); t=re.sub(r'<script.*?</script>','',t,flags=re.S)
    x=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t)))
    r=dict(a)
    m=re.search(r'Listing updated: '+DT,x); r["bijgewerkt"]=iso(m.group(1)) if m else None
    m=re.search(r'Pricing (.*?) (?:code|Developer info)',x); r["prijs"]=m.group(1).strip()[:60] if m else None
    m=re.search(r'Works with: (.*?) (?:Average rating|Overview)',x); r["werkt"]=m.group(1)[:120] if m else None
    m=re.search(r'Average rating: [\d.]+ stars? ([\d,]+) info More details about user reviews ([\d,.KMB+]+)',x)
    if m: r["reviews"]=int(m.group(1).replace(",","")); r["gebruikers_exact"]=m.group(2)
    else:
        m=re.search(r'More details about user reviews ([\d,.KMB+]+)',x); r["gebruikers_exact"]=m.group(1) if m else None; r["reviews"]=0
    i=x.find(' Reviews ',x.find('Permissions'))
    r["review_datums"]=sorted(set(iso(d) for d in re.findall(DT,x[i:]))) if i>0 else []
    r["ok"]=len(x)>2000
    return r
rows=[json.loads(l) for l in open(sys.argv[1])]
with open(sys.argv[2],"w") as f, cf.ThreadPoolExecutor(12) as ex:
    for r in ex.map(get,rows): f.write(json.dumps(r,ensure_ascii=False)+"\n")
