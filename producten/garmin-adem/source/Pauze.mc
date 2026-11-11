import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Mila blad v10 punt 2 (keuring bouw 5 punt 6): het pauzemenu in Ebb-stijl in plaats van het witte systeemmenu.
// De zee staat stil (platte kamlijn), bovenaan "paused" en welke ronde en hoe lang, drie keuzes Resume, Save, Discard;
// de gekozen keuze in een pil van schuim, en je eigen dier (gekozen in de sea log) wijst hem aan. Startkeuze Resume.
// Maten in 1/260 D (blad v10).
class PauzeView extends WatchUi.View {
    static const KEUZES = ["Resume", "Save", "Discard"] as Array<String>;
    static const Y = [106, 144, 182] as Array<Number>;
    var keuze as Number = 0;
    var regel as String;
    var dier as Number;

    function initialize(regelTekst as String, gezelschap as Number) {
        View.initialize();
        regel = regelTekst;
        dier = gezelschap;
    }

    // Regel onder "paused": welke ronde en hoe lang het huidige stuk al duurt, bijvoorbeeld "round 2 · 1:12".
    static function regelVan(view as EbbView) as String {
        var s = view.sessie.verstreken(System.getTimer()) / 1000;
        s = s < 0 ? 0 : s;
        return "round " + (view.sessie.ronde + 1) + " · " + (s / 60) + ":" + (s % 60).format("%02d");
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        EbbZee.stil(dc, d);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, EbbTeken.px(d, 24), EbbTeken.fS(), "paused", Graphics.TEXT_JUSTIFY_CENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, EbbTeken.px(d, 56), EbbTeken.fX(), regel, Graphics.TEXT_JUSTIFY_CENTER);
        var pb = EbbTeken.px(d, 110);
        var ph = EbbTeken.px(d, 32);
        var fh = dc.getFontHeight(EbbTeken.fS());
        ph = ph < fh + 2 ? fh + 2 : ph;
        for (var i = 0; i < KEUZES.size(); i += 1) {
            var y = EbbTeken.px(d, Y[i]);
            if (i == keuze) {
                dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
                dc.fillRoundedRectangle(w / 2 - pb / 2, y - ph / 2, pb, ph, ph / 2);
                dc.setColor(EbbTeken.ZEE_KLEUR[3], Graphics.COLOR_TRANSPARENT);
            } else {
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            }
            dc.drawText(w / 2, y, EbbTeken.fS(), KEUZES[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        // Je eigen dier wijst de keuze aan: midden 22 px (in 1/260) links van de pilrand.
        if (dier >= 0) {
            EbbDierVoorraad.teken(dc, dier, w / 2 - pb / 2 - EbbTeken.px(d, 22), EbbTeken.px(d, Y[keuze]), EbbTeken.px(d, 12), EbbDierPlaatje.GEVONDEN);
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, EbbTeken.px(d, 214), EbbTeken.fX(), "the sea waits", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

// Knoppen van het pauzemenu: omhoog en omlaag kiezen, START of tik kiest, terug is doorgaan.
// Keuring bouw 6 punt 4: één delegate voor Rounds en Calm; wat Resume, Save en Discard doen komt binnen als Method.
// Discard gooit weg en gaat terug naar het startmenu in plaats van de app te sluiten.
class PauzeDelegate extends WatchUi.BehaviorDelegate {
    private var _pv as PauzeView;
    private var _hervat as Method() as Void;
    private var _opslaan as Method() as Void;
    private var _weg as Method() as Void;

    function initialize(pv as PauzeView, hervat as Method() as Void, opslaan as Method() as Void, weg as Method() as Void) {
        BehaviorDelegate.initialize();
        _pv = pv;
        _hervat = hervat;
        _opslaan = opslaan;
        _weg = weg;
    }

    function schuif(stap as Number) as Boolean {
        _pv.keuze = (_pv.keuze + stap + 3) % 3;
        WatchUi.requestUpdate();
        return true;
    }

    function onNextPage() as Boolean {
        return schuif(1);
    }

    function onPreviousPage() as Boolean {
        return schuif(-1);
    }

    function onSelect() as Boolean {
        return kies(_pv.keuze);
    }

    function kies(k as Number) as Boolean {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (k == 0) {
            _hervat.invoke();
        } else if (k == 1) {
            // Keuring bouw 4 punt 9: na opslaan het eindscherm (met een verdiend dier), niet meteen de app dicht.
            _opslaan.invoke();
        } else {
            _weg.invoke();
            EbbNaarMenu.ga(WatchUi.SLIDE_RIGHT);
        }
        return true;
    }

    // Keuring bouw 6 punt 4 (Venu, vivoactive): een tik kiest de regel waarop je tikt; buiten de regels niets.
    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        var xy = evt.getCoordinates();
        var ds = System.getDeviceSettings();
        var d = ds.screenWidth < ds.screenHeight ? ds.screenWidth : ds.screenHeight;
        var i = regelBij(d, xy[1]);
        if (i >= 0) {
            _pv.keuze = i;
            return kies(i);
        }
        return true;
    }

    // Welke regel (0 Resume, 1 Save, 2 Discard) ligt op hoogte y; -1 als de tik buiten de regels valt.
    static function regelBij(d as Number, yTik as Number) as Number {
        var half = EbbTeken.px(d, 19);
        for (var i = 0; i < PauzeView.Y.size(); i += 1) {
            var y = EbbTeken.px(d, PauzeView.Y[i]);
            if (yTik >= y - half && yTik < y + half) {
                return i;
            }
        }
        return -1;
    }

    // Terug in het pauzemenu is ook doorgaan.
    function onBack() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        _hervat.invoke();
        return true;
    }
}
