# Nabootsing van Gijs' DierenData.mc (tak claude/garmin-2026-11-10b), zo letterlijk mogelijk:
# gehele getallen zoals Monkey C ((s8 * maat) / 90 kapt af naar nul), fillPolygon, fillCircle, stickerrand in 4 schuine richtingen.
# Zo zie ik de dieren zoals het horloge ze tekent, niet zoals mijn eigen tekenaar ze tekent.
# oog_modus: 'oud' = wit oog met pupil (DierenData.mc nu), 'v83' = mijn voorstel (zie ebb-blad-v8.md, v8.3).
import json
from PIL import Image, ImageDraw

SCHAAL = 90
SIL_VLAK, SIL_RAND = (0, 0, 85), (0, 170, 255)

def hx(s): s = int(s, 16); return ((s >> 16) & 255, (s >> 8) & 255, s & 255)

def idiv(a, b):            # Monkey C: deling van gehele getallen kapt af naar nul
    q = abs(a) // abs(b); return q if (a >= 0) == (b > 0) else -q

def laad(pad):
    d = json.load(open(pad))
    return d['dieren']

def fill_circle(dr, x, y, r, c):
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx*dx + dy*dy <= r*r: dr.point((x + dx, y + dy), fill=c)

def delen(dr, dier, cx, cy, maat, kleur, modus):
    b = dier['bytes']; t = [hx(c) for c in dier['tint']] + [hx(dier['rand'])]
    o = 1
    for _ in range(b[0]):
        rol, n = b[o], b[o + 1]; o += 2
        mee = True
        if modus in (0, 2): mee = rol != 9
        elif modus == 3: mee = rol in (7, 8, 10)
        if not mee: o += 2*n; continue
        pts = []
        for k in range(n):
            pts.append((cx + idiv(b[o]*maat, SCHAAL), cy + idiv(b[o + 1]*maat, SCHAAL))); o += 2
        c = kleur
        if modus == 0:
            if rol < 3: c = t[rol]
            elif rol == 7: c = t[1]
            elif rol == 8: c = t[2]
            elif rol == 3: c = (0, 0, 0)
            elif rol in (4, 10): c = (85, 85, 255)
            else: c = (255, 255, 255)
        if len(pts) >= 3: dr.polygon(pts, fill=c)
    return o

def ogen(dr, dier, o, cx, cy, maat, oog_modus):
    b = dier['bytes']; n = b[o]; o += 1
    for _ in range(n):
        x = cx + idiv(b[o]*maat, SCHAAL); y = cy + idiv(b[o + 1]*maat, SCHAAL); o += 2
        if oog_modus == 'oud':
            r = max(2, 13*maat // 100); p = max(1, 7*maat // 100)
            fill_circle(dr, x, y, r, (255, 255, 255))
            fill_circle(dr, x - r*3 // 10, y, p, (0, 0, 85))
            if maat >= 30:
                g = max(1, (35*maat + 500) // 1000)
                fill_circle(dr, x - r*55 // 100, y - r // 2, g, (255, 255, 255))
        else:   # v8.3: tot maat 60 een zwart vierkantje (2 x 2 op 260, 3 x 3 op 454); vanaf 60 een rond zwart oog met 1 px glimp
            if maat < 60:
                e = max(2, (8*maat + 50) // 100)
                dr.rectangle([x - e // 2, y - e // 2, x - e // 2 + e - 1, y - e // 2 + e - 1], fill=(0, 0, 0))
            else:
                r = max(3, maat // 20)
                fill_circle(dr, x, y, r, (0, 0, 0))
                dr.point((x - 1, y - 1), fill=(255, 255, 255))

def teken(dr, dier, cx, cy, maat, oog_modus='v83'):
    k = 3 if maat >= 60 else 2
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        delen(dr, dier, cx + dx*k, cy + dy*k, maat, hx(dier['rand']), 2)
    o = delen(dr, dier, cx, cy, maat, None, 0)
    ogen(dr, dier, o, cx, cy, maat, oog_modus)

def silhouet(dr, dier, cx, cy, maat):
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        delen(dr, dier, cx + dx*2, cy + dy*2, maat, SIL_RAND, 1)
    delen(dr, dier, cx, cy, maat, SIL_VLAK, 1)
    delen(dr, dier, cx, cy, maat, SIL_RAND, 3)

def raster(dieren, maat, oog_modus='v83', stap=None, kolommen=5, achter=(0, 0, 0)):
    """Alle dieren gevonden (boven) en als silhouet (eronder), op de maat van het horloge."""
    stap = stap or int(maat*2.6)
    rijen = (len(dieren) + kolommen - 1) // kolommen
    im = Image.new('RGB', (kolommen*stap, rijen*2*stap), achter); dr = ImageDraw.Draw(im)
    for i, d in enumerate(dieren):
        cx = (i % kolommen)*stap + stap // 2; cy = (i // kolommen)*2*stap + stap // 2
        teken(dr, d, cx, cy, maat, oog_modus)
        silhouet(dr, d, cx, cy + stap, maat)
    return im
