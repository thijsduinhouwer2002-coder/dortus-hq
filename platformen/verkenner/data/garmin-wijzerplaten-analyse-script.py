# Analyse betaalde Garmin-wijzerplaten van het laatste jaar. Invoer: wijzerplaten.json.gz (uit haal.py).
import json,gzip,re,sys,csv,statistics as st,datetime as dt,collections as C
D=list({a["id"]:a for f in sys.argv[1:] for a in json.load(gzip.open(f,"rt"))}.values())
NU=dt.datetime(2026,11,16)
def d(ms): return dt.datetime.fromtimestamp(ms/1000,dt.UTC).replace(tzinfo=None) if ms else None
for a in D: a['eerste']=d(a['first'])
jaar=[a for a in D if a['eerste'] and a['eerste']>=dt.datetime(2025,11,16)]
betaald=[a for a in jaar if a['prijs']]
gratis=[a for a in jaar if not a['prijs']]
print("alle opgehaald",len(D),"jaar",len(jaar),"betaald",len(betaald),"gratis",len(gratis))
print("valuta",C.Counter(a['valuta'] for a in betaald).most_common(5),"trial",sum(1 for a in betaald if a['trial']))
FIG=r"\b(cat|cats|kitty|kitten|dog|puppy|pet|pets|animal|animals|cartoon|mascot|cute|kawaii|chibi|dino|dinosaur|t-rex|panda|bear|penguin|owl|fox|bunny|rabbit|duck|frog|monster|tamagotchi|creature|critter|otter|hamster|pikachu|anime|alien|robot|slime|blob|unicorn|dragon|turtle|whale|fish|octopus|shark|bird|chick|sloth|koala|raccoon|capybara|axolotl|pug|corgi|minion|astronaut|snowman|santa|elf|gnome|mushroom|virtual pet|buddy|mochi)\b"
GRAP=r"\b(funny|joke|jokes|humou?r|meme|silly|lol|sarcastic|sarcasm|cheeky|goofy|grumpy|lazy|roast|witty)\b"
FUN={'stappen':r"\bsteps?\b",'hartslag':r"heart ?rate|\bhr\b|\bbpm\b",'batterij':r"\bbattery\b",'aod':r"always[- ]on|\baod\b|low[- ]power",
 'body battery':r"body ?battery",'weer':r"weather|temperature|forecast",'calorieen':r"calorie",'meldingen':r"notification",'zon op/onder':r"sunrise|sunset",
 'stress':r"\bstress\b",'trappen':r"floors?",'afstand':r"distance",'datum':r"\bdate\b",'zelf velden kiezen':r"customi[sz]|configurable|data fields?|complication|choose (from|what|your)",
 'kleuren/thema':r"colou?rs?|themes?",'stapdoel/voortgang':r"goal|progress",'animatie':r"animat",'aanraken':r"touch|tap",'12/24 uur':r"12[ /-]?h|24[ /-]?h|12/24"}
def txt(a): return ((a['naam'] or '')+' \n '+(a['beschrijving'] or '')).lower()
for a in jaar:
    t=txt(a); kop=((a['naam'] or '')+' '+(a['beschrijving'] or '')[:300]).lower()
    a['figuur']=bool(re.search(FIG,kop)) or len(set(re.findall(FIG,t)))>=3
    a['grap']=bool(re.search(GRAP,kop))
    a['functies']=[k for k,r in FUN.items() if re.search(r,t)]
mk=C.Counter(a['makerId'] for a in jaar)          # alle wijzerplaten van de maker in het jaar
mkb=C.Counter(a['makerId'] for a in betaald)
def stats(L,naam):
    if not L: print(naam,0); return
    dl=[a['dl'] or 0 for a in L]
    r=lambda x:100*sum(v>=x for v in dl)/len(L)
    pr=[a['prijs'] for a in L if a['prijs']]
    print(f"{naam:42s} n={len(L):5d} med={st.median(dl):>5} 10+={r(10):4.0f}% 100+={r(100):4.1f}% 1000+={r(1000):4.1f}% 10000+={r(10000):4.2f}% prijs_med={st.median(pr) if pr else '-'} rev_med={st.median([a['reviews'] or 0 for a in L])}")
