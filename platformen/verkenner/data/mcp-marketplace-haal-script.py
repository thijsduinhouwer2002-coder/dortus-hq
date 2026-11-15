import re,html,urllib.request,json
from concurrent.futures import ThreadPoolExecutor
def txt(u):
    s=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S); return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)))
cr=[l.strip() for l in open('/tmp/mcpm/creators.txt')]
def one(u):
    try: t=txt(u)
    except Exception as e: return {'u':u,'err':str(e)}
    i=t.find('Published Tools'); return {'u':u,'joined':(re.search(r'Joined (\w+ \d{4})',t) or [0,None])[1],'tools':t[i:i+700]}
with ThreadPoolExecutor(4) as ex: out=list(ex.map(one,cr))
json.dump(out,open('/tmp/mcpm/creators.json','w'))
for o in out:
    if 'No published tools' not in o.get('tools',''): print(o['u'].split('/')[-1],o.get('joined'),'|',o.get('tools','')[:300])
print(len(out),sum('No published tools' in o.get('tools','') for o in out))
