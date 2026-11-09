# Leest Cocos Store detailpagina's (server-rendered) en haalt velden uit window.__NUXT__ zonder code uit te voeren
import re, json, sys, time, urllib.request


def args_list(s):
    out = []; i = 0
    while i < len(s):
        c = s[i]
        if c in ' ,\n':
            i += 1; continue
        if c == '"':
            j = i + 1
            while s[j] != '"':
                j += 2 if s[j] == '\\' else 1
            out.append(json.loads(s[i:j + 1])); i = j + 1
        else:
            m = re.match(r'(void 0|null|true|false|-?[\d.]+(?:e[+-]?\d+)?|\{\}|\[\])', s[i:])
            if not m:
                out.append('?'); j = s.find(',', i); i = len(s) if j < 0 else j; continue
            t = m.group(1)
            out.append({'void 0': None, 'null': None, 'true': True, 'false': False, '{}': {}, '[]': []}.get(t, t)); i += len(t)
    return out


def parse(h):
    m = re.search(r'window\.__NUXT__=\(function\(([^)]*)\)\{(.*)\}\((.*)\)\);</script>', h, re.S)
    if not m:
        return None
    env = dict(zip(m.group(1).split(','), args_list(m.group(3))))
    body = m.group(2); i = body.find('info:{')
    seg = body[i:i + 300000]

    def f(k):
        mm = re.search(r'[{,]"?' + re.escape(k) + r'"?:("(?:[^"\\]|\\.)*"|[A-Za-z_$][\w$]*|-?[\d.]+)', seg)
        if not mm:
            return None
        v = mm.group(1)
        if v.startswith('"'):
            return json.loads(v)
        if re.match(r'-?[\d.]+$', v):
            return v
        return env.get(v, v)
    return {k: f(k) for k in ['name_en', 'author', 'price_person', 'price_person_en', 'score', 'score_number',
                              'update_time', 'c_time', 'buy_count', 'buycount', 'sale_count', 'sales', 'download_count']}


a, b, st = map(int, sys.argv[1:4])
for id in range(a, b + 1, st):
    try:
        req = urllib.request.Request(f'https://store.cocos.com/app/en/detail/{id}', headers={'User-Agent': 'Mozilla/5.0'})
        h = urllib.request.urlopen(req, timeout=20).read().decode('utf8', 'ignore')
        d = parse(h)
        print(json.dumps({'id': id, **(d or {'err': 'geen nuxt'})}, ensure_ascii=False), flush=True)
    except Exception as e:
        print(json.dumps({'id': id, 'err': str(e)[:60]}), flush=True)
    time.sleep(0.4)
