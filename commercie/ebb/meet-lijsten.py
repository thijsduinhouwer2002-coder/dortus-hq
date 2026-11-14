# Chris, 14 nov 2026: plek van Ebb in de lijsten van de Connect IQ-winkel.
# Gebruik: python3 meet-lijsten.py <sortType> <appType of -> <aantal paginas van 30>
# sortType: hotFresh ("Hot & Fresh Apps"), mostRecent ("New and Updated Apps"), trending, mostPopular, highestRated.
import json,subprocess,sys,datetime
B="https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"
sort,typ,pages=sys.argv[1],sys.argv[2],int(sys.argv[3])
EBB="5280653d-1681-452d-8c03-7cbdc7284641"
allx=[]
for p in range(pages):
    u=f"{B}?startPageIndex={p*30}&pageSize=30&sortType={sort}"+(f"&appType={typ}" if typ!="-" else "")
    r=subprocess.run(["curl","-s","--max-time","40",u],capture_output=True,text=True).stdout
    try: d=json.loads(r)
    except: print("fout",p,r[:100]); break
    if not d: break
    allx+=d
json.dump(allx,open(f"{sort}-{typ}.json","w"))
for i,a in enumerate(allx):
    if a['id']==EBB or 'Ebb' in a['appLocalizations'][0]['name']:
        print("Ebb-achtig op plek",i+1,a['appLocalizations'][0]['name'])
def t(ms): return datetime.datetime.fromtimestamp(ms/1000,datetime.UTC).strftime('%m-%d %H:%M') if ms else '-'
print(len(allx),"apps; eerste:",t(allx[0].get('firstApprovalDate')),"laatste firstApproval:",t(allx[-1].get('firstApprovalDate')))
for k in ['firstApprovalDate','releaseDate','creationDate']:
    v=[a.get(k) for a in allx[:5]]; print(k,[t(x) for x in v])
