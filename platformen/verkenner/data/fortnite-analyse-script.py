import json,statistics as st,collections,sys
R=[json.loads(l) for l in open(sys.argv[1])]
print("totaal",len(R),"fouten",collections.Counter(r.get('err') for r in R))
R=[r for r in R if r.get('creatorCode')!='epic' and r.get('createdIn')]
def s(r,k):
    m=r['m']; 
    if not m: return 0
    return sum(v['value'] or 0 for v in m[k])
def mx(r,k):
    m=r['m']
    if not m: return 0
    return max([v['value'] or 0 for v in m[k]]+[0])
for groep,G in [("alle makers",R),("UEFN",[r for r in R if r['createdIn']=='UEFN']),("FNC",[r for r in R if r['createdIn']=='FNC'])]:
    n=len(G); up=[s(r,'uniquePlayers') for r in G]; mins=[s(r,'minutesPlayed') for r in G]; ccu=[mx(r,'peakCCU') for r in G]
    act=sum(1 for u in up if u>0)
    print(f"\n{groep}: n={n}")
    print(" eilanden met enige dag >=5 spelers (zichtbaar):",act,f"{100*act/n:.1f}%")
    print(" mediaan som unieke spelers 7 dagen:",st.median(up))
    for d in [100,700,1000,7000]:
        k=sum(1 for u in up if u>=d);print(f"  som 7d unieke >= {d}: {k} ({100*k/n:.2f}%)")
    for d in [2,10,100]:
        k=sum(1 for c in ccu if c>=d);print(f"  piek CCU >= {d}: {k} ({100*k/n:.2f}%)")
    # geld: $1100 per miljoen minuten, x 30/7
    geld=[m*30/7*1100/1e6 for m in mins]
    for d in [10,100,1000]:
        k=sum(1 for g in geld if g>=d);print(f"  GOK maandgeld >= ${d}: {k} ({100*k/n:.2f}%)")
    print(" som minuten 7d:",sum(mins))
# positie in lijst tegenover activiteit
print("\nactiviteit per tiende van de lijst (positie):")
for b in range(10):
    G=[r for r in R if b*28613<=r['pos']<(b+1)*28613]
    a=sum(1 for r in G if s(r,'uniquePlayers')>0)
    print(b,len(G),f"{100*a/max(1,len(G)):.1f}%")
