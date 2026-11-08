# Olaf 8 nov 2026: zoekt print-add-ons op Superhive (zoeken in categorie Addons, id 6, gesorteerd op verkoop, pagina 1-2)
# en haalt per product: prijs, verkoopteller, gepubliceerd, maker, ratings, Blender-versie, omschrijving.
# Gebruik: python3 -I superhive-print-zoek-script.py uit.jsonl   (hervat: slaat slugs over die al in uit.jsonl staan)
# Zoektreffers per woord komen in superhive-print-zoektreffers-2026-11-08.json.
import re,sys,json,subprocess,time,html,urllib.parse,os,concurrent.futures as cf
out=sys.argv[1]
Q=["3d print","3d printing","printable","stl","3mf","split print","connector","dowel","hollow","wall thickness",
   "overhang","print support","lithophane","relief","bas relief","keychain","name tag","manifold","watertight",
   "tolerance","miniature base","resin","slicer","magnet","puzzle","joint","hinge","print ready",
   "printer","cookie cutter","emboss","engrave","mold","mould","lattice","cosplay","articulated","print in place",
   "screw thread","drain","infill","mesh repair","non-manifold","miniature","tabletop","sign","nameplate","figurine"]
def curl(u):
    return subprocess.run(['curl','-sL','--max-time','30','-A','Mozilla/5.0 (dortus-onderzoek)',u],capture_output=True,text=True).stdout
zt='superhive-print-zoektreffers-2026-11-08.json'
if os.path.exists(zt): hits=json.load(open(zt))
else:
    hits={}
    for q in Q:
        for p in (1,2):
            u='https://superhivemarket.com/search?'+urllib.parse.urlencode({'search[q]':q,'search[category_id]':6,'sort_sales':'desc','page':p})
            sl=re.findall(r'href="/products/([^"?/]+)\?search_id',curl(u))
            for s in dict.fromkeys(sl): hits.setdefault(s,[]).append(q)
            time.sleep(0.5)
            if len(set(sl))<20: break
    json.dump(hits,open(zt,'w'))
done=set()
if os.path.exists(out):
    for l in open(out): done.add(json.loads(l)['slug'])
def txt(h): return re.sub(r'\s+',' ',re.sub('<[^>]+>','|',h))
def info(s):
    t=curl('https://superhivemarket.com/products/'+s); x=txt(t)
    def na(lbl,n=120):
        i=x.find('|'+lbl+'|')
        if i<0: return None
        return re.sub(r'\|+','|',x[i+len(lbl)+2:i+len(lbl)+2+n]).strip('| ').split('|')[0].strip()
    d={'slug':s,'zoekwoorden':hits[s],'sales':na('Sales'),'published':na('Published'),'blender':na('Blender Version')}
    m=re.search(r'"price":"([\d.]+)"',t); d['prijs']=float(m.group(1)) if m else None
    m=re.search(r'"seller":\{"@type":"[A-Za-z]+","name":"([^"]*)"',t); d['maker']=html.unescape(m.group(1)) if m else None
    m=re.search(r'"reviewCount":"?(\d+)',t); d['reviews']=int(m.group(1)) if m else 0
    m=re.search(r'"ratingValue":"?([\d.]+)',t); d['rating']=float(m.group(1)) if m else None
    m=re.search(r'<title>([^<]*)',t); d['titel']=html.unescape(m.group(1)).strip() if m else None
    m=re.search(r'"description":"([^"]{0,300})',t); d['omschrijving']=html.unescape(m.group(1)) if m else None
    time.sleep(0.3); return d
todo=[s for s in hits if s not in done]
print(len(hits),len(todo),flush=True)
with open(out,'a') as f, cf.ThreadPoolExecutor(3) as ex:
    for d in ex.map(info,todo): f.write(json.dumps(d)+'\n'); f.flush()
