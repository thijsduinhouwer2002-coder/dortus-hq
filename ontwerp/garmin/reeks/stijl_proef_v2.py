# Reeks datawijzerplaten, stijlproef 2 "Tij" (Mila, 16 nov 2026). Body Battery is de zee onderin de plaat:
# het water staat zo hoog als je batterij, en een bootje dobbert erop. Leeg = bootje op de bodem.
# Nep-gegevens, alleen om de stijl te zien.  python3 stijl_proef_v2.py
import math, os
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
LET = os.path.join(HIER, 'BigShouldersDisplay.ttf')

def f(s, w=900):
    ft = ImageFont.truetype(LET, s)
    try: ft.set_variation_by_axes([w])
    except Exception: pass
    return ft

THEMAS = {  # zee boven, zee onder, uren, minuten, tekst, zwak, boot
    'Dusk':  ((255, 140, 60), (120, 30, 40), (255, 238, 214), (255, 170, 80), (255, 226, 190), (120, 84, 60), (255, 246, 230)),
    'Tide':  ((40, 200, 220), (10, 40, 90), (225, 248, 255), (60, 220, 230), (200, 236, 245), (60, 100, 120), (255, 255, 255)),
    'Kelp':  ((150, 210, 60), (20, 60, 30), (236, 244, 220), (170, 225, 70), (220, 232, 200), (90, 110, 70), (255, 250, 230)),
    'Night': ((90, 110, 255), (20, 10, 60), (240, 240, 255), (150, 160, 255), (220, 220, 245), (90, 90, 130), (255, 220, 120)),
}

def plaat(S, thema, batt=72, t=0.0):
    zb, zo, uur, mn, tekst, zwak, boot = THEMAS[thema]
    im = Image.new('RGB', (S, S), (0, 0, 0)); d = ImageDraw.Draw(im); c = S / 2
    # zee: hoogte = batterij (0 = onderrand, 100 = net onder de tijd)
    top, bodem = S * 0.66, S * 0.97
    niveau = bodem - (bodem - top) * batt / 100
    golf = lambda x: niveau + S * 0.012 * math.sin(x / S * 2 * math.pi * 2.2 + t)
    pts = [(x, golf(x)) for x in range(0, S + 1, 2)]
    zee = Image.new('RGB', (S, S)); zd = ImageDraw.Draw(zee)
    for y in range(S):
        k = max(0, min(1, (y - niveau) / (bodem - niveau + 1)))
        zd.line([(0, y), (S, y)], fill=tuple(int(zb[i] * (1 - k) + zo[i] * k) for i in range(3)))
    m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).polygon(pts + [(S, S), (0, S)], fill=255)
    im.paste(zee, (0, 0), m)
    d.line(pts, fill=tuple(min(255, v + 70) for v in zb), width=max(2, S // 110))
    # bootje op de golf
    bx = c + S * 0.20; by = golf(bx); s = S * 0.05
    hl = math.atan2(golf(bx + 4) - golf(bx - 4), 8)
    def rot(px, py): return (bx + px * math.cos(hl) - py * math.sin(hl), by + px * math.sin(hl) + py * math.cos(hl))
    d.polygon([rot(-s, -s * 0.15), rot(s, -s * 0.15), rot(s * 0.6, s * 0.35), rot(-s * 0.6, s * 0.35)], fill=boot)
    d.line([rot(0, -s * 0.15), rot(0, -s * 1.5)], fill=boot, width=max(2, S // 150))
    d.polygon([rot(s * 0.08, -s * 1.45), rot(s * 0.08, -s * 0.35), rot(s * 0.85, -s * 0.35)], fill=mn)
    # batterij in de zee, met richting
    # genoeg water: getal in de zee; weinig water: getal er net boven, in de zeekleur
    if bodem - niveau > S * 0.17:
        ny, kl = niveau + S * 0.09, (255, 255, 255)
    else:
        ny, kl = niveau - S * 0.10, tuple(min(255, v + 70) for v in zb)
    d.text((c - S * 0.12, ny), f'{batt}', font=f(int(S * 0.11)), fill=kl, anchor='mm')
    d.text((c - S * 0.12, ny + S * 0.072), 'BODY BATT ▲', font=f(int(S * 0.033), 700), fill=kl, anchor='mm')
    # tijd en datum
    d.text((c, S * 0.13), 'MON 16', font=f(int(S * 0.065), 700), fill=tekst, anchor='mm')
    ft = f(int(S * 0.30)); x = c - d.textlength('7:42', font=ft) / 2; y = S * 0.30
    for deel, kl in (('7', uur), (':', zwak), ('42', mn)):
        d.text((x, y), deel, font=ft, fill=kl, anchor='lm'); x += d.textlength(deel, font=ft)
    # drie kleine velden boven de zee
    for k, (lab, val) in enumerate([('HR', '58'), ('STRESS', '24'), ('STEPS', '8.4K')]):
        gx = c + (k - 1) * S * 0.22
        d.text((gx, S * 0.555), val, font=f(int(S * 0.065), 800), fill=tekst, anchor='mm')
        d.text((gx, S * 0.495), lab, font=f(int(S * 0.03), 600), fill=zwak, anchor='mm')
    m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new('RGB', (S, S), (40, 40, 40)); out.paste(im, (0, 0), m)
    return out

if __name__ == '__main__':
    W = 454 * 4 + 50 + 300
    blad = Image.new('RGB', (W, 520), (30, 30, 30)); d = ImageDraw.Draw(blad)
    for k, (t, b) in enumerate(zip(THEMAS, (72, 35, 90, 12))):
        blad.paste(plaat(454, t, b, k), (10 + k * 464, 10)); d.text((10 + k * 464 + 227, 490), f'{t}, batterij {b} (AMOLED 454)', font=f(26, 600), fill=(220, 220, 220), anchor='mm')
    blad.paste(plaat(260, 'Tide', 72), (W - 280, 107)); d.text((W - 150, 490), 'Tide (260, 1x)', font=f(26, 600), fill=(220, 220, 220), anchor='mm')
    blad.save(os.path.join(HIER, 'stijlproef-v2-tij.png')); print('klaar')
