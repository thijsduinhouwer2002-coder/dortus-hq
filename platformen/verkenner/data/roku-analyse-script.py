#!/usr/bin/env python3
import json, os, statistics, collections, datetime
OUT = os.path.dirname(os.path.abspath(__file__))
L = [json.loads(l) for l in open(f"{OUT}/list.jsonl")]
uniq = {}
for x in L: uniq.setdefault(x["id"], x)
paid = lambda p: p not in ("", "0", None, "Free")
print("lijst uniek", len(uniq), "betaald (lijstprijs)", sum(paid(x["price"]) for x in uniq.values()))
print("lijstprijzen", collections.Counter(x["price"] for x in uniq.values() if paid(x["price"])).most_common(12))
print("payment", collections.Counter(x.get("payment") for x in uniq.values()).most_common())

D = {}
for l in open(f"{OUT}/details.jsonl"):
    r = json.loads(l); D[r["id"]] = r
D = list(D.values())
print("\ndetails", len(D))
now = datetime.datetime(2026, 11, 13)
def age_m(r):
    d = r.get("publishedDate") or r.get("createdDate")
    if not d: return None
    return (now - datetime.datetime.fromisoformat(d[:19])).days / 30.4
def stats(rows, label):
    c = [r["ratingCount"] or 0 for r in rows]
    if not c: print(label, "geen"); return
    print(f"{label}: n={len(c)} mediaan={statistics.median(c)} gem={round(sum(c)/len(c))} "
          f"10+={round(100*sum(x>=10 for x in c)/len(c))}% 100+={round(100*sum(x>=100 for x in c)/len(c))}% 0={round(100*sum(x==0 for x in c)/len(c))}%")
isp = lambda r: (r.get("priceAsNumber") or 0) > 0
P = [r for r in D if isp(r)]; F = [r for r in D if not isp(r)]
stats(D, "alles"); stats(P, "betaald"); stats(F, "gratis")
for lo, hi in [(0, 3), (3, 12), (12, 36), (36, 999)]:
    sub = [r for r in D if age_m(r) is not None and lo <= age_m(r) < hi]
    stats([r for r in sub if isp(r)], f"betaald {lo}-{hi} mnd")
    stats([r for r in sub if not isp(r)], f"gratis {lo}-{hi} mnd")
kw = ["screensaver", "theme", "aquarium", "fireplace", "wallpaper"]
stats([r for r in D if any(k in (r["name"] or "").lower() for k in kw)], "screensaver/thema (naam)")
stats([r for r in D if "Games" in r["categories"]], "categorie Games")
stats([r for r in P if "Games" in r["categories"]], "betaald Games")
print("prijzen detail", collections.Counter(r["price"] for r in P).most_common(10))
print("revenue", collections.Counter(r["revenueSources"] for r in D).most_common(8))
print("IAP", sum(1 for r in D if r["isInAppPurchaseOffered"]))
# makers in lijst? lijst heeft geen maker; maker uit details
dev = collections.Counter(r["developer"] for r in D)
print("\nmakers met meeste kanalen in detail-steekproef:", dev.most_common(15))
print("\ntop betaalde kanalen op aantal beoordelingen:")
for r in sorted(P, key=lambda r: -(r["ratingCount"] or 0))[:25]:
    print(f"  {r['ratingCount']:>6} sterren={r['starRating']} score={r['rating']} {r['price']:>6} {r['name'][:45]!r} | {r['developer']} | pub {str(r['publishedDate'])[:10]} | {','.join(r['categories'])[:40]}")
