# Blad werelden v1.4 (Mila, run 42): besluit 12 nov 00:25 punt 2 en 3 die nog openstonden.
# Lucht per dagdeel (ochtend, dag, avond, nacht) en de maan in acht standen, alles in MIP-kleuren en alleen vlakken
# (rechthoek, cirkel, veelhoek). Plus per wereld de plek waar de bellen vandaan komen.
# Bouwt op werelden_v13 (zelfde werelden, zelfde data); alleen de lucht en de bellen zijn nieuw.
#   python3 werelden_v14.py <uitmap>
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v13 as W
from werelden_v13 import S, hx, TEKSTVAK, rond, STERREN, WIT
from PIL import Image, ImageDraw

# Elk dagdeel: lucht (één vlak), rand (band van `rand_hoog` boven de kam, alleen waar lucht is), zon of maan, sterren.
# Kleuren getoetst: kop 00FFFF, wit en menuregel 00AAFF houden minstens 4,5:1 op elke lucht (000055 14,8 / 0000AA 10,6 / 550055 11,0 en 5,4 voor 00AAFF).
DAGDELEN = {
    'ochtend': dict(uren=[6, 10], lucht='0x0000AA', rand='0xFF55AA', rand_hoog=9, rand2='0xFFAA55', rand2_hoog=4, zon=dict(kleur='0xFFFF55', x=96, y='kam+2', r=10),
                    sterren=False, maan=False, wat='roze en perzik streep op de horizon, grote zon komt links van het midden half uit het water (vrij van planten en rotsen)'),
    'dag':     dict(uren=[10, 17], lucht='0x0000AA', rand=None, rand_hoog=0, zon=dict(kleur='0xFFFF55', x=214, y=40, r=8),
                    wolk=[[208, 96], [214, 88], [224, 88], [230, 80], [240, 82], [246, 90], [250, 96]], wolk2=[[14, 110], [20, 104], [30, 105], [36, 100], [46, 104], [50, 110]],
                    sterren=False, maan=False, wat='zon hoog rechts op de plek van de maan, een grote wolk ervoor en een kleine links'),
    'avond':   dict(uren=[17, 21], lucht='0x550055', rand='0xFF5500', rand_hoog=7, zon=dict(kleur='0xFFAA00', x=166, y='kam+1', r=11),
                    sterren=True, maan=False, wat='paarse lucht, oranje streep, grote oranje zon zakt rechts van het midden in het water, eerste sterren'),
    'nacht':   dict(uren=[21, 6], lucht='0x000055', rand=None, rand_hoog=0, zon=None, sterren=True, maan=True,
                    wat='nachtblauw met sterren en de maan in de stand van vandaag'),
}
# Maan: middelpunt (214, 40), straal 8. Stand 0 tot 7 (0 nieuw, 4 vol). Tekenen met drie aanroepen, alles convex:
# 1. schijf in de luchtkleur (of 555555 bij nieuw, FFFFAA bij vol); 2. de verlichte helft FFFFAA (halve schijf: fillCircle plus
# een rechthoek in de luchtkleur over de donkere helft); 3. een ellips midden op de maan, halve breedte `ellips` x straal,
# in de luchtkleur bij een sikkel (snoept van de lichte helft) of FFFFAA bij bol (vult de donkere helft deels). Kwartier: geen ellips.
MAAN = dict(x=214, y=40, r=8)
MAANSTANDEN = [
    dict(nr=0, naam='nieuwe maan', licht=None, ellips=None, nieuw=True),
    dict(nr=1, naam='wassende sikkel', licht='rechts', ellips=('lucht', 0.35)),
    dict(nr=2, naam='eerste kwartier', licht='rechts', ellips=None),
    dict(nr=3, naam='wassend bol', licht='rechts', ellips=('licht', 0.6)),
    dict(nr=4, naam='volle maan', licht='heel', ellips=None),
    dict(nr=5, naam='afnemend bol', licht='links', ellips=('licht', 0.6)),
    dict(nr=6, naam='laatste kwartier', licht='links', ellips=None),
    dict(nr=7, naam='afnemende sikkel', licht='links', ellips=('lucht', 0.35)),
]
# Bellen: waar ze vandaan komen per wereld (1/260 D), drie ringen omhoog, om de 11 hoger, om en om 4 naar rechts.
BELLEN = {'Turtle': dict(bron='snuit van het dier (kader rechtsboven)', dx=10, dy=-6, wanneer='uitademen'),
          'Crab': dict(bron='mond van de krab', dx=8, dy=-8, wanneer='altijd, twee ringen'),
          'Clownfish': dict(bron='bek van de vis', dx=-10, dy=-4, wanneer='uitademen; in de anemoon komen ze tussen de vingers door')}

