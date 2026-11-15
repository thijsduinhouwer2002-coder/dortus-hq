# Google Play: makerpagina's van de lichting, telt apps per maker. Gebruik: python3 -I devs.py det.jsonl devs.json
import json,re,subprocess,urllib.parse,concurrent.futures as cf,sys,datetime
r=[json.loads(l) for l in open(sys.argv[1])]
c=[a for a in r if 'err' not in a and a.get('released') and a['released'][-4:]=='2026' and a['released'][:3] in ('May','Jun','Jul','Aug')]
devs=sorted({(a['developerId'],a['developer']) for a in c})
def get(u): return subprocess.run(["curl","-sL","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
def f(d):
    did,name=d
    u=("https://play.google.com/store/apps/dev?id=%s&hl=en&gl=US"%did) if did.isdigit() else ("https://play.google.com/store/apps/developer?id=%s&hl=en&gl=US"%did)  # developerId is al gecodeerd (fout van de eerste versie: dubbel gecodeerd, zie controleur 15 nov)
    s=set(re.findall(r'details\?id=([A-Za-z0-9._]+)',get(u)))
    return did,len(s)
with cf.ThreadPoolExecutor(6) as ex: res=dict(ex.map(f,devs))
json.dump(res,open(sys.argv[2],'w')); print(len(res))
