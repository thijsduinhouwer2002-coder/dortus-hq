# Herhaalmeting Notion Marketplace (Noor, 9 nov 2026). Gebruik: mkdir -p integrations; python3 -I notion-marketplace-meet.py custom-agent-templates | skills-templates | integrations/all
# Telt listings via __NEXT_DATA__ per pagina; kijk daarna naar price > 0 en installationCount.
import re,json,subprocess,sys,time
def get(url):
    t=subprocess.run(['curl','-sL','-m','40','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
    m=re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',t,re.S)
    return json.loads(m.group(1))['props']['pageProps'] if m else None
kind=sys.argv[1]
out=[];seen=set()
for page in range(1,200):
    pp=get(f'https://www.notion.com/{kind}?page={page}')
    if not pp: print('none',page);break
    items=pp.get('agents') or pp.get('skillItems') or pp.get('connections') or []
    new=0
    for it in items:
        key=json.dumps(it,sort_keys=True)[:300]
        i=it.get('id') or it.get('template',{}).get('id') or it.get('integration',{}).get('id')
        if i in seen: continue
        seen.add(i);out.append(it);new+=1
    print(page,len(items),new,len(out),pp.get('count'),file=sys.stderr)
    if new==0: break
    time.sleep(1)
json.dump(out,open(f'{kind}.json','w'))
