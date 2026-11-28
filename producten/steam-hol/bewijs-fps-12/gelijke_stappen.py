import sys,collections
for fn in sys.argv[1:]:
    seq=collections.defaultdict(list)
    for l in open(fn):
        if not l.startswith("STAPX"): continue
        _,i,x,st,f=l.split(); seq[i].append((int(f),float(x),float(st)))
    goed=tot=0
    for i,s in seq.items():
        moves=[];lastf=None
        for k in range(1,len(s)):
            f,x,st=s[k]; pf,px,_=s[k-1]
            if pf!=f-1: lastf=None; continue
            n=round(abs(x-px)/st)
            if n>0:
                if lastf is not None: moves.append((f-lastf,n))
                lastf=f
        if len(moves)<5: continue
        c=collections.Counter(moves); m=c.most_common(1)[0][1]
        goed+=m; tot+=len(moves)
    print(fn.split('/')[-1], f"gelijke stappen {goed}/{tot} = {100*goed/max(tot,1):.0f}%")
