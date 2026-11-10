# Bram 10 nov: hoe snel vult het Heldenboek (Sanne: "Hoe lang het meegaat, GOK, Bram meet na")
import random
import os
BRON=os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim.py")
src=open(BRON).read().split('if __name__ == "__main__"')[0]
O1='                uit = "gevallen"\n'; assert src.count(O1)==1
src=src.replace(O1,O1+'                BOEK.setdefault((h.get("soort",""), v["soort"]), t)\n')
O2='            st["gevlucht"] += 1\n'; assert src.count(O2)==1
src=src.replace(O2,O2+'            BOEK.setdefault((h.get("soort",""), "vlucht"), t)\n')
def med(x): x=sorted(x); return x[len(x)//2]
ns={"BOEK":{}}; exec(src,ns); ns["SOORTEN"]=True
hfd1=[]; hoed10=[]; b1000=[]; b3000=[]; magput=[]
for z in range(1,9):
    ns["BOEK"].clear()
    st=ns["speel"](140,z)
    B=ns["BOEK"]; need=[(s,w) for s in ["","ridder","dief","magier","bard"] for w in ["slijm","put","vlucht"]]
    hfd1.append(max(B.get(k,9e9) for k in need)/3600); magput.append(B.get(("magier","put"),9e9)/3600)
    ht=st["hap_tijden"]; r=random.Random(z); seen=set(); tt=None
    for i,tm in enumerate(ht):
        seen.add(r.randrange(10))
        if len(seen)==10: tt=tm; break
    hoed10.append(tt/3600 if tt else 9e9)
    b1000.append(ht[999]/3600 if len(ht)>=1000 else 9e9); b3000.append(ht[2999]/3600 if len(ht)>=3000 else 9e9)
for n,x in [("hoofdstuk 1 vol (15 stempels)",hfd1),("magier in de put",magput),("alle 10 hoeden (willekeurige hoed)",hoed10),("berg 1000",b1000),("berg 3000",b3000)]:
    print("%-36s min %.1f mediaan %.1f max %.1f uur open tijd"%(n,min(x),med(x),max(x)))
