#!/usr/bin/env python3
"""Analyse lichting Shopware: downloads-emmers per prijsmodel en maand. Gebruik: python3 shopware-analyse-script.py cohort.jsonl"""
import sys, json, collections, datetime, statistics
D = [json.loads(l) for l in open(sys.argv[1])]
order = {'<10': 5, '<25': 17, '<50': 37, '<100': 75}
def num(x):
    if x is None: return None
    return order.get(x, None) if x.startswith('<') else int(x.replace(',', ''))
def dt(s): return datetime.datetime.strptime(s, '%d %B %Y').date()
def rapport(naam, S):
    if not S: return
    c = collections.Counter(d.get('downloads') for d in S)
    n = len(S); h = sum(1 for d in S if num(d.get('downloads')) and num(d['downloads']) >= 100)
    nums = sorted(num(d.get('downloads')) or 0 for d in S)
    med = nums[n // 2]
    emmers = {k: c.get(k, 0) for k in ['<10', '<25', '<50', '<100']}
    print(f"{naam}: n={n} emmers={emmers} 100+={h} ({100*h/n:.0f}%) mediaan-emmer~{[k for k,v in order.items() if v==med] or med} reviews>=1: {sum(1 for d in S if (d.get('reviews') or 0)>0)}")
for d in D: d['pd'] = dt(d['publicatie'])
D = [d for d in D if not (d.get('url','').split('/en/')[1].lower().startswith('swag'))]  # Shopware zelf eruit
for lab, a, b in [('feb-apr 2026', '2026-02-01', '2026-04-30'), ('mei-aug 2026', '2026-05-01', '2026-08-31')]:
    a, b = datetime.date.fromisoformat(a), datetime.date.fromisoformat(b)
    S = [d for d in D if a <= d['pd'] <= b]
    rapport(lab + ' alles', S)
    for m in ['huur', 'gratis']:
        rapport(f"  {lab} {m}", [d for d in S if d['model'] == m])
    H = [d for d in S if d['model'] == 'huur' and d.get('per_maand')]
    if H: print('   mediaan maandprijs huur', statistics.median(d['per_maand'] for d in H))
    top = sorted([d for d in S if num(d.get('downloads')) and num(d['downloads']) >= 100], key=lambda d: -num(d['downloads']))
    for d in top[:12]: print('   ', d['downloads'], d['model'], d.get('per_maand'), d['maker'], '|', d['naam'][:50], '|', d.get('partnerstatus'), d.get('partner_sinds'), d['publicatie'])
