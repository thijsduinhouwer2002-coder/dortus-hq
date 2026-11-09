import json,sys,statistics as st
oud={}
for l in open(sys.argv[1]):
    d=json.loads(l); oud[d['slug']]=d
rows=[]
for l in open(sys.argv[2]):
    d=json.loads(l); o=oud.get(d['slug'])
    if not o or d['downloads'] is None or o['downloads'] is None: continue
    eerste=min(o.get('datums') or o.get('reviewdatums') or ['9999'])
    rows.append((d['downloads']-o['downloads'],o['downloads'],d['downloads'],eerste,d['maker'],d['titel']))
uren=float(sys.argv[3])
f=24/uren
rows.sort(reverse=True)
print('n',len(rows),'uren',uren)
ds=[r[0]*f for r in rows]
print('mediaan per dag',st.median(ds),'nul',sum(1 for r in rows if r[0]==0),'neg',sum(1 for r in rows if r[0]<0))
for drempel in (10,30,100,300):
    print('>=',drempel,'/dag:',sum(1 for x in ds if x>=drempel))
jong=[r for r in rows if r[3]>='2025-07-01']
print('jong (eerste review sinds jul 2025):',len(jong))
for r in jong: print(round(r[0]*f,1),r[1],r[3],r[4],'|',r[5])
print('top 25 alle:')
for r in rows[:25]: print(round(r[0]*f,1),r[1],r[3],r[4],'|',r[5])
