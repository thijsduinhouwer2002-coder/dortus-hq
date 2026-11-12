import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Garnaalwereld (wereld 2, Wout, 12 nov). Mila werelden v4 familie strand (ontwerp/garmin/bron/werelden_v4_strand.py,
// beelden werelden5/shrimp-* en werelden4/shrimp-*). De grap: boven water surft de garnaal op een geel surfplankje
// op jouw golf; onder water staat het plankje rechtop in het zand naast hem, op een kiezelstrandje onder een steiger.
// Opzet als KrabV2Schild.mc. Maten in 1/260 D.
module KrabV2Garnaal {
    const HOUT = 0xAA5500;
    const HOUT_L = 0xFFAA55;
    const KIEZEL = 0xAAAAAA;
    const KIEZEL_D = 0x555555;

    // Midden en maat van de garnaal per scherm: in, uit, Calm, inhouden, menu, eind (Mila: in 154,120; hoog 130).
    function held(s as Number) as Array<Number> {
        return ([[154, 120, 34], [130, 154, 34], [130, 130, 34], [110, 184, 44], [112, 196, 38], [70, 124, 30]] as Array<Array<Number> >)[s];
    }

    // Mila kantelt 8 bij inademen en 3 bij Calm (neus omhoog is min).
    function kantel(s as Number) as Float {
        return ([-8.0, 0.0, -3.0, 0.0, 0.0, 0.0] as Array<Float>)[s];
    }

    // Dikke staaf met ronde uiteinden en een lichte rand (steigerpaal). Maten in 1/260.
    function staaf(v as KrabV2View, dc as Graphics.Dc, x0 as Numeric, y0 as Numeric, x1 as Numeric, y1 as Numeric, b as Numeric, c as Number, rand as Number, rb as Numeric) as Void {
        for (var ronde = (rand >= 0 ? 0 : 1); ronde < 2; ronde += 1) {
            var w = (ronde == 0) ? b + 2 * rb : b;
            var p = v.q(w);
            v.kleur(dc, ronde == 0 ? rand : c);
            dc.setPenWidth(p < 1 ? 1 : p);
            dc.drawLine(v.q(x0), v.q(y0), v.q(x1), v.q(y1));
            var r = v.q(w / 2.0);
            dc.fillCircle(v.q(x0), v.q(y0), r < 1 ? 1 : r);
            dc.fillCircle(v.q(x1), v.q(y1), r < 1 ? 1 : r);
        }
        dc.setPenWidth(1);
    }

    // Geel surfplankje met rode middenstreep en witte rand. L is de halve lengte, hoek in graden (y omlaag).
    // Staand: rechtop (onder water in het zand) met een rood stipje; anders een rood vinnetje onder de staart.
    function plank(v as KrabV2View, dc as Graphics.Dc, cx as Numeric, cy as Numeric, L as Numeric, hoek as Numeric, staand as Boolean) as Void {
        var a = Math.toRadians(hoek + (staand ? -90 : 0));
        var ca = Math.cos(a);
        var sa = Math.sin(a);
        var p = [] as Array<Float>;
        for (var i = 0; i < 16; i += 1) {
            var t = i / 16.0 * 2.0 * Math.PI;
            var c = Math.cos(t);
            var x = L * c;
            var y = L * 0.25 * Math.sin(t) * (c < 0 ? 0.95 : 1.0 - 0.5 * c * c);
            p.add((cx + x * ca - y * sa).toFloat());
            p.add((cy + x * sa + y * ca).toFloat());
        }
        v.blob(dc, p, 0xFFFF00, 0xFFFFFF, 1.8);
        staaf(v, dc, cx - 0.82 * L * ca, cy - 0.82 * L * sa, cx + 0.82 * L * ca, cy + 0.82 * L * sa, 2.6, 0xFF0000, -1, 0);
        if (staand) {
            v.rondje(dc, cx - 0.55 * L * ca, cy - 0.55 * L * sa, 2.2, 2.2, 0xFF0000, -1, -1);
        } else {
            var f = [-0.78, 0.2, -0.62, 0.2, -0.74, 0.46] as Array<Float>;
            var vin = [] as Array<Float>;
            for (var i = 0; i < 3; i += 1) {
                var x = f[2 * i] * L;
                var y = f[2 * i + 1] * L;
                vin.add((cx + x * ca - y * sa).toFloat());
                vin.add((cy + x * sa + y * ca).toFloat());
            }
            v.blob(dc, vin, 0xFF0000, -1, 0.0);
        }
    }

    // Hoe ver de plek zakt: menu 6 (Mila), eindscherm 24 (onder de naam).
    function zak(scherm as Number) as Number {
        return scherm == 4 ? 6 : (scherm == 5 ? 24 : 0);
    }

    // Onder water: laag 1 verre ruggen en de grijze kiezelbank, laag 2 de steigerpalen, laag 3 de kiezels.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var z = zak(scherm);
        if (stap == 1) {
            var zeeTop = nacht ? 0x000069 : 0x00698C;
            var verder = am ? EbbTeken.meng(nacht ? 0x00003C : 0x001E46, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA);
            v.rondje(dc, 60, 200 + z, 90, 18, verder, -1, -1);
            v.rondje(dc, 210, 196 + z, 80, 22, verder, -1, -1);
            v.golf(dc, 221.8 + z, 262, KIEZEL, 3.0, 2, 0.0);
            v.golf(dc, 224 + z, 262, KIEZEL_D, 3.0, 2, 0.0);
        } else if (stap == 2) {
            // twee steigerpalen aan de randen; de bovenkant zakt tot hij 6/260 van tekst blijft
            // eindscherm: palen tegen de rand, de rechter stond op de FR255 tegen de naam van de nieuwe vriend (hoofdchat run 1)
            var px = (scherm == 5 ? [22, 238] : [36, 224]) as Array<Number>;
            for (var i = 0; i < 2; i += 1) {
                var top = 132 + z;
                while (top < 196 + z && KrabV2Tekst.raakt(v, px[i], top, 8)) {
                    top += 4;
                }
                staaf(v, dc, px[i], top, px[i], 236 + z, 12, HOUT, HOUT_L, 1.8);
                var aan = [176, 204] as Array<Number>;
                for (var j = 0; j < 2; j += 1) {
                    if (aan[j] + z > top + 4) {
                        v.rondje(dc, px[i], aan[j] + z, 6, 2, 0x55AA55, -1, -1);
                    }
                }
            }
        } else if (stap == 3) {
            // kiezels in een rij, om de drie een roze. Eigen kijkronde: op 238 sneed de ronde rand bijna alle kiezels
            // weg; nu hoger, en een kiezel die minder dan 4/260 van de rand blijft valt weg (hij hoort bij de bodem).
            var i = 0;
            for (var x = 10; x < 260; x += 15) {
                var y = 231 + z / 2 + 5 * (i % 2);
                var dx = x - 130;
                var dy = y - 130;
                if (Math.sqrt(dx * dx + dy * dy) + 7 <= 126) {
                    v.rondje(dc, x, y, 6.5, 4.6, (i % 3 == 0) ? 0xFFAAAA : KIEZEL, 0xFFFFFF, -1);
                }
                i += 1;
            }
        }
    }

    // Laag 4: boven water het surfplankje onder de garnaal (op de kam), onder water rechtop in het zand ernaast.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        var m = h[2];
        if (scherm <= 2) {
            var kam = KrabV2Tekst.KAM[scherm];
            var hoog = (scherm != 0);
            plank(v, dc, h[0] + 4, kam + (hoog ? 0 : 2), 40, (scherm == 0 ? 8 : (scherm == 2 ? 3 : 0)) * -0.6, false);
            return;
        }
        var x = h[0] + m * 1.25;
        var y = h[1] + 4;
        var o = KrabV2Lagen.inRond(x, y, m * 0.8);
        KrabV2Rand.meet(v, scherm, "surfplank", x + o[0], y + o[1], m * 0.8);
        plank(v, dc, x + o[0], y + o[1], m * 0.8, 0, true);
    }
}

// Aanmeldblok van de garnaal (zie KrabV2Werelden.mc).
class KrabV2WGarnaal extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 1;
    }

    function vriend() as Number {
        return 5;
    }

    function vriendNaam() as String {
        return "Seahorse";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Garnaal.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Garnaal.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Garnaal.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Garnaal.onderHeld(v, dc, scherm, am, h);
    }
}
