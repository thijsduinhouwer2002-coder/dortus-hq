# Gebruik: python3 -I trefwoord.py <map met analyse-soort.json en details.jsonl> <regex> [<regex> ...]
# Telt per trefwoord de Desktop Companion-apps (titel, korte tekst, labels) en toont de grootste.
import json,re,sys
d={x['appid']:x for x in json.load(open(sys.argv[1]+'/analyse-soort.json'))}
rows=[json.loads(l) for l in open(sys.argv[1]+'/details.jsonl')]
for kw in sys.argv[2:]:
    hits=[]
    for r in rows:
        a=d.get(r['appid'],{})
        txt=(a.get('title','')+' '+(r.get('short') or '')+' '+' '.join(r.get('tags') or [])).lower()
        if re.search(kw,txt): hits.append((a.get('rev') or 0,a.get('pos'),a.get('price'),a.get('rel'),a.get('title','')[:40]))
    hits.sort(reverse=True)
    print(f'== {kw}: {len(hits)} apps, reviews samen {sum(h[0] for h in hits)}')
    for h in hits[:8]: print('   ',h)
