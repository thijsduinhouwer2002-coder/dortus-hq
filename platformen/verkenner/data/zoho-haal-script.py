import re,html,subprocess,json,sys,concurrent.futures as cf
pages=['https://www.zoho.com/marketplace/crm/sales-integrations.html','https://www.zoho.com/marketplace/desk/support-integrations.html','https://www.zoho.com/marketplace/recruit/recruit-integrations.html','https://www.zoho.com/marketplace/marketplace-extensions.html','https://www.zoho.com/marketplace/industry-solutions.html']
def c(u): return subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
urls=set()
for p in pages:
    for m in re.findall(r'marketplace\.zoho\.[a-z.]+/app/([a-z]+/[a-z0-9-]+)',c(p)): urls.add('https://marketplace.zoho.com/app/'+m)
def g(u):
    s=c(u); s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S); t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))
    f=lambda p:(re.search(p,t) or [None,None])[1]
    return dict(url=u,installs=f(r'([\d.,]+[KM]?\+?) Installs'),pub=f(r'Published date (\w{3} \d+, \d{4})'),pricing=f(r'Pricing (Paid|Free|Freemium|Free Trial|Free plan available|[A-Z][a-z]+)'),dev=f(r'Developed by: (.+?) [\d.,]+[KM]?\+? Installs'))
with cf.ThreadPoolExecutor(6) as ex: out=list(ex.map(g,sorted(urls)))
json.dump(out,open(sys.argv[1],'w'),indent=0); print(len(out))
