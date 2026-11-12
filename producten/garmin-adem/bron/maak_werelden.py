# Zet Mila's werelden (ontwerp/garmin/werelden11/ebb-werelden-v11-data.json, kopie in deze map) om naar gegevens.
# Gebruik: python3 bron/maak_werelden.py bron/ebb-werelden-v11-data.json resources/werelden/werelden.xml source/WereldData.mc
# Codekeuring bouw 9 punt 1: de werelden zijn gegevens, geen code. Per wereld één jsonData in werelden.xml; het horloge
# laadt alleen de wereld van het gekozen dier (WatchUi.loadResource). WereldData.mc is alleen de lijst (heeft, laad).
# Per wereld: {"b": bovenkant van de strook, "t": thuis [x, y], "v": vlakken, "d": details, "f": voor het dier}.
# Eenheid 1/260 D. "b" is het hoogste punt van DEZE wereld (naar beneden afgerond op even; punt 2: niet de hoogste van
# alle werelden), y in v, d en f is al min b; "t" telt vanaf de bovenkant van het scherm.
# Een vlak met "week": n in de json is een detail dat pas verschijnt na n gehaalde weekdoelen (besluit 12 nov 00:25
# punt 4); die komen in "d" als [week, kleur, x, y, ...], oplopend op week. Kleuren als gewoon getal (json kent geen hex).
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
def rij(v, boven, week=False):
    assert 3 <= len(v['p']) <= 64, 'veelhoek met %d punten' % len(v['p'])
    g = ([int(v['week'])] if week else []) + [kleur(v['kleur'])]
    for x, y in v['p']:
        g += [int(round(x)), int(round(y)) - boven]
    return g
x = ['<!-- GEMAAKT door bron/maak_werelden.py uit %s (%s). Niet met de hand wijzigen. -->' % (bron.split('/')[-1], d['versie']), '<resources>']
m = ['import Toybox.Lang;', 'import Toybox.WatchUi;', '',
     '// GEMAAKT door bron/maak_werelden.py uit %s (%s). Niet met de hand wijzigen.' % (bron.split('/')[-1], d['versie']),
     '// Alleen de lijst van werelden; de punten staan per wereld in resources/werelden/werelden.xml en worden pas',
     '// geladen als het dier gekozen is. Sleutels: b bovenkant strook, t thuis, v vlakken, d details, f voor het dier.',
     'module EbbWereldData {', '    const EENHEID = 260;', '']
heeft, laad, verslag = [], [], []
for w in W:
    nr = w['nr'] - 1
    alle = w.get('vlakken', []) + w.get('voor_het_dier', [])
    n = sum(len(v['p']) for v in alle)
    assert n <= 120, '%s: %d punten' % (w['dier'], n)
    boven = min(int(round(p[1])) for v in alle for p in v['p'])
    boven -= boven % 2
    assert boven >= 0 and 20 <= w['thuis'][0] <= 240 and boven <= w['thuis'][1] <= 240, w['dier'] + ': thuis buiten de strook'
    g = {'b': boven, 't': [int(w['thuis'][0]), int(w['thuis'][1])],
         'v': [rij(v, boven) for v in w.get('vlakken', []) if 'week' not in v],
         'd': [rij(v, boven, True) for v in sorted([v for v in w.get('vlakken', []) if 'week' in v], key=lambda v: v['week'])],
         'f': [rij(v, boven) for v in w.get('voor_het_dier', [])]}
    x.append('    <!-- %s: %s -->' % (w['dier'], w['plek']))
    x.append('    <jsonData id="wereld%d">%s</jsonData>' % (nr, json.dumps(g, separators=(',', ':'))))
    heeft.append('dier == %d' % nr)
    laad.append('        if (dier == %d) { return WatchUi.loadResource(Rez.JsonData.wereld%d) as Dictionary; }   // %s' % (nr, nr, w['dier']))
    verslag.append((w['dier'], boven, len(g['v']), len(g['d']), len(g['f']), n))
x += ['</resources>', '']
m += ['    function heeft(dier as Number) as Boolean {', '        return ' + ' || '.join(heeft) + ';', '    }', '',
      '    // De gegevens van één wereld, of null als dit dier er geen heeft.',
      '    function laad(dier as Number) as Dictionary or Null {'] + laad + ['        return null;', '    }', '}', '']
open(uit_xml, 'w').write('\n'.join(x))
open(uit_mc, 'w').write('\n'.join(m))
print('werelden', len(W), verslag)
