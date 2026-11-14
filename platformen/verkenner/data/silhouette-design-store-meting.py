# Meting Silhouette Design Store, Vera 14 nov 2026.
# Stap 1: artiestenlijst https://www.silhouettedesignstore.com/artist?p=1..6 (pagina 7+ herhaalt pagina 1), alle links marketplace/seller/profile/shop/<naam>.
# Stap 2: elke profielpagina met curl opgehaald (4 tegelijk, pauze 0,5 s). Op het profiel staat: "<volgers> Followers <aantal> Designs Joined: <maand jaar>".
# Stap 3: dit script leest de csv en telt per jaar van aansluiten.
import csv,statistics as st
from datetime import datetime
r=[x for x in csv.DictReader(open('silhouette-design-store-artiesten-2026-11-14.csv')) if x['joined']]
for y in range(2024,2027):
    g=[int(x['followers']) for x in r if datetime.strptime(x['joined'],'%b %Y').year==y]
    print(y,len(g),'mediaan volgers',st.median(g),'100+',sum(v>=100 for v in g))
