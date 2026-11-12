import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// De krabwereld (wereld 0) in dezelfde vorm als elke andere wereld (WERELD-BOUWEN.md hoofdstuk 3): de zes functies
// plus het blok waarmee hij zich aanmeldt (KrabV2WKrab, onderaan). De code van laag 1 en 2 stond tot run 60 in
// KrabV2Lagen.mc en is letterlijk verhuisd; de zwemband staat in KrabV2Band.mc.
module KrabV2Krab {
    function held(s as Number) as Array<Number> {
        return ([[154, 142, 36], [124, 165, 36], [124, 141, 36], [118, 192, 43], [118, 186, 38], [76, 130, 34]] as Array<Array<Number> >)[s];
    }

    function kantel(s as Number) as Float {
        return (s == 0) ? 4.8 : ((s == 2) ? 1.8 : 0.0);
    }

    // Plek van de zwemband per scherm (was de slipper): x, y, schaal, hoek in graden. KrabV2Band leest dit uit v.sl.
    function sl(s as Number) as Array<Float> {
        return ([[158.0, 154.0, 1.4125, -13.0], [128.0, 179.0, 1.4125, -5.0], [128.0, 155.0, 1.4125, -8.0], [120.0, 215.65, 1.4907, -4.0],
            [120.0, 206.9, 1.3173, -4.0], [70.0, 152.0, 1.0, -6.0]] as Array<Array<Float> >)[s];
    }

    // Onder water, laag 1 (verre ruggen en zand) en laag 2 (rots met anemoon, rots met zeester).
    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        var zeeTop = nacht ? 0x000069 : 0x00698C;
        var eind = (scherm == 5);
        var zak = eind ? 22 : 0;
        if (stap == 1) {
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
            // Keuring 4 punt 2: bij nacht op MIP gedempt zand (555500 met een smalle lichte kam AAAA55), was AAAA55.
            var dof = nacht && !am;
            v.rondje(dc, 130, 276, 170, 54, dof ? 0xFFFFAA : 0xAAAA55, -1, -1);
            v.rondje(dc, 130, 278, 160, 52, am ? 0xEBE196 : (dof ? 0xAAAA55 : 0xFFFFAA), -1, -1);
            if (am) {
                v.gloed(dc, 124, 234, 36, 8, 0xFFFFFF, 46, 0xEBE196);
            }
        } else if (stap == 2) {
            // rots met anemoon (links, in het menu rechts) en rots met zeester
            var sp = (scherm == 4);
            var ady = eind ? 14 : (sp ? 10 : 0);
            var adx = eind ? -8 : 0;
            // Keuring 05:25 punt 5: anemoon en zeester staan heel in beeld; hun rots schuift mee.
            var oa = KrabV2Lagen.inRond(sp ? 260 - 36 - adx : 36 + adx, 166 + zak + ady / 2, 30);
            if (eind) {
                // Keuring 4 punt 1: op het eindscherm geen anemoon; zijn rots ligt laag tegen de linkerrand, zodat
                // "new friend" en de naam op een vrij vlak staan.
                oa = [-26.0, 14.0] as Array<Float>;
            }
            v.rondje(dc, (sp ? 224 : 36) + oa[0], 202 + zak + oa[1], 34, 26, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            var ax = (sp ? 260 - 36 - adx : 36 + adx) + oa[0];
            var by = 180 + zak + oa[1];
            var an = [18, 12, 158, 26, 22, 150, 36, 36, 146, 46, 50, 150, 54, 60, 160] as Array<Number>;
            // Keuring 3 punt 5: de anemoon blijft 6/260 van tekst. Raakt een armpje tekst, dan worden de armen korter
            // (0,8 en 0,6 keer); past het dan nog niet, dan blijft alleen zijn rots.
            var tips = [] as Array<Float>;
            for (var i = 0; i < 5; i += 1) {
                var tx = an[3 * i + 1] + adx;
                tips.add(((sp ? 260 - tx : tx) + oa[0]).toFloat());
                tips.add((an[3 * i + 2] + zak + ady + oa[1]).toFloat());
            }
            var ak = 0.0;
            var maten = [1.0, 0.8, 0.6] as Array<Float>;
            for (var m = 0; m < 3 && ak == 0.0 && !eind; m += 1) {
                var past = true;
                for (var i = 0; i < 5; i += 1) {
                    if (KrabV2Tekst.raakt(v, ax + (tips[2 * i] - ax) * maten[m], by + (tips[2 * i + 1] - by) * maten[m], 5)) {
                        past = false;
                    }
                }
                if (past) {
                    ak = maten[m];
                }
            }
            if (ak > 0.0) {
                KrabV2Rand.meet(v, scherm, "anemoon", ax, 166 + zak + ady / 2 + oa[1], 30 * ak);
            }
            for (var ronde = 0; ak > 0.0 && ronde < 2; ronde += 1) {
                for (var i = 0; i < 5; i += 1) {
                    var x0 = an[3 * i] + adx;
                    if (sp) {
                        x0 = 260 - x0;
                    }
                    var x1 = ax + (tips[2 * i] - ax) * ak;
                    var y1 = by + (tips[2 * i + 1] - by) * ak;
                    v.pen(dc, ronde == 0 ? 0xFFFFFF : 0xAA55FF);
                    dc.setPenWidth(v.q(ronde == 0 ? 8.6 : 5.6));
                    dc.drawLine(v.q(x0 + oa[0]), v.q(by), v.q(x1), v.q(y1));
                    v.rondje(dc, x1, y1, ronde == 0 ? 4.3 : 3.6, ronde == 0 ? 4.3 : 3.6, ronde == 0 ? 0xFFFFFF : 0xFF55AA, -1, -1);
                }
            }
            dc.setPenWidth(1);
            if (ak > 0.0) {
                v.rondje(dc, ax, by, 23.6, 8.6, 0xFFFFFF, -1, -1);
                v.rondje(dc, ax, by, 22, 7, 0xAA55FF, -1, -1);
            }
            var rx = 222 - zak / 3;
            var sx = sp ? 260 - (218 - zak / 3) : 218 - zak / 3;
            var os = KrabV2Lagen.inRond(sx, 197 + zak, 14);
            sx += os[0];
            zak += os[1];
            // Keuring 4 punt 1: op het eindscherm ligt ook deze rots tegen de rand (20 naar rechts); de zeester staat
            // er alleen als hij 6/260 van de tekst blijft.
            v.rondje(dc, (sp ? 260 - rx : rx) + os[0] + (eind ? 20 : 0), 210 + zak + (eind ? 6 : 0), 30, 22, 0x5555AA, 0xAAAAFF, 0xAAAAFF);
            if (eind && KrabV2Tekst.raakt(v, sx, 197 + zak, 12)) {
                return;
            }
            KrabV2Rand.meet(v, scherm, "zeester", sx, 197 + zak, 14);
            var ster = [] as Array<Float>;
            for (var i = 0; i < 10; i += 1) {
                var a = -Math.PI / 2 + i * Math.PI / 5;
                var rr = (i % 2 == 0) ? 11.0 : 4.6;
                ster.add((sx + rr * Math.cos(a)).toFloat());
                ster.add((197 + zak + rr * Math.sin(a)).toFloat());
            }
            v.blob(dc, ster, 0xFFFF55, 0xFFFFFF, 1.8);
        }
    }

