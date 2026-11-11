import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Eis 2 en blad v5 (S1): drie veiligheidsbladen bij de eerste start en elke 30 dagen. Tekst letterlijk gelijk aan
// het blad (`ontwerp/garmin/ebb-blad-v5.md`). Niet over te slaan: alleen START of een tik gaat naar het volgende blad;
// vegen en de bladertoetsen doen niets, terug gaat een blad terug (op het eerste blad: de app sluit, zonder bevestigen).
module EbbVeiligTekst {
    const BLADEN = [
        ["Sit or lie down.", "Never while standing,", "never in or near water,", "never while driving."],
        ["You can faint", "without warning.", "Never force a hold.", "Stop if dizzy."],
        ["Not if: pregnant,", "under 18, epilepsy,", "heart or blood", "pressure problems."]
    ] as Array<Array<String> >;
    const GEEL = "Not a medical device.";

    function knop(blad as Number) as String {
        return blad < BLADEN.size() - 1 ? "Next" : "OK";
    }
}

class VeiligView extends WatchUi.View {
    var blad as Number = 0;

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        System.println("VEILIG blad " + (blad + 1));
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        // Blad v6 scherm 10, 10b, 10c: rode driehoek, de regels wit (de laatste regel van blad 3 geel), knop als pil,
        // dunne zeestrook onderaan.
        var d = (w < h) ? w : h;
        EbbZee.strook(dc, d);
        var regels = EbbVeiligTekst.BLADEN[blad];
        var geel = (blad == EbbVeiligTekst.BLADEN.size() - 1);
        var f = EbbTeken.fLees();
        var lh = EbbTeken.leesRegel(dc, f);
        var n = regels.size() + (geel ? 1 : 0);
        // Keuring bouw 2 punt 10: driehoek 44 px op 454 (0,097 D).
        var s = (d * 0.097).toNumber();
        var yPil = 0.79;
        // Driehoek en regels samen rond 0,45 D (de breedste regels dicht bij het midden, binnen 80 procent van de cirkel).
        var blok = s + lh / 2 + n * lh;
        var top = (d * 0.45 - blok / 2).toNumber();
        var onder = top + blok + lh;
        if (onder > d * (yPil - 0.05)) {
            yPil = (onder + d * 0.05) / d.toFloat();
        }
        // Daan B5: de pil blijft minstens 0,02 D boven de hoogste golftop van de strook; zo nodig schuift het blok omhoog.
        var bh = (d * 0.10).toNumber();
        bh = bh < lh + 4 ? lh + 4 : bh;
        var pilMax = (EbbZee.STROOK_TOP - 0.02) * d - bh / 2.0;
        if (yPil * d > pilMax) {
            top -= (yPil * d - pilMax).toNumber();
            yPil = pilMax / d;
        }
        EbbTeken.driehoek(dc, d, top + s / 2, s);
        var y = top + s + lh / 2;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < regels.size(); i += 1) {
            dc.drawText(w / 2, y + i * lh, f, regels[i], Graphics.TEXT_JUSTIFY_CENTER);
        }
        if (geel) {
            dc.setColor(EbbTeken.GEEL, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, y + regels.size() * lh, f, EbbVeiligTekst.GEEL, Graphics.TEXT_JUSTIFY_CENTER);
        }
        EbbTeken.pil(dc, d, yPil, 0.30, 0.10, EbbVeiligTekst.knop(blad), f);
    }
}

class VeiligDelegate extends WatchUi.BehaviorDelegate {
    private var _view as VeiligView;

    function initialize(view as VeiligView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onSelect() as Boolean {
        if (_view.blad < EbbVeiligTekst.BLADEN.size() - 1) {
            _view.blad += 1;
            System.println("VEILIG blad " + (_view.blad + 1));
            WatchUi.requestUpdate();
            return true;
        }
        System.println("VEILIG bevestigd");
        EbbVeilig.bevestig();
        var mv = new EbbMenuView();
        WatchUi.switchToView(mv, new EbbMenuDelegate(mv), WatchUi.SLIDE_LEFT);
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
    }

    // Niet langs de bladen: vegen en bladeren doen niets.
    function onNextPage() as Boolean {
        return true;
    }

    function onPreviousPage() as Boolean {
        return true;
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        return true;
    }

    function onBack() as Boolean {
        if (_view.blad > 0) {
            _view.blad -= 1;
            System.println("VEILIG blad " + (_view.blad + 1));
            WatchUi.requestUpdate();
            return true;
        }
        return false;
    }
}
