import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// PROEF krabwereld v2.2 (zie KrabV2.mc): de lagen die stil staan, per beurt één. Kleuren en plekken uit Mila's
// bron/werelden_v21.py. AMOLED: verloop in 20 stroken, licht en gloed in drie vaste mengtinten (geen vervaging).
// MIP: vlakken uit de 64 kleuren, onder water bovenin een raster van 0055AA en 005555, geen lichtbundel.
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

    function vierhoek(v as KrabV2View, dc as Graphics.Dc, x0 as Number, y0 as Number, x1 as Number, y1 as Number, x2 as Number, y2 as Number, x3 as Number, y3 as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        pts.add([x0, y0]);
        pts.add([x1, y1]);
        pts.add([x2, y2]);
        pts.add([x3, y3]);
        dc.fillPolygon(pts);
        v.punten += 4;
    }

    // Raster van 1 px uit twee kleuren (MIP, tussentint) van y 0 tot onder: één strook van twee regels als plaatje,
    // daarna regel voor regel geplakt. Lukt het strookje niet, dan een vlak in de eerste kleur.
    function raster(v as KrabV2View, dc as Graphics.Dc, a as Number, b as Number, onder as Number) as Void {
        var w = dc.getWidth();
        v.kleur(dc, a);
        dc.fillRectangle(0, 0, w, onder);
        try {
            var ref = Graphics.createBufferedBitmap({:width => w, :height => 2});
            var bb = ref.get();
            if (bb != null) {
                var t = (bb as Graphics.BufferedBitmap).getDc();
                t.setColor(a, a);
                t.clear();
                t.setColor(b, b);
                for (var x = 0; x < w; x += 2) {
                    t.drawPoint(x, 0);
                    t.drawPoint(x + 1, 1);
                }
                for (var y = 0; y < onder; y += 2) {
                    dc.drawBitmap(0, y, bb as Graphics.BufferedBitmap);
                }
            }
        } catch (e instanceof Lang.Exception) {
            System.println("KRABV2 raster mislukt");
        }
    }

    // Boven water (in, uit, Calm): lucht met zon of maan, wolkje, meeuw, kam met schuim op hoogte top, twee golfrijen,
    // ver weg de andere slipper van het paar.
    function boven(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, top as Number) as Void {
        var l0 = nacht ? 0x000055 : 0x0055AA;
        var l1 = nacht ? 0x0000AA : 0x00AAFF;
        // Mila v3: kam en twee golfrijen eronder (drie of vier rijen was te veel punten per beurt)
        var rijY = [top, top + 34, top + 66] as Array<Number>;
        var rijA = [4.0, 3.0, 3.5] as Array<Float>;
        var rijN = [2, 4, 3] as Array<Number>;
        var rijF = [1.2, 0.3, 2.0] as Array<Float>;
        var kl = (am ? (nacht ? [0x004B96, 0x002D73, 0x000F4B] : [0x0055AF, 0x00378C, 0x001E64])
            : (nacht ? [0x0000AA, 0x000055, 0x000055] : [0x0055AA, 0x0000AA, 0x000055])) as Array<Number>;
        if (stap == 0) {
            if (am) {
                verloop(v, dc, 0, top + 6, l0, l1);
            } else {
                v.kleur(dc, l0);
                dc.fillRectangle(0, 0, dc.getWidth(), v.q(top + 6));
                if (!nacht) {
                    v.golf(dc, top - 28, top + 6, 0x0055FF, 2.5, 2, 0.0);
                }
            }
            if (nacht) {
                var st = [56, 50, 204, 44, 222, 82, 34, 100, 184, 24, 96, 20, 238, 110] as Array<Number>;
                v.kleur(dc, 0xFFFFFF);
                for (var i = 0; i < 7; i += 1) {
                    dc.fillCircle(v.q(st[2 * i]), v.q(st[2 * i + 1]), v.q(0.9) < 1 ? 1 : v.q(0.9));
                }
                v.rondje(dc, 40, 84, 13, 13, 0xFFFFAA, 0xAAAAFF, -1);
                v.rondje(dc, 47, 82, 11, 12, am ? 0x001978 : l0, -1, -1);
            } else {
                if (am) {
                    v.gloed(dc, 40, 86, 20, 20, 0xFFFFAA, 34, 0x0080D0);
                }
                v.rondje(dc, 40, 86, 14, 14, 0xFFFF55, 0xFFFFFF, 0xFFFFFF);
            }
            // wolkje rechts (bij nacht donker) en overdag een meeuw
            var wo = [214, 70, 14, 8, 226, 64, 12, 10, 236, 72, 11, 7] as Array<Number>;
            for (var ronde = 0; ronde < 2; ronde += 1) {
                var wk = (ronde == 0) ? (nacht ? 0x0000AA : 0xAAFFFF) : (nacht ? 0x5555AA : 0xFFFFFF);
                for (var i = 0; i < 3; i += 1) {
                    v.rondje(dc, wo[4 * i], wo[4 * i + 1] - ronde, wo[4 * i + 2] - 2 * ronde, wo[4 * i + 3] - 1.5 * ronde, wk, -1, -1);
                }
            }
            if (!nacht) {
                dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(v.q(1.8) < 2 ? 2 : v.q(1.8));
                for (var sg = -1; sg <= 1; sg += 2) {
                    dc.drawLine(v.q(62), v.q(54), v.q(62 + sg * 5), v.q(50));
                    dc.drawLine(v.q(62 + sg * 5), v.q(50), v.q(62 + sg * 9), v.q(53));
                }
                dc.setPenWidth(1);
            }
        } else if (stap == 1 || stap == 2) {
            if (stap == 1) {
                v.golf(dc, top - 3, 262, 0xFFFFFF, 4.0, 2, 1.2);
                v.golf(dc, top, 262, kl[0], 4.0, 2, 1.2);
            }
            for (var k = 2 * stap - 1; k <= 2 * stap && k < 3; k += 1) {
                v.golf(dc, rijY[k] - 1.6, 262, nacht ? 0x5555FF : 0x55AAFF, rijA[k], rijN[k], rijF[k]);
                v.golf(dc, rijY[k], 262, kl[k], rijA[k], rijN[k], rijF[k]);
            }
            if (stap == 2) {
                KrabV2Vonk.opWater(v, dc, top, nacht);
            }
        } else if (stap == 3) {
            // de grap: ver weg op de kam drijft de andere slipper van het paar
            var zx = 72.0;
            var zy = top - 2.0;
            var k = 2.4;
            var p = [zx - 7 * k, zy, zx - 4 * k, zy - 2.6 * k, zx + 3 * k, zy - 2.2 * k, zx + 8 * k, zy - 0.4 * k, zx + 3 * k, zy + 1.2 * k, zx - 4 * k, zy + 1.2 * k] as Array<Float>;
            v.blob(dc, p, 0xFF55AA, 0xFFFFFF, 1.4);
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(v.q(1.8) < 2 ? 2 : v.q(1.8));
            dc.drawLine(v.q(zx + 4 * k), v.q(zy - k), v.q(zx - k), v.q(zy - 2.4 * k));
            dc.drawLine(v.q(zx + 4 * k), v.q(zy - k), v.q(zx - k), v.q(zy + 0.3 * k));
            dc.fillCircle(v.q(zx + 4 * k), v.q(zy - k), v.q(1.6) < 1 ? 1 : v.q(1.6));
            dc.setPenWidth(1);
        }
    }

    // Onder water (inhouden 3, menu 4, eindscherm 5).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var zeeTop = nacht ? 0x000069 : 0x00698C;
        var licht = nacht ? 0xAAAAFF : 0x55FFFF;
        var eind = (scherm == 5);
        var zak = eind ? 22 : 0;
        if (stap == 0) {
            if (am) {
                verloop(v, dc, 0, 260, zeeTop, nacht ? 0x000016 : 0x00163C);
            } else {
                if (nacht) {
                    v.kleur(dc, 0x000055);
                    dc.fillRectangle(0, 0, dc.getWidth(), dc.getHeight());
                } else {
                    raster(v, dc, 0x005555, 0x0055AA, v.q(eind ? 152 : 148));
                    v.golf(dc, eind ? 146 : 142, 262, 0x000055, 3.0, 2, 1.0);
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
                    v.gloed(dc, 88, 5, 22, 17, 0xC8C8FF, 60, zeeTop);
                } else {
                    v.rondje(dc, 88, 6, 24, 12, 0x5555FF, -1, -1);
                    v.rondje(dc, 88, 5, 14, 7, 0xAAAAFF, -1, -1);
                }
            }
            if (am) {
                var xo = eind ? 184 : 118;
                var xh = eind ? 186 : 112;
                var yh = eind ? 164 : 236;
                var basis = nacht ? 0x000040 : 0x004060;
                // Mila v3.2 (a): boven de onderste tekstregel (kap) één zwakke tint, zodat wit daar 4,5 op 1 haalt
                var kap = eind ? 72 : 140;
                var t = kap / (yh * 1.0);
                var bx = xo + (xh - xo) * t;
                for (var i = 0; i < 4; i += 1) {
                    var f = (i == 3) ? 1.45 : 1.45 - 0.25 * i;
                    var a = (i == 3) ? (nacht ? 18 : 26) : (nacht ? 20 : 33);
                    var bw = (26 + 22 * t) * f;
                    v.glas(dc, a, licht, (i == 3) ? zeeTop : EbbTeken.meng(basis, licht, a * i / 255.0));
                    if (i == 3) {
                        vierhoek(v, dc, v.q(xo - 26 * f), 0, v.q(xo + 26 * f), 0, v.q(bx + bw), v.q(kap), v.q(bx - bw), v.q(kap));
                    } else {
                        vierhoek(v, dc, v.q(bx - bw), v.q(kap), v.q(bx + bw), v.q(kap), v.q(xh + 48 * f), v.q(yh), v.q(xh - 48 * f), v.q(yh));
                    }
                }
            }
        } else if (stap == 1) {
            var ver = am ? (nacht ? 0x00003C : 0x001E46) : (nacht ? 0x0000AA : 0x000055);
            var verder = am ? EbbTeken.meng(ver, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA); // nacht MIP: geen zwart (keuring 04:05 punt 3)
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
                v.gloed(dc, 124, 234, 36, 8, 0xFFFFFF, 46, 0xEBE196);
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
            // zwevende lichtjes (dag) of plankton (nacht), alleen opzij; bellen; op het eindscherm feest en het belletje
            var pl = (nacht ? [22, 112, 34, 138, 16, 158, 48, 120, 232, 104, 244, 132, 220, 146, 208, 118, 60, 150, 196, 156, 30, 92, 236, 84]
                : [20, 150, 36, 146, 240, 152, 242, 140, 214, 152, 18, 160, 30, 92, 230, 92, 44, 136, 216, 136]) as Array<Number>;
            for (var i = 0; i < pl.size() / 2; i += 1) {
                if (am && nacht) {
                    v.glas(dc, 66, 0x00FFAA, 0x000040);
                    dc.fillCircle(v.q(pl[2 * i]), v.q(pl[2 * i + 1]), v.q(3));
                }
                v.kleur(dc, nacht ? (am ? 0xAAFFAA : 0x55FFAA) : 0xAAFFFF);
                dc.fillCircle(v.q(pl[2 * i]), v.q(pl[2 * i + 1]), v.q(1.2) < 1 ? 1 : v.q(1.2));
            }
            var bl = (eind ? [40, 96, 3, 52, 82, 2, 224, 168, 2] : (scherm == 3 ? [192, 160, 3, 198, 148, 2] : [])) as Array<Number>;
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            for (var i = 0; i < bl.size() / 3; i += 1) {
                dc.drawCircle(v.q(bl[3 * i]), v.q(bl[3 * i + 1]), v.q(bl[3 * i + 2]));
            }
            if (!nacht) {
                dc.setColor(0xAAFFFF, Graphics.COLOR_TRANSPARENT);
                dc.drawCircle(v.q(26), v.q(132), v.q(2.6));
                dc.drawCircle(v.q(234), v.q(128), v.q(2.2));
            }
            if (eind) {
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
                if (am) {
                    v.gloed(dc, 184, 122, 35, 29, licht, 40, zeeTop);
                }
                // belletje van de sea log: vlak 0055AA, rand 00FFFF, glimpje
                v.rondje(dc, 184, 122, am ? 40.2 : 42.4, am ? 35.2 : 37.4, 0x00FFFF, -1, -1);
                v.rondje(dc, 184, 122, 40, 35, 0x0055AA, -1, -1);
                v.rondje(dc, 159, 104.5, 4, 4, 0xFFFFFF, -1, -1);
                // roze hartje tussen de krab en zijn nieuwe vriend
                var hart = [] as Array<Float>;
                for (var i = 0; i < 20; i += 1) {
                    var t = i / 20.0 * 2.0 * Math.PI;
                    var sn = Math.sin(t);
                    hart.add((126 + 6 * sn * sn * sn).toFloat());
                    hart.add((108 - (5 * Math.cos(t) - 2 * Math.cos(2 * t) - Math.cos(3 * t))).toFloat());
                }
                v.blob(dc, hart, 0xFF55AA, 0xFFFFFF, 1.6);
            }
        }
    }
}
