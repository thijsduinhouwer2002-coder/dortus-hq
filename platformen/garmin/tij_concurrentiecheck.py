# Concurrentiecheck voor Tij: nieuwste 60 wijzerplaten op twee woorden, en de eerste 60 op zeewoorden.
import json, subprocess, urllib.parse, time, csv, re, datetime, sys
B = 'https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords'
uit = sys.argv[1]
zoek = [('body battery', 'mostRecent'), ('big digits', 'mostRecent'), ('tide', 'mostRelevant'), ('sea', 'mostRelevant'),
        ('ocean', 'mostRelevant'), ('wave', 'mostRelevant'), ('boat', 'mostRelevant'), ('sail', 'mostRelevant'),
        ('water level', 'mostRelevant'), ('ship', 'mostRelevant'), ('battery level sea', 'mostRelevant')]
zee = re.compile(r'\b(sea|ocean|wave|waves|boat|sail|sailing|sailboat|ship|tide|tides|water level|waterline|liquid|fills? up|filling)\b', re.I)
bb = re.compile(r'body ?battery', re.I)
rijen = []
for w, s in zoek:
    plek = 0
    for p in range(2):
        u = f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex={p*30}&pageSize=30&sortType={s}&appType=watchface"
        r = subprocess.run(['curl', '-s', '-m', '40', u], capture_output=True, text=True).stdout
        try: d = json.loads(r)
        except Exception: print('fout', w, p, r[:100]); break
        for a in d['apps']:
            plek += 1
            loc = [l for l in a.get('appLocalizations', []) if l.get('locale') == 'en'] or a.get('appLocalizations', [{}])
            naam = loc[0].get('name') or ''; tekst = loc[0].get('description') or ''
            pr = (a.get('pricing') or {}).get('salePrice') or {}
            rijen.append([w, s, d['totalCount'], plek, naam, (a.get('developer') or {}).get('developerDisplayName') or (a.get('developer') or {}).get('fullName') or '',
                          pr.get('price', 0), a.get('downloadCount'), a.get('reviewCount'), a.get('averageRating'),
                          len(a.get('compatibleDeviceTypeIds', [])), 'ja' if bb.search(naam + ' ' + tekst) else 'nee',
                          ';'.join(sorted(set(m.lower() for m in zee.findall(naam + ' ' + tekst)))), a.get('id')])
        if len(d['apps']) < 30: break
        time.sleep(1.0)
    print(w, s, plek, flush=True)
with open(uit, 'w', newline='') as f:
    c = csv.writer(f); c.writerow(['zoekwoord', 'sortering', 'totaal', 'plek', 'naam', 'maker', 'prijs_usd_0_is_gratis', 'downloads', 'reviews', 'score', 'horloges', 'noemt_body_battery', 'zeewoorden_in_tekst', 'id'])
    c.writerows(rijen)
print(len(rijen))
