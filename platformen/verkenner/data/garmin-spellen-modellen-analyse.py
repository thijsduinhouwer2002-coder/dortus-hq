# Vera 13 nov 2026: tel horlogemodellen die reviewers van Garmin-spellen noemen (uitvoer van garmin-spellen-reviews-modellen-script.py)
# Gebruik: python3 -I garmin-spellen-modellen-analyse.py garmin-spellen-reviews-2026-11-13.jsonl
import json,re,sys,collections
M=[('Forerunner 255',r'(fr|forerunner) ?255'),('Forerunner 265',r'(fr|forerunner) ?265'),('Forerunner 965',r'(fr|forerunner) ?965'),('Forerunner 165',r'(fr|forerunner) ?165'),
('Forerunner 970/570',r'(fr|forerunner) ?(970|570)'),('Forerunner 245/745/945/55 (oud)',r'(fr|forerunner) ?(245|745|945|55)\b'),('Forerunner overig',r'forerunner|\bfr ?\d{2,3}'),
('fenix 8',r'f[eé]nix ?8'),('fenix 7',r'f[eé]nix ?7'),('fenix 6 of ouder',r'f[eé]nix ?[56]'),('fenix overig',r'f[eé]nix'),('epix',r'epix'),
('Venu 3/4/X1',r'venu ?(3|4|x1)'),('Venu overig',r'venu'),('vivoactive 5/6',r'vivo ?active ?(5|6)'),('vivoactive overig',r'vivo ?active|vivoactiv'),
('Instinct 3',r'instinct ?3'),('Instinct 2 of ouder',r'instinct ?2|instinct\b'),('Enduro',r'enduro'),('Approach',r'approach'),('Descent',r'descent')]
c=collections.Counter(); tot=0; met=0; tm=collections.Counter()
touch=re.compile(r'touch ?screen|no touch|without touch|touch display|ohne touch|non[- ]touch|buttons? (don.t|do not|doesn.t) work',re.I)
for l in open(sys.argv[1]):
  x=json.loads(l)
  for v in x['reviews']:
    t=v['t'].lower(); tot+=1
    if not t: continue
    hit=False
    for naam,r in M:
      if re.search(r,t): c[naam]+=1; hit=True; break
    met+=hit
    if touch.search(t): tm[x['naam']]+=1
print('reviews',tot,'met modelnaam',met)
for k,v in c.most_common(): print(f'{k}: {v}')
print('klachten over touch of knoppen:',sum(tm.values()),tm.most_common(8))
