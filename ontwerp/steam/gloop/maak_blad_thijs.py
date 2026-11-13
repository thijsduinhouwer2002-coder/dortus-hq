# Blad voor Thijs (Daan, 13 nov 2026): Gloop in 3 versies op ware grootte in de echte strook en vergroot, plus de huidige Gloop.
# Draai: python3 maak_blad_thijs.py <strook-120.png>   (schermen/steam-hol/main/strook-120.png, run 43417046565)
import os, sys
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import maak_gloop as mg, maak_blad as mb
KUNST = os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "godot", "kunst")
BG = (29, 20, 38); VAK = (63, 40, 70); TXT = (240, 230, 214); GOUD = (255, 205, 80)

def font(n):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(p): return ImageFont.truetype(p, n)
    return ImageFont.load_default()

strook = Image.open(sys.argv[1]).convert("RGBA")
X0, Y0, X1, Y1 = 380, 624, 720, 720   # schatkamer, zonder de regel van de testrunner erboven

def in_strook(g):
    s = strook.copy()
    if g is not None:
        patch = s.crop((524 - 48, 666, 582 - 48, 711)); s.paste(patch, (524, 666))  # oude Gloop weg met muur van een tegel links
        G = g.resize((g.width * 3, g.height * 3), Image.NEAREST)   # spel tekent op schaal 3
        s.paste(G, (552 - G.width // 2, 711 - G.height), G)
    return s.crop((X0, Y0, X1, Y1))

def frames(naam):
    st = Image.open(os.path.join(HIER, f"gloop_{naam}.png")); fw = st.width // 6
    f = [st.crop((i * fw, 0, (i + 1) * fw, st.height)) for i in range(6)]
    return f[0], f[4], f[5]

hoeden = [mg.hoed_beeld("kroon"), mg.hoed_beeld("puntmuts")]
oud = Image.open(os.path.join(KUNST, "slijm_groot2.png")).convert("RGBA").crop((0, 0, 20, 16))
rijen = [("Nu", "de Gloop van vandaag", None, oud)]
for naam, titel, uitleg in (("groot", "1  Groot", "groter, open oog, blosjes, lach"),
                            ("munt", "2  Muntje", "zoals 1, met een munt die in zijn buik glimt"),
                            ("glas", "3  Schatbuik", "doorzichtige buik met twee munten en belletjes")):
    rijen.append((titel, uitleg, naam, None))

W = 1800; RH = 330; H = 150 + RH * len(rijen) + 440
out = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(out)
d.text((30, 26), "Gloop: kies er een", fill=TXT, font=font(44))
d.text((30, 84), "Links op ware grootte in de echte strook van 120 px (Windows-build, run 43417046565). Rechts 8x vergroot: rust, hap, kauw, met hoedentoren.", fill=(200, 190, 180), font=font(20))
d.text((30, 112), "Ware grootte beslist. Alles is pixel voor pixel uit code. De kroon met de heksenhoed erop is de grap: hoeden van opgegeten helden.", fill=(200, 190, 180), font=font(20))
y = 150
for titel, uitleg, naam, img in rijen:
    d.rectangle((20, y, W - 20, y + RH - 14), fill=VAK)
    d.text((40, y + 14), titel, fill=GOUD, font=font(30)); d.text((40, y + 54), uitleg, fill=TXT, font=font(20))
    if naam is None:
        rust = img; hap = kauw = None; toren = mb.met_toren(img, hoeden, 2)
    else:
        rust, hap, kauw = frames(naam); toren = mb.met_toren(rust, hoeden, 2)
    out.paste(in_strook(rust), (40, y + 100)); out.paste(in_strook(toren), (40, y + 100 + 104))
    x = 420
    for b in (rust, hap, kauw, toren):
        if b is None: continue
        g = b.resize((b.width * 8, b.height * 8), Image.NEAREST)
        out.paste(g, (x, y + RH - 24 - g.height), g); x += g.width + 30
    y += RH
# toppers op dezelfde ware grootte
d.text((30, y + 6), "Ter vergelijking op ware grootte: Rusty's Retirement (figuren ±25 px) en Ropuka's Idle Island (±100 px), winkelplaatjes uit de Steam-API.", fill=(200, 190, 180), font=font(20))
v = Image.open(os.path.join(HIER, "vergelijk-ware-grootte.png")).convert("RGB")
r1 = v.crop((10, 24, 510, 384)); r2 = v.crop((520, 24, 1120, 404))  # niet schalen: ware grootte
out.paste(r1, (40, y + 40)); out.paste(r2, (40 + 500 + 20, y + 40))
out.save(os.path.join(HIER, "..", "gloop-blad-voor-thijs.png")); print(out.size)
