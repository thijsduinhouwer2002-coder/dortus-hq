import Toybox.Lang;
import Toybox.WatchUi;

// GEMAAKT door bron/maak_werelden.py uit ebb-werelden-v11-data.json (werelden v1.1). Niet met de hand wijzigen.
// Alleen de lijst van werelden; de punten staan per wereld in resources/werelden/werelden.xml en worden pas
// geladen als het dier gekozen is. Sleutels: b bovenkant strook, t thuis, v vlakken, d details, f voor het dier.
module EbbWereldData {
    const EENHEID = 260;

    function heeft(dier as Number) as Boolean {
        return dier == 3 || dier == 4 || dier == 7;
    }

    // De gegevens van één wereld, of null als dit dier er geen heeft.
    function laad(dier as Number) as Dictionary or Null {
        if (dier == 3) { return WatchUi.loadResource(Rez.JsonData.wereld3) as Dictionary; }   // Turtle
        if (dier == 4) { return WatchUi.loadResource(Rez.JsonData.wereld4) as Dictionary; }   // Crab
        if (dier == 7) { return WatchUi.loadResource(Rez.JsonData.wereld7) as Dictionary; }   // Clownfish
        return null;
    }
}
