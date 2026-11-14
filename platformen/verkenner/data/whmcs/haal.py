# Vera 14 nov: WHMCS Marketplace, lijst "New" en productpagina's
import re, html, json, sys, time, urllib.request
def get(u):
    r = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Dortus verkenner)"})
    return urllib.request.urlopen(r, timeout=30).read().decode("utf-8", "ignore")
ids = []
for p in range(1, 10):
    t = get(f"https://marketplace.whmcs.com/category/new?page={p}")
    for i in re.findall(r"marketplace.whmcs.com/product/(\d+)", t):
        if i not in ids: ids.append(i)
    time.sleep(1)
res = []
for i in ids:
    try:
        t = get(f"https://marketplace.whmcs.com/product/{i}")
    except Exception as e:
        res.append({"id": i, "err": str(e)[:60]}); continue
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)); s = re.sub(r"\s+", " ", s)
    m = re.search(r"Recently Updated Commercial (.*?) Developed By (.*?) (?:\S.*?) Updated (\d+\w* \w+ \d{4}) (\d+) Reviews? (?:Compatible with (.*?) )?(Buy Now for \$[\d.,]+|Get it Free|Free|Get Now|Download|Learn More|Contact|[A-Z][a-z]+ [A-Za-z]+)", s)
    rec = {"id": i}
    if m:
        rec.update(titel=m.group(1), maker=m.group(2), bijgewerkt=m.group(3), reviews=int(m.group(4)), knop=m.group(6))
    else:
        j = s.find("Developed By"); rec["ruw"] = s[max(0, j - 150): j + 300]
    res.append(rec); time.sleep(1)
json.dump(res, open(sys.argv[1], "w"), ensure_ascii=False, indent=0)
print("klaar", len(res))
