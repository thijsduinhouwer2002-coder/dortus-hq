import re,sys
CAT=[("lied",r"sang about your hole|song got popular|A song about you"),
 ("bard",r"the Bard tunes|hums on the way in|is here for a story"),
 ("dief",r"the Thief tiptoes|sneaks in\. Nobody|picks the lock"),
 ("magier",r"the Wizard sniffs|casts Light|knows every trap"),
 ("ridder",r"clanks in\.|polished up for this|is very slow\. Very sure"),
 ("trek",r"yawns\. Long walk|brought a pillow|the Sleepy|holds grudges|the Spiteful|keeps a list of names|slew a dragon|the Boastful|signs autographs"),
 ("aarts",r"Your nemesis|again\. Of course|trained all week"),
 ("terug",r" is back")]
def gaten(pad,eind=1800):
    smal=[];breed=[];gezien=set();liedt=[]
    for l in open(pad,errors="replace"):
        m=re.match(r"HOL hol-niveau \d+ \(faam \d+, t ([\d.]+)\)",l)
        if m: t=float(m[1]); smal.append(t); breed.append(t); continue
        m=re.match(r"HOL eerste koop mogelijk na (\d+) s",l)
        if m: breed.append(float(m[1])); continue
        m=re.match(r"HOL kroniek ([\d.]+) \(wacht [\d.]+\): (.*)$",l)
        if m:
            t=float(m[1]);z=m[2]
            for c,rx in CAT:
                if re.search(rx,z):
                    if c=="lied": smal.append(t); liedt.append(t)
                    if c not in gezien: gezien.add(c); breed.append(t)
                    break
    def g(ts):
        ts=sorted([0]+[t for t in ts if t<=eind]+[eind]); 
        best=max(zip(ts,ts[1:]),key=lambda p:p[1]-p[0]); return (best[1]-best[0])/60,best[0]/60,best[1]/60
    return g(smal),g(breed),liedt
for p in sys.argv[1:]:
    a,b,l=gaten(p)
    print(f"{p.split('/')[-1]}: smal (niveau+lied) {a[0]:.1f} min ({a[1]:.1f}-{a[2]:.1f}); breed (+eerste keer) {b[0]:.1f} min ({b[1]:.1f}-{b[2]:.1f}); lied op {[round(x/60,1) for x in l if x<=1800]}")
