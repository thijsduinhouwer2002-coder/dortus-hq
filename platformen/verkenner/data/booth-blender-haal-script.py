import json,time,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('/tmp/b/lijst.json'))
done=set()
for l in open('/tmp/b/items.jsonl'):
    try: done.add(json.loads(l)['id'])
    except: pass
todo=[x for x in d if x['id'] not in done]
f=open('/tmp/b/items.jsonl','a')
def get(x):
    u=f"https://booth.pm/ja/items/{x['id']}.json"
    r=subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
    try:
        j=json.loads(r)
        rec=dict(id=x['id'],name=j.get('name'),published_at=j.get('published_at'),likes=j.get('wish_lists_count'),
          cat=(j.get('category') or {}).get('name'),parent=((j.get('category') or {}).get('parent') or {}).get('name'),
          shop=(j.get('shop') or {}).get('subdomain'),prices=[v.get('price') for v in j.get('variations',[])],
          tags=[t.get('name') for t in j.get('tags',[])][:15],adult=j.get('is_adult'))
    except Exception as e:
        rec=dict(id=x['id'],err=str(e)[:80])
    time.sleep(0.5)
    return rec
with ThreadPoolExecutor(3) as ex:
    for rec in ex.map(get,todo):
        f.write(json.dumps(rec,ensure_ascii=False)+"\n"); f.flush()
