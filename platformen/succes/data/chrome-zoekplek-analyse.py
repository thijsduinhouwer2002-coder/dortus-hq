# Joris, run 32. Wat bepaalt de plek in de zoekbalk van de Chrome Web Store?
import re, sys, numpy as np, pandas as pd
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression
d = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'chrome-zoekplek-2026-11-17.csv')
NU = pd.Timestamp('2026-11-17').timestamp()
def woorden(s): return re.findall(r'[a-z0-9]+', str(s).lower())
def stam(w): return w[:-1] if len(w) > 3 and w.endswith('s') else w
def match(q, t):
    qw = [stam(w) for w in woorden(q)]; tw = set(stam(w) for w in woorden(t))
    return sum(w in tw for w in qw) / len(qw)
d['naam_alle'] = [match(q, n) == 1 for q, n in zip(d.zoekterm, d.naam)]
d['naam_deel'] = [match(q, n) for q, n in zip(d.zoekterm, d.naam)]
d['naam_zin'] = [' '.join(woorden(q)) in ' '.join(woorden(n)) for q, n in zip(d.zoekterm, d.naam)]
d['oms_alle'] = [match(q, o) == 1 for q, o in zip(d.zoekterm, d.korte_omschrijving)]
d['naam_lengte'] = [len(woorden(n)) for n in d.naam]
d['log_gebr'] = np.log10(d.gebruikers.fillna(0) + 1)
d['log_beoord'] = np.log10(d.beoordelingen.fillna(0) + 1)
d['jaren_oud'] = (NU - d.bijgewerkt.fillna(NU - 10*365*86400)) / (365*86400)
d['sterren'] = d.sterren.fillna(0)
print('rijen', len(d), 'zoektermen', d.zoekterm.nunique(), 'extensies', d.id.nunique())

# 1. Spearman per zoekterm tussen plek en kenmerk
print('\n1. Spearman plek tegen kenmerk (negatief = hoger kenmerk, betere plek), mediaan over zoektermen')
for k in ['log_gebr','log_beoord','sterren','jaren_oud','naam_deel','featured']:
    rs = []
    for q, g in d.groupby('zoekterm'):
        if len(g) >= 5 and g[k].nunique() > 1:
            rs.append(spearmanr(g.plek, g[k]).statistic)
    print(f'  {k:12s} mediaan {np.median(rs):+.2f}  aandeel negatief {np.mean(np.array(rs)<0):.0%}  n={len(rs)}')

# 2. Paren binnen dezelfde zoekterm: wie staat hoger?
feats = ['log_gebr','log_beoord','sterren','jaren_oud','naam_alle','naam_zin','oms_alle','featured','naam_lengte']
X, y = [], []
for q, g in d.groupby('zoekterm'):
    g = g.sort_values('plek'); v = g[feats].astype(float).values
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            X.append(v[i]-v[j]); y.append(1); X.append(v[j]-v[i]); y.append(0)
X = np.array(X); y = np.array(y); sd = X.std(0); sd[sd == 0] = 1
m = LogisticRegression(fit_intercept=False, C=10, max_iter=2000).fit(X/sd, y)
print('\n2. Paren (wie staat hoger), gestandaardiseerde gewichten; groter = belangrijker')
for f, c in sorted(zip(feats, m.coef_[0]), key=lambda t: -abs(t[1])): print(f'  {f:12s} {c:+.2f}')
print('  juist voorspeld', f'{m.score(X/sd, y):.0%}')
for sub in [['log_gebr'], ['naam_alle','naam_zin'], ['log_gebr','log_beoord','sterren','featured']]:
    idx = [feats.index(s) for s in sub]
    mm = LogisticRegression(fit_intercept=False, C=10, max_iter=2000).fit(X[:, idx]/sd[idx], y)
    print('  alleen', sub, f'{mm.score(X[:, idx]/sd[idx], y):.0%}')

# 3. Is nummer 1 de grootste?
g1 = d.groupby('zoekterm')
grootste = sum(g.sort_values('plek').gebruikers.iloc[0] == g.gebruikers.max() for q, g in g1)
print(f'\n3. Nr. 1 is de grootste van de 10: {grootste} van {d.zoekterm.nunique()}')
# hoeveel in top 3 met <1000 gebruikers, en wat hebben ze
for plek_max in [1, 3, 10]:
    s = d[d.plek <= plek_max]
    print(f'  top {plek_max}: {len(s)} rijen; <1.000 gebr {np.mean(s.gebruikers<1000):.0%}; <100 {np.mean(s.gebruikers<100):.0%}; naam alle woorden {s.naam_alle.mean():.0%}; zin {s.naam_zin.mean():.0%}; featured {s.featured.mean():.0%}; mediaan gebr {s.gebruikers.median():,.0f}')
