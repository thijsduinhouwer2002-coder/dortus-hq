# Reeks datawijzerplaten, stijlproef 1 (Mila, 16 nov 2026). Richting "Koers": elk veld heeft een kompasnaaldje
# dat wijst waar het getal heen gaat (plat = rechts, stijgt = schuin omhoog, zakt = schuin omlaag).
# Letter: Big Shoulders Display (OFL), zwaar en smal, zodat de tijd groot kan. Nep-gegevens, alleen om de stijl te zien.
#   python3 stijl_proef_v1.py
import math, os
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
LET = os.path.join(HIER, 'BigShouldersDisplay.ttf')

def f(s, w=900):
    ft = ImageFont.truetype(LET, s)
    try: ft.set_variation_by_axes([w])
    except Exception: pass
    return ft

THEMAS = {  # naam: (achtergrond, uren, minuten, tekst, zwak, stijgt, zakt)
    'Ember': ((0, 0, 0), (255, 238, 214), (255, 150, 40), (255, 226, 190), (120, 84, 60), (120, 230, 170), (255, 110, 90)),
    'Tide':  ((0, 0, 0), (225, 248, 255), (40, 210, 220), (200, 236, 245), (60, 100, 120), (120, 230, 170), (255, 120, 110)),
    'Moss':  ((0, 0, 0), (236, 244, 220), (170, 220, 60), (220, 232, 200), (90, 110, 70), (170, 220, 60), (255, 140, 80)),
    'Chalk': ((0, 0, 0), (255, 255, 255), (255, 255, 255), (230, 230, 230), (100, 100, 100), (255, 255, 255), (255, 255, 255)),
}
VELDEN = [('BODY BATT', '72', -35), ('STRESS', '24', 25), ('REST HR', '52', -10), ('STEPS', '8.4K', 50)]

def naald(d, cx, cy, r, hoek, kleur, zwak):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=zwak, width=max(1, r // 6))
    a = math.radians(hoek)
    tip = (cx + r * 0.95 * math.cos(a), cy - r * 0.95 * math.sin(a))
    staart = (cx - r * 0.55 * math.cos(a), cy + r * 0.55 * math.sin(a))
    zij = r * 0.32
    l = (cx + zij * math.cos(a + math.pi / 2), cy - zij * math.sin(a + math.pi / 2))
    rr = (cx + zij * math.cos(a - math.pi / 2), cy - zij * math.sin(a - math.pi / 2))
    d.polygon([tip, l, staart, rr], fill=kleur)

def plaat(S, thema):
    bg, uur, mn, tekst, zwak, op, neer = THEMAS[thema]
    im = Image.new('RGB', (S, S), bg); d = ImageDraw.Draw(im); c = S / 2
    # minutenstreepjes op de rand, elke 5 minuten iets langer
    for i in range(60):
        a = math.radians(90 - i * 6); r1 = c - S * 0.012; r2 = r1 - (S * 0.035 if i % 5 == 0 else S * 0.015)
        d.line([(c + r1 * math.cos(a), c - r1 * math.sin(a)), (c + r2 * math.cos(a), c - r2 * math.sin(a))], fill=mn if i == 0 else zwak, width=max(1, S // 150))
    d.text((c, S * 0.17), 'MON 16', font=f(int(S * 0.07), 700), fill=tekst, anchor='mm')
    ft = f(int(S * 0.36)); uw = d.textlength('7', font=ft); gw = d.textlength('7:42', font=ft)
    x = c - gw / 2; y = S * 0.40
    d.text((x, y), '7', font=ft, fill=uur, anchor='lm'); x += uw
    d.text((x, y), ':', font=ft, fill=zwak, anchor='lm'); x += d.textlength(':', font=ft)
    d.text((x, y), '42', font=ft, fill=mn, anchor='lm')
    # vier velden, 2 x 2
    for k, (lab, val, hoek) in enumerate(VELDEN):
        gx = c + (-1 if k % 2 == 0 else 1) * S * 0.20; gy = S * (0.63 if k < 2 else 0.79)
        r = int(S * 0.032); kleur = op if hoek > 8 else neer if hoek < -8 else tekst
        naald(d, gx - S * 0.10, gy, r, hoek, kleur, zwak)
        d.text((gx - S * 0.055, gy + S * 0.005), val, font=f(int(S * 0.095), 800), fill=tekst, anchor='lm')
        d.text((gx - S * 0.055, gy - S * 0.052), lab, font=f(int(S * 0.036), 600), fill=zwak, anchor='lm')
    m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new('RGB', (S, S), (40, 40, 40)); out.paste(im, (0, 0), m)
    return out

if __name__ == '__main__':
    rij = [plaat(454, t) for t in THEMAS]
    mip = plaat(260, 'Ember')
    W = 454 * 4 + 50 + 300
    blad = Image.new('RGB', (W, 520), (30, 30, 30)); d = ImageDraw.Draw(blad)
    for k, (t, p) in enumerate(zip(THEMAS, rij)):
        blad.paste(p, (10 + k * 464, 10)); d.text((10 + k * 464 + 227, 490), t + ' (AMOLED 454)', font=f(26, 600), fill=(220, 220, 220), anchor='mm')
    blad.paste(mip, (W - 280, 107)); d.text((W - 150, 490), 'Ember (MIP 260, 1x)', font=f(26, 600), fill=(220, 220, 220), anchor='mm')
    blad.save(os.path.join(HIER, 'stijlproef-v1-koers.png')); print('klaar')
