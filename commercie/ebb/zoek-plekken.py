# Chris, 16 nov 2026: plek van Ebb in de zoekbalk van de Connect IQ-winkel, eerste 60 treffers.
# Gebruik: python3 zoek-plekken.py <woord> [<woord> ...]   (TYP="&appType=watch-app" voor alleen apps)
import json,subprocess,sys,urllib.parse
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords"
EBB="5280653d-1681-452d-8c03-7cbdc7284641"
import os
TYP=os.environ.get('TYP','')
out={}
for w in sys.argv[1:]:
    res=[]
    for p in (0,30):
        u=f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex={p}&pageSize=30&sortType=mostRelevant"+TYP
        r=subprocess.run(["curl","-s","--max-time","40",u],capture_output=True,text=True).stdout
        try: d=json.loads(r)
        except: print("fout",w,r[:80]); break
        tot=d.get('totalCount'); d=d.get('apps',[])
        if not d: break
        res+=d
    out[w]=res
    ebb=[i+1 for i,a in enumerate(res) if a['id']==EBB]
    print(f"\n== {w}: {tot} treffers, Ebb plek {ebb[0] if ebb else '-'}")
    for i,a in enumerate(res[:8]):
        names={l['locale']:l['name'] for l in a['appLocalizations']}
        hit=[k for k,v in names.items() if w.lower() in v.lower()]
        print(f" {i+1}. {names.get('en') or list(names.values())[0]} | dl {a.get('downloadCount')} | woord in naam: {','.join(hit) or 'nee'}" + ("" if 'en' in hit or not hit else f" ({names[hit[0]]})"))
