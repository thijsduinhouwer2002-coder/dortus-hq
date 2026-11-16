import Toybox.Lang;

// GEMAAKT DOOR maak_kit.py uit ontwerp/garmin/gloop-spel/kit/kit.json. Niet met de hand aanpassen.
// Volgorde: 0 Gloop breed, 1 rust hoog, 2 hap hoog, 3 blij hoog, 4 slok breed, 5 slok hoog,
// 6 held breed, 7 held hoog, 8 helm breed, 9 helm hoog, 10 en 11 voet van de toren (px in de
// rustsprite), daarna per hoed breed en hoog (12 en 13 voor hoed 0, tot 30 en 31 voor hoed 9).
module Maten {
    function voor(breedte as Number) as Array<Number> {
        if (breedte >= 454) {
            return [154, 112, 119, 112, 154, 119, 119, 124, 101, 100, 82, 15, 77, 74, 77, 59, 72, 39, 77, 37, 60, 49, 77, 67, 77, 54, 77, 52, 77, 34, 77, 64] as Array<Number>;
        }
        if (breedte >= 416) {
            return [141, 103, 109, 103, 141, 109, 109, 113, 93, 91, 75, 13, 71, 67, 71, 54, 66, 36, 71, 34, 55, 45, 71, 61, 71, 49, 71, 47, 71, 31, 71, 59] as Array<Number>;
        }
        if (breedte >= 390) {
            return [133, 97, 103, 96, 133, 103, 103, 107, 86, 85, 70, 13, 66, 63, 66, 50, 61, 34, 66, 32, 52, 42, 66, 58, 66, 46, 66, 44, 66, 29, 66, 55] as Array<Number>;
        }
        if (breedte >= 320) {
            return [109, 79, 84, 79, 109, 84, 85, 88, 72, 70, 58, 10, 54, 52, 54, 41, 50, 28, 54, 26, 42, 35, 54, 47, 54, 38, 54, 36, 54, 24, 54, 45] as Array<Number>;
        }
        if (breedte >= 280) {
            return [97, 71, 76, 71, 97, 76, 77, 80, 66, 63, 51, 9, 50, 47, 50, 38, 47, 26, 50, 25, 39, 32, 50, 43, 50, 35, 50, 34, 50, 23, 50, 42] as Array<Number>;
        }
        return [90, 66, 70, 66, 90, 70, 72, 74, 60, 60, 48, 9, 46, 44, 46, 36, 43, 25, 46, 23, 36, 30, 46, 40, 46, 33, 46, 32, 46, 21, 46, 39] as Array<Number>;
    }
}
