# Zet Mila's dieren (ontwerp/garmin/bron/ebb_dieren_v6.py: 24 plus bonus; of v5, v4) om naar compacte data voor het horloge.
# Gebruik: python3 maak_dieren_data.py <map met Mila's bron> <uit: source/DierenData.mc> [v6|v5|v4]
# Per dier één ByteArray: [aantal delen, per deel: rol, aantal punten, x, y, ...; aantal ogen, per oog: x, y].
# Punten in honderdsten van de diermaat (int8, -127..127), al verschoven naar het zwaartepunt van het getekende dier,
# zodat het dier op (cx, cy) optisch in het midden staat (Mila moet-punt 7, Daan W2).
# Elke veelhoek hoogstens 60 punten (fillPolygon op Garmin kan er 64) door vereenvoudigen (Ramer-Douglas-Peucker).
import sys, os, math
sys.path.insert(0, os.path.abspath(sys.argv[1]))
_argv = sys.argv; sys.argv = ['x']
VERSIE = _argv[3] if len(_argv) > 3 else 'v5'
import ebb_blad_v3 as v3
if VERSIE == 'v6':
    import ebb_dieren_v6 as m
    DELEN = m.delen_v6
    RAND = m.RAND
elif VERSIE == 'v5':
    import ebb_dieren_v5 as m
    DELEN = m.delen_v5
    RAND = m.RAND
else:
    import ebb_dieren_v4 as m
    DELEN = m.nieuwe_delen
    RAND = {}
sys.argv = _argv

# Rollen: kleur uit TINT (lijf, licht, donker), of vast: zwart, muts (0x5555FF), wit.
ROL = {'lijf': 0, 'licht': 1, 'donker': 2, 'zwart': 3, 'muts': 4, 'witp': 5}
MAX = 60
# Punten in 1/SCHAAL eenheid: 90 in plaats van 100, zodat de slagtand van de narwal (v6, tot 1,4 eenheid) in int8 past.
SCHAAL = 90

def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0]-a[0], b[1]-a[1]; n = math.hypot(dx, dy)
    best, j = -1, 0
    for i in range(1, len(pts)-1):
        p = pts[i]
        d = abs(dy*(p[0]-a[0]) - dx*(p[1]-a[1]))/n if n else math.hypot(p[0]-a[0], p[1]-a[1])
        if d > best:
            best, j = d, i
    if best > eps:
        return rdp(pts[:j+1], eps)[:-1] + rdp(pts[j:], eps)
    return [a, b]

def vereenvoudig(pts):
    # dubbele punten weg, dan zo weinig mogelijk vereenvoudigen tot het past
    p = [pts[0]]
    for q in pts[1:]:
        if round(q[0]*100) != round(p[-1][0]*100) or round(q[1]*100) != round(p[-1][1]*100):
            p.append(q)
    eps = 0.004
    uit = rdp(p + [p[0]], eps)[:-1] if len(p) > 3 else p
    while len(uit) > MAX:
        eps *= 1.5
        uit = rdp(p + [p[0]], eps)[:-1]
    return uit

def i8(v):
    v = int(round(v * SCHAAL))
    assert -127 <= v <= 127, v
    return v

regels = []
tinten = []
namen = []
totaal = 0
for soort, naam in m.ALLE:
    delen, ogen = DELEN(soort)
    im, (zx, zy), _ = m.dier_beeld(soort, 100)
    c = im.width/2
    ox, oy = (zx - c)/100, (zy - c)/100     # zwaartepunt in eenheden
    b = [len(delen)]
    for pts, rol in delen:
        v = vereenvoudig([(x-ox, y-oy) for x, y in pts])
        b += [ROL[rol], len(v)]
        for x, y in v:
            b += [i8(x), i8(y)]
    b += [len(ogen)]
    for x, y in ogen:
        b += [i8(x-ox), i8(y-oy)]
    totaal += len(b)
    regels.append('        [' + ','.join(str(x & 0xFF) for x in b) + ']b')
    l, li, d = v3.TINT[soort]
    rand = '0x%02X%02X%02X' % RAND[soort] if soort in RAND else '-1'
    tinten.append('[0x%02X%02X%02X, 0x%02X%02X%02X, 0x%02X%02X%02X, %s]' % (l + li + d + (rand,)))
    namen.append(naam)

