import json,urllib.request,time
H={'User-Agent':'Mozilla/5.0','Api-Version-Date':'2026-11-14-1'}
def get(url): return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=60))
def all_(q):
    out=[];after=None
    while True:
        d=get('https://api.whop.com/api/v1/apps?first=100&include_total_count=true&'+q+(f'&after={after}' if after else ''))
        out+=d['data'];pi=d['page_info']
        if not pi.get('has_next_page'): break
        after=pi['end_cursor'];time.sleep(0.4)
    return out,pi.get('total_count')
res={}
for q in ['order=created_at','app_type=b2b_app&order=created_at','app_type=b2c_app&order=created_at','app_type=website&order=created_at','order=total_installs_last_30_days','app_type=b2c_app&order=total_installs_last_30_days','app_type=b2b_app&order=total_installs_last_30_days']:
    o,t=all_(q); res[q]=o; print(q,t,len(o),flush=True)
json.dump(res,open('/tmp/whop/res2.json','w'))
