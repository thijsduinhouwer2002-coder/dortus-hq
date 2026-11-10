# Mila 10 nov run 9: schermafbeeldingen 1920 x 1080 voor de winkelpagina, uit ECHTE opnames van de build.
# Regel van Valve (partner.steamgames.com/doc/store/assets/standard, met curl gelezen 10 nov): schermafbeeldingen tonen
# alleen gameplay, geen marketingtekst of beschrijving. Dus GEEN tekst in beeld; wat klein is en wat groot, zegt het beeld zelf:
#   boven: een stuk van de strook 6x vergroot (hele schaal, nearest: elke spelpixel 18 x 18 scherm-pixels), over de hele breedte;
#   onder: dezelfde opname op ware grootte (1:1) boven een kale taakbalk, met een vergrootkader dat naar het stuk boven wijst.
# Gebruik: python3 maak_schermen.py <opname.png> <x_links_van_het_stuk> <uit.png>
#   opname = een frame van de film (strook 120 px hoog, zoals steam-hol/main/film/los-*.png op de tak schermen).
import sys
from PIL import Image, ImageDraw

W, H = 1920, 1080
NACHT = (0x12, 0x0b, 0x18)
KADER = (0xff, 0xd2, 0x5c)
KADER_D = (0x8a, 0x52, 0x1c)
BALK = (0x1f, 0x19, 0x26)
ICOON = (0x3a, 0x31, 0x45)
Z = 6

def maak(opname, x0, uit):
    s = Image.open(opname).convert("RGB")
    sw, sh = s.size
    # de lucht boven het gras is doorzichtig (klikken gaan erdoor); de opname maakt hem zwart. Hier wordt hij de achtergrond.
    px = s.load()
    for y in range(min(sh, 16)):
        for x in range(sw):
            if px[x, y] == (0, 0, 0): px[x, y] = NACHT
    stuk_w = W // Z                      # 320 scherm-pixels uit de opname
    x0 = max(0, min(sw - stuk_w, x0))
    x0 -= x0 % 3                         # op de spelpixelrand (de strook tekent op schaal 3)
    groot = s.crop((x0, 0, x0 + stuk_w, sh)).resize((W, sh * Z), Image.NEAREST)
    im = Image.new("RGB", (W, H), NACHT)
    d = ImageDraw.Draw(im)
    gy = 40
    im.paste(groot, (0, gy))
    # ware grootte onderaan, gecentreerd, op een kale taakbalk (geen merk, geen iconen van anderen)
    by = H - 56
    d.rectangle((0, by, W, H), fill=BALK)
    for i in range(7):
        cx = W // 2 - 3 * 44 + i * 44
        d.rounded_rectangle((cx - 14, by + 14, cx + 14, by + 42), radius=6, fill=ICOON)
    sx = (W - sw) // 2
    sy = by - sh
    im.paste(s, (sx, sy))
    # vergrootkader: rechthoek om het stuk in de kleine strook, lijnen naar de onderhoeken van het grote beeld
    kx0, kx1 = sx + x0, sx + x0 + stuk_w
    onder = gy + sh * Z
    for (a, b) in (((kx0, sy), (0, onder)), ((kx1, sy), (W - 1, onder))):
        d.line((a, b), fill=KADER_D, width=5)
        d.line((a, b), fill=KADER, width=2)
    d.rectangle((kx0 - 3, sy - 3, kx1 + 2, sy + sh + 2), outline=KADER_D, width=5)
    d.rectangle((kx0 - 2, sy - 2, kx1 + 1, sy + sh + 1), outline=KADER, width=2)
    d.rectangle((0, gy - 4, W - 1, onder + 3), outline=KADER_D, width=4)
    d.rectangle((0, gy - 2, W - 1, onder + 1), outline=KADER, width=2)
    im.save(uit)

if __name__ == "__main__":
    maak(sys.argv[1], int(sys.argv[2]), sys.argv[3])
