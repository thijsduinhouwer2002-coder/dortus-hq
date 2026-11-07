# Analyse van Superhive add-ons: verkopen per leeftijdsgroep (Published) voor betaalde add-ons.
# Gebruik: python3 -I superhive-analyse-script.py addonurls.txt superhive.jsonl
import sys, json, re, statistics, collections
# Tweede vorm: python3 -I superhive-analyse-script.py sitemap superhive_sm.jsonl  (steekproef uit de sitemap, add-ons via subcategorie)
ADDON={'modeling','rendering-scripts-and-addons','rigging-scripts-and-addons','materials-and-shading-addons','interface','import-export','asset-management','animation-scripts-and-addons','vse'}
rs={}
if sys.argv[1]=='sitemap':
    urls=[]
    steek=set(u.strip() for u in open(sys.argv[3]))  # derde argument: de steekproeflijst (elke 3e url)
    for l in open(sys.argv[2]):
        j=json.loads(l)
        if j['code']=='200' and j['url'] in steek and ADDON & set(j.get('cat') or []): rs[j['url']]=j; urls.append(j['url'])
else:
    urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
    pos={u:i for i,u in enumerate(urls)}
    for l in open(sys.argv[2]):
        j=json.loads(l)
        if j['code']=='200' and j['url'] in pos: rs[j['url']]=j
def verk(s):
    if not s: return 0          # geen regel Sales = minder dan 10 (aanname, zie voorstel)
    return int(re.sub(r'\D','',s))
def maanden(p):
    if not p: return None
    if 'year' in p: return 12*int(re.sub(r'\D','',p) or 1)
    if 'month' in p: return int(re.sub(r'\D','',p) or 1)
    return 0
groep=collections.defaultdict(list)
for u,j in rs.items():
    m=maanden(j['published'])
    if j.get('price') is None or j['price']<=0: continue
    groep[m].append(j)
print('opgehaald',len(rs),'van',len(urls))
for m in sorted(k for k in groep if k is not None):
    g=groep[m]; v=[verk(j['sales']) for j in g]
    n=len(v)
    print(f"{m:>2} mnd n={n:4d} mediaan={statistics.median(v):5.0f} 10+={100*sum(x>=10 for x in v)/n:4.0f}% 50+={100*sum(x>=50 for x in v)/n:4.0f}% 100+={100*sum(x>=100 for x in v)/n:4.0f}% 500+={100*sum(x>=500 for x in v)/n:4.0f}% mediaanprijs={statistics.median(j['price'] for j in g):.0f}")
# venster 2 tot 6 maanden
w=[j for m in (2,3,4,5,6) for j in groep.get(m,[])]
if w:
    v=sorted(verk(j['sales']) for j in w); n=len(v)
    print('VENSTER 2-6 mnd betaald n=',n,'mediaan',statistics.median(v),'10+',sum(x>=10 for x in v),'50+',sum(x>=50 for x in v),'100+',sum(x>=100 for x in v),'500+',sum(x>=500 for x in v))
    omzet=[(verk(j['sales'])*(0.65*j['price']-0.49),j) for j in w]  # 70% min 5% betaalkosten min $0,49 per verkoop
    omzet.sort(key=lambda x:-x[0])
    print('ondergrens netto (teller x (65% van lijstprijs min $0,49)):')
    for o,j in omzet[:20]: print(f"  ${o:8.0f} {j['sales']:>6} ${j['price']:6.2f} {j['published']:>14} {j['maker']} {j['url'].split('/')[-1]}")
    makers=collections.Counter(j['maker'] for j in w)
    print('makers',len(makers),'meeste producten',makers.most_common(5))
    print('aantal boven $300/mnd ondergrens:',sum(1 for o,j in omzet if o/max(1,maanden(j['published']))>=300))
gratis=sum(1 for u,j in rs.items() if j.get('price') is not None and j['price']<=0)
print('gratis (prijs 0) overgeslagen:',gratis)
