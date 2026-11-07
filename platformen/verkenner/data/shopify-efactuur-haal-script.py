import re,html,json,subprocess,sys,concurrent.futures as cf
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
def get(u):
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    d={'url':u}
    m=re.search(r'Launched ([A-Z][a-z]+ \d+, \d{4})',t); d['launched']=m.group(1) if m else None
    m=re.search(r'"ratingCount":(\d+)',s); d['reviews']=int(m.group(1)) if m else 0
    m=re.search(r'Pricing (.{0,80}?) Rating',t) or re.search(r'Pricing (.{0,80}?) Developer',t); d['price']=m.group(1) if m else None
    m=re.search(r'"brand":"([^"]*)"',s); d['dev']=m.group(1) if m else None
    m=re.search(r'<title>([^<]*)',s); d['title']=html.unescape(m.group(1)) if m else None
    m=re.search(r'<meta name="description" content="([^"]*)"',s); d['desc']=html.unescape(m.group(1))[:300] if m else None
    low=t.lower()
    d['kw']=[k for k in ['peppol','xrechnung','zugferd','factur-x','e-invoic','einvoic','e-rechnung','ksef','fattura elettronica','sdi','verifactu','ticketbai','facture électronique','e-facture','ubl','chorus'] if k in low]
    d['ok']=len(s)>20000
    return d
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(get,urls))
json.dump(out,open(sys.argv[2],'w'))
print(len(out),sum(d['ok'] for d in out))
