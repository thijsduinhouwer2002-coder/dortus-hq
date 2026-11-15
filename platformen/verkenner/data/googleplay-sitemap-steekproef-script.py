# Google Play: kies willekeurige sitemapbestanden en haal de app-ids eruit. Gebruik (in een map met idx0.xml en idx1.xml uit play.google.com/sitemaps/sitemaps-index-0.xml en -1.xml): python3 -I script.py <aantal bestanden> <seed> uit.jsonl
import re,subprocess,random,sys,json,concurrent.futures as cf
idx=[]
for f in ['idx0.xml','idx1.xml']:
    idx+=re.findall(r'<loc>([^<]+)</loc>',open(f).read())
random.seed(int(sys.argv[2]))
pick=random.sample(idx,int(sys.argv[1]))
def g(u):
    x=subprocess.run(f"curl -s '{u}' | gunzip",shell=True,capture_output=True,text=True).stdout
    locs=re.findall(r'<loc>([^<]+)</loc>',x)
    apps=sorted({m for l in locs for m in re.findall(r'/store/apps/details\?id=([A-Za-z0-9._]+)',l)})
    return u,len(locs),apps
out=open(sys.argv[3],'a')
with cf.ThreadPoolExecutor(6) as ex:
    for u,n,a in ex.map(g,pick):
        out.write(json.dumps({'u':u,'n':n,'apps':a})+'\n')
