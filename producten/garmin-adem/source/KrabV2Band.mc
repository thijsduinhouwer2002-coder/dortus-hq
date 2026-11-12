import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// De krab zit in een rood-witte zwemband (Mila, ontwerp/garmin/ebb-krab-keuring2-antwoord.md en
// bron/krab_keuring2.py; besluit hoofdchat 12 nov 06:00 NL). Vervangt de slipper en het V-bandje. v.sl is nog
// steeds x, y, schaal en hoek van de oude slipper; de band draait 0,4 keer die hoek mee. Achterhelft eerst (in het
// plaatje), dan de krab, dan de voorhelft: zo zit hij er echt in. Maten in 1/260: rx 23, ry 8,5, buis 6,5.
module KrabV2Band {
    function r(v as KrabV2View, x as Float, y as Float) as Array<Float> {
        var a = Math.toRadians(v.sl[3] * 0.4);
        var c = Math.cos(a);
        var s = Math.sin(a);
        var k = v.sl[2] * 1.05;
        return [(v.sl[0] - 4.0 * v.sl[2] + (x * c - y * s) * k).toFloat(), (v.sl[1] - 3.0 * v.sl[2] + (x * s + y * c) * k).toFloat()] as Array<Float>;
    }

    // Stuk van de band tussen hoek a0 en a1 (graden, 0 rechts, 90 voor), n stappen per boog, zak lager.
    function stuk(v as KrabV2View, a0 as Float, a1 as Float, n as Number, zak as Float) as Array<Float> {
        var p = [] as Array<Float>;
        for (var i = 0; i <= n; i += 1) {
            var a = Math.toRadians(a0 + (a1 - a0) * i / n);
            var pt = r(v, (26.25 * Math.cos(a)).toFloat(), (11.75 * Math.sin(a)).toFloat());
            p.add(pt[0]);
            p.add(pt[1] + zak);
        }
        for (var i = 0; i <= n; i += 1) {
            var a = Math.toRadians(a1 - (a1 - a0) * i / n);
            var pt = r(v, (19.75 * Math.cos(a)).toFloat(), (5.25 * Math.sin(a)).toFloat());
            p.add(pt[0]);
            p.add(pt[1] + zak);
        }
        return p;
    }

    // voor false: de acht stukken achter de krab. voor true: donkere onderkant, de acht stukken voor de krab en
    // een wit glimlijntje links van het midden.
    function teken(v as KrabV2View, dc as Graphics.Dc, voor as Boolean) as Void {
        var a0 = voor ? 0.0 : 180.0;
        if (voor) {
            v.blob(dc, stuk(v, 0.0, 180.0, 8, 2.2 * v.sl[2] * 1.05), 0xAA0000, -1, 0.0);
        }
        for (var i = 0; i < 8; i += 1) {
            var aa = a0 + i * 22.5;
            v.blob(dc, stuk(v, aa, aa + 23.1, 2, 0.0), (i % 2 == 0) ? 0xFF0000 : 0xFFFFFF, -1, 0.0);
        }
        if (voor) {
            v.pen(dc, 0xFFFFFF);
            var w = v.q(1.4);
            dc.setPenWidth(w < 1 ? 1 : w);
            var vorig = r(v, -14.0, 6.1);
            for (var t = 2; t <= 8; t += 2) {
                var nu = r(v, -14.0 + t, 6.1 + 0.02 * t * t);
                dc.drawLine(v.q(vorig[0]), v.q(vorig[1]), v.q(nu[0]), v.q(nu[1]));
                vorig = nu;
            }
            dc.setPenWidth(1);
        }
    }
}
