# Leest Chrome Web Store-detailpagina's (toegestaan door robots.txt) en haalt
# naam, gebruikers, beoordeling, aantal beoordelingen, bijgewerkt, categorie, versie.
# Gebruik: python3 -I cws-detail-script.py ids.txt uit.jsonl   (ids.txt: één 32-letter-ID per regel)
import sys, re, json, html, time, subprocess
from concurrent.futures import ThreadPoolExecutor
ids=[l.strip() for l in open(sys.argv[1]) if re.fullmatch(r'[a-p]{32}', l.strip())]
ids=list(dict.fromkeys(ids))
def tekst(s):
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    s=html.unescape(re.sub(r'<[^>]+>','\n',s))
    return [l.strip() for l in s.split('\n') if l.strip()]
def haal(i):
    try:
        s=subprocess.run(['curl','-sL','--compressed','-m','30',f'https://chromewebstore.google.com/detail/{i}?hl=en'],capture_output=True,text=True).stdout
    except Exception as e:
        return {'id':i,'fout':str(e)}
    L=tekst(s); r={'id':i}
    if not L: return {'id':i,'fout':'leeg'}
    r['naam']=L[0].replace(' - Chrome Web Store','')
    for k,l in enumerate(L):
        m=re.fullmatch(r'([\d,]+)\+? users?',l)
        if m and 'users' not in r: r['users']=int(m.group(1).replace(',',''))
        m=re.fullmatch(r'([\d.]+K?M?) ratings?',l)
        if m and 'nratings' not in r:
            v=m.group(1); f=1000 if v.endswith('K') else 1e6 if v.endswith('M') else 1
            r['nratings']=int(float(v.rstrip('KM'))*f)
        m=re.fullmatch(r'([\d.]+) out of 5',l)
        if m: r['rating']=float(m.group(1))
        if l=='Updated' and k+1<len(L): r['updated']=L[k+1]
        if l=='Version' and k+1<len(L): r['versie']=L[k+1]
        if l in ('Extension','Theme') and 'cat' not in r and k+1<len(L): r['cat']=L[k+1]
        if l=='Trader': r['trader']=True
        if l=='Featured': r['featured']=True
    tx=' '.join(L).lower()
    r['betaal_woorden']=sorted(set(w for w in ['premium','pro plan','subscription','per month','/month','free trial','lifetime','upgrade','pricing','paid','abonnement','€'] if w in tx))
    time.sleep(0.5)
    return r
with ThreadPoolExecutor(3) as ex, open(sys.argv[2],'w') as f:
    for r in ex.map(haal,ids):
        f.write(json.dumps(r,ensure_ascii=False)+'\n')
