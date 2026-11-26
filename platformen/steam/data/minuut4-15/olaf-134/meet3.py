import re,sys,glob,statistics as st
for d in sys.argv[1:]:
    gk=[];leeg=[]
    for f in sorted(glob.glob(d+"/*.log")):
        L=open(f).read().splitlines()
        k=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ")]
        eind=min(720,k[5]) if len(k)>5 else 720
        q=[240]+[x for x in k if 240<x<eind]+[eind]
        gk.append(max(y-x for x,y in zip(q,q[1:])))
        leeg.append(max(0,720-k[5]) if len(k)>5 else 0)
    print(d,"gat met iets te koop (4-12): max %.0f, onder 180 in %d/%d | winkel leeg voor 12 min: %d runs, langst %.0f s"%(max(gk),sum(x<180 for x in gk),len(gk),sum(x>0 for x in leeg),max(leeg)))
