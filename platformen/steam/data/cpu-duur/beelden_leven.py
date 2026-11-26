"""Beelden per 10 s (HOL meting) in aan- en uit-blokken van wissel=leven (#190). Olaf 26 nov 2026. Gebruik: python3 beelden_leven.py <map> [...]"""
import re,sys,statistics as St
for d in sys.argv[1:]:
    uit=open(d+'/uit.txt').read()
    p=[(float(u),float(t)) for u,t in re.findall(r'HOL wissel leven \w+ unix=([\d.]+) t=([\d.]+)',uit) if float(t)>1]
    off=St.median(u-t for u,t in p)
    m=[(float(t)+off,int(b)) for t,b in re.findall(r'HOL meting t=([\d.]+) beelden=(\d+)',open(d+'/hol.log').read())]
    aan=[];uitb=[]
    for u,b in m:
        mid=u-5  # meting telt de 10 s ervoor
        blok=int(mid//20); pos=mid-blok*20
        if 5<=pos<=15:
            (aan if blok%2==0 else uitb).append(b)
    print(d.split('/')[-1], f"aan {St.mean(aan):.1f} beelden/10s (n {len(aan)}), uit {St.mean(uitb):.1f} (n {len(uitb)}), verschil {(St.mean(aan)/St.mean(uitb)-1)*100:+.1f} procent")
