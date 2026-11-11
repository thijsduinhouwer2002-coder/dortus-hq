import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
module EbbStart {
    const MENU_AANTAL = 4;
    const UITLEG = "uitlegGezien";   // blad v7 scherm 1c gezien
    // Kop van het startscherm (blad v5, 1b): "Rounds 3 x 30".
    // Blad v6 scherm 1b: "3 rounds · 30 breaths".
    function startKop() as String {
        var r = EbbInstellingen.waarde(EbbInstellingen.RONDES);
        return r + (r == 1 ? " round · " : " rounds · ") + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " breaths";
    }

    function rondesKop() as String {
        return "Rounds " + EbbInstellingen.waarde(EbbInstellingen.RONDES) + " x " + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN);
    }

    // De drie vaste patronen uit Ebb.patronen(), in dezelfde volgorde.
    const PATROON_NAMEN = ["Box", "4-7-8", "Calm"] as Array<String>;

    function eigenTekst() as String {
        var p = EbbInstellingen.eigenPatroon();
        return (p[0] / 1000) + "-" + (p[1] / 1000) + "-" + (p[2] / 1000) + "-" + (p[3] / 1000);
    }


}


// Blad v6 scherm 1 (keuring 01:55, besluit 22:53 punt 7): eigen startscherm in plaats van een systeemmenu.
// "Ebb" bovenaan, twee gelijke pillen Rounds en Calm 4-7-8 (gekozen = dikke schuimrand), daaronder "Sea log · Settings",
// onderaan de zee met je eigen dier. Box staat er niet meer in; My pattern zit in de instellingen.
class EbbMenuView extends WatchUi.View {
    var keuze as Number = 0;   // 0 Rounds, 1 Calm 4-7-8, 2 Sea log, 3 Settings (EbbStart.MENU_AANTAL)

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        System.println("MENU keuze " + keuze);
    }

    function pilRand(dc as Graphics.Dc, d as Number, y as Float, tekst as String, gekozen as Boolean) as Void {
        var bw = (d * 0.62).toNumber();
        var fh = dc.getFontHeight(Graphics.FONT_SMALL);
        var bh = (d * 0.15).toNumber();
        bh = bh < fh + 6 ? fh + 6 : bh;
        var lw = (d / 130 > 2 ? d / 130 : 2) * (gekozen ? 2 : 1);
        var x0 = d / 2 - bw / 2;
        var y0 = (d * y).toNumber() - bh / 2;
        dc.setColor(gekozen ? EbbTeken.SCHUIM : EbbTeken.ZEE_KLEUR[1], Graphics.COLOR_TRANSPARENT);
        dc.fillRoundedRectangle(x0, y0, bw, bh, bh / 2);
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.fillRoundedRectangle(x0 + lw, y0 + lw, bw - 2 * lw, bh - 2 * lw, (bh - 2 * lw) / 2);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), Graphics.FONT_SMALL, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        EbbTeken.golf(dc, d, 0.775, d * 0.008, EbbTeken.ZEE_KLEUR[1], 0.0, true);
        EbbTeken.golf(dc, d, 0.86, d * 0.008, EbbTeken.ZEE_KLEUR[2], 1.3, false);
        // Keuring bouw 1 punt 6: je eigen dier (niet de rode vis), in de eigen kleuren; zonder dier alleen de zee.
        var eigen = EbbTrouw.zwemmer();
        if (eigen >= 0) {
            EbbDierData.teken(dc, eigen, d / 2, (d * 0.875).toNumber(), (d * 0.05).toNumber(), -1);
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.165).toNumber(), Graphics.FONT_MEDIUM, "Ebb", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        pilRand(dc, d, 0.335, "Rounds", keuze == 0);
        pilRand(dc, d, 0.510, "Calm 4-7-8", keuze == 1);
        // "Sea log · Settings": het gekozen woord wit met een schuimstreep eronder, het andere lichtcyaan.
        var f = Graphics.FONT_XTINY;
        var a = "Sea log";
        var m = "  ·  ";
        var b = "Settings";
        var wa = dc.getTextWidthInPixels(a, f);
        var wm = dc.getTextWidthInPixels(m, f);
        var wb = dc.getTextWidthInPixels(b, f);
        var x0 = d / 2 - (wa + wm + wb) / 2;
        var y = (d * 0.655).toNumber();
        var fh = dc.getFontHeight(f);
        dc.setColor(keuze == 2 ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0, y, f, a, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + wa, y, f, m, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(keuze == 3 ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + wa + wm, y, f, b, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        if (keuze >= 2) {
            dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
            var lw = d / 130 > 2 ? d / 130 : 2;
            var xs = keuze == 2 ? x0 : x0 + wa + wm;
            dc.fillRectangle(xs, y + fh / 2, keuze == 2 ? wa : wb, lw);
        }
    }
}

class EbbMenuDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbMenuView;

    function initialize(view as EbbMenuView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function stap(n as Number) as Boolean {
        _view.keuze = (_view.keuze + n + EbbStart.MENU_AANTAL) % EbbStart.MENU_AANTAL;
        System.println("MENU keuze " + _view.keuze);
        WatchUi.requestUpdate();
        return true;
    }

    function onNextPage() as Boolean {
        return stap(1);
    }

    function onPreviousPage() as Boolean {
        return stap(-1);
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        var r = evt.getDirection();
        if (r == WatchUi.SWIPE_UP) {
            return stap(1);
        } else if (r == WatchUi.SWIPE_DOWN) {
            return stap(-1);
        }
        return false;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        var xy = evt.getCoordinates();
        var d = System.getDeviceSettings().screenWidth;
        var y = xy[1].toFloat() / d;
        if (y < 0.42) {
            _view.keuze = 0;
        } else if (y < 0.59) {
            _view.keuze = 1;
        } else if (y < 0.74) {
            _view.keuze = (xy[0] < d / 2) ? 2 : 3;
        } else {
            return false;
        }
        return onSelect();
    }

    function onSelect() as Boolean {
        var k = _view.keuze;
        System.println("MENU kies " + k);
        if (k == 0) {
            // Blad v5 (S2): eerst de startcheck (en bij de eerste keer de uitleg), pas dan de sessie.
            var sc = new StartCheckView();
            WatchUi.pushView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
        } else if (k == 1) {
            var rv = new RustigView(Ebb.patronen()[1], EbbStart.PATROON_NAMEN[1]);
            (Application.getApp() as EbbApp).zetRustig(rv);
            WatchUi.pushView(rv, new RustigDelegate(rv), WatchUi.SLIDE_LEFT);
        } else if (k == 2) {
            var dv = new DierenView();
            WatchUi.pushView(dv, new DierenDelegate(dv), WatchUi.SLIDE_LEFT);
        } else {
            var iv = new EbbInstellingenView();
            WatchUi.pushView(iv, new EbbInstellingenDelegate(iv), WatchUi.SLIDE_LEFT);
        }
        return true;
    }

    function onBack() as Boolean {
        System.exit();
        return true;
    }
}
