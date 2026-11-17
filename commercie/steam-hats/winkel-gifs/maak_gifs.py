# Maakt de 4 gifs voor de lange beschrijving op de Steampagina van Hats of the Fallen (Z6, voorstel Sem).
# Chris, 17 nov 2026. Bron: echte losse beelden uit de Windows-build (Olaf, tak schermen, commit 453aac1), 3 beelden per s.
# Gebruik: python3 maak_gifs.py <map-met-beelden> <uitmap>
#   <map-met-beelden> bevat demo/f<nr*5>.png en week/f<nr*5>.png zoals op schermen (steam-hol/winkel-1920-demo-160/los en ...-week-.../los).
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
for g in GIFS:
    schaal=W/g['bw']; h=int(round(160*schaal))
    lijst=[]
    for f in beelden(g['soort'],g['van'],g['tot']):
        s=Image.open(f).convert('RGBA').crop((g['x0'],0,g['x0']+g['bw'],160)).resize((W,h),Image.LANCZOS)
        a=achtergrond(W,h).convert('RGBA'); a.alpha_composite(s); lijst.append(a.convert('RGB'))
    gif_uit_beelden(lijst,f"{UIT}/{g['uit']}")
# gif 4: de hele strook klein boven een eenvoudig, eigen bureaublad (geen echt besturingssysteem, geen logo's)
H4=280; TB=12; STROOK=1450   # strook zonder het logpaneel rechts (Engelse tekst), zodat het spel groter staat
lijst=[]
for f in beelden('week',0,40):
    a=achtergrond(W,H4); d=ImageDraw.Draw(a)
    d.rounded_rectangle((60,26,330,150),6,fill=(236,238,242)); d.rectangle((60,26,330,40),fill=(206,210,220))   # leeg venster
    d.rounded_rectangle((300,56,560,180),6,fill=(246,247,249)); d.rectangle((300,56,560,70),fill=(214,218,228))
    for y in range(82,172,14): d.rectangle((316,y,316+((y*37)%180)+40,y+6),fill=(222,225,232))              # grijze regels, geen tekst
    d.rectangle((0,H4-TB,W,H4),fill=(28,32,44))                                                            # taakbalk
    s=Image.open(f).convert('RGBA').crop((0,0,STROOK,160)); sh=int(round(160*W/STROOK)); s=s.resize((W,sh),Image.LANCZOS)
    a=a.convert('RGBA'); a.alpha_composite(s,(0,H4-TB-sh)); lijst.append(a.convert('RGB'))
gif_uit_beelden(lijst,f'{UIT}/4-it-keeps-going-while-you-work.gif',fps=3,hold_eind=0)
for n in sorted(os.listdir(UIT)):
    if n.endswith('.gif'): print(n, os.path.getsize(f'{UIT}/{n}'), Image.open(f'{UIT}/{n}').size, Image.open(f'{UIT}/{n}').n_frames)
