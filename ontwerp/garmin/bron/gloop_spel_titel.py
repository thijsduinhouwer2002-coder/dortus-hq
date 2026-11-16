# Gloop: Hat Tower, titelplaatje voor het startscherm (Mila, 16 nov 2026), op vraag van Gijs:
# het systeemfont van "GLOOP" is op AMOLED dun. Lilita One zoals Het Hol, mint als Gloop, donkere stripletterrand,
# de kroon uit het spel scheef op de eerste O. Per kitmaat een titel.png; MIP in de 64 kleuren met harde rand.
#   python3 gloop_spel_titel.py <kitmap>
import sys, os, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
KIT = sys.argv[1]
HIER = os.path.dirname(os.path.abspath(__file__))
LET = os.path.join(HIER, '..', '..', 'steam', 'capsule-3d', 'LilitaOne-Regular.ttf')
MINT, MINT_D, GEEL, RAND = (130, 255, 205), (40, 190, 140), (255, 214, 64), (20, 8, 2)
BREED = 0.48   # deel van de schermbreedte; bovenkant op 0,08 x de hoogte, midden, dan blijft de GULP-boog rechts vrij


def titel(W, M):
    S = 4; tw = int(W * BREED) * S
    big = ImageFont.truetype(LET, 200)
    d0 = ImageDraw.Draw(Image.new('L', (10, 10)))
    w1 = d0.textlength('GLOOP', font=big); m1 = int(200 * tw / w1)
    f1 = ImageFont.truetype(LET, m1); f2 = ImageFont.truetype(LET, int(m1 * 0.42))
    w2 = d0.textlength('HAT TOWER', font=f2)
    st = max(2, m1 // 11)
    kroon_h = int(m1 * 0.42)
    H = kroon_h + int(m1 * 1.02) + int(m1 * 0.50) + 2 * st
    im = Image.new('RGBA', (tw + 4 * st, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x1 = (im.width - w1 * m1 / 200) / 2; y1 = kroon_h - int(m1 * 0.12)
    # tweekleurig mint: licht boven, donkerder onder (zoals Gloops glans), via masker
    tm = Image.new('L', im.size, 0); ImageDraw.Draw(tm).text((x1, y1), 'GLOOP', font=f1, fill=255)
    d.text((x1, y1), 'GLOOP', font=f1, fill=RAND, stroke_width=st, stroke_fill=RAND)
    verloop = Image.new('RGBA', im.size)
    top, bot = y1 + m1 * 0.25, y1 + m1 * 0.95
    for y in range(im.height):
        t = min(1, max(0, (y - top) / (bot - top)))
        ImageDraw.Draw(verloop).line([(0, y), (im.width, y)], fill=tuple(int(MINT[i] * (1 - t) + MINT_D[i] * t) for i in range(3)) + (255,))
    im.paste(verloop, (0, 0), tm)
    y2 = y1 + int(m1 * 1.0)
    d.text(((im.width - w2) / 2, y2), 'HAT TOWER', font=f2, fill=GEEL, stroke_width=max(2, st * 2 // 3), stroke_fill=RAND)
    # kroon uit de kit scheef op de eerste O
    kr = Image.open(os.path.join(KIT, '454', 'hoed-04-kroon.png')).convert('RGBA')
    kw = int(m1 * 0.62); kr = kr.resize((kw, int(kr.height * kw / kr.width)), Image.LANCZOS)
    rand = kr.getchannel('A').point(lambda v: 255 if v > 60 else 0).filter(ImageFilter.MaxFilter(2 * (st // 2) + 1))
    kk = Image.new('RGBA', kr.size, RAND + (0,)); kk.putalpha(rand); kk.alpha_composite(kr)
    kk = kk.rotate(18, expand=True, resample=Image.BICUBIC)
    ox = x1 + d0.textlength('GL', font=f1) + d0.textlength('O', font=f1) * 0.5
    im.alpha_composite(kk, (int(ox - kk.width * 0.55), int(y1 + m1 * 0.22 - kk.height * 0.92)))
    im = im.crop(im.getbbox())
    im = im.resize((im.width // S, im.height // S), Image.LANCZOS)
    if M:   # 64 kleuren, harde rand
        a = im.getchannel('A').point(lambda v: 255 if v >= 128 else 0)
        plat = Image.new('RGBA', im.size, RAND + (255,)); plat.alpha_composite(im)
        kl = plat.convert('RGB').point(lambda v: round(v / 85) * 85).convert('RGBA'); kl.putalpha(a)
        im = kl
    return im


if __name__ == '__main__':
    info = json.load(open(os.path.join(KIT, 'kit.json')))
    for naam in sorted(os.listdir(KIT)):
        p = os.path.join(KIT, naam)
        if not os.path.isdir(p): continue
        W = int(naam.split('-')[0]); M = naam.endswith('-mip')
        t = titel(W, M); t.save(os.path.join(p, 'titel.png'))
        info.setdefault(naam, {})['titel'] = [t.width, t.height]
        info[naam].setdefault('_ankers', {})['titel_boven_y_deel_van_scherm'] = 0.08
        print(naam, t.size)
    json.dump(info, open(os.path.join(KIT, 'kit.json'), 'w'), indent=1)
