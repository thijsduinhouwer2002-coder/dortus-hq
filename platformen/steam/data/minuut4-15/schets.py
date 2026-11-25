# Ruwe schets minuut 4 tot 15 (Sanne 25 nov). GOK: geen spel, een model. Ijking: oude regels moeten
# koop 2 rond 555 tot 660 s geven (Iris, logs zaad 2 tot 5, GEZIEN).
import random, statistics as st, sys
def run(seed, k=0.62, B=6, pech=99, geluk=False, geluk_x=1, prijzen=None, put_na_gloop=False, T=900):
    r = random.Random(seed)
    prijzen = prijzen or {"slijm":[45,126,353],"stekelput":[45,126,353]}
    niv = {"slijm":0,"stekelput":0}; goud=0; t=0.0; plat_tot=-1; vlucht_rij=0; geluk_aan=False
    kopen=[]; vangsten=[7.6,25.2,73.4]; sinds={}
    goud = 40; held_t = 94.0  # BEGIN: vaste helden; log zaad 3 had 50 goud op 192 s na 4 vangsten (GEZIEN), dus ±40 na het begin
    while t < T:
        t = held_t
        # held komt; kansen per verdediging (held.gd), een deel helden keert om of is terugkomer: ijkfactor k
        ps = (0.45+0.07*niv["slijm"])*k if t>plat_tot else 0
        pp = (0.35+0.07*niv["stekelput"])*k
        valt = r.random() < 1-(1-ps)*(1-pp)
        dwing = vlucht_rij >= pech or geluk_aan
        if valt or dwing:
            buit = B + r.choice([0,0,3,3,6]) + 1
            if geluk_aan: buit *= geluk_x
            goud += buit; vangsten.append(t+17); vlucht_rij=0; geluk_aan=False
            if r.random()<0.5: plat_tot = t+17+(60 if niv["slijm"]<2 else 40)
        else:
            vlucht_rij += 1
        held_t = t + r.uniform(28,38) + r.uniform(0,10)  # gat plus wachten op max 2 tegelijk
        # koper: koopt goedkoopste die kan (na 8 s)
        for s in ["slijm","stekelput"]:
            if put_na_gloop and s=="stekelput" and niv["slijm"]==0: continue
            if niv[s]<3 and goud>=prijzen[s][niv[s]]:
                goud -= prijzen[s][niv[s]]; niv[s]+=1; kopen.append(t+20)
                if geluk: geluk_aan=True
                break
    return kopen, vangsten
def meet(**kw):
    k2=[];n15=[];gat=[];vg=[]
    for sd in range(300):
        kopen,v = run(sd,**kw)
        k2.append(kopen[1] if len(kopen)>1 else 900)
        n15.append(len(kopen))
        punten=[240]+[x for x in kopen if 240<x<900]+[900]
        gat.append(max(b-a for a,b in zip(punten,punten[1:])))
        vv=[240]+[x for x in v if 240<x<900]+[900]
        vg.append(max(b-a for a,b in zip(vv,vv[1:])))
    k1=[(run(sd,**kw)[0] or [900])[0] for sd in range(300)]
    return "koop1 %3.0f koop2 %3.0f  kopen<15min %.1f  langste gat zonder koop min4-15 %3.0f s  langste gat zonder vangst %3.0f s" % (st.median(k1),st.median(k2),st.mean(n15),st.median(gat),st.median(vg))

for k in [0.5,0.6,0.7,0.8]:
    print("ijk k=%.1f" % k, meet(k=k))
K=float(sys.argv[1]) if len(sys.argv)>1 else 0.6
print("nu                 ", meet(k=K))
print("pech 2             ", meet(k=K,pech=2))
print("pech2+geluk x2     ", meet(k=K,pech=2,geluk=True,geluk_x=2))
P={"slijm":[45,90,250],"stekelput":[30,80,200]}
print("+put30 na G, 90/80 ", meet(k=K,pech=2,geluk=True,geluk_x=2,put_na_gloop=True,prijzen=P))
print("+B9                ", meet(k=K,B=9,pech=2,geluk=True,geluk_x=2,put_na_gloop=True,prijzen=P))
P2={"slijm":[45,70,200],"stekelput":[25,60,160]}
print("B9 45/25 70/60     ", meet(k=K,B=9,pech=2,geluk=True,geluk_x=2,put_na_gloop=True,prijzen=P2))
P3={"slijm":[45,90,250],"stekelput":[45,80,200]}
print("KEUS B9 45/45 90/80 ", meet(k=K,B=9,pech=2,geluk=True,geluk_x=2,prijzen=P3))
print("KEUS zonder geluk   ", meet(k=K,B=9,pech=2,prijzen=P3))
