import json,sys,collections,statistics,os
D=sys.argv[1]
it=json.load(open(D+'/items.json')); cr=json.load(open(D+'/creators.json')); tot=json.load(open(D+'/totals.json'))
print('uniek',len({i['id'] for i in it}))
for k,v in tot.items(): print(v,k)
def pr(i): 
    try: return float(i['priceData']['current'].replace('$',''))
    except: return None
ps=[pr(i) for i in it if pr(i) is not None]
print('prijs mediaan',statistics.median(ps),'gem',round(sum(ps)/len(ps),2),'gratis',sum(1 for p in ps if p==0),'abonnement',sum(i['subscription'] for i in it),'bundel',sum(i['isBundle'] for i in it))
bycat=collections.defaultdict(set); pc=collections.defaultdict(list)
for i in it:
    for c in i['categoryLabels']: bycat[c].add(i['creator']['slug']); pc[c].append(pr(i) or 0)
for c in bycat: print(c,'makers',len(bycat[c]),'items',len(pc[c]),'mediaanprijs',statistics.median(pc[c]))
m=collections.Counter(i['sitemap_lastmod'][:7] for i in it if i['sitemap_lastmod']); print('lastmod per maand',sorted(m.items()))
cr.sort(key=lambda c:-c['downloadCount'])
for c in cr[:10]: print(c['name'],c['downloadCount'],c['approvedPackageCount'])
print('makers <=3 items',sum(c['approvedPackageCount']<=3 for c in cr))
print('nieuwste 10:',[ (i['title'],i['creator']['name'],i['categoryLabels']) for i in it[:10]])
