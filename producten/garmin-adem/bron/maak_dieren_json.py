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
// %d bytes voor alle dieren samen. Gevonden: EbbDierData.teken(dc, nummer, cx, cy, maat, -1) (met witte stickerrand);
// niet gevonden: EbbDierData.silhouet(dc, nummer, cx, cy, maat) (vlak %06X, rand en kenmerk %06X).
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

    // Keuring bouw 2 punt 1 (watchdog in sea log en inhoudscherm): elk dier wordt één keer in een BufferedBitmap
    // getekend en daarna als plaatje hergebruikt. De rand komt uit een masker (het dier één keer in de randkleur) dat
    // het horloge zelf 8 keer verschoven plakt, zonder bytecode per punt. Eerst 9 keer alle punten per dier per beurt.
    var _cache as Dictionary<Number, Graphics.BufferedBitmapReference> = {} as Dictionary<Number, Graphics.BufferedBitmapReference>;
    var _palet as Array<Number>? = null;
    const CACHE_MAX = 14;

    // De 64 kleuren van het MIP-scherm plus doorzichtig; alle dieren gebruiken alleen deze kleuren.
    function palet() as Array<Number> {
        if (_palet == null) {
            var p = [Graphics.COLOR_TRANSPARENT] as Array<Number>;
            for (var r = 0; r < 4; r += 1) {
                for (var g = 0; g < 4; g += 1) {
                    for (var b = 0; b < 4; b += 1) {
                        p.add(r * 0x550000 + g * 0x5500 + b * 0x55);
                    }
                }
            }
            _palet = p;
        }
        return _palet as Array<Number>;
    }

    function sleutel(i as Number, maat as Number, soort as Number) as Number {
        return (i * 512 + maat) * 2 + soort;
    }

    // Staat het plaatje al klaar? soort 0 gevonden, 1 silhouet. De sea log maakt per beurt maar een paar nieuwe.
    function klaar(i as Number, maat as Number, soort as Number) as Boolean {
        var r = _cache.get(sleutel(i, maat, soort));
        return r != null && r.get() != null;
    }

    // Halve breedte van het plaatje: verste punt of oog, plus oog, rand en marge.
    function halve(i as Number, maat as Number) as Number {
        var b = DATA[i];
        var m = 0;
        var o = 1;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var n = b[o + 1];
            o += 2;
            for (var k = 0; k < 2 * n; k += 1) {
                var v = s8(b[o + k]);
                v = v < 0 ? -v : v;
                m = v > m ? v : m;
            }
            o += 2 * n;
        }
        var aantalOgen = b[o];
        for (var k = 0; k < 2 * aantalOgen; k += 1) {
            var v = s8(b[o + 1 + k]);
            v = v < 0 ? -v : v;
            m = v > m ? v : m;
        }
        return (m * maat) / SCHAAL + (13 * maat) / 100 + randPx(maat) + 3;
    }

    function leeg(dc as Graphics.Dc) as Void {
        dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
        dc.clear();
    }

    function plaatje(i as Number, maat as Number, soort as Number) as Graphics.BufferedBitmap {
        var s = sleutel(i, maat, soort);
        var r = _cache.get(s);
        if (r != null) {
            var oud = r.get();
            if (oud != null) {
                return oud as Graphics.BufferedBitmap;
            }
        }
        if (_cache.size() >= CACHE_MAX) {
            _cache = {} as Dictionary<Number, Graphics.BufferedBitmapReference>;
        }
        var h = halve(i, maat);
        var z = 2 * h + 1;
        var ref = Graphics.createBufferedBitmap({:width => z, :height => z, :palette => palet()});
        var bb = ref.get() as Graphics.BufferedBitmap;
        var dc = bb.getDc();
        leeg(dc);
        var k = (soort == 0) ? randPx(maat) : 2;
        var randKleur = (soort == 0) ? TINT[i][3] : SIL_RAND;
        var mref = Graphics.createBufferedBitmap({:width => z, :height => z, :palette => [Graphics.COLOR_TRANSPARENT, randKleur] as Array<Number>});
        var mb = mref.get() as Graphics.BufferedBitmap;
        var mdc = mb.getDc();
        leeg(mdc);
        delen(mdc, i, h, h, maat, randKleur, (soort == 0) ? 2 : 1);
        for (var dx = -1; dx <= 1; dx += 1) {
            for (var dy = -1; dy <= 1; dy += 1) {
                if (dx != 0 || dy != 0) {
                    dc.drawBitmap(dx * k, dy * k, mb);
                }
            }
        }
        if (soort == 0) {
            var o = delen(dc, i, h, h, maat, -1, 0);
            ogen(dc, i, o, h, h, maat);
        } else {
            delen(dc, i, h, h, maat, SIL_VLAK, 1);
            delen(dc, i, h, h, maat, SIL_RAND, 3);
        }
        _cache.put(s, ref);
        return bb;
    }

    // Gevonden dier i op zijn zwaartepunt (cx, cy); maat in px per eenheid (het dier is ±2 eenheden breed).
    // kleur -1: met witte stickerrand en ogen, uit het plaatje. kleur >= 0: het hele dier in die ene kleur, zonder ogen.
    function teken(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, kleur as Number) as Void {
        if (kleur >= 0) {
            delen(dc, i, cx, cy, maat, kleur, 1);
            return;
        }
        var bb = plaatje(i, maat, 0);
        dc.drawBitmap(cx - bb.getWidth() / 2, cy - bb.getHeight() / 2, bb);
    }

    // Niet gevonden (Mila v8): de buitenvorm met alle delen (ook rol 9) in de randkleur 2 px verschoven, dan in het vlak,
    // daarna het kenmerk (rol 7, 8 en 10) in de randkleur erover. Zonder ogen. Uit het plaatje.
    function silhouet(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number) as Void {
        var bb = plaatje(i, maat, 1);
        dc.drawBitmap(cx - bb.getWidth() / 2, cy - bb.getHeight() / 2, bb);
    }

    // Oude aanroep: kleur -1 is het gevonden dier zonder rand, anders alle delen in die kleur.
    function vlakken(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, kleur as Number) as Number {
        return delen(dc, i, cx, cy, maat, kleur, kleur < 0 ? 0 : 1);
    }

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

    // Mila v8: één oogvorm voor alle dieren (wit oog, donkere pupil, glimpje vanaf maat 30).
    function ogen(dc as Graphics.Dc, i as Number, o as Number, cx as Number, cy as Number, maat as Number) as Void {
        var b = DATA[i];
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
            if (maat >= 30) {
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
'''
open(sys.argv[2], 'w').write(kop + rest)
print('dieren', len(namen), 'bytes', totaal)
