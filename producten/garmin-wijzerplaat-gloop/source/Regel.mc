import Toybox.Lang;

// De regels van de toren, los van het scherm zodat ze te testen zijn.
module Regel {
    // Meer dan dit past op geen enkel scherm.
    const MAX_HOEDEN = 14;

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
}
