import sys, os, re, random, glob, json
base = sys.argv[1]
def load(path):
    d = {}
    if not os.path.exists(path): return d
    txt = open(path, encoding='utf-8', errors='replace').read()
    lines = txt.split('\n'); i = 0; buf = ''
    for raw in lines:
        line = raw.rstrip('\r')
        if not buf and (line.strip().startswith('#') or line.strip().startswith('!') or not line.strip()): continue
        if line.endswith('\\') and not line.endswith('\\\\'):
            buf += line[:-1].lstrip() if buf else line[:-1]; continue
        line = (buf + line.lstrip()) if buf else line; buf = ''
        m = re.match(r'\s*((?:\\.|[^=:\s])+)\s*[=:\s]\s*(.*)$', line)
        if m: d[m.group(1)] = m.group(2)
    return d
ph = lambda s: sorted(re.findall(r'\{(\d+)', s))
tags = lambda s: sorted(t.lower() for t in re.findall(r'</?([a-zA-Z]+)', s))
def mn(s): return len(re.findall(r'(?<![&\\])&(?![&#a-zA-Z]+;)|_(?=\w)', s)) if False else s.count('&') - 2*s.count('&&')
tot = {}
samples = []
for lang in ['fr','es']:
    t = dict(keys=0, missing=0, same=0, ph=0, tags=0, mnem=0)
    for f in sorted(glob.glob(f'{base}/en/*.properties')):
        n = os.path.basename(f)
        en = load(f); tr = load(f'{base}/{lang}j/messages/{n}')
        for k, v in en.items():
            t['keys'] += 1
            if k not in tr: t['missing'] += 1; continue
            w = tr[k]
            if w == v and re.search(r'[a-z]{3,} [a-z]{3,}', v): t['same'] += 1
            if ph(w) != ph(v): t['ph'] += 1
            if tags(w) != tags(v): t['tags'] += 1
            if ('&' in v and '&' not in w): t['mnem'] += 1
            if lang == 'fr' and len(v) > 12 and re.search(r'[a-z]{3,} [a-z]{3,}', v): samples.append((n, k, v, w))
    tot[lang] = t
print(json.dumps(tot, indent=1))
random.seed(8112026)
with open(sys.argv[2], 'w') as o:
    for n, k, v, w in random.sample(samples, 120):
        o.write(f'{n} | {k}\nEN: {v}\nFR: {w}\n\n')
