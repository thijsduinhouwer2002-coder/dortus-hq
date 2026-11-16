# Mila, 16 nov 2026: concept betaalde wijzerplaat "Gloop's Hat Tower" (bericht hoofdchat 09:55 NL).
# Haak: elke 1.000 stappen krijgt Gloop een hoed op zijn toren; bij je stapdoel komt de kroon bovenop.
# Alles uit de spelkit (ontwerp/garmin/gloop-spel/kit/454), dus hetzelfde figuur als het spel.
import os, json
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HIER, '../gloop-spel/kit')
F = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
def tekst(d, xy, s, maat, kleur, rand=4, anker='mm'):
    f = ImageFont.truetype(F, maat)
    d.text(xy, s, font=f, fill=kleur, anchor=anker, stroke_width=rand, stroke_fill=(24, 10, 4))
def maak(W, maat, stappen, doel, tijd, datum, hart, accu, aod=False):
    k = json.load(open(os.path.join(KIT, 'kit.json')))[maat]; a = k['_ankers']
    im = Image.open(os.path.join(KIT, maat, 'grot-donker.png')).convert('RGBA') if not aod else Image.new('RGBA', (W, W), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    g = Image.open(os.path.join(KIT, maat, 'gloop-blij.png')).convert('RGBA')
    if aod:   # AOD: alleen een donkere silhouet met mint rand, weinig pixels aan
        al = g.split()[3]; g = Image.new('RGBA', g.size, (0, 0, 0, 0)); rand = al.point(lambda v: 255 if v > 128 else 0)
        from PIL import ImageFilter
        r2 = rand.filter(ImageFilter.MaxFilter(5)); ring = Image.composite(Image.new('RGBA', g.size, (60, 200, 160, 255)), g, r2)
        g = Image.composite(Image.new('RGBA', g.size, (0, 0, 0, 255)), ring, rand)
    gx = round(W * 0.64 - g.width / 2); gy = round(W * a['gloop_voet_y_deel_van_scherm']) - g.height
    # toren: een hoed per 1.000 stappen, kroon bij het doel
    n = min(stappen // 1000, 9); y = gy + a['toren_voet'][1]; cx = gx + a['toren_voet'][0]
    volg = [0, 1, 2, 3, 5, 6, 7, 8, 9]
    lagen = []
    for i in range(n):
        h = Image.open(os.path.join(KIT, maat, 'hoed-0%d-%s.png' % (volg[i], ['helm','puntmuts','kap','pet','kroon','koksmuts','emmer','hoge_hoed','pan','veermuts'][volg[i]]))).convert('RGBA')
        lagen.append((h, cx - h.width // 2 + (4 if i % 2 else -4), y - h.height)); y -= round(h.height * a['hoed_stap_deel_van_hoedhoogte'])
    if stappen >= doel:
        h = Image.open(os.path.join(KIT, maat, 'hoed-04-kroon.png')).convert('RGBA'); lagen.append((h, cx - h.width // 2, y - h.height))
    if not aod:
        for h, x, yy in reversed(lagen): pass
        for h, x, yy in lagen[::-1]: im.alpha_composite(h, (x, yy))
    im.alpha_composite(g, (gx, gy))
    if not aod:
        for h, x, yy in lagen: im.alpha_composite(h, (x, yy))   # van onder naar boven, bovenste hoed vooraan
    # tijd groot bovenaan, links van de toren als die hoog is
    tx = W * 0.34
    tekst(d, (tx, W * 0.36), tijd, round(W * 0.17), (255, 255, 255) if not aod else (200, 200, 200), rand=round(W * 0.012))
    if not aod:
        tekst(d, (tx, W * 0.24), datum, round(W * 0.055), (255, 205, 90), rand=3)
        # stappen naast de toren, met het doel als "hoeden"
        tekst(d, (tx, W * 0.49), f"{stappen:,}".replace(',', '.'), round(W * 0.065), (120, 240, 200), rand=3)
        tekst(d, (tx, W * 0.555), f"{min(n, 9) + (1 if stappen >= doel else 0)}/{doel // 1000} HATS", round(W * 0.04), (255, 205, 90), rand=3)
        # hart en accu klein onderaan in de rand
        tekst(d, (W * 0.25, W * 0.68), f"HR {hart}", round(W * 0.045), (255, 120, 120), rand=3)
        tekst(d, (W * 0.25, W * 0.75), f"{accu}%", round(W * 0.045), (230, 230, 230), rand=3)
    m = Image.new('L', (W, W), 0); ImageDraw.Draw(m).ellipse((0, 0, W - 1, W - 1), fill=255)
    uit = Image.new('RGBA', (W, W), (0, 0, 0, 255)); uit.paste(im, (0, 0), m)
    return uit.convert('RGB')
if __name__ == '__main__':
    W = 454
    a = maak(W, '454', 3420, 10000, '10:08', 'MON 16', 62, 81)
    b = maak(W, '454', 7612, 10000, '14:37', 'MON 16', 88, 64)
    c = maak(W, '454', 10230, 10000, '19:52', 'MON 16', 71, 40)
    d = maak(W, '454', 7612, 10000, '14:37', 'MON 16', 88, 64, aod=True)
    B = Image.new('RGB', (W * 4 + 30, W), (40, 40, 40))
    for i, x in enumerate([a, b, c, d]): B.paste(x, (i * (W + 10), 0))
    B.save(os.path.join(HIER, 'concept-454-ochtend-middag-doel-aod.png'))
