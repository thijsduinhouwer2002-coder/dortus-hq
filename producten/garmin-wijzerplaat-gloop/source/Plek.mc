import Toybox.Lang;

// GEMAAKT uit ontwerp/garmin/wijzerplaat-gloop/kit/wijzerplaat.json (Mila). Niet met de hand aanpassen.
// Volgorde: 0 Gloop midden x, 1 Gloop voet y, 2 tijd rechts x, 3 datum y, 4 uren boven y, 5 minuten boven y,
// 6 stappen y, 7 regel y, 8 veld y, 9 cijfer breed, 10 cijfer hoog, 11 overlap van de cijfers, 12 rand van
// de lijnplaatjes voor de slaapstand; daarna 24 keer de x van het midden van een hoed ten opzichte van de
// torenvoet (plek 13 is de onderste hoed). Alles in pixels.
module Plek {
    function voor(breedte as Number) as Array<Number> {
        if (breedte >= 454) {
            return [300, 422, 227, 98, 114, 190, 299, 327, 409, 76, 89, 5, 2, -4, 4, -4, 4, -4, 4, 1, 18, 20, 39, 44, 65, 71, 94, 102, 126, 135, 160, 170, 196, 207, 234, 246, 274] as Array<Number>;
        }
        if (breedte >= 416) {
            return [275, 387, 208, 89, 104, 175, 275, 300, 374, 70, 82, 5, 2, -4, 4, -4, 4, -4, 4, 1, 17, 18, 36, 40, 60, 65, 87, 93, 116, 123, 147, 155, 180, 189, 215, 225, 251] as Array<Number>;
        }
        if (breedte >= 390) {
            return [257, 363, 195, 84, 98, 163, 256, 280, 351, 65, 76, 5, 2, -4, 4, -4, 4, -4, 4, 1, 16, 17, 34, 37, 57, 61, 82, 87, 109, 115, 138, 145, 169, 177, 202, 210, 236] as Array<Number>;
        }
        if (breedte >= 320) {
            return [211, 342, 160, 61, 72, 127, 207, 229, 335, 55, 64, 4, 2, -3, 3, -3, 3, -3, 3, 1, 13, 14, 28, 31, 46, 50, 67, 72, 89, 95, 113, 120, 138, 146, 165, 173, 193] as Array<Number>;
        }
        if (breedte >= 280) {
            return [185, 260, 140, 60, 70, 116, 183, 200, 252, 47, 54, 3, 2, -3, 3, -3, 3, -3, 3, 0, 12, 12, 25, 27, 41, 43, 59, 62, 78, 83, 99, 104, 121, 127, 145, 151, 169] as Array<Number>;
        }
        if (breedte >= 260) {
            return [172, 242, 130, 56, 65, 109, 172, 187, 234, 44, 51, 3, 2, -2, 2, -2, 2, -2, 2, 1, 10, 12, 22, 25, 37, 41, 54, 59, 72, 77, 91, 98, 112, 119, 134, 141, 156] as Array<Number>;
        }
        if (breedte >= 240) {
            return [158, 223, 120, 52, 60, 101, 160, 174, 216, 41, 48, 3, 2, -2, 2, -2, 2, -2, 2, 1, 9, 11, 21, 23, 34, 38, 50, 54, 66, 71, 84, 90, 104, 109, 124, 130, 145] as Array<Number>;
        }
        return [137, 193, 104, 45, 52, 87, 138, 150, 187, 34, 41, 2, 2, -2, 2, -2, 2, -2, 2, 0, 8, 9, 18, 20, 30, 33, 43, 46, 58, 62, 73, 78, 90, 95, 107, 112, 126] as Array<Number>;
    }
}
