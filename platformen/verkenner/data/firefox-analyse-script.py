# Telt de Firefox-steekproef: per maand gemaakt, gebruikers per dag (ADU), mediaan en aandelen.
import json,sys,statistics as st
from collections import Counter
d=json.load(open(sys.argv[1]))
print('n',len(d),'oudste',min(a['created'] for a in d)[:10])
print('per maand in steekproef',sorted(Counter(a['created'][:7] for a in d).items()))
def g(lo,hi,naam,f=lambda a:True):
    x=sorted(a['adu'] for a in d if lo<=a['created'][:10]<=hi and f(a))
    print(naam,'n',len(x),'mediaan',st.median(x),'10+',round(100*sum(v>=10 for v in x)/len(x)),'%','100+',round(100*sum(v>=100 for v in x)/len(x)),'%','1000+',sum(v>=1000 for v in x),'top',x[-3:])
g('2026-06-10','2026-08-31','jun-aug 2026')
g('2026-06-10','2026-07-31','jun-jul 2026')
g('2026-06-10','2026-08-31','jun-aug betaald',lambda a:a['requires_payment'])
g('2026-06-10','2026-08-31','jun-aug met reviews',lambda a:a['ratings']>0)
