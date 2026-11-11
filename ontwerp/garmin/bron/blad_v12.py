# Blad v12 (Mila, run 36, 11 nov avond), opdracht keuring bouw 7 "Voor Mila" punt 3:
# instellingen blad 2 (scène 20) was half leeg en "Ebb makes no sound" dof.
# Regel: onderaan de lijst ben je op de bodem. Bij de laatste twee regels komt de zee hoger (kamlijn op 0,74 D),
# met de vaste zin wit IN het water en je eigen dier eronder. Bij de allerlaatste regel (Safety info) blijft de lijst
# staan en zakt de pil één plek, zodat er twee regels boven staan en niets leeg is. Safety info krijgt een waarde
# ("read again") zodat de pil twee regels heeft zoals alle andere.
#   python3 blad_v12.py <uitmap>
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from blad_v9 import zee, rond, tekst, f, FM, FS, SCHUIM, MIDDEN, WIT, D
from PIL import Image, ImageDraw
LICHTCYAAN, ZACHT = (170, 255, 255), (85, 170, 170)

REGELS = [('Rounds', '3'), ('Breathing pace', '15 per min'), ('Breaths', '30'), ('Recovery hold', '15 s'), ('Weekly goal', '3'),
          ('Buzz every 30 s', 'on'), ('Buzz on last 3 breaths', 'on'), ('Vibration', 'on'),
          ('My pattern: in', '4 s'), ('My pattern: hold', '4 s'), ('My pattern: out', '6 s'), ('My pattern: rest', '2 s'),
          ('Start my pattern', '4-4-6-2'), ('Safety info', 'read again')]
NOTITIE = 'Ebb is silent. Buzz only.'
N = len(REGELS)

# Plekken in D (gemeten op scène 19, fenix 8 47 mm): kop 0,214, regel 0,304, pil 0,377 tot 0,584, regels 0,659 en 0,771.
KOP, R1, PIL_H, STAP = 0.214, 0.304, 0.207, 0.080
PIL_GEWOON = 0.480
PIL_LAAG = 0.564        # laatste regel: pil één plek lager (twee regels erboven)
ZEE_GEWOON, ZEE_BODEM = 0.872, 0.745


def scherm(D_, keuze, oud=False, dier=4):
    s = D_ / 260; c = D_ // 2
    im = Image.new('RGB', (D_, D_)); dr = ImageDraw.Draw(im)
    bodem = (keuze >= N - 2) and not oud
    zee(im, round((ZEE_BODEM if bodem else ZEE_GEWOON) * D_), D_); dr = ImageDraw.Draw(im)
    fk, fr, fn, fv = f(FS, round(25 * s)), f(FM, round(17 * s)), f(FS, round(24 * s)), f(FM, round(18 * s))
    tekst(dr, c, KOP * D_ - 14 * s, 'settings', fk, SCHUIM)
    laag = keuze == N - 1 and not oud
    py = (PIL_LAAG if laag else PIL_GEWOON) * D_
    def regel(r, y):
        n, v = REGELS[r]; tekst(dr, c, y - 10 * s, f'{n}  {v}', fr, LICHTCYAAN)
    if laag:
        regel(keuze - 2, R1 * D_); regel(keuze - 1, (R1 + STAP) * D_)
    elif keuze > 0:
        regel(keuze - 1, R1 * D_)
    n, v = REGELS[keuze]
    bw = max(dr.textlength(n, font=fn), dr.textlength(v, font=fv)) + 24 * s; bw = max(bw, 0.5 * D_)
    bh = PIL_H * D_
    dr.rounded_rectangle([c - bw / 2, py - bh / 2, c + bw / 2, py + bh / 2], radius=bh / 2, fill=MIDDEN)
    if oud and keuze == N - 1:
        tekst(dr, c, py - 14 * s, n, fn, WIT)
    else:
        tekst(dr, c, py - 0.045 * D_ - 14 * s, n, fn, WIT)
        tekst(dr, c, py + 0.055 * D_ - 11 * s, v, fv, LICHTCYAAN)
    if oud:
        y1 = 0.659 * D_
        if keuze + 1 < N: regel(keuze + 1, y1)
        yg = y1 if keuze + 1 == N else y1 + STAP * D_
        if keuze >= N - 2: tekst(dr, c, yg - 10 * s, 'Ebb makes no sound', fr, ZACHT)
    else:
        if not laag and keuze + 1 < N: regel(keuze + 1, 0.659 * D_)
        if not laag and keuze + 2 < N and not bodem: regel(keuze + 2, 0.771 * D_)
        if bodem:
            # de vaste zin in het water, wit (leest als zee-tekst, niet als knop), je eigen dier eronder
            tekst(dr, c, 0.802 * D_ - 9 * s, NOTITIE, f(FM, round(15 * s)), WIT)
            h.teken(dr, D[dier], c, round(0.890 * D_), max(8, round(12 * s)))
    return rond(im)


def groot(im, k): return im.resize((im.width * k, im.height * k), Image.NEAREST)


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    rij = []
    for D_ in (454, 260):
        for naam, kz, oud in (('oud', N - 1, True), ('nieuw-13', N - 2, False), ('nieuw-14', N - 1, False)):
            im = scherm(D_, kz, oud); im.save(os.path.join(uit, f'instellingen-{naam}-{D_}.png')); rij.append((D_, naam, im))
    # overzicht: boven 454 ware grootte, onder 260 dubbel
    W = 3 * 470 + 10; H = 470 + 530 + 20
    ov = Image.new('RGB', (W, H), (30, 30, 30))
    for i, (D_, naam, im) in enumerate(rij):
        if D_ == 454: ov.paste(im, (10 + (i % 3) * 470, 10))
        else: ov.paste(groot(im, 2), (10 + (i % 3) * 470, 490))
    ov.save(os.path.join(uit, 'instellingen-oud-nieuw.png'))
    print('klaar', uit)
