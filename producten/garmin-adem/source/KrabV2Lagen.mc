import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF krabwereld v2 (zie KrabV2.mc): de lagen die stil staan, per beurt één. Kleuren en plekken uit Mila's
// bron/werelden_v2.py. AMOLED: verloop in 20 stroken en doorschijnende vlakken (setFill) in plaats van vervaging.
// MIP: vlakken uit de 64 kleuren, geen lichtbundel.
module KrabV2Lagen {
    function verloop(v as KrabV2View, dc as Graphics.Dc, y0 as Number, y1 as Number, k0 as Number, k1 as Number) as Void {
        var n = 20;
        for (var i = 0; i < n; i += 1) {
            var a = v.q(y0 + (y1 - y0) * i / n);
            var b = v.q(y0 + (y1 - y0) * (i + 1) / n);
            v.kleur(dc, EbbTeken.meng(k0, k1, i / (n - 1.0)));
            dc.fillRectangle(0, a, dc.getWidth(), b - a + 1);
        }
    }

    // Boven water (inademen): lucht met zon of maan, kam met schuim, vier golfrijen, baan van licht.
    function boven(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean) as Void {
        var top = 132;
        var l0 = nacht ? 0x000055 : 0x0055AA;
        var l1 = nacht ? 0x0000AA : 0x00AAFF;
        var rijY = [top, top + 34, top + 66, top + 98] as Array<Number>;
        var rijA = [4.0, 3.0, 3.5, 4.0] as Array<Float>;
        var rijN = [2, 4, 3, 2] as Array<Number>;
        var rijF = [1.2, 0.3, 2.0, 0.8] as Array<Float>;
        var kl = (am ? (nacht ? [0x001496, 0x000A78, 0x00005F, 0x000046] : [0x0055AF, 0x004196, 0x002D7D, 0x001C5F])
            : (nacht ? [0x0000AA, 0x0000AA, 0x000055, 0x000055] : [0x0055AA, 0x0055AA, 0x0000AA, 0x0000AA])) as Array<Number>;
        if (stap == 0) {
            if (am) {
                verloop(v, dc, 0, top + 6, l0, l1);
            } else {
                v.kleur(dc, l0);
                dc.fillRectangle(0, 0, dc.getWidth(), v.q(top + 6));
                v.golf(dc, 104, top + 6, l1, 2.5, 2, 0.0);
            }
            if (nacht) {
                var st = [56, 50, 204, 44, 222, 82, 34, 100, 184, 24, 96, 20, 238, 110] as Array<Number>;
                v.kleur(dc, 0xFFFFFF);
                for (var i = 0; i < 7; i += 1) {
                    dc.fillCircle(v.q(st[2 * i]), v.q(st[2 * i + 1]), v.q(0.9) < 1 ? 1 : v.q(0.9));
                }
                v.rondje(dc, 40, 102, 13, 13, 0xFFFFAA, 0xAAAAFF, -1);
                v.rondje(dc, 47, 100, 11, 12, am ? 0x001978 : l1, -1, -1);
            } else {
                v.rondje(dc, 40, 104, 14, 14, 0xFFFF55, 0xFFFFFF, 0xFFFFFF);
            }
            v.golf(dc, top - 3, 262, 0xFFFFFF, 4.0, 2, 1.2);
            v.golf(dc, top, 262, kl[0], 4.0, 2, 1.2);
        } else if (stap == 1 || stap == 2) {
            for (var k = 2 * stap - 1; k <= 2 * stap && k < 4; k += 1) {
                v.golf(dc, rijY[k] - 1.6, 262, nacht ? 0x5555FF : 0x55AAFF, rijA[k], rijN[k], rijF[k]);
                v.golf(dc, rijY[k], 262, kl[k], rijA[k], rijN[k], rijF[k]);
            }
        } else if (stap == 3) {
            var gl = nacht ? 0xAAAAFF : 0xFFFFAA;
            if (am) {
                v.glas(dc, 70, gl);
                v.vierhoek(dc, v.q(28), v.q(top + 4), v.q(52), v.q(top + 4), v.q(44), v.q(top + 52), v.q(36), v.q(top + 52));
            }
            var vk = [34, 9, 9, 47, 11, 7, 40, 18, 10, 33, 26, 5, 45, 29, 6, 39, 37, 5, 42, 46, 3] as Array<Number>;
            v.kleur(dc, gl);
            for (var i = 0; i < 7; i += 1) {
                var b = vk[3 * i + 2];
                var h = v.q(2.2) < 2 ? 2 : v.q(2.2);
                dc.fillRoundedRectangle(v.q(vk[3 * i] - b / 2.0), v.q(top + vk[3 * i + 1]), v.q(b), h, h / 2);
            }
        }
    }

