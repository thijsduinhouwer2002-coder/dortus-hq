import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
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

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var view = new EbbView();
        if (EbbBouw.DEMO) {
            // Testbouw eis 10: 2 ademhalingen van 250 ms, 2 rondes, herstel 500 ms.
            view.sessie = new Ebb.Rondes(2, 250, 2, 500, System.getTimer());
        }
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

    var opname as EbbOpname = new EbbOpname();
    private var _gestart as Boolean = false;
    private var _lapsGesloten as Number = 0;

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            opname.start();
        }
        _timer.start(method(:tik), 100, true);
    }

    // Stop het inhouden op tijdstip nu (uit de knophandler of de testbouw) en zet de tijd op de lap.
    function stopInhouden(nu as Number) as Boolean {
        var tijd = sessie.stopInhouden(nu);
        if (tijd < 0) {
            return false;
        }
        opname.inhouden((tijd + 500) / 1000);
        return true;
    }

    // Dagnummer van de lokale datum (dagen sinds 1970).
    static function vandaag() as Number {
        return (Time.today().value() + System.getClockTime().timeZoneOffset) / 86400;
    }

    // Opslaan: activiteit bewaren en de inhoudtijden in de 56 dagen zetten.
    function opslaan() as Boolean {
        var ok = opname.opslaan();
        System.println("OPNAME opgeslagen " + ok + " laps " + (opname.laps + 1) + " beste " + opname.besteS);
        var opslag = new EbbOpslag();
        var dag = vandaag();
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            opslag.voegToe(dag, (sessie.inhoudtijden[i] + 500) / 1000);
        }
        opslag.bewaar();
        if (EbbBouw.DEMO) {
            // Eis 10, tweede helft: een opname die wordt weggegooid mag geen FIT-bestand geven.
            var tweede = new EbbOpname();
            tweede.start();
            tweede.inhouden(9);
            tweede.weggooien();
            System.println("OPNAME tweede weggegooid");
        }
        return ok;
    }

    function weggooien() as Void {
        opname.weggooien();
        System.println("OPNAME weggegooid");
    }

    function onHide() as Void {
        _timer.stop();
    }

    private var _vorigeFase as Number = -1;
    private var _vorigIn as Boolean = false;

    function tik() as Void {
        var nu = System.getTimer();
        if (EbbBouw.DEMO && sessie.fase == Ebb.FASE_INHOUDEN) {
            var doel = EbbBouw.INHOUD_MS[sessie.ronde % EbbBouw.INHOUD_MS.size()];
            if (sessie.verstreken(nu) >= doel) {
                stopInhouden(sessie.segmentStart + doel);
            }
        }
        sessie.bijwerken(nu);
        // Elke afgeronde ronde die niet de laatste is sluit een lap (onUpdate kan de ronde al verder gezet hebben).
        while (_lapsGesloten < sessie.ronde && _lapsGesloten < sessie.rondes - 1) {
            opname.rondeKlaar();
            _lapsGesloten += 1;
        }
        if (sessie.fase == Ebb.FASE_KLAAR && opname.loopt()) {
            opslaan();
        }
        trilBijWissel(nu);
        WatchUi.requestUpdate();
    }

    // Trilt één keer bij elke wissel van fase of van in naar uit (eis 6).
    function trilBijWissel(nu as Number) as Void {
        var fase = sessie.fase as Number;
        var isIn = (fase == Ebb.FASE_ADEMEN) && sessie.isIn(nu);
        if (fase != _vorigeFase) {
            if (fase == Ebb.FASE_ADEMEN) {
                EbbTrillen.tril(_vorigeFase == Ebb.FASE_HERSTEL ? EbbTrillen.M_LOS : EbbTrillen.M_IN);
            } else if (fase == Ebb.FASE_INHOUDEN) {
                EbbTrillen.tril(EbbTrillen.M_INHOUDEN);
            } else if (fase == Ebb.FASE_HERSTEL) {
                EbbTrillen.tril(EbbTrillen.M_HERSTEL);
            } else if (fase == Ebb.FASE_KLAAR) {
                EbbTrillen.tril(EbbTrillen.M_KLAAR);
            }
        } else if (fase == Ebb.FASE_ADEMEN && isIn != _vorigIn) {
            EbbTrillen.tril(isIn ? EbbTrillen.M_IN : EbbTrillen.M_UIT);
        }
        _vorigeFase = fase;
        _vorigIn = isIn;
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
        if (_view.stopInhouden(nu)) {
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
        WatchUi.pushView(menu, new PauzeDelegate(_view), WatchUi.SLIDE_UP);
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

// Pauzemenu: doorgaan, opslaan (activiteit en 56 dagen) of weggooien (geen FIT-bestand).
class PauzeDelegate extends WatchUi.Menu2InputDelegate {
    private var _view as EbbView;

    function initialize(view as EbbView) {
        Menu2InputDelegate.initialize();
        _view = view;
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (id == :opslaan) {
            _view.opslaan();
            System.exit();
        } else if (id == :weggooien) {
            _view.weggooien();
            System.exit();
        }
    }
}
