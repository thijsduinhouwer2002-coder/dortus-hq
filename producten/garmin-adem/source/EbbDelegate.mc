import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

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

    // Wat terug doet: tijdens inhouden stoppen, na de sessie naar het menu (nooit het pauzemenu,
    // keuring bouw 1 punt 1), anders het pauzemenu (doorgaan, opslaan, weggooien).
    function terugActie() as Symbol {
        var f = _view.sessie.fase;
        if (f == Ebb.FASE_KLAAR) {
            return :menu;
        }
        return (f == Ebb.FASE_INHOUDEN) ? :stop : :pauze;
    }

    function onBack() as Boolean {
        var actie = terugActie();
        if (actie == :stop) {
            return stop();
        }
        if (actie == :menu) {
            // De sessie is af en al bewaard (tik slaat op bij FASE_KLAAR); opslaan() telt hoogstens één keer.
            _view.opslaan();
            var mv = new EbbMenuView();
            WatchUi.switchToView(mv, new EbbMenuDelegate(mv), WatchUi.SLIDE_RIGHT);
            return true;
        }
        _view.pauzeer(System.getTimer());
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

    // Aanraakscherm uit tijdens een sessie (productkeuring): tikken en vegen doen niets, alleen de knoppen werken.
    // Na de sessie mag vegen weer wisselen tussen vandaag en 8 weken.
    function aanraakAan() as Boolean {
        return _view.sessie.fase == Ebb.FASE_KLAAR;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return !aanraakAan();
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        return !aanraakAan();
    }

    // Na de sessie wisselen omhoog en omlaag in de rij eindscherm, today, 8 weeks; anders stoppen ze het inhouden.
    function wissel() as Boolean {
        if (_view.sessie.fase == Ebb.FASE_KLAAR) {
            if (_view.einde) {
                _view.einde = false;
                _view.getij = false;
            } else if (!_view.getij) {
                _view.getij = true;
            } else {
                _view.einde = true;
            }
            WatchUi.requestUpdate();
            return true;
        }
        return stop();
    }

    function onNextPage() as Boolean {
        return wissel();
    }

    function onPreviousPage() as Boolean {
        return wissel();
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
        if (id == :doorgaan) {
            _view.hervat(System.getTimer());
        } else if (id == :opslaan) {
            // Keuring bouw 4 punt 9: na opslaan het eindscherm (met een verdiend dier), niet meteen de app dicht.
            _view.opslaanEnTonen();
        } else if (id == :weggooien) {
            _view.weggooien();
            System.exit();
        }
    }

    // Terug in het pauzemenu is ook doorgaan.
    function onBack() as Void {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        _view.hervat(System.getTimer());
    }
}
