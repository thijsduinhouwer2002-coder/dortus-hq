# Haalt per pakket uit yak.rhino3d.com alle versies (datum eerste versie, downloads, beschrijving).
import json,sys,time,subprocess,urllib.parse
lijst=json.load(open(sys.argv[1])); out=open(sys.argv[2],'a')
klaar=set()
try:
    for l in open(sys.argv[2]): klaar.add(json.loads(l)['name'])
except Exception: pass
for p in lijst:
    n=p['name']
    if n in klaar: continue
    r=subprocess.run(['curl','-sL','-m','40','https://yak.rhino3d.com/versions/'+urllib.parse.quote(n)],capture_output=True,text=True)
    try: v=json.loads(r.stdout)
    except Exception: v=None
    rec={'name':n,'authors':p['authors'],'download_count':p['download_count'],'updated_at':p['updated_at']}
    if isinstance(v,list) and v:
        ds=sorted(x.get('created_at') or '' for x in v)
        rec['eerste']=ds[0]; rec['nversies']=len(v)
        nieuw=max(v,key=lambda x:x.get('created_at') or '')
        rec['desc']=(nieuw.get('description') or '')[:600]; rec['homepage']=nieuw.get('homepage_url')
        rec['keywords']=nieuw.get('keywords'); rec['prerelease']=nieuw.get('prerelease')
        rec['rhino']=sorted({d.get('rhino_version') for x in v for d in (x.get('distributions') or [])})
    else: rec['fout']=r.stdout[:100]
    out.write(json.dumps(rec)+'\n'); out.flush(); time.sleep(0.6)
