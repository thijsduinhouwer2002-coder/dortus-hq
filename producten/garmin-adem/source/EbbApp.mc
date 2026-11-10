import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Timer;
import Toybox.WatchUi;

// Ebb (Gijs, 10 nov 2026): eerste bouwstap. Rondes met water dat stijgt en zakt, inhouden met groot getal.
// Uiterlijk is voorlopig; Mila maakt de stijl (ontwerp/garmin/tij-stijl.md).
class EbbApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var view = new EbbView();
        return [view, new EbbDelegate(view)];
    }
}

class EbbView extends WatchUi.View {
    var sessie as Ebb.Rondes;
    private var _timer as Timer.Timer = new Timer.Timer();

    function initialize() {
        View.initialize();
        sessie = new Ebb.Rondes(30, 1600, 3, 15000, System.getTimer());
    }

    function onShow() as Void {
        _timer.start(method(:tik), 100, true);
    }

    function onHide() as Void {
        _timer.stop();
    }

    function tik() as Void {
        sessie.bijwerken(System.getTimer());
        WatchUi.requestUpdate();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var nu = System.getTimer();
        sessie.bijwerken(nu);
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();

        var fase = sessie.fase;
        var kleur = 0x00AAFF;
        if (fase == Ebb.FASE_INHOUDEN) {
            var diepte = sessie.verstreken(nu) / 15000;
            kleur = (diepte < 1) ? 0x0055AA : 0x000055;
        }
        var lijn = h - (sessie.water(nu) * h * 0.8).toNumber() - h / 10;
        dc.setColor(kleur, kleur);
        dc.fillRectangle(0, lijn, w, h - lijn);
        dc.setColor(0x00FFFF, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(3);
        dc.drawLine(0, lijn, w, lijn);

        var woord = "";
        var groot = "";
        if (fase == Ebb.FASE_ADEMEN) {
            woord = sessie.isIn(nu) ? "in" : "out";
            groot = sessie.ademhaling(nu).toString();
        } else if (fase == Ebb.FASE_INHOUDEN) {
            woord = "hold";
            var s = sessie.verstreken(nu) / 1000;
            groot = (s / 60).toString() + ":" + (s % 60).format("%02d");
        } else if (fase == Ebb.FASE_HERSTEL) {
            woord = "hold in";
            groot = ((sessie.herstelMs - sessie.verstreken(nu)) / 1000 + 1).toString();
        } else {
            woord = "done";
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, h / 6, Graphics.FONT_SMALL, woord, Graphics.TEXT_JUSTIFY_CENTER);
        dc.drawText(w / 2, h / 2, Graphics.FONT_NUMBER_THAI_HOT, groot, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}

class EbbDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbView;

    function initialize(view as EbbView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    // Stoptijd wordt in de knophandler vastgelegd (eis 4): de klok wordt gelezen in de handler zelf.
    function stop() as Boolean {
        return stopOp(System.getTimer());
    }

    // Los van de klok, zodat de toets een nagebootste tijd kan geven.
    function stopOp(nu as Number) as Boolean {
        if (_view.sessie.fase == Ebb.FASE_INHOUDEN) {
            _view.sessie.stopInhouden(nu);
            WatchUi.requestUpdate();
            return true;
        }
        return false;
    }

    // Wat terug doet: tijdens inhouden stoppen, anders het pauzemenu (doorgaan, opslaan, weggooien).
    function terugActie() as Symbol {
        return (_view.sessie.fase == Ebb.FASE_INHOUDEN) ? :stop : :pauze;
    }

    function onBack() as Boolean {
        if (terugActie() == :stop) {
            return stop();
        }
        var menu = new WatchUi.Menu2({:title => "Paused"});
        menu.addItem(new WatchUi.MenuItem("Resume", null, :doorgaan, null));
        menu.addItem(new WatchUi.MenuItem("Save", null, :opslaan, null));
        menu.addItem(new WatchUi.MenuItem("Discard", null, :weggooien, null));
        WatchUi.pushView(menu, new PauzeDelegate(), WatchUi.SLIDE_UP);
        return true;
    }

    function onSelect() as Boolean {
        return stop();
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return stop();
    }

    function onNextPage() as Boolean {
        return stop();
    }

    function onPreviousPage() as Boolean {
        return stop();
    }
}

// Pauzemenu. Opslaan en weggooien sluiten nu nog alleen de app; opname volgt bij eis 10.
class PauzeDelegate extends WatchUi.Menu2InputDelegate {
    function initialize() {
        Menu2InputDelegate.initialize();
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (id == :opslaan || id == :weggooien) {
            System.exit();
        }
    }
}
