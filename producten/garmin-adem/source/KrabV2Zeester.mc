import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Zeesterwereld (wereld 3, Wout, 12 nov). Mila werelden v4 familie strand (ontwerp/garmin/bron/werelden_v4_strand.py,
// beelden werelden5/starfish-* en werelden4/starfish-*). De grap: de zeester is sterrenkijker. Boven water staat hij
// in de golf met een telescoopje op drie pootjes naast zich, gericht op zon of maan (bij dag een donker glaasje, bij
// nacht een geel); onder water ligt de telescoop naast hem in een getijdenpoel. Opzet als KrabV2Schild.mc.
module KrabV2Zeester {
    const ROTS = 0xAAAAAA;
    const ROTS_D = 0x555555;

    // Midden en maat per scherm: in, uit, Calm, inhouden, menu, eind (Mila: in 160, hoog 138, hy = kam - 2).
    function held(s as Number) as Array<Number> {
        return ([[160, 132, 34], [138, 168, 34], [138, 144, 34], [112, 188, 40], [112, 196, 37], [70, 122, 29]] as Array<Array<Number> >)[s];
    }

    // Mila kantelt de zeester half zo veel als de andere dieren.
    function kantel(s as Number) as Float {
        return ([-4.0, 0.0, -1.5, 0.0, 0.0, 0.0] as Array<Float>)[s];
    }

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

    // Telescoopje: oogstuk, oranje buis, paarse kop met glaasje. (x, y) is het draaipunt, hoek in graden (y omlaag),
    // k de schaal. Met poten: drie houten pootjes naar beneden.
    function telescoop(v as KrabV2View, dc as Graphics.Dc, x as Numeric, y as Numeric, hoek as Numeric, k as Numeric, nacht as Boolean, poten as Boolean) as Void {
        var a = Math.toRadians(hoek);
        var ca = Math.cos(a);
        var sa = Math.sin(a);
        if (poten) {
            var dx = [-9, 0, 9] as Array<Number>;
            for (var i = 0; i < 3; i += 1) {
                staaf(v, dc, x, y, x + dx[i] * k, y + 18 * k, 2.4 * k, 0xAA5500, -1, 0);
            }
        }
        staaf(v, dc, x - 14 * k * ca, y - 14 * k * sa, x + 10 * k * ca, y + 10 * k * sa, 8 * k, 0xFF5500, 0xFFFFFF, 1.6);
        staaf(v, dc, x + 10 * k * ca, y + 10 * k * sa, x + 22 * k * ca, y + 22 * k * sa, 11 * k, 0xAA0055, 0xFFFFFF, 1.6);
        staaf(v, dc, x - 24 * k * ca, y - 24 * k * sa, x - 14 * k * ca, y - 14 * k * sa, 5 * k, 0xFFAA00, 0xFFFFFF, 1.2);
        // glaasje: ovaal dwars op de buis, als veelhoek zodat het mee draait
        var lx = x + 22.5 * k * ca;
        var ly = y + 22.5 * k * sa;
        var p = [] as Array<Float>;
        for (var i = 0; i < 10; i += 1) {
            var t = i / 10.0 * 2.0 * Math.PI;
            var u = 2.6 * k * Math.cos(t);
            var w = 5.0 * k * Math.sin(t);
            p.add((lx + u * ca - w * sa).toFloat());
            p.add((ly + u * sa + w * ca).toFloat());
        }
        v.blob(dc, p, nacht ? 0xFFFFAA : 0x000000, -1, 0.0);
        v.rondje(dc, x, y, 2.4 * k, 2.4 * k, 0xFFFF00, -1, -1);
    }

    function zak(scherm as Number) as Number {
        return scherm == 4 ? 6 : (scherm == 5 ? 24 : 0);
    }

    // Onder water: laag 1 verre ruggen en de grijze bodem, laag 2 de getijdenpoel en de rotsen, laag 3 mossels.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var z = zak(scherm);
        if (stap == 1) {
            var zeeTop = nacht ? 0x000069 : 0x00698C;
            var verder = am ? EbbTeken.meng(nacht ? 0x00003C : 0x001E46, zeeTop, 0.5) : (nacht ? 0x0000AA : 0x0055AA);
            v.rondje(dc, 60, 196 + z, 90, 18, verder, -1, -1);
            v.rondje(dc, 210, 192 + z, 80, 22, verder, -1, -1);
            v.golf(dc, 215.8 + z, 262, ROTS, 3.0, 2, 0.0);
            v.golf(dc, 218 + z, 262, ROTS_D, 3.0, 2, 0.0);
        } else if (stap == 2) {
            v.rondje(dc, 130, 246 + z, 96, 20, 0x00AAAA, 0xFFFFFF, -1);
            v.rondje(dc, 130, 250 + z, 80, 12, 0x55FFFF, -1, -1);
            // rotsen aan de randen mogen door de ronde rand (regel 10); ze zakken als ze tekst raken
            var r = [22, 220, 26, 20, 238, 218, 26, 22, 40, 244, 16, 10, 222, 244, 16, 10] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                var y = r[4 * i + 1] + z;
                if (KrabV2Tekst.raakt(v, r[4 * i], y - r[4 * i + 3], 2)) {
                    continue;
                }
                v.rondje(dc, r[4 * i], y, r[4 * i + 2], r[4 * i + 3], ROTS, 0xFFFFFF, 0xFFFFFF);
            }
        } else if (stap == 3) {
            // mossels op de rotsen, heel binnen de ronde rand
            var m = [30, 204, 44, 210, 230, 202, 216, 208] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                var o = KrabV2Lagen.inRond(m[2 * i], m[2 * i + 1] + z, 6);
                var x = m[2 * i] + o[0];
                var y = m[2 * i + 1] + z + o[1];
                if (KrabV2Tekst.raakt(v, x, y, 6)) {
                    continue;
                }
                v.rondje(dc, x, y, 5, 3, 0x000055, 0x5555FF, -1);
            }
        }
    }

    // Laag 4: boven water het telescoopje op pootjes naast de zeester, onder water de telescoop naast hem in de poel.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        var m = h[2];
        if (scherm <= 2) {
            var hoekMila = (scherm == 0) ? 8 : (scherm == 2 ? 3 : 0);
            telescoop(v, dc, h[0] - 40, h[1] - 6, -152 - hoekMila, 1.15, v.nacht, true);
            return;
        }
        var x = h[0] + m * 1.5;
        var y = h[1] + m * 0.45;
        var k = 1.45 * m / 40.0;
        if (scherm == 5) {
            x = 104;
            y = 128;
            k = 0.8;
        }
        var o = KrabV2Lagen.inRond(x, y, 24 * k);
        KrabV2Rand.meet(v, scherm, "telescoop", x + o[0], y + o[1], 24 * k);
        telescoop(v, dc, x + o[0], y + o[1], scherm == 5 ? -30 : -20, k, v.nacht, false);
    }
}

// Aanmeldblok van de zeester (zie KrabV2Werelden.mc).
class KrabV2WZeester extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 6;
    }

    function vriend() as Number {
        return 8;
    }

    function vriendNaam() as String {
        return "Pufferfish";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Zeester.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Zeester.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Zeester.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Zeester.onderHeld(v, dc, scherm, am, h);
    }
}
