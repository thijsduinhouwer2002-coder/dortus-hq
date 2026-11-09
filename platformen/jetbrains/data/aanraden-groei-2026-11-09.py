"""Groei van aangeraden plugins tussen twee metingen, per plugin en per bestandssoort.
Gebruik: python3 aanraden-groei-2026-11-09.py oud.tsv nieuw.tsv uit_plugins.tsv uit_soorten.tsv
"""
import csv, sys, collections
oud_f, nieuw_f, uit_p, uit_s = sys.argv[1:5]
def lees(f):
    rows = list(csv.DictReader(open(f), delimiter='\t'))
    return rows
oud, nieuw = lees(oud_f), lees(nieuw_f)
dl_oud = {r['xmlId']: r['downloads'] for r in oud}
info = {}
soorten = collections.defaultdict(set)
for r in nieuw:
    soorten[r['soort']].add(r['xmlId'])
    info[r['xmlId']] = r
def num(x):
    try: return int(x)
    except: return None
groei = {}
for x, r in info.items():
    a, b = num(dl_oud.get(x)), num(r['downloads'])
    groei[x] = (b - a) if a is not None and b is not None else None
with open(uit_p, 'w') as w:
    w.write("groei\tdownloads\tid\tnaam\txmlId\tsoorten\n")
    per_plugin_soorten = collections.defaultdict(list)
    for s, xs in soorten.items():
        for x in xs: per_plugin_soorten[x].append(s)
    for x in sorted(info, key=lambda x: -(groei[x] or -1)):
        r = info[x]
        w.write(f"{groei[x]}\t{r['downloads']}\t{r['id']}\t{r['naam']}\t{x}\t{' '.join(sorted(per_plugin_soorten[x]))}\n")
with open(uit_s, 'w') as w:
    w.write("groei_totaal\taantal_plugins\tsoort\tgrootste_groeier\tgroei_grootste\n")
    rij = []
    for s, xs in soorten.items():
        g = [(groei[x] or 0, x) for x in xs]
        tot = sum(v for v, _ in g)
        top = max(g)
        rij.append((tot, len(xs), s, info[top[1]]['naam'], top[0]))
    for t in sorted(rij, reverse=True):
        w.write("\t".join(map(str, t)) + "\n")
print(len(info), "plugins,", len(soorten), "soorten; zonder vergelijking:", sum(1 for v in groei.values() if v is None))
