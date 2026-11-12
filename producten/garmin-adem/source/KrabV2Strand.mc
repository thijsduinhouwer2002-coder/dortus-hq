import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Gedeelde tekenhulpen voor de strandwerelden van Wout (kreeft, zeehond, zeeotter), letterlijk naar Mila
// (ontwerp/garmin/bron/werelden_v4_strand.py). Maten in 1/260 D. De staaf zelf staat in KrabV2Garnaal.staaf.
module KrabV2Strand {
    const WIT = 0xFFFFFF;
    const ROOD = 0xFF0000;
    const GROEN = 0x00AA55;
    const GROEN_L = 0x55FF55;
    const GROEN_D = 0x005500;
    const HOUT = 0xAA5500;

    // Punten (dx, dy om en om) rond x, y, geschaald met kx en ky.
    function pk(x as Numeric, y as Numeric, kx as Numeric, ky as Numeric, rel as Array<Numeric>) as Array<Float> {
        var p = [] as Array<Float>;
        for (var i = 0; i + 1 < rel.size(); i += 2) {
            p.add((x + rel[i] * kx).toFloat());
            p.add((y + rel[i + 1] * ky).toFloat());
        }
        return p;
    }

    // Lijn door punten (x, y om en om) met dikte b en ronde hoeken.
    function lijn(v as KrabV2View, dc as Graphics.Dc, p as Array<Float>, c as Number, b as Numeric) as Void {
        var w = v.q(b);
        v.kleur(dc, c);
        dc.setPenWidth(w < 1 ? 1 : w);
        var r = v.q(b / 2.0);
        for (var i = 0; i + 1 < p.size(); i += 2) {
            if (i + 3 < p.size()) {
                dc.drawLine(v.q(p[i]), v.q(p[i + 1]), v.q(p[i + 2]), v.q(p[i + 3]));
            }
            if (r >= 1) {
                dc.fillCircle(v.q(p[i]), v.q(p[i + 1]), r);
            }
        }
        dc.setPenWidth(1);
    }

    function rechthoek(v as KrabV2View, dc as Graphics.Dc, x0 as Numeric, y0 as Numeric, x1 as Numeric, y1 as Numeric, c as Number) as Void {
        v.kleur(dc, c);
        var a = v.q(x0 < x1 ? x0 : x1);
        var b = v.q(y0);
        dc.fillRectangle(a, b, v.q(x0 < x1 ? x1 : x0) - a + 1, v.q(y1) - b + 1);
    }

    // Druppel (ruitje) met de punt naar boven.
    function druppel(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric, rand as Number) as Void {
        v.blob(dc, pk(x, y, k, k, [0, -2.6, 1.6, 0.6, 0, 1.8, -1.6, 0.6] as Array<Numeric>), 0x55FFFF, rand, 0.8);
    }

