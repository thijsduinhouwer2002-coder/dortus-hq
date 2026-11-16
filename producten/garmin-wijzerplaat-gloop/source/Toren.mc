import Toybox.Graphics;
import Toybox.Lang;

// De hoedentoren op Gloops kruin, los van de rest van de wijzerplaat.
module Toren {
    // Volgorde van de gewone hoeden in de toren (Mila). De kroon (hoed 4) komt alleen bij het stapdoel
    // en staat dan altijd bovenop.
    const VOLGORDE = [0, 1, 2, 3, 5, 6, 7, 8, 9] as Array<Number>;
    const KROON = 4;
    // Hoe ver elke hoed boven de vorige staat, als deel van zijn eigen hoogte (Mila: 0,46).
    const HOED_STAP = 0.46;

    // Welke hoed op plek i (van onder) staat als er `toon` in de toren zitten.
    function hoedOp(i as Number, toon as Number, kroonOp as Boolean) as Number {
        return (kroonOp && i == toon - 1) ? KROON : VOLGORDE[i % 9];
    }

    // Stapelt `toon` hoeden op de kruin volgens de torentabel van Mila: tot 6 hoeden een wiebel, daarna
    // buigt de toren naar rechtsboven, weg van de tijd. Bij het doel staat de kroon bovenop en in beeld.
    // `pl` zijn de plaatjes van de view (hoed k staat op plek 2 + k), `m` de maten en `p` de plekken.
    function teken(dc as Graphics.Dc, rond as Boolean, voetX as Number, voetY as Number, toon as Number, kroonOp as Boolean, zweef as Boolean, pl as Array<Plaatje>, m as Array<Number>, p as Array<Number>) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var y = voetY;
        // Op een rond scherm stopt de toren bij de laatste hoed die heel binnen de cirkel past (moet van
        // Daan, 16 nov: nooit een hoed kapot tegen de rand). De kroon blijft dan bovenop staan. Op een
        // rechthoekig scherm loopt de toren boven het scherm uit.
        if (rond) {
            var past = Regel.zichtbaar(toon, kroonOp, Rand.gewoon(w), Rand.kroon(w));
            if (past < toon) {
                zweef = zweef && kroonOp;
                toon = past;
            }
        }
        for (var i = 0; i < toon; i += 1) {
            var k = hoedOp(i, toon, kroonOp);
            var hb = m[12 + 2 * k];
            var hh = m[13 + 2 * k];
            var x = voetX + p[13 + (i < 24 ? i : 23)];
            var top = y - hh;
            if (top + hh < 0) {
                break;
            }
            if (zweef && i == toon - 1) {
                // De bovenste hoed hangt nog boven de toren, maar blijft in beeld (punt van Daan).
                var rand = Regel.randBoven(x, w, h, rond, 3);
                var hoog = top - hh;
                if (hoog < rand) {
                    hoog = rand;
                }
                if (hoog > top - hh / 3) {
                    hoog = top - hh / 3;
                }
                top = hoog;
            }
            dc.drawBitmap(x - hb / 2, top, pl[2 + k]);
            y = y - (hh * HOED_STAP + 0.5).toNumber();
        }
    }
}
