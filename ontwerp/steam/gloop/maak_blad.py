# Werkblad Gloop (Daan): elke versie op ware grootte (schaal 3) en 8x vergroot, met hoedentoren uit de echte held_hoeden.png.
import os, sys
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
KUNST = os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "godot", "kunst")
sys.path.insert(0, HIER)
import maak_gloop as mg

BG = (63, 40, 70); BG2 = (29, 20, 38); TXT = (240, 230, 214)

def hoeden():
    sheet = Image.open(os.path.join(KUNST, "held_hoeden.png")).convert("RGBA")
    uit = []
    for i in range(sheet.width // 16):
        h = sheet.crop((i * 16, 0, i * 16 + 16, 16)); bb = h.getbbox()
        uit.append(h.crop(bb) if bb else None)
    return uit

def met_toren(gloop, hats, n):
    """Gloop met n hoeden gestapeld, om en om scheef, 1 px in de vorige gezakt."""
    bb = gloop.getbbox(); top = bb[1]
    hoogte = sum(hats[i].height - 1 for i in range(n))
    im = Image.new("RGBA", (gloop.width + 6, gloop.height + hoogte + 2), (0, 0, 0, 0))
    gy = im.height - gloop.height; im.paste(gloop, (3, gy), gloop)
    # ronde 2: de onderste hoed zakt 1 px over het hoofd, elke volgende 2 px in de vorige, recht boven elkaar (kijkers: "zweeft los")
    y = gy + top + 1; mid = 3 + gloop.width // 2
    for k in range(n):
        h = hats[k]; y -= h.height - (2 if k == 0 else 0)  # op het hoofd 2 px gezakt, op elkaar rakend zodat de kroonpunten te zien blijven
        dx = [0, 0, 1, 0][k % 4]
        im.paste(h, (mid - h.width // 2 + dx, y), h)
    return im

def blad():
    hats = hoeden(); keuze = [hats[4], hats[5], hats[1]]  # kroon, koksmuts, puntmuts (punt bovenaan) (helm en hoge hoed lazen als "pot" of "emmer")
    font = ImageFont.load_default()
    kol = []
    for v, naam in (("A", "A druppel"), ("B", "B groot"), ("C", "C gelei")):
        s = Image.open(os.path.join(HIER, f"gloop_{v}.png"))
        fw = s.width // 6; fh = s.height; rust = s.crop((0, 0, fw, fh)); hap = s.crop((4 * fw, 0, 5 * fw, fh)); kauw = s.crop((5 * fw, 0, 6 * fw, fh))
        toren = met_toren(rust, [mg.hoed_beeld("kroon"), mg.hoed_beeld("puntmuts")], 2) if v == "B" else met_toren(rust, keuze, 3)
        kol.append((naam, [rust, hap, kauw, toren]))
    W = 1500; H = 900
    out = Image.new("RGB", (W, H), BG2); d = ImageDraw.Draw(out)
    for i, (naam, beelden) in enumerate(kol):
        x0 = 20 + i * 490
        d.rectangle((x0, 20, x0 + 470, 880), fill=BG)
        d.text((x0 + 10, 28), naam + "   (boven: ware grootte x3, onder: x8)", fill=TXT, font=font)
        x = x0 + 14
        for b in beelden:
            g = b.resize((b.width * 3, b.height * 3), Image.NEAREST); out.paste(g, (x, 150 - g.height), g); x += g.width + 12
        x = x0 + 10; y = 180
        for j, b in enumerate(beelden):
            g = b.resize((b.width * 8, b.height * 8), Image.NEAREST)
            px = x0 + 10 + (j % 2) * 230; py = 180 + (j // 2) * 340 + (300 - g.height)
            out.paste(g, (px, py), g)
    out.save(os.path.join(HIER, "werkblad.png"))

if __name__ == "__main__":
    blad(); print("ok")
