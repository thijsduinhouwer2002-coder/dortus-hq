"""Hoeveel zaden zien Two for one in het eerste uur na de koop (kegel, 0,50, ridder-klap). Draai: python3 -I platformen/steam/data/sim-rolsteen-kegel/eerste-uur.py"""
import os,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kegel as K, rolsteen as R
K.KEGEL["aan"]=True
ns=R.bron(steen_basis=0.50, edel_goud=2, mis_klap="ridder")
hits=0; n=0; ts=[]
for z in range(1,101):
    st=ns["speel"](3.0,z,R.spec(True))
    ks=[x[0] for x in st["aankopen"] if x[1]=="tegen_rolsteen"]
    if not ks: continue
    n+=1; ts.append(ks[0]/60)
# per-seed count in first hour after purchase: run until purchase+60 min
import statistics as S
for z in range(1,101):
    st=ns["speel"](3.0,z,R.spec(True))
    ks=[x[0] for x in st["aankopen"] if x[1]=="tegen_rolsteen"]
    if not ks: continue
    st2=ns["speel"]((ks[0]+3600)/3600.0,z,R.spec(True))
    hits+= st2["steen"]["twee"]>=1
print("zaden met steen",n,"mediaan koop",S.median(ts),"Two for one in eerste uur na koop:",hits)
