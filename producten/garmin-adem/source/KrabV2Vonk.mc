import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF krabwereld (zie KrabV2.mc): vonkjes op het water onder zon of maan in plaats van een baan van licht
// (Mila v3, bericht 12 nov 02:15 UTC punt 2; de baan was op de fenix 8 een harde trapezium). Overdag drie sterretjes
// met vier punten in lichtgeel (9, 7 en 5 breed op 260, Mila 12 nov 03:45 UTC), bij nacht drie puntjes van 3. Plekken en maten uit bron/werelden_v3.py (zee).
module KrabV2Vonk {
    function opWater(v as KrabV2View, dc as Graphics.Dc, top as Number, nacht as Boolean) as Void {
        var w = [34.0, 9.0, 4.5, 48.0, 17.0, 3.5, 30.0, 26.0, 2.5] as Array<Float>;
        for (var j = 0; j < 3; j += 1) {
            var x = w[3 * j];
            var y = top + w[3 * j + 1];
            var k = w[3 * j + 2];
            if (y < 238.0) {
                if (nacht) {
                    v.rondje(dc, x, y, 1.5, 1.5, 0xFFFFAA, -1, -1);
                } else {
                    var p = [] as Array<Float>;
                    for (var i = 0; i < 8; i += 1) {
                        var a = i * Math.PI / 4.0;
                        var rr = (i % 2 == 0) ? k : k * 0.28;
                        p.add((x + rr * Math.sin(a)).toFloat());
                        p.add((y - rr * Math.cos(a)).toFloat());
                    }
                    v.blob(dc, p, 0xFFFFAA, -1, 0.0);
                }
            }
        }
    }
}
