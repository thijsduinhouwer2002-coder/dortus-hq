# Sem, run 19 (17 nov 2026): welke aangekondigde bureaubladspellen hebben een vaste dag op de pagina?
# Leest de releasedatum-tekst opnieuw uit appdetails (openbare winkel-API), rustig 1,5 s per spel.
import csv,json,re,sys,time,urllib.request
from datetime import datetime
bron='platformen/steam/marketing/data/volgers-binnenkort-2026-11-16.csv'
uit=sys.argv[1]
rows=list(csv.DictReader(open(bron)))
def soort(d):
    for f in ('%d %b, %Y','%b %d, %Y','%d %B, %Y','%B %d, %Y'):
        try: return 'vaste dag',datetime.strptime(d,f).date().isoformat()
        except: pass
    if re.search(r'Q\d|quarter',d,re.I): return 'kwartaal',''
    if re.match(r'^[A-Za-z]+ \d{4}$',d): return 'maand',''
    if re.match(r'^\d{4}$',d): return 'jaar',''
    return 'binnenkort',''
out=[]
for x in rows:
    url=f"https://store.steampowered.com/api/appdetails?appids={x['appid']}&cc=nl&l=english&filters=release_date"
    try:
        j=json.load(urllib.request.urlopen(url,timeout=20))[x['appid']]
        rd=j['data']['release_date'] if j.get('success') else None
    except Exception as e:
        rd=None
    tekst=rd['date'] if rd else ''
    s,dag=soort(tekst) if rd and rd.get('coming_soon') else (('uit' if rd else 'onbekend'),'')
    out.append(dict(appid=x['appid'],naam=x['naam'],datumtekst=tekst,soort=s,dag=dag,volgers_16nov=x['volgers']))
    time.sleep(1.5)
w=csv.DictWriter(open(uit,'w',newline=''),fieldnames=list(out[0]))
w.writeheader(); w.writerows(out)
