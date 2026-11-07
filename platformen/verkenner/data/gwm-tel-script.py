# Vera, 7 nov 2026. Telt de uitkomst van gwm-haal-script.py.
import json, sys, statistics as st, collections as C
def num(s):
    if not s: return None
    s=s.replace(",","").replace("+","").strip(); f={"K":1e3,"M":1e6,"B":1e9}
    try: return float(s[:-1])*f[s[-1]] if s[-1] in f else float(s)
    except: return None
R=[json.loads(l) for l in open(sys.argv[1])]
R=[r for r in R if r.get("ok")]
for r in R: r["u"]=num(r.get("gebruikers_exact") or r.get("gebruikers"))
def show(nm,G):
    u=[r["u"] for r in G if r["u"] is not None]
    if not u: print(nm,"leeg"); return
    print("%-48s n=%5d mediaan=%8.0f 100+=%3.0f%% 1000+=%3.0f%% 10K+=%3.0f%%"%(nm,len(u),st.median(u),
      100*sum(x>=100 for x in u)/len(u),100*sum(x>=1000 for x in u)/len(u),100*sum(x>=10000 for x in u)/len(u)))
show("alle",R)
google=[r for r in R if (r.get("maker") or "").lower().startswith("google")]
print("door Google:",len(google))
P=C.Counter((r.get("prijs") or "?") for r in R); print(P.most_common(8))
for y in ["2024","2025","2026"]:
    show("bijgewerkt in "+y,[r for r in R if (r.get("bijgewerkt") or "").startswith(y)])
show("bijgewerkt mei-aug 2026",[r for r in R if "2026-05"<= (r.get("bijgewerkt") or "")[:7] <="2026-08"])
# cohort op eerste review, alleen als alle reviews zichtbaar zijn
full=[r for r in R if r.get("reviews",0)>0 and len(r["review_datums"])>=r["reviews"]]
print("apps met alle reviewdatums zichtbaar:",len(full),"van",sum(r.get('reviews',0)>0 for r in R),"met reviews")
for a,b,nm in [("2026-05","2026-08","eerste review mei-aug 2026"),("2026-01","2026-04","eerste review jan-apr 2026"),("2025-07","2025-12","eerste review jul-dec 2025")]:
    G=[r for r in full if a<=r["review_datums"][0][:7]<=b]; show(nm,G)
print("--- vervolg: betaald = prijs met 'paid' of 'trial' of 'Paid'")
def betaald(r): p=(r.get("prijs") or "").lower(); return "paid" in p or "trial" in p
print("betaalvorm in hele winkel:",sum(betaald(r) for r in R),"van",len(R))
def nieuw(r,a="2026-05",b="2026-08"):
    if not (a<=(r.get("bijgewerkt") or "")[:7]<=b): return False
    if r.get("reviews",0)==0: return True
    return len(r["review_datums"])>=r["reviews"] and r["review_datums"][0][:7]>=a[:5]+"%02d"%(int(a[5:])-1)
for a,b in [("2026-05","2026-08"),("2026-03","2026-06")]:
    G=[r for r in R if nieuw(r,a,b)]
    show("waarschijnlijk nieuw, bijgewerkt %s..%s"%(a,b),G)
    show("  zonder reviews",[r for r in G if r.get("reviews",0)==0])
    show("  met reviews",[r for r in G if r.get("reviews",0)>0])
    show("  met betaalvorm",[r for r in G if betaald(r)])
    show("  gratis",[r for r in G if not betaald(r)])
