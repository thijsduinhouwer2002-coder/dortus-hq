import random,sys
OUD=["Bram","Odo","Wout","Gerda","Pim","Rik","Mara","Joost","Fenna","Tibbe","Lotte","Kees"]
NIEUW=OUD+["Henk","Geert","Teun","Siem","Kobus","Jop","Femke","Ineke","Anouk","Merel","Elke","Maud"]
def run(namen,nieuw,seed,T=75*60,gap=30):
    r=random.Random(seed);cnt={};terug=[];hol=[];pens=[];recent=[];log=[]
    t=0
    while t<T:
        t+=r.uniform(gap*0.5,gap*1.5)
        hol=[h for h in hol if h[1]>t]; terug=[h for h in terug if h[1]>t]
        bezet={h[0].split()[0] for h in hol+terug}
        vrij=[n for n in namen if n not in bezet]
        z=[n for n in vrij if n not in pens]; vrij=z or vrij
        if not vrij: vrij=list(namen)
        if not nieuw:
            nooit=[n for n in vrij if n not in cnt]
            if nooit: nm=r.choice(nooit)
            else:
                kan=[n for n in vrij if cnt[n]<3]
                if not kan:
                    nm=r.choice(vrij); cnt.pop(nm)
                else:
                    b=r.choice(kan); nm=b+(" II" if cnt[b]==1 else " III")
        else:
            if all(cnt.get(n,0)>=3 for n in vrij): cnt={}
            k=[n for n in vrij if n not in recent[-6:]] or vrij
            lo=min(cnt.get(n,0) for n in k); b=r.choice([n for n in k if cnt.get(n,0)==lo])
            c=cnt.get(b,0); nm=b+["", " II", " III"][min(c,2)]
            recent.append(b)
        log.append((t,nm))
        b=nm.split()[0]
        if r.random()<0.9: cnt[b]=cnt.get(b,0)+1; hol.append((nm,t+20))
        else: terug.append((nm,t+r.uniform(300,900)))
        if r.random()<0.02: pens=(pens+[b])[-5:]
    # Iris check
    worst=0;fam=0
    for i,(t0,_) in enumerate(log):
        w={}
        for t1,n in log:
            if t0<=t1<t0+600: w[n.split()[0]]=w.get(n.split()[0],0)+1
        worst=max(worst,max(w.values()))
    for i in range(len(log)-2):
        a=[log[i+j][1].split()[0] for j in range(3)]
        if a[0]==a[1]: fam+=1
    return worst,fam,len(log)
for nm,lab,nw in [(OUD,"oud",False),(NIEUW,"nieuw24",True),(OUD,"nieuw12",True)]:
    res=[run(nm,nw,s) for s in range(200)]
    print(lab,"max per 10min:",max(x[0] for x in res),"gem",sum(x[0] for x in res)/200,"direct na elkaar runs:",sum(1 for x in res if x[1]),"helden",res[0][2])
