import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Keuring bouw 7 punt 3: schermen stapelen niet. Na een sessie terug naar het menu dat er al onder ligt
// (popView); alleen als er geen menu onder ligt (testbouw, plaatjesbouw) komt er een nieuw menu.
module EbbNaarMenu {
    var onderop as Boolean = false;

    function ga(slide as WatchUi.SlideType) as Void {
        if (onderop) {
            WatchUi.popView(slide);
            return;
        }
        var mv = new EbbMenuView();
        WatchUi.switchToView(mv, new EbbMenuDelegate(mv), slide);
    }
}

// Keuring bouw 7 punt 6: today en 8 weeks vanuit het menu (ook na Calm). Zelfde tekenwerk als na een sessie
// (EbbOverzicht); omhoog, omlaag, START of een tik wisselt tussen de twee, BACK gaat terug naar het menu.
class EbbOverzichtView extends WatchUi.View {
    var weken as Boolean = false;

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        System.println("OVERZICHT " + (weken ? "8 weeks" : "today"));
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        if (weken) {
            EbbOverzicht.weken(dc, d, null);
        } else {
            EbbOverzicht.vandaag(dc, d, null);
        }
    }
}

class EbbOverzichtDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbOverzichtView;

    function initialize(view as EbbOverzichtView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function wissel() as Boolean {
        _view.weken = !_view.weken;
        System.println("OVERZICHT " + (_view.weken ? "8 weeks" : "today"));
        WatchUi.requestUpdate();
        return true;
    }

    function onNextPage() as Boolean {
        return wissel();
    }

    function onPreviousPage() as Boolean {
        return wissel();
    }

    function onSelect() as Boolean {
        return wissel();
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return wissel();
    }
}
