# Fenna verhaal 22: claims over speeltijd in de winkeltekst naast de meest behulpzame reviews.
import json, re, html, glob, csv, sys, statistics as st
S=sys.argv[1]; OUT=sys.argv[2]
win={json.loads(l)['appid']:json.loads(l) for l in open(S+'/winkel.jsonl')}
def soort(d):
    t=html.unescape(re.sub('<[^>]+>',' ',d['short']+' '+d['about'])).lower()
    if re.search(r"don't expect hours|not an infinitely|not a short",t): return 'eerlijk begrensd'
    if re.search(r'\d+\+?\s*hours of (content|meditative|gameplay|play)|hundreds of hours|tens of hours|thousands of hours of content',t): return 'uren genoemd'
    if re.search(r'endless|infinite|never[- ]ending|no end|no cap|forever|limitless',t): return 'eindeloos'
    return 'niets'
kort=re.compile(r"\b(short|not much content|lack(?:s|ing)? (?:of )?content|no content|runs? out of content|ran out|nothing (?:left|else|more) to do|finished (?:it|the game)|beat (?:it|the game)|completed (?:it|the game)|after \d+ ?(?:hours|h)\b.{0,40}(?:nothing|done|all)|too fast)",re.I)
grind=re.compile(r"\b(grind|grindy|slow(?:s|ed)? (?:down|to a crawl)|too slow|wall|takes forever|tedious)",re.I)
rows=[]
for f in glob.glob(S+'/breed/*.json'):
    d=json.load(open(f)); a=d['appid']; R=d['reviews']
    if len(R)<5: continue
    w=win[a]; neg=[r for r in R if not r['up']]; pos=[r for r in R if r['up']]
    rows.append({'appid':a,'naam':w['naam'],'soort_claim':soort(w),'reviews_totaal':int(w['reviews']),'pct_positief':int(w['pct'] or 0),'prijs':float(w['prijs'] or 0),
      'gelezen':len(R),'neg_gelezen':len(neg),'neg_te_kort':sum(1 for r in neg if kort.search(r['tekst'])),'neg_grind':sum(1 for r in neg if grind.search(r['tekst'])),
      'med_uur_pos':st.median([r['uur'] for r in pos if r['uur'] is not None]) if pos else '', 'med_uur_neg':st.median([r['uur'] for r in neg if r['uur'] is not None]) if neg else ''})
rows.sort(key=lambda r:-r['reviews_totaal'])
with open(OUT,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('spellen',len(rows))
from collections import defaultdict
g=defaultdict(list)
for r in rows: g[r['soort_claim']].append(r)
for k,v in g.items():
    neg=sum(r['neg_gelezen'] for r in v); 
    print(k,len(v),'mediaan %pos',st.median([r['pct_positief'] for r in v]),'neg gelezen',neg,'te kort',sum(r['neg_te_kort'] for r in v),'grind',sum(r['neg_grind'] for r in v),
      'med uur pos',round(st.median([r['med_uur_pos'] for r in v if r['med_uur_pos']!='']),1))
negall=sum(r['neg_gelezen'] for r in rows); print('alle neg',negall,'te kort',sum(r['neg_te_kort'] for r in rows),'grind',sum(r['neg_grind'] for r in rows))
mp=[r['med_uur_pos'] for r in rows if r['med_uur_pos']!='']; mn=[r['med_uur_neg'] for r in rows if r['med_uur_neg']!='']
print('mediaan over spellen: uur pos',st.median(mp),'uur neg',st.median(mn))
