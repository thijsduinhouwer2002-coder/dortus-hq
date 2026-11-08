# Vera 8 nov 2026: kijkt in de README van de nieuwste N communityplugins of ze betaling vragen.
import json,sys,re,subprocess,concurrent.futures as cf
N=int(sys.argv[1]); out=sys.argv[2]
def curl(u):
    return subprocess.run(['curl','-sL','--max-time','20',u],capture_output=True,text=True).stdout
pl=json.loads(curl('https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json'))
st=json.loads(curl('https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json'))
nieuw=pl[-N:]
PAT={'sleutel':r'licen[cs]e key|activation key|serial key','winkel':r'gumroad\.com|polar\.sh|lemonsqueezy|buy\.stripe|paddle\.com|payhip|ko-fi\.com/s/',
     'pro':r'\bpro version\b|\bpremium\b|\bpaid (plan|version|tier|feature)|\bsubscription\b|\bupgrade to\b|payment is required'}
def doe(p):
    t=''
    for br in ('HEAD','main','master'):
        t=curl(f"https://raw.githubusercontent.com/{p['repo']}/{br}/README.md")
        if t and not t.startswith('404'): break
    h={k:bool(re.search(v,t,re.I)) for k,v in PAT.items()}
    return {'id':p['id'],'naam':p['name'],'repo':p['repo'],'downloads':(st.get(p['id']) or {}).get('downloads'),'readme':len(t),**h}
with cf.ThreadPoolExecutor(6) as ex, open(out,'w') as f:
    for r in ex.map(doe,nieuw): f.write(json.dumps(r)+'\n')
print(len(pl))
