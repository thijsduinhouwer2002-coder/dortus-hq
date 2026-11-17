import csv, json, time, subprocess, sys, os
r=[x for x in csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv')) if x['binnenkort']=='False']
r.sort(key=lambda x:-int(x['reviews_totaal'] or 0))
out='platforms.jsonl'
done=set()
if os.path.exists(out):
    for l in open(out): done.add(json.loads(l)['appid'])
f=open(out,'a')
for x in r:
    a=x['appid']
    if a in done: continue
    for t in range(4):
        s=subprocess.run(['curl','-s','--compressed','-m','20',f'https://store.steampowered.com/api/appdetails?appids={a}&filters=platforms'],capture_output=True,text=True).stdout
        try:
            d=json.loads(s); break
        except Exception:
            print("wacht",a,flush=True); time.sleep(30)
    else:
        d=None
    p=None
    if d and d.get(a,{}).get('success'):
        p=d[a]['data'].get('platforms')
    f.write(json.dumps({'appid':a,'platforms':p})+'\n'); f.flush()
    time.sleep(1.0)
