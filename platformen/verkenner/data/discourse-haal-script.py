# Leest de nieuwste draden van een Discourse-categorie. Gebruik: python3 -I discourse-haal-script.py <basis-url> <categorie-id> <slug> <paginas> uit.json
import json,sys,time,subprocess
base,cat,slug,pages,out=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5]
rows=[]
for p in range(pages):
    url=f"{base}/c/{slug}/{cat}/l/latest.json?order=created&page={p}"
    r=subprocess.run(["curl","-sL","-m","30",url],capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception: print("fout",p,r.stdout[:200]); break
    t=d['topic_list']['topics']
    if not t: break
    for x in t:
        rows.append({k:x.get(k) for k in ['id','title','created_at','views','like_count','posts_count','pinned','last_posted_at']})
    time.sleep(1.5)
json.dump(rows,open(out,'w'))
print(len(rows), rows[0]['created_at'] if rows else '', rows[-1]['created_at'] if rows else '')