    // Onder water (inhouden 1, menu 2, eindscherm 3).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var zeeTop = nacht ? 0x000069 : 0x00698C;
        var licht = nacht ? 0xAAAAFF : 0x55FFFF;
        var eind = (scherm == 3);
        var zak = eind ? 22 : 0;
        if (stap == 0) {
            if (am) {
                verloop(v, dc, 0, 260, zeeTop, nacht ? 0x000016 : 0x00163C);
            } else {
                v.kleur(dc, nacht ? 0x000055 : 0x005555);
                dc.fillRectangle(0, 0, dc.getWidth(), dc.getHeight());
                if (!nacht) {
                    v.golf(dc, 150, 262, 0x000055, 2.5, 2, 0.0);
                }
            }
            // oppervlak: lichte golvende rand bovenin
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var x = 0; x <= 260; x += 10) {
                pts.add([v.q(x), v.q(7 + 2.5 * Math.sin(x / 260.0 * 2.0 * Math.PI * 5))]);
            }
            pts.add([v.q(260), 0]);
            pts.add([0, 0]);
            v.kleur(dc, am ? EbbTeken.meng(licht, zeeTop, 0.5) : (nacht ? 0x5555FF : 0x0055FF));
            dc.fillPolygon(pts);
            v.punten += pts.size();
            if (nacht) {
                if (am) {
                    v.glas(dc, 70, 0xC8C8FF);
                    dc.fillEllipse(v.q(88), v.q(5), v.q(30), v.q(22));
                    v.glas(dc, 80, 0xC8C8FF);
                    dc.fillEllipse(v.q(88), v.q(5), v.q(18), v.q(13));
                } else {
                    v.rondje(dc, 88, 6, 24, 12, 0x5555FF, -1, -1);
                    v.rondje(dc, 88, 5, 14, 7, 0xAAAAFF, -1, -1);
                }
            }
            if (am) {
                // lichtbundel in drie doorschijnende stappen (vervagen kan het horloge niet)
                var xo = eind ? 104 : 118;
                var xh = eind ? 104 : 112;
                var yh = eind ? 170 : 236;
                for (var i = 0; i < 3; i += 1) {
                    var f = 1.0 - 0.3 * i;
                    v.glas(dc, nacht ? 18 : 28, licht);
                    v.vierhoek(dc, v.q(xo - 26 * f), 0, v.q(xo + 26 * f), 0, v.q(xh + 48 * f), v.q(yh), v.q(xh - 48 * f), v.q(yh));
                }
            }
        } else if (stap == 1) {
            var ver = am ? (nacht ? 0x00003C : 0x001E46) : (nacht ? 0x0000AA : 0x000055);
            var verder = am ? EbbTeken.meng(ver, zeeTop, 0.5) : (nacht ? 0x000055 : 0x0055AA);
            var r1 = [40, 176, 60, 26, 150, 186, 70, 20, 240, 168, 46, 30] as Array<Number>;
            var r2 = [10, 192, 52, 36, 78, 208, 46, 20, 186, 206, 50, 20, 252, 186, 50, 40] as Array<Number>;
            for (var i = 0; i < 3; i += 1) {
                v.rondje(dc, r1[4 * i], r1[4 * i + 1], r1[4 * i + 2], r1[4 * i + 3], verder, -1, -1);
            }
            for (var i = 0; i < 4; i += 1) {
                v.rondje(dc, r2[4 * i], r2[4 * i + 1], r2[4 * i + 2], r2[4 * i + 3], ver, -1, -1);
            }
            v.rondje(dc, 130, 276, 170, 54, 0xAAAA55, -1, -1);
            v.rondje(dc, 130, 278, 160, 52, am ? 0xEBE196 : 0xFFFFAA, -1, -1);
            if (am) {
                v.glas(dc, 60, 0xFFFFFF);
                dc.fillEllipse(v.q(118), v.q(234), v.q(52), v.q(12));
            }
        } else if (stap == 2) {
            // rots met anemoon (links, in het menu rechts) en rots met zeester
            var sp = (scherm == 2);
            var ady = eind ? 14 : (sp ? 10 : 0);
            var adx = eind ? -8 : 0;
            v.rondje(dc, sp ? 224 : 36, 202 + zak, 34, 26, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            var an = [18, 12, 158, 26, 22, 150, 36, 36, 146, 46, 50, 150, 54, 60, 160] as Array<Number>;
            for (var ronde = 0; ronde < 2; ronde += 1) {
                for (var i = 0; i < 5; i += 1) {
                    var x0 = an[3 * i] + adx;
                    var x1 = an[3 * i + 1] + adx;
                    if (sp) {
                        x0 = 260 - x0;
                        x1 = 260 - x1;
                    }
                    var y1 = an[3 * i + 2] + zak + ady;
                    dc.setColor(ronde == 0 ? 0xFFFFFF : 0xAA55FF, Graphics.COLOR_TRANSPARENT);
                    dc.setPenWidth(v.q(ronde == 0 ? 8.6 : 5.6));
                    dc.drawLine(v.q(x0), v.q(180 + zak), v.q(x1), v.q(y1));
                    v.rondje(dc, x1, y1, ronde == 0 ? 4.3 : 3.6, ronde == 0 ? 4.3 : 3.6, ronde == 0 ? 0xFFFFFF : 0xFF55AA, -1, -1);
                }
            }
            dc.setPenWidth(1);
            var ax = sp ? 260 - 36 - adx : 36 + adx;
            v.rondje(dc, ax, 180 + zak, 23.6, 8.6, 0xFFFFFF, -1, -1);
            v.rondje(dc, ax, 180 + zak, 22, 7, 0xAA55FF, -1, -1);
            var rx = 222 - zak / 3;
            v.rondje(dc, sp ? 260 - rx : rx, 210 + zak, 30, 22, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            var ster = [] as Array<Float>;
            var sx = sp ? 260 - (218 - zak / 3) : 218 - zak / 3;
            for (var i = 0; i < 10; i += 1) {
                var a = -Math.PI / 2 + i * Math.PI / 5;
                var rr = (i % 2 == 0) ? 11.0 : 4.6;
                ster.add((sx + rr * Math.cos(a)).toFloat());
                ster.add((197 + zak + rr * Math.sin(a)).toFloat());
            }
            v.blob(dc, ster, 0xFFFF55, 0xFFFFFF, 1.8);
        } else if (stap == 3) {
            // zwevende lichtjes (dag) of plankton (nacht), alleen opzij; bellen; op het eindscherm feest en lichtkring
            var pl = (nacht ? [22, 112, 34, 138, 16, 158, 48, 120, 232, 104, 244, 132, 220, 146, 208, 118, 60, 150, 196, 156, 30, 92, 236, 84]
                : [24, 120, 36, 146, 230, 112, 242, 140, 214, 152, 18, 160]) as Array<Number>;
            v.kleur(dc, nacht ? (am ? 0xAAFFAA : 0x55FFAA) : 0xAAFFFF);
            for (var i = 0; i < pl.size() / 2; i += 1) {
                dc.fillCircle(v.q(pl[2 * i]), v.q(pl[2 * i + 1]), v.q(1.2) < 1 ? 1 : v.q(1.2));
            }
            var bl = (eind ? [44, 120, 5, 58, 98, 3, 40, 82, 2, 196, 132, 4, 212, 110, 3, 200, 88, 2] : (scherm == 1 ? [192, 160, 3, 198, 148, 2] : [])) as Array<Number>;
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            for (var i = 0; i < bl.size() / 3; i += 1) {
                dc.drawCircle(v.q(bl[3 * i]), v.q(bl[3 * i + 1]), v.q(bl[3 * i + 2]));
            }
            if (eind) {
                var fo = [58, 108, 9, 194, 96, 8, 176, 150, 5, 46, 142, 5] as Array<Number>;
                for (var j = 0; j < 4; j += 1) {
                    var p = [] as Array<Float>;
                    for (var i = 0; i < 8; i += 1) {
                        var a = i * Math.PI / 4;
                        var rr = fo[3 * j + 2] * ((i % 2 == 0) ? 1.0 : 0.28);
                        p.add((fo[3 * j] + rr * Math.sin(a)).toFloat());
                        p.add((fo[3 * j + 1] - rr * Math.cos(a)).toFloat());
                    }
                    v.blob(dc, p, 0xFFFFAA, -1, 0.0);
                }
                if (am) {
                    for (var i = 0; i < 3; i += 1) {
                        v.glas(dc, 30, licht);
                        dc.fillEllipse(v.q(128), v.q(124), v.q(58 - 12 * i), v.q(46 - 10 * i));
                    }
                } else {
                    v.rondje(dc, 128, 124, 59.6, 37.6, nacht ? 0x5555FF : 0x00AAFF, -1, -1);
                    v.rondje(dc, 128, 124, 58, 36, nacht ? 0x0000AA : 0x0055AA, -1, -1);
                }
            }
        }
    }
}
