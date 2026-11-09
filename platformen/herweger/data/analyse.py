import json,sys,datetime,statistics as st
from collections import defaultdict
d=json.load(open(sys.argv[1]))
def dt(s): return datetime.datetime.strptime(s,'%b %d, %Y')
groups=defaultdict(list); rows=[]
for x in d:
    h=x.get('hist',{})
    if 'err' in h or not h: continue
    R=dt(x['released']).replace(tzinfo=datetime.timezone.utc).timestamp()
    tot=sum(r['recommendations_up']+r['recommendations_down'] for r in h['rollups'])
    f28=sum(r['recommendations_up']+r['recommendations_down'] for r in h['rollups'] if r['date']<R+28*86400)
    # eerste review kan voor release liggen (playtest/early access): tel die mee in f28
    m=dt(x['released']).strftime('%Y-%m')
    if h['type']!='week': m+='*'
    groups[m].append((f28,tot,x['price'])); rows.append((x['appid'],x['title'],x['released'],x['price'],f28,tot,h['type']))
print('maand  n  med28  >=5in28  >=10in28  >=30in28  med_tot  >=10tot')
for m in sorted(groups):
    g=groups[m]; n=len(g); f=[a for a,_,_ in g]; t=[b for _,b,_ in g]
    pc=lambda v,k: f"{100*sum(1 for a in v if a>=k)//n}%"
    print(m,n,st.median(f),pc(f,5),pc(f,10),pc(f,30),st.median(t),pc(t,10))
json.dump(rows,open(sys.argv[2],'w'),ensure_ascii=False)
