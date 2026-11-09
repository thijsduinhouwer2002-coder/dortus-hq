# Leest productpagina's van de cTrader Store (uit sitemap-store.xml) en haalt de kerngegevens
# uit __NEXT_DATA__: soort, prijs, gebruikers (userCount), reviews, versie en datum, en de
# verkoperskaart (lid sinds, totalSales, totalFreeInstalls). Rustig: 1 pagina tegelijk.
# Gebruik: python3 -I ctrader-pagina-script.py ids.txt uit.jsonl
import json, re, sys, time, subprocess
ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
uit = open(sys.argv[2], "a")
for pid in ids:
    r = subprocess.run(["curl", "-sS", "-m", "60", "-A", "DortusVerkenner/1.0",
                        f"https://ctrader.com/products/{pid}"], capture_output=True, text=True)
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.stdout, re.S)
    rec = {"id": int(pid)}
    if m:
        try:
            st = json.loads(m.group(1))["props"]["pageProps"]["initialState"]
            p = st["product"]["data"].get(pid, {})
            s = st.get("sellerCard", {}).get("data", {}) or {}
            it = p.get("item") or {}
            rec.update({
                "titel": p.get("title"), "soort": p.get("type"), "status": p.get("status"),
                "prijs": it.get("price"), "promo": it.get("promoPrice"), "proef": p.get("hasTrial"),
                "abonnees": p.get("subscribersCount"), "abo": p.get("minSubscriptionPrice"),
                "gebruikers": p.get("userCount"), "reviews": (p.get("ratingSummary") or {}).get("totalReviews"),
                "rating": (p.get("ratingSummary") or {}).get("averageRating"),
                "versie": p.get("lastVersion"), "versiedatum": p.get("lastVersionDate"), "bijgewerkt": p.get("updatedAt"),
                "maker": p.get("userNick"), "maker_id": p.get("userId"),
                "maker_sinds": s.get("joinAt"), "maker_verkopen": s.get("totalSales"),
                "maker_gratis_installs": s.get("totalFreeInstalls"), "maker_kyc": s.get("kycStatus"),
            })
        except Exception as e:
            rec["fout"] = str(e)[:100]
    else:
        rec["fout"] = "geen data"
    uit.write(json.dumps(rec) + "\n"); uit.flush()
    time.sleep(1)
