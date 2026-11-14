# Vera 14 nov: haal DoliStore-productpagina's op (Crawl-delay 2 uit robots.txt)
import re, html, json, sys, time, urllib.request
lo, hi, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
res = []
for i in range(hi, lo - 1, -1):
    url = f"https://www.dolistore.com/product.php?id={i}&l=en"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Dortus verkenner)"})
        t = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    except Exception as e:
        res.append({"id": i, "err": str(e)[:80]}); time.sleep(2); continue
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)); s = re.sub(r"\s+", " ", s)
    j = s.find(" View larger ")
    if j < 0:
        res.append({"id": i, "leeg": True}); time.sleep(2); continue
    blok = s[j:j + 1500]
    def g(p):
        m = re.search(p, blok); return m.group(1).strip() if m else None
    res.append({"id": i,
        "titel": g(r"View larger (.*?) Ref "),
        "prijs": g(r"(FREE|[\d.,]+ €)"),
        "auteur": g(r"Author (.*?) Module version"),
        "versie": g(r"Module version (.*?) Release date"),
        "uitgave": g(r"Release date (\d\d/\d\d/\d{4})"),
        "laatst": g(r"Last update (\d\d/\d\d/\d{4})"),
        "compat": g(r"Compatibility (.*?) (?:Last update|More info)")})
    time.sleep(2)
    if len(res) % 25 == 0:
        json.dump(res, open(out, "w"), ensure_ascii=False)
json.dump(res, open(out, "w"), ensure_ascii=False)
print("klaar", len(res))
