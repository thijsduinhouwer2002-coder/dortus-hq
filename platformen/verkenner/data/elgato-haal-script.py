import re,json,random,subprocess,sys,concurrent.futures as cf
locs=[l for l in re.findall(r'<loc>([^<]+)</loc>',open('sm.xml').read()) if '/product/' in l]
random.seed(7); smp=random.sample(locs,int(sys.argv[1]))
def g(pat,s):
    m=re.search(pat,s); return m.group(1) if m else None
def get(u):
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    s=s.replace('\\"','"')
    return {'url':u,'created':g(r'"content":\{"id":"[^"]+","created_at":"([^"]+)"',s),'app':g(r'"application":"([^"]+)"',s),
      'ext':g(r'"extension":"([^"]+)"',s),'free':g(r'"is_free":(true|false)',s),'org':g(r'"org_slug":"([^"]+)"',s),
      'price':g(r'"unit_amount":(\d+)',s)}
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(get,smp))
json.dump(out,open(sys.argv[2],'w')); print(len(out),sum(1 for d in out if d['created']))
