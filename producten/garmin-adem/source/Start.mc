import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
module EbbStart {
    const MENU_AANTAL = 5;
    const UITLEG = "uitlegGezien";   // blad v7 scherm 1c gezien
    // Kop van het startscherm (blad v5, 1b): "Rounds 3 x 30".
    // Blad v6 scherm 1b: "3 rounds · 30 breaths".
    function startKop() as String {
        var r = EbbInstellingen.waarde(EbbInstellingen.RONDES);
        return r + (r == 1 ? " round · " : " rounds · ") + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " breaths";
    }

    // Keuring bouw 2 punt 12: "Box" weg (besluit 2); in het menu staat alleen Calm 4-7-8 (Ebb.calm()).
    const CALM_NAAM = "4-7-8";

    // Duur van een Calm-sessie: onder 1 minuut in seconden ("45 s"), anders afgerond op minuten ("4 min").
    function duurTekst(ms as Number) as String {
        if (ms < 60000) {
            return (ms / 1000) + " s";
        }
        return ((ms + 30000) / 60000) + " min";
    }

    function eigenTekst() as String {
        var p = EbbInstellingen.eigenPatroon();
        return (p[0] / 1000) + "-" + (p[1] / 1000) + "-" + (p[2] / 1000) + "-" + (p[3] / 1000);
    }


}


