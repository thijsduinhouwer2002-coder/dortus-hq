# Vera 17 nov 2026: vult elke regel uit chrome-zoek-ids-script.py aan met gebruikers, sterren en aanmaakdatum op 14 aug 2026 uit de dataset van Palant (codeberg).
# Gebruik: python3 -I chrome-palant-aug-script.py x uit.jsonl [meer.jsonl] > aangevuld.jsonl
import json,sys,subprocess,re,time
rows={}
for f in sys.argv[2:]:
    for l in open(f):
        r=json.loads(l); rows.setdefault(r['id'],r)
for i,r in rows.items():
    t=subprocess.run(['curl','-sS','-m','30',f'https://codeberg.org/palant/chrome-extension-manifests-dataset/raw/branch/main/manifests-2026-08-14/{i}.json'],capture_output=True,text=True).stdout
    u=re.search(r'^user_count: (\d+)',t,re.M); c=re.search(r"^creation_date: '([\d-]+)",t,re.M); rc=re.search(r'^rating: ([\d.]+)',t,re.M)
    r['aug']=int(u.group(1)) if u else None; r['gemaakt']=c.group(1) if c else ''; r['ster_aug']=rc.group(1)[:4] if rc else ''
    print(json.dumps(r),flush=True); time.sleep(0.5)
