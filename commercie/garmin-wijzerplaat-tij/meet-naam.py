import json, subprocess, urllib.parse, time, sys, re
B='https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords'
def zoek(w, typ='watchface', n=30):
    u=f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex=0&pageSize={n}&sortType=mostRelevant" + (f"&appType={typ}" if typ else '')
    d=json.loads(subprocess.run(['curl','-s','-m','40',u],capture_output=True,text=True).stdout)
    namen=[]
    for a in d['apps']:
        loc=[l for l in a.get('appLocalizations',[]) if l.get('locale')=='en'] or a.get('appLocalizations',[{}])
        namen.append((loc[0].get('name') or '', a.get('downloadCount'), a.get('appType')))
    return d['totalCount'], namen
for w in sys.argv[1:]:
    t,n=zoek(w); 
    innaam=[x for x in n if re.search(r'\b'+re.escape(w)+r'\b', x[0], re.I)]
    t2,n2=zoek(w,None)
    innaam2=[x for x in n2 if re.search(r'\b'+re.escape(w)+r'\b', x[0], re.I)]
    print(f"{w!r}: wijzerplaten totaal {t}, in naam (top30) {len(innaam)}: {[x[0][:40] for x in innaam[:5]]} | alle soorten totaal {t2}, in naam {len(innaam2)}: {[(x[0][:30],x[2]) for x in innaam2[:4]]}", flush=True)
    time.sleep(1)