// Blad v6 scherm 1 (keuring 01:55, besluit 22:53 punt 7): eigen startscherm in plaats van een systeemmenu.
// "Ebb" bovenaan, twee gelijke pillen Rounds en Calm 4-7-8 (gekozen = dikke schuimrand), daaronder "Sea log · Settings",
// onderaan je eigen dier op de zandbodem van het thuiswater (Thuis.mc). Box staat er niet meer in; My pattern zit in de instellingen.
class EbbMenuView extends WatchUi.View {
    var keuze as Number = 0;   // 0 Rounds, 1 Calm 4-7-8, 2 Sea log, 3 Settings, 4 Today (EbbStart.MENU_AANTAL)

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        System.println("MENU keuze " + keuze);
    }

    function pilRand(dc as Graphics.Dc, d as Number, y as Float, tekst as String, gekozen as Boolean) as Void {
        var bw = (d * 0.62).toNumber();
        var fh = dc.getFontHeight(EbbTeken.fS());
        var bh = (d * 0.15).toNumber();
        bh = bh < fh + 6 ? fh + 6 : bh;
        var lw = (d / 130 > 2 ? d / 130 : 2) * (gekozen ? 2 : 1);
        var x0 = d / 2 - bw / 2;
        var y0 = (d * y).toNumber() - bh / 2;
        // Op het thuiswater: rand in 00AAFF (0055AA viel weg tegen het water), binnenkant nachtblauw.
        dc.setColor(gekozen ? EbbTeken.SCHUIM : EbbTeken.ZEE_KLEUR[0], Graphics.COLOR_TRANSPARENT);
        dc.fillRoundedRectangle(x0, y0, bw, bh, bh / 2);
        dc.setColor(EbbTeken.NACHT, EbbTeken.NACHT);
        dc.fillRoundedRectangle(x0 + lw, y0 + lw, bw - 2 * lw, bh - 2 * lw, (bh - 2 * lw) / 2);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), EbbTeken.fS(), tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        if (EbbBouw.PLAATJE) {
            // Bouw 3 punt 5: hoogtes van de systeemletters, zodat Barlow straks precies even hoog wordt (staat in het log).
            System.println("LETTERHOOGTE d " + d + " xtiny " + dc.getFontHeight(Graphics.FONT_XTINY) + " small " + dc.getFontHeight(Graphics.FONT_SMALL)
                + " medium " + dc.getFontHeight(EbbTeken.fM()) + " ascent " + Graphics.getFontAscent(EbbTeken.fX()) + "/" + Graphics.getFontAscent(EbbTeken.fS()) + "/" + Graphics.getFontAscent(EbbTeken.fM()));
        }
        // Keuring bouw 1 punt 6: je eigen dier (niet de rode vis), in de eigen kleuren; zonder dier alleen de zee.
        var eigen = EbbTrouw.zwemmer();
        // Thuiswater (Thuis.mc) in plaats van de zeebanden. Tekstvakken: "Ebb", de twee pillen, de menuregel en het
        // dier (of de twee regels "first friend"). Met dier ligt het zand onder het dier, anders 6/260 onder de regels.
        var f = EbbTeken.fX();
        var fh = dc.getFontHeight(f);
        var m = "  ·  ";
        var tot = regelBreed(dc, f, m);
        if (tot > d * 0.84) {
            m = " · ";
            tot = regelBreed(dc, f, m);
        }
        var c = d / 2;
        var yb = (d * 0.783).toNumber() + 4 + fh / 2;
        var half = (eigen >= 0) ? d / 10 : dc.getTextWidthInPixels("after 1 session", f) / 2;
        var vakken = [
            c - d / 6, (d * 0.165).toNumber() - dc.getFontHeight(EbbTeken.fM()) / 2, c + d / 6, (d * 0.165).toNumber() + dc.getFontHeight(EbbTeken.fM()) / 2,
            c - (d * 0.31).toNumber(), (d * 0.25).toNumber(), c + (d * 0.31).toNumber(), (d * 0.595).toNumber(),
            c - tot / 2 - d / 30, (d * 0.655).toNumber() - fh / 2 - d / 60, c + tot / 2 + d / 30, (d * 0.655).toNumber() + fh / 2 + d / 60,
            c - half, (eigen >= 0) ? (d * 0.715).toNumber() : yb - fh / 2, c + half, (eigen >= 0) ? (d * 0.875).toNumber() : yb + fh + fh / 2
        ] as Array<Number>;
        var zand = (eigen >= 0) ? (d * 0.855).toNumber() : yb + fh + fh / 2 + EbbTeken.px(d, 6) + 3;
        if (!EbbThuis.teken(dc, d, zand, vakken, EbbThuis.MENU)) {
            WatchUi.requestUpdate();
        }
        if (eigen >= 0) {
            // Keuring bouw 2 punt 7: het dier ±80 px breed op 454 (0,17 D), op de kamlijn (0,775 D), onder "Sea log · Settings".
            // Keuring bouw 3 punt 8: menu-dier 80 px breed op 454 (0,176 D).
            var mm = EbbDierMaat.inVak(eigen, (d * 0.176).toNumber(), (d * 0.14).toNumber());
            EbbDierVoorraad.teken(dc, eigen, d / 2, (d * 0.795).toNumber(), mm, EbbThuis.nacht() ? EbbDierPlaatje.NACHT : EbbDierPlaatje.GEVONDEN);
        } else {
            // Keuring bouw 4 punt 11: bij de eerste start een belofte waar straks het dier zwemt.
            // Keuring bouw 6 punt 5 (scène 28): beide regels helemaal in het water, 4 px onder 0,783 D (yb, hierboven).
            var fx = fh;
            dc.setColor(EbbTeken.LICHT, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, yb, EbbTeken.fX(), "first friend", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            dc.drawText(d / 2, yb + fx, EbbTeken.fX(), "after 1 session", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.165).toNumber(), EbbTeken.fM(), "Ebb", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        pilRand(dc, d, 0.335, "Rounds", keuze == 0);
        pilRand(dc, d, 0.510, "Calm 4-7-8", keuze == 1);
        // "Sea log · Settings · Today": het gekozen woord wit in een pil met schuimrand, de andere lichtcyaan.
        // Keuring bouw 7 punt 6: today en 8 weeks ook vanuit het menu. Past de regel niet, dan smallere tussenruimte.
        var y = (d * 0.655).toNumber();
        var wm = dc.getTextWidthInPixels(m, f);
        var x = d / 2 - tot / 2;
        for (var i = 0; i < WOORDEN.size(); i += 1) {
            var ww = dc.getTextWidthInPixels(WOORDEN[i], f);
            var gekozen = (keuze == i + 2);
            dc.setColor(gekozen ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(x, y, f, WOORDEN[i], Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
            if (gekozen) {
                // Keuring bouw 8 punt 3: het gekozen woord in een pil met schuimrand (was een streep van 1 px).
                // Beeld run 43113167622: met de halve tussenruimte raakte de rand het puntje ernaast; nu een derde.
                var pad = wm / 3;
                var maxPad = (d * 0.03).toNumber();
                pad = pad > maxPad ? maxPad : (pad < 3 ? 3 : pad);
                // Keuring bouw 9 punt 1: de staart van de "y" in "Today" raakte de rand; nu 3 px lucht (5 op 454).
                var om = d / 90 > 3 ? d / 90 : 3;
                var ph = fh + 2 * om;
                dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(d / 130 > 2 ? d / 130 : 2);
                dc.drawRoundedRectangle(x - pad, y - ph / 2, ww + 2 * pad, ph, ph / 2);
                dc.setPenWidth(1);
            }
            x += ww;
            // Tot hier (midden van de tussenruimte) hoort een tik bij dit woord.
            grens[i] = x + wm / 2;
            if (i < WOORDEN.size() - 1) {
                dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
                dc.drawText(x, y, f, m, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
                x += wm;
            }
        }
    }

    const WOORDEN = ["Sea log", "Settings", "Today"] as Array<String>;
    var grens as Array<Number> = [0, 0, 0] as Array<Number>;

    function regelBreed(dc as Graphics.Dc, f as Graphics.FontType, m as String) as Number {
        var t = (WOORDEN.size() - 1) * dc.getTextWidthInPixels(m, f);
        for (var i = 0; i < WOORDEN.size(); i += 1) {
            t += dc.getTextWidthInPixels(WOORDEN[i], f);
        }
        return t;
    }

    // Welke keuze hoort bij een tik op x in de onderste regel (2 Sea log, 3 Settings, 4 Today).
    function keuzeBij(x as Number) as Number {
        if (x < grens[0]) {
            return 2;
        }
        return x < grens[1] ? 3 : 4;
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
            _view.keuze = _view.keuzeBij(xy[0]);
        } else {
            return false;
        }
        return onSelect();
    }

    function onSelect() as Boolean {
        var k = _view.keuze;
        System.println("MENU kies " + k);
        EbbNaarMenu.onderop = true;
        if (k == 0) {
            // Blad v5 (S2): eerst de startcheck (en bij de eerste keer de uitleg), pas dan de sessie.
            var sc = new StartCheckView();
            WatchUi.pushView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
        } else if (k == 1) {
            // Besluit 11 nov 04:30 (besluit 4): ook voor Calm eerst "Sit or lie down".
            var sc = new StartCheckView();
            sc.zetCalm();
            WatchUi.pushView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
        } else if (k == 2) {
            var dv = new DierenView();
            WatchUi.pushView(dv, new DierenDelegate(dv), WatchUi.SLIDE_LEFT);
        } else if (k == 3) {
            var iv = new EbbInstellingenView();
            WatchUi.pushView(iv, new EbbInstellingenDelegate(iv), WatchUi.SLIDE_LEFT);
        } else {
            var ov = new EbbOverzichtView();
            WatchUi.pushView(ov, new EbbOverzichtDelegate(ov), WatchUi.SLIDE_LEFT);
        }
        return true;
    }

    // Keuring bouw 4 punt 12: terug in het startmenu sluit de app; het systeem doet dat zelf als we false geven
    // (geen System.exit met een onbereikbare return erachter).
    function onBack() as Boolean {
        return false;
    }
}
