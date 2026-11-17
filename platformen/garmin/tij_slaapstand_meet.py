# Meet hoeveel van het scherm aan staat in de slaapstand van Tij (regel Garmin: onder 10%).
import sys, math
from PIL import Image, ImageDraw, ImageFont
LET = sys.argv[1]
def font(s, w):
    ft = ImageFont.truetype(LET, int(s))
    try: ft.set_variation_by_axes([w])
    except Exception as e: print('geen as', e)
    return ft
def meet(S, tijdpx, w, grijs, omtrek=0, tekst='00:00'):
    im = Image.new('L', (S, S), 0); d = ImageDraw.Draw(im)
    ft = font(tijdpx, w)
    if omtrek:
        d.text((S/2, 0.30*S), tekst, font=ft, fill=0, anchor='mm', stroke_width=omtrek, stroke_fill=grijs)
    else:
        d.text((S/2, 0.30*S), tekst, font=ft, fill=grijs, anchor='mm')
    # waterlijn 2 px over de breedte en bootje als omtrek (ruwe schatting: driehoek en romp)
    y = int(0.75*S); d.line([(0.04*S, y), (0.96*S, y)], fill=grijs, width=2)
    x = 0.70*S; hb = 0.05*S; m = 0.075*S
    d.line([(x-hb, y-2), (x+hb, y-2), (x+hb*0.7, y+0.02*S), (x-hb*0.7, y+0.02*S), (x-hb, y-2)], fill=grijs, width=2)
    d.line([(x, y-2), (x, y-m), (x+hb, y-6), (x, y-6)], fill=grijs, width=2)
    px = im.load(); aan = 0; licht = 0; n = 0; r = S/2
    for yy in range(S):
        for xx in range(S):
            if (xx-r+0.5)**2 + (yy-r+0.5)**2 <= r*r:
                n += 1; v = px[xx, yy]
                if v > 0: aan += 1; licht += v/255
    return 100*aan/n, 100*licht/n
tab = {390: 117, 416: 125, 454: 136}
print('S | variant | pixels aan % | licht %')
for S, t in tab.items():
    for naam, w, g, o, tk in [('900 vol wit', 900, 255, 0, '00:00'), ('900 vol grijs 170', 900, 170, 0, '00:00'),
                           ('900 vol grijs 170, 08:08', 900, 170, 0, '08:08'), ('900 omtrek 2 px grijs 170', 900, 170, 2, '00:00'),
                           ('400 vol grijs 170', 400, 170, 0, '00:00'), ('300 vol grijs 170', 300, 170, 0, '00:00'), ('100 vol grijs 170', 100, 170, 0, '00:00')]:
        a, l = meet(S, t, w, g, o, tk)
        print(S, '|', naam, '|', round(a, 1), '|', round(l, 1))
