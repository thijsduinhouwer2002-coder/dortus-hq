#!/usr/bin/env python3
"""Analyse van filament-plugins-<datum>.json: bereik van nieuwe plugins en leiders per categorie.
Gebruik: python3 filament-plugins-analyse.py filament-plugins-2026-11-08.json"""
import json, sys, statistics as st, collections
P = json.load(open(sys.argv[1]))
met = [p for p in P if p.get('downloads')]
print('plugins', len(P), 'met Packagist-tellers', len(met), 'betaald', sum(1 for p in P if p.get('price')))
def q(xs, f):
    xs = sorted(xs); return xs[int(f * (len(xs) - 1))] if xs else None
for van, tot in (('2025-11', '2026-02'), ('2026-02', '2026-05'), ('2026-05', '2026-08'), ('2026-08', '2026-10')):
    g = [p for p in met if van <= p['publish_date'][:7] < tot and not p.get('price')]
    tl = [p['downloads']['total'] for p in g]; mo = [p['downloads']['monthly'] for p in g]
    if g:
        print(f'gratis, gepubliceerd {van} tot {tot}: n={len(g)} totaal mediaan {st.median(tl)} p75 {q(tl,.75)} p90 {q(tl,.9)}; per maand mediaan {st.median(mo)} p90 {q(mo,.9)}; 1000+ totaal {sum(1 for x in tl if x>=1000)}')
print('\nTop 25 gratis plugins op downloads per maand:')
for p in sorted(met, key=lambda p: -p['downloads']['monthly'])[:25]:
    print(p['downloads']['monthly'], p['downloads']['total'], p['publish_date'][:10], p['name'][:40], p['author_slug'], p['categories'][:3], p['versions'])
print('\nNieuw sinds 2026-03 met 2000+ downloads per maand:')
for p in sorted(met, key=lambda p: -p['downloads']['monthly']):
    if p['publish_date'] >= '2026-03' and p['downloads']['monthly'] >= 2000:
        print(p['downloads']['monthly'], p['downloads']['total'], p['publish_date'][:10], p['name'][:40], p['author_slug'], p['categories'][:3], 'BETAALD' if p.get('price') else '')
