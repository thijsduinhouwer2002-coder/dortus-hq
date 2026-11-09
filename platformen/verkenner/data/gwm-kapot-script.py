# Vera, 9 nov 2026. Productkans Google Workspace: haalt van alle add-ons met 100K+ gebruikers
# de vermelding opnieuw op en telt reviews uit 2026 die zeggen dat de add-on niet (meer) werkt,
# en reviews die over betalen gaan. Gebruik: python3 -I gwm-kapot-script.py gwm-detail-2026-11-07.jsonl uit.jsonl
import re, sys, json, subprocess, html, concurrent.futures as cf
M="January|February|March|April|May|June|July|August|September|October|November|December"
MM=M.split("|")
KAPOT=re.compile(r"stopp?ed working|not working|doesn'?t work|does not work|no longer work|isn'?t working|broken|only (?:option|shows?).{0,20}help|stopped functioning|won'?t (?:open|load|work)",re.I)
BETAAL=re.compile(r"\bpaid\b|\bpay\b|subscription|refund|\$\d|premium|purchase|bought",re.I)
def n(s):
    if not s: return 0
    s=s.replace('+','').replace(',',''); m={'K':1e3,'M':1e6}
    return float(s[:-1])*m[s[-1]] if s[-1] in m else float(s)
def get(r):
    url="https://workspace.google.com/marketplace/app/%s/%s"%(r["slug"],r["id"])
    t=subprocess.run(["curl","-sL","-m","40","-H","Accept-Language: en",url],capture_output=True,text=True,errors="ignore").stdout
    t=re.sub(r'<style.*?</style>','',t,flags=re.S); t=re.sub(r'<script.*?</script>','',t,flags=re.S)
    x=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t)))
    i=x.find('Learn more about reviews open_in_new'); revs=[]
    if i>0:
        p=re.split(r'((?:%s) \d{1,2}, 20\d\d) more_vert Options Report review'%M,x[i+36:])
        for k in range(1,len(p)-1,2):
            m,d,y=re.match(r'(\w+) (\d+), (\d+)',p[k]).groups()
            txt=p[k+1].split('Is this review helpful')[0].strip()[:400]
            revs.append({"d":"%s-%02d-%02d"%(y,MM.index(m)+1,int(d)),"t":txt})
    o={k:r.get(k) for k in ("slug","id","naam","maker","ster","reviews","bijgewerkt","prijs")}
    o["u"]=n(r.get("gebruikers_exact") or r.get("gebruikers")); o["revs"]=revs; o["ok"]=len(x)>2000
    r26=[v for v in revs if v["d"]>="2026-01-01"]
    o["n2026"]=len(r26); o["kapot2026"]=sum(1 for v in r26 if KAPOT.search(v["t"])); o["betaal"]=sum(1 for v in revs if BETAAL.search(v["t"]))
    return o
rows=[json.loads(l) for l in open(sys.argv[1])]
rows=[r for r in rows if n(r.get("gebruikers_exact") or r.get("gebruikers"))>=100000]
with open(sys.argv[2],"w") as f, cf.ThreadPoolExecutor(6) as ex:
    for o in ex.map(get,rows): f.write(json.dumps(o,ensure_ascii=False)+"\n"); f.flush()
