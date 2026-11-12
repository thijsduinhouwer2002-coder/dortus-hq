import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Zeehondwereld (Wout, 12 nov). Mila werelden v4 familie strand (ontwerp/garmin/bron/werelden_v4_strand.py,
// beelden werelden5/seal-*). De grap: de zeehond zit te vissen. Boven water ligt hij op een ijsschots met een hengel
// en een rood-witte dobber op jouw golf; onder water zit hij onder het ijs, de dobber hangt naast hem met een visje
// erbij. Opzet als KrabV2Garnaal.mc, tekenhulpen in KrabV2Strand.mc. Maten in 1/260.
module KrabV2Zeehond {
    // in, uit, Calm, inhouden, menu, eind (Mila: laag hx 176, hy kam min 11; hoog hx 140, hy kam min 16).
    function held(s as Number) as Array<Number> {
        return ([[176, 123, 32], [140, 154, 32], [140, 130, 32], [116, 192, 38], [118, 200, 33], [70, 120, 26]] as Array<Array<Number> >)[s];
    }

    function kantel(s as Number) as Float {
        return ([-4.8, 0.0, -1.8, 0.0, 0.0, 0.0] as Array<Float>)[s];
    }

    function zak(scherm as Number) as Number {
        return scherm == 4 ? 6 : (scherm == 5 ? 24 : 0);
    }

    // Onder water: laag 1 de ijsrand bovenin (niet op het eindscherm) en de stenen bodem, laag 3 twee stenen aan de kanten.
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var z = zak(scherm);
        if (stap == 1) {
            if (scherm != 5) {
                for (var ronde = 0; ronde < 2; ronde += 1) {
                    var pts = [] as Array<[Numeric, Numeric]>;
                    for (var x = 0; x <= 260; x += 6) {
                        pts.add([v.q(x), v.q(14 + 4 * Math.sin(x / 9.0) + 3 * Math.sin(x / 23.0) + (ronde == 0 ? 2 : 0))]);
                    }
                    pts.add([v.q(260), 0]);
                    pts.add([0, 0]);
                    v.kleur(dc, ronde == 0 ? (nacht ? 0x5555FF : 0x55AAFF) : (nacht ? 0x0000AA : 0x0055AA));
                    dc.fillPolygon(pts);
                }
            }
            v.golf(dc, 223.8 + z, 262, 0x55AAAA, 3.0, 2, 0.0);
            v.golf(dc, 226 + z, 262, 0x005555, 3.0, 2, 0.0);
        } else if (stap == 3) {
            // stenen ver van de held (grijs zoals de zeehond: niet achter hem); wat de ronde rand raakt valt weg
            var st = [58, 224, 7, 80, 230, 4, 180, 230, 4, 202, 224, 7] as Array<Number>;
            for (var i = 0; i + 2 < st.size(); i += 3) {
                if (KrabV2Strand.binnen(st[i], st[i + 1] + z / 2, st[i + 2] - 6)) {
                    v.rondje(dc, st[i], st[i + 1] + z / 2, st[i + 2], st[i + 2] * 0.7, 0x555555, 0xAAAAAA, -1);
                }
            }
        }
    }

    // Laag 4: boven water de ijsschots onder hem; onder water de dobber aan zijn lijntje met het visje.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        var m = h[2];
        if (scherm <= 2) {
            KrabV2Strand.schots(v, dc, h[0] + 6, KrabV2Tekst.KAM[scherm] + 2, 52, 9);
            return;
        }
        var dx = scherm == 5 ? 104 : h[0] + m * 1.35;
        var dy = scherm == 5 ? 104 : h[1] - m * 0.7;
        var k = scherm == 5 ? 1.0 : 1.25;
        // het lijntje komt van boven; het begint pas 6/260 onder tekst
        var top = dy - 20;
        while (top < dy - 10 && KrabV2Tekst.raakt(v, dx, top, 1)) {
            top += 2;
        }
        if (scherm == 5) {
            top = 78;
            while (top < 96 && KrabV2Tekst.raakt(v, dx, top, 1)) {
                top += 2;
            }
        }
        KrabV2Strand.lijn(v, dc, [dx.toFloat(), top.toFloat(), dx.toFloat(), (dy - 10 * k).toFloat()] as Array<Float>, 0xFFFFFF, 1.2);
        KrabV2Rand.meet(v, scherm, "dobber", dx, dy, 8 * k);
        KrabV2Strand.dobber(v, dc, dx, dy, k);
        var vk = scherm == 5 ? 0.8 : 1.0;
        var vx = dx + (scherm == 5 ? 6 : 4);
        var vy = dy + 18;
        KrabV2Rand.meet(v, scherm, "visje", vx + 2 * vk, vy, 11 * vk);
        KrabV2Strand.visje(v, dc, vx, vy, vk);
    }

    // Voor de held, boven water: hengel uit zijn vinnen naar de dobber op de golf. De top wijkt voor de cijfers.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        if (scherm > 2) {
            return;
        }
        var kam = KrabV2Tekst.KAM[scherm];
        var dobx = h[0] - (scherm == 0 ? 76 : 80);
        var doby = kam + 8;
        var tx = h[0] - 60;
        var ty = h[1] - 18;
        var n = 0;
        while (n < 8 && KrabV2Tekst.raakt(v, tx, ty, 2)) {
            ty += 2;
            n += 1;
        }
        KrabV2Strand.hengel(v, dc, h[0] - 26, h[1] + 8, tx, ty, dobx, doby);
        KrabV2Strand.dobber(v, dc, dobx, doby, 1.2);
    }
}

// Aanmeldblok van de zeehond (zie KrabV2Werelden.mc).
class KrabV2WZeehond extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 12;
    }

    function vriend() as Number {
        return 13;
    }

    function vriendNaam() as String {
        return "Dolphin";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Zeehond.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Zeehond.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Zeehond.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Zeehond.onderHeld(v, dc, scherm, am, h);
    }

    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Zeehond.voor(v, dc, scherm, am, nacht, h, graden);
    }
}
