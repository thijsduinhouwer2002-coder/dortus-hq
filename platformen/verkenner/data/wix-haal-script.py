# Haalt alle subcategorie-pagina's van de Wix App Market (openbare HTML, eerste 48 apps per subcategorie plus totaal).
# Gebruik: python3 wix-haal-script.py uit.json
import re,base64,json,sys,time,subprocess
def page(url):
    s=subprocess.run(['curl','-s','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
    for k,v in re.findall(r"window\.(__\w+)\s*=\s*JSON\.parse\(__decodeBase64\('([A-Za-z0-9+/=]+)'\)\)",s):
        if k=='__REACT_QUERY_STATE__': return json.loads(base64.b64decode(v).decode())
home=page('https://www.wix.com/app-market/category/marketing')
side=[q for q in home['queries'] if q['queryKey']==['get-dynamic-sidebar-items']][0]['state']['data']['sections']
subs=[(c['categoryLink']['slug'],s['slug']) for c in side if c['type']=='CATEGORY_LINK' for s in c['categoryLink'].get('subCategoryLinks',[])]
out={}
for cat,sub in subs:
    d=page(f'https://www.wix.com/app-market/category/{cat}/{sub}')
    for q in d['queries']:
        if q['queryKey'][0].startswith('initial-apps-fetch'):
            x=q['state']['data']; out[f'{cat}/{sub}']={'total':x['paging']['total'],'apps':x['appGroup']['apps']}
            print(cat,sub,x['paging']['total'],len(x['appGroup']['apps']),flush=True)
    time.sleep(1)
json.dump(out,open(sys.argv[1],'w'))
