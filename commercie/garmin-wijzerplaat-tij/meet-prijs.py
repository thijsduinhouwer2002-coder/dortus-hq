import json, subprocess, urllib.parse, sys, statistics, collections
B='https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords'
rows={}
for w in ['body battery','stress','body battery stress','data rich','big digits','health']:
  for p in range(2):
    u=f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex={p*30}&pageSize=30&sortType=mostRelevant&appType=watchface"
    try: d=json.loads(subprocess.run(['curl','-s','-m','40',u],capture_output=True,text=True).stdout)
    except Exception as e: print('fout',w,e); continue
    for a in d['apps']:
      loc=[l for l in a.get('appLocalizations',[]) if l.get('locale')=='en'] or a.get('appLocalizations',[{}])
      pr=((a.get('pricing') or {}).get('salePrice') or {}).get('price',0)
      rows[a['id']]=dict(n=(loc[0].get('name') or '')[:55],dl=a.get('downloadCount'),pr=float(pr or 0),w=w,dev=len(a.get('compatibleDeviceTypeIds') or []),rev=(a.get('reviewCount') if 'reviewCount' in a else a.get('averageRating')))
paid=[r for r in rows.values() if r['pr']>0]
print('uniek',len(rows),'betaald',len(paid))
print('mediaan prijs',statistics.median(r['pr'] for r in paid))
print(collections.Counter(r['pr'] for r in paid).most_common(12))
for dl in sorted(set(r['dl'] for r in paid), key=lambda x:str(x)):
  ps=[r['pr'] for r in paid if r['dl']==dl]; print('dl',dl,len(ps),'mediaan',statistics.median(ps))
for r in sorted(paid,key=lambda r:-(r['dl'] or 0))[:25]: print(r)
import csv
with open(sys.argv[1] if len(sys.argv)>1 else 'prijs.csv','w',newline='') as f:
  c=csv.writer(f); c.writerow(['naam','downloads','prijs_usd','zoekwoord','horloges','reviews_of_score'])
  [c.writerow([r['n'],r['dl'],r['pr'],r['w'],r['dev'],r['rev']]) for r in rows.values()]
