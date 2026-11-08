# Wear OS-wijzerplaten, vier scripts achter elkaar: zaad.py (zoekopdrachten en categorie), details.py (google-play-scraper), devs.py (makerpagina s), analyse.py
import re,subprocess,json,urllib.parse,concurrent.futures as cf,time,sys
UA="Mozilla/5.0"
def get(u):
    return subprocess.run(["curl","-sL","-A",UA,u],capture_output=True,text=True).stdout
ids=set()
cat=get("https://play.google.com/store/apps/category/WATCH_FACE?hl=en&gl=US")
ids|=set(re.findall(r'details\?id=([A-Za-z0-9._]+)',cat))
qs=["watch face","wear os watch face","digital watch face","analog watch face","watch face galaxy watch","pixel watch face","minimal watch face","hybrid watch face","animated watch face","cute watch face","sport watch face","aviator watch face","retro watch face","neon watch face","luxury watch face","health watch face","weather watch face","fitness watch face","classic watch face","modern watch face","military watch face","halloween watch face","christmas watch face","autumn watch face","cat watch face","anime watch face","space watch face","floral watch face","racing watch face","diver watch face","chronograph watch face","bold watch face","big numbers watch face","AOD watch face","WFF watch face","watch face for women","dark watch face","colorful watch face","premium watch face","free watch face wear os","new watch face 2026","dashboard watch face","pilot watch face","info watch face","steampunk watch face","ocean watch face","nature watch face","car watch face","gradient watch face","glass watch face"]
for q in qs:
    h=get("https://play.google.com/store/search?q="+urllib.parse.quote(q)+"&c=apps&hl=en&gl=US")
    ids|=set(re.findall(r'details\?id=([A-Za-z0-9._]+)',h)); time.sleep(0.3)
print(len(ids),file=sys.stderr)
json.dump(sorted(ids),open(sys.argv[1],'w'))
import json,sys,concurrent.futures as cf,time
from google_play_scraper import app
ids=json.load(open(sys.argv[1])); out=sys.argv[2]
done=set()
try:
    for l in open(out): done.add(json.loads(l)['appId'])
except FileNotFoundError: pass
K=['appId','title','minInstalls','realInstalls','released','price','free','offersIAP','genreId','developer','developerId','ratings','score','updated','currency']
def f(i):
    for t in range(3):
        try:
            d=app(i,lang='en',country='us'); return {k:d.get(k) for k in K}
        except Exception as e:
            if 'not found' in str(e).lower() or 'NotFound' in type(e).__name__: return {'appId':i,'err':'404'}
            time.sleep(2)
    return {'appId':i,'err':'fail'}
todo=[i for i in ids if i not in done]
with open(out,'a') as w, cf.ThreadPoolExecutor(6) as ex:
    for r in ex.map(f,todo): w.write(json.dumps(r)+'\n')
print(len(todo),file=sys.stderr)
import json,re,subprocess,urllib.parse,concurrent.futures as cf,sys
r=[json.loads(l) for l in open(sys.argv[1])]
devs={(a['developerId'],a['developer']) for a in r if 'err' not in a}
known={a['appId'] for a in r}
def get(u): return subprocess.run(["curl","-sL","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
def f(d):
    did,name=d; s=set()
    for u in ["https://play.google.com/store/apps/dev?id=%s&hl=en&gl=US"%did,"https://play.google.com/store/apps/developer?id=%s&hl=en&gl=US"%urllib.parse.quote(name)]:
        s|=set(re.findall(r'details\?id=([A-Za-z0-9._]+)',get(u)))
    return did,name,sorted(s)
res=[]
with cf.ThreadPoolExecutor(4) as ex:
    for x in ex.map(f,sorted(devs)): res.append(x)
json.dump(res,open(sys.argv[2],'w'))
new=set(i for _,_,l in res for i in l)-known
print(len(devs),len(new),max(len(l) for _,_,l in res),file=sys.stderr)
json.dump(sorted(new),open(sys.argv[3],'w'))
import json,collections,statistics as st,datetime,sys
r=[json.loads(l) for l in open(sys.argv[1])]
ok=[a for a in r if 'err' not in a and a.get('released')]
print('totaal',len(r),'fout',sum('err' in a for a in r))
def wf(a): t=a['title'].lower(); return a['genreId']=='PERSONALIZATION' and ('watch' in t or 'face' in t or 'wear' in t)
w=[a for a in ok if wf(a)]
for a in w: a['d']=datetime.datetime.strptime(a['released'],'%b %d, %Y').date()
print('wijzerplaten',len(w),'makers',len({a['developerId'] for a in w}))
m=collections.Counter(a['d'].strftime('%Y-%m') for a in w if a['d'].year>=2025); print(sorted(m.items()))
dp=json.load(open(sys.argv[2])); full={d for d,_,l in dp if len(l)<29}
def rep(lbl,c):
    if not c: return
    ri=[a['realInstalls'] or 0 for a in c]
    print(f"{lbl}: n={len(c)} mediaan={st.median(ri):.0f} 100+={100*sum(x>=100 for x in ri)/len(c):.1f}% 1000+={100*sum(x>=1000 for x in ri)/len(c):.1f}% 10000+={100*sum(x>=10000 for x in ri)/len(c):.1f}% max={max(ri)} p75={sorted(ri)[int(.75*len(ri))]} p90={sorted(ri)[int(.9*len(ri))]}")
c=[a for a in w if datetime.date(2026,5,1)<=a['d']<=datetime.date(2026,8,31)]
rep('mei-aug 2026 alle',c)
rep('  betaald',[a for a in c if not a['free']]); rep('  gratis',[a for a in c if a['free']])
rep('  makers met volledige lijst',[a for a in c if a['developerId'] in full])
rep('  betaald, volledige lijst',[a for a in c if a['developerId'] in full and not a['free']])
pr=collections.Counter(a['price'] for a in c if not a['free']); print('prijzen',pr.most_common(8))
rep('2025 alle',[a for a in w if a['d'].year==2025]); rep('2025 betaald',[a for a in w if a['d'].year==2025 and not a['free']])
# omzet schatting betaald cohort
b=[a for a in c if not a['free']]
print('betaald cohort som installs',sum(a['realInstalls'] or 0 for a in b),'bruto $',round(sum((a['realInstalls'] or 0)*a['price'] for a in b)))
b.sort(key=lambda a:-(a['realInstalls'] or 0))
for a in b[:12]: print(' ',a['realInstalls'],a['price'],a['released'],a['developer'],'|',a['title'][:50])
