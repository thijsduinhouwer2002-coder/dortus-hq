import json,re,html,urllib.request,time,sys
from concurrent.futures import ThreadPoolExecutor
r=json.load(open('/tmp/whop/res2.json'))
apps=r['order=created_at']
def one(a):
    try:
        s=urllib.request.urlopen(urllib.request.Request(f"https://whop.com/apps/{a['id']}/",headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode()
    except Exception as e: return {'id':a['id'],'err':str(e)}
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S); t=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)))
    dates=re.findall(r'Written ([A-Z][a-z]+ \d{1,2}, \d{4})',t)
    price=re.findall(r'\$\s?\d[\d,.]*(?:\s?/\s?(?:mo|month|year|yr))?',t)
    return {'id':a['id'],'name':a['name'],'reviews':a.get('published_reviews_count'),'dates':dates,'prices':price[:10],'whop':a.get('is_whop_app'),'type':a['app_type'],'creator':a['creator']['username'],'cat':(a.get('category') or {}).get('name'),'desc':a.get('description')}
with ThreadPoolExecutor(4) as ex: out=list(ex.map(one,apps))
json.dump(out,open('/tmp/whop/pages194.json','w'))
print(len(out),sum('err' in o for o in out))
