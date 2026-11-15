# Haalt per Poki-spelpagina (uit de sitemap) naam, maker, datePublished, ratingCount en ratingValue uit de JSON-LD.
# Gebruik: python3 poki-haal-script.py urls.txt uit.csv
import sys, re, csv, time, json, subprocess
from concurrent.futures import ThreadPoolExecutor
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
def get(u):
    time.sleep(0.4)
    h=subprocess.run(["curl","-s","-m","30",u],capture_output=True,text=True).stdout
    def f(p):
        m=re.search(p,h); return m.group(1) if m else ""
    return [u.rsplit("/",1)[-1], f(r'"author":\{"@type":"[^"]*","name":"([^"]*)"'), f(r'"datePublished":"([^"]*)"'),
            f(r'"dateModified":"([^"]*)"'), f(r'"ratingCount":(\d+)'), f(r'"ratingValue":([\d.]+)')]
with ThreadPoolExecutor(3) as ex: rows=list(ex.map(get,urls))
w=csv.writer(open(sys.argv[2],"w")); w.writerow(["slug","maker","gepubliceerd","gewijzigd","stemmen","score"]); w.writerows(rows)
