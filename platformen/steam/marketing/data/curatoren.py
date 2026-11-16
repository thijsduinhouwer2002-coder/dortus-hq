# Steam-curatoren die een lijst spellen recenseerden (Sem). Gebruik:
#   python3 curatoren.py <uit.csv> appid:naam appid:naam ...
# Leest de openbare lijst "curators reviewing" per spel (store.steampowered.com/curators/ajaxgetcurators),
# telt per curator hoeveel van de spellen hij deed, met volgers, aantal recensies, laatste recensie.
# volgers_hoge_waarde = Steam-veld total_high_value_followers (Valve's eigen telling van volgers die meetellen;
# een groot verschil met volgers wijst op nepvolgers). Bewaart alleen namen, links en getallen; geen mailadressen.
import csv, json, re, sys, time, urllib.request, datetime
def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=25) as f:
                return json.load(f)
        except Exception:
            time.sleep(4)
    return None
uit = sys.argv[1]
spellen = [a.split(':', 1) for a in sys.argv[2:]]
cur = {}
for appid, naam in spellen:
    start, totaal = 0, 1
    while start < totaal and start < 400:
        d = get(f"https://store.steampowered.com/curators/ajaxgetcurators/render/?query=&start={start}&count=50&filter=top_curators_reviewing&appid={appid}")
        if not d:
            break
        totaal = d.get('total_count', 0)
        m = re.search(r'g_rgTopCurators = (\[.*?\]);\s*\n', d['results_html'], re.S)
        lijst = json.loads(m.group(1)) if m else []
        for c in lijst:
            k = c['clanID']
            r = cur.setdefault(k, {'naam': c['name'], 'link': c['link'], 'volgers': c['total_followers'], 'echte_volgers': c.get('total_high_value_followers', ''),
                                   'recensies': c['total_reviews'], 'laatste': c.get('last_curation_date') or 0,
                                   'spellen': [], 'gratis_gekregen': 0, 'betaald': 0,
                                   'tekst': (c.get('curator_description') or '').replace('\n', ' ')[:160]})
            for rec in c.get('m_rgAppRecommendations', []):
                if str(rec['appid']) == appid:
                    r['spellen'].append(naam)
                    r['gratis_gekregen'] += rec.get('received_for_free', 0)
                    r['betaald'] += rec.get('received_compensation', 0)
                    break
            else:
                r['spellen'].append(naam)
        start += 50
        time.sleep(1.5)
    print(naam, appid, totaal, file=sys.stderr)
rij = []
for k, r in cur.items():
    dag = datetime.datetime.fromtimestamp(r['laatste'], datetime.timezone.utc).date().isoformat() if r['laatste'] else ''
    rij.append([k, r['naam'], r['link'], r['volgers'], r['echte_volgers'], r['recensies'], dag, len(set(r['spellen'])),
                ';'.join(sorted(set(r['spellen']))), r['gratis_gekregen'], r['betaald'], r['tekst']])
rij.sort(key=lambda x: (-x[7], -x[3]))
w = csv.writer(open(uit, 'w', newline=''))
w.writerow(['clanid', 'naam', 'link', 'volgers', 'volgers_hoge_waarde', 'recensies', 'laatste_recensie', 'aantal_spellen', 'spellen',
            'gratis_gekregen', 'betaald_gemeld', 'omschrijving'])
w.writerows(rij)
print(datetime.datetime.now(datetime.timezone.utc).isoformat(), len(rij), file=sys.stderr)
