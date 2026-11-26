import re,sys,glob,statistics as st
d=sys.argv[1]; k1=[];k2=[];g12=[];g0=[];n=[];k3=[]
def gat(p,a,b):
    q=[a]+[x for x in p if a<x<b]+[b]; return max(y-x for x,y in zip(q,q[1:]))
for f in sorted(glob.glob(d+"/*.log")):
    L=open(f).read().splitlines()
    k=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ")]
    k+= [9999]*3
    k1.append(k[0]);k2.append(k[1]);k3.append(k[2]);g12.append(k[1]-k[0]);g0.append(gat(k,k[0],1200));n.append(len([x for x in k if x<9999]))
med=st.median
print(f"{d}: runs {len(k1)} | koop1 med {med(k1):.0f} | koop2 med {med(k2):.0f} | gat 1-2 med {med(g12):.0f} max {max(g12):.0f}, boven 170: {sum(x>170 for x in g12)} | koop3 med {med(k3):.0f} | langste gat na koop1 tot 1200 med {med(g0):.0f} max {max(g0):.0f} | kopen tot 1200: {min(n)}-{max(n)}")
g2=[];ont=[]
for f in sorted(glob.glob(d+"/*.log")):
    L=open(f).read().splitlines()
    k=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ")]
    g2.append(gat(k,660,1200))
    t=0;h=0;v=0
    for l in L:
        m=re.match(r"HOL kroniek ([\d.]+)",l)
        if m: t=float(m.group(1))
        if t<240: continue
        if l.startswith("HOL held binnen"): h+=1
        if re.match(r"HOL kroniek [\d.]+ .*\+\d+$",l): v+=1
    ont.append(1-v/max(1,h))
print(f"   gat min 11-20 med {med(g2):.0f} max {max(g2):.0f} onder 180: {sum(x<180 for x in g2)}/{len(g2)} | ontsnapt na 240 s {100*st.mean(ont):.0f}%")
