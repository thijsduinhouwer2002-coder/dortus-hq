import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF krabwereld v2.2 (zie KrabV2.mc): de lagen die stil staan, per beurt één. Kleuren en plekken uit Mila's
// ontwerp/garmin/bron/werelden_v21.py. Niets doorschijnend: AMOLED krijgt een verloop in stroken met de lichtbundel
// per strook in drie vaste mengtinten; MIP krijgt vlakken uit de 64 kleuren en bovenin een raster van 1 px.
module KrabV2Lagen {
    function vierhoek(v as KrabV2View, dc as Graphics.Dc, x0 as Number, y0 as Number, x1 as Number, y1 as Number, x2 as Number, y2 as Number, x3 as Number, y3 as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        pts.add([x0, y0]);
        pts.add([x1, y1]);
        pts.add([x2, y2]);
        pts.add([x3, y3]);
        dc.fillPolygon(pts);
        v.punten += 4;
    }

    function zeeTop(nacht as Boolean) as Number {
        return nacht ? 0x000069 : 0x00698C;
    }

    // Kleur van het water op AMOLED op hoogte y (1/260).
    function water(nacht as Boolean, y as Numeric) as Number {
        return EbbTeken.meng(zeeTop(nacht), nacht ? 0x000016 : 0x00163C, (y / 260.0).toFloat());
    }

    // Lucht op AMOLED: verloop van boven tot de kam.
    function lucht(v as KrabV2View, dc as Graphics.Dc, y1 as Number, k0 as Number, k1 as Number) as Void {
        var n = 20;
        for (var i = 0; i < n; i += 1) {
            var a = v.q(y1 * i / n.toFloat());
            var b = v.q(y1 * (i + 1) / n.toFloat());
            v.kleur(dc, EbbTeken.meng(k0, k1, i / (n - 1.0)));
            dc.fillRectangle(0, a, dc.getWidth(), b - a + 1);
        }
    }

    // Water op AMOLED: verloop in 26 stroken. bundel 0 geen, 1 op de held (inhouden, menu), 2 op de nieuwe vriend (eind).
    // De bundel is per strook drie vlakken, buiten breed en zwak, binnen smal, elk een vaste mengtint van het water.
    function waterAm(v as KrabV2View, dc as Graphics.Dc, nacht as Boolean, bundel as Number) as Void {
        var n = 26;
        var licht = nacht ? 0xAAAAFF : 0x55FFFF;
        var a = nacht ? 0.0795 : 0.1293;
        var xo = (bundel == 2) ? 184.0 : 118.0;
        var xh = (bundel == 2) ? 186.0 : 112.0;
        var yh = (bundel == 2) ? 164.0 : 236.0;
        var kk = [1.45, 1.2, 0.95] as Array<Float>;
        for (var i = 0; i < n; i += 1) {
            var ya = 260.0 * i / n;
            var yb = 260.0 * (i + 1) / n;
            var c = EbbTeken.meng(zeeTop(nacht), nacht ? 0x000016 : 0x00163C, i / (n - 1.0));
            v.kleur(dc, c);
            dc.fillRectangle(0, v.q(ya), dc.getWidth(), v.q(yb) - v.q(ya) + 1);
            if (bundel > 0 && ya < yh) {
                if (yb > yh) {
                    yb = yh;
                }
                var ma = xo + (xh - xo) * ya / yh;
                var mb = xo + (xh - xo) * yb / yh;
                for (var j = 0; j < 3; j += 1) {
                    var ha = (26.0 + 22.0 * ya / yh) * kk[j];
                    var hb = (26.0 + 22.0 * yb / yh) * kk[j];
                    c = EbbTeken.meng(c, licht, a);
                    v.kleur(dc, c);
                    vierhoek(v, dc, v.q(ma - ha), v.q(ya), v.q(ma + ha), v.q(ya), v.q(mb + hb), v.q(yb) + 1, v.q(mb - hb), v.q(yb) + 1);
                }
            }
        }
    }

