# Zet Mila's werelden (ontwerp/garmin/werelden11/ebb-werelden-v11-data.json, kopie in deze map) om naar WereldData.mc.
# Gebruik: python3 bron/maak_werelden.py bron/ebb-werelden-v11-data.json source/WereldData.mc
# Eenheid blijft 1/260 D. De strook begint op BOVEN (hoogste punt van alle werelden, naar beneden afgerond op even);
# y in de data is al min BOVEN, zodat het horloge niets hoeft te verschuiven.
# Toetst: alleen MIP-kleuren (elk kanaal 00, 55, AA, FF), hoogstens 64 punten per veelhoek, hoogstens 120 punten per wereld.
import json, sys
bron, uit = sys.argv[1], sys.argv[2]
d = json.load(open(bron))
W = d['werelden']
def kleur(s):
    k = int(s, 16)
    for sh in (16, 8, 0):
        assert (k >> sh) & 255 in (0, 0x55, 0xAA, 0xFF), 'geen MIP-kleur: ' + s
    return k
boven = min(p[1] for w in W for laag in ('vlakken', 'voor_het_dier') for v in w.get(laag, []) for p in v['p'])
boven -= boven % 2
def rij(v):
    assert 3 <= len(v['p']) <= 64, 'veelhoek met %d punten' % len(v['p'])
    g = ['0x%06X' % kleur(v['kleur'])]
    for x, y in v['p']:
        g += [str(int(round(x))), str(int(round(y)) - boven)]
    return '[' + ', '.join(g) + ']'
def blok(naam, laag):
    r = ['    function %s(dier as Number) as Array<Array<Number> > or Null {' % naam]
    for w in W:
        vl = w.get(laag, [])
        if not vl:
            continue
        r.append('        if (dier == %d) {   // %s: %s' % (w['nr'] - 1, w['dier'], w['plek']))
        r.append('            return [')
        r.append(',\n'.join('                ' + rij(v) for v in vl))
        r.append('            ] as Array<Array<Number> >;')
        r.append('        }')
    r.append('        return null;')
    r.append('    }')
    return '\n'.join(r)
for w in W:
    n = sum(len(v['p']) for laag in ('vlakken', 'voor_het_dier') for v in w.get(laag, []))
    assert n <= 120, '%s: %d punten' % (w['dier'], n)
t = ['import Toybox.Lang;', '',
     '// GEMAAKT door bron/maak_werelden.py uit %s (%s). Niet met de hand wijzigen.' % (bron.split('/')[-1], d['versie']),
     '// Per veelhoek [kleur, x, y, x, y, ...] in 1/260 D; y telt vanaf de bovenkant van de strook (BOVEN).',
     'module EbbWereldData {', '    const EENHEID = 260;', '    const BOVEN = %d;' % boven, '',
     blok('vlakken', 'vlakken'), '', '    // Komt over het dier heen (bijvoorbeeld de voorste vingers van de anemoon).', blok('voor', 'voor_het_dier'), '',
     '    // Waar het dier woont (midden van het dier), in 1/260 D van het hele scherm.',
     '    function thuis(dier as Number) as Array<Number> or Null {']
for w in W:
    t.append('        if (dier == %d) { return [%d, %d] as Array<Number>; }' % (w['nr'] - 1, w['thuis'][0], w['thuis'][1]))
t += ['        return null;', '    }', '}', '']
open(uit, 'w').write('\n'.join(t))
print('werelden', len(W), 'boven', boven, [(w['dier'], len(w['vlakken']), len(w.get('voor_het_dier', []))) for w in W])
