import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Het laden van losse plaatjes op nummer (uit GloopFaceView gehaald, zodat dat bestand korter blijft).
module Laad {
    // Laadt het plaatje van een cijfer: nr 0 tot 9 is een uurcijfer (wit), 10 tot 19 een minuutcijfer (mint).
    function cijfer(nr as Number) as Plaatje {
        var r = Rez.Drawables.Uur0;
        switch (nr) {
            case 1: r = Rez.Drawables.Uur1; break;
            case 2: r = Rez.Drawables.Uur2; break;
            case 3: r = Rez.Drawables.Uur3; break;
            case 4: r = Rez.Drawables.Uur4; break;
            case 5: r = Rez.Drawables.Uur5; break;
            case 6: r = Rez.Drawables.Uur6; break;
            case 7: r = Rez.Drawables.Uur7; break;
            case 8: r = Rez.Drawables.Uur8; break;
            case 9: r = Rez.Drawables.Uur9; break;
            case 10: r = Rez.Drawables.Min0; break;
            case 11: r = Rez.Drawables.Min1; break;
            case 12: r = Rez.Drawables.Min2; break;
            case 13: r = Rez.Drawables.Min3; break;
            case 14: r = Rez.Drawables.Min4; break;
            case 15: r = Rez.Drawables.Min5; break;
            case 16: r = Rez.Drawables.Min6; break;
            case 17: r = Rez.Drawables.Min7; break;
            case 18: r = Rez.Drawables.Min8; break;
            case 19: r = Rez.Drawables.Min9; break;
            case 20: r = Rez.Drawables.Grijs0; break;
            case 21: r = Rez.Drawables.Grijs1; break;
            case 22: r = Rez.Drawables.Grijs2; break;
            case 23: r = Rez.Drawables.Grijs3; break;
            case 24: r = Rez.Drawables.Grijs4; break;
            case 25: r = Rez.Drawables.Grijs5; break;
            case 26: r = Rez.Drawables.Grijs6; break;
            case 27: r = Rez.Drawables.Grijs7; break;
            case 28: r = Rez.Drawables.Grijs8; break;
            case 29: r = Rez.Drawables.Grijs9; break;
            default: break;
        }
        return WatchUi.loadResource(r) as Plaatje;
    }

    function lijnHoed(k as Number) as Plaatje {
        var r = Rez.Drawables.HoedAod0;
        switch (k) {
            case 1: r = Rez.Drawables.HoedAod1; break;
            case 2: r = Rez.Drawables.HoedAod2; break;
            case 3: r = Rez.Drawables.HoedAod3; break;
            case 4: r = Rez.Drawables.HoedAod4; break;
            case 5: r = Rez.Drawables.HoedAod5; break;
            case 6: r = Rez.Drawables.HoedAod6; break;
            case 7: r = Rez.Drawables.HoedAod7; break;
            case 8: r = Rez.Drawables.HoedAod8; break;
            case 9: r = Rez.Drawables.HoedAod9; break;
            default: break;
        }
        return WatchUi.loadResource(r) as Plaatje;
    }
}
