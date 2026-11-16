# Mila, 16 nov 2026: kit voor de wijzerplaat "Gloop's Hat Tower", voor Gijs.
# Antwoord op zijn vijf vragen (berichten/mila.md 10:30) en Daans moets (11:00).
# Alles wordt gemaakt uit de spelkit (../gloop-spel/kit/<maat>), dus hetzelfde figuur.
#   <maat>/gloop-dicht.png     knipperframe, oog dicht, zelfde maat en voet als gloop-kijk
#   <maat>/gloop-kijk.png      Gloop met open oog dat omhoog naar zijn toren kijkt (moet 1 Daan)
#   <maat>/achter.png          achtergrond: AMOLED donkere grot met licht op de toren, MIP 5 kleuren met dambord
#   <maat>/uur-0..9.png        cijfers uren (wit), <maat>/min-0..9.png cijfers minuten (mint), stripletter met rand
#   <maat>/gloop-aod.png       (alleen AMOLED) Gloop als mint lijn met oog
#   <maat>/hoed-XX-aod.png     (alleen AMOLED) elke hoed als lijn, voor de bovenste hoed in AOD
#   wijzerplaat.json           per maat: plekken (deel van breedte/hoogte) en de toren-tabel (dx, dy per hoed)
#   proef-*.png                alleen uit deze plaatjes en de tabel samengesteld, zoals Gijs het tekent
import os, json, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HIER = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HIER, '../gloop-spel/kit')
UIT = os.path.join(HIER, 'kit')
F = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'
MATEN = {'208-mip': (208, 208), '240-mip': (240, 240), '260-mip': (260, 260), '280-mip': (280, 280),
         '320': (320, 360), '390': (390, 390), '416': (416, 416), '454': (454, 454)}
HOEDEN = ['helm', 'puntmuts', 'kap', 'pet', 'kroon', 'koksmuts', 'emmer', 'hoge_hoed', 'pan', 'veermuts']
VOLG = [0, 1, 2, 3, 5, 6, 7, 8, 9]          # kroon (4) komt alleen bij het doel
DONKER = (24, 10, 4)
MINT = (120, 240, 200)
GOUD = (255, 205, 90)


def mip(m):
    return m.endswith('-mip')


def hoed(maat, i):
    return Image.open(os.path.join(KIT, maat, 'hoed-%02d-%s.png' % (i, HOEDEN[i]))).convert('RGBA')


def oog(g):
    """Midden en straal van het oogwit. Mila 16 nov 12:10: alleen de grootste samenhangende witte vlek die de
    pupil omsluit, niet alle witte pixels; anders tellen de glans linksboven en het tandje mee en wordt de
    schijf twee keer te groot (fout in de eerste kit: een witte ring over het hele gezicht)."""
    px = g.load(); W, H = g.size
    def is_wit(x, y):
        c = px[x, y]
        return c[3] > 200 and min(c[:3]) > 215 and max(c[:3]) - min(c[:3]) < 25
    gezien = set(); vlekken = []
    for y in range(int(H * 0.7)):
        for x in range(W):
            if (x, y) in gezien or not is_wit(x, y):
                continue
            stapel = [(x, y)]; gezien.add((x, y)); vlek = []
            while stapel:
                a, b = stapel.pop(); vlek.append((a, b))
                for na, nb in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                    if 0 <= na < W and 0 <= nb < int(H * 0.7) and (na, nb) not in gezien and is_wit(na, nb):
                        gezien.add((na, nb)); stapel.append((na, nb))
            vlekken.append(vlek)
    vlek = max(vlekken, key=len)
    xs = [p[0] for p in vlek]; ys = [p[1] for p in vlek]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    return (x0 + x1) / 2, (y0 + y1) / 2, max(x1 - x0, y1 - y0) / 2


# ---------- 1. Gloop kijkt omhoog naar zijn toren ----------
def gloop_kijk(maat):
    g = Image.open(os.path.join(KIT, maat, 'gloop-rust.png')).convert('RGBA')
    px = g.load(); W, H = g.size
    # oogwit: licht en grijs, in de bovenste 70%
    cx, cy, R = oog(g)
    # pupil = alles binnen de schijf dat niet wit is
    pup = Image.new('RGBA', g.size, (0, 0, 0, 0)); pp = pup.load()
    for y in range(H):
        for x in range(W):
            if math.hypot(x - cx, y - cy) < R - 1.2:
                c = px[x, y]
                if not (min(c[:3]) > 215):
                    pp[x, y] = c
                px[x, y] = (250, 250, 250, 255)
    # pupil omhoog en een tikje naar rechts: hij kijkt naar de hoeden op zijn kop
    dx, dy = round(R * 0.12), -round(R * 0.36)
    pup = ImageChops.offset(pup, dx, dy)
    m = Image.new('L', g.size, 0)
    ImageDraw.Draw(m).ellipse((cx - R + 1.5, cy - R + 1.5, cx + R - 1.5, cy + R - 1.5), fill=255)
    pup.putalpha(ImageChops.multiply(pup.split()[3], m))
    g.alpha_composite(pup)
    return g


