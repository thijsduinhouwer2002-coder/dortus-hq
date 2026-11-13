#!/usr/bin/env python3
"""Roku Channel Store meting. Alleen lezen, hooguit 2 verzoeken per seconde."""
import json, subprocess, sys, time, urllib.parse, os

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://channelstore.roku.com"
LOC = "country=US&language=en"
last = [0.0]

def get(url):
    wait = 0.55 - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    last[0] = time.time()
    r = subprocess.run(["curl", "-sS", "-m", "30", url], capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except Exception:
        return None

def listing(phase_deadline):
    seen = {}
    cats = json.load(open(f"{OUT}/raw/categories.json"))
    tagcats = [c for c in cats if c["categoryType"] == "tag"]
    counts = {}
    f = open(f"{OUT}/list.jsonl", "a")
    # 1. categorieen volledig doorbladeren (zolang tijd)
    order = ["Games", "Apps", "Educational", "Health & Wellness", "Animals & Pets", "Travel", "Comedy",
             "Food & Home", "Music & Podcasts", "Kids", "Faith-Based", "Classic TV", "Crime & Mystery",
             "News & Weather", "Sports", "International", "TV en Español", "Movies & TV", "Watch with Cable Subscription"]
    tagcats.sort(key=lambda c: order.index(c["name"]) if c["name"] in order else 99)
    for c in tagcats:
        lastid, n, complete = "", 0, False
        while time.time() < phase_deadline:
            d = get(f"{BASE}/api/v7/channels?category={c['id']}&pagesize=24&lastChId={urllib.parse.quote(lastid)}&categoryType=tag&{LOC}")
            if not d:
                complete = True
                break
            new = 0
            for ch in d:
                n += 1
                if ch["id"] not in seen:
                    seen[ch["id"]] = ch
                    new += 1
                    f.write(json.dumps({"src": "cat:" + c["name"], **ch}) + "\n")
            if lastid == d[-1]["id"] or len(d) < 24:
                complete = True
                break
            lastid = d[-1]["id"]
        counts[c["name"]] = {"seen": n, "complete": complete}
        print("cat", c["name"], n, complete, flush=True)
        if time.time() > phase_deadline:
            break
    json.dump(counts, open(f"{OUT}/category_counts.json", "w"), indent=1)
    return seen

def search(q, pages, seen, f):
    n = 0
    for p in range(pages):
        d = get(f"{BASE}/api/v6/channels?pagesize=24&pagestart={p*24}&q={urllib.parse.quote(q)}&{LOC}")
        if not d:
            break
        for ch in d:
            n += 1
            if ch["id"] not in seen:
                seen[ch["id"]] = ch
                f.write(json.dumps({"src": "q:" + q, **ch}) + "\n")
        if len(d) < 24:
            break
    print("search", q, n, flush=True)
    return n

def details(ids, deadline):
    f = open(f"{OUT}/details.jsonl", "a")
    done = set()
    try:
        for line in open(f"{OUT}/details.jsonl"):
            done.add(json.loads(line)["id"])
    except Exception:
        pass
    for i in ids:
        if i in done:
            continue
        if time.time() > deadline:
            break
        d = get(f"{BASE}/api/v6/channels/detailsunion/{urllib.parse.quote(i)}?{LOC}")
        if not d or "details" not in d:
            continue
        x = d["details"]
        cd = x.get("currentDetail") or {}
        rec = {
            "id": i, "name": x.get("name"), "developer": x.get("developerName"), "developerId": x.get("developerId"),
            "price": x.get("price"), "priceAsNumber": x.get("priceAsNumber"),
            "starRating": x.get("starRating"), "rating": x.get("rating"), "ratingCount": x.get("starRatingCount"),
            "createdDate": x.get("createdDate"), "publishedDate": x.get("publishedDate"), "modifiedDate": x.get("modifiedDate"),
            "currentPublished": cd.get("publishedDate"),
            "categories": [c["name"] for c in (x.get("categoryList") or [])],
            "revenueSources": cd.get("literalRevenueSources"), "isInAppPurchaseOffered": x.get("isInAppPurchaseOffered"),
            "isSubscription": cd.get("isSubscription"), "isOneTimePurchase": cd.get("isOneTimePurchase"),
            "isFree": cd.get("isFree"), "freeTrial": cd.get("freeTrial"), "paymentSchedule": x.get("paymentSchedule"),
            "channelStoreCodes": cd.get("channelStoreCodes"), "channelVersionType": x.get("channelVersionType"),
        }
        f.write(json.dumps(rec) + "\n")
        f.flush()

if __name__ == "__main__":
    t0 = time.time()
    list_secs = float(sys.argv[1]) if len(sys.argv) > 1 else 300
    det_secs = float(sys.argv[2]) if len(sys.argv) > 2 else 360
    seen = listing(t0 + list_secs)
    f = open(f"{OUT}/list.jsonl", "a")
    for q in ["screensaver", "theme", "game", "puzzle", "solitaire", "trivia", "aquarium", "fireplace", "clock", "arcade"]:
        search(q, 8, seen, f)
    f.close()
    # steekproef: betaald eerst, dan screensaver/theme/game, dan rest
    allch = list(seen.values())
    def prio(ch):
        name = (ch.get("name") or "").lower()
        paid = ch.get("price") not in ("", "0", None)
        small = any(k in name for k in ["screensaver", "theme", "game", "puzzle", "solitaire", "trivia", "aquarium", "fireplace", "clock"])
        return (0 if paid else 1, 0 if small else 1)
    allch.sort(key=prio)
    json.dump([c["id"] for c in allch], open(f"{OUT}/detail_order.json", "w"))
    print("total unique listed", len(allch), "paid", sum(1 for c in allch if c.get("price") not in ("", "0", None)), flush=True)
    details([c["id"] for c in allch], time.time() + det_secs)
    print("klaar", round(time.time() - t0), flush=True)
