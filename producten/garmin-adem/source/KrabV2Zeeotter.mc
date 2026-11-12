import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Zeeotterwereld (Wout, 12 nov). Mila werelden v4 familie strand (ontwerp/garmin/bron/werelden_v4_strand.py, ronde 4,
// beelden werelden5/otter-*). De grap: de otter drijft op zijn rug met een grote mok warme chocolademelk op zijn buik
// (zijn buik is een tafel); onder water in een kelpwoud, vastgeknoopt aan een kelplint, de mok nog op zijn buik.
// Opzet als KrabV2Garnaal.mc, tekenhulpen in KrabV2Strand.mc. Maten in 1/260.
module KrabV2Zeeotter {
    // in, uit, Calm, inhouden, menu, eind (Mila: laag hx 168, hoog hx 136, hy kam min 4).
    function held(s as Number) as Array<Number> {
        return ([[168, 130, 36], [136, 166, 36], [136, 142, 36], [116, 200, 42], [116, 198, 36], [74, 124, 30]] as Array<Array<Number> >)[s];
    }

    function kantel(s as Number) as Float {
        return ([-4.8, 0.0, -1.8, 0.0, 0.0, 0.0] as Array<Float>)[s];
    }

    function zak(scherm as Number) as Number {
        return scherm == 4 ? 6 : (scherm == 5 ? 24 : 0);
    }

    // Onder water: laag 1 donkergroene bodem, laag 2 hoge kelplinten aan beide kanten met blaadjes en gele blaasjes.
    // De top van een lint zakt tot hij 6/260 van tekst blijft; op het eindscherm zijn ze korter (naam en belletje).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var z = zak(scherm);
        if (stap == 1) {
            v.golf(dc, 225.8 + z, 262, 0x55AA00, 3.0, 2, 0.0);
            v.golf(dc, 228 + z, 262, 0x005500, 3.0, 2, 0.0);
        } else if (stap == 2) {
            var kl = [14, 9, 150, 34, 8, 112, 54, 7, 80, 208, 7, 86, 228, 8, 120, 248, 9, 156] as Array<Number>;
            for (var i = 0; i + 2 < kl.size(); i += 3) {
                var x0 = kl[i];
                var hh = kl[i + 2] * (scherm == 5 ? 0.6 : 1.0);
                var sg = x0 < 130 ? 1 : -1;
                var top = 236 + z - hh;
                while (top < 220 + z && KrabV2Tekst.raakt(v, x0, top, 6)) {
                    top += 4;
                }
                hh = 236 + z - top;
                KrabV2Strand.kelp(v, dc, x0, 240 + z, x0 + 6 * sg, top, 5, kl[i + 1] * 0.75);
                for (var j = 0; j < 3; j += 1) {
                    var yy = 236 + z - hh * (0.3 + j * 0.25);
                    if (!KrabV2Strand.binnen(x0 + sg * 6, yy, 6) || KrabV2Tekst.raakt(v, x0 + sg * 6, yy, 6)) {
                        continue;
                    }
                    v.blob(dc, KrabV2Strand.pk(x0, yy, sg, 1, [0, 0, 11, -7, 3, -2] as Array<Numeric>), 0x55AA00, 0xAAFF55, 1.0);
                    v.rondje(dc, x0 + sg * 4, yy + 3, 2.2, 2.2, 0xFFFF55, -1, -1);
                }
            }
        }
    }

    // Laag 4 onder water: het kelplint waaraan hij vastgeknoopt is, achter hem tot de bodem.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        if (scherm < 3 || scherm == 5) {
            return;
        }
        var m = h[2];
        KrabV2Strand.kelp(v, dc, h[0] + 6, 244 + zak(scherm), h[0] + 2, h[1] + m * 0.35, 6, 5);
    }

    // Voor de held: de mok op zijn buik (stoom alleen als die vrij van tekst blijft) en onder water de knoop.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        var m = h[2];
        var x = 0.0;
        var yb = 0.0;
        var k = 1.0;
        if (scherm <= 2) {
            x = h[0] + 2;
            yb = h[1] - 4;
            k = 1.05;
        } else if (scherm == 5) {
            x = h[0] + 1;
            yb = h[1] - 3;
            k = 0.82;
        } else {
            x = h[0] + 0.04 * m;
            yb = h[1] - 0.12 * m;
            k = 1.05 * m / 36.0;
        }
        var stoomTop = yb - 22 * k - 16 * k;
        var stoom = !KrabV2Tekst.raakt(v, x, stoomTop, 6 * k) && !KrabV2Tekst.raakt(v, x, yb - 22 * k - 8 * k, 6 * k);
        KrabV2Strand.mok(v, dc, x, yb, k, stoom);
        if (scherm == 3 || scherm == 4) {
            var bx = h[0] + 2;
            var by = h[1] + m * 0.38;
            for (var sg = -1; sg <= 1; sg += 2) {
                v.blob(dc, KrabV2Strand.pk(bx, by, sg, 1, [0, 0, 10, -6, 10, 6] as Array<Numeric>), 0x55AA00, 0xAAFF55, 1.2);
            }
            v.rondje(dc, bx, by, 3, 3, 0xAAFF55, -1, -1);
        }
    }
}

// Aanmeldblok van de zeeotter (zie KrabV2Werelden.mc).
class KrabV2WZeeotter extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 15;
    }

    function vriend() as Number {
        return 18;
    }

    function vriendNaam() as String {
        return "Sunfish";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Zeeotter.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Zeeotter.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Zeeotter.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Zeeotter.onderHeld(v, dc, scherm, am, h);
    }

    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Zeeotter.voor(v, dc, scherm, am, nacht, h, graden);
    }
}
