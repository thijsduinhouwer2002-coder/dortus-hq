import re,sys,glob,statistics as st
d=sys.argv[1]
def gat(p,a,b):
    q=[a]+[x for x in p if a<x<b]+[b]; return max(y-x for x,y in zip(q,q[1:]))
g12=[];g15=[];k1=[];k2=[];n=[];vang=[];buit=[]
for f in sorted(glob.glob(d+"/*.log")):
    L=open(f).read().splitlines()
    kopen=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ")]
    v=[(float(m.group(1)),int(m.group(2))) for l in L for m in [re.match(r"HOL kroniek ([\d.]+) .*\+(\d+)$",l)] if m]
    g12.append(gat(kopen,240,720)); g15.append(gat(kopen,240,900)); k1.append(kopen[0]); k2.append(kopen[1] if len(kopen)>1 else 999); n.append(len(kopen))
    vang.append(len(v)); buit+= [b for t,b in v if t>240]
    if len(sys.argv)>2: print(f.split('/')[-1],[round(k) for k in kopen],round(gat(kopen,240,720)),round(gat(kopen,240,900)))
k6=[]
for f in sorted(glob.glob(d+'/*.log')):
    L=open(f).read().splitlines(); kk=[float(re.search(r'koop ([\d.]+):',l).group(1)) for l in L if l.startswith('HOL koop ')]
    k6.append(kk[5] if len(kk)>5 else 999)
print(f"{d}: winkel leeg voor 540 s: {sum(x<540 for x in k6)} | koop6 med {st.median(k6):.0f} | runs {len(g12)} | gat 4-12: max {max(g12):.0f} med {st.median(g12):.0f} onder180 {sum(x<180 for x in g12)}/{len(g12)} | gat 4-15: max {max(g15):.0f} med {st.median(g15):.0f} | koop1 med {st.median(k1):.0f} koop2 med {st.median(k2):.0f} | kopen {min(n)}-{max(n)} | vangsten med {st.median(vang)} | buit na 240 gem {st.mean(buit):.1f}")
fr=[]
for f in glob.glob(d+'/*.log'):
    L=open(f).read().splitlines(); t=0;h=0;v=0
    for l in L:
        m=re.match(r"HOL kroniek ([\d.]+)",l)
        if m: t=float(m.group(1))
        if t<240: continue
        if l.startswith("HOL held binnen"): h+=1
        if re.match(r"HOL kroniek [\d.]+ .*\+\d+$",l): v+=1
    fr.append(1-v/h)
print("   ontsnapt na 240 s: %.0f%%"%(100*st.mean(fr)))
