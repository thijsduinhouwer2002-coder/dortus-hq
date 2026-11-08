# Groei per Obsidian-plugin over 30 en 90 dagen (Olaf, 8 nov 2026).
# Bron: de geschiedenis van community-plugin-stats.json in obsidianmd/obsidian-releases (elke dag een commit).
# Zo haal je de momentopnamen op (git clone werkt, de GitHub-API is voor andere repo's dicht):
#   git clone -q --filter=blob:none --no-checkout https://github.com/obsidianmd/obsidian-releases.git or
#   c=$(git -C or log -1 --format=%h --before="2026-10-09T23:59" -- community-plugin-stats.json)
#   git -C or show $c:community-plugin-stats.json > /tmp/claude-0/s-2026-10-09.json
# en evenzo voor de andere data en community-plugins.json (plugins.json).
import json,datetime as dt,csv,sys
L=lambda d:json.load(open(f'/tmp/claude-0/s-{d}.json'))
a,b,c,y=L('2026-11-08'),L('2026-10-09'),L('2026-08-10'),L('2025-11-08')
P={p['id']:p for p in json.load(open('/tmp/claude-0/plugins.json'))}
rows=[]
for k,v in a.items():
    if not isinstance(v,dict): continue
    n=v.get('downloads',0); upd=v.get('updated',0)
    g30=n-b.get(k,{}).get('downloads',n) if isinstance(b.get(k),dict) else None
    g90=n-c.get(k,{}).get('downloads',n) if isinstance(c.get(k),dict) else None
    new=k not in y
    p=P.get(k,{})
    age=(dt.datetime(2026,11,8)-dt.datetime.utcfromtimestamp(upd/1000)).days if upd else None
    rows.append(dict(id=k,naam=p.get('name',''),auteur=p.get('author',''),downloads=n,g30=g30,g90=g90,nieuw_in_jaar=new,dagen_sinds_update=age,omschr=p.get('description','')[:120]))
w=csv.DictWriter(open('/tmp/claude-0/groei.csv','w'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows))