    // Gieter met het handvat in de schaar (cx, cy); tuit naar links, broes linksboven. Geeft de broes terug (x, y, r).
    function gieter(v as KrabV2View, dc as Graphics.Dc, cx as Numeric, cy as Numeric, k as Numeric, g as Number, gl as Number, gd as Number, druppels as Boolean) as Array<Float> {
        var x = cx - 7 * k;
        var y = cy + 18 * k;
        KrabV2Garnaal.staaf(v, dc, x - 6 * k, y - 2 * k, x - 21 * k, y - 15 * k, 3.6 * k, g, WIT, 1.4);
        v.rondje(dc, x - 22.5 * k, y - 16 * k, 4.6 * k, 4.6 * k, gl, WIT, -1);
        // handvat: halve boog boven de bus
        for (var ronde = 0; ronde < 2; ronde += 1) {
            var w = v.q((ronde == 0 ? 5.6 : 3.0) * k);
            v.kleur(dc, ronde == 0 ? WIT : gd);
            dc.setPenWidth(w < 1 ? 1 : w);
            dc.drawArc(v.q(x + 7 * k), v.q(y - 10 * k), v.q(8.5 * k), Graphics.ARC_COUNTER_CLOCKWISE, 0, 180);
        }
        dc.setPenWidth(1);
        v.blob(dc, pk(x, y, k, k, [12, -10, -8, -10, -7, 6, 11, 6] as Array<Numeric>), g, WIT, 1.8);
        rechthoek(v, dc, x - 7.6 * k, y - 4 * k, x + 11.6 * k, y - 1.6 * k, gl);
        var bx = x - 24 * k;
        var by = y - 12 * k;
        if (druppels) {
            var d = [-3, 6, 1, 11, -5, 15, -1, 19] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                druppel(v, dc, bx + d[2 * i] * k * 0.8, by + d[2 * i + 1] * k * 0.8, k, WIT);
            }
        }
        return [(x - 22.5 * k).toFloat(), (y - 16 * k).toFloat(), (6.8 * k).toFloat()] as Array<Float>;
    }

    // Strohoedje met rood bandje (de tuinman). x, y is de onderkant van de bol.
    function strohoed(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        v.rondje(dc, x, y, 19 * k, 4.6 * k, 0xFFFF55, HOUT, -1);
        v.blob(dc, pk(x, y, k, k, [-10, 0, -9, -10, -4, -13, 4, -13, 9, -10, 10, 0] as Array<Numeric>), 0xFFFF55, HOUT, 1.4);
        rechthoek(v, dc, x - 9.6 * k, y - 4.6 * k, x + 9.6 * k, y - 1.4 * k, ROOD);
    }

    // Drijvend eilandje met een stekje in een potje; x, y is de onderkant van het potje.
    function eiland(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        v.rondje(dc, x, y + 3 * k, 17 * k, 5.5 * k, 0xFFFFAA, WIT, -1);
        v.rondje(dc, x, y + 1.4 * k, 14 * k, 3 * k, GROEN_L, -1, -1);
        KrabV2Garnaal.staaf(v, dc, x, y - 7 * k, x, y - 17 * k, 1.8 * k, GROEN_D, -1, 0);
        for (var s = -1; s <= 1; s += 2) {
            v.blob(dc, pk(x, y, k, k, [0, -14, 4 * s, -20, 10 * s, -19, 6 * s, -13.5] as Array<Numeric>), GROEN_L, GROEN_D, 1.2);
        }
        pot(v, dc, x, y, k);
    }

    function pot(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        v.blob(dc, pk(x, y, k, k, [-7, -7, 7, -7, 5, 2, -5, 2] as Array<Numeric>), 0xFF5500, WIT, 1.4);
        rechthoek(v, dc, x - 8 * k, y - 9 * k, x + 8 * k, y - 5.6 * k, HOUT);
    }

    // Bloempotje met een roze bloem (onder water: hier vallen de druppels op).
    function bloempot(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        KrabV2Garnaal.staaf(v, dc, x, y - 6 * k, x, y - 18 * k, 2 * k, GROEN, -1, 0);
        for (var a = 0; a < 5; a += 1) {
            var t = a / 5.0 * 2 * Math.PI;
            v.rondje(dc, x + 4.4 * k * Math.cos(t), y - 21 * k + 4.4 * k * Math.sin(t), 3 * k, 3 * k, 0xFF55AA, -1, -1);
        }
        v.rondje(dc, x, y - 21 * k, 2.6 * k, 2.6 * k, 0xFFFF00, -1, -1);
        v.blob(dc, pk(x, y, k, k, [-9, -6, 9, -6, 6.5, 7, -6.5, 7] as Array<Numeric>), 0xFF5500, WIT, 1.5);
        rechthoek(v, dc, x - 10.5 * k, y - 8.5 * k, x + 10.5 * k, y - 4 * k, HOUT);
    }

    // IJsschots met witte bovenkant.
    function schots(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, b as Numeric, h as Numeric) as Void {
        v.blob(dc, pk(x, y, b, h, [-1, 0, -0.8, -1, 0.7, -1.1, 1, -0.2, 0.85, 0.5, -0.85, 0.5] as Array<Numeric>), 0xAAFFFF, WIT, 1.8);
        v.blob(dc, pk(x, y, b, h, [-0.7, -0.7, 0.55, -0.85, 0.5, -0.45, -0.65, -0.3] as Array<Numeric>), WIT, -1, 0.0);
    }

    // Rood-witte dobber met steeltje.
    function dobber(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        v.rondje(dc, x, y, 5.6 * k, 5.6 * k, ROOD, WIT, -1);
        var p = [] as Array<Float>;
        for (var i = 0; i <= 8; i += 1) {
            var t = i / 8.0 * Math.PI;
            p.add((x + 5.6 * k * Math.cos(t)).toFloat());
            p.add((y + 5.6 * k * Math.sin(t)).toFloat());
        }
        v.blob(dc, p, WIT, -1, 0.0);
        KrabV2Garnaal.staaf(v, dc, x, y - 5 * k, x, y - 10 * k, 2 * k, ROOD, -1, 0);
    }

    // Hengel van hand naar top, met een witte lijn naar de dobber.
    function hengel(v as KrabV2View, dc as Graphics.Dc, hx as Numeric, hy as Numeric, tx as Numeric, ty as Numeric, dx as Numeric, dy as Numeric) as Void {
        KrabV2Garnaal.staaf(v, dc, hx, hy, tx, ty, 3.2, HOUT, WIT, 1.2);
        v.rondje(dc, hx, hy, 3.2, 3.2, 0x555555, WIT, -1);
        lijn(v, dc, [tx.toFloat(), ty.toFloat(), ((tx + dx) / 2.0).toFloat(), ((ty + dy) / 2.0 + 8).toFloat(), dx.toFloat(), (dy - 10).toFloat()] as Array<Float>, WIT, 1.2);
    }

    // Oranje visje dat naar links kijkt.
    function visje(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, k as Numeric) as Void {
        v.blob(dc, pk(x, y, k, k, [6, 0, 12, -5, 12, 5] as Array<Numeric>), 0xFFAA00, WIT, 1.1);
        v.rondje(dc, x, y, 8 * k, 5 * k, 0xFFAA00, WIT, -1);
        v.rondje(dc, x - 4 * k, y - k, 1.3 * k, 1.3 * k, 0x000000, -1, -1);
    }

    // Rode mok warme chocolademelk met een wit hartje en stoom; yb is de onderkant.
    function mok(v as KrabV2View, dc as Graphics.Dc, x as Numeric, yb as Numeric, k as Numeric, stoom as Boolean) as Void {
        var w = 11 * k;
        var h = 22 * k;
        v.rondje(dc, x + w + 2 * k, yb - h * 0.5, 6 * k, 6.5 * k, WIT, -1, -1);
        v.rondje(dc, x + w + 2 * k, yb - h * 0.5, 4.4 * k, 4.9 * k, ROOD, -1, -1);
        v.rondje(dc, x + w + 2 * k, yb - h * 0.5, 2.0 * k, 2.6 * k, 0x000055, -1, -1);
        v.blob(dc, [(x - w).toFloat(), (yb - h).toFloat(), (x + w).toFloat(), (yb - h).toFloat(), (x + w * 0.92).toFloat(), (yb - 2 * k).toFloat(),
            (x + w * 0.7).toFloat(), yb.toFloat(), (x - w * 0.7).toFloat(), yb.toFloat(), (x - w * 0.92).toFloat(), (yb - 2 * k).toFloat()] as Array<Float>, ROOD, WIT, 1.8);
        v.rondje(dc, x, yb - h, w, 3.4 * k, WIT, -1, -1);
        v.rondje(dc, x, yb - h + 0.3 * k, w - 1.8 * k, 2.2 * k, HOUT, -1, -1);
        v.rondje(dc, x - 3 * k, yb - h * 0.55, 2.6 * k, 2.6 * k, WIT, -1, -1);
        v.rondje(dc, x + 3 * k, yb - h * 0.55, 2.6 * k, 2.6 * k, WIT, -1, -1);
        v.blob(dc, [(x - 5.4 * k).toFloat(), (yb - h * 0.5).toFloat(), (x + 5.4 * k).toFloat(), (yb - h * 0.5).toFloat(), x.toFloat(), (yb - h * 0.22).toFloat()] as Array<Float>, WIT, -1, 0.0);
        if (stoom) {
            for (var j = 0; j < 2; j += 1) {
                var p = [] as Array<Float>;
                for (var i = 0; i < 5; i += 1) {
                    p.add((x + (j == 0 ? -4.5 : 4.5) * k + 2.6 * k * Math.sin(i / 6.0 * 2 * Math.PI + j * Math.PI)).toFloat());
                    p.add((yb - h - 5 * k - i * 2.2 * k).toFloat());
                }
                lijn(v, dc, p, WIT, 2.4 * k);
            }
        }
    }

    // Golvend kelplint van onder (x0, y0) naar boven (x1, y1).
    function kelp(v as KrabV2View, dc as Graphics.Dc, x0 as Numeric, y0 as Numeric, x1 as Numeric, y1 as Numeric, buig as Numeric, b as Numeric) as Void {
        var p = [] as Array<Float>;
        for (var i = 0; i < 13; i += 1) {
            var t = i / 12.0;
            p.add((x0 + (x1 - x0) * t + buig * Math.sin(t * Math.PI * 2)).toFloat());
            p.add((y0 + (y1 - y0) * t).toFloat());
        }
        lijn(v, dc, p, 0xAAFF55, b + 2.4);
        lijn(v, dc, p, 0x55AA00, b);
    }

    // Staat een cirkel (x, y, r) ruim binnen de ronde rand (10/260)?
    function binnen(x as Numeric, y as Numeric, r as Numeric) as Boolean {
        var dx = x - 130.0;
        var dy = y - 130.0;
        return Math.sqrt(dx * dx + dy * dy) + r <= 120.0;
    }
}
