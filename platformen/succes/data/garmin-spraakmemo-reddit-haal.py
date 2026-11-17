# Joris, run 35 (17 nov 2026). Haalt Reddit-berichten op titelwoord via Arctic Shift. Gebruik: python3 -I garmin-spraakmemo-reddit-haal.py <sub> <woord>  (een woord; zinnen geven 0)
import json,subprocess,time,sys,urllib.parse
sub,q=sys.argv[1],sys.argv[2]
out=open('g.jsonl','a');before=None;n=0
for pg in range(8):
  par={'subreddit':sub,'title':q,'after':'2023-01-01','limit':100}
  if before: par['before']=before
  r=subprocess.run(['curl','-sS','--max-time','60','https://arctic-shift.photon-reddit.com/api/posts/search?'+urllib.parse.urlencode(par)],capture_output=True,text=True).stdout
  try: d=json.loads(r)['data']
  except Exception: d=None
  if d is None: print('fout',r[:80]); time.sleep(8); continue
  for p in d:
    p['_sub']=sub; out.write(json.dumps({k:p.get(k) for k in ['id','title','selftext','score','num_comments','created_utc','author','_sub']})+'\n'); n+=1
  if len(d)<100: break
  before=int(min(p['created_utc'] for p in d)); time.sleep(3)
print(sub,q,n)
