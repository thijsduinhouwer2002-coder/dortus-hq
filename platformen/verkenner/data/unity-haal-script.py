# Leest productpagina's van de Unity Asset Store (sitemap + pagina, geen sleutel).
# LET OP (6 nov 21:31): de regex pakt het EERSTE reviewCount en firstPublishedDate op de pagina. Dat is soms een ander product (bijvoorbeeld lcloud-for-playmaker-2 kreeg de 645 reviews van Playmaker 2). Eerst ombouwen: lees het blok van het product met het id uit de URL. Uitkomsten van deze versie niet gebruiken.
# Gebruik: python3 -I unity-haal-script.py <urls.txt> <uitvoer.json>
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
def f(rx, t):
    m = re.search(rx, t); return m.group(1) if m else None
def get(u):
    for k in range(3):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"dortus-verkenner"}), timeout=40).read().decode("utf-8","replace")
            pid = u.rsplit("-",1)[1]
            return {"url":u,"id":pid,"eerst":f(r'firstPublishedDate":"([^"]+)"',t),"reviews":f(r'"reviewCount":(\d+)',t),
                    "rating":f(r'"rating":\{"average":(\d+),"count":(\d+)',t) and re.search(r'"rating":\{"average":(\d+),"count":(\d+)',t).groups(),
                    "prijs":f(r'"finalPrice":"([^"]+)"',t),"vrij":f(r'"isFree":(true|false)',t),
                    "uitgever":f(r'"ProductPublisher":\{"(\d+)"',t),"uitgevernaam":f(r'"ProductPublisher":\{"\d+":\{"id":"\d+","name":"([^"]+)"',t)}
        except Exception as e:
            time.sleep(3)
    return {"url":u,"fout":True}
with ThreadPoolExecutor(6) as ex: out = list(ex.map(get, urls))
json.dump(out, open(sys.argv[2],"w"))
print("klaar", len(out), "fouten", sum(1 for o in out if o.get("fout")))
