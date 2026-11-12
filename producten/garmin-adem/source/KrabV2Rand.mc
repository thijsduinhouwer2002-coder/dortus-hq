import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// Werelden (zie KrabV2.mc), frisse keuring 3 (12 nov 07:35 NL), als regel en meting voor elke wereld.
// Punt 4: een los voorwerp staat minstens 10/260 binnen de ronde rand; raakt het de rand, dan is het NEE en
// wordt de plaatjesrun rood (de workflow zoekt "VEILIG ... NEE").
// Punt 6: nachtwater op MIP is één gedempt blauw (000055) met dunne golflijnen (0000AA), Mila nachtregel v1.3.
module KrabV2Rand {
    const NORM = 10;

    // Meet de omcirkel (x, y, r in 1/260) van een los voorwerp tegen de ronde rand en meldt het in het log.
    function meet(v as KrabV2View, scherm as Number, naam as String, x as Numeric, y as Numeric, r as Numeric) as Void {
        var dx = x - 130.0;
        var dy = y - 130.0;
        var lucht = 130.0 - Math.sqrt(dx * dx + dy * dy) - r;
        System.println("VEILIG wereld " + v.wereld + " scherm " + scherm + " rand " + naam + " lucht " + lucht.format("%.1f") + " van 260, norm " + NORM + (lucht >= NORM - 0.05 ? " ja" : " NEE"));
    }

    // Golflijnen van 1 px over het nachtwater op MIP, van y0 tot y1 (1/260), om de 18; niet door tekst.
    // De kleuren zijn al nachtkleuren en gaan daarom niet nog eens door de nachtregel.
    function nachtwater(v as KrabV2View, dc as Graphics.Dc, y0 as Number, y1 as Number) as Void {
        dc.setColor(0x0000AA, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(1);
        for (var y = y0; y <= y1; y += 18) {
            var px = 0;
            var py = v.q(y + 2.0 * Math.sin(y));
            for (var x = 20; x <= 260; x += 20) {
                var ny = v.q(y + 2.0 * Math.sin(x / 260.0 * 2.0 * Math.PI * 3 + y));
                if (!KrabV2Tekst.raakt(v, x - 10, y, 10)) {
                    dc.drawLine(px, py, v.q(x), ny);
                }
                px = v.q(x);
                py = ny;
            }
        }
    }
}