    // Boven water (inademen, uitademen, Calm): lucht met zon of maan, wolkje, meeuw, kam met schuim, vier golfrijen,
    // ver weg de andere slipper van het paar. top is de hoogte van de kam.
    function boven(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, top as Number) as Void {
        var l0 = nacht ? 0x000055 : 0x0055AA;
        var l1 = nacht ? 0x0000AA : 0x00AAFF;
        var rijY = [top, top + 34, top + 66, top + 98] as Array<Number>;
        var rijA = [4.0, 3.0, 3.5, 4.0] as Array<Float>;
        var rijN = [2, 4, 3, 2] as Array<Number>;
        var rijF = [1.2, 0.3, 2.0, 0.8] as Array<Float>;
        var kl = (am ? (nacht ? [0x004B96, 0x00377D, 0x002364, 0x000F4B] : [0x0055AF, 0x004196, 0x002D7D, 0x001C5F])
            : (nacht ? [0x0000AA, 0x0000AA, 0x000055, 0x000055] : [0x0055AA, 0x0055AA, 0x0000AA, 0x0000AA])) as Array<Number>;
        if (stap == 0) {
            if (am) {
                lucht(v, dc, top + 6, l0, l1);
            } else {
                v.kleur(dc, l0);
                dc.fillRectangle(0, 0, dc.getWidth(), v.q(top + 6));
                if (!nacht) {
                    v.golf(dc, top - 28, top + 6, l1, 2.5, 2, 0.0);
                }
            }
            // kleur van de lucht achter zon en maan (y 84 tot 86)
            var achter = am ? EbbTeken.meng(l0, l1, (85.0 / top).toFloat()) : l0;
            if (nacht) {
                var st = [56, 50, 204, 44, 222, 82, 34, 100, 184, 24, 96, 20, 238, 110] as Array<Number>;
                v.kleur(dc, 0xFFFFFF);
                for (var i = 0; i < 7; i += 1) {
                    dc.fillCircle(v.q(st[2 * i]), v.q(st[2 * i + 1]), v.q(0.9) < 1 ? 1 : v.q(0.9));
                }
                v.rondjeD(dc, 40, 84, 13, 13, 0xFFFFAA, 0xAAAAFF, -1, 1.6);
                v.rondje(dc, 47, 82, 11, 12, achter, -1, -1);
            } else {
                if (am) {
                    v.gloed(dc, 40, 86, 20, 20, achter, 0xFFFFAA, 0.35, 3, 0.35);
                }
                v.rondjeD(dc, 40, 86, 14, 14, 0xFFFF55, 0xFFFFFF, 0xFFFFFF, 2.0);
            }
            // wolkje rechts (bij nacht donker), overdag een meeuw
            var wr = nacht ? 0x0000AA : 0xAAFFFF;
            var wk = nacht ? 0x5555AA : 0xFFFFFF;
            v.rondje(dc, 214, 70, 14, 8, wr, -1, -1);
            v.rondje(dc, 226, 64, 12, 10, wr, -1, -1);
            v.rondje(dc, 236, 72, 11, 7, wr, -1, -1);
            v.rondje(dc, 214, 69, 12, 6.5, wk, -1, -1);
            v.rondje(dc, 226, 63, 10, 8.5, wk, -1, -1);
            v.rondje(dc, 236, 71, 9, 5.5, wk, -1, -1);
            if (!nacht) {
                dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(v.q(1.8) < 2 ? 2 : v.q(1.8));
                for (var sgn = -1; sgn <= 1; sgn += 2) {
                    dc.drawLine(v.q(62), v.q(54), v.q(62 + sgn * 5), v.q(50));
                    dc.drawLine(v.q(62 + sgn * 5), v.q(50), v.q(62 + sgn * 9), v.q(53));
                }
                dc.setPenWidth(1);
            }
            v.golf(dc, top - 3, 262, 0xFFFFFF, 4.0, 2, 1.2);
            v.golf(dc, top, 262, kl[0], 4.0, 2, 1.2);
        } else if (stap == 1 || stap == 2) {
            for (var k = 2 * stap - 1; k <= 2 * stap && k < 4; k += 1) {
                v.golf(dc, rijY[k] - 1.6, 262, nacht ? 0x5555FF : 0x55AAFF, rijA[k], rijN[k], rijF[k]);
                v.golf(dc, rijY[k], 262, kl[k], rijA[k], rijN[k], rijF[k]);
            }
        } else if (stap == 3) {
            // de grap: ver weg op de kam drijft de andere slipper van het paar
            var zx = 76.0;
            var zy = top - 2.0;
            var k = 1.7;
            var p = [zx - 7 * k, zy, zx - 4 * k, zy - 2.6 * k, zx + 3 * k, zy - 2.2 * k, zx + 8 * k, zy - 0.4 * k, zx + 3 * k, zy + 1.2 * k, zx - 4 * k, zy + 1.2 * k] as Array<Float>;
            v.blob(dc, p, 0xFF55AA, 0xFFFFFF, 1.4);
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(v.q(1.4) < 1 ? 1 : v.q(1.4));
            dc.drawLine(v.q(zx + 4 * k), v.q(zy - k), v.q(zx - k), v.q(zy - 2.4 * k));
            dc.drawLine(v.q(zx - k), v.q(zy - 2.4 * k), v.q(zx + 4 * k), v.q(zy + 0.2 * k));
            dc.setPenWidth(1);
        }
    }

