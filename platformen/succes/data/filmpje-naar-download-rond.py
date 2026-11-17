# Per filmpje over een add-on: downloads per dag van de versie die liep op de dag van het filmpje,
# naast de versie ervoor en erna (downloads gelijk verdeeld over de dagen dat een versie de nieuwste was).
# Invoer: csv met kolommen datum,views,slug,bron. Gebruik: python3 filmpje-naar-download-rond.py <in.csv> <werkmap>
import csv, sys, os, datetime
import re, subprocess, time
os.makedirs(sys.argv[2], exist_ok=True); os.chdir(sys.argv[2])
def versions(slug):
    # zelfde lezer als blendernation-versies-haal.py
    f = f'v_{slug}.html'
    if not os.path.exists(f):
        subprocess.run(["curl","-sS","-o",f,f"https://extensions.blender.org/add-ons/{slug}/versions/"]); time.sleep(1)
    h = open(f, errors='ignore').read()
    t = re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' | ',h)); t = re.sub(r'(\| )+','| ',t)
    out = []
    for m in re.finditer(r'\| (\d[\w.\-+]*) \| Compatibility \|.*?\| [\d.]+ [KMG]?B \| ([\d,]+) \| (\w+ \d+)\w\w, (\d{4}) \|', t):
        d = datetime.datetime.strptime(m.group(3)+' '+m.group(4), '%B %d %Y').date()
        out.append((m.group(1), int(m.group(2).replace(',','')), str(d)))
    return out
vandaag = datetime.date(2026, 11, 17)
w = csv.writer(sys.stdout)
w.writerow(['bron','datum','views','slug','versie_nu','start_nu','dag_in_versie','per_dag_voor','per_dag_nu','per_dag_na','verhouding','meetbaar'])
for r in csv.DictReader(open(sys.argv[1])):
    v = versions(r['slug'])
    if not v: w.writerow([r['bron'],r['datum'],r['views'],r['slug'],'geen versies']); continue
    v = sorted(reversed(v), key=lambda x: x[2])  # pagina staat nieuwste eerst; zelfde dag: latere versie achteraan
    rij = []
    for i,(nr,dl,d) in enumerate(v):
        s = datetime.date.fromisoformat(d)
        e = datetime.date.fromisoformat(v[i+1][2]) if i+1 < len(v) else vandaag
        rij.append((nr, dl, s, e, dl / max((e - s).days, 1)))
    f = datetime.date.fromisoformat(r['datum'])
    idx = [i for i,x in enumerate(rij) if x[2] <= f < x[3] or (x[2] <= f and i == len(rij)-1)]
    if not idx: w.writerow([r['bron'],r['datum'],r['views'],r['slug'],'voor eerste versie']); continue
    i = idx[0]; nu = rij[i]
    voor = rij[i-1][4] if i > 0 else None
    na = rij[i+1][4] if i+1 < len(rij) else None
    dag = (f - nu[2]).days; lengte = (nu[3] - nu[2]).days
    meet = 'ja' if voor and dag <= 3 and lengte <= 21 else 'nee'
    w.writerow([r['bron'],r['datum'],r['views'],r['slug'],nu[0],nu[2],dag,
                round(voor,1) if voor else '', round(nu[4],1), round(na,1) if na else '',
                round(nu[4]/voor,2) if voor else '', meet])
