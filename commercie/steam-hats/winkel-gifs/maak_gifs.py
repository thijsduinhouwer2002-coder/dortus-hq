# Maakt de 4 gifs voor de lange beschrijving op de Steampagina van Hats of the Fallen (Z6, voorstel Sem).
# Chris, 17 nov 2026. Bron: echte losse beelden uit de Windows-build (Olaf, tak schermen, commit 453aac1), 3 beelden per s.
# Gebruik: python3 maak_gifs.py <map-met-beelden> <uitmap> [alleen4]   (alleen4: maak alleen gif 4, dan is alleen hap/ nodig)
#   <map-met-beelden> bevat demo/, week/ en hap/ met f<nr*5>.png zoals op schermen (steam-hol/winkel-1920-demo-160/los en ...-week-.../los).
# Breedte 616 px: de breedte die Rusty's Retirement voor 3 van zijn 5 beschrijvingsbeelden gebruikt (GEZIEN 17 nov).
# Geen tekst in de gifs: Steam raadt dat aan, want tekst in beelden moet je per taal opnieuw maken (DERDEN, partner.steamgames.com/doc/store/page/description).
import json,os,subprocess,sys
from PIL import Image,ImageDraw
BRON,UIT=sys.argv[1],sys.argv[2]; os.makedirs(UIT,exist_ok=True)
W=616
LUCHT_BOVEN,LUCHT_ONDER=(46,58,92),(118,134,176)   # eigen bureaubladkleur, schemerblauw, geen merk
def achtergrond(w,h):
    im=Image.new('RGB',(w,h)); d=ImageDraw.Draw(im)
    for y in range(h):
        t=y/max(h-1,1); d.line((0,y,w,y),fill=tuple(int(LUCHT_BOVEN[k]+(LUCHT_ONDER[k]-LUCHT_BOVEN[k])*t) for k in range(3)))
    return im
def beelden(soort,van,tot): return [f'{BRON}/{soort}/f{i*5:08d}.png' for i in range(van,tot+1)]
GIFS=[
 # naam, soort, eerste, laatste beeld, uitsnede x0 en breedte in de strook van 1920x160
 dict(uit='1-heroes-come-in.gif',  soort='demo',van=141,tot=158,x0=760, bw=616),  # held loopt het hol in, over de spijkers, naar Gloop
 dict(uit='2-gloop-wears-their-hats.gif',soort='demo',van=152,tot=163,x0=1090,bw=308),  # hap en de emmer landt op Gloop (2x)
 dict(uit='3-they-come-back.gif',  soort='demo',van=188,tot=213,x0=440, bw=616),  # terugkomer met wrok (rode bel) op weg naar de spijkers
]
def gif_uit_beelden(lijst,pad,fps=3,hold_eind=4):
    tmp=pad+'.d'; os.makedirs(tmp,exist_ok=True)
    for k,im in enumerate(lijst): im.save(f'{tmp}/{k:04d}.png')
    for j in range(hold_eind): lijst[-1].save(f'{tmp}/{len(lijst)+j:04d}.png')
    subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(fps),'-i',f'{tmp}/%04d.png','-vf',
      'split[a][b];[a]palettegen=max_colors=192:stats_mode=full[p];[b][p]paletteuse=dither=sierra2_4a','-loop','0',pad],check=True)
for g in ([] if 'alleen4' in sys.argv[3:] else GIFS):
    schaal=W/g['bw']; h=int(round(160*schaal))
    lijst=[]
    for f in beelden(g['soort'],g['van'],g['tot']):
        s=Image.open(f).convert('RGBA').crop((g['x0'],0,g['x0']+g['bw'],160)).resize((W,h),Image.LANCZOS)
        a=achtergrond(W,h).convert('RGBA'); a.alpha_composite(s); lijst.append(a.convert('RGB'))
    gif_uit_beelden(lijst,f"{UIT}/{g['uit']}")
# gif 4 (run 72, na Daan 17 nov 01:30): uitsnede op de rechterhelft van het hol (x 700 tot 1460, zonder logpaneel),
# strook ±130 px hoog, boven alleen de onderrand van één werkvenster (gevulde regels in rustige kleuren, knipperend cursortje),
# eronder een taakbalk. Bron: hap/ = steam-hol/winkel-1920-week-160-momenthap-run43741420761/los (schermen).
# Wat er gebeurt: een munt vliegt naar de schat en Gloop knijpt tevreden zijn oog dicht (f210 tot f240), dan de hap:
# Gloop knijpt zijn oog dicht, er ligt een laars bij de schat (f280 tot f335). Het stille stuk ertussen (±13 s waarin niets beweegt)
# is weggelaten; de beelden zelf zijn echt en onbewerkt. Laatste beeld ±1 s stil.
X0,BW=700,760; TB=12; SH=int(round(160*W/BW)); VR=74; H4=VR+SH+TB
REGELS=[(36,180,(120,150,200)),(52,260,(150,170,150)),(36,120,(200,170,120)),(52,210,(150,160,190)),(36,90,(170,150,190))]
# Run 73 (na Daan 17 nov 02:45): het stille midden en het lange stille eind ingekort. Gemeten (pixelverschil per beeld,
# uitsnede x 700 tot 1460): beweging f205 tot f240 en f305 tot f315, verder stil. Nu: begin rustig op f215 (geen munt in de lucht),
# munt en knipoog f220 tot f240, dan één stil beeld (f300, gelijk aan f240), de hap f305 tot f315 (f315 is ook het eindbeeld: f320 en later zijn gelijk), eind 3 beelden (1 s) stil.
nrs=list(range(215,241,5))+[300]+list(range(305,316,5))
lijst=[]
for k,nr in enumerate(nrs):
    a=achtergrond(W,H4); d=ImageDraw.Draw(a)
    d.rounded_rectangle((22,-12,W-22,VR+20),8,fill=(244,245,248))                       # onderrand van één werkvenster
    y=6
    for kk,(x,lengte,kl) in enumerate(REGELS):
        d.rounded_rectangle((x,y,x+lengte,y+6),3,fill=kl); y+=12
    if k%2==0:                                                                          # knipperend cursortje achter de laatste regel
        x,lengte,_=REGELS[-1]; d.rectangle((x+lengte+6,y-14,x+lengte+8,y-4),fill=(60,70,90))
    d.rectangle((0,H4-TB,W,H4),fill=(28,32,44))                                         # taakbalk
    s=Image.open(f'{BRON}/hap/f{nr:08d}.png').convert('RGBA').crop((X0,0,X0+BW,160)).resize((W,SH),Image.LANCZOS)
    a=a.convert('RGBA'); a.alpha_composite(s,(0,VR)); lijst.append(a.convert('RGB'))
gif_uit_beelden(lijst,f'{UIT}/4-it-keeps-going-while-you-work.gif',fps=3,hold_eind=2)
for n in sorted(os.listdir(UIT)):
    if n.endswith('.gif'): print(n, os.path.getsize(f'{UIT}/{n}'), Image.open(f'{UIT}/{n}').size, Image.open(f'{UIT}/{n}').n_frames)