STAND = {'dagdeel': 'nacht', 'maan': 7}

def maan(dr, D_, lucht_kleur, nr):
    m = MAANSTANDEN[nr]; s = D_ / 260; R = round(MAAN['r'] * s); X, Y = S(MAAN['x'], D_), S(MAAN['y'], D_)
    LICHT_ = hx('0xFFFFAA'); L_ = hx(lucht_kleur)
    if m.get('nieuw'): dr.ellipse([X - R, Y - R, X + R, Y + R], fill=hx('0x555555')); return
    dr.ellipse([X - R, Y - R, X + R, Y + R], fill=LICHT_)
    if m['licht'] == 'rechts': dr.rectangle([X - R - 1, Y - R - 1, X - 1, Y + R + 1], fill=L_)
    if m['licht'] == 'links': dr.rectangle([X + 1, Y - R - 1, X + R + 1, Y + R + 1], fill=L_)
    if m['ellips']:
        soort, b = m['ellips']; w = round(b * R)
        dr.ellipse([X - w, Y - R, X + w, Y + R], fill=L_ if soort == 'lucht' else LICHT_)

def lucht_dagdeel(dr, D_, top_px):
    d = DAGDELEN[STAND['dagdeel']]; s = D_ / 260; kam = top_px / s
    dr.rectangle([0, 0, D_, D_], fill=hx(d['lucht']))
    if d['rand']: dr.rectangle([0, S(kam - d['rand_hoog'], D_), D_, D_], fill=hx(d['rand']))
    if d.get('rand2'): dr.rectangle([0, S(kam - d['rand2_hoog'], D_), D_, D_], fill=hx(d['rand2']))
    if d['sterren']:
        e = 1 if D_ < 300 else 2
        for x, y in (STERREN if d['maan'] else STERREN[:3]):
            if y < kam - 8: dr.rectangle([S(x, D_), S(y, D_), S(x, D_) + e - 1, S(y, D_) + e - 1], fill=WIT)
    for k in ('wolk', 'wolk2'):
        if d.get(k) and max(y for _, y in d[k]) < kam - 4: dr.polygon([(S(x, D_), S(y, D_)) for x, y in d[k]], fill=WIT)
    z = d['zon']
    if z:
        y = kam + int(z['y'][3:]) if isinstance(z['y'], str) else z['y']
        if y < kam - 2 or isinstance(z['y'], str):
            R = round(z['r'] * s); X, Y = S(z['x'], D_), S(y, D_); dr.ellipse([X - R, Y - R, X + R, Y + R], fill=hx(z['kleur']))
    if d['maan'] and MAAN['y'] + MAAN['r'] < kam - 2: maan(dr, D_, d['lucht'], STAND['maan'])

