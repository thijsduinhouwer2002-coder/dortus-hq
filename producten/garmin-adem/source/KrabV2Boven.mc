import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// PROEF werelden (zie KrabV2.mc): de lagen boven water die stil staan. Uit KrabV2Lagen.mc gehaald in run 55 (regel
// van 300). Lucht, zon of maan, wolk, kam en twee golfrijen zijn voor elke wereld gelijk; laag 3 is van de wereld
// (krab: de verre slipper, schildpad: een drijvend blad zeegras).
module KrabV2Boven {
    // Boven water (in, uit, Calm): lucht met zon of maan, wolkje, meeuw, kam met schuim op hoogte top, twee golfrijen,
    // ver weg de andere slipper van het paar.
    function boven(v as KrabV2View, dc as Graphics.Dc, stap as Number, am as Boolean, nacht as Boolean, top as Number) as Void {
        var l0 = nacht ? 0x000055 : 0x0055AA;
        var l1 = nacht ? 0x0000AA : 0x00AAFF;
        // Mila v3: kam en twee golfrijen eronder (drie of vier rijen was te veel punten per beurt)
        // Keuring 05:25 punt 6: geen golflijn binnen 6/260 van de onderste regel. De rijen wijken voor het gemeten
        // tekstvak (echte letter): rij 1 eindigt 6 erboven, rij 2 begint 6 eronder; de regel staat in een rustige band.
        var orr = KrabV2Tekst.onderRegel();
        var r1 = orr[0] * 260 / dc.getWidth() - 11;
        var r2 = orr[1] * 260 / dc.getWidth() + 13;
        var rijY = [top, r1 < top + 34 ? r1 : top + 34, r2 > top + 66 ? r2 : top + 66] as Array<Number>;
        var rijA = [4.0, 3.0, 3.5] as Array<Float>;
        var rijN = [2, 4, 3] as Array<Number>;
        var rijF = [1.2, 0.3, 2.0] as Array<Float>;
        var kl = (am ? (nacht ? [0x004B96, 0x002D73, 0x000F4B] : [0x0055AF, 0x00378C, 0x001E64])
            : (nacht ? [0x0000AA, 0x0000AA, 0x0000AA] : [0x0055AA, 0x0000AA, 0x000055])) as Array<Number>; // nacht MIP: na de nachtregel één blauw 000055 (v1.3)
        if (stap == 0) {
            if (am) {
                KrabV2Lagen.verloop(v, dc, 0, top + 6, l0, l1);
            } else {
                v.kleur(dc, l0);
                dc.fillRectangle(0, 0, dc.getWidth(), v.q(top + 6));
                // bij de krab is de band 0055FF weg: zijn rand liep als een lijn dwars door de krab (keuring 05:25 punt 6)
                if (!nacht && v.wereld != 0) {
                    v.golf(dc, top - 28, top + 6, 0x0055FF, 2.5, 2, 0.0);
                }
            }
            if (nacht) {
                var st = [56, 50, 204, 44, 222, 82, 34, 100, 184, 24, 96, 20, 238, 110] as Array<Number>;
                v.kleur(dc, 0xFFFFFF);
                for (var i = 0; i < 7; i += 1) {
                    if (!KrabV2Tekst.vrij(v, st[2 * i], st[2 * i + 1], 1)) {
                        continue;
                    }
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
            // wolkje rechts (bij nacht donker)
            var wo = [214, 70, 14, 8, 226, 64, 12, 10, 236, 72, 11, 7] as Array<Number>;
            for (var ronde = 0; ronde < 2; ronde += 1) {
                var wk = (ronde == 0) ? (nacht ? 0x0000AA : 0xAAFFFF) : (nacht ? 0x5555AA : 0xFFFFFF);
                for (var i = 0; i < 3; i += 1) {
                    v.rondje(dc, wo[4 * i], wo[4 * i + 1] - ronde, wo[4 * i + 2] - 2 * ronde, wo[4 * i + 3] - 1.5 * ronde, wk, -1, -1);
                }
            }
            // De meeuw van de krab is weg (keuring 3 punt 6, Thijs 12 nov 08:10): een los tekentje naast "breathe in"
            // waarvan een kijker niet weet wat het is. Regel: niets in beeld dat je niet herkent.
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
        } else if (stap == 3 && v.wereld == 1) {
            KrabV2Schild.blad(v, dc, top);
        }
        // De verre slipper van het paar is weg: de krab zit nu in een zwemband (Mila keuring 2, 12 nov 04:25 UTC).
    }
}
