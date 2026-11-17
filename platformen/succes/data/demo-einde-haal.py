# Verhaal 23 (Fenna): winkeltekst van de demo's van bureaubladspellen ophalen.
# Gebruik: python3 demo-einde-haal.py <uitmap>. Leest Vera's kaart, schrijft <uitmap>/demos.jsonl.
import csv,json,time,subprocess,sys,os
S=sys.argv[1]
r=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv')))
d=sorted([x for x in r if x['demo']=='True'],key=lambda x:(x['binnenkort']=='True',-int(x['reviews_totaal'] or 0)))
p=S+'/demos.jsonl'; done=set()
if os.path.exists(p):
    for l in open(p):
        try: done.add(json.loads(l)['appid'])
        except: pass
out=open(p,'a')
def get(a):
    for t in range(3):
        o=subprocess.run(['curl','-s','-m','20',f'https://store.steampowered.com/api/appdetails?appids={a}&cc=us&l=english'],capture_output=True,text=True).stdout
        try: return json.loads(o)[str(a)]
        except: time.sleep(60)
    return None
for x in d:
    a=x['appid']
    if a in done: continue
    j=get(a); rec={'appid':a,'naam':x['naam'],'binnenkort':x['binnenkort'],'reviews':x['reviews_totaal'],'pct':x['pct_positief'],'lijkt':x['lijkt_op_hats']}
    if j and j.get('success'):
        dd=j['data']; rec['demos']=dd.get('demos'); rec['full_desc']=dd.get('detailed_description','')
        if dd.get('demos'):
            time.sleep(1.2)
            dm=get(dd['demos'][0]['appid'])
            if dm and dm.get('success'):
                q=dm['data']; rec['demo_short']=q.get('short_description'); rec['demo_desc']=q.get('detailed_description'); rec['demo_release']=q.get('release_date')
    out.write(json.dumps(rec)+'\n'); out.flush()
    time.sleep(1.2)
