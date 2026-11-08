# Leest opgehaalde Playdate Catalog-pagina's (map met <slug>.html) en maakt een tabel.
# Ophalen: lijst via https://play.date/games/tags/all/?sort=newest&page=N (tot de pagina's herhalen),
# daarna elke https://play.date/games/<slug>/ met 0,4 s pauze.
import re, html, sys, os, json, collections, statistics
d = sys.argv[1]
rows = []
for f in sorted(os.listdir(d)):
    t = open(os.path.join(d, f), errors="ignore").read()
    tt = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S))))
    m = re.search(r'First published (\d\d)/(\d\d)/(\d{4})', tt)
    if not m: continue
    pub = f"{m.group(3)}-{m.group(1)}-{m.group(2)}"
    ai = re.search(r"(This game's developer declares that it was created without the use of generative AI|The developer used generative AI to create [^.]+|hasn.t reported on its use of generative A[Il])", tt)
    pr = re.search(r'Buy \$(\d+(?:\.\d\d)?)', tt)
    free = 'Free' in tt.split('First published')[1][:600] if pr is None else False
    dev = re.search(r'Made by (.+?) (?:[A-Z][a-z]+ ){0,1}', tt)
    sc = 'Scoreboards' in tt
    kind = 'app' if re.search(r'Catalog (Apps|App)\b', tt[:600]) else 'spel'
    rows.append(dict(slug=f[:-5], pub=pub, prijs=float(pr.group(1)) if pr else None, gratis=free,
                     ai=(ai.group(1) if ai else 'onbekend'), scoreboard=sc, soort=kind))
json.dump(rows, open(sys.argv[2], 'w'), indent=0)
print('titels', len(rows))
pm = collections.Counter(r['pub'][:7] for r in rows)
for y in ['2023', '2024', '2025', '2026']:
    print(y, sum(v for k, v in pm.items() if k.startswith(y)), ' '.join(f"{k[5:]}:{v}" for k, v in sorted(pm.items()) if k.startswith(y)))
p = [r['prijs'] for r in rows if r['prijs']]
print('met prijs', len(p), 'mediaan', statistics.median(p), 'gem', round(sum(p)/len(p), 2))
r26 = [r for r in rows if r['pub'] >= '2026-01']
p26 = [r['prijs'] for r in r26 if r['prijs']]
print('2026: titels', len(r26), 'mediaanprijs', statistics.median(p26) if p26 else None)
ai = collections.Counter('geen AI' if 'without' in r['ai'] else ('onbekend' if 'report' in r['ai'] or r['ai'] == 'onbekend' else 'wel AI') for r in rows)
print('AI', dict(ai))
ai26 = collections.Counter('geen AI' if 'without' in r['ai'] else ('onbekend' if 'report' in r['ai'] or r['ai'] == 'onbekend' else 'wel AI') for r in r26)
print('AI 2026', dict(ai26))
print('apps', sum(r['soort'] == 'app' for r in rows))
