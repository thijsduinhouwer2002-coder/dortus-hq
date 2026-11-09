# Analyse VTuber-tools op itch (9 nov run 08:31). Gebruik: python3 -I vtuber-itch-analyse-script.py RSS_MAP PAGINA.jsonl
# RSS_MAP: map met rss1.xml.. van https://itch.io/tools/newest/tag-vtuber.xml?page=N (datum per item). PAGINA.jsonl: uit itch-pagina-script.py.
import sys,glob,re,json,email.utils,datetime,statistics as st
from collections import Counter
rss={}
for f in glob.glob(sys.argv[1]+'/rss*.xml'):
    for b in re.findall(r'<item>(.*?)</item>',open(f).read(),re.S):
        u=re.search(r'<link>(.*?)</link>',b).group(1).strip()
        rss[u]={'pub':email.utils.parsedate_to_datetime(re.search(r'<pubDate>(.*?)</pubDate>',b).group(1)),
                'maak':(re.search(r'<createDate>(.*?)</createDate>',b) or [0,''])[1]}
P={json.loads(l)['url']:json.loads(l) for l in open(sys.argv[2])}
print('rss',len(rss),'pagina',len(P))
c=Counter(v['pub'].strftime('%Y-%m') for v in rss.values()); print('per maand (RSS pubDate)',sorted(c.items()))
def soort(r):
    t=' '.join(r['tags']).lower()+' '+(r['title'] or '').lower()
    if re.search(r'overlay|obs|widget|alert|chat box|bracket|credits|goal',t): return 'overlay/OBS'
    if re.search(r'pngtuber|png tuber',t): return 'pngtuber'
    if re.search(r'vtube studio|vts|warudo|vnyan|vseeface|plugin|tracking|lipsync',t): return 'plugin/tracking'
    return 'overig'
rows=[]
for u,v in rss.items():
    r=P.get(u)
    if not r: continue
    r=dict(r); r['d']=v['pub']; r['soort']=soort(r)
    r['betaald']=bool(r['price']) and float(r['price'])>0 and not r['pwyw']
    rows.append(r)
def blok(naam,L):
    rs=[r['ratings'] for r in L]
    if not rs: print(naam,0); return
    print(f"{naam}: n={len(L)} mediaan={st.median(rs)} 0={sum(x==0 for x in rs)} 3+={sum(x>=3 for x in rs)} 10+={sum(x>=10 for x in rs)}")
oud=[r for r in rows if r['d']<datetime.datetime(2026,8,9,tzinfo=datetime.timezone.utc)]
jong=[r for r in rows if r not in oud]
print('ouder dan 3 maanden',len(oud),'jonger',len(jong))
blok('oud alle',oud); blok('oud betaald',[r for r in oud if r['betaald']]); blok('oud gratis/pwyw',[r for r in oud if not r['betaald']])
for s in ['overlay/OBS','pngtuber','plugin/tracking','overig']:
    blok('oud '+s,[r for r in oud if r['soort']==s]); blok('jong '+s,[r for r in jong if r['soort']==s])
print('AI-melding jong',sum(1 for r in jong if r['ai']),'van',len(jong),'| oud',sum(1 for r in oud if r['ai']),'van',len(oud))
print('jong betaald',sum(r['betaald'] for r in jong),'prijzen',sorted(float(r['price']) for r in jong if r['betaald']))
mk=Counter(r['url'].split('//')[1].split('.')[0] for r in jong); print('makers jong top',mk.most_common(5))
print('--- top op ratings (alle)')
for r in sorted(rows,key=lambda r:-r['ratings'])[:15]: print(r['ratings'],r['d'].date(),r['price'],r['pwyw'],r['soort'],(r['title'] or '')[:60])
