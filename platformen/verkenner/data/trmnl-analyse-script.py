import json, sys, statistics as st, collections as c
d=json.load(open(sys.argv[1]))
for r in d:
    r['m']=r['published_at'][:7]; r['con']=r['stats']['installs']+r['stats']['forks']
print('totaal',len(d), 'connections totaal', sum(r['con'] for r in d))
per=c.defaultdict(list)
for r in d: per[r['m']].append(r['con'])
print('maand  aantal  mediaan  %50+  %100+  max')
for m in sorted(per):
    v=per[m]; print(m, len(v), st.median(v), round(100*sum(x>=50 for x in v)/len(v)), round(100*sum(x>=100 for x in v)/len(v)), max(v))
# makers
auth=c.Counter(); ac=c.Counter()
for r in d: auth[r['user_id']]+=r['con']; ac[r['user_id']]+=1
tot=sum(auth.values())
print('makers',len(auth))
q=[r for r in d if r['con']>=50]
print('recipes met 50+ (drempel fonds):',len(q),'van makers:',len({r['user_id'] for r in q}))
qa=c.Counter()
for r in q: qa[r['user_id']]+=r['con']
qt=sum(qa.values())
print('top 15 makers (aandeel connections bij 50+ recipes, aantal recipes):')
for u,v in qa.most_common(15): print(u, v, round(100*v/qt,1),'%', ac[u])
print('top 15 recipes:')
for r in sorted(d,key=lambda r:-r['con'])[:15]: print(r['con'], r['published_at'][:10], r['user_id'], r['name'])
cat=c.Counter((r.get('author_bio') or {}).get('category','?') for r in d)
print(cat.most_common(25))
