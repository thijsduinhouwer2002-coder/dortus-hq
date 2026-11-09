import Toybox.Application;
import Toybox.Lang;
import Toybox.WatchUi;

// Proef van de bouwstraat (Gijs, 9 nov 2026): compileren, testen en schermafbeelding in de simulator.
class ProefApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        return [new AdemView()];
    }
}
