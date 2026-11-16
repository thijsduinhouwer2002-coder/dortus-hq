import Toybox.Application;
import Toybox.Lang;
import Toybox.WatchUi;

// Speelbare proef van het Gloop-spel (Gijs, 16 nov 2026). Eerst leuk, dan mooi:
// alles is getekend met eenvoudige vormen, nog zonder plaatjes.
class GloopApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var spel = new Spel(1234);
        var beste = Application.Storage.getValue("beste");
        if (beste instanceof Lang.Number) {
            spel.beste = beste;
        }
        return [new SpelView(spel), new SpelDelegate(spel)];
    }
}
