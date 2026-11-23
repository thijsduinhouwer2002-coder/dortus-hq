import sys, numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2] / "commercie/filmpjes/stem"))
import splits
SR=splits.SR
def toon(d): t=np.arange(int(d*SR))/SR; return (0.5*np.sin(2*np.pi*220*t)).astype(np.float32)
def st(d): return np.zeros(int(d*SR),np.float32)
# zin1 a (pauze 0.9) b ; 0.5 ; zin2 c d ; 0.4 ; zin3 g h ; 0.45 ; zin4 e f
seg=[("st",0.3),("a",0.3),("st",0.9),("b",0.3),("st",0.5),("c",0.3),("st",0.05),("d",0.3),("st",0.4),("g",0.3),("st",0.05),("h",0.3),("st",0.45),("e",0.3),("st",0.05),("f",0.3),("st",0.4)]
x=[];t=0;woorden=[];gaten=[]
for n,d in seg:
    x.append(st(d) if n=="st" else toon(d))
    if n!="st": woorden.append((n,t,t+d))
    t+=d
x=np.concatenate(x); x=x+np.random.default_rng(1).normal(0,0.003,len(x)).astype(np.float32)
zinnen=[{"tekst":"a b"},{"tekst":"c d"},{"tekst":"g h"},{"tekst":"e f"}]
gehoord=[w for w in woorden if w[0] not in ("c","d")]  # zin 2 helemaal niet verstaan
print("echte gaten: 1.80-2.30, 2.95-3.35, 4.00-4.45")
print(splits.grenzen_whisper(x,zinnen,gehoord))
print(splits.knip(x,zinnen,gehoord)[1])