oud=[a for a in betaald if a['eerste']<dt.datetime(2026,8,16)]   # minstens 3 maanden in de winkel
print("\n== betaald, alle vs minstens 3 maanden oud");stats(betaald,"betaald jaar");stats(oud,"betaald >=3 mnd");stats([a for a in gratis if a['eerste']<dt.datetime(2026,8,16)],"gratis >=3 mnd")
print("\n== per maand (betaald)")
for m,L in sorted(C.defaultdict(list,{}).items()): pass
pm=C.defaultdict(list)
for a in betaald: pm[a['eerste'].strftime('%Y-%m')].append(a)
for m in sorted(pm): stats(pm[m],m+f" (gratis {sum(1 for g in gratis if g['eerste'].strftime('%Y-%m')==m)})")
print("\n== prijsklassen (>=3 mnd)")
for lo,hi in [(0,1.5),(1.5,2.0),(2.0,2.5),(2.5,3.0),(3.0,4.0),(4.0,5.0),(5.0,99)]:
    stats([a for a in oud if lo<=a['prijs']<hi],f"${lo}-{hi}")
print("\n== makergrootte (betaalde in het jaar), >=3 mnd")
for lo,hi in [(1,3),(4,20),(21,50),(51,200),(201,99999)]:
    stats([a for a in oud if lo<=mk[a['makerId']]<=hi],f"maker met {lo}-{hi} wijzerplaten/jaar")
print("\n== figuur / grap (>=3 mnd)")
stats([a for a in oud if a['figuur']],"figuur");stats([a for a in oud if not a['figuur']],"geen figuur");stats([a for a in oud if a['grap']],"grap")
stats([a for a in oud if a['figuur'] and mk[a['makerId']]<=20],"figuur, kleine maker (<=20)");stats([a for a in oud if not a['figuur'] and mk[a['makerId']]<=20],"geen figuur, kleine maker")
print("\n== functies genoemd (>=3 mnd): aandeel bij 100+ vs onder 10")
top=[a for a in oud if (a['dl'] or 0)>=100]; flop=[a for a in oud if (a['dl'] or 0)<10]
for k in FUN: print(f"  {k:20s} 100+: {100*sum(k in a['functies'] for a in top)/len(top):4.0f}%   <10: {100*sum(k in a['functies'] for a in flop)/len(flop):4.0f}%   alle: {100*sum(k in a['functies'] for a in oud)/len(oud):4.0f}%")
for kol,f in [('beschrijving lang (>1500 tekens)',lambda a:len(a['beschrijving'] or '')>1500),('video',lambda a:a['video']),('5+ schermbeelden',lambda a:a['nscreens']>=5),('meer talen',lambda a:len(a['talen'])>1),('trial',lambda a:a['trial']),('60+ horloges',lambda a:a['ndev']>=60)]:
    stats([a for a in oud if f(a)],kol+" ja");stats([a for a in oud if not f(a)],kol+" nee")
print("\n== makers: geschatte verkopen (som ondergrens downloadklasse) betaald jaar")
agg=C.defaultdict(lambda:dict(n=0,dl=0,omzet=0,h=0,naam='',ngratis=0))
for a in betaald:
    g=agg[a['makerId']]; g['n']+=1; g['dl']+=a['dl'] or 0; g['omzet']+=(a['dl'] or 0)*a['prijs']*0.85; g['h']+=(a['dl'] or 0)>=100; g['naam']=a['maker']
for a in gratis:
    if a['makerId'] in agg: agg[a['makerId']]['ngratis']+=1
tot=sum(g['omzet'] for g in agg.values())
rk=sorted(agg.values(),key=lambda g:-g['omzet'])
print("makers met betaald:",len(agg),"totale geschatte omzet ondergrens $",round(tot))
cum=0
for i,g in enumerate(rk[:25]):
    cum+=g['omzet']; print(f"{i+1:2d} {g['naam'][:22]:22s} betaald={g['n']:4d} gratis={g['ngratis']:4d} 100+={g['h']:3d} dl_som={g['dl']:7d} omzet>=${g['omzet']:8.0f} cum={100*cum/tot:3.0f}%")
for p in [10,50]: print(f"top {p} makers aandeel omzet: {100*sum(g['omzet'] for g in rk[:p])/tot:.0f}%")
print("makers met >= $1000 ondergrens:",sum(g['omzet']>=1000 for g in rk),"; met >= $100:",sum(g['omzet']>=100 for g in rk))
json.dump([dict(id=a['id'],naam=a['naam'],maker=a['maker'],eerste=a['eerste'].strftime('%Y-%m-%d'),prijs=a['prijs'],dl=a['dl'],reviews=a['reviews'],rating=a['rating'],figuur=a['figuur'],grap=a['grap'],functies=a['functies'],makerwp=mk[a['makerId']],trial=a['trial'],talen=len(a['talen']),video=a['video'],nscreens=a['nscreens'],ndev=a['ndev']) for a in betaald],open('betaald.json','w'))
