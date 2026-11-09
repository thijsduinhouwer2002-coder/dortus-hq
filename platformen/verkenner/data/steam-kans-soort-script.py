"""Soort per app op alleen titel + korte tekst (eerste treffer in volgorde), en per soort de vraag (reviews) en de tevredenheid.
Gebruik: python3 -I steam-kans-soort-script.py <uitmap>"""
import json,sys,re,statistics as st
out=sys.argv[1]
A=json.load(open(out+'/analyse.json'));D={json.loads(l)['appid']:json.loads(l) for l in open(out+'/details.jsonl')}
ORDE=[('idle-rpg/gevecht',r'rpg|dungeon|loot|raid|hero|warrior|battle|monster|mobs|goblin|defen|slay|enem|squad|adventure team'),
('vriendin/anime-figuur',r'girlfriend|wife|fianc|mom\b|mother|stepmom|sister|waifu|anime|girl\b|lilith|princess|maid'),
('focus/werkhulp',r'focus|pomodoro|productiv|study|work session|to-?do|task|habit|deadline'),
('vissen',r'fish|angler|pond'),
('huisdier/dier verzorgen',r'\bpet|cat\b|kitty|kitten|dog\b|puppy|hamster|bird|animal|creature|critter|axolotl|frog|duck|slime'),
('tuin/boerderij',r'farm|garden|plant|crop|flower|mushroom|seed|grow'),
('winkel/fabriek/stad',r'shop|market|store|factory|tavern|town|city|village|restaurant|cafe|bakery|train|station|mine|mining|dig'),
('kamer/sfeer/muziek',r'room|cottage|cozy space|lofi|lo-fi|music|ambient|decorat'),
('toets/klik-teller',r'keystroke|keyboard|typing|click|tap\b|every key'),
]
def soort(x):
    t=(x['title']+' '+D[x['appid']].get('short','')).lower()
    for k,rx in ORDE:
        if re.search(rx,t): return k
    return 'overig'
for x in A: x['soort']=soort(x)
json.dump(A,open(out+'/analyse-soort.json','w'))
w=[x for x in A if x['price']>0 and '2026-01-01'<=x['rel']<='2026-09-30']
oud=[x for x in A if x['price']>0 and x['rel']<'2026-01-01']
print('soort | betaald jan-sep 2026 | mediaan rev | 10+ | 100+ | som rev 2026 | gewogen %pos 2026 | aandeel rev bij apps <80% | oudere betaalde apps | som rev oud')
for k in [o[0] for o in ORDE]+['overig']:
    g=[x for x in w if x['soort']==k]; o=[x for x in oud if x['soort']==k]
    if not g and not o: continue
    v=sorted(x['rev'] for x in g); s=sum(v)
    wp=sum(x['rev']*(x['pos'] or 0) for x in g)/s if s else 0
    laag=sum(x['rev'] for x in g if x['pos'] is not None and x['pos']<80)/s if s else 0
    print(f"{k} | {len(g)} | {v[len(v)//2] if v else 0} | {sum(1 for i in v if i>=10)} | {sum(1 for i in v if i>=100)} | {s} | {wp:.0f}% | {laag:.0%} | {len(o)} | {sum(x['rev'] for x in o)}")
