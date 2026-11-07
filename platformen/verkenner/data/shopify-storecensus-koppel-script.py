import re,html,json,subprocess,sys,concurrent.futures as cf
locs=set(l.rstrip('/').rsplit('/',1)[1] for l in re.findall(r'<loc>([^<]+)</loc>',open(sys.argv[1]).read()))
sc=json.load(open(sys.argv[2])); slugs=[x['sc'] for x in sc if x['sc'] in locs]
def get(slug):
    u='https://apps.shopify.com/'+slug
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    d={'slug':slug,'ok':len(s)>20000}
    m=re.search(r'Launched ([A-Z][a-z]+ \d+, \d{4})',t); d['launched']=m.group(1) if m else None
    m=re.search(r'"ratingCount":(\d+)',s); d['reviews']=int(m.group(1)) if m else 0
    m=re.search(r'Pricing (.{0,80}?) Rating',t) or re.search(r'Pricing (.{0,80}?) Developer',t); d['price']=m.group(1) if m else None
    m=re.search(r'"brand":"([^"]*)"',s); d['dev']=m.group(1) if m else None
    m=re.search(r'href="https://apps.shopify.com/partners/([^"?/]+)',s); d['devslug']=m.group(1) if m else None
    return d
out=list(cf.ThreadPoolExecutor(8).map(get,slugs))
json.dump(out,open(sys.argv[3],'w'),indent=0)
print(len(out),sum(d['ok'] for d in out),sum(1 for d in out if d['launched']))
