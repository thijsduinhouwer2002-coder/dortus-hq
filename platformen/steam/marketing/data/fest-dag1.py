# Sem, run 12 (16 nov 2026): wat deed dag 1 van een thema-fest met de demo's erin?
# Stap 1: per demo het gemiddelde vóór de start (12:50 tot 16:53 UTC) en ná de start (19:36 tot 22:38 UTC) uit de uurmetingen
#         (autobattler-demos-voor-fest-2026-11-16.csv, autobattler-fest-2026-11.csv en tak fest-metingen).
# Stap 2: per spel de uitgavedatum uit de openbare winkel-API appdetails (rustig, 1 verzoek per seconde).
# Uitkomst: autobattler-fest-dag1-2026-11-16.csv (delta, pre, post, maxpost, appid, naam, coming_soon, datum, uitgever).
# Gebruik: python3 fest-dag1.py <csv met kolommen delta,pre,post,maxpost,appid,naam> <uit.csv>
import csv,json,sys,time,urllib.request
rows=list(csv.DictReader(open(sys.argv[1])))
out=[]
for r in rows:
    a=r['appid']
    try:
        req=urllib.request.Request(f"https://store.steampowered.com/api/appdetails?appids={a}&cc=us&l=english",headers={'User-Agent':'Mozilla/5.0'})
        d=json.load(urllib.request.urlopen(req,timeout=20))[a]
        dd=d.get('data',{}) if d.get('success') else {}
        rd=dd.get('release_date',{})
        out.append(dict(r,coming_soon=rd.get('coming_soon'),datum=rd.get('date'),uitgever=';'.join(dd.get('publishers',[]))))
    except Exception:
        out.append(dict(r,coming_soon='',datum='fout',uitgever=''))
    time.sleep(1.0)
w=csv.DictWriter(open(sys.argv[2],'w'),fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
