# Verhaal 30 (Joris): welke onderschriften werken binnen hetzelfde TikTok-account?
# Invoer: map met <account>.json (yt-dlp --flat-playlist -J --playlist-end 600).
# Elk filmpje wordt vergeleken met de mediaan van de 10 filmpjes ervoor en de 10 erna
# van hetzelfde account (zelfde werkwijze als verhaal 27 en 28).
# Uitvoer: tabel per kenmerk + csv met alleen cijfers en kenmerken (geen onderschriften).
# Gebruik: python3 tiktok-onderschrift-analyse.py <map> <uit.csv>
import json, os, re, sys, statistics as st, csv, time, random

map_ = sys.argv[1]; uit = sys.argv[2]
NU = time.time(); GRENS = NU - 14 * 86400
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')

def kenmerken(t):
    tl = t.lower()
    tags = re.findall(r'#\w+', t)
    rest = re.sub(r'#\w+', ' ', t)
    rest = re.sub(r'@[\w.]+', ' ', rest)
    woorden = re.findall(r"[A-Za-z0-9']+", rest)
    eerste = re.split(r'[.!?\n]', rest.strip())[0].lower() if rest.strip() else ''
    k = {
        'vraag': '?' in rest,
        'begint_met_vraag': bool(re.match(r'\s*(how|what|why|would|did you|do you|can you|which|who|is this|should)\b', rest.lower())),
        'getal_in_eerste_zin': bool(re.search(r'\d', eerste)),
        'free': bool(re.search(r'\bfree\b', tl)),
        'link': 'link' in tl,
        'vraagt_volgen': bool(re.search(r'\bfollow\b', tl)),
        'vraagt_reactie': bool(re.search(r'\bcomment|let me know|tell me|\bdrop a\b', tl)),
        'vraagt_bewaren': bool(re.search(r'\bsave (this|it|for)|\bbookmark', tl)),
        'pov': bool(re.search(r'\bpov\b', tl)),
        'uitleg_tip': bool(re.search(r'\bhow to\b|\btutorial\b|\btips?\b|\bhack\b|\btrick\b', tl)),
        'deel_reeks': bool(re.search(r'\bpart \d|\bpt\.? ?\d|\bday \d|\bep(isode)? ?\d', tl)),
        'noemt_iemand': '@' in t,
        'emoji': bool(EMOJI.search(t)),
        'hoofdletterwoord': bool(re.search(r'\b[A-Z]{4,}\b', rest)),
        'geen_tekst': len(woorden) == 0,
    }
    nw = len(woorden)
    k['woorden'] = '0' if nw == 0 else '1-5' if nw <= 5 else '6-15' if nw <= 15 else '16-40' if nw <= 40 else '41+'
    nt = len(tags)
    k['hashtags'] = '0' if nt == 0 else '1-3' if nt <= 3 else '4-6' if nt <= 6 else '7+'
    return k

rijen = []
for f in sorted(os.listdir(map_)):
    if not f.endswith('.json'): continue
    acc = f[:-5]
    try: d = json.load(open(os.path.join(map_, f)))
    except Exception: continue
    es = [e for e in d.get('entries') or [] if e.get('timestamp') and e.get('view_count') is not None]
    es.sort(key=lambda e: e['timestamp'])
    for i, e in enumerate(es):
        if e['timestamp'] > GRENS: continue
        buren = [x['view_count'] for x in es[max(0, i-10):i] + es[i+1:i+11]]
        if len(buren) < 10: continue
        ref = st.median(buren)
        if ref <= 0: continue
        t = e.get('description') or e.get('title') or ''
        k = kenmerken(t)
        rijen.append(dict(account=acc, id=e['id'], datum=time.strftime('%Y-%m-%d', time.gmtime(e['timestamp'])),
                          views=e['view_count'], ratio=round(e['view_count']/ref, 3), **k))

with open(uit, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rijen[0].keys())); w.writeheader(); w.writerows(rijen)

accs = sorted({r['account'] for r in rijen})
print('filmpjes', len(rijen), 'accounts', len(accs))

def per_account(sel_ja, sel_nee, min_n=8):
    """per account mediaan ratio met en zonder; geeft lijst verhoudingen (met/zonder)."""
    out = []
    for a in accs:
        ja = [r['ratio'] for r in rijen if r['account'] == a and sel_ja(r)]
        nee = [r['ratio'] for r in rijen if r['account'] == a and sel_nee(r)]
        if len(ja) >= min_n and len(nee) >= min_n:
            out.append(st.median(ja) / st.median(nee))
    return out

def rapport(naam, sel):
    ja = [r['ratio'] for r in rijen if sel(r)]
    nee = [r['ratio'] for r in rijen if not sel(r)]
    if len(ja) < 30:
        print(f'{naam:22s} te weinig ({len(ja)})'); return
    pa = per_account(sel, lambda r: not sel(r))
    beter = sum(1 for x in pa if x > 1)
    hit_ja = sum(1 for x in ja if x >= 3) / len(ja); hit_nee = sum(1 for x in nee if x >= 3) / len(nee)
    # bootstrap over accounts voor de mediaan van de per-account verhouding
    bs = []
    random.seed(1)
    for _ in range(2000):
        s = [random.choice(pa) for _ in pa]
        bs.append(st.median(s))
    bs.sort()
    ci = (bs[50], bs[1949]) if pa else (0, 0)
    print(f'{naam:22s} n={len(ja):5d} ({len(ja)/len(rijen):4.0%}) med {st.median(ja):.2f} vs {st.median(nee):.2f} | '
          f'hit3x {hit_ja:4.0%} vs {hit_nee:4.0%} | accounts {beter}/{len(pa)} beter, med per account {st.median(pa) if pa else 0:.2f} '
          f'[{ci[0]:.2f}-{ci[1]:.2f}]')

for k in ['vraag','begint_met_vraag','getal_in_eerste_zin','free','link','vraagt_volgen','vraagt_reactie','vraagt_bewaren',
          'pov','uitleg_tip','deel_reeks','noemt_iemand','emoji','hoofdletterwoord','geen_tekst']:
    rapport(k, lambda r, k=k: r[k])
for groep, waarden in [('woorden', ['0','1-5','6-15','16-40','41+']), ('hashtags', ['0','1-3','4-6','7+'])]:
    for v in waarden:
        rapport(f'{groep}={v}', lambda r, g=groep, v=v: r[g] == v)
