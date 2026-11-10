import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Ebb (Gijs, 10 nov 2026): eerste bouwstap. Rondes met water dat stijgt en zakt, inhouden met groot getal.
// Uiterlijk is voorlopig; Mila maakt de stijl (ontwerp/garmin/tij-stijl.md).
class EbbApp extends Application.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    // Stopt de app zonder opslaan (bijvoorbeeld afgesloten van buitenaf), dan wordt de opname weggegooid:
    // alleen "Save" in het pauzemenu of het einde van de sessie bewaart een activiteit.
    function onStop(state as Dictionary?) as Void {
        if (_view != null && (_view as EbbView).opname.loopt()) {
            (_view as EbbView).weggooien();
        }
        if (_rustig != null && (_rustig as RustigView).opname.loopt()) {
            (_rustig as RustigView).opname.weggooien();
        }
    }

    private var _rustig as RustigView or Null = null;

    function zetRustig(view as RustigView) as Void {
        _rustig = view;
    }

    private var _view as EbbView or Null = null;

    function zetView(view as EbbView) as Void {
        _view = view;
    }

    function getInitialView() as [WatchUi.Views] or [WatchUi.Views, WatchUi.InputDelegates] {
        var view = new EbbView();
        _view = view;
        if (EbbBouw.DEMO) {
            // Testbouw eis 10: 2 ademhalingen van 250 ms, 2 rondes, herstel 500 ms.
            view.sessie = new Ebb.Rondes(2, 250, 2, 500, System.getTimer());
            // Eis 10, tweede helft: bij elke tweede start van de testbouw wordt een opname weggegooid;
            // de workflow kijkt dat die start geen FIT-bestand geeft. (Weggooien en opslaan in één start
            // liet in de simulator de weggegooide lap in het volgende bestand achter.)
            var keer = Application.Storage.getValue("demokeer");
            var k = (keer instanceof Number) ? keer as Number : 0;
            Application.Storage.setValue("demokeer", k + 1);
            if (k % 2 == 1) {
                view.opnemen = false;
                var weg = new EbbOpname();
                weg.start();
                // Proef 10 nov 07:05: zonder setData, om te zien of de lek de lap zelf is of de veldwaarde.
                weg.weggooien();
                System.println("OPNAME proef weggegooid");
            }
        }
        if (!EbbBouw.DEMO) {
            EbbTrillen.aan = EbbInstellingen.trillen();
            if (EbbVeilig.moetTonen()) {
                return [new VeiligView(), new VeiligDelegate()];
            }
            return [EbbStart.menu(), new StartDelegate()];
        }
        return [view, new EbbDelegate(view)];
    }
}

// Eis 2: veiligheidsscherm bij de eerste start; na bevestigen nooit meer (tenzij "opnieuw tonen").
class VeiligView extends WatchUi.View {
    function initialize() {
        View.initialize();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var regels = ["Sit or lie down.", "Never in or near water,", "never while driving.", "Dizzy? Stop."];
        var f = Graphics.FONT_XTINY;
        var lh = dc.getFontHeight(f);
        var y = h / 2 - (regels.size() * lh) / 2 - lh / 2;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < regels.size(); i += 1) {
            dc.drawText(w / 2, y + i * lh, f, regels[i], Graphics.TEXT_JUSTIFY_CENTER);
        }
        dc.setColor(0x00AAFF, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, y + regels.size() * lh + lh / 2, f, "Press start: OK", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

class VeiligDelegate extends WatchUi.BehaviorDelegate {
    function initialize() {
        BehaviorDelegate.initialize();
    }

    function onSelect() as Boolean {
        EbbVeilig.bevestig();
        WatchUi.switchToView(EbbStart.menu(), new StartDelegate(), WatchUi.SLIDE_LEFT);
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
    }
}

class EbbView extends WatchUi.View {
    var sessie as Ebb.Rondes;
    private var _timer as Timer.Timer = new Timer.Timer();

    function initialize() {
        View.initialize();
        sessie = EbbInstellingen.rondes(System.getTimer());
    }

    var opname as EbbOpname = new EbbOpname();
    var koraal as Boolean = false;
    var opnemen as Boolean = true;
    // Scherm 5: na de sessie wisselen tussen duikprofiel (vandaag) en getijdenlijn (8 weken) met de knoppen.
    var getij as Boolean = false;
    private var _klaarSinds as Number = -1;
    private var _startTijd as Number = System.getTimer();
    private var _gestart as Boolean = false;
    private var _lapsGesloten as Number = 0;

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            sessie.segmentStart = System.getTimer();
            if (opnemen) {
                opname.start();
            }
        }
        _timer.start(method(:tik), 100, true);
    }

