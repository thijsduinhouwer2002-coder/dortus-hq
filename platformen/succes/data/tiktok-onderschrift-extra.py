import json, os, re, sys, statistics as st, time, random
map_=sys.argv[1]; GRENS=time.time()-14*86400
R=[]
for f in sorted(os.listdir(map_)):
    if not f.endswith('.json'): continue
    a=f[:-5]; es=[e for e in json.load(open(os.path.join(map_,f)))['entries'] if e.get('timestamp') and e.get('view_count') is not None]
    es.sort(key=lambda e:e['timestamp'])
    for i,e in enumerate(es):
        if e['timestamp']>GRENS: continue
        b=[x['view_count'] for x in es[max(0,i-10):i]+es[i+1:i+11]]
        if len(b)<10 or st.median(b)<=0: continue
        R.append((a,e['view_count']/st.median(b),e.get('description') or ''))
accs=sorted({r[0] for r in R})
def test(naam,sel,min_n=8):
    pa=[]
    for a in accs:
        ja=[r[1] for r in R if r[0]==a and sel(r[2])]; nee=[r[1] for r in R if r[0]==a and not sel(r[2])]
        if len(ja)>=min_n and len(nee)>=min_n: pa.append(st.median(ja)/st.median(nee))
    n=sum(1 for r in R if sel(r[2]))
    if not pa: print(naam,n,'geen accounts'); return
    random.seed(1); bs=sorted(st.median([random.choice(pa) for _ in pa]) for _ in range(2000))
    print(f'{naam:30s} n={n:5d} accounts {sum(x>1 for x in pa)}/{len(pa)} med {st.median(pa):.2f} [{bs[50]:.2f}-{bs[1949]:.2f}]')
def eerste(t):
    rest=re.sub(r'#\w+|@[\w.]+',' ',t).strip(); return re.split(r'[.!?\n]',rest)[0].lower() if rest else ''
test('fyp/foryou/viral tag', lambda t: bool(re.search(r'#(fyp|foryou|foryoupage|viral|xyzbca|trending)\b',t.lower())))
test('getal: aantal+zelfst. (3 tips)', lambda t: bool(re.search(r'\b\d+\s+(ways?|tips?|things|reasons|steps|addons?|add-ons?|tricks|hacks|minutes?|seconds?|hours?|days?|prints?|models?)\b',eerste(t))))
test('getal: maat/geld ($,mm,%)', lambda t: bool(re.search(r'\$\s?\d|\d+\s?(mm|cm|%|k\b)',eerste(t))))
test('getal: jaartal/versie', lambda t: bool(re.search(r'\b(19|20)\d\d\b|\bv?\d\.\d',eerste(t))))
test('getal: ander', lambda t: bool(re.search(r'\d',eerste(t))) and not re.search(r'\b\d+\s+(ways?|tips?|things|reasons|steps|addons?|add-ons?|tricks|hacks|minutes?|seconds?|hours?|days?|prints?|models?)\b|\$\s?\d|\d+\s?(mm|cm|%|k\b)|\b(19|20)\d\d\b|\bv?\d\.\d',eerste(t)))
test('vraag aan het eind', lambda t: re.sub(r'#\w+|@[\w.]+','',t).strip().endswith('?'))
test('vraag in eerste zin', lambda t: '?' in re.sub(r'#\w+|@[\w.]+',' ',t).strip()[:len(eerste(t))+1])
test('"you/your" in eerste zin', lambda t: bool(re.search(r'\byou(r)?\b',eerste(t))))
test('productnaam/merk @ of "thanks"', lambda t: bool(re.search(r'thanks to|sponsored|#ad\b|partner',t.lower())))
test('ontbreekt niche-tag (#3d.. #blender..)', lambda t: '#' in t and not re.search(r'#(3d\w*|blender\w*|b3d|print\w*|maker\w*|cosplay\w*|fdm|resin\w*|bambu\w*|prusa\w*|creality\w*|cad\w*|engineer\w*|filament\w*)',t.lower()))
test('"link in bio"', lambda t: 'link in bio' in t.lower() or 'link in my bio' in t.lower())
test('"comment"', lambda t: bool(re.search(r'\bcomment',t.lower())))
# ricntval: alleen kleine accounts (mediaan views < 5000)
print('==== na correctie 3D')
def e2(t): return re.sub(r'\b3d\b','',eerste(t))
test('echt getal in eerste zin (geen 3D)', lambda t: bool(re.search(r'\d',e2(t))))
test('onderwerpwoord in eerste zin (3D/print/Blender)', lambda t: bool(re.search(r'\b3d\b|\bprint|\bblender\b|\bb3d\b',eerste(t))))
test('"3D printed" in eerste zin', lambda t: bool(re.search(r'3d print',eerste(t))))
test('Blender in eerste zin', lambda t: bool(re.search(r'\bblender\b',eerste(t))))
test('hoofdletterwoord (geen merk)', lambda t: bool(re.search(r'\b(?!STLFLIX|HALO|FDM|PLA|PETG|TPU|CNC|STL|DIY)[A-Z]{4,}\b',re.sub(r'#\w+|@[\w.]+',' ',t))))
print('==== I made')
test('"I made/built/designed" begin', lambda t: bool(re.match(r'\W*(i|we)\s+(made|built|designed|created|printed|3d printed|modeled|turned)\b', re.sub(r'#\w+|@[\w.]+',' ',t).strip().lower())))
test('"I made" ergens', lambda t: bool(re.search(r'\b(i|we)\s+(made|built|designed|created)\b', t.lower())))
test('prijs in onderschrift ($)', lambda t: bool(re.search(r'[$€£]\s?\d', t)))