# ---------- 1b. knipperframe: zelfde Gloop, oog dicht (Gijs 11:25 punt 2) ----------
def gloop_dicht(maat):
    """Zelfde maat en voet als gloop-kijk.png. Het oog wordt een ooglid in lijfkleur met een donkere
    sluitlijn die iets naar beneden buigt (geen lachboogje: dat las op horlogemaat als slapen).
    Alleen voor één knipperframe van ±150 ms."""
    g = Image.open(os.path.join(KIT, maat, 'gloop-rust.png')).convert('RGBA')
    px = g.load(); W, H = g.size
    cx, cy, R = oog(g)
    # lijfkleur net onder het oog
    # naast het oog, niet eronder (daar zit het tandje); gemiddelde van een vlakje, zodat het dambord op MIP mengt
    vak = [px[x, y] for x in range(max(0, int(cx - R - 7)), max(1, int(cx - R - 2))) for y in range(int(cy - 2), int(cy + 3)) if px[x, y][3] > 200]
    lijf = tuple(sum(c[i] for c in vak) // len(vak) for i in range(3)) + (255,)
    lid = tuple(max(0, int(c * 0.86)) for c in lijf[:3]) + (255,)
    d = ImageDraw.Draw(g)
    d.ellipse((cx - R - 0.5, cy - R - 0.5, cx + R + 0.5, cy + R + 0.5), fill=lid)
    dik = max(2, round(R * 0.22))
    d.arc((cx - R * 0.9, cy - R * 0.45, cx + R * 0.9, cy + R * 0.35), 15, 165, fill=DONKER + (255,), width=dik)
    return g


# ---------- 2. Achtergrond ----------
def achter(maat, w, h, gx, gy):
    img = Image.new('RGB', (w, h)); px = img.load()
    if not mip(maat):
        TINT = [(176, 90, 14), (134, 64, 12), (96, 44, 10), (62, 28, 8), (34, 15, 5)]
    else:   # MIP: alleen kleuren uit het 64-kleurenpalet; tussenringen als dambord van 1 px
        # bruin uit oranje en zwart gemengd (dambord 50% en 25%), geen rood: zo blijft het het warme hol
        A, C = (170, 85, 0), (0, 0, 0)
        TINT = [A, (A, C, A, A), (A, C, C, A), (A, C, C, C), C]
    rmax = math.hypot(w * 0.75, h * 0.85)
    for y in range(h):
        for x in range(w):
            r = math.hypot(x - gx, (y - gy) * 1.05) / rmax
            k = min(4, int(min(1, max(0, (r - 0.10) / 0.80)) * 5))
            t = TINT[k]
            if isinstance(t[0], tuple):   # 2x2-patroon: plek 0..3
                t = t[(x % 2) + 2 * (y % 2) if len(t) == 4 else (x + y) % 2]
            px[x, y] = t
    # spotlicht van rechtsboven op de toren: de toren staat op een podium
    ax, bx, by = gx + w * 0.10, gx, gy
    rb, ro = w * 0.06, w * 0.17
    vlak = [(ax - rb, -2), (ax + rb, -2), (bx + ro, by), (bx - ro, by)]
    msk = Image.new('L', (w, h), 0); ImageDraw.Draw(msk).polygon(vlak, fill=255)
    if not mip(maat):
        licht = Image.blend(img, Image.new('RGB', (w, h), (255, 184, 96)), 0.22)
        img = Image.composite(licht, img, msk)
    else:
        mp = msk.load(); px = img.load()
        for y in range(h):
            for x in range(w):
                if mp[x, y] and (x + y) % 2 == 0:
                    c = px[x, y]
                    px[x, y] = (255, 170, 85) if c == (170, 85, 0) else (170, 85, 0) if c == (0, 0, 0) and y > h * 0.25 else c
    # vloer onder Gloop
    msk = Image.new('L', (w, h), 0)
    ew, eh = int(w * 0.62), int(h * 0.13)
    ImageDraw.Draw(msk).ellipse((gx - ew, h - eh, gx + ew, h + eh), fill=255)
    img = Image.composite(Image.new('RGB', (w, h), (74, 10, 4) if not mip(maat) else (85, 0, 0)), img, msk)
    n = len(img.getcolors(1 << 16))
    return img.quantize(colors=min(n, 16 if not mip(maat) else 8), method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


# ---------- 3. Cijfers ----------
def cijfers(maat, w, hoogte, kleur, prefix):
    f = ImageFont.truetype(F, hoogte)
    rand = max(2, round(w * 0.011)); schaduw = max(1, round(w * 0.008))
    # alle cijfers even breed (tabelcijfers), zodat de tijd niet verspringt
    bw = max(f.getbbox(str(c))[2] - f.getbbox(str(c))[0] for c in range(10)) + 2 * rand
    top = min(f.getbbox(str(c))[1] for c in range(10)); bot = max(f.getbbox(str(c))[3] for c in range(10))
    bh = bot - top + 2 * rand + schaduw
    for c in range(10):
        im = Image.new('RGBA', (bw, bh), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        b = f.getbbox(str(c)); x = (bw - (b[2] - b[0])) / 2 - b[0]; y = rand - top
        d.text((x, y + schaduw), str(c), font=f, fill=DONKER, stroke_width=rand, stroke_fill=DONKER)
        d.text((x, y), str(c), font=f, fill=kleur, stroke_width=rand, stroke_fill=DONKER)
        if mip(maat):   # harde randen: geen halve pixels die op MIP vlekken
            a = im.split()[3].point(lambda v: 255 if v > 110 else 0); im.putalpha(a)
            im = Image.composite(im, Image.new('RGBA', im.size, (0, 0, 0, 0)), a)
        im.save(os.path.join(UIT, maat, '%s-%d.png' % (prefix, c)), optimize=True)
    return bw, bh


# ---------- 4. AOD-lijnen ----------
def lijn(im, kleur, dik):
    # rondom dik px groter, zodat de lijn bovenaan niet tegen de rand van het plaatje wegvalt
    p = Image.new('RGBA', (im.width + 2 * dik, im.height + 2 * dik), (0, 0, 0, 0)); p.alpha_composite(im, (dik, dik)); im = p
    a = im.split()[3].point(lambda v: 255 if v > 128 else 0)
    buiten = a.filter(ImageFilter.MaxFilter(dik * 2 + 1))
    ring = ImageChops.subtract(buiten, a)
    out = Image.new('RGBA', (im.width + 0, im.height), (0, 0, 0, 0))
    out.paste(Image.new('RGBA', im.size, (0, 0, 0, 255)), (0, 0), a)
    out.paste(Image.new('RGBA', im.size, kleur + (255,)), (0, 0), ring)
    return out


def gloop_aod(g, w):
    dik = max(2, round(w * 0.005))
    out = lijn(g, MINT, dik)
    # oog: grijze ring en grijze pupil uit de kijk-Gloop, zodat het geen wolk is
    p = Image.new('RGBA', (g.width + 2 * dik, g.height + 2 * dik), (0, 0, 0, 0)); p.alpha_composite(g, (dik, dik)); g = p
    px = g.load(); W, H = g.size; d = ImageDraw.Draw(out)
    cx, cy, R = oog(g)   # Mila 16 nov 12:10: zelfde vlekzoeker als kijk, de glans telde mee
    d.ellipse((cx - R, cy - R, cx + R, cy + R), outline=(200, 200, 200, 255), width=dik)
    pz = [(x, y) for y in range(H) for x in range(W) if px[x, y][3] > 200 and max(px[x, y][:3]) < 90 and math.hypot(x - cx, y - cy) < R]
    if pz:
        qx = sum(p[0] for p in pz) / len(pz); qy = sum(p[1] for p in pz) / len(pz); r = R * 0.42
        d.ellipse((qx - r, qy - r, qx + r, qy + r), fill=(200, 200, 200, 255))
    # Mila 16 nov 13:00: de mond als roze lijn, zodat Gloop ook in de slaapstand grijnst (zonder mond las hij als bom)
    mond = Image.new('L', (W, H), 0); mp = mond.load()
    for y in range(int(cy + R * 0.9), H):
        for x in range(W):
            c = px[x, y]
            if c[3] > 200 and (max(c[:3]) < 110 or (c[0] > 200 and c[1] < 150)) and abs(x - cx) < R * 1.0:
                mp[x, y] = 255
    mond = mond.filter(ImageFilter.MedianFilter(3))
    bb = mond.getbbox()
    if bb:   # als lach getekend (bovenkant recht, onderkant rond), niet als vlek: dat leest op 1x als grijns
        mx0, my0, mx1, my1 = bb; mh = max(my1 - my0, dik * 3)
        d.chord((mx0, my0 - mh, mx1, my0 + mh), 0, 180, outline=(255, 130, 160, 255), width=dik)
    return out


# ---------- 5. Toren-tabel ----------
def toren(maat, n_max=24):
    """dx per plek in de toren (van onder naar boven): verschuiving van het MIDDEN van de hoed t.o.v. het torenvoetpunt.
    Tot 6 hoeden recht met een wiebel; vanaf de 7e buigt hij naar rechtsboven, naar de rand.
    De hoogte rekent Gijs zoals in het spel: y -= hoedhoogte * hoed_stap_deel_van_hoedhoogte."""
    w = MATEN[maat][0]; wieb = max(2, round(w * 0.009))
    return [(wieb if i % 2 else -wieb) + (0 if i < 6 else round(w * 0.012 * (i - 5) ** 1.35)) for i in range(n_max)]


def hoedvolgorde(n, doel):
    """welke hoed op plek i: tot het doel de vaste volgorde; bij het doel de kroon bovenop;
    daarna komen nieuwe hoeden ONDER de kroon en schuift de kroon de rand uit (de grap)."""
    if n < doel:
        return [VOLG[i % len(VOLG)] for i in range(n)]
    extra = n - doel
    return [VOLG[i % len(VOLG)] for i in range(doel - 1 + extra)] + [4]


# ---------- proef ----------
def proef(maat, L, stappen, doel=10000, uur='10', minu='23', datum='MON 16', aod=False):
    w, h = MATEN[maat]; d0 = os.path.join(UIT, maat)
    im = (Image.open(os.path.join(d0, 'achter.png')).convert('RGBA') if not aod
          else Image.new('RGBA', (w, h), (0, 0, 0, 255)))
    g = Image.open(os.path.join(d0, 'gloop-aod.png' if aod else 'gloop-kijk.png')).convert('RGBA')
    gx = round(w * L['gloop_midden_x'] - g.width / 2); gy = round(h * L['gloop_voet_y']) - g.height
    tv = L['toren_voet_in_gloop']; vx, vy = gx + tv[0], gy + tv[1]
    n = stappen // 1000; nd = doel // 1000
    volg = hoedvolgorde(n, nd)
    T = L['toren']; stap = L['hoed_stap']
    lagen = []; y = vy
    for i, hi in enumerate(volg):
        hh = hoed(maat, hi)
        lagen.append((hh, vx + T[min(i, len(T) - 1)] - hh.width // 2, y - hh.height))
        y -= round(hh.height * stap)
    if aod:
        if volg:   # AOD: alleen de bovenste hoed, direct op zijn hoofd
            ha = Image.open(os.path.join(d0, 'hoed-%02d-%s-aod.png' % (volg[-1], HOEDEN[volg[-1]]))).convert('RGBA')
            im.alpha_composite(ha, (vx - ha.width // 2, vy - ha.height + L['aod_rand']))
        im.alpha_composite(g, (gx - L['aod_rand'], gy - L['aod_rand']))
    else:
        im.alpha_composite(g, (gx, gy))
        for hh, x, y in lagen:
            im.alpha_composite(hh, (x, y))
    # tijd: uren boven minuten, groot, links
    def zet(prefix, s, xr, yt):
        cs = [Image.open(os.path.join(d0, '%s-%s.png' % (prefix, c))).convert('RGBA') for c in s]
        if aod:
            cs = [Image.composite(Image.new('RGBA', c.size, (170, 170, 170, 255)), Image.new('RGBA', c.size, (0, 0, 0, 0)),
                                  c.split()[3].point(lambda v: 255 if v > 128 else 0)) for c in cs]
        x = round(xr - sum(c.width for c in cs) + (len(cs) - 1) * L['cijfer_overlap'])
        for c in cs:
            im.alpha_composite(c, (x, round(yt))); x += c.width - L['cijfer_overlap']
        return x
    zet('uur', uur, w * L['tijd_rechts_x'], h * L['uur_boven_y'])
    zet('min', minu, w * L['tijd_rechts_x'], h * L['min_boven_y'])
    dr = ImageDraw.Draw(im)
    def tekst(xy, s, maat_, kleur, anker='rm'):
        f = ImageFont.truetype(F, maat_)
        dr.text(xy, s, font=f, fill=kleur, anchor=anker, stroke_width=max(2, round(w * 0.007)), stroke_fill=DONKER)
    if not aod:
        tekst((w * L['tijd_rechts_x'], h * L['datum_y']), datum, round(w * 0.056), GOUD)
        regel = ('%d/%d HATS' % (n, nd)) if n < nd else ('GOAL!' if n == nd else 'GOAL! +%d' % (n - nd))
        tekst((w * L['tijd_rechts_x'], h * L['stappen_y']), f"{stappen:,}".replace(',', '.'), round(w * 0.062), MINT)
        tekst((w * L['tijd_rechts_x'], h * L['regel_y']), regel, round(w * 0.045), GOUD)
        # vrij veld (koper kiest: hartslag, batterij, ...): hier hartslag met een getekend hartje
        hx, hy, r = w * 0.45, h * L['veld_y'], max(3, round(w * 0.014))
        dr.ellipse((hx - 2 * r, hy - r, hx, hy + r * 0.3), fill=(255, 90, 90)); dr.ellipse((hx - r * 0.2, hy - r, hx + r * 1.8, hy + r * 0.3), fill=(255, 90, 90))
        dr.polygon([(hx - 2 * r, hy - r * 0.1), (hx + r * 1.8, hy - r * 0.1), (hx - r * 0.1, hy + r * 1.7)], fill=(255, 90, 90))
        tekst((hx + r * 2.6, hy), '64', round(w * 0.05), (255, 140, 140), anker='lm')
    if w == h:
        m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).ellipse((0, 0, w - 1, h - 1), fill=255)
        uit = Image.new('RGBA', (w, h), (0, 0, 0, 255)); uit.paste(im, (0, 0), m); im = uit
    return im.convert('RGB'), lagen


def indeling(maat, w, h, ch_u):
    rond = w == h
    L = {
        'gloop_midden_x': 0.66, 'gloop_voet_y': 0.93 if rond else 0.95,
        'tijd_rechts_x': 0.50,
        'datum_y': 0.215 if rond else 0.17,
        'uur_boven_y': 0.25 if rond else 0.20,
        'stappen_y': 0.0, 'regel_y': 0.0, 'veld_y': 0.90 if rond else 0.93,
    }
    L['min_boven_y'] = L['uur_boven_y'] + ch_u / h * 0.86
    eind = L['min_boven_y'] + ch_u / h
    L['stappen_y'] = eind + 0.045
    L['regel_y'] = eind + 0.105
    return L


if __name__ == '__main__':
    alles = {}
    for maat, (w, h) in MATEN.items():
        os.makedirs(os.path.join(UIT, maat), exist_ok=True)
        g = gloop_kijk(maat); g.save(os.path.join(UIT, maat, 'gloop-kijk.png'), optimize=True)
        gloop_dicht(maat).save(os.path.join(UIT, maat, 'gloop-dicht.png'), optimize=True)
        ch = round(w * 0.215)
        bw, bh = cijfers(maat, w, ch, (255, 255, 255), 'uur')
        cijfers(maat, w, ch, MINT, 'min')
        L = indeling(maat, w, h, bh)
        L['aod_rand'] = max(2, round(w * 0.005))   # -aod.png plaatjes zijn rondom zoveel px groter: teken ze zoveel naar linksboven
        L['cijfer_overlap'] = max(1, round(w * 0.012))
        L['cijfer_maat'] = [bw, bh]
        a = json.load(open(os.path.join(KIT, 'kit.json')))[maat]['_ankers']
        L['toren_voet_in_gloop'] = a['toren_voet']
        L['toren'] = toren(maat)
        L['hoed_stap'] = 0.46   # dichter op elkaar dan in het spel, zodat de kroon bij 10 hoeden net binnen het scherm staat
        gx = w * L['gloop_midden_x']; gy = h * L['gloop_voet_y'] - g.height * 0.5
        achter(maat, w, h, gx, gy).save(os.path.join(UIT, maat, 'achter.png'), optimize=True)
        if not mip(maat):
            gloop_aod(g, w).save(os.path.join(UIT, maat, 'gloop-aod.png'), optimize=True)
            for i in range(10):
                lijn(hoed(maat, i), GOUD, max(2, round(w * 0.004))).save(os.path.join(UIT, maat, 'hoed-%02d-%s-aod.png' % (i, HOEDEN[i])), optimize=True)
        alles[maat] = L
    json.dump(alles, open(os.path.join(UIT, 'wijzerplaat.json'), 'w'), indent=1)
