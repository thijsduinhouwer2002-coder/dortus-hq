import json,subprocess,time,sys,urllib.parse
uit=sys.argv[1]; apps=[]; tok=None
while True:
    u='https://marketplace.zoom.us/api/v1/marketplaceV2/homepage/search?pageSize=100'+('&nextPageToken='+urllib.parse.quote(tok) if tok else '')
    r=subprocess.run(['curl','-sS','-m','40',u],capture_output=True,text=True); d=json.loads(r.stdout)
    apps+= [{k:a.get(k) for k in ('id','displayName','companyName','categories','agentApp')} for a in d['apps']]
    tok=d.get('nextPageToken')
    if not tok or not d['apps']: break
    time.sleep(1)
json.dump(apps,open(uit,'w')); print(len(apps),d.get('total'))
