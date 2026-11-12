# Eén blad voor Thijs (nummer 6 van besluit 12 nov 11:50): alle schermen van vijf dieren (krab, schildpad, twee dieren
# in de basiswereld en het startdier) op fenix 8 47 mm en Forerunner 255, dag en nacht, plus eerste start, start, pauze, sea log en eindscherm.
# Alleen echte schermafbeeldingen uit de plaatjesrun (map namen/), uitgesneden op het ronde scherm; er wordt niets
# bijgetekend. Een beeld dat ontbreekt krijgt een grijs vak met zijn naam, zodat je ziet wat er nog niet is.
#   python3 bron/blad_voor_thijs.py <map met de beelden op naam> <uit.png>
import sys, os
from PIL import Image, ImageDraw, ImageFont
m, uit = sys.argv[1], sys.argv[2]
# Uitsnede: precies het ronde scherm in de simulatorfoto. Gemeten in run 64 op de beelden van run 43210421635:
# fenix 8 47 mm 454 px vanaf (135, 247), Forerunner 255 260 px vanaf (80, 184). De oude vakken lagen ernaast (bij de
# FR255 kwam rechts een randje kast in beeld). Wat buiten de cirkel valt (de kast) krijgt de kleur van het blad.
HORLOGES = [('fenix847mm', 'fenix 8, 47 mm (AMOLED)', (135, 247, 589, 701)), ('fr255', 'Forerunner 255 (MIP)', (80, 184, 340, 444))]
# Run 68 (hoofdchat 12 nov 14:50): twee basisdieren uit verschillende families naast elkaar, zodat het verschil in kleur
# en bodem te zien is: dolfijn (familie vliegers, zand) en zeeotter (familie strand, zeegras), KrabV2Basis.FAM en BODEM.
# Daaronder de eerste sessie van een koper: de vis als startdier.
DIEREN = [('krab', 'Crab, with his swim ring (own world)'), ('schild', 'Turtle, with the gull (own world)'),
          ('basis', 'Dolphin, shared sea (family: flyers, sand floor)'), ('otter', 'Sea otter, shared sea (family: beach, seagrass floor)'),
          ('eerste', 'First session after buying: the starter fish')]
SESSIE = [('in-dag', 'breathe in, day'), ('uit-dag', 'breathe out, day'), ('hold-dag', 'hold, day'),
          ('in-nacht', 'breathe in, night'), ('uit-nacht', 'breathe out, night'), ('hold-nacht', 'hold, night')]
# Start, pauze en sea log komen uit de acht thuisscènes van Bas (thuiswater); Today en het eindscherm uit de gewone scènes.
REST = [('thuis-menu-leeg-dag', 'very first start'), ('thuis-menu-dag', 'start, day'), ('thuis-menu-nacht', 'start, night'), ('thuis-pauze-dag', 'pause'),
        ('thuis-sealog-dag', 'sea log'), ('einde-6c-krab', 'end of a session')]
C, GAT, KOP = 300, 14, 26
def letter(maat):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/dejavu/DejaVuSans.ttf']:
        if os.path.exists(p):
            return ImageFont.truetype(p, maat)
    return ImageFont.load_default()
F, FG = letter(15), letter(22)
ROND = Image.new('L', (C * 4, C * 4), 0)
ImageDraw.Draw(ROND).ellipse([0, 0, C * 4 - 1, C * 4 - 1], fill=255)
ROND = ROND.resize((C, C), Image.LANCZOS)
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
            blad.paste(im, (x, y), ROND)
        else:
            mis += 1
            dr.rectangle([x, y, x + C - 1, y + C - 1], fill=(60, 60, 70))
            dr.text((x + 10, y + C // 2 - 10), 'ontbreekt:', fill=(255, 200, 120), font=F)
            dr.text((x + 10, y + C // 2 + 10), naam[:36], fill=(255, 200, 120), font=F)
        dr.text((x, y + C + 3), t, fill=(190, 200, 230), font=F)
    y += C + 22 + GAT
blad.save(uit, optimize=True)
print('blad', uit, blad.size, os.path.getsize(uit), 'bytes;', mis, 'beelden ontbreken')
