"""Ruwe balansproef voor de eerste speelbare versie van Het Hol (Sanne). Geen vervanging van Bram's sim/, alleen om startgetallen te kiezen.
Speler koopt steeds het goedkoopste wat kan. Meet: tijd tot elke aankoop, langste wachttijd, aandeel vluchters.
Gebruik: python3 -I balans-proef.py"""
import random
random.seed(7)
HELD_ELKE=50          # seconden tussen helden (strook.gd 25-70 s, voortgang.gd 47,5 s)
GOUD_PER_VAL=6       # basisgoud van een gevallen held
def kansen(staat,niveau):
    # kans dat de held valt: elke verdediging op zijn pad heeft een kans, helden worden sterker met faam
    p_blijft=1.0
    for soort,aantal,upg in staat['verd']:
        basis={'slijm':0.30,'put':0.22}[soort]+0.07*upg
        for _ in range(aantal): p_blijft*=1-basis*(0.9**niveau)
    return 1-p_blijft
def winkel(staat):
    w=[]
    if staat['gang']<40: w.append(('graaf',int(5+staat['gang']*1.2),None))
    for i,(soort,aantal,upg) in enumerate(staat['verd']):
        if aantal<4 and staat['gang']>=8*aantal: w.append((f'extra {soort}',int(40*2.6**aantal),i))
        if upg<3: w.append((f'upgrade {soort}',int(60*2.8**upg),i))
    return min(w,key=lambda x:x[1]) if w else None
staat={'gang':6,'verd':[['slijm',1,0],['put',1,0]],'goud':0}
t=0;niveau=0;gevallen=0;gevlucht=0;aankopen=[];vorige=0
while t<12*3600:
    t+=HELD_ELKE
    p=kansen(staat,niveau)
    if random.random()<p:
        gevallen+=1;staat['goud']+=int(GOUD_PER_VAL*(1+0.1*niveau)*(1+staat['gang']/40))
    else: gevlucht+=1
    niveau=(gevallen+gevlucht)//60   # faam: elke 60 helden een niveau sterker en rijker
    while True:
        k=winkel(staat)
        if not k or k[1]>staat['goud']: break
        staat['goud']-=k[1];naam,_,i=k
        if naam=='graaf': staat['gang']+=1
        elif naam.startswith('extra'): staat['verd'][i][1]+=1
        else: staat['verd'][i][2]+=1
        aankopen.append((t,naam,t-vorige));vorige=t
    if not winkel(staat) and 'klaar' not in staat: staat['klaar']=t
print('aankopen:',len(aankopen),'| eerste aankoop na',aankopen[0][0],'s | alles gekocht na',round(staat.get('klaar',0)/3600,1),'uur')
for grens in (1,3,6):
    gaps=[g for (tt,n,g) in aankopen if tt<=grens*3600]
    print(f'tot {grens} uur: {len(gaps)} aankopen, langste wachttijd {max(gaps)//60} min')
tot=gevallen+gevlucht
print('helden',tot,'gevallen',gevallen,'gevlucht',gevlucht,f'= {gevlucht/tot:.0%} vlucht')
# vluchtaandeel per uur
