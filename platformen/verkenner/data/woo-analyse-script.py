# Analyse van woo-haal-script.py-uitvoer. Gebruik: python3 -I woo-analyse-script.py woo*.jsonl
import sys,json,statistics as st,datetime as dt,collections as C
rs={}
for f in sys.argv[1:]:
    for l in open(f):
        r=json.loads(l); rs[r["url"]]=r
rs=list(rs.values())
fout=[r for r in rs if "fout" in r]; ok=[r for r in rs if r.get("datum")]
print("pagina's",len(rs),"fout",len(fout),"met datum",len(ok))
for r in ok: r["d"]=dt.datetime.strptime(r["datum"],"%B %d, %Y").date()
def p(x):
    try: return float(x)
    except: return None
print("types",C.Counter(r.get("type") for r in ok).most_common())
print("thema",sum(1 for r in ok if r.get("isTheme")),"door Woo",sum(1 for r in ok if r.get("developedByWoo")))
per=C.Counter((r["d"].year,r["d"].month) for r in ok if r["d"].year>=2025)
print("nieuw per maand",sorted(per.items()))
pl=[r for r in ok if r.get("isPlugin") and not r.get("developedByWoo") and r.get("installations") is not None]
def groep(naam,g):
    if not g: print(naam,"leeg"); return
    i=[r["installations"] for r in g]
    print(f"{naam}: n={len(g)} mediaan={st.median(i)} 100+={sum(x>=100 for x in i)/len(g):.0%} 1000+={sum(x>=1000 for x in i)/len(g):.0%} 0={sum(x==0 for x in i)/len(g):.0%} reviews>=1={sum((r['numberOfReviews'] or 0)>=1 for r in g)/len(g):.0%}")
    pr=[p(r.get("prijs")) for r in g if p(r.get("prijs"))]
    if pr: print("   mediaanprijs",st.median(pr),"gratis/0",sum(1 for r in g if not p(r.get('prijs'))))
    print("   type",C.Counter(r.get("type") for r in g).most_common(4))
D=dt.date
groep("plugins mei-aug 2026",[r for r in pl if D(2026,5,1)<=r["d"]<=D(2026,8,31)])
groep("plugins jan-apr 2026",[r for r in pl if D(2026,1,1)<=r["d"]<=D(2026,4,30)])
groep("plugins 2025",[r for r in pl if r["d"].year==2025])
groep("plugins 2024",[r for r in pl if r["d"].year==2024])
groep("plugins voor 2024",[r for r in pl if r["d"].year<2024])
groep("plugins sep-nov 2026",[r for r in pl if r["d"]>=D(2026,9,1)])
# geld-GOK: actieve installs x jaarprijs x 70% / 12, alleen betaald
print("\nnieuwe betaalde plugins sinds 2025 met 100+ installs (GOK maandbedrag = installs x prijs x 0,7 / 12):")
for r in sorted([r for r in pl if r["d"]>=D(2025,1,1) and r["installations"]>=100 and p(r.get("prijs"))],key=lambda r:-r["installations"]*p(r["prijs"])):
    print(f'  {r["d"]} {r["installations"]:>6} ${p(r["prijs"]):>6.0f} ~${r["installations"]*p(r["prijs"])*0.7/12:>7.0f}/mnd  {r["productName"]} | {r["vendorName"]} | {r["type"]}')
# maker: hoeveel producten heeft de maker in totaal
vc=C.Counter(r.get("vendorName") for r in ok)
print("\nmakers totaal",len(vc),"met 1 product",sum(1 for v in vc.values() if v==1))
