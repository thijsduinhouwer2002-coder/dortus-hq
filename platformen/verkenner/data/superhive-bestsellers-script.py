# Vera 8 nov 2026: best verkochte add-ons op Superhive met ondersteunde Blender-versies.
# Gebruik: python3 -I superhive-bestsellers-script.py <paginas> uit.jsonl
import re,sys,json,subprocess,time,concurrent.futures as cf
P=int(sys.argv[1]); out=sys.argv[2]
def curl(u):
    return subprocess.run(['curl','-sL','--max-time','30','-A','Mozilla/5.0 (dortus-verkenner)',u],capture_output=True,text=True).stdout
links=[]
for p in range(1,P+1):
    t=curl(f'https://superhivemarket.com/categories/addons/browse?sort_sales=desc&page={p}')
    for l in re.findall(r'href="/products/([^"?/]+)"',t):
        if l not in links: links.append(l)
    time.sleep(0.5)
def txt(h): return re.sub(r'\s+',' ',re.sub('<[^>]+>','|',h))
def info(slug):
    t=curl('https://superhivemarket.com/products/'+slug); s=txt(t)
    def na(lbl,n=120):
        i=s.find('|'+lbl+'|')
        if i<0: return None
        return re.sub(r'\|+','|',s[i+len(lbl)+2:i+len(lbl)+2+n]).strip('| ')
    bv=na('Blender Version',300) or ''
    vers=[float(v) if v.count('.')==1 else 0 for v in re.findall(r'\b\d\.\d{1,2}\b',bv.split('|')[0])]
    m=re.search(r'"price"\s*:\s*"?([\d.]+)',t)
    return {'slug':slug,'sales':(na('Sales',20) or '').split('|')[0],'published':(na('Published',40) or '').split('|')[0],
            'max_blender':max(vers) if vers else None,'blender':bv.split('|')[0][:80],'prijs':float(m.group(1)) if m else None}
with cf.ThreadPoolExecutor(3) as ex, open(out,'w') as f:
    for r in ex.map(info,links): f.write(json.dumps(r)+'\n')
print(len(links))
