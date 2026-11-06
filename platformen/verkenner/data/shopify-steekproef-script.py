import re,html,json,random,subprocess,sys,concurrent.futures as cf
locs=re.findall(r'<loc>([^<]+)</loc>',open('/tmp/claude-0/sh/en.xml').read())
random.seed(42); smp=random.sample(locs,int(sys.argv[1]))
def get(u):
    try:
        s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    except Exception as e: return {'url':u,'err':str(e)}
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    d={'url':u}
    m=re.search(r'Launched ([A-Z][a-z]+ \d+, \d{4})',t); d['launched']=m.group(1) if m else None
    m=re.search(r'"ratingCount":(\d+)',s); d['reviews']=int(m.group(1)) if m else 0
    m=re.search(r'"ratingValue":([\d.]+)',s); d['rating']=float(m.group(1)) if m else None
    m=re.search(r'Pricing (.{0,80}?) Rating',t) or re.search(r'Pricing (.{0,80}?) Developer',t); d['price']=m.group(1) if m else None
    m=re.search(r'"brand":"([^"]*)"',s); d['dev']=m.group(1) if m else None
    m=re.search(r'href="https://apps.shopify.com/partners/([^"?/]+)',s); d['devslug']=m.group(1) if m else None
    d['bfs']=('built-for-shopify' in s.lower() and 'Built for Shopify' in t[:3000])
    d['ok']=len(s)>20000
    return d
out=[]
with cf.ThreadPoolExecutor(8) as ex:
    for d in ex.map(get,smp): out.append(d)
json.dump(out,open(sys.argv[2],'w'))
print(len(out),sum(1 for d in out if d.get('ok')))
