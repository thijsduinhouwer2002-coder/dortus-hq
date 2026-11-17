# Verhaal 31: deelt de steekproef "eigen geluid" in naar stil, gesproken en geluid zonder spraak
# en vergelijkt ze binnen hetzelfde account (ratio uit tiktok-geluid-2026-11-17.csv).
# Gebruik: python3 tiktok-geluid-audio-analyse.py <analyse.csv> <volume.csv> <spraak.csv> <uit.csv>
import csv, sys, statistics as st, collections, random
ana, vol, spr, uit = sys.argv[1:5]
R = {r['id']: r for r in csv.DictReader(open(ana))}
V = {r['id']: r for r in csv.DictReader(open(vol))}
S = {r[0]: r for r in csv.reader(open(spr))}
rij = []
for i, v in V.items():
    if not v['mean_db'] or i not in R: continue
    mx = float(v['max_db']) if v['max_db'] != '-inf' else -99; mean = float(v['mean_db']) if v['mean_db'] != '-inf' else -99
    s = S.get(i)
    if mx < -40 or mean < -60: k = 'stil'
    elif s and s[2] and float(s[2]) >= 5 and int(s[3]) >= 10: k = 'spraak'
    elif s and s[2] != '': k = 'geluid_zonder_spraak'
    else: continue
    rij.append(dict(account=R[i]['account'], id=i, ratio=float(R[i]['ratio']), views=int(R[i]['views']), klasse=k))
with open(uit, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['account', 'id', 'views', 'ratio', 'klasse']); w.writeheader(); w.writerows(rij)
print('gemeten', len(rij), collections.Counter(r['klasse'] for r in rij))
for k in ['stil', 'spraak', 'geluid_zonder_spraak']:
    x = [r['ratio'] for r in rij if r['klasse'] == k]
    if x: print(f'{k:22s} n={len(x):3d} mediaan ratio {st.median(x):.2f} hit3x {sum(1 for v in x if v>=3)/len(x):.0%} onder 0,5x {sum(1 for v in x if v<0.5)/len(x):.0%}')
accs = sorted({r['account'] for r in rij})
def verg(a_, b_, mn=4):
    out = []
    for a in accs:
        x = [r['ratio'] for r in rij if r['account'] == a and r['klasse'] == a_]
        y = [r['ratio'] for r in rij if r['account'] == a and r['klasse'] == b_]
        if len(x) >= mn and len(y) >= mn: out.append((a, len(x), len(y), round(st.median(x)/st.median(y), 2)))
    if out:
        vs = [o[3] for o in out]
        print(f'{a_} vs {b_}: accounts {sum(1 for v in vs if v>1)}/{len(vs)} beter, mediaan {st.median(vs):.2f}', out)
verg('spraak', 'geluid_zonder_spraak'); verg('stil', 'geluid_zonder_spraak', 2); verg('stil', 'spraak', 2)
print('per account aandeel')
for a in accs:
    c = collections.Counter(r['klasse'] for r in rij if r['account'] == a); n = sum(c.values())
    print(f'{a:22s} n={n:2d} stil {c["stil"]:2d} spraak {c["spraak"]:2d} zonder_spraak {c["geluid_zonder_spraak"]:2d}')
