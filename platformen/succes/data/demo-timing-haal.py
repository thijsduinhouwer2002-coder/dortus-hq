import csv,json,time,subprocess,sys,os
S=sys.argv[1]
r=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv')))
d=sorted([x for x in r if x['demo']=='True'],key=lambda x:(x['binnenkort']=='True',-int(x['reviews_totaal'] or 0)))
out=open(S+'/apps.jsonl','a')
done=set()
if os.path.exists(S+'/apps.jsonl'):
    for l in open(S+'/apps.jsonl'):
        try: done.add(json.loads(l)['appid'])
        except: pass
def get(a):
    for t in range(3):
        o=subprocess.run(['curl','-s','-m','20',f'https://store.steampowered.com/api/appdetails?appids={a}&cc=us&l=english'],capture_output=True,text=True).stdout
        try: return json.loads(o)[str(a)]
        except: time.sleep(60)
    return None
for x in d:
    a=x['appid']
    if a in done: continue
    j=get(a); rec={'appid':a,'naam':x['naam']}
    if j and j.get('success'):
        dd=j['data']; rec['release']=dd.get('release_date'); rec['demos']=dd.get('demos')
        if dd.get('demos'):
            time.sleep(1.3)
            dm=get(dd['demos'][0]['appid'])
            if dm and dm.get('success'): rec['demo_release']=dm['data'].get('release_date')
            else: rec['demo_release']=None
    out.write(json.dumps(rec)+'\n'); out.flush()
    time.sleep(1.3)