    function bellen(v as KrabV2View, dc as Graphics.Dc, bl as Array<Numeric>, k as Number) as Void {
        for (var i = 0; i < bl.size() / 3; i += 1) {
            var r = bl[3 * i + 2];
            dc.setColor(k, Graphics.COLOR_TRANSPARENT);
            dc.drawCircle(v.q(bl[3 * i]), v.q(bl[3 * i + 1]), v.q(r));
            dc.fillCircle(v.q(bl[3 * i] - r * 0.25), v.q(bl[3 * i + 1] - r * 0.35), v.q(r * 0.2) < 1 ? 1 : v.q(r * 0.2));
        }
    }

    // Onder water (inhouden 3, menu 4, eindscherm 5).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var licht = nacht ? 0xAAAAFF : 0x55FFFF;
        var eind = (scherm == 5);
        var zak = eind ? 22 : 0;
        if (stap == 0) {
            if (am) {
                waterAm(v, dc, nacht, eind ? 2 : 1);
            } else {
                // MIP overdag (v2.2): bovenin een raster van 005555 en 0055AA (leest als teal), daaronder vlak 000055
                // vanaf y 142 (eind 146). Het raster zijn schuine lijnen om de 2 px. Nacht: 000055, daaronder zwart.
                var w = dc.getWidth();
                v.kleur(dc, nacht ? 0x000055 : 0x005555);
                dc.fillRectangle(0, 0, w, dc.getHeight());
                var ry = nacht ? 150 : (eind ? 146 : 142);
                if (!nacht) {
                    var h = v.q(ry + 5);
                    dc.setClip(0, 0, w, h);
                    dc.setColor(0x0055AA, Graphics.COLOR_TRANSPARENT);
                    dc.setPenWidth(1);
                    for (var x = -h; x < w; x += 2) {
                        dc.drawLine(x, 0, x + h, h);
                    }
                    dc.clearClip();
                }
                v.golf(dc, ry, 262, nacht ? 0x000000 : 0x000055, 3.0, 2, 1.0);
            }
            // oppervlak: lichte golvende rand bovenin
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var x = 0; x <= 260; x += 10) {
                pts.add([v.q(x), v.q(7 + 2.5 * Math.sin(x / 260.0 * 2.0 * Math.PI * 5))]);
            }
            pts.add([v.q(260), 0]);
            pts.add([0, 0]);
            var rand = am ? EbbTeken.meng(licht, zeeTop(nacht), 0.5) : (nacht ? 0x5555FF : 0x0055FF);
            v.kleur(dc, rand);
            dc.fillPolygon(pts);
            v.punten += pts.size();
            if (nacht) {
                // maanvlek op het oppervlak
                if (am) {
                    v.gloed(dc, 88, 5, 22, 17, water(nacht, 10), 0xC8C8FF, 0.55, 3, 0.35);
                } else {
                    v.rondje(dc, 88, 6, 24, 12, 0x5555FF, -1, -1);
                    v.rondje(dc, 88, 5, 14, 7, 0xAAAAFF, -1, -1);
                }
            }
        } else if (stap == 1) {
            var ver = am ? (nacht ? 0x00003C : 0x001E46) : (nacht ? 0x0000AA : 0x000055);
            var verder = am ? EbbTeken.meng(ver, zeeTop(nacht), 0.5) : (nacht ? 0x000055 : 0x0055AA);
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
                // lichtvlek van de bundel op het zand
                v.gloed(dc, 124, 234, 48, 11, 0xEBE196, 0xFFFFFF, 0.45, 3, 0.35);
            }
        } else if (stap == 2) {
            // rots met anemoon (links, in het menu rechts) en rots met zeester
            var sp = (scherm == 4);
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
            // zwevende lichtjes en bellen (dag) of plankton (nacht), alleen opzij en nooit in de tekstregels
            if (nacht) {
                var pl = [22, 112, 1.6, 34, 138, 1.1, 16, 158, 1.3, 48, 120, 0.9, 232, 104, 1.6, 244, 132, 1.1,
                    220, 146, 1.3, 208, 118, 0.9, 60, 150, 1.0, 196, 156, 1.0, 30, 92, 0.9, 236, 84, 0.9] as Array<Numeric>;
                for (var i = 0; i < pl.size() / 3; i += 1) {
                    var r = pl[3 * i + 2];
                    if (am) {
                        v.gloed(dc, pl[3 * i], pl[3 * i + 1], r * 2.4, r * 2.4, water(nacht, pl[3 * i + 1]), 0x00FFAA, 0.45, 2, 0.5);
                    }
                    v.kleur(dc, am ? 0xAAFFAA : 0x55FFAA);
                    dc.fillCircle(v.q(pl[3 * i]), v.q(pl[3 * i + 1]), v.q(r) < 1 ? 1 : v.q(r));
                }
            } else {
                var st = [20, 150, 1.1, 36, 146, 0.8, 240, 152, 1.1, 242, 140, 0.8, 214, 152, 0.7, 18, 160, 0.7,
                    30, 92, 1.0, 230, 92, 1.0, 44, 136, 0.8, 216, 136, 0.8] as Array<Numeric>;
                v.kleur(dc, 0xAAFFFF);
                for (var i = 0; i < st.size() / 3; i += 1) {
                    var r = st[3 * i + 2] * (am ? 1.0 : 1.3);
                    dc.fillCircle(v.q(st[3 * i]), v.q(st[3 * i + 1]), v.q(r) < 1 ? 1 : v.q(r));
                }
                bellen(v, dc, [26, 132, 2.6, 234, 128, 2.2] as Array<Numeric>, 0xAAFFFF);
            }
            if (scherm == 3) {
                bellen(v, dc, [192, 160, 3, 198, 148, 2.2] as Array<Numeric>, 0xFFFFFF);
            }
            if (eind) {
                bellen(v, dc, [40, 96, 2.6, 52, 82, 1.8, 224, 168, 2.4] as Array<Numeric>, 0xFFFFFF);
                var fo = [226, 82, 8, 146, 86, 5, 236, 146, 5] as Array<Number>;
                for (var j = 0; j < 3; j += 1) {
                    var p = [] as Array<Float>;
                    for (var i = 0; i < 8; i += 1) {
                        var a = i * Math.PI / 4;
                        var rr = fo[3 * j + 2] * ((i % 2 == 0) ? 1.0 : 0.28);
                        p.add((fo[3 * j] + rr * Math.sin(a)).toFloat());
                        p.add((fo[3 * j + 1] - rr * Math.cos(a)).toFloat());
                    }
                    v.blob(dc, p, 0xFFFFAA, -1, 0.0);
                }
                // de nieuwe vriend in een belletje in de stijl van de sea log, op AMOLED met een lichtkring erachter
                if (am) {
                    v.gloed(dc, 184, 122, 35.2, 28.6, water(nacht, 122), licht, 0.4, 3, 0.35);
                }
                v.rondjeD(dc, 184, 122, 40, 35, 0x0055AA, 0x00FFFF, -1, 2.4);
                v.rondje(dc, 184 - 24.8, 122 - 17.5, 4, 4, 0xFFFFFF, -1, -1);
                // roze hartje tussen de krab en zijn nieuwe vriend
                var hart = [] as Array<Float>;
                for (var i = 0; i < 20; i += 1) {
                    var t = i / 20.0 * 2.0 * Math.PI;
                    var s3 = Math.sin(t);
                    hart.add((126 + 6 * s3 * s3 * s3).toFloat());
                    hart.add((108 - (5 * Math.cos(t) - 2 * Math.cos(2 * t) - Math.cos(3 * t))).toFloat());
                }
                v.blob(dc, hart, 0xFF55AA, 0xFFFFFF, 1.6);
            }
        }
    }
}
