import Toybox.Application;
import Toybox.Lang;
import Toybox.WatchUi;

// Wijzerplaat "Gloop's Hat Tower", kale proef (Gijs, 16 nov 2026): elke 1.000 stappen een hoed
// op Gloops toren, de kroon bij het stapdoel. Ontwerp van Mila, plaatjes uit de kit van het spel.
class GloopFaceApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        return [new GloopFaceView()];
    }
}
