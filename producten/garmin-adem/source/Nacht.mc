import Toybox.Lang;

// Nachtregel v1.2 van Mila (ontwerp/garmin/ebb-nachtregel-v1.json, besluit hoofdchat 12 nov 06:00 NL): bij nacht
// gaat elke kleur die geen tekst is door deze regel. MIP: elk kanaal een trede omlaag (00 en 55 worden 00, AA wordt
// 55, FF wordt AA) en groen hooguit zo sterk als rood of blauw, of 55. AMOLED: per kanaal 0,7 x 255 x (v/255)^2,
// groen hooguit max(rood, blauw, 80), daarna 30 procent naar grijs. Tekst, paginastipjes en knoprandjes niet.
module EbbNacht {
    function trede(v as Number) as Number {
        var i = (v + 42) / 85;
        return i < 2 ? 0 : (i - 1) * 85;
    }

    function k(c as Number, am as Boolean) as Number {
        var r = (c >> 16) & 0xFF;
        var g = (c >> 8) & 0xFF;
        var b = c & 0xFF;
        var m = 0;
        if (am) {
            r = (7 * r * r + 1274) / 2550;
            g = (7 * g * g + 1274) / 2550;
            b = (7 * b * b + 1274) / 2550;
            m = r > b ? r : b;
            m = m < 80 ? 80 : m;
            g = g > m ? m : g;
            var y = 299 * r + 587 * g + 114 * b;
            r = (7000 * r + 3 * y + 5000) / 10000;
            g = (7000 * g + 3 * y + 5000) / 10000;
            b = (7000 * b + 3 * y + 5000) / 10000;
        } else {
            r = trede(r);
            g = trede(g);
            b = trede(b);
            m = r > b ? r : b;
            m = m < 85 ? 85 : m;
            g = g > m ? m : g;
        }
        return (r << 16) | (g << 8) | b;
    }
}
