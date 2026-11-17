import Toybox.Lang;
import Toybox.WatchUi;

// Maten per scherm, in pixels. De getallen komen uit het blad van Mila (maten-tij-tabel.md) en worden
// door maak_maten.py per schermmaat in resources*/jsondata/maten.json gezet. Het horloge laadt alleen
// de lijst van zijn eigen scherm. De nummers hieronder zijn de plek in die lijst (zelfde volgorde als NAMEN
// in maak_maten.py).
module Maten {
    const AANTAL = 29;
    const DATUM_Y = 0;
    const DATUM_PX = 1;
    const TIJD_Y = 2;
    const TIJD_PX = 3;
    const VELD_XL = 4;
    const VELD_XM = 5;
    const VELD_XR = 6;
    const ICOON_Y = 7;
    const ICOON_H = 8;
    const VELD_Y = 9;
    const VELD_PX = 10;
    const WATER_TOP = 11;
    const WATER_BODEM = 12;
    const NU_X = 13;
    const LIJN_X = 14;
    const BAND_0 = 15;
    const BAND_1 = 16;
    const BAND_2 = 17;
    const BAND_3 = 18;
    const LIJN_DIK = 19;
    const BOOT_HALF = 20;
    const MAST = 21;
    const BB_Y = 22;
    const BB_PX = 23;
    const BB_RAND = 24;
    const GOLF_B = 25;
    const GOLF_DIK = 26;
    const GOLF_AFSTAND = 27;
    const VEILIG = 28;

    var lijst as Array<Number>? = null;

    // Laadt de lijst één keer. Een lijst met een verkeerd aantal getallen telt als leeg.
    function laad() as Array<Number> {
        if (lijst == null) {
            var bron = WatchUi.loadResource(Rez.JsonData.Maten);
            var l = [] as Array<Number>;
            if (bron instanceof Lang.Array && bron.size() == AANTAL) {
                l = bron as Array<Number>;
            }
            lijst = l;
        }
        return lijst as Array<Number>;
    }

    // Eén maat. Buiten de lijst of lijst leeg: 0, zodat tekenen niet stopt.
    function m(i as Number) as Number {
        var l = laad();
        if (i < 0 || i >= l.size()) {
            return 0;
        }
        // De lijst komt uit maak_maten.py (alleen hele getallen) en de toets testMatenVan260 kijkt hem na.
        return l[i];
    }
}
