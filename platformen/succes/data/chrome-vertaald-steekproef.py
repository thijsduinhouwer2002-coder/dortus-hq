# Joris, run 34. Steekproef 45 top-3 en 45 plek 8-10 uit chrome-zoekplek: heeft de naam een Portugese (pt-BR) versie?
import csv,random,subprocess,re,time,html,json
R=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/succes/data/chrome-zoekplek-2026-11-17.csv')))
random.seed(34)
seen=set();rows=[]
for r in R:
  if r['id'] in seen: continue
  seen.add(r['id']);rows.append(r)
top=[r for r in rows if int(r['plek'])<=3]; laag=[r for r in rows if int(r['plek'])>=8]
S=random.sample(top,45)+random.sample(laag,45)
out=[]
for r in S:
  h=subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0','https://chromewebstore.google.com/detail/'+r['id']+'?hl=pt-BR'],capture_output=True,text=True).stdout
  t=re.search(r'<title>(.*?) - Chrome Web Store',h,re.S)
  pt=html.unescape(t.group(1)) if t else ''
  out.append({'id':r['id'],'plek':int(r['plek']),'naam':r['naam'],'pt':pt,'gebruikers':r['gebruikers'],'vertaald':bool(pt) and pt.strip()!=r['naam'].strip()})
  time.sleep(1.2)
json.dump(out,open('vertaald.json','w'),indent=1)
import statistics
for g,f in [('top3',lambda o:o['plek']<=3),('plek8-10',lambda o:o['plek']>=8)]:
  G=[o for o in out if f(o) and o['pt']]
  print(g,len(G),'vertaald',sum(o['vertaald'] for o in G))
