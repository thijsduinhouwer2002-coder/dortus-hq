# Leest productpagina's van de Unity Asset Store (sitemap + pagina, geen sleutel).
# Versie 2 (6 nov 22:31): leest de paginadata als JSON (ReactDOMrender(...)) en pakt
# alleen het product met het id uit de URL (data.ENTITY.Product[id]). Zo kan het niet
# meer de cijfers van een ander product op de pagina pakken (fout uit versie 1).
# Velden: rating.count = aantal sterbeoordelingen, reviewCount = geschreven reviews.
# Gebruik: python3 -I unity-haal-script.py <urls.txt> <uitvoer.json>
import json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
DEC = json.JSONDecoder()

def lees(u):
    pid = u.rsplit("-", 1)[1]
    for k in range(3):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "dortus-verkenner"})
            t = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
            i = t.find("ReactDOMrender(")
            if i < 0:
                return {"url": u, "id": pid, "fout": "geen data"}
            d, _ = DEC.raw_decode(t, i + len("ReactDOMrender("))
            E = d["data"]["ENTITY"]
            p = E.get("Product", {}).get(pid)
            if not p:
                return {"url": u, "id": pid, "fout": "product niet in data"}
            pubid = (p.get("publisher") or {}).get("id", [None, None])[1]
            pub = E.get("ProductPublisher", {}).get(pubid, {}) if pubid else {}
            catid = (p.get("category") or {}).get("id", [None, None])[1]
            cat = E.get("Category", {}).get(catid, {}) if catid else {}
            pr = p.get("originalPrice") or {}
            r = p.get("rating") or {}
            return {"url": u, "id": pid, "naam": p.get("name"),
                    "eerst": p.get("firstPublishedDate"),
                    "beoordelingen": r.get("count"), "gemiddeld": r.get("average"),
                    "reviews": p.get("reviewCount"),
                    "prijs": pr.get("originalPrice"), "vrij": pr.get("isFree"),
                    "uitgever_id": pubid, "uitgever": pub.get("name"),
                    "categorie": cat.get("name") or catid,
                    "hotness": p.get("packageInListHotness"), "staat": p.get("state")}
        except Exception as e:
            err = str(e)
            time.sleep(3)
    return {"url": u, "id": pid, "fout": err}

with ThreadPoolExecutor(8) as ex:
    out = list(ex.map(lees, urls))
json.dump(out, open(sys.argv[2], "w"))
print("klaar", len(out), "fouten", sum(1 for o in out if o.get("fout")))
