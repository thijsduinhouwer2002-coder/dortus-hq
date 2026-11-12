import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Kreeftwereld (Wout, 12 nov). Mila werelden v4 familie strand (ontwerp/garmin/bron/werelden_v4_strand.py,
// beelden werelden5/lobster-*). De grap: de kreeft is tuinman. Boven water met strohoed en een groene gieter in zijn
// schaar boven een stekje in een potje op een drijvend eilandje; onder water in een tuin met gazon en wit hekje,
// hij giet een bloempotje op de bodem. Opzet als KrabV2Garnaal.mc, tekenhulpen in KrabV2Strand.mc. Maten in 1/260.
module KrabV2Kreeft {
    // in, uit, Calm, inhouden, menu, eind (Mila: hx 166, 140, 180 op kam 134, 170, 146; hy kam min 4).
    function held(s as Number) as Array<Number> {
        return ([[166, 130, 38], [140, 166, 38], [180, 142, 38], [130, 194, 42], [128, 196, 36], [76, 118, 28]] as Array<Array<Number> >)[s];
    }

    function kantel(s as Number) as Float {
        return ([-8.0, 0.0, -3.0, 0.0, 0.0, 0.0] as Array<Float>)[s];
    }

    function zak(scherm as Number) as Number {
        return scherm == 4 ? 6 : (scherm == 5 ? 24 : 0);
    }

    // Onder water: laag 1 groen gazon, laag 2 wit tuinhekje rechts (de held en zijn bloempot staan vrij).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var z = zak(scherm);
        if (stap == 1) {
            v.golf(dc, 219.8 + z, 262, KrabV2Strand.GROEN_L, 3.0, 2, 0.0);
            v.golf(dc, 222 + z, 262, KrabV2Strand.GROEN, 3.0, 2, 0.0);
        } else if (stap == 2) {
            var e = scherm == 5 ? 12 : 0;
            var x0 = scherm == 5 ? 30 : 196;
            for (var x = x0; x < 252; x += 16) {
                if (scherm == 5 && x > 60 && x < 200) {
                    continue;
                }
                if (!KrabV2Strand.binnen(x, 194 + z + e, 4)) {
                    continue;
                }
                v.blob(dc, KrabV2Strand.pk(x, 0, 1, 1, [-4, 224 + z, -4, 196 + z + e, 0, 191 + z + e, 4, 196 + z + e, 4, 224 + z] as Array<Numeric>), 0xFFFFFF, 0x555555, 1.0);
            }
            if (scherm != 5) {
                var ys = [202, 214] as Array<Number>;
                for (var i = 0; i < 2; i += 1) {
                    KrabV2Strand.rechthoek(v, dc, x0 - 4, ys[i] + z, 250, ys[i] + 3 + z, 0xFFFFFF);
                }
            }
        }
    }

    // Laag 4: boven water het eilandje met stekje en de druppels; onder water het bloempotje onder de broes.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        var m = h[2];
        if (scherm <= 2) {
            var k = 1.25;
            var gx = h[0] - 30;
            var gy = h[1] - 26;
            var bx = gx - 31 * k;
            var by = gy + 6 * k;
            KrabV2Strand.eiland(v, dc, bx - 3, by + 43, 1.1);
            var d = [-3, 5, 1, 10, -5, 14, -1, 18] as Array<Number>;
            for (var i = 0; i < 4; i += 1) {
                KrabV2Strand.druppel(v, dc, bx + d[2 * i] * k * 0.8, by + d[2 * i + 1] * k * 0.8, k * 1.15, 0x000055);
            }
            return;
        }
        if (scherm == 5) {
            return;
        }
        var k = 1.45 * m / 40.0;
        var x = h[0] - 0.78 * m - 7 * k - 24 * k;
        var y = 216 + zak(scherm);
        var o = KrabV2Lagen.inRond(x, y - 8, 12);
        KrabV2Rand.meet(v, scherm, "bloempot", x + o[0], y - 8 + o[1], 12);
        KrabV2Strand.bloempot(v, dc, x + o[0], y + o[1], 0.75);
    }

    // Voor de held: gieter in de schaar en strohoed op zijn kop.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        var m = h[2];
        if (scherm <= 2) {
            KrabV2Strand.gieter(v, dc, h[0] - 30, h[1] - 26, 1.25, KrabV2Strand.GROEN, KrabV2Strand.GROEN_L, KrabV2Strand.GROEN_D, false);
            KrabV2Strand.strohoed(v, dc, h[0] + 2, h[1] - 25, 1.15);
            return;
        }
        var k = scherm == 5 ? 1.0 : 1.45 * m / 40.0;
        var b = KrabV2Strand.gieter(v, dc, h[0] - 0.78 * m, h[1] - 0.58 * m, k, 0x00AAFF, 0x55FFFF, 0x0000AA, scherm != 5);
        KrabV2Rand.meet(v, scherm, "gieter", b[0], b[1], b[2]);
        if (scherm == 5) {
            KrabV2Strand.strohoed(v, dc, h[0] + 2, h[1] - 18, 0.85);
        } else {
            KrabV2Strand.strohoed(v, dc, h[0] + 2, h[1] - 0.66 * m, 1.15 * m / 38.0);
        }
    }
}

// Aanmeldblok van de kreeft (zie KrabV2Werelden.mc).
class KrabV2WKreeft extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 22;
    }

    function vriend() as Number {
        return 23;
    }

    function vriendNaam() as String {
        return "Whale";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Kreeft.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Kreeft.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Kreeft.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Kreeft.onderHeld(v, dc, scherm, am, h);
    }

    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Kreeft.voor(v, dc, scherm, am, nacht, h, graden);
    }
}
