# Haalt de lijst betaalde tools op itch.io (RSS, nieuwste eerst) tot een datum.
# Gebruik: python3 itch-lijst-script.py <categorie> <tot JJJJ-MM-DD> <uit.json>
import sys, json, time, re, urllib.request, email.utils, datetime
cat, tot, uit = sys.argv[1], sys.argv[2], sys.argv[3]
grens = datetime.datetime.fromisoformat(tot).replace(tzinfo=datetime.timezone.utc)
items, page = [], 1
while True:
    url = f"https://itch.io/{cat}/newest/store.xml?page={page}"
    for poging in range(4):
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (onderzoek)"}), timeout=30).read().decode()
            break
        except Exception as e:
            time.sleep(5)
    else:
        print("mislukt", page); break
    blokken = re.findall(r"<item>(.*?)</item>", x, re.S)
    if not blokken: break
    datums = []
    for b in blokken:
        g = lambda t: (re.search(f"<{t}>(.*?)</{t}>", b, re.S) or [None, None])[1]
        pd = email.utils.parsedate_to_datetime(g("pubDate"))
        items.append({"url": g("link"), "titel": g("plainTitle"), "prijs": g("price"), "pub": pd.isoformat(),
                      "maak": g("createDate"), "upd": g("updateDate")})
        datums.append(pd)
    datums.sort(); oudste = datums[len(datums)//2]  # mediaan van de pagina, de lijst is niet strikt op volgorde
    if page % 20 == 0: print(page, oudste, len(items), flush=True)
    if oudste < grens: break
    page += 1; time.sleep(0.4)
json.dump(items, open(uit, "w"), indent=0)
print("klaar", len(items), "pagina's", page)
