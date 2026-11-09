# Haalt alle assets van Orbolt (SideFX, Houdini) op: lijst op datum, dan elke assetpagina.
# Velden: naam, maker, prijs (gratis/bedragen), reviews, created, assettype.
# Gebruik: python3 -I orbolt-haal-script.py uit.jsonl
import sys,re,html,json,subprocess,time
from concurrent.futures import ThreadPoolExecutor
def get(u):
    return subprocess.run(['curl','-sL','--compressed','-m','30',u],capture_output=True,text=True).stdout
links=[]
for p in range(1,40):
    s=get(f'https://www.orbolt.com/search/?search_ui=NONE&sort=-date&page={p}')
    l=re.findall(r'href="(/asset/[^"]+)"',s)
    new=[x for x in dict.fromkeys(l) if x not in links]
    if not new: break
    links+=new; time.sleep(0.5)
def tekst(s):
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    return [x.strip() for x in html.unescape(re.sub(r'<[^>]+>','\n',s)).split('\n') if x.strip()]
def haal(u):
    L=tekst(get('https://www.orbolt.com'+u)); r={'url':u}
    for k,x in enumerate(L):
        if x.startswith('3D Asset Details for'): r['naam']=x[21:]
        for veld in ['Author:','Created:','Asset Type:','Version:']:
            if x==veld and k+1<len(L): r[veld.rstrip(':').lower()]=L[k+1]
    m=re.search(r'Details for .*?\n',' ')
    # reviews: eerste "(n)" na de titelregel
    for k,x in enumerate(L):
        if x.startswith('3D Asset Details for'):
            for y in L[k:k+12]:
                mm=re.fullmatch(r'\((\d+)\)',y)
                if mm: r['reviews']=int(mm.group(1)); break
            break
    tx=' '.join(L)
    r['gratis']=' Free Download' in ' '+tx or 'Free  Download' in tx
    r['prijzen']=re.findall(r'\$\s?[\d,.]+',tx)[:6]
    time.sleep(0.4); return r
with ThreadPoolExecutor(3) as ex, open(sys.argv[1],'w') as f:
    for r in ex.map(haal,links): f.write(json.dumps(r)+'\n')
print(len(links))