def water(im, top, D_):
    dr = ImageDraw.Draw(im); lucht_dagdeel(dr, D_, top)
    s = D_ / 260; a = 4 * s
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 2.5)); dr.line([(x, yk), (x, D_)], fill=W.MIDDEN)
    for r in W.STRALEN:
        t = top / s + 8
        if t < 200:
            dr.polygon([(S(r['x_top'], D_), S(t, D_)), (S(r['x_top'] + r['breed'], D_), S(t, D_)),
                        (S(r['x_onder'] + r['breed'] / 2, D_), S(205, D_)), (S(r['x_onder'], D_), S(205, D_))], fill=hx(W.STRAAL_KLEUR))
    for v in W.VISJES:
        if top / s + 10 < min(y for _, y in v): dr.polygon([(S(x, D_), S(y, D_)) for x, y in v], fill=hx(W.VIS_KLEUR))
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 2.5))
        dr.line([(x, yk + round(2 * s)), (x, yk + round(5 * s))], fill=W.LICHT); dr.line([(x, yk), (x, yk + round(2 * s) - 1)], fill=W.SCHUIM)

W.water = water

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    wd = W.WERELDEN
    # 1. dagdelen: menu en adem uit van de schildpad, krab en clownvis, elk dagdeel een kolom (260 ware grootte en 2x)
    rij260 = []; meting = []; vreemd = 0
    for maak in (lambda w: W.menu(260, w, 4), lambda w: W.adem(260, w, False, 4)):
        for w in wd:
            rij = []
            for dd in DAGDELEN:
                STAND['dagdeel'] = dd; TEKSTVAK.clear(); im, nm = maak(w); vak = list(TEKSTVAK); rij.append(im)
                oud = W.V.tekst; W.V.tekst = lambda *a, **k: None; TEKSTVAK.clear(); kaal, _ = maak(w); W.V.tekst = oud
                meting += [(dd,) + tuple(m) for m in W.meet(kaal, vak)]; vreemd += W.pixeltoets(kaal)
            rij260.append(rij)
    ov = W.rij_beeld(rij260, 260); ov.save(os.path.join(uit, 'dagdelen-260-1x.png'))
    ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'dagdelen-260-2x.png'))
    # 454: menu schildpad per dagdeel
    r454 = []
    for dd in DAGDELEN:
        STAND['dagdeel'] = dd; TEKSTVAK.clear(); r454.append(W.menu(454, wd[0], 4)[0])
    W.rij_beeld([r454], 454).save(os.path.join(uit, 'dagdelen-454.png'))
    # 2. maanstanden: uitsnede rond de maan op 260, 6x vergroot, en het hele menu bij vol en sikkel
    STAND['dagdeel'] = 'nacht'; maanrij = []
    for m in MAANSTANDEN:
        STAND['maan'] = m['nr']; TEKSTVAK.clear(); im, _ = W.menu(260, wd[1], 4)
        maanrij.append(im.crop((190, 16, 238, 64)).resize((144, 144), Image.NEAREST))
    mr = Image.new('RGB', (8 * 154 + 10, 154), (30, 30, 30))
    for i, im in enumerate(maanrij): mr.paste(im, (10 + i * 154, 5))
    mr.save(os.path.join(uit, 'maanstanden-6x.png'))
    # data
    json.dump({'versie': 'werelden v1.4 lucht en bellen (bij werelden v1.3-data)', 'eenheid': '1/260 D, y van boven',
               'dagdelen': DAGDELEN, 'maan': MAAN, 'maanstanden': MAANSTANDEN, 'bellen': BELLEN,
               'regels': ['dagdeel uit de klok van het horloge; maanstand uit de datum (synodische maand 29,53 dagen vanaf een bekende nieuwe maan), afronden op de dichtstbijzijnde van 8',
                          'zon en maan alleen tekenen als ze minstens 2 boven de kam vallen (op hold dekt het water ze)',
                          'de rand (horizonstreep) ligt direct boven de kam en beweegt mee met de kam',
                          'avond: alleen de eerste drie sterren']},
              open(os.path.join(uit, 'ebb-lucht-v14-data.json'), 'w'), indent=1)
    lo = sorted(meting, key=lambda r: r[3])[:6]
    print('pixels buiten MIP', vreemd); print('laagste contrast', lo)
