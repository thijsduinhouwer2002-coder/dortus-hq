# Bram 17 nov: CPU per 10 s gesplitst naar held in beeld (helden) en of het vaste beeld opnieuw tekende (hol_vast).
# "stil" = geen held en geen nieuw vast beeld: wat kost het spel als er niets gebeurt (vraag Sanne 03:15).
# Gebruik: python3 cpu_stil.py <map> [<map> ...]   (map met cpu-per-10s.txt en hol.log van tak schermen)
import re,sys,statistics as S
def lees(d):
    cpu=[float(x) for x in open(d+'/cpu-per-10s.txt').read().split()]
    m=[(float(a),int(b),int(c),int(e)) for a,b,c,e in re.findall(r'meting t=([\d.]+) beelden=(\d+) helden=(\d+) hol_vast=(\d+)',open(d+'/hol.log').read())]
    bl=[x[1] for x in m]
    def cor(a,b):
        n=min(len(a),len(b)); return S.correlation(a[:n],b[:n]) if n>3 else 0
    L=max(range(-3,4),key=lambda L: cor(cpu[max(0,L):], bl[max(0,-L):]))   # zelfde uitlijning als cpu_per_beeld.py
    c=cpu[max(0,L):]; mm=m[max(0,-L):]; n=min(len(c),len(mm))
    return [(mm[i][0],c[i],mm[i][1],mm[i][2],mm[i][3]-(mm[i-1][3] if i else mm[i][3])) for i in range(n)]
for d in sys.argv[1:]:
    rows=lees(d); print(d)
    for naam,f in [('stil (geen held, vast gelijk)',lambda r:r[3]==0 and r[4]==0),('geen held, vast nieuw',lambda r:r[3]==0 and r[4]>0),
                   ('held in beeld',lambda r:r[3]>0)]:
        sel=[r for r in rows if f(r)]
        if sel: print('  %-30s n=%3d  cpu %.2f  beelden/10s %3.0f  ms per beeld %.1f'%(naam,len(sel),S.mean(r[1] for r in sel),
                      S.mean(r[2] for r in sel),1000*sum(r[1] for r in sel)/max(1,sum(r[2] for r in sel))))
    print('  alles: cpu %.3f  ms per beeld %.1f'%(S.mean(r[1] for r in rows),1000*sum(r[1] for r in rows)/sum(r[2] for r in rows)))
