# Vera 17 nov 2026: zoekt in de Chrome Web Store en geeft per resultaat id, naam, gebruikers, sterren, in-app en datum bijgewerkt (JSON per regel).
# Gebruik: python3 -I chrome-zoek-ids-script.py "zoekterm 1" "zoekterm 2" > uit.jsonl
import re, subprocess, sys, time, urllib.parse, json
def haal(url):
    return subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
def getal(t): return int(t.replace(',','')) if t else 0
seen={}
out=[]
for zoek in sys.argv[1:]:
    h=haal('https://chromewebstore.google.com/search/'+urllib.parse.quote(zoek)+'?hl=en')
    paden=[]
    for p in re.findall(r'detail/[a-z0-9-]*/[a-p]{32}',h):
        if p not in paden: paden.append(p)
    for rank,p in enumerate(paden[:10],1):
        i=p[-32:]
        if i not in seen:
            time.sleep(1)
            d=haal('https://chromewebstore.google.com/'+p+'?hl=en')
            n=re.search(r'<title>([^<]*?) - Chrome Web Store',d)
            u=re.search(r'>([\d,]+) users?<',d)
            s=re.search(r'([\d.]+) out of 5',d)
            a=re.search(r'>?([\d,.K]+) ratings?<',d)
            up=re.search(r'Updated</div><div[^>]*>([^<]+)<',d)
            seen[i]=dict(id=i,naam=(n.group(1) if n else p)[:60],users=getal(u.group(1)) if u else 0,ster=s.group(1) if s else '-',beoord=a.group(1) if a else '0',iap='in-app purchases' in d,upd=up.group(1) if up else '')
        r=dict(seen[i]);r['zoek']=zoek;r['rank']=rank;out.append(r)
        print(json.dumps(r),flush=True)
