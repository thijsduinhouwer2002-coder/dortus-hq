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
            opname.metRondes = false;
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
        // Keuring bouw 1 punt 5 (blad v6 scherm 5): zwart, fasewoord bovenaan, groot cijfer met "s", de zee onderaan
        // die zacht mee ademt (hoogste golf 0,60 D), het cijfer staat altijd boven de hoogste golfstand; geen teal vlak.
        EbbTeken.ademZee(dc, d, sessie.water(nu), _golf);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.18).toNumber(), Graphics.FONT_SMALL, WOORDEN[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        var font = EbbTeken.grootFont(dc, d);
        var getal = sessie.overS(nu).toString();
        var gb = dc.getTextWidthInPixels(getal, font);
        var sb = dc.getTextWidthInPixels("s", Graphics.FONT_SMALL);
        var cy = (d * 0.39).toNumber();
        var cx = w / 2 - sb / 2 - 2;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, cy, font, getal, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        var onder = cy - dc.getFontHeight(font) / 2 + (dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font)) / 2 + Graphics.getFontAscent(font);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx + gb / 2 + 4, onder - Graphics.getFontAscent(Graphics.FONT_SMALL), Graphics.FONT_SMALL, "s", Graphics.TEXT_JUSTIFY_LEFT);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var label = naam.equals("4-7-8") ? "Calm 4-7-8" : naam;
        dc.drawText(w / 2, (d * 0.84).toNumber(), Graphics.FONT_SMALL, label, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
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
            // Ook rustig ademen telt voor trouw; daarna het eindscherm 6d (blad v7, "counts as a session").
            var s = _view.sessie;
            var ms = s.klok(System.getTimer()) - s.startMs;
            var meetelt = EbbTrouw.telt(0, ms);
            var tellers = meetelt ? EbbTrouw.naSessie(EbbView.vandaag()) : EbbTrouw.stand(EbbView.vandaag());
            var nieuw = meetelt ? EbbTrouw.nieuweDieren(tellers) : [] as Array<Number>;
            System.println("TROUW telt " + meetelt + " nieuwe dieren " + nieuw);
            var c = s.cyclus();
            var ev = new CalmEindeView(ms, c > 0 ? ms / c : 0, nieuw, tellers[1]);
            WatchUi.switchToView(ev, new CalmEindeDelegate(), WatchUi.SLIDE_UP);
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

// Blad v7 scherm 6d (Calm-eindscherm): "calm done", minuten en ademhalingen, je dier in de zee (een nieuw dier groot
// met "new friend"), "counts as a session", zeven stippen voor de reeks met label. Terug of select: naar het startscherm.
class CalmEindeView extends WatchUi.View {
    var ms as Number;
    var ademhalingen as Number;
    var nieuw as Array<Number>;
    var reeks as Number;
    var telt as Boolean = true;

    function initialize(ms as Number, ademhalingen as Number, nieuw as Array<Number>, reeks as Number) {
        View.initialize();
        telt = EbbTrouw.telt(0, ms);
        self.ms = ms;
        self.ademhalingen = ademhalingen;
        self.nieuw = nieuw;
        self.reeks = reeks;
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        EbbTeken.golf(dc, d, 0.326, d * 0.010, EbbTeken.ZEE_KLEUR[1], 0.4, true);
        EbbTeken.golf(dc, d, 0.60, d * 0.006, EbbTeken.ZEE_KLEUR[2], 1.7, false);
        EbbTeken.golf(dc, d, 0.88, d * 0.006, EbbTeken.ZEE_KLEUR[3], 2.9, false);
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.17).toNumber(), Graphics.FONT_SMALL, "calm done", midden);
        var minuten = (ms + 30000) / 60000;
        minuten = minuten < 1 ? 1 : minuten;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.25).toNumber(), Graphics.FONT_SMALL, minuten + " min · " + ademhalingen + (ademhalingen == 1 ? " breath" : " breaths"), midden);
        var cy = (d * 0.465).toNumber();
        // Besluit 11 nov 04:30 (besluit 3): Calm telt pas vanaf 1 minuut.
        var regel = telt ? "counts as a session" : "from 1 min it counts";
        var kleur = Graphics.COLOR_WHITE;
        if (nieuw.size() > 0) {
            EbbDierData.teken(dc, nieuw[0], w / 2, cy, (d * 0.15).toNumber(), -1);
            regel = "new friend: " + EbbDierData.NAMEN[nieuw[0]];
            kleur = EbbTeken.LICHT;
        } else {
            var dier = EbbTrouw.zwemmer();
            if (dier >= 0) {
                EbbDierData.teken(dc, dier, w / 2, cy, (d * 0.105).toNumber(), -1);
            }
        }
        tekst(dc, d, 0.645, regel, kleur);
        var label = EbbTeken.weekStippen(dc, d, reeks, ((EbbBouw.DEMO || EbbBouw.PLAATJE) ? 2 : EbbTrouw.dezeWeek(EbbView.vandaag())), EbbTrouw.weekdoel());
        tekst(dc, d, 0.795, label, EbbTeken.LICHTCYAAN);
    }

    function tekst(dc as Graphics.Dc, d as Number, y as Float, t as String, kleur as Number) as Void {
        var dy = y - 0.5;
        var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.86;
        var f = (dc.getTextWidthInPixels(t, Graphics.FONT_SMALL) <= koorde) ? Graphics.FONT_SMALL : Graphics.FONT_XTINY;
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, t, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}

class CalmEindeDelegate extends WatchUi.BehaviorDelegate {
    function initialize() {
        BehaviorDelegate.initialize();
    }

    function naarMenu() as Boolean {
        var mv = new EbbMenuView();
        WatchUi.switchToView(mv, new EbbMenuDelegate(mv), WatchUi.SLIDE_RIGHT);
        return true;
    }

    function onBack() as Boolean {
        return naarMenu();
    }

    function onSelect() as Boolean {
        return naarMenu();
    }
}
