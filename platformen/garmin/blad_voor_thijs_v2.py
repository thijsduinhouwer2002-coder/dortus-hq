# Bladen voor Thijs, versie 2 (Gijs, run 70, 12 nov 2026; opdracht hoofdchat 18:40 NL).
# Vier smalle bladen die op een telefoon te lezen zijn: drie schermen naast elkaar, per rij het horloge en dag of nacht.
# Alleen echte schermafbeeldingen uit de simulator, uitgesneden op het ronde scherm; er wordt niets bijgetekend.
# Een beeld dat ontbreekt krijgt een grijs vak met zijn naam.
#   python3 blad_voor_thijs_v2.py <map namen (volle ronde)> <map proef (9b0879b3)> <map kijk (56876656)> <uit-voorvoegsel>
import sys, os
from PIL import Image, ImageDraw, ImageFont
NAMEN, PROEF, KIJK, UIT = sys.argv[1:5]
MAP = {'n': NAMEN, 'p': PROEF, 'k': KIJK}
# Uitsnede van het ronde scherm in de simulatorfoto (gemeten in run 64).
HORLOGES = [('fenix847mm', 'fenix 8, 47 mm', (135, 247, 589, 701)), ('fr255', 'Forerunner 255', (80, 184, 340, 444))]
C, GAT = 340, 16
W = 3 * C + 4 * GAT
ACHTER = (16, 20, 40)
def letter(maat, vet=False):
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if vet else ''), maat)
FT, FK, FR, FC, FV = letter(40, True), letter(30, True), letter(26), letter(23), letter(19)
ROND = Image.new('L', (C * 4, C * 4), 0)
ImageDraw.Draw(ROND).ellipse([0, 0, C * 4 - 1, C * 4 - 1], fill=255)
ROND = ROND.resize((C, C), Image.LANCZOS)
mis = []

def sessie(dier, kop):
    # Eén dier: vier rijen (twee horloges, dag en nacht), in, uit en hold naast elkaar.
    rijen = []
    for h, hnaam, vak in HORLOGES:
        for dn, dnnaam in [('dag', 'dag'), ('nacht', 'nacht')]:
            rijen.append((hnaam + ', ' + dnnaam, [(('n', 'sessie-%s-%s-%s' % (dier, s, dn)), t) for s, t in
                                                 [('in', 'inademen'), ('uit', 'uitademen'), ('hold', 'inhouden')]], h))
    return (kop, rijen)

def rest(kop, rij):
    # Dezelfde drie schermen op beide horloges.
    return (kop, [(hnaam, rij, h) for h, hnaam, vak in HORLOGES])

def maak(nr, titel, blokken, voet):
    hoogte = GAT + 56
    for kop, rijen in blokken:
        hoogte += 46 + len(rijen) * (38 + C + 36 + GAT)
    hoogte += 30 * len(voet) + GAT
    blad = Image.new('RGB', (W, hoogte), ACHTER)
    dr = ImageDraw.Draw(blad)
    dr.text((GAT, GAT), titel, fill=(255, 255, 255), font=FT)
    y = GAT + 56
    vakken = dict((h, vak) for h, n, vak in HORLOGES)
    for kop, rijen in blokken:
        dr.text((GAT, y + 4), kop, fill=(255, 230, 120), font=FK)
        y += 46
        for rnaam, cellen, h in rijen:
            dr.text((GAT, y + 2), rnaam, fill=(150, 220, 255), font=FR)
            y += 38
            for i, ((bron, naam), t) in enumerate(cellen):
                x = GAT + i * (C + GAT)
                p = os.path.join(MAP[bron], '%s-%s.png' % (naam, h))
                if os.path.exists(p):
                    im = Image.open(p).convert('RGB').crop(vakken[h]).resize((C, C), Image.LANCZOS)
                    blad.paste(im, (x, y), ROND)
                else:
                    mis.append(p)
                    dr.rectangle([x, y, x + C - 1, y + C - 1], fill=(60, 60, 70))
                    dr.text((x + 10, y + C // 2), 'ontbreekt: ' + naam[:22], fill=(255, 200, 120), font=FV)
                tw = dr.textlength(t, font=FC)
                dr.text((x + (C - tw) // 2, y + C + 4), t, fill=(225, 230, 245), font=FC)
            y += C + 36 + GAT
    for regel in voet:
        dr.text((GAT, y), regel, fill=(160, 170, 200), font=FV)
        y += 30
    uit = '%s-%d.png' % (UIT, nr)
    blad.save(uit, optimize=True)
    print(uit, blad.size, os.path.getsize(uit), 'bytes')

VOET = ['Echte schermen uit de Connect IQ-simulator, niets bijgetekend.', 'Volle ronde run 43257045972 (commit 3bc2008), alle 13 horloges groen.']
VOET2 = VOET + ['De code is daarna alleen veranderd in tekst en gedrag (9b0879b3),', 'niet in deze schermen.']
maak(1, 'Ebb 1 van 4: krab en schildpad', [sessie('krab', 'Krab met zwemband (eigen wereld)'), sessie('schild', 'Schildpad met meeuw (eigen wereld)')], VOET2)
maak(2, 'Ebb 2 van 4: twee basisdieren', [sessie('basis', 'Dolfijn (familie vliegers, zandbodem)'), sessie('otter', 'Zeeotter (familie strand, zeegras)')], VOET2)
maak(3, 'Ebb 3 van 4: eerste sessie en einde', [
    sessie('eerste', 'Eerste sessie na het kopen: de vis'),
    rest('Eindscherm na de rondes', [(('k', 'einde-6b'), 'na sessie 1'), (('n', 'einde-6b'), 'nieuw dier'), (('n', 'einde-6c'), 'volgend dier in zicht')]),
    rest('Eindscherm, bijzondere gevallen', [(('k', 'einde-6c'), 'vanzelf gestopt op 5:00'), (('n', 'einde-6d'), 'na Calm'), (('n', 'einde-sea-complete'), 'alle 24 dieren')])],
    VOET + ['"Fish stays with you" en "5:00 auto": kijkproef op de nieuwste code', '(run 43266852163, commit 5687665), zelfde code als 9b0879b3.'])
maak(4, 'Ebb 4 van 4: start, pauze, sea log', [
    rest('Startscherm', [(('n', 'thuis-menu-leeg-dag'), 'allereerste start'), (('n', 'thuis-menu-dag'), 'dag, met je dier'), (('n', 'thuis-menu-nacht'), 'nacht')]),
    rest('Uitleg en pauze', [(('p', 'uitleg'), 'uitleg, eerste keer'), (('p', 'thuis-pauze-dag'), 'pauze, dag'), (('p', 'thuis-pauze-nacht'), 'pauze, nacht')]),
    rest('Sea log', [(('n', 'thuis-sealog-dag'), '8 van 24, dag'), (('n', 'thuis-sealog-nacht'), '8 van 24, nacht'), (('n', 'thuis-sealog-alle-nacht'), 'alles, nacht')]),
    rest('Today, 8 weeks en Calm', [(('n', 'today'), 'Today'), (('n', '8weeks'), '8 weeks'), (('n', 'rustig'), 'Calm 4-7-8')])],
    VOET + ['Uitleg en pauze: korte ronde run 43268276127 (commit 9b0879b3).'])
print(len(mis), 'beelden ontbreken', mis)
