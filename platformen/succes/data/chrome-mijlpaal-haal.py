# Joris, run 34 (17 nov 2026). Haalt mijlpaalberichten (users, installs, MRR) van Reddit via Arctic Shift. Gebruik: python3 -I chrome-mijlpaal-haal.py subs termen
import json,subprocess,time,sys,urllib.parse
out=open('posts.jsonl','a')
def get(u):
  r=subprocess.run(['curl','-sS','-A','dortus-onderzoek/1.0','--max-time','120',u],capture_output=True,text=True)
  return json.loads(r.stdout)['data']
subs=sys.argv[1].split(',')
QS=sys.argv[2].split(',')
for sub in subs:
  for q in QS:
    before=None
    for page in range(15):
      u='https://arctic-shift.photon-reddit.com/api/posts/search?'+urllib.parse.urlencode({'subreddit':sub,'title':q,'after':'2024-01-01','limit':100,**({'before':before} if before else {}),'sort':'desc'})
      d=None
      for t in range(3):
        try: d=get(u); break
        except Exception as e: time.sleep(3)
      if d is None: print(sub,q,'fout',file=sys.stderr);break
      if not d: break
      for p in d:
        p['_sub']=sub; out.write(json.dumps({k:p.get(k) for k in ['id','title','selftext','score','num_comments','created_utc','url','_sub','author']})+'\n')
      before=str(int(d[-1]['created_utc']))
      time.sleep(1.5)
      
    print(sub,q,page,file=sys.stderr)
