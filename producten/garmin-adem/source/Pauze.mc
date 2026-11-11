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

    function px(d as Number, v as Number) as Number {
        return (v * d + 130) / 260;
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        // Stille zee: platte kamlijn op 84, één tint 0055AA, vanaf 208 de diepte 000055.
        dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);
        dc.fillRectangle(0, px(d, 84), w, px(d, 208) - px(d, 84));
        dc.setColor(EbbTeken.ZEE_KLEUR[3], EbbTeken.ZEE_KLEUR[3]);
        dc.fillRectangle(0, px(d, 208), w, h - px(d, 208));
        dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
        dc.fillRectangle(0, px(d, 84) - 1, w, d >= 300 ? 3 : 2);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, px(d, 24), EbbTeken.fS(), "paused", Graphics.TEXT_JUSTIFY_CENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, px(d, 56), EbbTeken.fX(), regel, Graphics.TEXT_JUSTIFY_CENTER);
        var pb = px(d, 110);
        var ph = px(d, 32);
        var fh = dc.getFontHeight(EbbTeken.fS());
        ph = ph < fh + 2 ? fh + 2 : ph;
        for (var i = 0; i < KEUZES.size(); i += 1) {
            var y = px(d, Y[i]);
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
            EbbDierVoorraad.teken(dc, dier, w / 2 - pb / 2 - px(d, 22), px(d, Y[keuze]), px(d, 12), EbbDierPlaatje.GEVONDEN);
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, px(d, 214), EbbTeken.fX(), "the sea waits", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

// Knoppen van het pauzemenu: omhoog en omlaag kiezen, START of tik kiest, terug is doorgaan.
class PauzeDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbView;
    private var _pv as PauzeView;

    function initialize(view as EbbView, pv as PauzeView) {
        BehaviorDelegate.initialize();
        _view = view;
        _pv = pv;
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
        var k = _pv.keuze;
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (k == 0) {
            _view.hervat(System.getTimer());
        } else if (k == 1) {
            // Keuring bouw 4 punt 9: na opslaan het eindscherm (met een verdiend dier), niet meteen de app dicht.
            _view.opslaanEnTonen();
        } else {
            _view.weggooien();
            System.exit();
        }
        return true;
    }

    // Terug in het pauzemenu is ook doorgaan.
    function onBack() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        _view.hervat(System.getTimer());
        return true;
    }
}
