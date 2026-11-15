# Haalt per Y8-spelpagina: plays (userInteractionCount), Developer en "Added on" uit de tekst.
# Gebruik: python3 y8-haal-script.py urls.txt aantal uit.csv  (willekeurige steekproef, seed 15)
import sys,re,csv,time,random,subprocess,html
from concurrent.futures import ThreadPoolExecutor
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]; random.seed(15); urls=random.sample(urls,int(sys.argv[2]))
def get(u):
    time.sleep(0.4)
    h=subprocess.run(["curl","-s","-m","30",u],capture_output=True,text=True).stdout
    p=re.search(r'"userInteractionCount":(\d+)',h)
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S);t=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)))
    d=re.search(r'Developer: (.*?) Added on (\d+ \w+ \d{4})',t); a=re.search(r'Added on (\d+ \w+ \d{4})',t)
    tech="html5" if "HTML5" in t[:3000] else ("flash" if "Ruffle" in t[:3000] else "")
    return [u.rsplit('/',1)[-1], d.group(1) if d else "", a.group(1) if a else "", p.group(1) if p else ""]
with ThreadPoolExecutor(3) as ex: rows=list(ex.map(get,urls))
w=csv.writer(open(sys.argv[3],"w")); w.writerow(["slug","maker","toegevoegd","plays"]); w.writerows(rows)
