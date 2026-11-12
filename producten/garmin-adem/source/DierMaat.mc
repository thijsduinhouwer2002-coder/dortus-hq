import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Maat en plaats van een dier in een vak (sea log, inhouden, eindschermen, menu).
// Keuring bouw 3 punt 8 en 9: maten van een dier uit zijn eigen punten, zodat het in een vak past.
module EbbDierMaat {
    // [links, rechts, boven, onder] in 1/SCHAAL van de diermaat.
    // Run 66: onthouden per dier. De wereld vroeg de grenzen een paar keer per beeld op (kam, kader, held) en elke
    // keer liep dit langs alle punten van het dier; met de garnaal gaf dat op de FR255 "Watchdog Tripped, Code
    // Executed Too Long" en een crash bij het eerste beeld van de sessie (toetsrun 43228227771, tweede start fr255).
    // Wie de grenzen krijgt mag ze niet wijzigen: het is de bewaarde lijst zelf.
    var _grenzen as Array<Array<Number>?>? = null;
    function grenzen(i as Number) as Array<Number> {
        if (_grenzen == null) {
            _grenzen = new [EbbDierData.DATA.size()] as Array<Array<Number>?>;
        }
        var lijst = _grenzen as Array<Array<Number>?>;
        var al = lijst[i];
        if (al != null) {
            return al;
        }
        var nieuw = grenzenTel(i);
        lijst[i] = nieuw;
        return nieuw;
    }

    // De telling zelf, langs alle punten (traag; alleen via grenzen aanroepen).
    function grenzenTel(i as Number) as Array<Number> {
        var b = EbbDierData.DATA[i];
        var o = 1;
        var g = [0, 0, 0, 0] as Array<Number>;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var n = b[o + 1];
            o += 2;
            for (var k = 0; k < n; k += 1) {
                var x = EbbDierData.s8(b[o]);
                var y = EbbDierData.s8(b[o + 1]);
                if (x < g[0]) { g[0] = x; }
                if (x > g[1]) { g[1] = x; }
                if (y < g[2]) { g[2] = y; }
                if (y > g[3]) { g[3] = y; }
                o += 2;
            }
        }
        return g;
    }

    // Keuring bouw 4 punt 5 (beelden run 42970833817): dier tussen twee tekstregels, binnen top en onder (px) en
    // hoogstens breed px breed, nooit groter dan maxMaat; het vak zelf staat in het midden tussen top en onder.
    function inBand(dc as Graphics.Dc, i as Number, cx as Number, top as Number, onder as Number, breed as Number, maxMaat as Number, soort as Number) as Void {
        var m = inVak(i, breed, onder - top);
        m = m > maxMaat ? maxMaat : m;
        var g = grenzen(i);
        var cy = (top + onder) / 2 - (g[2] + g[3]) * m / (2 * EbbDierData.SCHAAL);
        EbbDierVoorraad.teken(dc, i, cx, cy, m, soort);
    }

    // Grootste maat waarbij dier i (met stickerrand) binnen breed x hoog px past.
    function inVak(i as Number, breed as Number, hoog as Number) as Number {
        var g = grenzen(i);
        var s = EbbDierData.SCHAAL;
        var mb = (breed - 4) * s / (g[1] - g[0]);
        var mh = (hoog - 4) * s / (g[3] - g[2]);
        var m = mb < mh ? mb : mh;
        return m < 4 ? 4 : m;
    }
}
