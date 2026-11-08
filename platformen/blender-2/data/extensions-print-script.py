# Olaf 8 nov 2026: haalt voor print-add-ons op extensions.blender.org downloads, gemiddelde score, aantal reviews, eerste/laatste datum.
# Gebruik: python3 -I extensions-print-script.py extensions-api-2026-11-08.json uit.jsonl
import json,re,sys,subprocess,time
d=json.load(open(sys.argv[1]))['data']
kw=re.compile(r'3d.?print|printab|stl\b|3mf|manifold|watertight|lithophan|relief|keychain|hollow|overhang|slicer|dovetail|connector for|tolerance|resin|filament|mold|interlock',re.I)
r=[x for x in d if x['type']=='add-on' and kw.search(x['name']+' '+x['tagline']+' '+' '.join(x.get('tags',[])))]
extra=['easy-print','easy-slice-print','snapsplit','print3d-toolbox']
def curl(u): return subprocess.run(['curl','-sL','--max-time','30','-A','Mozilla/5.0 (dortus-onderzoek)',u],capture_output=True,text=True).stdout
with open(sys.argv[2],'w') as f:
    for x in r:
        t=curl(x['website']); s=re.sub(r'\s+',' ',t)
        def dd(lbl):
            m=re.search(r'<dt>\s*'+lbl+r'\s*</dt>\s*<dd>(.*?)</dd>',s)
            return re.sub('<[^>]+>','',m.group(1)).strip() if m else None
        m=re.search(r'([\d.]+)\s*out of 5|rating-stars[^>]*title="([\d.]+)',s)
        o={'slug':x['website'].rstrip('/').split('/')[-1],'naam':x['name'],'tagline':x['tagline'],'maker':x['maintainer'],
           'versie':x['version'],'downloads':dd('Downloads'),'gepubliceerd':dd('Published'),'bijgewerkt':dd('Updated'),
           'reviews':dd('Reviews') ,'ratings_ruw':(m.group(0) if m else None)}
        f.write(json.dumps(o)+'\n'); time.sleep(0.5)