with open(sys.argv[2], 'w') as f:
    f.write('''import Toybox.Graphics;
import Toybox.Lang;

// GEMAAKT door bron/maak_dieren_data.py uit Mila's ebb_dieren_%s.py (%d dieren). Niet met de hand wijzigen.
// %d bytes voor alle dieren samen. Tekenen met EbbDierData.teken(dc, nummer, cx, cy, maat).
module EbbDierData {
    const NAMEN = [%s] as Array<String>;
    // Per dier [lijf, licht, donker, rand] in MIP-kleuren; rand -1 is geen lichte rand (Mila v5: zeldzame donkere dieren).
    const TINT = [%s] as Array<Array<Number> >;
    // Zeekomkommer: ooglid half dicht.
    const SLAPERIG = %d;
    // Punten in 1/SCHAAL van de diermaat.
    const SCHAAL = %d;
    const DATA = [
%s
    ] as Array<ByteArray>;
''' % (VERSIE, len(namen), totaal, ', '.join('"%s"' % n for n in namen), ', '.join(tinten), [s for s, _ in m.ALLE].index('komkom'), SCHAAL, ',\n'.join(regels)))
    f.write('''
    function s8(b as Number) as Number {
        return b > 127 ? b - 256 : b;
    }

    // Tekent dier i met zijn zwaartepunt op (cx, cy); maat in px per eenheid (het dier is ±2 eenheden breed).
    // kleur: -1 voor de eigen kleuren, anders één kleur voor alles (silhouet), zonder ogen.
    function teken(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, kleur as Number) as Void {
        var t = TINT[i];
        if (kleur < 0 && t[3] >= 0) {
            // Lichte rand: hetzelfde dier vier keer iets verschoven eronder, in de randkleur.
            var k = (maat + 22) / 45;
            k = k < 1 ? 1 : k;
            vlakken(dc, i, cx - k, cy, maat, t[3]);
            vlakken(dc, i, cx + k, cy, maat, t[3]);
            vlakken(dc, i, cx, cy - k, maat, t[3]);
            vlakken(dc, i, cx, cy + k, maat, t[3]);
        }
        var o = vlakken(dc, i, cx, cy, maat, kleur);
        if (kleur >= 0) {
            return;
        }
        ogen(dc, i, o, cx, cy, maat);
    }

    // Alle vlakken van dier i; kleur -1 is de eigen kleuren. Geeft de plek in de bytes waar de ogen beginnen.
    function vlakken(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, kleur as Number) as Number {
        var b = DATA[i];
        var t = TINT[i];
        var o = 1;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var rol = b[o];
            var n = b[o + 1];
            o += 2;
            var pts = new [n] as Array<[Numeric, Numeric]>;
            for (var k = 0; k < n; k += 1) {
                pts[k] = [cx + (s8(b[o]) * maat) / SCHAAL, cy + (s8(b[o + 1]) * maat) / SCHAAL] as [Numeric, Numeric];
                o += 2;
            }
            var c = kleur;
            if (c < 0) {
                c = (rol < 3) ? t[rol] : ((rol == 3) ? 0x000000 : ((rol == 4) ? 0x5555FF : 0xFFFFFF));
            }
            dc.setColor(c, c);
            if (n >= 3) {
                dc.fillPolygon(pts);
            }
        }
        return o;
    }

    function ogen(dc as Graphics.Dc, i as Number, o as Number, cx as Number, cy as Number, maat as Number) as Void {
        var b = DATA[i];
        var t = TINT[i];
        var aantal = b[o];
        o += 1;
        for (var k = 0; k < aantal; k += 1) {
            var x = cx + (s8(b[o]) * maat) / SCHAAL;
            var y = cy + (s8(b[o + 1]) * maat) / SCHAAL;
            o += 2;
            var r = (13 * maat) / 100;
            r = r < 2 ? 2 : r;
            var p = (7 * maat) / 100;
            p = p < 1 ? 1 : p;
            dc.setColor(0xFFFFFF, 0xFFFFFF);
            dc.fillCircle(x, y, r);
            dc.setColor(0x000055, 0x000055);
            dc.fillCircle(x - (r * 3) / 10, y, p);
            if (i == SLAPERIG) {
                // Ooglid half dicht: de bovenste helft van het oog in de donkere kleur.
                dc.setClip(x - r, y - r, 2 * r + 1, r);
                dc.setColor(t[2], t[2]);
                dc.fillCircle(x, y, r);
                dc.clearClip();
            } else if (maat >= 30) {
                var g = (35 * maat + 500) / 1000;
                g = g < 1 ? 1 : g;
                dc.setColor(0xFFFFFF, 0xFFFFFF);
                dc.fillCircle(x - (r * 55) / 100, y - r / 2, g);
            }
        }
    }

    // Aantal veelhoeken en punten van dier i, voor de toets: [delen, punten, ogen].
    function telling(i as Number) as Array<Number> {
        var b = DATA[i];
        var o = 1;
        var punten = 0;
        for (var deel = 0; deel < b[0]; deel += 1) {
            punten += b[o + 1];
            o += 2 + 2 * b[o + 1];
        }
        return [b[0], punten, b[o]] as Array<Number>;
    }
}
''')
print('bytes', totaal)
