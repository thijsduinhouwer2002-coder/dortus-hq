# Haalt OpenCart-extensiepagina's op per extension_id en leest prijs, datum, sales, comments, maker.
# Gebruik: python3 opencart-haal-script.py START EIND UIT.jsonl
import re, html, json, sys, time, subprocess
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 DortusVerkenner"
def get(i):
    u=f"https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id={i}"
    for _ in range(3):
        r=subprocess.run(["curl","-sL","-m","30","-A",UA,u],capture_output=True)
        if r.returncode==0 and r.stdout: break
        time.sleep(2)
    s=r.stdout.decode('utf8','ignore')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    d={'id':i}
    m=re.search(r'Last Update (\d+ \w+ \d{4}) Created (\d+ \w+ \d{4}) (\d+) (Sales|Downloads) (\d+) Comments',t)
    if not m:
        m2=re.search(r'Created (\d+ \w+ \d{4})',t)
        d['ok']=False; d['created']=m2.group(1) if m2 else None
        return d
    d.update(ok=True,updated=m.group(1),created=m.group(2),count=int(m.group(3)),kind=m.group(4),comments=int(m.group(5)))
    p=re.search(r'Price (\$[\d,.]+|Free|FREE)',t); d['price']=p.group(1) if p else None
    if not p:
        p=re.search(r'(\$[\d,.]+) Developed by',t); d['price']=p.group(1) if p else ('Free' if re.search(r'\bDownload\b',t) else None)
    mk=re.search(r'Comments Share (.+?) Member since: (\d+ \w+ \d{4})',t)
    if mk: d['maker']=mk.group(1); d['member_since']=mk.group(2)
    ti=re.search(r'<title>(.*?)</title>',s,re.S); d['title']=html.unescape(ti.group(1).strip()) if ti else None
    dv=re.search(r'Developed by (.+?) (?:\d+ Months|Documentation|Rating)',t); d['dev']=dv.group(1) if dv else None
    return d
a,b,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
step=int(sys.argv[4]) if len(sys.argv)>4 else 1
with ThreadPoolExecutor(4) as ex, open(out,'a') as f:
    for d in ex.map(get,range(a,b,step)):
        f.write(json.dumps(d)+"\n"); f.flush()
