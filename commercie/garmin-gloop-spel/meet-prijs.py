# Chris 15 nov 2026: prijs tegen downloads bij betaalde Garmin-spellen, zonder ThijsGer/QuadroGames en zonder de 10 die (waarschijnlijk) eerst gratis waren
# Gebruik: python3 -I prijs2.py garmin-spellen-details-2026-11-13.jsonl
import json,sys,datetime,collections
rows=[json.loads(l) for l in open(sys.argv[1])]
weg={('Crossy Road 3D','MangoIQ'),('Stack - Blocks Game','garminland'),('Stack','MangoIQ'),('Google Dinosaur Game','MangoIQ'),
 ('Flags Quiz Game – Flag Trivia','KBialy'),('Dots And Boxes (SP, MP & AI)','nioquant'),('Tic Tac Toe (SP & MP)','nioquant'),
 ('Connect4 (SP, MP & AI)','nioquant'),('ZigZag - Reflex Game','garminland')}
now=datetime.datetime(2026,11,13)
def age(r): return (now-datetime.datetime.fromtimestamp(r['eerst']/1000)).days/30.4 if r.get('eerst') else None
paid=[r for r in rows if r['prijs'] and r['maker'] not in ('ThijsGer','QuadroGames') and (r['naam'],r['maker']) not in weg
      and not (r['maker']=='li2niu' and r['naam'].startswith('Snake'))]
def b(p): return '1,99 of minder' if p<=1.99 else ('2,00 tot 2,99' if p<3 else '3,00 en meer')
for lo,hi,lab in [(3,10,'3 tot 10 maanden oud'),(10,60,'10 maanden en ouder'),(0,3,'jonger dan 3 maanden')]:
    print('##',lab)
    g=collections.defaultdict(list)
    for r in paid:
        a=age(r)
        if a is not None and lo<=a<hi: g[b(r['prijs'])].append(r)
    for k in ['1,99 of minder','2,00 tot 2,99','3,00 en meer']:
        L=g[k]; n=len(L)
        if not n: print(k,'n 0'); continue
        h=sum(r['dl']>=100 for r in L); t=sum(r['dl']>=1000 for r in L)
        print(f"{k} | n {n} | mediaan {sorted(r['dl'] for r in L)[n//2]}+ | 100+ {h} ({round(100*h/n)}%) | 1.000+ {t} ({round(100*t/n)}%) | top: "+
              ', '.join(f"{r['naam'][:24]} ${r['prijs']} {r['dl']}+" for r in sorted(L,key=lambda r:-r['dl'])[:4]))
