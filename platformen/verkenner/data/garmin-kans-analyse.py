import json,glob,collections as C,datetime as D
A={}
for f in glob.glob('*_*.json')+['datafield.json']:
    try:
        for a in json.load(open(f)): A[a['id']]=a
    except Exception: pass
A=[a for a in A.values() if a['type']!='1']
NEW={'318','319','320','326','327','328','337','343','344','345','348','349','350','351','352','353','354'}
FR970={'320'}
def d(ms): return D.datetime.utcfromtimestamp(ms/1000).date() if ms else None
for a in A:
    a['rel']=d(a['release']); a['f']=d(a['first']); dv=set(a['devs']); a['fr970']=bool(dv&FR970); a['nieuw']=len(dv&NEW); a['ndev']=len(dv)
    a['betaald']=bool(a['pay']) or bool(a['extsub'])
print('apps (geen wijzerplaat)',len(A),C.Counter(a['type'] for a in A))
P=[a for a in A if a['betaald']]
print('betaald',len(P),'pay',sum(bool(a['pay']) for a in P),'extsub',sum(bool(a['extsub']) for a in P))
big=[a for a in P if a['dl']>=1000]
print('betaald 1000+',len(big))
oud=lambda a:a['rel'] and a['rel']<D.date(2025,5,1)
print('betaald 1000+, laatste versie voor mei 2025:',sum(oud(a) for a in big),' zonder FR970:',sum(not a['fr970'] for a in big))
json.dump(A,open('alles.json','w'),default=str)
