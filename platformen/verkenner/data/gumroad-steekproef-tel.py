import sys,re,html,json,glob,hashlib,statistics as st
rows=[]
for u in open('sample.txt').read().split():
    f='pages/'+hashlib.md5((u+'\n').encode()).hexdigest()[:12]+'.html'
    try: t=html.unescape(open(f,errors='ignore').read())
    except: continue
    if len(t)<3000: rows.append(dict(u=u,ok=0)); continue
    rc=re.search(r'"ratings":\{"count":(\d+)',t); sc=re.search(r'"sales_count":(null|\d+)',t)
    pc=re.search(r'"price_cents":(\d+)',t); cur=re.search(r'"currency_code":"(\w+)"',t)
    title=re.search(r'<title[^>]*>([^<]*)',t)
    rows.append(dict(u=u,ok=1,r=int(rc.group(1)) if rc else None,s=None if not sc or sc.group(1)=='null' else int(sc.group(1)),p=int(pc.group(1)) if pc else None,c=cur.group(1) if cur else None,t=title.group(1)[:60] if title else ''))
json.dump(rows,open('rows.json','w'))
ok=[r for r in rows if r['ok']]; paid=[r for r in ok if r['p']]
print('totaal',len(rows),'leesbaar',len(ok),'betaald',len(paid),'gratis/pwyw0',len(ok)-len(paid))
for name,g in [('alle',ok),('betaald',paid)]:
    rr=[r['r'] or 0 for r in g]
    print(name,'>=1 rating',sum(x>=1 for x in rr),'>=5',sum(x>=5 for x in rr),'>=20',sum(x>=20 for x in rr))
    sv=[r for r in g if r['s'] is not None]
    print(name,'met teller',len(sv),'teller>=1',sum(r['s']>=1 for r in sv),'>=10',sum(r['s']>=10 for r in sv),'>=100',sum(r['s']>=100 for r in sv))
print('mediaan prijs (cent, betaald)',st.median([r['p'] for r in paid]) if paid else None)
for r in sorted(ok,key=lambda r:-(r['r'] or 0)-(r['s'] or 0))[:15]: print(r['r'],r['s'],r['p'],r['c'],r['t'],r['u'])
