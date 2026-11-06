import json,sys,datetime,collections as C
apps={}
for f in sys.argv[1:]:
    for a in json.load(open(f)): apps[a['id']]=a
D=lambda x:datetime.datetime.fromtimestamp(x/1000,datetime.UTC).date()
T={'1':'wijzerplaat','2':'app','3':'widget','4':'dataveld','5':'muziek'}
isp=lambda a: bool(a.get('pricing') and a['pricing'].get('salePrice'))
def rep(sel,label):
    n=len(sel)
    if not n: print(label,0);return
    dl=sorted(a['downloadCount'] for a in sel)
    med=dl[n//2]
    p=lambda k: round(100*sum(1 for x in dl if x>=k)/n,1)
    print(f"{label}: n={n} mediaan-emmer={med}+ 10+={p(10)}% 100+={p(100)}% 1000+={p(1000)}% 10000+={p(10000)}%")
print("uniek",len(apps))
lo,hi=datetime.date(2026,5,6),datetime.date(2026,8,6)
win=[a for a in apps.values() if a['firstApprovalDate'] and lo<=D(a['firstApprovalDate'])<=hi]
rep(win,"ALLES mei-aug 2026")
for t in T: rep([a for a in win if a['typeId']==t],"  "+T[t])
rep([a for a in win if isp(a)],"  betaald")
rep([a for a in win if not isp(a)],"  gratis")
for t in ['1','2','4','3']:
    rep([a for a in win if isp(a) and a['typeId']==t],"  betaald "+T[t])
    rep([a for a in win if not isp(a) and a['typeId']==t],"  gratis "+T[t])
# ouder venster voor vergelijking
lo2,hi2=datetime.date(2025,11,1),datetime.date(2026,2,28)
win2=[a for a in apps.values() if a['firstApprovalDate'] and lo2<=D(a['firstApprovalDate'])<=hi2]
rep(win2,"ALLES nov25-feb26")
rep([a for a in win2 if isp(a)],"  betaald nov25-feb26")
for t in ['2','4']: rep([a for a in win2 if isp(a) and a['typeId']==t],"  betaald nov25-feb26 "+T[t])
# makers: aantal apps per maker in venster
dev=C.Counter(a['developerId'] for a in win)
print("makers in venster",len(dev),"top",[(c) for d,c in dev.most_common(10)])
print("apps van makers met <=5 apps in venster:",sum(c for c in dev.values() if c<=5))
rep([a for a in win if dev[a['developerId']]<=5],"  kleine makers (<=5 nieuw)")
rep([a for a in win if dev[a['developerId']]<=5 and a['typeId']!='1'],"  kleine makers geen wijzerplaat")
rep([a for a in win if dev[a['developerId']]<=5 and a['typeId']!='1' and isp(a)],"  kleine makers geen wijzerplaat betaald")
# betaald totaal
P=[a for a in apps.values() if isp(a)]
print("betaald totaal",len(P), "met 1000+",sum(a['downloadCount']>=1000 for a in P),"10000+",sum(a['downloadCount']>=10000 for a in P))
pr=sorted(a['pricing']['salePrice']['price'] for a in P); print("prijsmediaan",pr[len(pr)//2], C.Counter(a['pricing']['salePrice']['currencyCode'] for a in P).most_common(3))
print("betaald per maand eerste goedkeuring",sorted(C.Counter(D(a['firstApprovalDate']).strftime('%Y-%m') for a in P if a['firstApprovalDate']).items())[-14:])
print("betaald 1000+ geen wijzerplaat, eerste goedkeuring >=2025-06:")
for a in sorted(P,key=lambda a:-a['downloadCount']):
    if a['downloadCount']>=1000 and a['typeId']!='1' and D(a['firstApprovalDate'])>=datetime.date(2025,6,1):
        print("  ",a['downloadCount'],a['pricing']['salePrice']['price'],T[a['typeId']],D(a['firstApprovalDate']),a['developer'],'|',a['naam'][:50],'| makerapps',sum(1 for b in apps.values() if b['developerId']==a['developerId']))
