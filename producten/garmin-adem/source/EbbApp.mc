import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Ebb (Gijs, 10 nov 2026): eerste bouwstap. Rondes met water dat stijgt en zakt, inhouden met groot getal.
// Uiterlijk is voorlopig; Mila maakt de stijl (ontwerp/garmin/tij-stijl.md).
class EbbApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    // Stopt de app zonder opslaan (bijvoorbeeld afgesloten van buitenaf), dan wordt de opname weggegooid:
    // alleen "Save" in het pauzemenu of het einde van de sessie bewaart een activiteit.
    function onStop(state as Dictionary?) as Void {
        if (_view != null && (_view as EbbView).opname.loopt()) {
            (_view as EbbView).weggooien();
        }
        if (_rustig != null && (_rustig as RustigView).opname.loopt()) {
            (_rustig as RustigView).opname.weggooien();
        }
    }

    private var _rustig as RustigView or Null = null;

    function zetRustig(view as RustigView) as Void {
        _rustig = view;
    }

    private var _view as EbbView or Null = null;

    function zetView(view as EbbView) as Void {
        _view = view;
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var view = new EbbView();
        _view = view;
        if (EbbBouw.DEMO) {
            // Testbouw eis 10: 2 ademhalingen van 250 ms, 2 rondes, herstel 500 ms.
            view.sessie = new Ebb.Rondes(2, 250, 2, 500, System.getTimer());
            // Eis 10, tweede helft: bij elke tweede start van de testbouw wordt een opname weggegooid;
            // de workflow kijkt dat die start geen FIT-bestand geeft. (Weggooien en opslaan in één start
            // liet in de simulator de weggegooide lap in het volgende bestand achter.)
            var keer = Application.Storage.getValue("demokeer");
            var k = (keer instanceof Number) ? keer as Number : 0;
            Application.Storage.setValue("demokeer", k + 1);
            if (k % 2 == 1) {
                view.opnemen = false;
                var weg = new EbbOpname();
                weg.start();
                // Proef 10 nov 07:05: zonder setData, om te zien of de lek de lap zelf is of de veldwaarde.
                weg.weggooien();
                System.println("OPNAME proef weggegooid");
            }
        }
        if (EbbBouw.PLAATJE) {
            // Testbeelden van elk scherm, één scène per start: zie Scenes.mc.
            return EbbScenes.start(self, view);
        }
        if (!EbbBouw.DEMO) {
            // Keuring bouw 3 punt 10: oude reeks in dagen één keer wissen (opslagversie 2).
            EbbTrouw.werkOpslagBij();
            EbbTrillen.aan = EbbInstellingen.trillen();
            if (EbbVeilig.moetTonen()) {
                var vv = new VeiligView();
                return [vv, new VeiligDelegate(vv)];
            }
            var mv = new EbbMenuView();
            return [mv, new EbbMenuDelegate(mv)];
        }
        return [view, new EbbDelegate(view)];
    }
}
