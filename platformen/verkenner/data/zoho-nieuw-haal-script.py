import re,html,subprocess,json,sys,concurrent.futures as cf
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
def c(u): return subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
def g(i):
    u='https://marketplace.zoho.com/app/'+i
    s=c(u); s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S); t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))
    f=lambda p:(re.search(p,t) or [None,None])[1]
    return dict(url=u,installs=f(r'([\d.,]+[KM]?\+?) Installs'),pub=f(r'Published date (\w{3} \d+, \d{4})'),pricing=f(r'Pricing (\w[\w ]{0,20}?) (?:Category|Developed|Support|Published|Version|Ratings|$)'),dev=f(r'Developed by: (.+?) (?:[\d.,]+[KM]?\+? Installs|Published|Pricing)'),reviews=f(r'(\d+) (?:Reviews|Ratings)'),ok=len(t)>2000)
with cf.ThreadPoolExecutor(6) as ex: out=list(ex.map(g,ids))
json.dump(out,open(sys.argv[2],'w'),indent=0); print(len(out))
