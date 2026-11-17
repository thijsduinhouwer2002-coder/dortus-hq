import sys, json, time, re, urllib.request, email.utils, datetime
pad, tot, uit = sys.argv[1], sys.argv[2], sys.argv[3]
grens = datetime.datetime.fromisoformat(tot).replace(tzinfo=datetime.timezone.utc)
items, page, laag = [], 1, 0
while page <= 200:
    url = f"https://itch.io/{pad}.xml?page={page}"
    x = None
    for poging in range(4):
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (onderzoek)"}), timeout=30).read().decode(); break
        except Exception: time.sleep(5)
    if x is None: break
    bl = re.findall(r"<item>(.*?)</item>", x, re.S)
    if not bl: break
    ds=[]
    for b in bl:
        g = lambda t: (re.search(f"<{t}>(.*?)</{t}>", b, re.S) or [None, None])[1]
        pd = email.utils.parsedate_to_datetime(g("pubDate"))
        items.append({"url": g("link"), "titel": g("plainTitle"), "prijs": g("price"), "pub": pd.isoformat(), "maak": g("createDate")}); ds.append(pd)
    ds.sort()
    if ds[len(ds)//2] < grens:
        laag += 1
        if laag >= 3: break
    page += 1; time.sleep(0.4)
json.dump(items, open(uit, "w"))
print(pad, "klaar", len(items), "pagina", page, items[-1]["pub"] if items else "")
