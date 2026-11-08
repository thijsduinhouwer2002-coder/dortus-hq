"""Telt alle producten in cTrader Store (ctrader.com) via de sitemap en de openbare _next/data-JSON per product.
Per product: type, prijs, abonnement, gebruikers (userCount), beoordelingen, tags, verkoper, versiedatum.
Per verkoper (sellerCard): lid sinds, totalSales, totalFreeInstalls.
Gebruik: python3 -I data/ctrader-store-meet.py data/ctrader-store-<datum>.json   (±10 minuten, rustig: 3 tegelijk)
Noor, 8 nov 2026."""
import sys, re, json, time, urllib.request, concurrent.futures as cf
UA = {"User-Agent": "Mozilla/5.0 (onderzoek; alleen lezen)"}
def get(u, tries=3):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read().decode()
        except Exception as e:
            if i == tries - 1: return None
            time.sleep(2 + 3 * i)
out = sys.argv[1]
home = get("https://ctrader.com/")
build = re.search(r'"buildId":"([^"]+)"', home).group(1)
sm = get("https://ctrader.com/sitemap-store.xml")
ids = sorted({int(x) for x in re.findall(r"<loc>https://ctrader.com/products/(\d+)</loc>", sm)})
print("producten in sitemap:", len(ids), "buildId", build, flush=True)
def one(pid):
    t = get(f"https://ctrader.com/_next/data/{build}/en/products/{pid}.json?productId={pid}")
    time.sleep(0.15)
    if not t: return pid, None, None
    try:
        s = json.loads(t)["pageProps"]["initialState"]
    except Exception:
        return pid, None, None
    x = s["product"]["data"].get(str(pid))
    if not x: return pid, None, None
    keep = {k: x.get(k) for k in ["productId", "userId", "userNick", "type", "title", "updatedAt", "userCount", "labels", "hasTrial",
            "minSubscriptionPeriod", "minSubscriptionPrice", "status", "lastVersion", "lastVersionDate", "suitableForPropFirms",
            "pluginCategory", "indicatorCategory", "subscribersCount", "shortDescription"]}
    keep["price"] = (x.get("item") or {}).get("price"); keep["promoPrice"] = (x.get("item") or {}).get("promoPrice")
    keep["tags"] = [g["name"] for g in x.get("tagList") or []]
    rs = x.get("ratingSummary") or {}; keep["rating"] = rs.get("averageRating"); keep["reviews"] = rs.get("totalReviews")
    sc = (s.get("sellerCard") or {}).get("data") or {}
    seller = {k: sc.get(k) for k in ["sellerId", "nickName", "joinAt", "kycStatus", "totalFreeInstalls", "totalSales"]}
    return pid, keep, seller
prods, sellers, fail = [], {}, []
with cf.ThreadPoolExecutor(3) as ex:
    for n, (pid, p, sc) in enumerate(ex.map(one, ids)):
        if p: prods.append(p)
        else: fail.append(pid)
        if sc and sc.get("sellerId"): sellers[str(sc["sellerId"])] = sc
        if n % 500 == 0: print(n, len(prods), flush=True)
json.dump({"datum": time.strftime("%Y-%m-%d"), "producten": prods, "verkopers": sellers, "mislukt": fail}, open(out, "w"))
print("klaar:", len(prods), "producten,", len(sellers), "verkopers,", len(fail), "mislukt")
