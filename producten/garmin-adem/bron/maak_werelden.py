# Zet Mila's werelden (ontwerp/garmin/werelden13/ebb-werelden-v13-data.json, kopie in deze map) om naar gegevens.
# Gebruik: python3 bron/maak_werelden.py bron/ebb-werelden-v13-data.json resources/werelden/werelden.xml source/WereldData.mc
# Codekeuring bouw 9 punt 1: de werelden zijn gegevens, geen code. Per wereld één jsonData in werelden.xml; het horloge
# laadt alleen de wereld van het gekozen dier (WatchUi.loadResource). WereldData.mc is alleen de lijst (heeft, laad).
# Per wereld (eenheid 1/260 D):
#   "b" bovenkant van het plaatje (hoogste punt van wat IN het plaatje komt, afgerond op even; punt 2: per wereld),
#   "t" thuis [x, y], "m" maat van het dier (schermen.hold in de json),
#   "v" vlakken in het plaatje (lagen ver en midden, zonder p2 en zonder week): [kleur, x, y - b, ...],
#   "d" details in het plaatje (week > 0): [week, kleur, x, y - b, ...], oplopend op week,
#   "p" planten (vlakken met p2), direct getekend na het plaatje: [kleur, x, y, ...] met y vanaf de bovenkant van het
#       scherm, en "q" dezelfde vlakken in de stand bij inademen (zelfde aantal punten, zelfde kleur vooraan),
#   "f" wat over het dier heen komt (voor_het_dier), direct getekend, en "g" de stand bij inademen of null.
# Punt 2 en 7: in het plaatje alleen wat stil staat; planten en voorlaag gaan direct, samen hoogstens 40 punten.
# Kleuren als gewoon getal (json kent geen hex).
# Toetst: alleen MIP-kleuren (elk kanaal 00, 55, AA, FF), hoogstens 64 punten per veelhoek, hoogstens 120 punten per wereld.
import json, sys
bron, uit_xml, uit_mc = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(bron))
W = d['werelden']
def kleur(s):
    k = int(s, 16)
    for sh in (16, 8, 0):
        assert (k >> sh) & 255 in (0, 0x55, 0xAA, 0xFF), 'geen MIP-kleur: ' + s
    return k
def rij(v, boven, week=False, sleutel='p'):
    assert 3 <= len(v[sleutel]) <= 64, 'veelhoek met %d punten' % len(v[sleutel])
    assert len(v[sleutel]) == len(v['p']), 'p2 met een ander aantal punten dan p'
    g = ([int(v['week'])] if week else []) + [kleur(v['kleur'])]
    for x, y in v[sleutel]:
        g += [int(round(x)), int(round(y)) - boven]
    return g
MAAT = int(d.get('schermen', {}).get('hold', {}).get('dier', {}).get('maat_260', 20))
x = ['<!-- GEMAAKT door bron/maak_werelden.py uit %s (%s). Niet met de hand wijzigen. -->' % (bron.split('/')[-1], d['versie']), '<resources>']
m = ['import Toybox.Lang;', 'import Toybox.WatchUi;', '',
     '// GEMAAKT door bron/maak_werelden.py uit %s (%s). Niet met de hand wijzigen.' % (bron.split('/')[-1], d['versie']),
     '// Alleen de lijst van werelden; de punten staan per wereld in resources/werelden/werelden.xml en worden pas',
     '// geladen als het dier gekozen is. Sleutels: zie bron/maak_werelden.py (b, t, m, v, d, p, q, f, g).',
     'module EbbWereldData {', '    const EENHEID = 260;', '']
heeft, laad, verslag = [], [], []
for w in W:
    nr = w['nr'] - 1
    V, F = w.get('vlakken', []), w.get('voor_het_dier', [])
    n = sum(len(v['p']) for v in V + F)
    assert n <= 120, '%s: %d punten' % (w['dier'], n)
    stil = [v for v in V if 'p2' not in v]
    planten = [v for v in V if 'p2' in v]
    assert all(not v.get('week') for v in planten + F), w['dier'] + ': een plant of voorlaag met een week kan nog niet'
    direct = sum(len(v['p']) for v in planten + F)
    assert direct <= 40, '%s: %d punten direct getekend (grens 40 per beurt)' % (w['dier'], direct)
    boven = min(int(round(p[1])) for v in stil for p in v['p'])
    boven -= boven % 2
    assert boven >= 0 and 20 <= w['thuis'][0] <= 240 and 100 <= w['thuis'][1] <= 240, w['dier'] + ': thuis buiten het scherm'
    g = {'b': boven, 't': [int(w['thuis'][0]), int(w['thuis'][1])], 'm': MAAT,
         'v': [rij(v, boven) for v in stil if not v.get('week')],
         'd': [rij(v, boven, True) for v in sorted([v for v in stil if v.get('week')], key=lambda v: v['week'])],
         'p': [rij(v, 0) for v in planten], 'q': [rij(v, 0, False, 'p2') for v in planten],
         'f': [rij(v, 0) for v in F], 'g': [rij(v, 0, False, 'p2') if 'p2' in v else None for v in F]}
    x.append('    <!-- %s: %s -->' % (w['dier'], w['plek']))
    x.append('    <jsonData id="wereld%d">%s</jsonData>' % (nr, json.dumps(g, separators=(',', ':'))))
    heeft.append('dier == %d' % nr)
    laad.append('        if (dier == %d) { return WatchUi.loadResource(Rez.JsonData.wereld%d) as Dictionary; }   // %s' % (nr, nr, w['dier']))
    verslag.append((w['dier'], 'boven', boven, 'vlakken', len(g['v']), 'details', len(g['d']), 'planten', len(g['p']), 'voor', len(g['f']), 'punten', n, 'direct', direct))
x += ['</resources>', '']
m += ['    function heeft(dier as Number) as Boolean {', '        return ' + ' || '.join(heeft) + ';', '    }', '',
      '    // De gegevens van één wereld, of null als dit dier er geen heeft.',
      '    function laad(dier as Number) as Dictionary or Null {'] + laad + ['        return null;', '    }', '}', '']
open(uit_xml, 'w').write('\n'.join(x))
open(uit_mc, 'w').write('\n'.join(m))
print('werelden', len(W), verslag)
