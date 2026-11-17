import Toybox.Application;
import Toybox.Lang;
import Toybox.WatchUi;

// Kale proef voor de reeks datawijzerplaten (Gijs, 16 nov 2026). Niet voor de winkel.
// Laat in de simulator zien wat een wijzerplaat kan lezen: de geschiedenis van Body Battery en
// stress, het weer per uur, het geheugen, en hoe lang een heuvellijn en een golf tekenen duurt.
class KernApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    var view as KernView? = null;

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var v = new KernView();
        view = v;
        return [v];
    }

    // De drager veranderde een instelling in Garmin Connect terwijl de plaat draait.
    function onSettingsChanged() as Void {
        if (view != null) {
            (view as KernView).instellingenVeranderd();
        }
    }
}
