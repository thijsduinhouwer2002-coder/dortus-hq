import re,html,json,subprocess,sys,concurrent.futures as cf
locs=[l for l in re.findall(r'<loc>([^<]+)</loc>',open(sys.argv[1]).read()) if '/stats/app/' in l]
def num(p,t):
    m=re.search(p,t); return int(m.group(1).replace(',','')) if m else None
def get(u):
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    t=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S))); t=re.sub(r'\s+',' ',t)
    d={'sc':u.rsplit('/',1)[1],'ok':len(s)>50000}
    d['installs']=num(r'Active Installs : ([\d,]+)',t)
    d['d30']=num(r'past 30 days, .{0,80}?has (?:gained|lost) ([\d,]+) net',t)
    m=re.search(r'past 30 days, .{0,80}?has (gained|lost)',t); d['d30dir']=m.group(1) if m else None
    d['yr_from']=num(r'moving from ([\d,]+) installs',t)
    d['notyr']='not tracked in our system a year ago' in t
    m=re.search(r'How Many Shopify Stores Use (.+?) \?',t); d['name']=m.group(1) if m else None
    m=re.search(r'href="https://apps\.shopify\.com/([a-z0-9-]+)',s); d['shop']=m.group(1) if m else None
    return d
out=list(cf.ThreadPoolExecutor(10).map(get,locs))
json.dump(out,open(sys.argv[2],'w'),indent=0)
print(len(out),sum(d['ok'] for d in out),sum(1 for d in out if d['installs'] is not None),sum(1 for d in out if d['shop']))
