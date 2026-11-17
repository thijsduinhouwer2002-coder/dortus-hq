import re,sys,statistics as S
for d in sys.argv[1:]:
    cpu=[float(x) for x in open(d+'/cpu-per-10s.txt').read().split()]
    m=[(float(a),int(b),int(c),int(e)) for a,b,c,e in re.findall(r'meting t=([\d.]+) beelden=(\d+) helden=(\d+) hol_vast=(\d+)',open(d+'/hol.log').read())]
    bl=[x[1] for x in m]; hv=[0]+[m[i][3]-m[i-1][3] for i in range(1,len(m))]; hd=[x[2] for x in m]
    def cor(a,b):
        n=min(len(a),len(b)); a,b=a[:n],b[:n]
        return S.correlation(a,b) if n>3 else 0
    best=max(range(-3,4),key=lambda L: cor(cpu[max(0,L):], bl[max(0,-L):]))
    L=best; c=cpu[max(0,L):]; n=min(len(c),len(bl)-max(0,-L))
    b2=bl[max(0,-L):][:n]; h2=hv[max(0,-L):][:n]; hd2=hd[max(0,-L):][:n]; c=c[:n]
    print(d, "lag",L,"n",n,"cor beelden %.2f hol_vast %.2f helden %.2f"%(cor(c,b2),cor(c,h2),cor(c,hd2)),
          "| gem beelden/10s %.0f, hol_vast per 10s %.2f, cpu %.2f"%(S.mean(bl),S.mean(hv),S.mean(cpu)))
    # cpu per beeld
    print("   cpu-ms per beeld %.1f; cpu bij helden=0: %.2f, >=1: %.2f" % (1000*sum(c)/sum(b2), S.mean([x for x,h in zip(c,hd2) if h==0] or [0]), S.mean([x for x,h in zip(c,hd2) if h>0] or [0])))
