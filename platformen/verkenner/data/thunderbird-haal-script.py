# Haalt alle Thunderbird-extensies via de open API van addons.thunderbird.net, nieuwste eerst.
# Gebruik: python3 thunderbird-haal-script.py uit.json
import json,sys,subprocess,time
out=[];page=1
while True:
    u=f'https://addons.thunderbird.net/api/v4/addons/search/?app=thunderbird&type=extension&sort=created&page_size=50&page={page}'
    d=json.loads(subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout)
    for a in d['results']:
        out.append({k:a.get(k) for k in ['slug','created','last_updated','average_daily_users','weekly_downloads','ratings','is_experimental','authors','homepage','contributions_url','requires_payment','summary','current_version']})
    print(page,len(out),flush=True)
    if not d.get('next'): break
    page+=1; time.sleep(0.5)
for a in out:
    a['authors']=[x.get('name') for x in (a['authors'] or [])]
    v=a.pop('current_version') or {}; a['compat']=v.get('compatibility'); a['version']=v.get('version')
    s=a.get('summary'); a['summary']=(s.get('en-US') if isinstance(s,dict) else s)
json.dump(out,open(sys.argv[1],'w'))
