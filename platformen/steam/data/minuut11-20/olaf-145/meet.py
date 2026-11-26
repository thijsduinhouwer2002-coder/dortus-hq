import re,sys,glob,statistics as st
# meet.py map [-v]: langste stuk zonder koop in minuut 11 tot 20 (660 tot 1200 s), en de eerste zes kopen (minuut 0 tot 11)
d=sys.argv[1]
def gat(p,a,b):
    q=[a]+[x for x in p if a<x<b]+[b]; return max(y-x for x,y in zip(q,q[1:]))
g=[];g4=[];ks=[[] for _ in range(6)];n=[];ont=[];goud=[];eerste=[]
for f in sorted(glob.glob(d+"/*.log")):
    L=open(f).read().splitlines()
    kopen=[float(re.search(r"koop ([\d.]+):",l).group(1)) for l in L if l.startswith("HOL koop ")]
    g.append(gat(kopen,660,1200)); g4.append(gat(kopen,240,1200)); n.append(len(kopen))
    for i in range(6): ks[i].append(kopen[i] if len(kopen)>i else 9999)
    t=0;h=0;v=0
    for l in L:
        m=re.match(r"HOL kroniek ([\d.]+)",l)
        if m: t=float(m.group(1))
        if t<240: continue
        if l.startswith("HOL held binnen"): h+=1
        if re.match(r"HOL kroniek [\d.]+ .*\+\d+$",l): v+=1
    ont.append(1-v/max(1,h))
    m=[re.search(r"goud=(\d+)",l) for l in L if l.startswith("HOL einde")]
    goud.append(int(m[0].group(1)) if m else -1)
    if f.endswith("-r1.log"): eerste.append(round(g[-1]))
    if len(sys.argv)>2: print(f.split('/')[-1],[round(k) for k in kopen],"gat 11-20:",round(g[-1]))
print(f"{d}: runs {len(g)} | gat min 11-20: max {max(g):.0f} med {st.median(g):.0f} onder 180 in {sum(x<180 for x in g)}/{len(g)} | gat min 4-20 max {max(g4):.0f}")
print("  kopen per run %d tot %d | koop 1-6 mediaan: %s" % (min(n),max(n),", ".join("%.0f"%st.median(k) for k in ks)))
print("  eerste run per zaad (gat 11-20): %s | goud op 1200 s mediaan %d | ontsnapt na 240 s: %.0f%%" % (eerste, st.median(goud), 100*st.mean(ont)))
