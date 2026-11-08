# Haalt per betaalde plugin uit pluglist.php de marketplace-pagina op (installaties, downloads 90 dagen, prijzen).
# Gebruik: python3 moodle-marketplace-haal-script.py pluglist.json uit.jsonl   (10 s tussen verzoeken, robots.txt crawl-delay)
import json,sys,re,html,time,subprocess,os
pl=json.load(open(sys.argv[1]))['plugins']; uit=sys.argv[2]
done=set()
if os.path.exists(uit):
    for l in open(uit): done.add(json.loads(l)['component'])
paid=[p for p in pl if p.get('isPaid')]
for p in paid:
    c=p['component']
    if c in done: continue
    url=f"https://marketplace.moodle.com/plugins/{c}"
    t=subprocess.run(['curl','-sL','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
    t2=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S); t2=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t2)))
    g=lambda r: (re.search(r,t2).group(1) if re.search(r,t2) else None)
    vs=p['versions']; first=min(v['timecreated'] for v in vs) if vs else None
    rec=dict(component=c,name=p['name'],eerste_versie=first,laatste=p['timelastreleased'],
        installaties=g(r'Installations:\s*([\d,]+)'),downloads90=g(r'Downloads \(last 90 days\):\s*([\d,]+)'),
        onderhouden=g(r'Maintained by (.{0,120}?) (?:The|A |An |\w+ \w+ for)'),
        prijzen=re.findall(r'(\$[\d,\.]+ USD/\w+|€[\d,\.]+ EUR/\w+|\$[\d,\.]+ USD)',t2)[:6],
        gratis_optie=('Free option available' in t2) or (' Price option: Free' in t2),
        kop=t2[t2.find('Maintained by'):t2.find('Maintained by')+400] if 'Maintained by' in t2 else t2[:300])
    open(uit,'a').write(json.dumps(rec,ensure_ascii=False)+'\n'); time.sleep(10)
