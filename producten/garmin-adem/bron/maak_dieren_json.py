# Zet Mila's dieren als data (ontwerp/garmin/ebb-dieren-v8-data.json, of later) om naar source/DierenData.mc.
# Gebruik: python3 maak_dieren_json.py <json> <uit: source/DierenData.mc>
# Bytes per dier zoals Mila ze geeft: [aantal delen, per deel: rol, aantal punten, x, y, ...; aantal ogen, per oog: x, y],
# punten in 1/schaal van de diermaat op het zwaartepunt. Rollen: 0 lijf, 1 licht, 2 donker, 3 zwart, 4 muts (5555FF),
# 5 wit, 7 licht kenmerk, 8 donker kenmerk, 9 alleen in het silhouet, 10 muts kenmerk.
import json, sys

j = json.load(open(sys.argv[1]))
schaal = j['schaal']
regels, tinten, namen = [], [], []
totaal = 0
for d in j['dieren']:
    b = d['bytes']
    o = 1
    for _ in range(b[0]):
        assert b[o] in (0, 1, 2, 3, 4, 5, 7, 8, 9, 10), (d['naam'], b[o])
        n = b[o + 1]
        assert 3 <= n <= 60, (d['naam'], n)
        o += 2 + 2 * n
    assert o + 1 + 2 * b[o] == len(b), d['naam']
    assert all(-127 <= v <= 127 for v in b)
    totaal += len(b)
    regels.append('        [' + ','.join(str(v & 0xFF) for v in b) + ']b')
    t = [int(x, 16) for x in d['tint']] + [int(d['rand'], 16)]
    tinten.append('[' + ', '.join('0x%06X' % v for v in t) + ']')
    namen.append(d['naam'])
vlak = int(j['silhouet']['vlak'], 16)
rand = int(j['silhouet']['rand'], 16)

kop = '''import Toybox.Graphics;
import Toybox.Lang;

// GEMAAKT door bron/maak_dieren_json.py uit Mila's %s (%d dieren). Niet met de hand wijzigen.
// %d bytes voor alle dieren samen. Tekenen: EbbDierPlaatje.laag
// (gevonden met stickerrand, niet gevonden als silhouet: vlak %06X, rand %06X), zie REGELS.md.
module EbbDierData {
    const NAMEN = [%s] as Array<String>;
    // Per dier [lijf, licht, donker, stickerrand].
    const TINT = [%s] as Array<Array<Number> >;
    const SIL_VLAK = 0x%06X;
    const SIL_RAND = 0x%06X;
    // Punten in 1/SCHAAL van de diermaat.
    const SCHAAL = %d;
    const DATA = [
%s
    ] as Array<ByteArray>;
''' % (j.get('bron', sys.argv[1]), len(namen), totaal, vlak, rand, ', '.join('"%s"' % n for n in namen),
       ', '.join(tinten), vlak, rand, schaal, ',\n'.join(regels))

rest = '''
    function s8(b as Number) as Number {
        return b > 127 ? b - 256 : b;
    }

    // Dikte van de stickerrand: 2 px, 3 px op de grote maat (Mila: 3 px op 454).
    function randPx(maat as Number) as Number {
        return maat >= 60 ? 3 : 2;
    }

    // Keuring bouw 2 punt 1 (watchdog): de rand in 4 schuine richtingen in plaats van 8, dus 5 keer tekenen per dier
    // in plaats van 9. De sea log tekent zijn dieren daarbij over een paar beurten in een eigen plaatje (DierenView).
    const RAND_DX = [-1, 1, -1, 1] as Array<Number>;
    const RAND_DY = [-1, -1, 1, 1] as Array<Number>;

    // Tekenen gaat alleen via EbbDierPlaatje.laag (REGELS.md punt 4); hier alleen de data en delen() en ogen().

    // modus 0: eigen kleuren, rol 9 overslaan. 1: alle delen in kleur. 2: alle delen behalve rol 9 in kleur (stickerrand).
    // 3: alleen het kenmerk (rol 7, 8, 10) in kleur. Geeft de plek in de bytes waar de ogen beginnen.
    function delen(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, kleur as Number, modus as Number) as Number {
        var b = DATA[i];
        var t = TINT[i];
        var o = 1;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var rol = b[o];
            var n = b[o + 1];
            o += 2;
            var mee = true;
            if (modus == 0 || modus == 2) {
                mee = (rol != 9);
            } else if (modus == 3) {
                mee = (rol == 7 || rol == 8 || rol == 10);
            }
            if (!mee) {
                o += 2 * n;
                continue;
            }
            var pts = new [n] as Array<[Numeric, Numeric]>;
            for (var k = 0; k < n; k += 1) {
                pts[k] = [cx + (s8(b[o]) * maat) / SCHAAL, cy + (s8(b[o + 1]) * maat) / SCHAAL] as [Numeric, Numeric];
                o += 2;
            }
            var c = kleur;
            if (modus == 0) {
                if (rol < 3) {
                    c = t[rol];
                } else if (rol == 7) {
                    c = t[1];
                } else if (rol == 8) {
                    c = t[2];
                } else if (rol == 3) {
                    c = 0x000000;
                } else if (rol == 4 || rol == 10) {
                    c = 0x5555FF;
                } else {
                    c = 0xFFFFFF;
                }
            }
            dc.setColor(c, c);
            dc.fillPolygon(pts);
        }
        return o;
    }

    // Mila v8.3 (keuring bouw 3, voor Mila punt 1): één donkere pupil zonder wit. Onder maat 60 een vierkantje van
    // ±0,08 maat (2 x 2 op 260), daarboven een rondje met één wit glimpunt (3 x 3 op 454). Geen witte plusjes meer.
    function ogen(dc as Graphics.Dc, i as Number, o as Number, cx as Number, cy as Number, maat as Number) as Void {
        var b = DATA[i];
        var aantal = b[o];
        o += 1;
        for (var k = 0; k < aantal; k += 1) {
            var x = cx + (s8(b[o]) * maat) / SCHAAL;
            var y = cy + (s8(b[o + 1]) * maat) / SCHAAL;
            o += 2;
            if (maat < 60) {
                var e = (8 * maat + 50) / 100;
                e = e < 2 ? 2 : e;
                dc.setColor(0x000000, 0x000000);
                dc.fillRectangle(x - e / 2, y - e / 2, e, e);
            } else {
                var r = maat / 20;
                r = r < 3 ? 3 : r;
                dc.setColor(0x000000, 0x000000);
                dc.fillCircle(x, y, r);
                dc.setColor(0xFFFFFF, 0xFFFFFF);
                dc.drawPoint(x - 1, y - 1);
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
'''
open(sys.argv[2], 'w').write(kop + rest)
print('dieren', len(namen), 'bytes', totaal)
