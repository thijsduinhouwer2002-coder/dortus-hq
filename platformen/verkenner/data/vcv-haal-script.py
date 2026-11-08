# VCV Rack Library: haalt alle plugins via de open API en meet bereik per lichting.
# Gebruik: python3 vcv-haal-script.py   (popularity = totaal downloads/abonnementen, alleen bij gratis plugins)
import json,urllib.request,datetime as dt,statistics as st,collections
d=json.load(urllib.request.urlopen('https://api.vcvrack.com/library/manifests?version=2'))['manifests']
v=list(d.values()) if isinstance(d,dict) else d
f=lambda t:dt.datetime.fromtimestamp(t,dt.UTC).strftime('%Y-%m')
print('plugins',len(v),'premium',sum(1 for x in v if x.get('premium')))
for lo,hi in [('2025-01','2025-12'),('2026-02','2026-07'),('2026-09','2026-11')]:
    pop=[x['popularity'] for x in v if lo<=f(x['creationTimestamp'])<=hi and not x.get('premium') and 'popularity' in x]
    if pop: print(lo,hi,'n',len(pop),'mediaan',st.median(pop),'min',min(pop),'100+',sum(p>=100 for p in pop)/len(pop))
print(sorted(collections.Counter(f(x['creationTimestamp']) for x in v if f(x['creationTimestamp'])>='2025-01').items()))
