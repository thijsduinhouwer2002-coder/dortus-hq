import json,re,sys,statistics as st
R=json.load(open(sys.argv[1]))
NEG={'grind/traag/muur':r'grind|tedious|too slow|slow progress|takes (so|too) long|stuck|wall|hours? (of|to) (wait|unlock)',
'te weinig te doen/kort/saai':r'nothing to do|not much to do|little to do|short|boring|repetitive|shallow|lack of content|no content|run out|ran out|finished (it|the game)|beat (it|the game)|end ?game',
'moet steeds klikken/niet idle':r'not (really )?idle|active|have to click|constant(ly)? click|babysit|micromanag|attention|keep (checking|clicking)',
'zwaar voor pc/neemt scherm':r'cpu|gpu|fps|performance|lag|ram\b|memory|screen space|takes up|too (big|large)|window|monitor|taskbar|resolution|fullscreen',
'bugs/save weg':r'bug|crash|glitch|broken|lost (my )?(save|progress)|save (file|got|was)|freez',
'geld/dlc/prijs':r'dlc|microtransaction|cash|gacha|pay(ing)? (to|for)|price|overpriced|money|monetiz',
'doel/zin ontbreekt':r'no (real )?(goal|point|purpose|reason)|pointless|what.s the point|aimless|no progression',
'weinig controle/keuze':r'no control|can.t (choose|control|move|place)|no choice|random|rng',
'interactie/geen invloed':r'interact|just watch|watching|screensaver'}
POS={'ontspannend/rustig':r'relax|chill|cozy|cosy|calm|peaceful|zen|wholesome',
'mooi/kunst/pixel':r'cute|beautiful|art|pixel|adorable|charming|gorgeous|pretty|aesthetic',
'naast werk/studie':r'work|study|studying|while (i|you)|background|second monitor|side',
'voortgang/ontgrendelen':r'progress|unlock|upgrade|grow|expand|collect',
'muziek/geluid':r'music|sound|ost|soundtrack',
'prijs/waar voor geld':r'price|cheap|worth|bucks|\$',
'humor/grappig':r'funny|hilarious|humor|humour|lol\b|silly|laugh',
'neemt weinig ruimte/licht':r'small|unobtrusive|doesn.t take|lightweight|bottom of (my|the) screen|taskbar'}
naam={'2666510':"Rusty's Retirement",'3416070':"Ropuka's Idle Island",'3167550':'Tiny Pasture','4623570':'Deskrawl'}
def tel(lijst,D):
    return {k:sum(1 for x in lijst if re.search(rx,x['tekst'].lower())) for k,rx in D.items()}
tot={'neg':{},'pos':{}};n={'neg':0,'pos':0}
for a,d in R.items():
    print('\n##',naam[a])
    for kant,D in(('neg',NEG),('pos',POS)):
        l=d[kant];t=tel(l,D);n[kant]+=len(l)
        for k,v in t.items(): tot[kant][k]=tot[kant].get(k,0)+v
        u=[x['uren'] for x in l if x['uren'] is not None]
        print(kant,len(l),'uren mediaan',round(st.median(u),1) if u else '-', 'onder 2u:',sum(1 for x in u if x<2),'boven 20u:',sum(1 for x in u if x>20))
        print('  ',sorted(t.items(),key=lambda z:-z[1]))
print('\n## Totaal')
for kant in tot: print(kant,n[kant],sorted(tot[kant].items(),key=lambda z:-z[1]))
