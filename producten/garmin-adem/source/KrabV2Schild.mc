import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF schildpadwereld (Mila v3.2, ontwerp/garmin/bron/werelden_v3.py en werelden_v32.py; hoofdchat 12 nov 03:55 NL
// punt 2): de zeegrasweide onder water en de grap boven water (de schildpad is een eilandje, er lift een meeuw mee
// op zijn schild). Zelfde opzet als de krab (KrabV2.mc): wat stil staat gaat per beurt in het plaatje, wat bij de
// held hoort (golfje voor zijn buik, meeuw, blad in zijn bek) wordt elke beurt na de held getekend. Maten in 1/260 D.
module KrabV2Schild {
    const GRAS = 0x00AA55;
    const GRAS_L = 0x55FF55;
    const GRAS_D = 0x005500;

    // Midden van het kader en maat van de schildpad per scherm: in, uit, Calm, inhouden, menu, eind. Run 55: bij
    // inademen 5 naar rechts en bij uitademen 4 lager dan het blad, want de meeuw stond 3 px van de cijfers op de FR255.
    function held(s as Number) as Array<Number> {
        return ([[177, 130, 44], [128, 166, 44], [172, 138, 44], [136, 182, 46], [132, 192, 42], [76, 134, 36]] as Array<Array<Number> >)[s];
    }

    // Kantelen in graden (min is met de klok mee: neus omhoog, het dier kijkt naar links).
    function kantel(s as Number) as Float {
        return ([-8.0, 0.0, -3.0, -7.0, -7.0, -6.0] as Array<Float>)[s];
    }

    // Zeegrasspriet als veelhoek met een lichte rand; hap: een ronde hap uit de rechterrand (de schildpad eet zeegras).
    function spriet(v as KrabV2View, dc as Graphics.Dc, x0 as Numeric, y0 as Numeric, lengte as Numeric, buig as Numeric, breed as Numeric, c as Number, hap as Boolean) as Void {
        var n = hap ? 10 : 5;
        for (var ronde = 0; ronde < 2; ronde += 1) {
            var e = (ronde == 0) ? 1.3 : 0.0;
            var li = [] as Array<[Numeric, Numeric]>;
            var re = [] as Array<[Numeric, Numeric]>;
            for (var i = 0; i <= n; i += 1) {
                var t = i / (n * 1.0);
                var x = x0 + buig * t * t;
                var y = y0 - (lengte + e) * t;
                var b = breed * (1.0 - 0.35 * t);
                var u = (t - 0.8) / 0.12;
                var h = (hap && u > -1.0 && u < 1.0) ? b * 0.75 * Math.sqrt(1.0 - u * u) : 0.0;
                li.add([v.q(x - b / 2 - e), v.q(y)]);
                re.add([v.q(x + b / 2 + e - h), v.q(y)]);
            }
            for (var i = n; i >= 0; i -= 1) {
                li.add(re[i]);
            }
            v.kleur(dc, ronde == 0 ? GRAS_L : c);
            dc.fillPolygon(li);
            v.punten += li.size();
        }
    }

    // Pluk kort zeegras: n sprietjes die uitwaaieren, elk twee dikke lijnstukken (goedkoper dan veelhoeken).
    function pluk(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, n as Number, hoogte as Numeric, c as Number) as Void {
        for (var ronde = 0; ronde < 2; ronde += 1) {
            var w = v.q(ronde == 0 ? 6.6 : 4.0);
            v.pen(dc, ronde == 0 ? GRAS_L : c);
            dc.setPenWidth(w < 2 ? 2 : w);
            for (var i = 0; i < n; i += 1) {
                var u = i / (n - 1.0) - 0.5;
                var h = hoogte * (1.0 - (u < 0 ? -u : u) * 0.6);
                var x0 = x + u * 12;
                dc.drawLine(v.q(x0), v.q(y), v.q(x0 + u * 5.5), v.q(y - h * 0.5));
                dc.drawLine(v.q(x0 + u * 5.5), v.q(y - h * 0.5), v.q(x0 + u * 22), v.q(y - h));
            }
        }
        dc.setPenWidth(1);
    }

    // Boven water, laag 3: een losgeraakt blad zeegras drijft onder het oppervlak.
    function blad(v as KrabV2View, dc as Graphics.Dc, top as Number) as Void {
        var y = top + 74;
        if (y >= 236) {
            return;
        }
        var p = [] as Array<Float>;
        for (var i = 0; i <= 10; i += 1) {
            p.add((162 + i * 3.4).toFloat());
            p.add((y + 4 * Math.sin(i * 0.5)).toFloat());
        }
        for (var i = 10; i >= 0; i -= 1) {
            p.add((162 + i * 3.4).toFloat());
            p.add((y + 5 + 4 * Math.sin(i * 0.5)).toFloat());
        }
        v.blob(dc, p, GRAS, GRAS_L, 1.1);
    }

    // Onder water, laag 1 tot 3 van de weide: verre ruggen en zand, hoge sprieten aan de randen, klein spul vooraan.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var sp = (scherm == 4);
        var zak = sp ? 18 : (scherm == 5 ? 10 : 0);
        if (stap == 1) {
            var zeeTop = nacht ? 0x000069 : 0x00698C;
            var verder = am ? EbbTeken.meng(nacht ? 0x00003C : 0x001E46, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA);
            v.rondje(dc, 60, 196 + zak, 90, 18, verder, -1, -1);
            v.rondje(dc, 210, 192 + zak, 80, 22, verder, -1, -1);
            v.rondje(dc, 130, 273 + zak / 2.0, 190, 67 - zak / 2.0, 0xAAAA55, -1, -1);
            v.rondje(dc, 130, 275 + zak / 2.0, 180, 65 - zak / 2.0, am ? 0xEBE196 : 0xFFFFAA, -1, -1);
            if (am) {
                v.gloed(dc, scherm == 5 ? 124 : held(scherm)[0], 230 + zak, 52, 10, 0xFFFFFF, 46, 0xEBE196);
            }
        } else if (stap == 2) {
            // x, lengte, breed, buig, tint (1 licht groen, 0 donker); links staan ze op 222, rechts op 224
            var s = [14, 86, 8, 10, 0, 28, 104, 9, 10, 0, 42, 74, 8, -8, 1, 56, 54, 7, 10, 1, 204, 60, 7, 9, 0, 218, 92, 9, -12, 1, 234, 78, 8, -12, 1, 248, 98, 8, 9, 1] as Array<Number>;
            // Mila run 53: op menu en eindscherm de hoge sprieten 8/260 korter, zodat "Today" en de naam vrij blijven
            var kort = (scherm >= 4) ? 8 : 0;
            for (var i = 0; i < 8; i += 1) {
                var x = s[5 * i];
                spriet(v, dc, sp ? 260 - x : x, (i < 4 ? 222 : 224) + zak, s[5 * i + 1] - kort, sp ? -s[5 * i + 3] : s[5 * i + 3], s[5 * i + 2], s[5 * i + 4] == 1 ? GRAS : GRAS_D, false);
            }
        } else if (stap == 3) {
            // een schelp en een steentje op het zand, vier plukken, een zeester: de weide is een plek, geen behang
            v.rondje(dc, sp ? 84 : 176, 240 + zak, 6, 4, 0xFFAAAA, 0xFFFFFF, -1);
            v.rondje(dc, sp ? 164 : 96, 244 + zak, 5, 3, 0xAAAAFF, 0xFFFFFF, -1);
            var p = [34, 232, 5, 30, 0, 52, 240, 4, 20, 1, 226, 232, 5, 32, 1, 206, 242, 4, 18, 0] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                pluk(v, dc, sp ? 260 - p[5 * i] : p[5 * i], p[5 * i + 1] + zak, p[5 * i + 2], p[5 * i + 3], p[5 * i + 4] == 1 ? GRAS : GRAS_D);
            }
            var ster = [] as Array<Float>;
            for (var i = 0; i < 10; i += 1) {
                var a = -Math.PI / 2 + i * Math.PI / 5;
                var rr = (i % 2 == 0) ? 7.5 : 3.15;
                ster.add(((sp ? 70 : 190) + rr * Math.cos(a)).toFloat());
                ster.add((230 + zak + rr * Math.sin(a)).toFloat());
            }
            v.blob(dc, ster, 0xFFAA00, 0xFFFFFF, 1.4);
        }
    }

    // Onder water, laag 4 (inhouden en menu): schaduw onder de schildpad en de spriet waar hij een hap uit nam.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        if (scherm != 3 && scherm != 4) {
            return;
        }
        var m = h[2];
        if (am) {
            v.gloed(dc, h[0] + 4, h[1] + m * 0.72, m * 0.95, 4.5, 0x5A5028, 53, 0xEBE196);
        } else {
            v.rondje(dc, h[0] + 4, h[1] + m * 0.72, m * 0.9, 4, 0xAAAA55, -1, -1);
        }
        spriet(v, dc, h[0] - 0.86 * m - 8, h[1] + m * 0.8, m * 1.15, 4, 10, GRAS, true);
    }

    // Breed blad zeegras tussen de kaken (bx, by is de bek), k is de schaal.
    function inBek(v as KrabV2View, dc as Graphics.Dc, bx as Float, by as Float, k as Float) as Void {
        var b = [4, -4, -14, -6, -30, -2, -38, 8, -28, 8, -12, 5, 4, 4] as Array<Number>;
        var p = [] as Array<Float>;
        for (var i = 0; i < 7; i += 1) {
            p.add((bx + b[2 * i] * k).toFloat());
            p.add((by + b[2 * i + 1] * k).toFloat());
        }
        v.blob(dc, p, GRAS, 0xFFFFFF, 1.5);
        v.pen(dc, GRAS_D);
        dc.setPenWidth(v.q(1.2) < 1 ? 1 : v.q(1.2));
        dc.drawLine(v.q(bx + 2 * k), v.q(by), v.q(bx - 26 * k), v.q(by + 2 * k));
        dc.setPenWidth(1);
    }

    // Een meeuw die op het schild staat en de andere kant op kijkt dan de schildpad (de grap). Ook bij nacht wit.
    function meeuw(v as KrabV2View, dc as Graphics.Dc, x as Float, y as Float, k as Float) as Void {
        v.pen(dc, 0xFFAA00);
        dc.setPenWidth(v.q(1.5 * k) < 1 ? 1 : v.q(1.5 * k));
        dc.drawLine(v.q(x - 2 * k), v.q(y + 3 * k), v.q(x - 2.6 * k), v.q(y + 8 * k));
        dc.drawLine(v.q(x + 2 * k), v.q(y + 3 * k), v.q(x + 2.6 * k), v.q(y + 8 * k));
        dc.setPenWidth(1);
        var lijf = [-10, -1, -4, -4.5, 5, -4, 7, 1, 1, 4.5, -6, 3] as Array<Numeric>;
        var vleugel = [-9, -1.4, -3, -3, 3, -1, -4, 1.2] as Array<Numeric>;
        var snavel = [9, -7, 14, -5.6, 9, -4.6] as Array<Numeric>;
        v.blob(dc, punten(lijf, x, y, k), 0xFFFFFF, 0x000055, 1.2);
        v.blob(dc, punten(vleugel, x, y, k), 0xAAAAAA, -1, 0.0);
        v.rondje(dc, x + 6 * k, y - 6 * k, 3.6 * k - 1.0, 3.4 * k - 1.0, 0xFFFFFF, 0x000055, -1);
        v.blob(dc, punten(snavel, x, y, k), 0xFFAA00, -1, 0.0);
        v.kleur(dc, 0x000000);
        dc.fillCircle(v.q(x + 7 * k), v.q(y - 6.6 * k), v.q(0.9 * k) < 1 ? 1 : v.q(0.9 * k));
    }

    function punten(b as Array<Numeric>, x as Float, y as Float, k as Float) as Array<Float> {
        var p = [] as Array<Float>;
        for (var i = 0; i < b.size(); i += 2) {
            p.add((x + b[i] * k).toFloat());
            p.add((y + b[i + 1] * k).toFloat());
        }
        return p;
    }

    // Plek van de meeuw: de schildtop (0,16 m, min 0,6 m vanaf het midden), mee gekanteld, dan 11 hoger.
    function meeuwPlek(h as Array<Number>, graden as Float) as Array<Float> {
        var a = Math.toRadians(-graden);
        var sx = 0.16 * h[2];
        var sy = -0.6 * h[2];
        return [(h[0] + sx * Math.cos(a) + sy * Math.sin(a)).toFloat(), (h[1] - sx * Math.sin(a) + sy * Math.cos(a) - 11).toFloat()] as Array<Float>;
    }

    // Na de held, elke beurt. Boven water: het golfje voor zijn buik (hij drijft IN het water) en de meeuw op zijn
    // schild. Onder water: het blad in zijn bek en bij inhouden en menu twee groene kruimels ervoor.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        var m = h[2];
        if (scherm <= 2) {
            var y0 = h[1] + 14;
            for (var ronde = 0; ronde < 2; ronde += 1) {
                var pts = [] as Array<[Numeric, Numeric]>;
                for (var x = h[0] - m; x <= h[0] + m; x += 8) {
                    pts.add([v.q(x), v.q(y0 + 1.8 * Math.sin((x - h[0]) / 7.0) - (ronde == 0 ? 1.6 : 0.0))]);
                }
                pts.add([v.q(h[0] + m * 0.9), v.q(y0 + 7)]);
                pts.add([v.q(h[0] - m * 0.9), v.q(y0 + 7)]);
                v.kleur(dc, ronde == 0 ? 0xFFFFFF : (am ? (nacht ? 0x004B96 : 0x0055AF) : (nacht ? 0x0000AA : 0x0055AA)));
                dc.fillPolygon(pts);
            }
            var mp = meeuwPlek(h, graden);
            meeuw(v, dc, mp[0], mp[1], 1.4);
            return;
        }
        // run 55: 5 naar links en 3 lager dan het blad, anders ligt het blad over zijn oog (beelden f1433af)
        var bx = (h[0] - 0.86 * m - 5).toFloat();
        var by = (scherm == 5) ? (h[1] + 1).toFloat() : (h[1] + 0.06 * m - 2).toFloat();
        inBek(v, dc, bx, by, scherm == 5 ? 0.8 : 1.0);
        if (scherm != 5) {
            var kr = [-9.0, -6.0, 2.0, -14.0, 2.0, 1.5] as Array<Float>;
            for (var i = 0; i < 2; i += 1) {
                var cx = bx + kr[3 * i];
                var cy = by + kr[3 * i + 1];
                var r = kr[3 * i + 2];
                v.blob(dc, [cx - r, cy, cx, cy - r * 1.4, cx + r, cy, cx, cy + r * 0.8] as Array<Float>, GRAS_L, 0xFFFFFF, 0.9);
            }
        }
    }
}
