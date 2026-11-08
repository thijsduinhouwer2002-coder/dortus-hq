# Haalt alle apps uit de Miro Marketplace-pagina (miro.com/marketplace/, robots.txt staat het toe).
# Gebruik: curl -sL https://miro.com/marketplace/ -o m.html; python3 -I miro-haal-script.py m.html uit.json
import re,json,sys
t=open(sys.argv[1]).read()
parts=re.split(r'\{"id":"(\d+)","appKey":"[^"]*","name":"',t)
apps={}
for k in range(1,len(parts),2):
    aid=parts[k]; c=parts[k+1]
    u=re.search(r'"usageCount":(\d+)',c)
    if not u: continue
    r=re.search(r'"ratingCount":(\d+)',c); pt=re.search(r'"appPaymentType":"(\w+)"',c)
    dev=re.search(r'"developer":\{"id":"(\d+)","name":"([^"]*)"',c); tier=re.search(r'"tier":"(\w+)"',c)
    apps[aid]=dict(id=aid,name=c.split('"',1)[0],usage=int(u[1]),ratings=int(r[1]) if r else 0,pay=pt[1] if pt else '',dev=dev[2] if dev else '',devid=dev[1] if dev else '',tier=tier[1] if tier else '')
json.dump(list(apps.values()),open(sys.argv[2],'w'))
print(len(apps))
