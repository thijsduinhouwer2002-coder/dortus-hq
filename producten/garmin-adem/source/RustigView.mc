import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Timer;
import Toybox.WatchUi;

// Rustig ademen (ontwerp eis 5): het water stijgt bij in, blijft staan bij vast, zakt bij uit.
// Bovenaan het fasewoord, in het midden de seconden die nog over zijn in deze fase, onderin de naam van het patroon.
// Loopt door tot terug; dan het pauzemenu (doorgaan, opslaan als activiteit, weggooien).
class RustigView extends WatchUi.View {
    var sessie as Ebb.Rustig;
    var naam as String;
    var opname as EbbOpname = new EbbOpname();
    private var _timer as Timer.Timer = new Timer.Timer();
    private var _gestart as Boolean = false;
    private var _vorige as Number = -1;
    private var _golf as Float = 0.0;
    // Winkelplaatje (B3, Daan keuring 2): >= 0 zet de klok vast op zoveel ms na de start, zodat het grote getal boven de golf staat.
    var plaatjeMs as Number = -1;

    function initialize(patroon as Array<Number>, naam as String) {
        View.initialize();
        sessie = new Ebb.Rustig(patroon, System.getTimer());
        self.naam = naam;
    }

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            if (plaatjeMs >= 0) {
                _golf = Math.PI.toFloat();
            }
            sessie.startMs = System.getTimer();
            opname.start();
        }
        _timer.start(method(:tik), 100, true);
    }

    function onHide() as Void {
        _timer.stop();
    }

    function tik() as Void {
        if (sessie.pauzeSinds >= 0) {
            return;
        }
        var i = sessie.faseIndex(System.getTimer());
        if (i != _vorige) {
            // Een vast-fase van 0 s wordt overgeslagen, dus alleen trillen bij een fase die er echt is.
            EbbTrillen.tril(i == 0 ? EbbTrillen.M_IN : (i == 2 ? EbbTrillen.M_UIT : EbbTrillen.M_VAST));
            _vorige = i;
        }
        if (plaatjeMs < 0) {
            _golf += 0.15;
        }
        WatchUi.requestUpdate();
    }

    static const WOORDEN = ["in", "hold", "out", "hold"] as Array<String>;

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var nu = plaatjeMs >= 0 ? sessie.startMs + plaatjeMs : sessie.klok(System.getTimer());
        var i = sessie.faseIndex(nu);
        var peil = 0.2 + 0.52 * sessie.water(nu);
        EbbTeken.water(dc, d, peil, EbbTeken.DIEPTE[i == 3 ? 1 : 0], _golf);
        dc.setColor(peil > EbbTeken.PEIL_DONKER ? EbbTeken.DIEPTE[3] : EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.13).toNumber(), Graphics.FONT_SMALL, WOORDEN[i], Graphics.TEXT_JUSTIFY_CENTER);
        var font = EbbTeken.grootFont(dc, d);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.38).toNumber() + dc.getFontHeight(font) / 2, font, sessie.overS(nu).toString(),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.drawText(w / 2, (d * 0.76).toNumber(), Graphics.FONT_XTINY, naam, Graphics.TEXT_JUSTIFY_CENTER);
    }

    function pauzeer() as Void {
        sessie.pauzeer(System.getTimer());
        opname.pauzeer();
    }

    function hervat() as Void {
        sessie.hervat(System.getTimer());
        opname.hervat();
    }
}

class RustigDelegate extends WatchUi.BehaviorDelegate {
    private var _view as RustigView;

    function initialize(view as RustigView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onBack() as Boolean {
        _view.pauzeer();
        var menu = new WatchUi.Menu2({:title => "Paused"});
        menu.addItem(new WatchUi.MenuItem("Resume", null, :doorgaan, null));
        menu.addItem(new WatchUi.MenuItem("Save", null, :opslaan, null));
        menu.addItem(new WatchUi.MenuItem("Discard", null, :weggooien, null));
        WatchUi.pushView(menu, new RustigPauzeDelegate(_view), WatchUi.SLIDE_UP);
        return true;
    }

    // Aanraakscherm uit tijdens rustig ademen: alleen de knoppen werken (productkeuring).
    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return true;
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        return true;
    }
}

class RustigPauzeDelegate extends WatchUi.Menu2InputDelegate {
    private var _view as RustigView;

    function initialize(view as RustigView) {
        Menu2InputDelegate.initialize();
        _view = view;
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (id == :doorgaan) {
            _view.hervat();
        } else if (id == :opslaan) {
            _view.opname.opslaan();
            // Ook rustig ademen telt voor trouw; het eindscherm met een nieuw dier komt met blad v4.1.
            System.println("TROUW nieuwe dieren " + EbbTrouw.nieuweDieren(EbbTrouw.naSessie(EbbView.vandaag())));
            System.exit();
        } else if (id == :weggooien) {
            _view.opname.weggooien();
            System.exit();
        }
    }

    function onBack() as Void {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        _view.hervat();
    }
}
