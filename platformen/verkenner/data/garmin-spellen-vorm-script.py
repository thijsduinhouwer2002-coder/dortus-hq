# Vera 13 nov 2026: deel alle Garmin-spellen grof in op vorm (op naam). Gebruik: python3 -I garmin-spellen-vorm-script.py garmin-niet-wijzerplaten-2026-11-09.json.gz [lijst.txt]
import gzip,json,re,sys,collections
d=json.load(gzip.open(sys.argv[1]))
g=[x for x in d if x['cat']=='206']
V=[('stappen/fitness-spel',r'step|walk|run.*rpg|steprpg|farmer|fitness|habit|beastie|move|stride|pace'),
 ('huisdier',r'pet|tamagotchi|watchkin|critter|skyling|friend|beastie'),
 ('idle/tycoon/bouwen',r'idle|tycoon|builder|colony|farm|clicker|craft'),
 ('stapelen/timing',r'stack|tower|timber|drwal|chop'),
 ('flappy/vliegen',r'flappy|floppy|wings|fly|bird|chopper|helicopter'),
 ('runner/springen/dino',r'run|dino|jump|kangaroo|hop|crossy|climb|drive|racing|kart|road|zigzag'),
 ('snake',r'snake|blobs|worm'),
 ('blokjes/tetris/brick',r'tetris|block|brick|drop|tile|bubble'),
 ('2048/puzzel',r'2048|puzzle|sudoku|sokoban|maze|15-|slider|minesweep|mines|sweeper|mastermind|simon|memory'),
 ('woord/quiz',r'word|quiz|trivia|flag|hangman|guess'),
 ('kaart/casino/dobbel',r'solitaire|blackjack|poker|card|yahtzee|dice|farkle|tri peaks|eremit|pasjans|slay'),
 ('bord (schaak, dammen, 4 op rij)',r'chess|checker|reversi|connect 4|four|tic tac|go\b|backgammon'),
 ('pong/ballen/sport',r'pong|golf|hoops|billiard|pinball|paddle|ball|soccer|football|tennis|bowling|flick'),
 ('schieten/ruimte/arcade',r'astro|space|shoot|sniper|asteroid|roid|blast|invader|eagle|force|zombie|pac|catapult|axe|ninja|fruit|void|warp|orbit|lander|hunter|fishing|arena|survivor'),
]
def vorm(n):
  n=n.lower()
  for v,r in V:
    if re.search(r,n): return v
  return 'overig'
rows=collections.defaultdict(list)
for x in g:
  x['vorm']=vorm(x['naam'] or '')
  x['prijs']=x['pricing']['salePrice']['price'] if x['pricing'] else 0
  rows[x['vorm']].append(x)
out=[]
for v,xs in sorted(rows.items(),key=lambda kv:-len(kv[1])):
  bet=[x for x in xs if x['prijs']]
  grat=[x for x in xs if not x['prijs'] and x['pay']!=1]
  bg=max(grat,key=lambda x:(x['dl'],x['reviews']),default=None)
  bb=max(bet,key=lambda x:(x['dl'],x['reviews']),default=None)
  print(f"{v}: {len(xs)} spellen, betaald {len(bet)}, gratis {len(grat)}; gratis 10k+: {sum(x['dl']>=10000 for x in grat)}, gratis 1k+: {sum(x['dl']>=1000 for x in grat)}; betaald 1k+: {sum(x['dl']>=1000 for x in bet)}")
  if bg: print(f"   beste gratis: {bg['naam'][:40]} ({bg['maker']}) {bg['dl']}+ {bg['reviews']}r {bg['rating']}")
  if bb: print(f"   beste betaald: {bb['naam'][:40]} ({bb['maker']}) {bb['dl']}+ {bb['reviews']}r {bb['rating']} ${bb['prijs']}")
if len(sys.argv)>2:
  for x in sorted(g,key=lambda x:(x['vorm'],-x['dl'])):
    print(x['vorm'],'|',x['naam'][:45],'|',x['maker'],'|',x['dl'],x['reviews'],x['prijs'] or ('U' if x['pay']==1 else 0),file=open(sys.argv[2],'a'))
