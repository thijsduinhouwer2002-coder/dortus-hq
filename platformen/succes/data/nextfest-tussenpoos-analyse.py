#!/usr/bin/env python3
"""Verhaal 24 (Fenna): indelen per tussenpoos tussen het einde van Next Fest en de uitgave.

Next Fest-edities (startdag, 7 dagen; GEZIEN in de aankondigingen van Steamworks, appid 593110,
behalve feb 2026: die post ontbreekt in de nieuws-API, datum 23 feb uit DERDEN).
Een spel telt als "deed Next Fest" als de maker een aankondiging met "Next Fest" plaatste
tussen 21 dagen voor de start en 3 dagen na het einde van een editie, en die editie eindigde voor de uitgave.
"""
import json, os, datetime, statistics, csv

HIER = os.path.dirname(os.path.abspath(__file__))
RUW = os.path.join(HIER, 'nextfest-tussenpoos-ruw.json')
CSV = os.path.join(HIER, 'nextfest-tussenpoos-bureaublad-2026-11-17.csv')

EDITIES = ['2024-02-05', '2024-06-10', '2024-10-14', '2025-02-24', '2025-06-09', '2025-10-13',
           '2026-02-23', '2026-06-15', '2026-10-19']
D = lambda s: datetime.date.fromisoformat(s)
ED = [(D(s), D(s) + datetime.timedelta(days=7)) for s in EDITIES]

def editie(posts, rel):
    beste = None
    for st, eind in ED:
        if eind > rel:
            continue
        for p in posts or []:
            pd = datetime.datetime.fromtimestamp(p['datum'], datetime.UTC).date()
            if st - datetime.timedelta(days=21) <= pd <= eind + datetime.timedelta(days=3) and pd <= rel:
                beste = (st, eind)
    return beste

def groep(gap):
    if gap is None: return 'geen Next Fest-post'
    if gap <= 7: return '0 tot 7 dagen'
    if gap <= 30: return '8 tot 30 dagen'
    if gap <= 90: return '31 tot 90 dagen'
    return 'meer dan 90 dagen'

def main():
    ruw = json.load(open(RUW))
    rijen = []
    for x in ruw:
        if x.get('nextfest_posts') is None:
            continue
        rel = D(x['releasedatum'])
        e = editie(x['nextfest_posts'], rel)
        gap = (rel - e[1]).days if e else None
        rijen.append({**{k: x[k] for k in ['appid', 'naam', 'releasedatum', 'prijs_usd', 'reviews_totaal', 'pct_positief', 'soort_spel', 'lijkt_op_hats']},
                      'nextfest_editie': e[0].isoformat() if e else '', 'dagen_na_fest': gap if gap is not None else '',
                      'groep': groep(gap), 'reviews_eerste_28d': x.get('rev28'), 'grafiek': x.get('grafiek', '')})
    with open(CSV, 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=list(rijen[0].keys())); w.writeheader(); w.writerows(rijen)
    print('spellen', len(rijen))
    for g in ['0 tot 7 dagen', '8 tot 30 dagen', '31 tot 90 dagen', 'meer dan 90 dagen', 'geen Next Fest-post']:
        s = [r for r in rijen if r['groep'] == g]
        v = sorted(r['reviews_eerste_28d'] or 0 for r in s)
        if not v: continue
        q = lambda p: v[min(len(v) - 1, int(p * len(v)))]
        print(f"{g:22s} n={len(s):3d} mediaan28d={statistics.median(v):6.1f} p75={q(0.75):5d} p90={q(0.9):5d} "
              f"50+={sum(1 for a in v if a >= 50):3d} ({100*sum(1 for a in v if a >= 50)/len(v):.0f}%) "
              f"200+={sum(1 for a in v if a >= 200):2d} totaal_mediaan={statistics.median(r['reviews_totaal'] for r in s)}")

if __name__ == '__main__':
    main()