    // Stop het inhouden op tijdstip nu (uit de knophandler of de testbouw) en zet de tijd op de lap.
    function stopInhouden(nu as Number) as Boolean {
        var tijd = sessie.stopInhouden(nu);
        if (tijd < 0) {
            return false;
        }
        opname.inhouden((tijd + 500) / 1000);
        for (var i = 0; i <= EbbProfiel.gehaald(tijd); i += 1) {
            EbbProfiel.eersteKeer(i);
        }
        return true;
    }

    // Dagnummer van de lokale datum (dagen sinds 1970).
    static function vandaag() as Number {
        return (Time.today().value() + System.getClockTime().timeZoneOffset) / 86400;
    }

    // Opslaan: activiteit bewaren en de inhoudtijden in de 56 dagen zetten.
    function opslaan() as Boolean {
        var ok = opname.opslaan();
        System.println("OPNAME opgeslagen " + ok + " laps " + (opname.laps + 1) + " beste " + opname.besteS);
        var opslag = new EbbOpslag();
        var dag = vandaag();
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            opslag.voegToe(dag, (sessie.inhoudtijden[i] + 500) / 1000);
        }
        opslag.bewaar();
        var record = EbbProfiel.record();
        koraal = EbbProfiel.nieuwRecord(sessie.inhoudtijden, record * 1000 + 999);
        if (koraal) {
            EbbProfiel.bewaarRecord(sessie.inhoudtijden[EbbProfiel.diepste(sessie.inhoudtijden)] / 1000);
        }
        return ok;
    }

    // Pauze zet de klok en de opname stil; doorgaan gaat verder waar je was.
    function pauzeer(nu as Number) as Void {
        sessie.pauzeer(nu);
        opname.pauzeer();
    }

    function hervat(nu as Number) as Void {
        sessie.hervat(nu);
        opname.hervat();
        _vorigIn = sessie.isIn(nu);
    }

    function weggooien() as Void {
        opname.weggooien();
        System.println("OPNAME weggegooid");
    }

    function onHide() as Void {
        _timer.stop();
    }

    private var _vorigeFase as Number = -1;
    private var _vorigIn as Boolean = false;

    function tik() as Void {
        var nu = System.getTimer();
        if (sessie.gepauzeerd()) {
            return;
        }
        if (EbbBouw.DEMO && sessie.fase == Ebb.FASE_INHOUDEN) {
            var doel = EbbBouw.INHOUD_MS[sessie.ronde % EbbBouw.INHOUD_MS.size()];
            if (sessie.verstreken(nu) >= doel) {
                stopInhouden(sessie.segmentStart + doel);
            }
        }
        sessie.bijwerken(nu);
        // Elke afgeronde ronde die niet de laatste is sluit een lap (onUpdate kan de ronde al verder gezet hebben).
        while (_lapsGesloten < sessie.ronde && _lapsGesloten < sessie.rondes - 1) {
            opname.rondeKlaar();
            _lapsGesloten += 1;
        }
        if (sessie.fase == Ebb.FASE_KLAAR && opname.loopt()) {
            opslaan();
        }
        if (sessie.fase == Ebb.FASE_KLAAR && _klaarSinds < 0) {
            _klaarSinds = nu;
        }
        // Testbouw: 15 s na het duikprofiel vanzelf naar de getijdenlijn, voor de schermafbeelding d.
        if (EbbBouw.DEMO && _klaarSinds >= 0 && !getij && nu - _klaarSinds >= 15000) {
            getij = true;
            System.println("GETIJ getoond, klaar na " + (_klaarSinds - _startTijd) + " ms");
        }
        trilBijWissel(nu);
        WatchUi.requestUpdate();
    }

    // Trilt één keer bij elke wissel van fase of van in naar uit (eis 6).
    function trilBijWissel(nu as Number) as Void {
        var fase = sessie.fase as Number;
        var isIn = (fase == Ebb.FASE_ADEMEN) && sessie.isIn(nu);
        if (fase != _vorigeFase) {
            if (fase == Ebb.FASE_ADEMEN) {
                EbbTrillen.tril(_vorigeFase == Ebb.FASE_HERSTEL ? EbbTrillen.M_LOS : EbbTrillen.M_IN);
            } else if (fase == Ebb.FASE_INHOUDEN) {
                EbbTrillen.tril(EbbTrillen.M_INHOUDEN);
            } else if (fase == Ebb.FASE_HERSTEL) {
                EbbTrillen.tril(EbbTrillen.M_HERSTEL);
            } else if (fase == Ebb.FASE_KLAAR) {
                EbbTrillen.tril(EbbTrillen.M_KLAAR);
            }
        } else if (fase == Ebb.FASE_ADEMEN && isIn != _vorigIn) {
            EbbTrillen.tril(isIn ? EbbTrillen.M_IN : EbbTrillen.M_UIT);
        }
        _vorigeFase = fase;
        _vorigIn = isIn;
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var nu = System.getTimer();
        sessie.bijwerken(nu);
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();

        var fase = sessie.fase;
        var d = (w < h) ? w : h;
        var golfFase = (nu % 3142) / 500.0;   // golf schuift ±2 rad per seconde
        var t = sessie.verstreken(nu);
        var woord = "";
        var groot = "";
        var klein = "";
        var yGroot = 0.38;
        var yKlein = 0.73;
        var font = EbbTeken.grootFont(dc, d);
        var donker = false;
        if (fase == Ebb.FASE_ADEMEN) {
            // 1. Ademen: peil volgt de adem, onderin 20% bij uit, 80% bij in.
            var peilA = 0.2 + 0.6 * sessie.water(nu);
            EbbTeken.water(dc, d, peilA, EbbTeken.DIEPTE[0], golfFase);
            donker = peilA > EbbTeken.PEIL_DONKER;
            woord = sessie.isIn(nu) ? "in" : "out";
            groot = sessie.ademhaling(nu).toString();
            klein = "of " + sessie.ademhalingen + " · round " + (sessie.ronde + 1);
        } else if (fase == Ebb.FASE_INHOUDEN) {
            // 2. Duiken: bijna alles water, per 15 s een tint dieper, belletjes stijgen, dier in koraal.
            var tint = t / 15000;
            EbbTeken.water(dc, d, 0.93, EbbTeken.DIEPTE[tint > 3 ? 3 : tint], golfFase);
            var stijg = (t % 8000) / 8000.0;
            EbbTeken.bellen(dc, d, [
                [0.30, 0.70 - 0.30 * stijg, 0.018], [0.33, 0.85 - 0.30 * stijg, 0.012],
                [0.70, 0.55 - 0.30 * stijg, 0.015], [0.68, 0.45 - 0.25 * stijg, 0.009]] as Array<Array<Float> >);
            var soort = EbbProfiel.dier(t);
            if (soort >= 0) {
                var p = (t - EbbProfiel.DREMPELS[soort]).toFloat() / EbbProfiel.IN_BEELD_MS;
                EbbTeken.dier(dc, d, soort, ((1.1 - 1.2 * p) * d).toNumber(), (0.66 * d).toNumber());
            }
            var s = t / 1000;
            groot = (s / 60).toString() + ":" + (s % 60).format("%02d");
            klein = s + " m";
            yGroot = 0.30;
            yKlein = 0.62;
        } else if (fase == Ebb.FASE_HERSTEL) {
            // 3. Boven: water schiet in 0,5 s van 93% naar 80%, plons van vijf belletjes.
            var peil = (t < 500) ? 0.93 - 0.13 * t / 500.0 : 0.80;
            EbbTeken.water(dc, d, peil.toFloat(), EbbTeken.DIEPTE[0], golfFase);
            donker = peil > EbbTeken.PEIL_DONKER;
            EbbTeken.bellen(dc, d, [[0.22, 0.20, 0.022], [0.30, 0.12, 0.014], [0.50, 0.08, 0.018],
                [0.70, 0.13, 0.012], [0.78, 0.22, 0.020]] as Array<Array<Float> >);
            groot = ((sessie.herstelMs - t) / 1000 + 1).toString();
            klein = "hold · recover";
            yGroot = 0.30;
            yKlein = 0.66;
        } else {
            // 4. Duikprofiel, of 5. getijdenlijn.
            if (getij) {
                tekenGetij(dc, d);
            } else {
                tekenProfiel(dc, d);
            }
        }
        if (woord.length() > 0) {
            // Staat het lichte water tot boven, dan leest het zachte woord niet meer: dan donkerblauw.
            dc.setColor(donker ? EbbTeken.DIEPTE[3] : EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * 0.13).toNumber(), Graphics.FONT_SMALL, woord, Graphics.TEXT_JUSTIFY_CENTER);
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (groot.length() > 0) {
            dc.drawText(w / 2, (d * yGroot).toNumber() + dc.getFontHeight(font) / 2, font, groot, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        if (klein.length() > 0) {
            dc.setColor(fase == Ebb.FASE_INHOUDEN ? EbbTeken.ZACHT : Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * yKlein).toNumber(), Graphics.FONT_XTINY, klein, Graphics.TEXT_JUSTIFY_CENTER);
        }
        if (EbbBouw.DEMO) {
            meet(dc, w, fase as Number, groot, font);
        }
    }

    // Eis 11 en 12, alleen in de testbouw: breedte van het grote getal per fase (eerste keer)
    // en het hoogste geheugengebruik, gemeld zodra het duikprofiel getekend is.
    private var _grootGemeld as Array<Boolean> = [false, false, false, false, false] as Array<Boolean>;
    private var _maxGeheugen as Number = 0;
    private var _geheugenGemeld as Boolean = false;

    // Eis 11 meet de hoogte van de cijfers (ascent; een "1" is nooit 30% breed), breedte staat er ter info bij.
    function meet(dc as Graphics.Dc, w as Number, fase as Number, groot as String, font as Graphics.FontType) as Void {
        if (groot.length() > 0 && !_grootGemeld[fase]) {
            _grootGemeld[fase] = true;
            if (fase == 0) {
                for (var i = 0; i < EbbTeken.GROOT_LIJST.size(); i += 1) {
                    var f = EbbTeken.GROOT_LIJST[i];
                    System.println("LETTER " + i + " ascent " + Graphics.getFontAscent(f) + " hoogte " + dc.getFontHeight(f) + " breedte0:00 " + dc.getTextWidthInPixels("0:00", f) + " van " + w);
                }
            }
            var b = dc.getTextWidthInPixels(groot, font);
            var hoog = Graphics.getFontAscent(font);
            System.println("GROOT fase " + fase + " tekst " + groot + " breedte " + b + " hoogte " + hoog + " van " + w + " = " + (hoog * 100 / w) + "%");
        }
        var st = System.getSystemStats();
        if (st.usedMemory > _maxGeheugen) {
            _maxGeheugen = st.usedMemory;
        }
        if (fase == Ebb.FASE_KLAAR && !_geheugenGemeld) {
            _geheugenGemeld = true;
            System.println("GEHEUGEN hoogste " + _maxGeheugen + " van " + st.totalMemory + " = " + (_maxGeheugen.toLong() * 100 / st.totalMemory) + "%");
        }
    }

    // Eis 7: duikprofiel na de sessie (schets Mila scherm 4): oppervlakte op 32%, per ronde een V tot evenredige
    // diepte (diepste tot 70%), vlakken in oplopende tint, schuimlijn erover; stip bij de diepste met de tijd links;
    // koraal en "new best" alleen bij een record, anders lichtgeel en het aantal rondes.
    function tekenProfiel(dc as Graphics.Dc, d as Number) as Void {
        var t = sessie.inhoudtijden;
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.12).toNumber(), Graphics.FONT_XTINY, "today", Graphics.TEXT_JUSTIFY_CENTER);
        if (t.size() == 0) {
            return;
        }
        var opp = (d * 0.32).toNumber();
        var x0 = (d * 0.16).toNumber();
        var p = EbbProfiel.vPunten(t, x0, opp, (d * 0.68).toNumber(), (d * 0.38).toNumber());
        dc.setPenWidth(d / 160 > 1 ? d / 160 : 1);
        dc.drawLine(x0 - d / 25, opp, x0 + (d * 0.68).toNumber() + d / 25, opp);
        for (var i = 0; i < t.size(); i += 1) {
            var a = p[2 * i];
            var tip = p[2 * i + 1];
            var b = p[2 * i + 2];
            var k = EbbTeken.DIEPTE[1 + (i < 2 ? i : 2)];
            dc.setColor(k, k);
            dc.fillPolygon([[a[0], a[1]], [tip[0], tip[1]], [b[0], b[1]]]);
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(d / 110 > 2 ? d / 110 : 2);
            dc.drawLine(a[0], a[1], tip[0], tip[1]);
            dc.drawLine(tip[0], tip[1], b[0], b[1]);
        }
        var j = EbbProfiel.diepste(t);
        var diep = p[2 * j + 1];
        var kleur = koraal ? EbbTeken.KORAAL : EbbTeken.LICHT;
        var r = (d * 0.022).toNumber();
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(diep[0], diep[1], r > 3 ? r : 3);
        var s = t[j] / 1000;
        dc.drawText(diep[0] - (r * 16) / 10, diep[1], Graphics.FONT_SMALL, (s / 60).toString() + ":" + (s % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_RIGHT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(koraal ? EbbTeken.KORAAL : EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.80).toNumber(), Graphics.FONT_XTINY, koraal ? "new best" : t.size() + " rounds", Graphics.TEXT_JUSTIFY_CENTER);
    }

    // Getijdenlijn van 8 weken (in de testbouw nagebootst, zodat de schermafbeelding iets laat zien).
    function getijLijn() as Array<Array<Number> or Null> {
        if (EbbBouw.DEMO) {
            var lijn = [] as Array<Array<Number> or Null>;
            for (var i = 0; i < EbbOpslag.DAGEN; i += 1) {
                // Iemand die één dag per week overslaat en langzaam beter wordt, met wat schommeling.
                if (i % 7 == 3) {
                    lijn.add(null);
                } else {
                    var beste = (62 + 1.1 * i + 7 * Math.sin(i / 2.5)).toNumber();
                    lijn.add([beste, beste - 14 - (i % 3) * 3] as Array<Number>);
                }
            }
            return lijn;
        }
        return EbbProfiel.getijden(new EbbOpslag(), vandaag());
    }

    // Scherm 5 (schets Mila, tij-stijl.md): golvende lijn door je beste tijd per dag, het gemiddelde als
    // lichte schaduw eronder, gaten waar je niet ademde, weekstreepjes op de bodem, koraal bij je hoogste dag.
    function tekenGetij(dc as Graphics.Dc, d as Number) as Void {
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.12).toNumber(), Graphics.FONT_XTINY, "8 weeks", Graphics.TEXT_JUSTIFY_CENTER);
        var lijn = getijLijn();
        var x0 = (d * 0.14).toNumber();
        var bodem = (d * 0.68).toNumber();
        var w = (d * 0.72).toNumber();
        var p = EbbProfiel.getijPunten(lijn, x0, bodem, w, (d * 0.36).toNumber());
        var stap = (p.size() > 1) ? w / (p.size() - 1) : w;
        var half = (stap / 2 > 1) ? stap / 2 : 1;
        // Schaduw: per reeks dagen achter elkaar één vlak van de bodem tot het gemiddelde (een eiland per reeks).
        dc.setColor(EbbTeken.DIEPTE[2], EbbTeken.DIEPTE[2]);
        var i0 = 0;
        while (i0 < p.size()) {
            if (p[i0] == null) {
                i0 += 1;
                continue;
            }
            var vlak = [] as Array<[Numeric, Numeric]>;
            var eerste = p[i0] as Array<Number>;
            vlak.add([eerste[0] - half, bodem]);
            vlak.add([eerste[0] - half, eerste[2]]);
            var laatste = eerste;
            while (i0 < p.size() && p[i0] != null) {
                laatste = p[i0] as Array<Number>;
                vlak.add([laatste[0], laatste[2]]);
                i0 += 1;
            }
            vlak.add([laatste[0] + half, laatste[2]]);
            vlak.add([laatste[0] + half, bodem]);
            dc.fillPolygon(vlak);
        }
        // Bodem met een streepje per week.
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(1);
        dc.drawLine(x0 - half, bodem, x0 + w + half, bodem);
        for (var k = 0; k <= 8; k += 1) {
            var x = x0 + (w * k * 7) / (EbbOpslag.DAGEN - 1 > 0 ? EbbOpslag.DAGEN - 1 : 1);
            if (x > x0 + w) { x = x0 + w; }
            dc.drawLine(x, bodem, x, bodem + d / 40);
        }
        // Lijn door de beste tijden, onderbroken bij een gat.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 80 > 2 ? d / 80 : 2);
        var dagen = 0;
        for (var i = 0; i < p.size(); i += 1) {
            if (p[i] != null) {
                var q = p[i] as Array<Number>;
                dagen += 1;
                if (i > 0 && p[i - 1] != null) {
                    var v = p[i - 1] as Array<Number>;
                    dc.drawLine(v[0], v[1], q[0], q[1]);
                } else if (i + 1 >= p.size() || p[i + 1] == null) {
                    dc.fillCircle(q[0], q[1], d / 110 > 2 ? d / 110 : 2);
                }
            }
        }
        var j = EbbProfiel.hoogsteDag(lijn);
        if (j < 0) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, (d * 0.44).toNumber(), Graphics.FONT_SMALL, "no dives yet", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            return;
        }
        var top = p[j] as Array<Number>;
        var r = (d * 0.022).toNumber();
        dc.setColor(EbbTeken.KORAAL, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(top[0], top[1], r > 3 ? r : 3);
        var s = (lijn[j] as Array<Number>)[0];
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.72).toNumber(), Graphics.FONT_SMALL, "best " + (s / 60).toString() + ":" + (s % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_CENTER);
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.86).toNumber(), Graphics.FONT_XTINY, dagen + " days", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

class EbbDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbView;

    function initialize(view as EbbView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    // Stoptijd wordt in de knophandler vastgelegd (eis 4): de klok wordt gelezen in de handler zelf.
    function stop() as Boolean {
        return stopOp(System.getTimer());
    }

    // Los van de klok, zodat de toets een nagebootste tijd kan geven.
    function stopOp(nu as Number) as Boolean {
        if (_view.stopInhouden(nu)) {
            WatchUi.requestUpdate();
            return true;
        }
        return false;
    }

    // Wat terug doet: tijdens inhouden stoppen, anders het pauzemenu (doorgaan, opslaan, weggooien).
    function terugActie() as Symbol {
        return (_view.sessie.fase == Ebb.FASE_INHOUDEN) ? :stop : :pauze;
    }

    function onBack() as Boolean {
        if (terugActie() == :stop) {
            return stop();
        }
        _view.pauzeer(System.getTimer());
        var menu = new WatchUi.Menu2({:title => "Paused"});
        menu.addItem(new WatchUi.MenuItem("Resume", null, :doorgaan, null));
        menu.addItem(new WatchUi.MenuItem("Save", null, :opslaan, null));
        menu.addItem(new WatchUi.MenuItem("Discard", null, :weggooien, null));
        WatchUi.pushView(menu, new PauzeDelegate(_view), WatchUi.SLIDE_UP);
        return true;
    }

    function onSelect() as Boolean {
        return stop();
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return stop();
    }

    // Na de sessie wisselen omhoog en omlaag tussen duikprofiel en getijdenlijn; anders stoppen ze het inhouden.
    function wissel() as Boolean {
        if (_view.sessie.fase == Ebb.FASE_KLAAR) {
            _view.getij = !_view.getij;
            WatchUi.requestUpdate();
            return true;
        }
        return stop();
    }

    function onNextPage() as Boolean {
        return wissel();
    }

    function onPreviousPage() as Boolean {
        return wissel();
    }
}

// Pauzemenu: doorgaan, opslaan (activiteit en 56 dagen) of weggooien (geen FIT-bestand).
class PauzeDelegate extends WatchUi.Menu2InputDelegate {
    private var _view as EbbView;

    function initialize(view as EbbView) {
        Menu2InputDelegate.initialize();
        _view = view;
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        if (id == :doorgaan) {
            _view.hervat(System.getTimer());
        } else if (id == :opslaan) {
            _view.opslaan();
            System.exit();
        } else if (id == :weggooien) {
            _view.weggooien();
            System.exit();
        }
    }

    // Terug in het pauzemenu is ook doorgaan.
    function onBack() as Void {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        _view.hervat(System.getTimer());
    }
}
