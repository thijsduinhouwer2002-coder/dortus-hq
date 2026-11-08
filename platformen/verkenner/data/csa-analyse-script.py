# Analyse CLIP STUDIO ASSETS: GOLD-cohort en gratis/Clippy-steekproef. Gebruik: python3 csa-analyse-script.py
import json,collections,statistics as st,glob
corp=set(json.load(open('csa-corp-ids.json')))
def load(fs):
    d={}
    for f in fs:
        for l in open(f):
            r=json.loads(l); d[r['material_id']]=r
    return list(d.values())
def stats(rs,label):
    pc=[int(r['purchase_count']) for r in rs]
    if not pc: print(label,0);return
    pct=lambda k:round(100*sum(p>=k for p in pc)/len(pc),1)
    print(f"{label}: n={len(pc)} mediaan={st.median(pc)} 0={pct(0)-pct(1):.1f}% 1+={pct(1)}% 10+={pct(10)}% 100+={pct(100)}% 1000+={pct(1000)}% makers={len({r['clip_user_id'] for r in rs})}")
gold=[r for r in load(['csa-gold-mrt-okt.jsonl']) if r['material_id'] not in corp]
coh=[r for r in gold if r['_maand'] in ('2026-05','2026-06','2026-07','2026-08')]
print("== GOLD zonder bedrijven ==")
for m in sorted({r['_maand'] for r in gold}): stats([r for r in gold if r['_maand']==m],m)
stats(coh,"cohort mei-aug")
# per maker
mk=collections.Counter(r['clip_user_id'] for r in coh)
stats([r for r in coh if mk[r['clip_user_id']]<10],"cohort, makers met <10 GOLD-items in mei-aug")
stats([r for r in coh if mk[r['clip_user_id']]>=10],"cohort, makers met 10+")
try:
    hist=json.load(open('csa-makers.json'))
    nieuw=[r for r in coh if hist.get(r['clip_user_handle'],{}).get('gold_voor_mei_2026',1)==0]
    stats(nieuw,"cohort, makers zonder GOLD-items voor mei 2026 (nieuwe verkopers)")
    nieuw25=[r for r in coh if hist.get(r['clip_user_handle'],{}).get('gold_voor_2026',1)==0]
    stats(nieuw25,"cohort, makers zonder GOLD-items voor 2026")
    print("nieuwe verkopers (geen GOLD voor mei 2026):",sorted({r['clip_user_handle'] for r in nieuw}))
except FileNotFoundError: print("geen makers-bestand")
# omzet schatting per maker in cohort: som downloads*prijs*0.7
om=collections.defaultdict(int)
for r in coh: om[r['clip_user_handle']]+=int(r['purchase_count'])*int(r['gold'])
v=sorted(om.values(),reverse=True)
print("GOLD-omzet (downloads x prijs) per maker, cohort-items:",'mediaan',st.median(v),'top10',v[:10])
print("makers met >=10.000 GOLD (bruto) uit cohort-items:",sum(x>=10000 for x in v),"van",len(v), " >=50.000:",sum(x>=50000 for x in v))
print("types cohort:",collections.Counter(r['material_type'] for r in coh).most_common())
for t in ['other_3dmodel','catalog','image']:
    stats([r for r in coh if r['material_type']==t],"cohort type "+t)
print("prijs mediaan",st.median([int(r['gold']) for r in coh]))
print("== Alle materialen (gratis, Clippy, GOLD) ==")
allr=[r for r in load(glob.glob('csa-mei-aug.jsonl')+['csa-juli.jsonl']) if r['material_id'] not in corp]
for m in sorted({r['_maand'] for r in allr}):
    rs=[r for r in allr if r['_maand']==m]
    stats([r for r in rs if r['point_type']=='0'],m+" gratis")
    stats([r for r in rs if int(r['clippy'])>0 and int(r['gold'])==0],m+" alleen Clippy")
    stats([r for r in rs if int(r['gold'])>0],m+" GOLD")
