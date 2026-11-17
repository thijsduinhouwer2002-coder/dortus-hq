#!/usr/bin/env python3
"""Verhaal 24 (Fenna): hoeveel dagen tussen Next Fest en uitbrengen, en doet een korte tussenpoos het beter?

Stap 1: voor elk betaald bureaubladspel uit Vera's kaart dat tussen 1 jan 2024 en 15 okt 2026 uitkwam,
de aankondigingen van de maker ophalen (ISteamNews/GetNewsForApp) en zoeken naar "Next Fest" vóór de uitgave.
Stap 2: reviews in de eerste 28 dagen na de uitgave (weekgrafiek appreviewhistogram, alle talen).
Alleen openbare API's, rustig (0,35 s tussen verzoeken). Uitvoer: nextfest-tussenpoos-ruw.json
"""
import csv, json, time, sys, urllib.request, urllib.parse, datetime, os, re

HIER = os.path.dirname(os.path.abspath(__file__))
KAART = os.path.join(HIER, '..', '..', 'verkenner', 'data', 'steam-desktop-kaart-2026-11-16.csv')
UIT = os.path.join(HIER, 'nextfest-tussenpoos-ruw.json')

def haal(url):
    for poging in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as f:
                return json.loads(f.read().decode('utf8', 'ignore'))
        except Exception as e:
            time.sleep(2 + poging * 3)
    return None

def nieuws(appid):
    u = f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={appid}&count=300&maxlength=0&feeds=steam_community_announcements'
    d = haal(u)
    if not d:
        return None
    uit = []
    for it in d.get('appnews', {}).get('newsitems', []):
        tekst = (it.get('title') or '') + ' ' + (it.get('contents') or '')
        if re.search(r'next\s*fest', tekst, re.I):
            uit.append({'datum': it['date'], 'titel': it.get('title', '')[:140]})
    return uit

def reviews_28d(appid, start_ts):
    """Reviews in de eerste 28 dagen uit de weekgrafiek van Steam (appreviewhistogram, alle talen).
    appreviews stuurt sinds nov 2026 door naar de voorpagina. Is de grafiek per maand (oudere spellen),
    dan: de uitgavemaand plus het deel van de volgende maand tot dag 28 (naar rato, benadering)."""
    d = haal(f'https://store.steampowered.com/appreviewhistogram/{appid}?l=english&review_score_preference=0')
    if not d or not d.get('results'):
        return None, None, None
    res = d['results']; soort = res.get('rollup_type')
    rol = sorted(res.get('rollups', []), key=lambda x: x['date'])
    eind = start_ts + 28 * 86400
    n = pos = 0.0
    if soort == 'week':
        for w in rol:
            if start_ts - 3 * 86400 <= w['date'] < eind - 3 * 86400:
                n += w['recommendations_up'] + w['recommendations_down']; pos += w['recommendations_up']
    else:
        for i, m in enumerate(rol):
            volgende = rol[i + 1]['date'] if i + 1 < len(rol) else m['date'] + 31 * 86400
            if volgende <= start_ts or m['date'] >= eind:
                continue
            lengte = volgende - m['date']
            if m['date'] <= start_ts:
                deel = 1.0  # uitgavemaand: alle reviews vallen na de uitgave
            else:
                deel = min(1.0, (eind - m['date']) / lengte)
            n += deel * (m['recommendations_up'] + m['recommendations_down']); pos += deel * m['recommendations_up']
    return round(n), round(pos), soort

def main():
    rijen = list(csv.DictReader(open(KAART, encoding='utf8')))
    kies = [r for r in rijen if r['gratis'] == 'False' and r['binnenkort'] == 'False'
            and '2024-01-01' <= r['releasedatum'] <= '2026-10-15']
    oud = {}
    if os.path.exists(UIT):
        oud = {str(x['appid']): x for x in json.load(open(UIT))}
    uit = list(oud.values())
    import threading
    from concurrent.futures import ThreadPoolExecutor
    slot = threading.Lock()

    def een(r):
        nv = nieuws(r['appid'])
        time.sleep(0.35)
        rel = datetime.datetime.strptime(r['releasedatum'], '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)
        x = {'appid': r['appid'], 'naam': r['naam'], 'releasedatum': r['releasedatum'],
             'prijs_usd': r['prijs_usd'], 'reviews_totaal': int(r['reviews_totaal'] or 0),
             'pct_positief': r['pct_positief'], 'soort_spel': r['soort_spel'], 'lijkt_op_hats': r['lijkt_op_hats'],
             'nextfest_posts': nv}
        if x['reviews_totaal'] >= 10:
            n, pos, soort = reviews_28d(r['appid'], int(rel.timestamp()))
            x['rev28'] = n; x['rev28_pos'] = pos; x['grafiek'] = soort
            time.sleep(0.35)
        else:
            x['rev28'] = x['reviews_totaal']; x['rev28_pos'] = None
        with slot:
            uit.append(x)
            if len(uit) % 25 == 0:
                json.dump(uit, open(UIT, 'w'), indent=0)
                print(len(uit), len(kies), flush=True)

    # drie tegelijk: rustig genoeg voor openbare API's
    with ThreadPoolExecutor(3) as pool:
        list(pool.map(een, [r for r in kies if r['appid'] not in oud]))
    json.dump(uit, open(UIT, 'w'), indent=0)
    print('klaar', len(uit))

if __name__ == '__main__':
    main()
