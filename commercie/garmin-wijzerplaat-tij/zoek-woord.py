import json, subprocess, urllib.parse, sys
B='https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords'
w=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
u=f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex=0&pageSize={n}&sortType=mostRelevant&appType=watchface"
d=json.loads(subprocess.run(['curl','-s','-m','40',u],capture_output=True,text=True).stdout)
print(w,'totaal',d['totalCount'])
for i,a in enumerate(d['apps'],1):
    loc=[l for l in a.get('appLocalizations',[]) if l.get('locale')=='en'] or a.get('appLocalizations',[{}])
    pr=((a.get('pricing') or {}).get('salePrice') or {}).get('price',0)
    print(i, (loc[0].get('name') or '')[:60], '|', a.get('downloadCount'), '| $',pr)
