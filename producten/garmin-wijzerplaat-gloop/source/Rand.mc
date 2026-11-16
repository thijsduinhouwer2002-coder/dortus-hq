import Toybox.Lang;

// GEMAAKT DOOR bron/maak_rand.py uit de hoedenplaatjes van de kit, Maten.mc en Plek.mc. Niet met de hand
// aanpassen. Op een rond scherm blijft elke hoed minstens 4 px binnen de cirkel (moet van Daan, 16 nov).
module Rand {
    // Zoveel gewone hoeden passen heel in beeld (hoed 0 tot en met dit aantal min 1).
    function gewoon(breedte as Number) as Number {
        if (breedte >= 454) {
            return 9;
        }
        if (breedte >= 416) {
            return 9;
        }
        if (breedte >= 390) {
            return 9;
        }
        if (breedte >= 280) {
            return 9;
        }
        if (breedte >= 260) {
            return 8;
        }
        if (breedte >= 240) {
            return 8;
        }
        return 8;
    }

    // De hoogste plek (vanaf 0) waarop de kroon nog heel in beeld staat.
    function kroon(breedte as Number) as Number {
        if (breedte >= 454) {
            return 9;
        }
        if (breedte >= 416) {
            return 9;
        }
        if (breedte >= 390) {
            return 9;
        }
        if (breedte >= 280) {
            return 8;
        }
        if (breedte >= 260) {
            return 8;
        }
        if (breedte >= 240) {
            return 8;
        }
        return 8;
    }
}
