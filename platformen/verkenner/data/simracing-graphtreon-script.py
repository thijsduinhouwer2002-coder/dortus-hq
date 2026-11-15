import re,html,sys,subprocess,time,json
out=[]
for slug in open(sys.argv[1]).read().split():
    s=subprocess.run(['curl','-s','-A','Mozilla/5.0','https://graphtreon.com'+slug],capture_output=True,text=True).stdout
    s=re.sub(r'(?s)<(script|style).*?</\1>','',s);t=html.unescape(re.sub(r'<[^>]+>',' ',s));t=re.sub(r'\s+',' ',t)
    name=t.split(':')[0].strip()[:60]
    pm=re.search(r'Paid Members (?:was )?([\d,]+)',t); er=re.search(r'Estimated Earnings per month (?:was )?\$([\d,]+) - \$([\d,]+)',t)
    ex=re.search(r'is earning \$([\d,]+(?: - \$[\d,]+)?) per month',t)
    la=re.search(r'Launched (\w+ \d+, \d{4})',t); priv='private' in t[:600]
    out.append(dict(slug=slug,name=name,paid=pm.group(1) if pm else None,earn=ex.group(1) if ex else None,launched=la.group(1) if la else None,private=priv))
    time.sleep(1)
for o in out: print(json.dumps(o,ensure_ascii=False))
