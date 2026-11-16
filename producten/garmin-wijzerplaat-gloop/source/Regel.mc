import Toybox.Lang;
import Toybox.Math;

// De regels van de toren, los van het scherm zodat ze te testen zijn.
module Regel {
    // Na het doel groeit de toren het scherm uit; de teller telt door tot dit aantal.
    const MAX_HOEDEN = 60;

    // Elke 1.000 stappen een hoed (de kroon telt niet mee).
    function hoeden(stappen as Number) as Number {
        if (stappen < 0) {
            return 0;
        }
        var n = stappen / 1000;
        return n > MAX_HOEDEN ? MAX_HOEDEN : n;
    }

    // De kroon komt erbij zodra het stapdoel gehaald is. Zonder doel geen kroon.
    function kroon(stappen as Number, doel as Number) as Boolean {
        return doel > 0 && stappen >= doel;
    }

    // Hoeveel hoeden bij dit doel horen (voor de regel "3/10 HATS").
    function hoedenBijDoel(doel as Number) as Number {
        if (doel <= 0) {
            return 10;
        }
        var n = (doel + 999) / 1000;
        return n > MAX_HOEDEN ? MAX_HOEDEN : n;
    }

    // Uren voor de klok: 24 uur of 12 uur (12 in plaats van 0).
    function uur(uur24 as Number, is24 as Boolean) as Number {
        if (is24) {
            return uur24;
        }
        var u = uur24 % 12;
        return u == 0 ? 12 : u;
    }

    // Hoe ver elke hoed boven de vorige staat, als deel van zijn eigen hoogte. Gewoon 0,56 (regel van
    // Mila uit het spel). Past de toren van het doel (alle hoeden van het doel, `som` px hoog, plus
    // de kroon) dan niet in `ruimte` px, dan schuiven de hoeden dichter in elkaar, zodat de kroon op
    // het moment van het doel precies helemaal in beeld staat. Daarna blijft de stap gelijk en groeit
    // de toren het scherm uit (regel van Daan, 16 nov). Nooit dichter dan 0,18.
    function stap(som as Number, ruimte as Number) as Float {
        if (som <= 0 || som * 0.56 <= ruimte) {
            return 0.56;
        }
        var f = ruimte.toFloat() / som;
        return f < 0.18 ? 0.18 : f;
    }

    // De toren buigt licht naar rechts: hoed i (vanaf 0) schuift i*i/(n*n) keer `maxBuig` px op,
    // met n het aantal hoeden bij het doel. Bij het doel is dat dus precies `maxBuig`.
    function buiging(i as Number, n as Number, maxBuig as Number) as Number {
        if (n <= 0) {
            return 0;
        }
        return maxBuig * i * i / (n * n);
    }

    // Hoeveel px vanaf de linkerrand een regel tussen y0 en y1 mag beginnen. Op een rond scherm
    // volgt dat de cirkel, zodat tekst niet achter de rand verdwijnt.
    function randLinks(y0 as Number, y1 as Number, w as Number, h as Number, rond as Boolean, marge as Number) as Number {
        if (!rond) {
            return marge;
        }
        var r = w / 2;
        var d0 = y0 - h / 2;
        var d1 = y1 - h / 2;
        if (d0 < 0) { d0 = -d0; }
        if (d1 < 0) { d1 = -d1; }
        var d = d0 > d1 ? d0 : d1;
        if (d >= r) {
            return r;
        }
        return r - Math.sqrt(r * r - d * d).toNumber() + marge;
    }

    // De hoogste y waarop een punt met deze x nog binnen een rond scherm valt (voor de kroon).
    function randBoven(x as Number, w as Number, h as Number, rond as Boolean, marge as Number) as Number {
        if (!rond) {
            return marge;
        }
        var r = w / 2;
        var d = x - r;
        if (d < 0) { d = -d; }
        if (d >= r) {
            return h / 2;
        }
        return h / 2 - Math.sqrt(r * r - d * d).toNumber() + marge;
    }
}
