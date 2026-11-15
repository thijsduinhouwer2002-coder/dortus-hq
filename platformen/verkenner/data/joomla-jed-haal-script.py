import re,subprocess,html,time,json,sys
from concurrent.futures import ThreadPoolExecutor
A="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
def cu(u): return html.unescape(subprocess.run(['curl','-sL','-m','30','-A',A,u],capture_output=True,text=True).stdout)
links=[]
for s in range(0,int(sys.argv[2]),18):
    for l in re.findall(r'href="(/extension/[^"]+/)"',cu(f'https://extensions.joomla.org/browse/new?start={s}')):
        if l.count('/')>=4 and l not in links: links.append(l)
    time.sleep(0.7)
def get(a):
    i,l=a; time.sleep(0.5); h=cu('https://extensions.joomla.org'+l)
    t=re.sub(r'<script.*?</script>','',h,flags=re.S);t=re.sub(r'<[^>]+>',' ',t);t=re.sub(r'\s+',' ',t)
    rv=re.search(r'Reviews \((\d+)\)',t); lu=re.search(r'Last updated:\s*([A-Za-z]+ \d{1,2},? \d{4}|\d{1,2} [A-Za-z]+ \d{4}|[\d-]{8,10})',t)
    da=re.search(r'Date added:\s*([A-Za-z]+ \d{1,2},? \d{4}|\d{1,2} [A-Za-z]+ \d{4}|[\d-]{8,10})',t)
    return {'pos':i,'url':l,'reviews':int(rv.group(1)) if rv else 0,'type':(re.search(r'Type:\s*(Paid download|Free download|Free|Paid|[A-Za-z ]{3,30}?) (?:In|Includes|Version|Ext)',t) or re.search(r'Type:\s*(\S+ \S+)',t)).group(1) if 'Type:' in t else None,'maker':(re.search(r'Developer:?\s*([^|]{2,60}?) Last updated',t) or re.search(r'([A-Za-z0-9 .&-]{2,60}) Last updated',t)).group(1) if 'Last updated' in t else None,'last':lu.group(1) if lu else None,'added':da.group(1) if da else None}
with open(sys.argv[1],'w') as o, ThreadPoolExecutor(3) as ex:
    for r in ex.map(get,list(enumerate(links))): o.write(json.dumps(r)+'\n')
