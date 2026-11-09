import re,html,json,sys,time,urllib.request
rows=[l.split('\t') for l in open(sys.argv[1]).read().split('\n') if '/plugins/' in l]
rows=[r for r in rows if r[1]>=sys.argv[2]]
out=open(sys.argv[3],'w')
for url,lm in rows:
  try:
    s=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; DortusResearch/1.0)'}),timeout=30).read().decode('utf8','ignore')
  except Exception as e:
    out.write(json.dumps({'url':url,'err':str(e)})+'\n'); continue
  fr=s[s.find('Freshness'):]; fr=fr[:fr.find('Share')]; dts=re.findall(r'datetime="([^"]+)"',fr)
  t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S);t=re.sub('<[^>]+>',' ',t);t=html.unescape(re.sub(r'\s+',' ',t))
  m=re.search(r'Home Plugins (.*?) (\S+) (\$[\d,.]+|Free) \((\d[\d,]*) reviews?\) By (.*?) Find their',t)
  m2=re.search(r'Screenshots? (?:All screenshots )?([\d.,]+[km]?) ([\d.,]+[km]?) [\d.]+ [kMG]?B',t)
  m3=re.search(r'Freshness Updated .*? ago ([A-Z][a-z]+ \d+, \d{4})',t) or re.search(r'Freshness .*?([A-Z][a-z]+ \d+, \d{4}) Share',t)
  m4=re.search(r'Total versions (\d+)',t)
  if not m:
    m=re.search(r'Home Plugins (.*?) (\S+) (\$[\d,.]+|Free) ()By (.*?) Find their',t)
  d={'url':url,'lastmod':lm,'titel':m.group(1) if m else None,'prijs':m.group(3) if m else None,'reviews':(m.group(4) or '0') if m else None,'maker':m.group(5) if m else None,
     'views':m2.group(1) if m2 else None,'downloads':m2.group(2) if m2 else None,'gemaakt':dts[-1][:10] if dts else None,'versies':m4.group(1) if m4 else None}
  out.write(json.dumps(d)+'\n'); out.flush(); time.sleep(0.7)
