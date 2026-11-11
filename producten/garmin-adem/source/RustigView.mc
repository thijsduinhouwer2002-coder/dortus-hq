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
        // Keuring bouw 7 punt 7 (batterij): tijdens vasthouden staat de zee stil en verandert alleen het cijfer,
        // dus dan eens per seconde tekenen in plaats van tien keer.
        if (i == 1 || i == 3) {
            var sec = sessie.overS(sessie.klok(System.getTimer()));
            if (sec == _getekendSec) {
                return;
            }
            _getekendSec = sec;
        } else {
            _getekendSec = -1;
        }
        if (plaatjeMs < 0) {
            _golf += 0.15;
        }
        WatchUi.requestUpdate();
    }

    private var _getekendSec as Number = -1;

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
        EbbZee.ademZee(dc, d, sessie.water(nu), _golf);
        var font = EbbTeken.grootFont(dc, d);
        var getal = sessie.overS(nu).toString();
        var gb = dc.getTextWidthInPixels(getal, font);
        var cy = (d * 0.39).toNumber();
        // Keuring bouw 3 punt 6 (scène 7): het cijfer zelf in het midden, "s" los erachter.
        var cx = w / 2;
        // Kop minstens 12 px (454) of 6 px (260) boven de bovenkant van de cijfers.
        var leeg = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
        var topC = cy - dc.getFontHeight(font) / 2 + (leeg > 0 ? leeg : 0);
        var gat = (d * 0.026).toNumber();
        gat = gat < 6 ? 6 : gat;
        var yKop = topC - gat - dc.getFontHeight(EbbTeken.fS()) / 2;
        var yKop0 = (d * 0.18).toNumber();
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (yKop < yKop0 ? (yKop < d * 0.12 ? (d * 0.12).toNumber() : yKop) : yKop0), EbbTeken.fS(), WOORDEN[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, cy, font, getal, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        var onder = cy - dc.getFontHeight(font) / 2 + (dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font)) / 2 + Graphics.getFontAscent(font);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx + gb / 2 + 4, onder - Graphics.getFontAscent(EbbTeken.fS()), EbbTeken.fS(), "s", Graphics.TEXT_JUSTIFY_LEFT);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var label = naam.equals("4-7-8") ? "Calm 4-7-8" : naam;
        dc.drawText(w / 2, (d * 0.84).toNumber(), EbbTeken.fS(), label, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function pauzeer() as Void {
        sessie.pauzeer(System.getTimer());
        opname.pauzeer();
    }

    // Save uit het pauzemenu: opslaan, trouw tellen, dan het eindscherm 6d (blad v7, "counts as a session").
    function opslaanEnTonen() as Void {
        opname.opslaan();
        var ms = sessie.klok(System.getTimer()) - sessie.startMs;
        var meetelt = EbbTrouw.telt(0, ms);
        var tellers = meetelt ? EbbTrouw.naSessie(EbbView.vandaag()) : EbbTrouw.stand(EbbView.vandaag());
        var nieuw = meetelt ? EbbTrouw.nieuweDieren(tellers) : [] as Array<Number>;
        System.println("TROUW telt " + meetelt + " nieuwe dieren " + nieuw);
        var c = sessie.cyclus();
        var ev = new CalmEindeView(ms, c > 0 ? ms / c : 0, nieuw, tellers[1]);
        // Codelezing hoofdchat 11 nov: komt het 24e dier door Calm, dan ook hier het feestscherm (één keer).
        ev.feest = EbbTrouw.feestNu(meetelt, tellers);
        WatchUi.switchToView(ev, new CalmEindeDelegate(), WatchUi.SLIDE_UP);
    }

    function weggooien() as Void {
        opname.weggooien();
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

    // Keuring bouw 6 punt 4: ook Calm pauzeert in het pauzemenu in Ebb-stijl (Pauze.mc), niet in het systeemmenu.
    function onBack() as Boolean {
        _view.pauzeer();
        var s = (_view.sessie.klok(System.getTimer()) - _view.sessie.startMs) / 1000;
        s = s < 0 ? 0 : s;
        var pv = new PauzeView("calm · " + (s / 60) + ":" + (s % 60).format("%02d"), EbbTrouw.zwemmer());
        WatchUi.pushView(pv, new PauzeDelegate(pv, _view.method(:hervat), _view.method(:opslaanEnTonen), _view.method(:weggooien)), WatchUi.SLIDE_UP);
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

// Blad v7 scherm 6d (Calm-eindscherm): "calm done", minuten en ademhalingen, je dier in de zee (een nieuw dier groot
// met "new friend"), "counts as a session", zeven stippen voor de reeks met label. Terug of select: naar het startscherm.
class CalmEindeView extends WatchUi.View {
    var ms as Number;
    var ademhalingen as Number;
    var nieuw as Array<Number>;
    var reeks as Number;
    var telt as Boolean = true;
    var feest as Boolean = false;

    function onHide() as Void {
        EbbSeaComplete.los();
    }

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
        if (feest) {
            EbbSeaComplete.teken(dc, d, reeks);
            return;
        }
        // Mila blad v13: zelfde indeling als het eindscherm van Rounds (kop 38, regel 67, kamlijn 94, dier in het vak
        // 98 tot 144 onder de kamlijn, in 1/260 D).
        var yKop = EbbTeken.px(d, EbbEindScherm.KOP);
        var yRegel1 = EbbTeken.px(d, EbbEindScherm.TIJD);
        var kam = EbbEindScherm.kamlijn(d, yRegel1 + dc.getFontHeight(EbbTeken.fX()) / 2);
        EbbZee.zeeBanden(dc, d, [EbbEindScherm.zeeTopBij(d, kam), 0.60, 0.88] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, yKop, EbbTeken.fS(), "calm done", midden);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        // Keuring bouw 3 punt 11: onder 1 minuut seconden ("45 s"), niet "1 min"; punt 6: deze regel kleiner.
        dc.drawText(w / 2, yRegel1, EbbTeken.fX(), EbbStart.duurTekst(ms) + " · " + ademhalingen + (ademhalingen == 1 ? " breath" : " breaths"), midden);
        var bandTop = EbbEindScherm.vakTop(d, kam);
        var bandOnder = EbbTeken.px(d, EbbEindScherm.VAK_ONDER);
        var bandBreed = EbbTeken.px(d, EbbEindScherm.VAK_BREED);
        var naamY = EbbEindScherm.NAAM / 260.0;
        // Besluit 11 nov 04:30 (besluit 3): Calm telt pas vanaf 1 minuut.
        var regel = telt ? "counts as a session" : "from 1 min it counts";
        var kleur = Graphics.COLOR_WHITE;
        if (nieuw.size() > 0) {
            EbbDierMaat.inBand(dc, nieuw[0], w / 2, bandTop, bandOnder, bandBreed, d, EbbDierPlaatje.GEVONDEN);
            regel = "new friend: " + EbbDierData.NAMEN[nieuw[0]];
            kleur = EbbTeken.LICHT;
        } else {
            var dier = EbbTrouw.zwemmer();
            if (dier >= 0) {
                EbbDierMaat.inBand(dc, dier, w / 2, bandTop, bandOnder, bandBreed, d, EbbDierPlaatje.GEVONDEN);
            }
        }
        EbbTeken.tekstInRonde(dc, d, naamY, regel, kleur);
        EbbTeken.weekStippen(dc, d, reeks, ((EbbBouw.DEMO || EbbBouw.PLAATJE) ? 2 : EbbTrouw.dezeWeek(EbbView.vandaag())), EbbTrouw.weekdoel(), EbbTeken.px(d, EbbEindScherm.STIP));
    }
}

class CalmEindeDelegate extends WatchUi.BehaviorDelegate {
    function initialize() {
        BehaviorDelegate.initialize();
    }

    function naarMenu() as Boolean {
        EbbNaarMenu.ga(WatchUi.SLIDE_RIGHT);
        return true;
    }

    function onBack() as Boolean {
        return naarMenu();
    }

    function onSelect() as Boolean {
        return naarMenu();
    }
}
