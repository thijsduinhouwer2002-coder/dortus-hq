import re,sys,statistics as S
for d in sys.argv[1:]:
    cpu=[float(x) for x in open(d+'/cpu-per-10s.txt').read().split()]
    log=open(d+'/hol.log').read()
    ev=[(float(t),w) for t,w in re.findall(r'HOL (?:kroniek|slijm|regel)?\s*([\d.]+)[^\n]*?(flat|up again)',log)]
    held={}
    for t,h in re.findall(r'meting t=([\d.]+) beelden=\d+ helden=(\d+)',log): held[int(float(t))//10]=int(h)
    plat=[0]*(len(cpu)+5); st=None
    for t,w in ev:
        if w=='flat': st=t
        elif st is not None:
            for b in range(int(st)//10,int(t)//10+1): plat[b]=1
            st=None
    # cpu index i ~ meting window i+1 (lag -1)
    rows=[(cpu[i],plat[i+1] if i+1<len(plat) else 0,held.get(i+1,0)) for i in range(len(cpu))]
    def g(f): v=[c for c,p,h in rows if f(p,h)]; return "%.2f (n%d)"%(S.mean(v),len(v)) if v else "-"
    print(d,"plat-events",len([e for e in ev if e[1]=='flat']),"| geen held, niet plat",g(lambda p,h:h==0 and not p),"| geen held, plat",g(lambda p,h:h==0 and p),"| held, niet plat",g(lambda p,h:h>0 and not p),"| held, plat",g(lambda p,h:h>0 and p))
