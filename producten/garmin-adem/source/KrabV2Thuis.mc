import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF thuiswater (Mila, ontwerp/garmin/ebb-onderwater-v1.md, 12 nov 04:40 UTC): de onderwaterachtergrond voor
// startscherm, pauze en sea log. Zelfde water en oppervlak als inhouden maar zonder lichtbundel, met een lage bodem:
// twee verre ruggen, zandrand met witte lijn, twee kiezels, links en rechts een pluk kelp. y is de hoogte van de
// bodem in 1/260 (start 214, pauze 226, sea log 222). Per beurt één laag, zoals de werelden.
module KrabV2Thuis {
    function laag(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, y as Number) as Void {
        if (stap == 0) {
            KrabV2Lagen.onder(v, dc, 0, am, nacht, 4);
        } else if (stap == 1) {
            var zeeTop = nacht ? 0x000069 : 0x00698C;
            var ver = am ? EbbTeken.meng(nacht ? 0x00003C : 0x001E46, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA);
            v.rondje(dc, 30, y + 4, 70, 22, ver, -1, -1);
            v.rondje(dc, 230, y, 64, 26, ver, -1, -1);
            v.golf(dc, y + 10, 262, nacht ? 0x5555AA : 0xFFFFAA, 2.0, 2, 0.6);
            v.pen(dc, 0xFFFFFF);
            dc.setPenWidth(v.q(1.2) < 1 ? 1 : v.q(1.2));
            for (var x = 0; x < 260; x += 10) {
                dc.drawLine(v.q(x), v.q(y + 10 + 2.0 * Math.sin(x / 260.0 * 4.0 * Math.PI + 0.6)), v.q(x + 10), v.q(y + 10 + 2.0 * Math.sin((x + 10) / 260.0 * 4.0 * Math.PI + 0.6)));
            }
            dc.setPenWidth(1);
            var ki = [96.0, 22.0, 3.5, 168.0, 20.0, 2.6] as Array<Float>;
            for (var i = 0; i < 2; i += 1) {
                v.rondje(dc, ki[3 * i], y + ki[3 * i + 1], ki[3 * i + 2] * 1.3 + 1, ki[3 * i + 2] + 1, 0xFFFFFF, -1, -1);
                v.rondje(dc, ki[3 * i], y + ki[3 * i + 1], ki[3 * i + 2] * 1.3, ki[3 * i + 2], 0xAAAA55, -1, -1);
            }
        } else if (stap == 2) {
            // kelp: drie sprieten per kant, licht slingerend, met een bolletje bovenop
            var sp = [0, 46, 8, 34, -7, 28] as Array<Number>;
            var w = v.q(4) < 2 ? 2 : v.q(4);
            for (var kant = -1; kant <= 1; kant += 2) {
                var x0 = (kant == 1) ? 32 : 230;
                for (var i = 0; i < 3; i += 1) {
                    var xa = (x0 + sp[2 * i]).toFloat();
                    var ya = (y + 12).toFloat();
                    v.pen(dc, 0x00AA55);
                    dc.setPenWidth(w);
                    for (var t = 3; t < sp[2 * i + 1]; t += 3) {
                        var xb = (x0 + sp[2 * i] + kant * 5.0 * Math.sin(t / 10.0)).toFloat();
                        var yb = (y + 12 - t).toFloat();
                        dc.drawLine(v.q(xa), v.q(ya), v.q(xb), v.q(yb));
                        xa = xb;
                        ya = yb;
                    }
                    dc.setPenWidth(1);
                    v.rondje(dc, xa, ya, 2.4, 2.4, 0x55FFAA, -1, -1);
                }
            }
        } else if (stap == 3) {
            KrabV2Lagen.onder(v, dc, 3, am, nacht, 4);
            // startscherm: twee belletjes boven het eigen dier
            // v1.1: je vriend blaast twee belletjes en de bovenste is een roze hartje op (166, 150): hij wacht op je
            if (KrabV2Tekst.vrij(v, 166, 150, 6)) {
                var hart = [] as Array<Float>;
                for (var i = 0; i < 12; i += 1) {
                    var t = i * Math.PI / 6;
                    var sn = Math.sin(t);
                    hart.add((166 + 0.3 * 16 * sn * sn * sn).toFloat());
                    hart.add((150 - 0.3 * (13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t))).toFloat());
                }
                v.blob(dc, hart, 0xFF55AA, 0xFFFFFF, 1.4);
            }
            var bl = [152.0, 170.0, 2.2] as Array<Float>;
            v.pen(dc, 0xAAFFFF);
            for (var i = 0; i < 1; i += 1) {
                if (KrabV2Tekst.vrij(v, bl[3 * i], bl[3 * i + 1], bl[3 * i + 2])) {
                    dc.drawCircle(v.q(bl[3 * i]), v.q(bl[3 * i + 1]), v.q(bl[3 * i + 2]) < 2 ? 2 : v.q(bl[3 * i + 2]));
                }
            }
        }
    }
}
