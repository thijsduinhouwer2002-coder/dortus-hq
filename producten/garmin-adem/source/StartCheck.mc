import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Blad v5 (S2): bij elke Rounds-start eerst "Seated or lying?" met START. Terug gaat naar het menu.
class StartCheckView extends WatchUi.View {
    // Blad v7 punt 8: bij de eerste Rounds eerst één uitlegscherm "how it works" (blad 0), daarna de startcheck (blad 1).
    var blad as Number = 1;
    // Besluit hoofdchat 11 nov 04:30 (besluit 4): ook Calm krijgt de check, want ook daar houd je 7 s in. Zonder uitleg.
    var calm as Boolean = false;
    // Keuring bouw 3 punt 3: ook My pattern loopt via deze check; dan een ander patroon en een andere naam.
    var rustPatroon as Array<Number>? = null;
    var rustNaam as String = EbbStart.CALM_NAAM;

    function zetCalm() as Void {
        calm = true;
        blad = 1;
        rustPatroon = Ebb.calm();
        rustNaam = EbbStart.CALM_NAAM;
    }

    function zetEigen() as Void {
        calm = true;
        blad = 1;
        rustPatroon = EbbInstellingen.eigenPatroon();
        rustNaam = "My pattern";
    }

    // Keuring bouw 3 punt 3: bij Calm de naam als kop ("Calm 4-7-8"), niet het aantal rondes.
    function kop() as String {
        if (!calm) {
            return EbbStart.startKop();
        }
        return rustNaam.equals(EbbStart.CALM_NAAM) ? "Calm " + EbbStart.CALM_NAAM : rustNaam + " " + EbbStart.eigenTekst();
    }

    function initialize() {
        View.initialize();
        var g = Application.Storage.getValue(EbbStart.UITLEG);
        blad = ((g instanceof Boolean) && (g as Boolean)) ? 1 : 0;
    }

    function onShow() as Void {
        System.println(blad == 0 ? "STARTCHECK uitleg" : "STARTCHECK");
    }

    function verder() as Void {
        Application.Storage.setValue(EbbStart.UITLEG, true);
        blad = 1;
        System.println("STARTCHECK");
        WatchUi.requestUpdate();
    }

    // Blad v7 scherm 1c: "how it works", in gewone woorden, met de juiste knop per horloge.
    function tekenUitleg(dc as Graphics.Dc, d as Number) as Void {
        EbbZee.strook(dc, d);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.20).toNumber(), EbbTeken.fS(), "how it works", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        var f = EbbTeken.fX();
        var lh = dc.getFontHeight(f);
        var regels = [EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " deep breaths,", "then hold only", "while it feels easy.",
            WatchUi.loadResource(Rez.Strings.UitlegStart) as String, "BACK stops."] as Array<String>;
        var y = (d * 0.46).toNumber() - (regels.size() * lh) / 2;
        for (var i = 0; i < regels.size(); i += 1) {
            dc.setColor(i < 3 ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, y + i * lh, f, regels[i], Graphics.TEXT_JUSTIFY_CENTER);
        }
        EbbTeken.pil(dc, d, 0.77, 0.30, 0.10, "OK", f);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        if (blad == 0) {
            tekenUitleg(dc, (w < h) ? w : h);
            return;
        }
        // Blad v6 scherm 1b: kop met rondes en ademhalingen, groot "Seated / or lying?", knop Start als pil, zee onderaan.
        var d = (w < h) ? w : h;
        // Daan B5: zee iets lager (0,83 D), zodat de pil Start ruim boven de golf blijft.
        EbbZee.zeeBanden(dc, d, [0.83, 0.90] as Array<Float>, [1, 2] as Array<Number>, 0.010, 0.0);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.235).toNumber(), EbbTeken.fX(), kop(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        // Blad v7 punt 7: "Sit or lie down" in plaats van "Seated or lying?".
        dc.drawText(w / 2, (d * 0.385).toNumber(), EbbTeken.fM(), "Sit or", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.drawText(w / 2, (d * 0.49).toNumber(), EbbTeken.fM(), "lie down", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbTeken.pil(dc, d, 0.655, 0.40, 0.13, "Start", EbbTeken.fS());
    }
}

class StartCheckDelegate extends WatchUi.BehaviorDelegate {
    private var _view as StartCheckView;

    function initialize(view as StartCheckView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onSelect() as Boolean {
        if (_view.blad == 0) {
            _view.verder();
            return true;
        }
        System.println("STARTCHECK start");
        if (_view.calm) {
            var rv = new RustigView(_view.rustPatroon as Array<Number>, _view.rustNaam);
            (Application.getApp() as EbbApp).zetRustig(rv);
            WatchUi.switchToView(rv, new RustigDelegate(rv), WatchUi.SLIDE_LEFT);
            return true;
        }
        var view = new EbbView();
        (Application.getApp() as EbbApp).zetView(view);
        WatchUi.switchToView(view, new EbbDelegate(view), WatchUi.SLIDE_LEFT);
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
    }
}
