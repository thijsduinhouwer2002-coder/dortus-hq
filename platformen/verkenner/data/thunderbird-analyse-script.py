# Telt nieuwe Thunderbird-extensies per periode: gebruikers per dag (ADU), mediaan en aandeel 100+.
import json,sys,statistics as st
from collections import Counter
d=json.load(open(sys.argv[1]))
print('totaal',len(d))
print('nieuw per maand 2025-2026',sorted(Counter(a['created'][:7] for a in d if a['created']>='2025-01').items()))
def groep(lo,hi,naam):
    g=[a for a in d if lo<=a['created'][:7]<=hi]
    u=sorted(a['average_daily_users'] for a in g)
    if not u: return
    print(naam,'n',len(g),'mediaan',st.median(u),'10+',round(100*sum(x>=10 for x in u)/len(u)),'%','100+',round(100*sum(x>=100 for x in u)/len(u)),'%','1000+',sum(x>=1000 for x in u),'top',u[-5:])
groep('2026-05','2026-08','mei-aug 2026')
groep('2026-02','2026-05','feb-mei 2026')
groep('2025-05','2025-10','mei-okt 2025')
groep('2000','2099','alles')
pay=[a for a in d if a.get('requires_payment')]
print('requires_payment',len(pay),[ (a['slug'],a['average_daily_users']) for a in pay][:15])
