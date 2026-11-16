# Vera 16 nov 2026: volgers (leden van de officiele spelgroep) per Steam-app ophalen.
# Openbare XML van steamcommunity.com/games/<appid>/memberslistxml/?xml=1.
# Steam geeft 429 na ±45 snelle verzoeken; die grens respecteren we: 1 verzoek per 10 s,
# bij 429 stoppen we 5 minuten. Geen omweg via andere adressen.
# Gebruik: python3 -I steam-volgers-script.py lijst.json uit.jsonl   (lijst = JSON-lijst met appids)
import json, sys, time, re, urllib.request, urllib.error
ids, uit = json.load(open(sys.argv[1])), sys.argv[2]
f = open(uit, 'a')
for a in ids:
    url = f"https://steamcommunity.com/games/{a}/memberslistxml/?xml=1"
    n, fout = None, None
    for poging in range(2):
        try:
            t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read(60000).decode('utf8', 'replace')
            m = re.search(r'<memberCount>(\d+)', t)
            n = int(m.group(1)) if m else None; fout = None if m else 'geen teller'
            break
        except urllib.error.HTTPError as e:
            fout = str(e.code); time.sleep(300 if e.code == 429 else 10)
        except Exception as e:
            fout = type(e).__name__; time.sleep(10)
    f.write(json.dumps({'appid': a, 'volgers': n, 'fout': fout, 'gemeten': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}) + '\n'); f.flush()
    time.sleep(10)
