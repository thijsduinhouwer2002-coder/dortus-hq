import sys, numpy as np
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2] / "commercie/filmpjes/stem")); import splits; SR=splits.SR
def toon(d): t=np.arange(int(d*SR))/SR; return (0.5*np.sin(2*np.pi*220*t)).astype(np.float32)
def st(d): return np.zeros(int(d*SR),np.float32)
# zin1 a b ; gat 0.2 ; zin2 c (0.15) d (0.15) k ; gat 0.5 ; zin3 g h ; 0.45 ; zin4 e f
seg=[("st",0.3),("a",0.3),("st",0.05),("b",0.3),("st",0.2),("c",0.3),("st",0.15),("d",0.3),("st",0.15),("k",0.3),("st",0.5),("g",0.3),("st",0.05),("h",0.3),("st",0.45),("e",0.3),("st",0.05),("f",0.3),("st",0.4)]
x=[];t=0;w=[]
for n,d in seg:
    x.append(st(d) if n=="st" else toon(d))
    if n!="st": w.append([n,t,t+d])
    t+=d
x=np.concatenate(x)+np.random.default_rng(1).normal(0,0.003,int(t*SR)+50)[:sum(len(a) for a in x)].astype(np.float32)
for v in w:
    if v[0]=="b": v[2]+=0.25   # whisper legt eind van b 0,2 s te laat
g=[tuple(v) for v in w if v[0] not in ("c","d","k")]
print("echte gaten: 0.95-1.15 (zin 1|2), 2.35-2.85 (zin 2|3); goed is knip 1 tussen 0.95 en 1.15")
try: print(splits.knip(x,[{"tekst":"a b"},{"tekst":"c d k"},{"tekst":"g h"},{"tekst":"e f"}],g)[1])
except Exception as f: print("FOUT", f)
