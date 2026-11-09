import json,subprocess,time,sys
land=sys.argv[1]; taal=sys.argv[2]; uit=sys.argv[3]
H=['-H','Accept: application/json','-H','X-Block-Cookies: true']
def get(u):
    r=subprocess.run(['curl','-sS','-m','40']+H+[u],capture_output=True,text=True)
    return json.loads(r.stdout)
base='https://squareup.com/app-marketplace/api/partner_application_categories'
cats=get(f'{base}?country={land}&language_code={taal}')['partner_application_categories']
apps={}
for c in cats:
    p=1
    while True:
        time.sleep(3)
        d=get(f"{base}/{c['name_key']}?country={land}&language_code={taal}&limit=100&page={p}")
        pa=d['partner_applications']; 
        for a in pa['data']: a.pop('pricing_tiers_x',None); apps[a['id']]=a
        if p*100>=pa['total'] or not pa['data']: break
        p+=1
    print(c['name_key'],pa['total'],len(apps),flush=True)
json.dump(list(apps.values()),open(uit,'w'))
