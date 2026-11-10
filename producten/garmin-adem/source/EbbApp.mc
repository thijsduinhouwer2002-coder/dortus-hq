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

    // Stopt de app zonder opslaan (bijvoorbeeld afgesloten van buitenaf), dan wordt de opname weggegooid:
    // alleen "Save" in het pauzemenu of het einde van de sessie bewaart een activiteit.
    function onStop(state as Dictionary?) as Void {
        if (_view != null && (_view as EbbView).opname.loopt()) {
            (_view as EbbView).weggooien();
        }
    }

    private var _view as EbbView or Null = null;

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var view = new EbbView();
        _view = view;
        if (EbbBouw.DEMO) {
            // Testbouw eis 10: 2 ademhalingen van 250 ms, 2 rondes, herstel 500 ms.
            view.sessie = new Ebb.Rondes(2, 250, 2, 500, System.getTimer());
            // Eis 10, tweede helft: een opname die wordt weggegooid mag geen FIT-bestand geven.
            var eerst = new EbbOpname();
            eerst.start();
            eerst.inhouden(9);
            eerst.weggooien();
            System.println("OPNAME eerste proef weggegooid");
        }
        if (!EbbBouw.DEMO && EbbVeilig.moetTonen()) {
            return [new VeiligView(), new VeiligDelegate(view)];
        }
        return [view, new EbbDelegate(view)];
    }
}

// Eis 2: veiligheidsscherm bij de eerste start; na bevestigen nooit meer (tenzij "opnieuw tonen").
class VeiligView extends WatchUi.View {
    function initialize() {
        View.initialize();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var regels = ["Sit or lie down.", "Never in or near water,", "never while driving.", "Dizzy? Stop."];
        var f = Graphics.FONT_XTINY;
        var lh = dc.getFontHeight(f);
        var y = h / 2 - (regels.size() * lh) / 2 - lh / 2;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < regels.size(); i += 1) {
            dc.drawText(w / 2, y + i * lh, f, regels[i], Graphics.TEXT_JUSTIFY_CENTER);
        }
        dc.setColor(0x00AAFF, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, y + regels.size() * lh + lh / 2, f, "Press start: OK", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

class VeiligDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbView;

    function initialize(view as EbbView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onSelect() as Boolean {
        EbbVeilig.bevestig();
        WatchUi.switchToView(_view, new EbbDelegate(_view), WatchUi.SLIDE_LEFT);
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
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
    var koraal as Boolean = false;
    private var _gestart as Boolean = false;
    private var _lapsGesloten as Number = 0;

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            sessie.segmentStart = System.getTimer();
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
        for (var i = 0; i <= EbbProfiel.gehaald(tijd); i += 1) {
            EbbProfiel.eersteKeer(i);
        }
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
        var record = EbbProfiel.record();
        koraal = EbbProfiel.nieuwRecord(sessie.inhoudtijden, record * 1000 + 999);
        if (koraal) {
            EbbProfiel.bewaarRecord(sessie.inhoudtijden[EbbProfiel.diepste(sessie.inhoudtijden)] / 1000);
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
            tekenProfiel(dc, w, h);
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, h / 6, Graphics.FONT_SMALL, woord, Graphics.TEXT_JUSTIFY_CENTER);
        dc.drawText(w / 2, h / 2, Graphics.FONT_NUMBER_THAI_HOT, groot, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        if (fase == Ebb.FASE_INHOUDEN) {
            var d = EbbProfiel.dier(sessie.verstreken(nu));
            if (d >= 0) {
                var namen = ["a fish", "a jellyfish", "a turtle", "a whale"];
                dc.drawText(w / 2, (h * 3) / 4, Graphics.FONT_XTINY, namen[d] + " swims by", Graphics.TEXT_JUSTIFY_CENTER);
            }
        }
    }

    // Eis 7: duikprofiel na de sessie, een V per ronde, lichtpuntje bij de diepste, koraal bij een nieuw record.
    // Voorlopig uiterlijk tot de schets van Mila.
    function tekenProfiel(dc as Graphics.Dc, w as Number, h as Number) as Void {
        var t = sessie.inhoudtijden;
        if (t.size() == 0) {
            return;
        }
        var p = EbbProfiel.vPunten(t, w / 6, h / 3, (w * 2) / 3, h / 3);
        dc.setPenWidth(3);
        dc.setColor(0x00FFFF, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i + 1 < p.size(); i += 1) {
            dc.drawLine(p[i][0], p[i][1], p[i + 1][0], p[i + 1][1]);
        }
        var diep = p[2 * EbbProfiel.diepste(t) + 1];
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(diep[0], diep[1], 5);
        if (koraal) {
            dc.setColor(0xFF5555, Graphics.COLOR_TRANSPARENT);
            dc.fillCircle(diep[0] - 8, diep[1] + 10, 4);
            dc.fillCircle(diep[0] + 8, diep[1] + 10, 4);
            dc.fillCircle(diep[0], diep[1] + 14, 4);
        }
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
