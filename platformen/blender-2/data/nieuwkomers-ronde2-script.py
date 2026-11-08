# Ronde 2 (Olaf, 8 nov 2026): nieuwkomers (10 maanden of jonger) met 100+ verkopen op Superhive.
# Bron: data van Vera (top 600 add-ons op verkoop, 8 nov; steekproef 7 nov), zelf alleen gefilterd.
# Gebruik: python3 -I nieuwkomers-ronde2-script.py <map platformen/verkenner/data>
import json,re,sys,collections
d=sys.argv[1]
def m(p):
    p=(p or 'x').lower()
    if 'day' in p or 'hour' in p: return 0
    x=re.search(r'(\d+) months',p)
    return int(x.group(1)) if x else (1 if 'month' in p else 99)
def s(v): return int((v or '0').rstrip('+').replace(',',''))
top=[json.loads(l) for l in open(d+'/superhive-top600-beoordelingen-2026-11-08.jsonl')]
print('# top 600, 10 maanden of jonger')
for r in sorted([r for r in top if m(r['published'])<=10],key=lambda r:-s(r['sales'])):
    print(r['sales'],'|',r['published'],'|',r['prijs'],'|',r['slug'],'|',r['categorie'])
st=[json.loads(l) for l in open(d+'/superhive-steekproef-2026-11-07.jsonl')]
mk=collections.defaultdict(list)
for r in st: mk[r['maker']].append(r)
print('# steekproef 7 nov, 100+, met andere producten van dezelfde maker in de steekproef')
for r in sorted([r for r in st if s(r['sales'])>=100],key=lambda r:-s(r['sales'])):
    o=[x for x in mk[r['maker']] if x is not r]
    print(r['sales'],'|',r['published'],'|',r['price'],'|',r['url'].split('/')[-1],'|',r['maker'],'| andere:',len(o),sum(s(x['sales']) for x in o),'|',r['cat'])