klein = d[(d.plek <= 3) & (d.gebruikers < 1000)]
print('\n  Klein (<1.000) in de top 3:')
for r in klein.itertuples(): print(f'   "{r.zoekterm}" #{r.plek} {r.naam[:55]} | {r.gebruikers} gebr | {r.beoordelingen} beoord {r.sterren:.1f} | naam_alle {r.naam_alle} | bijgewerkt {r.jaren_oud:.1f} jr')
# 4. Naam met alle woorden: plek
print('\n4. Plek naar naam')
for k in ['naam_zin','naam_alle']:
    print(' ', k, d.groupby(k).plek.mean().round(2).to_dict(), d.groupby(k).gebruikers.median().to_dict(), d.groupby(k).size().to_dict())
# 5. Binnen kleine (<10.000) extensies: naam tegen plek
s = d[d.gebruikers < 10000]
print('\n5. Onder de 10.000 gebruikers:', len(s), 'gemiddelde plek naam_alle', s.groupby('naam_alle').plek.mean().round(2).to_dict(), 'aantal', s.groupby('naam_alle').size().to_dict())
d.to_csv('/tmp/claude-0/-home-claude/798d2537-5944-5387-8954-de7e3def2afb/scratchpad/cws/verrijkt.csv', index=False)

# 6. Paren: hoe vaak staat de grootste hoger, en wat beslist bij ongeveer even groot?
P = []
for q, g in d.groupby('zoekterm'):
    g = g.sort_values('plek').reset_index(drop=True)
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            a, b = g.loc[i], g.loc[j]   # a staat hoger
            P.append(dict(gebr_hoger=a.gebruikers > b.gebruikers, gelijk=a.gebruikers == b.gebruikers,
                          ratio=(a.gebruikers+1)/(b.gebruikers+1), naam_a=a.naam_alle, naam_b=b.naam_alle))
P = pd.DataFrame(P); nz = P[~P.gelijk]
print(f'\n6. Paren met verschil in gebruikers: {len(nz)}; de grootste staat hoger in {nz.gebr_hoger.mean():.0%}')
for lo, hi in [(10, 1e12), (3, 10), (1/3, 3)]:
    s = nz[((nz.ratio >= lo) & (nz.ratio < hi)) | ((1/nz.ratio >= lo) & (1/nz.ratio < hi))]
    print(f'   verschil factor {lo:.2g} tot {hi:.2g}: {len(s)} paren, grootste hoger {s.gebr_hoger.mean():.0%}')
s = nz[(nz.naam_a != nz.naam_b)]
print(f'   paren waar maar één de zoekwoorden in de naam heeft: {len(s)}, die met naam staat hoger {(s.naam_a).mean():.0%}')
s2 = s[(s.ratio < 1)]
print(f'   ... en de kleinste van de twee heeft de naam: {len(s2[s2.naam_a | s2.naam_b])}, waarvan kleinste-met-naam hoger {(s2.naam_a).mean():.0%} (n={len(s2)})')
s3 = s[(s.ratio > 1)]  # hogere is groter
print(f'   bij de omgekeerde: grotere hoger {len(s3)} paren')
# kleinere met naam tegen grotere zonder naam
kl = []
for q, g in d.groupby('zoekterm'):
    for _, a in g[g.naam_alle].iterrows():
        for _, b in g[~g.naam_alle].iterrows():
            if a.gebruikers < b.gebruikers:
                r = b.gebruikers / max(a.gebruikers, 1)
                kl.append((r, a.plek < b.plek))
kl = pd.DataFrame(kl, columns=['r', 'kleine_hoger'])
for lo, hi in [(1, 3), (3, 10), (10, 100), (100, 1e12)]:
    s = kl[(kl.r >= lo) & (kl.r < hi)]
    print(f'   kleinere MET naam tegen grotere ZONDER naam, factor {lo}-{hi:.0g}: {len(s)} paren, kleinere staat hoger {s.kleine_hoger.mean():.0%}')

# 7. Moeilijkheid per zoekterm
t = d.groupby('zoekterm').apply(lambda g: pd.Series(dict(woorden=len(woorden(g.name)), top3_min=g[g.plek<=3].gebruikers.min(), nr10=g.sort_values('plek').gebruikers.iloc[-1], top10_med=g.gebruikers.median())), include_groups=False)
t['lang'] = t.woorden >= 3
print('\n7. Drempel per soort zoekterm (mediaan over zoektermen)')
print(t.groupby('lang')[['top3_min','nr10','top10_med']].median(), t.groupby('lang').size().to_dict())
print('   zoektermen waar de top 3 een extensie onder 1.000 heeft:', (t.top3_min < 1000).sum(), 'van', len(t), '; bij 3+ woorden', (t[t.lang].top3_min < 1000).sum(), 'van', t.lang.sum())
print(t.sort_values('top3_min').head(25).to_string())
