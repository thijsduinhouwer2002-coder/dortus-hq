# Vera, 7 nov 2026. Analyse van AnkiWeb-add-ons (lijst.json en info.json van de haal-scripts).
# Gebruik: python3 anki-analyse-script.py <map>
import json, datetime, statistics, collections, sys, re
S = sys.argv[1]
L = {x['id']: x for x in json.load(open(S + '/lijst.json'))}
I = {x['id']: x for x in json.load(open(S + '/info.json')) if 'fout' not in x}
D = lambda t: datetime.datetime.fromtimestamp(t, datetime.UTC)
ts = lambda s: datetime.datetime.fromisoformat(s + 'T00:00:00+00:00').timestamp()
def pr(naam, u):
    u = sorted(u)
    if not u: print(naam, 'leeg'); return
    p = lambda k: round(100 * sum(v >= k for v in u) / len(u), 1)
    print(f"{naam}: n={len(u)} mediaan={statistics.median(u)} 1+={p(1)}% 10+={p(10)}% 50+={p(50)}% 100+={p(100)}% top={u[-6:]}")
print('add-ons in lijst', len(L), 'met info', len(I))
pr('alle add-ons, duimpjes omhoog', [x['up'] for x in L.values()])
print('zonder enige beoordeling', sum(1 for x in L.values() if x['up'] + x['down'] == 0))
recent = [x for x in L.values() if x['mtime'] >= ts('2025-11-01')]
print('gewijzigd sinds 1 nov 2025', len(recent), 'waarvan zonder beoordeling', sum(1 for x in recent if x['up'] + x['down'] == 0))
def first(x):
    t = [r['t'] for r in x['reviews'] if r['t']]; return min(t) if t else None
fm = collections.Counter(); coh = collections.defaultdict(list)
for x in I.values():
    f = first(x)
    if f:
        k = D(f).strftime('%Y-%m'); fm[k] += 1; coh[k].append(x)
print('add-ons per maand van hun eerste beoordeling:', [(k, v) for k, v in sorted(fm.items()) if k >= '2025-01'])
pr('lichting eerste beoordeling mei t/m aug 2026', [x['up'] for k, v in coh.items() if '2026-05' <= k <= '2026-08' for x in v])
pr('lichting eerste beoordeling nov 2025 t/m apr 2026', [x['up'] for k, v in coh.items() if '2025-11' <= k <= '2026-04' for x in v])
big = sorted(((x['up'], D(first(x)).strftime('%Y-%m-%d'), x['title'][:45], x['id']) for k, v in coh.items() if k >= '2025-11' for x in v), reverse=True)[:15]
print('grootste nieuwkomers (eerste beoordeling sinds nov 2025):'); [print('  ', b) for b in big]
rv = collections.Counter(D(r['t']).strftime('%Y-%m') for x in I.values() for r in x['reviews'] if r['t'])
print('beoordelingen per maand (add-ons met info):', [(k, v) for k, v in sorted(rv.items()) if k >= '2025-07'])
mon = collections.Counter(); paid = []
for x in I.values():
    t = (x['desc'] + ' ' + x['support']).lower()
    for m in ['patreon', 'ko-fi', 'buymeacoffee', 'gumroad', 'lemonsqueezy', 'paypal', 'subscription', 'premium', 'pro version', 'license', 'trial']:
        if m in t: mon[m] += 1
    if any(m in t for m in ['subscription', 'premium', 'license key', 'trial', 'pro version', 'gumroad', 'lemonsqueezy', 'one time', 'one-time']):
        paid.append((x['up'], x['title'][:50], x['id']))
print('geldwoorden in beschrijvingen (add-ons met info):', mon.most_common())
print('mogelijk betaalde laag:', len(paid)); [print('  ', p) for p in sorted(paid, reverse=True)[:20]]
