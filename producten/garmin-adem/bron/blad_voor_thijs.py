# Eén blad voor Thijs (nummer 6 van besluit 12 nov 11:50): alle schermen van drie dieren (krab, schildpad en één dier
# in de basiswereld) op fenix 8 47 mm en Forerunner 255, dag en nacht, plus start, pauze, sea log en Today.
# Alleen echte schermafbeeldingen uit de plaatjesrun (map namen/), uitgesneden op het ronde scherm; er wordt niets
# bijgetekend. Een beeld dat ontbreekt krijgt een grijs vak met zijn naam, zodat je ziet wat er nog niet is.
#   python3 bron/blad_voor_thijs.py <map met de beelden op naam> <uit.png>
import sys, os
from PIL import Image, ImageDraw, ImageFont
m, uit = sys.argv[1], sys.argv[2]
# Uitsnede van het scherm in de bijgesneden simulatorfoto (gemeten door Wout, werelden-stand.md).
HORLOGES = [('fenix847mm', 'fenix 8, 47 mm (AMOLED)', (152, 233, 572, 653)), ('fr255', 'Forerunner 255 (MIP)', (83, 155, 363, 435))]
DIEREN = [('krab', 'Crab, with his swim ring'), ('schild', 'Turtle, with the gull'), ('basis', 'Dolphin, the shared sea')]
SESSIE = [('in-dag', 'breathe in, day'), ('uit-dag', 'breathe out, day'), ('hold-dag', 'hold, day'),
          ('in-nacht', 'breathe in, night'), ('uit-nacht', 'breathe out, night'), ('hold-nacht', 'hold, night')]
REST = [('thuis-start-dag', 'start, day'), ('thuis-start-nacht', 'start, night'), ('pauze', 'pause'), ('sealog-1', 'sea log'),
        ('today', 'Today'), ('einde-6c-krab', 'end of a session')]
C, GAT, KOP = 300, 14, 26
def letter(maat):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/dejavu/DejaVuSans.ttf']:
        if os.path.exists(p):
            return ImageFont.truetype(p, maat)
    return ImageFont.load_default()
F, FG = letter(15), letter(22)
rijen = []
for d, dnaam in DIEREN:
    for h, hnaam, vak in HORLOGES:
        rijen.append((dnaam + '  ·  ' + hnaam, [('sessie-%s-%s-%s.png' % (d, s, h), t, vak) for s, t in SESSIE]))
for h, hnaam, vak in HORLOGES:
    rijen.append(('Other screens  ·  ' + hnaam, [('%s-%s.png' % (n, h), t, vak) for n, t in REST]))
W = GAT + 6 * (C + GAT)
H = GAT + len(rijen) * (KOP + 8 + C + 22 + GAT)
blad = Image.new('RGB', (W, H), (16, 20, 40))
dr = ImageDraw.Draw(blad)
mis = 0
y = GAT
for kop, cellen in rijen:
    dr.text((GAT, y), kop, fill=(255, 255, 255), font=FG)
    y += KOP + 8
    for i, (naam, t, vak) in enumerate(cellen):
        x = GAT + i * (C + GAT)
        p = os.path.join(m, naam)
        if os.path.exists(p):
            im = Image.open(p).convert('RGB').crop(vak).resize((C, C), Image.LANCZOS)
            blad.paste(im, (x, y))
        else:
            mis += 1
            dr.rectangle([x, y, x + C - 1, y + C - 1], fill=(60, 60, 70))
            dr.text((x + 10, y + C // 2 - 10), 'ontbreekt:', fill=(255, 200, 120), font=F)
            dr.text((x + 10, y + C // 2 + 10), naam[:36], fill=(255, 200, 120), font=F)
        dr.text((x, y + C + 3), t, fill=(190, 200, 230), font=F)
    y += C + 22 + GAT
blad.save(uit, optimize=True)
print('blad', uit, blad.size, os.path.getsize(uit), 'bytes;', mis, 'beelden ontbreken')