    // Laag 4: schaduw onder de krab (inhouden en menu) en de achterhelft van de zwemband.
    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        if (scherm == 3 || scherm == 4) {
            if (am) {
                v.gloed(dc, v.sl[0] - 4.0 * v.sl[2], v.sl[1] + 15, 33, 4, 0x5A5028, 53, 0xEBE196);
            } else {
                v.rondje(dc, v.sl[0] - 4.0 * v.sl[2], v.sl[1] + 15, 42, 5, 0xAAAA55, -1, -1);
            }
        }
        KrabV2Band.teken(v, dc, false);
    }

    // Na de held: de voorhelft van de zwemband.
    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Band.teken(v, dc, true);
    }
}

// Het aanmeldblok van de krab. Alleen wat afwijkt van KrabV2Wereld (KrabV2Werelden.mc) staat erin.
class KrabV2WKrab extends KrabV2Wereld {
    function initialize() {
        KrabV2Wereld.initialize();
    }

    function dier() as Number {
        return 4;
    }

    function vriend() as Number {
        return 1;
    }

    function vriendNaam() as String {
        return "Shrimp";
    }

    function held(s as Number) as Array<Number> {
        return KrabV2Krab.held(s);
    }

    function kantel(s as Number) as Float {
        return KrabV2Krab.kantel(s);
    }

    function onder(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, scherm as Number) as Void {
        KrabV2Krab.onder(v, dc, stap, am, nacht, scherm);
    }

    function onderHeld(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, h as Array<Number>) as Void {
        KrabV2Krab.onderHeld(v, dc, scherm, am, h);
    }

    function voor(v as KrabV2View, dc as Graphics.Dc, scherm as Number, am as Boolean, nacht as Boolean, h as Array<Number>, graden as Float) as Void {
        KrabV2Krab.voor(v, dc, scherm, am, nacht, h, graden);
    }

    // De uitzonderingen van de krab, elk uit een keuring (zie KrabV2Wereld voor wat ze doen).
    function start(v as KrabV2View, s as Number) as Void {
        v.sl = KrabV2Krab.sl(s);
    }

    function kam(s as Number) as Number {
        return s == 0 ? 150 : KrabV2Tekst.KAM[s];
    }

    function bundel(scherm as Number) as Array<Number> {
        return [118, 112] as Array<Number>;
    }

    function bellen(scherm as Number) as Array<Number> {
        return (scherm == 3 ? [192, 160, 3, 198, 148, 2] : []) as Array<Number>;
    }

    function luchtband() as Boolean {
        return false;
    }

    function ruimte() as Number {
        return 11;
    }

    function streng() as Boolean {
        return true;
    }

    // Bij de krab zijn de scharen de bovenkant (vaste maten van het blad).
    function heldBoven(v as KrabV2View, scherm as Number) as Number {
        if (scherm <= 2) {
            return v.held()[1] - 24;
        }
        return scherm == 3 ? 164 : (scherm == 4 ? 186 - 25 : 130 - 22);
    }
}
