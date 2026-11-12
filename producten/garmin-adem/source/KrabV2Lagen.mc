import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// PROEF krabwereld v2.2 (zie KrabV2.mc): de lagen onder water die stil staan, per beurt één (boven water: KrabV2Boven.mc). Kleuren en plekken uit Mila's
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
                t.setColor(v.nk(a), v.nk(a));
                t.clear();
                t.setColor(v.nk(b), v.nk(b));
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

    // Onder water (inhouden 3, menu 4, eindscherm 5).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var zeeTop = nacht ? 0x000069 : 0x00698C;
        var licht = nacht ? 0xAAAAFF : 0x55FFFF;
        var eind = (scherm == 5);
        // Laag 1 tot 3 is van de wereld zelf (KrabV2Werelden.mc); in laag 3 komt daarna wat elke wereld deelt.
        if (stap >= 1 && stap <= 3) {
            v.w().onder(v, dc, stap, am, nacht, scherm);
            if (stap < 3) {
                return;
            }
        }
        if (stap == 0) {
            if (am) {
                verloop(v, dc, 0, 260, zeeTop, nacht ? 0x000016 : 0x00163C);
            } else {
                if (nacht) {
                    // Mila nachtregel v1.3 (mip_nachtwater): één gedempt blauw met golflijnen, geen blokken
                    // Keuring 4 punt 2: het ene blauw oogde fel naast het zwarte inademscherm. Nu zwart water met
                    // donkerblauwe golflijnen; de ruggen op de bodem zijn het donkerste blauw (000055).
                    dc.setColor(0x000000, 0x000000);
                    dc.fillRectangle(0, 0, dc.getWidth(), dc.getHeight());
                    KrabV2Rand.nachtwater(v, dc, 100, 244);
                } else {
                    raster(v, dc, 0x005555, 0x0055AA, v.q(eind ? 152 : 148));
                    v.golf(dc, eind ? 146 : 142, 262, 0x000055, 3.0, 2, 1.0);
                }
            }
            // oppervlak: lichte golvende rand bovenin. Op MIP weg (keuring 3 punt 3): de ronde rand sneed hem af
            // tot een losse blauwe boog.
            if (am) {
                var pts = [] as Array<[Numeric, Numeric]>;
                for (var x = 0; x <= 260; x += 10) {
                    pts.add([v.q(x), v.q(7 + 2.5 * Math.sin(x / 260.0 * 2.0 * Math.PI * 5))]);
                }
                pts.add([v.q(260), 0]);
                pts.add([0, 0]);
                v.kleur(dc, EbbTeken.meng(licht, zeeTop, 0.5));
                dc.fillPolygon(pts);
                v.punten += pts.size();
            }
            // de maanvlek bovenin is weg: de ronde rand sneed hem half af (keuring 05:25 punt 5)
            if (am && v.wereld != KrabV2Werelden.THUIS) { // het thuiswater heeft geen lichtbundel (Mila onderwater v1)
                var bu = v.w().bundel(scherm);
                var xo = eind ? 184 : bu[0];
                var xh = eind ? 186 : bu[1];
                var yh = eind ? 164 : 236;
                var basis = nacht ? 0x000040 : 0x004060;
                var kap = eind ? 72 : 140; // Mila v3.2 (a): boven de onderste tekstregel één zwakke tint (wit 4,5 op 1)
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
        } else if (stap == 3) {
            // zwevende lichtjes (dag) of plankton (nacht), alleen opzij; bellen; op het eindscherm feest en het belletje
            var pl = (nacht ? [22, 112, 34, 138, 16, 158, 48, 120, 232, 104, 244, 132, 220, 146, 208, 118, 60, 150, 196, 156, 30, 92, 236, 84]
                : [20, 150, 36, 146, 240, 152, 242, 140, 214, 152, 18, 160, 30, 92, 230, 92, 44, 136, 216, 136]) as Array<Number>;
            for (var i = 0; i < pl.size() / 2; i += 1) {
                if (!KrabV2Tekst.vrij(v, pl[2 * i], pl[2 * i + 1], 3)) {
                    continue;
                }
                if (am && nacht) {
                    v.glas(dc, 66, 0x00FFAA, 0x000040);
                    dc.fillCircle(v.q(pl[2 * i]), v.q(pl[2 * i + 1]), v.q(3));
                }
                v.kleur(dc, nacht ? (am ? 0xAAFFAA : 0x55FFAA) : 0xAAFFFF);
                dc.fillCircle(v.q(pl[2 * i]), v.q(pl[2 * i + 1]), v.q(1.2) < 1 ? 1 : v.q(1.2));
            }
            var bl = (eind ? [40, 96, 3, 52, 82, 2, 224, 168, 2] : v.w().bellen(scherm)) as Array<Number>;
            v.pen(dc, 0xFFFFFF);
            for (var i = 0; i < bl.size() / 3; i += 1) {
                if (!KrabV2Tekst.vrij(v, bl[3 * i], bl[3 * i + 1], bl[3 * i + 2])) {
                    continue;
                }
                dc.drawCircle(v.q(bl[3 * i]), v.q(bl[3 * i + 1]), v.q(bl[3 * i + 2]));
            }
            if (!nacht) {
                v.pen(dc, 0xAAFFFF);
                if (KrabV2Tekst.vrij(v, 26, 132, 3)) {
                    dc.drawCircle(v.q(26), v.q(132), v.q(2.6));
                }
                if (KrabV2Tekst.vrij(v, 234, 128, 3)) {
                    dc.drawCircle(v.q(234), v.q(128), v.q(2.2));
                }
            }
            if (eind) {
                var fo = [226, 82, 8, 146, 86, 5, 236, 146, 5] as Array<Number>;
                for (var j = 0; j < 3; j += 1) {
                    if (!KrabV2Tekst.vrij(v, fo[3 * j], fo[3 * j + 1], fo[3 * j + 2])) {
                        continue;
                    }
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
                    v.gloed(dc, 184, 123, 32, 27, licht, 40, zeeTop);
                }
                // belletje van de sea log: vlak 0055AA, rand 00FFFF, glimpje. Hoofdchat 10:55 punt 1: iets kleiner
                // (was 40 x 35 om 184, 122), zodat de tijden erboven 6/260 lucht houden; bovenkant nu op 88,6.
                v.rondje(dc, 184, 123, am ? 37.2 : 39.4, am ? 32.2 : 34.4, 0x00FFFF, -1, -1);
                v.rondje(dc, 184, 123, 37, 32, 0x0055AA, -1, -1);
                v.rondje(dc, 161, 107, 4, 4, 0xFFFFFF, -1, -1);
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

    // Keuring 05:25 punt 5: een los voorwerp staat heel in beeld. Geeft de verschuiving (1/260) die een cirkel
    // (x, y, r) binnen de ronde rand brengt, met 10 lucht (keuring 3 punt 4, was 3); 0 als hij al past.
    function inRond(x as Numeric, y as Numeric, r as Numeric) as Array<Float> {
        var dx = x - 130.0;
        var dy = y - 130.0;
        var l = Math.sqrt(dx * dx + dy * dy);
        var max = 130.0 - KrabV2Rand.NORM - r;
        if (l <= max || l < 1.0) {
            return [0.0, 0.0] as Array<Float>;
        }
        var f = (max - l) / l;
        return [(dx * f).toFloat(), (dy * f).toFloat()] as Array<Float>;
    }
}
