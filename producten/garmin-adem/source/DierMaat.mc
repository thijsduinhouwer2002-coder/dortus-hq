import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Sea log volgens blad v7 en v8 (keuring bouw 1 punt 8): raster 3 x 3 over drie bladen met Mila's dieren als data.
// Gevonden dieren in eigen kleuren met witte stickerrand, de rest als silhouet met kenmerk. Bovenaan "sea log" en
// "8 of 24", onderaan naam en eerlijk wat er nog nodig is, daaronder drie bladstippen. Omhoog en omlaag (of vegen)
// verschuift de keuze; select kiest een gevonden dier dat met je meezwemt.
// Keuring bouw 3 punt 8 en 9: maten van een dier uit zijn eigen punten, zodat het in een vak past.
module EbbDierMaat {
    // [links, rechts, boven, onder] in 1/SCHAAL van de diermaat.
    function grenzen(i as Number) as Array<Number> {
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
