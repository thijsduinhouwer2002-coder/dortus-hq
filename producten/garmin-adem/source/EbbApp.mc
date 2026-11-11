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
        if (EbbBouw.PLAATJE) {
            // Testbeelden van elk scherm (nachtronde 11 nov 01:58, voor Daans keuring van de echte bouw), één scène per start:
            // 0 tot 3 inhouden 0:30, 1:45, 2:30, 3:04 (blad v6 3a, 3b, 3d, 3c), 4 sea log, 5 today, 6 8 weeks, 7 rustig 4-7-8,
            // 8 herstel, 9 ademen, 10 startscherm, 11 uitleg, 12 startcheck, 13 tot 15 veiligheid 1 tot 3,
            // 16 eindscherm 6c, 17 eindscherm 6b, 18 eindscherm 6c met 6 rondes, 19 en 20 settings 1 en 2, 21 Calm-eindscherm 6d.
            // Keuring v5 G1: het dier hangt niet van de inhoudtijd af (vis, schildpad, walvis, schildpad).
            var keer = Application.Storage.getValue("plaatjekeer");
            var k = ((keer instanceof Number) ? keer as Number : 0) % EbbBouw.SCENES;
            Application.Storage.setValue("plaatjekeer", k + 1);
            EbbTrillen.aan = false;
            System.println("PLAATJE scene " + k);
            // Keuring bouw 3 punt 4: de zwaarste schermen echt in de simulator (alleen deze scènes bewijzen geen watchdog).
            // 22 Calm-check ("Calm 4-7-8" als kop), 23 sea log blad 3 met alle 25 dieren (keuze 18), 24 inhouden met de krab.
            Application.Storage.deleteValue(EbbTrouw.GEKOZEN);
            if (k == 22) {
                var cc = new StartCheckView();
                cc.zetCalm();
                return [cc, new StartCheckDelegate(cc)];
            }
            // Keuring bouw 3 punt 14: 27 sea log blad 2, 28 menu bij de eerste start (nog geen dier).
            if (k == 27) {
                Application.Storage.setValue(EbbTrouw.BITS, 255);
                var dv2 = new DierenView();
                dv2.keuze = 12;
                return [dv2, new DierenDelegate(dv2)];
            }
            if (k == 28) {
                Application.Storage.setValue(EbbTrouw.BITS, 0);
                var mv0 = new EbbMenuView();
                return [mv0, new EbbMenuDelegate(mv0)];
            }
            if (k == 23) {
                Application.Storage.setValue(EbbTrouw.BITS, (1 << 25) - 1);
                var dv3 = new DierenView();
                dv3.keuze = 18;
                return [dv3, new DierenDelegate(dv3)];
            }
            if (k == 4) {
                // Blad v8 C1: 8 gevonden, de keuze op de Pufferfish (nog niet gevonden).
                Application.Storage.setValue(EbbTrouw.BITS, 255);
                var dv = new DierenView();
                dv.keuze = 8;
                return [dv, new DierenDelegate(dv)];
            }
            if (k == 7) {
                var rv = new RustigView(Ebb.calm(), EbbStart.CALM_NAAM);
                // Stilgezet 0,53 s in de fase "in": het getal staat boven de golf (run 42868087287).
                rv.plaatjeMs = 530;
                zetRustig(rv);
                return [rv, new RustigDelegate(rv)];
            }
            if (k == 10) {
                Application.Storage.setValue(EbbTrouw.BITS, 15);
                var mv = new EbbMenuView();
                return [mv, new EbbMenuDelegate(mv)];
            }
            if (k == 11 || k == 12) {
                Application.Storage.setValue(EbbStart.UITLEG, k == 12);
                var sc = new StartCheckView();
                return [sc, new StartCheckDelegate(sc)];
            }
            if (k >= 13 && k <= 15) {
                var vv = new VeiligView();
                vv.blad = k - 13;
                return [vv, new VeiligDelegate(vv)];
            }
            view.sessie = new Ebb.Rondes(30, 1500, 3, 15000, System.getTimer());
            view.opnemen = false;
            if (k == 29) {
                // Keuring bouw 3 punt 14: weekdoel gehaald (3 van 3 deze week, 5 weken op rij), eindscherm zonder nieuw dier.
                view.sessie.fase = Ebb.FASE_KLAAR;
                view.opgeslagen = true;
                view.einde = true;
                view.eindReeks = 5;
                view.plaatjeWeek = 3;
                view.sessie.inhoudtijden = [70000, 85000, 100000] as Array<Number>;
                view.eindVolgend = 7;
                view.eindRest = 2;
                view.gezelschap = EbbTrouw.zwemmer();
                return [view, new EbbDelegate(view)];
            }
            if (k == 26) {
                // Keuring bouw 3 punt 14: Calm onder 1 minuut (45 s, telt niet mee: "from 1 min it counts").
                Application.Storage.setValue(EbbTrouw.BITS, 15);
                return [new CalmEindeView(45000, 4, [] as Array<Number>, 5), new CalmEindeDelegate()];
            }
            if (k == 25) {
                // Keuring bouw 3 punt 12 en 14: alle 24 gevonden, "sea complete", reeks 12 weken.
                Application.Storage.setValue(EbbTrouw.BITS, (1 << 25) - 1);
                Application.Storage.setValue(EbbTrouw.GEKOZEN, 23);
                view.sessie.fase = Ebb.FASE_KLAAR;
                view.opgeslagen = true;
                view.einde = true;
                view.eindReeks = 12;
                view.sessie.inhoudtijden = [80000, 105000, 118000] as Array<Number>;
                view.eindVolgend = -1;
                return [view, new EbbDelegate(view)];
            }
            if (k == 21) {
                // Calm-eindscherm 6d (blad v7): 4 min, 12 ademhalingen, je schildpad, 5 dagen op rij.
                Application.Storage.setValue(EbbTrouw.BITS, 15);
                return [new CalmEindeView(240000, 12, [] as Array<Number>, 5), new CalmEindeDelegate()];
            }
            if (k == 19 || k == 20) {
                // Settings 1 en 2 (blad v7 scherm 9 en 9b): keuze op Breathing pace, en op "Ebb makes no sound".
                var iv = new EbbInstellingenView();
                iv.keuze = (k == 19) ? 1 : 12;
                return [iv, new EbbInstellingenDelegate(iv)];
            }
            if (k >= 16 && k <= 18) {
                // Eindschermen (keuring bouw 1 punt 7): 16 is 6c (3 rondes, Clownfish nog 1), 17 is 6b (Starfish nieuw),
                // 18 is 6c met 6 rondes (past het op 260?).
                view.sessie.fase = Ebb.FASE_KLAAR;
                view.opgeslagen = true;
                view.einde = true;
                view.eindReeks = 4;
                if (k == 17) {
                    view.sessie.inhoudtijden = [70000, 85000, 100000] as Array<Number>;
                    view.nieuweDieren = [6] as Array<Number>;
                } else {
                    view.sessie.inhoudtijden = (k == 16) ? [80000, 105000, 184000] as Array<Number>
                        : [62000, 75000, 81000, 95000, 104000, 112000] as Array<Number>;
                    view.eindVolgend = 7;
                    view.eindRest = 1;
                }
                return [view, new EbbDelegate(view)];
            }
            if (k == 5 || k == 6) {
                view.sessie.fase = Ebb.FASE_KLAAR;
                view.sessie.inhoudtijden = [85000, 118000, 96000] as Array<Number>;
                view.getij = (k == 6);
                return [view, new EbbDelegate(view)];
            }
            if (k == 8) {
                // Herstel na ronde 2 (1:45), "15 s" (blad v6 scherm 4).
                view.sessie.inhoudtijden = [80000, 105000] as Array<Number>;
                view.sessie.ronde = 1;
                view.plaatjeFase = Ebb.FASE_HERSTEL;
                view.plaatjeMs = 200;
            } else if (k == 9) {
                // Ademen: ademhaling 23 van 30, ronde 2, in (blad v6 scherm 2).
                view.sessie.inhoudtijden = [80000] as Array<Number>;
                view.sessie.ronde = 1;
                view.plaatjeFase = Ebb.FASE_ADEMEN;
                view.plaatjeMs = 22 * 3000 + 400;
            } else if (k == 30) {
                // Keuring bouw 3 punt 14: ademen uit (ademhaling 23, tweede helft).
                view.sessie.inhoudtijden = [80000] as Array<Number>;
                view.sessie.ronde = 1;
                view.plaatjeFase = Ebb.FASE_ADEMEN;
                view.plaatjeMs = 22 * 3000 + 2100;
            } else if (k == 24) {
                // Inhouden op 1:45 met de krab als gekozen maatje (4 dieren gevonden plus de krab).
                Application.Storage.setValue(EbbTrouw.BITS, 31);
                Application.Storage.setValue(EbbTrouw.GEKOZEN, 4);
                view.sessie.ronde = 1;
                view.plaatjeMs = 105000;
            } else {
                var tijd = [30000, 105000, 150000, 184000] as Array<Number>;
                var ronde = [0, 1, 2, 2] as Array<Number>;
                // Keuring bouw 3 punt 8: de testreeks steeds met hetzelfde eigen dier (de schildpad).
                Application.Storage.setValue(EbbTrouw.BITS, 15);
                view.sessie.ronde = ronde[k];
                view.plaatjeMs = tijd[k];
            }
            view.gezelschap = EbbTrouw.zwemmer();
            return [view, new EbbDelegate(view)];
        }
        if (!EbbBouw.DEMO) {
            // Keuring bouw 3 punt 10: oude reeks in dagen één keer wissen (opslagversie 2).
            EbbTrouw.werkOpslagBij();
            EbbTrillen.aan = EbbInstellingen.trillen();
            if (EbbVeilig.moetTonen()) {
                var vv = new VeiligView();
                return [vv, new VeiligDelegate(vv)];
            }
            var mv = new EbbMenuView();
            return [mv, new EbbMenuDelegate(mv)];
        }
        return [view, new EbbDelegate(view)];
    }
}

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
        EbbTeken.strook(dc, d);
        var regels = EbbVeiligTekst.BLADEN[blad];
        var geel = (blad == EbbVeiligTekst.BLADEN.size() - 1);
        var f = Graphics.FONT_XTINY;
        var lh = dc.getFontHeight(f);
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
        var pilMax = (EbbTeken.STROOK_TOP - 0.02) * d - bh / 2.0;
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
        EbbTeken.strook(dc, d);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.20).toNumber(), Graphics.FONT_SMALL, "how it works", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        var f = Graphics.FONT_XTINY;
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
        EbbTeken.zeeBanden(dc, d, [0.83, 0.90] as Array<Float>, [1, 2] as Array<Number>, 0.010, 0.0);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.235).toNumber(), Graphics.FONT_XTINY, kop(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        // Blad v7 punt 7: "Sit or lie down" in plaats van "Seated or lying?".
        dc.drawText(w / 2, (d * 0.385).toNumber(), Graphics.FONT_MEDIUM, "Sit or", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.drawText(w / 2, (d * 0.49).toNumber(), Graphics.FONT_MEDIUM, "lie down", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbTeken.pil(dc, d, 0.655, 0.40, 0.13, "Start", Graphics.FONT_SMALL);
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

class EbbView extends WatchUi.View {
    var sessie as Ebb.Rondes;
    private var _timer as Timer.Timer = new Timer.Timer();

    function initialize() {
        View.initialize();
        sessie = EbbInstellingen.rondes(System.getTimer());
    }

    var opname as EbbOpname = new EbbOpname();
    // Dieren die je deze sessie verdiende (nummers in EbbTrouw.DIEREN); het scherm "new friend" komt met blad v4.
    var nieuweDieren as Array<Number> = [] as Array<Number>;
    var opnemen as Boolean = true;
    // Alleen in de plaatjesbouw: start meteen in het inhouden op deze tijd en zet de klok stil.
    var plaatjeMs as Number = -1;
    var plaatjeFase as Ebb.Fase = Ebb.FASE_INHOUDEN;
    var plaatjeWeek as Number = 2;   // sessies deze week in de testbeelden
    // Na de sessie: today en 8 weeks (getij = true) wisselen met de knoppen.
    var getij as Boolean = false;
    // Keuring bouw 1 punt 7: eerst het eindscherm (6b met nieuw dier, 6c zonder), daarna today en 8 weeks.
    var einde as Boolean = false;
    var eindReeks as Number = 0;      // weken op rij na deze sessie
    var eindVolgend as Number = -1;   // volgende dier (nummer in EbbTrouw.DIEREN), -1 als je alles hebt
    var eindRest as Number = 0;       // wat er nog nodig is voor dat dier (0: ligt klaar voor de volgende sessie)
    const YKLEIN_ADEMEN = 0.855;
    const ONDER_MIDDEN = 0.84;
    private var _klaarSinds as Number = -1;
    var gezelschap as Number = EbbTrouw.zwemmer();
    private var _dierPlaatje as EbbDierPlaatje or Null = null;
    private var _startTijd as Number = System.getTimer();
    private var _gestart as Boolean = false;
    private var _lapsGesloten as Number = 0;

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            sessie.segmentStart = System.getTimer();
            if (plaatjeMs >= 0) {
                var nu = System.getTimer();
                sessie.fase = plaatjeFase;
                sessie.segmentStart = nu - plaatjeMs;
                sessie.pauzeer(nu);
            }
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
        opname.inhouden((tijd + 500) / 1000, sessie.ademhalingen);
        return true;
    }

    // Dagnummer van de lokale datum (dagen sinds 1970).
    static function vandaag() as Number {
        return (Time.today().value() + System.getClockTime().timeZoneOffset) / 86400;
    }

    // Opslaan: activiteit bewaren en de inhoudtijden in de 56 dagen zetten.
    // Keuring bouw 1 punt 1: een sessie telt maar één keer (today, 8 weeks, dagen, dieren), ook als opslaan twee keer wordt gevraagd.
    var opgeslagen as Boolean = false;

    function opslaan() as Boolean {
        if (opgeslagen) {
            System.println("OPNAME al opgeslagen, niet dubbel");
            return false;
        }
        opgeslagen = true;
        var ok = opname.opslaan();
        System.println("OPNAME opgeslagen " + ok + " laps " + (opname.laps + 1));
        var opslag = new EbbOpslag();
        var dag = vandaag();
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            opslag.voegToe(dag, (sessie.inhoudtijden[i] + 500) / 1000);
        }
        opslag.bewaar();
        // Blad v6 today: de hele dag, per sessie de klok en de inhoudtijden.
        var secs = [] as Array<Number>;
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            secs.add((sessie.inhoudtijden[i] + 500) / 1000);
        }
        var klok = System.getClockTime();
        // Keuring bouw 3 punt 11: geen lege sessie in Today bij 0 inhouden.
        if (secs.size() > 0) {
            EbbVandaag.bewaar(dag, klok.hour * 60 + klok.min, secs);
        }
        // Trouw: tellers en nieuwe dieren pas aan het eind van de sessie (besluit 22:53, punt 1 en 4).
        var meetelt = EbbTrouw.telt(sessie.inhoudtijden.size(), 0);
        var tellers = meetelt ? EbbTrouw.naSessie(dag) : EbbTrouw.stand(dag);
        nieuweDieren = meetelt ? EbbTrouw.nieuweDieren(tellers) : [] as Array<Number>;
        eindReeks = tellers[1];
        var v = EbbTrouw.volgende(tellers);
        eindVolgend = v[0];
        eindRest = v[1];
        System.println("TROUW nieuwe dieren " + nieuweDieren);
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
    private var _vorigInhoudMs as Number = 0;
    private var _tik30 as Boolean = EbbInstellingen.tik30();
    private var _laatste3 as Boolean = EbbInstellingen.laatste3();

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
            // Alleen aanzetten: de testbeelden zetten einde zelf (scène 16 tot 18) en mogen niet overschreven worden.
            if (!EbbBouw.DEMO && !EbbBouw.PLAATJE) {
                einde = true;
            }
        }
        // Testbouw: 15 s na het today vanzelf naar 8 weeks, voor de schermafbeelding d.
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
                _vorigInhoudMs = 0;
                EbbTrillen.tril(EbbTrillen.M_INHOUDEN);
            } else if (fase == Ebb.FASE_HERSTEL) {
                EbbTrillen.tril(EbbTrillen.M_HERSTEL);
            } else if (fase == Ebb.FASE_KLAAR) {
                EbbTrillen.tril(EbbTrillen.M_KLAAR);
            }
        } else if (fase == Ebb.FASE_ADEMEN && isIn != _vorigIn) {
            if (isIn && _laatste3 && sessie.laatsteDrie(nu)) {
                EbbTrillen.tril(EbbTrillen.M_LAATSTE);
            } else {
                EbbTrillen.tril(isIn ? EbbTrillen.M_IN : EbbTrillen.M_UIT);
            }
        } else if (fase == Ebb.FASE_INHOUDEN) {
            var ms = sessie.verstreken(nu);
            var sig = Ebb.inhoudSignaal(_vorigInhoudMs, ms, _tik30);
            if (sig == 2) {
                EbbTrillen.tril(EbbTrillen.M_DRIE_MIN);
            } else if (sig == 1) {
                EbbTrillen.tril(EbbTrillen.M_DERTIG);
            }
            _vorigInhoudMs = ms;
        }
        _vorigeFase = fase;
        _vorigIn = isIn;
    }

    // Keuring 01:55 punt 6: hoe je het inhouden stopt, per horloge de juiste knop (resources-venu2, -venu3, -vivoactive5).
    private var _stop as String or Null = null;
    function stopTekst() as String {
        if (_stop == null) {
            _stop = WatchUi.loadResource(Rez.Strings.StopTekst) as String;
        }
        return _stop as String;
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
        var grootDx = 0;
        if (fase == Ebb.FASE_ADEMEN) {
            // 1. Ademen: peil volgt de adem, 20% bij uit, 72% bij in (Mila 80%; lager zodat het fasewoord nooit onder water staat, beeld run 42800407029).
            // Keuring bouw 1 punt 5 en Daan B2: zee onderaan zoals blad v6 scherm 2, het getal altijd erboven.
            EbbTeken.ademZee(dc, d, sessie.water(nu), golfFase);
            yGroot = 0.39 - dc.getFontHeight(font).toFloat() / d / 2;
            woord = sessie.isIn(nu) ? "breathe in" : "breathe out";   // blad v6 scherm 2
            groot = sessie.ademhaling(nu).toString();
            klein = "of " + sessie.ademhalingen + " · round " + (sessie.ronde + 1);
            // Daan M1: laagste golfrand ligt op 1 - 0,20 + 0,025 = 0,825 D; de ondertekst begint eronder (0,855; run 42826914263 gaf bij 0,84 maar 2 px ruimte op 260 px),
            // zodat hij altijd helemaal in het water staat en nooit op de schuimrand.
            // Keuring bouw 2 punt 10: onderste regel op alle ademschermen op dezelfde hoogte, midden op 0,84 D (381 px op 454).
            yKlein = ONDER_MIDDEN - dc.getFontHeight(Graphics.FONT_XTINY).toFloat() / d / 2;
        } else if (fase == Ebb.FASE_INHOUDEN) {
            // Blad v6 (3a, 3b, 3d, 3c; keuring 01:55 punt 2): de zee wordt elke 30 s een stand donkerder tot 2:30
            // (EbbProfiel.zeeStand), daarna gelijk. Bovenaan "hold" (na 3:00 "time to breathe" met trilteken),
            // daaronder hoe je stopt, dan de tijd, je dier, en onderaan hartslag en ronde.
            var s = t / 1000;
            var stand = EbbProfiel.zeeStand(s);
            EbbTeken.zee(dc, d, stand, golfFase);
            var fhT = dc.getFontHeight(Graphics.FONT_SMALL);
            var fhK = dc.getFontHeight(Graphics.FONT_XTINY);
            var yKop = (d * 0.20).toNumber();
            if (s < 180) {
                dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
                dc.drawText(w / 2, yKop, Graphics.FONT_SMALL, "hold", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            } else {
                var tb = "time to breathe";
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
                dc.drawText(w / 2, yKop, Graphics.FONT_XTINY, tb, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
                EbbTeken.trilboog(dc, d, yKop, dc.getTextWidthInPixels(tb, Graphics.FONT_XTINY));
            }
            var yStop = yKop + fhT / 2 + fhK / 2;
            dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, yStop, Graphics.FONT_XTINY, stopTekst(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            // De tijd direct onder de stopregel: de lege ruimte boven de cijfers (hoogte min ascent min descent)
            // valt weg, zodat de cijfers 2% D onder de stopregel beginnen.
            var leeg = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            var yTijd = yStop + fhK / 2 + (d * 0.02).toNumber() - (leeg > 0 ? leeg : 0);
            yGroot = yTijd.toFloat() / d;
            var onderCijfer = yTijd + (leeg > 0 ? leeg : 0) + Graphics.getFontAscent(font);
            // Beelden run 42938098473 (fr265): de walvis raakte de hartregel en met zijn fontein bijna de cijfers.
            // Daarom het kleine dier (zoals in de sea log, blad v6: 0,10 D) vlak onder de cijfers en de hartregel lager.
            // Keuring bouw 2 punt 7: het dier groter (±0,19 D breed: 86 px op 454, 49 px op 260), midden onder de tijd.
            var yDier = onderCijfer + (d * 0.085).toNumber();
            var yRegel = (d * ONDER_MIDDEN).toNumber();
            // Belletjes links en rechts van het dier, vanaf 2:30 geen belletjes meer (blad v6 punt 5).
            if (stand < 5) {
                var stijg = (t % 8000) / 8000.0;
                var yd = yDier.toFloat() / d;
                // Keuring bouw 2 punt 7: belletjes alleen bij het dier, net naast zijn kop en staart.
                EbbTeken.bellen(dc, d, [[0.37, yd - 0.02 - 0.06 * stijg, 0.011], [0.63, yd - 0.04 - 0.06 * stijg, 0.008]] as Array<Array<Float> >);
            }
            // Daan B3 en keuring bouw 1 punt 6: je eigen dier rust in het midden onder de tijd (geen rode vis die
            // voorbij zwemt), in de eigen kleuren van Mila's data; zonder dier (nieuwe gebruiker) alleen de zee.
            if (gezelschap >= 0) {
                // Rustig heen en weer: ±1,5 procent D in 8 s (in de testbeelden stil in het midden).
                var dx = EbbBouw.PLAATJE ? 0 : (Math.sin((t % 8000) * 2.0 * Math.PI / 8000.0) * d * 0.015).toNumber();
                // Keuring bouw 3 punt 8: het dier past in 90 x 70 op 454 (50 x 40 op 260), onderkant 8 px boven de hartslagregel.
                var mz = EbbDierMaat.inVak(gezelschap, (d * 0.198).toNumber(), (d * 0.154).toNumber());
                var gz = EbbDierMaat.grenzen(gezelschap);
                var yOnder = yRegel - dc.getFontHeight(Graphics.FONT_XTINY) / 2 - 8 - EbbDierData.randPx(mz);
                var yd2 = yOnder - gz[3] * mz / EbbDierData.SCHAAL;
                var dp = _dierPlaatje;
                if (dp == null || dp.dier != gezelschap || dp.maat != mz) {
                    dp = new EbbDierPlaatje(gezelschap, mz);
                    _dierPlaatje = dp;
                }
                if (dp.verder()) {
                    dp.plak(dc, w / 2 + dx, yd2 < yDier ? yDier : yd2);
                } else {
                    WatchUi.requestUpdate();
                }
            }
            groot = (s / 60).toString() + ":" + (s % 60).format("%02d");
            // Daan K2: in de stilgezette testbeelden een nagebootste hartslag (61), zodat je ziet hoe het eruitziet als het werkt.
            EbbTeken.hartRonde(dc, d, yRegel, EbbBouw.PLAATJE ? 61 : EbbOpname.hartslag(), sessie.ronde + 1);
        } else if (fase == Ebb.FASE_HERSTEL) {
            // Blad v6 scherm 4 (herstel): de zon komt op achter de zee (W0, W1, W2), bovenaan "big breath in, hold",
            // groot de seconden met een kleine "s", onderaan "round 2 held 1:45".
            // Keuring bouw 2 punt 10 en beelden run 42955254555: de zon raakte de onderkant van "15" nog. Nu staat de
            // bovenkant van de zon 10 px onder de onderkant van de cijfers (zelfde rekensom als hieronder voor "s").
            var zr = (d * 0.10).toNumber();
            var yG = 0.415 - dc.getFontHeight(font).toFloat() / d / 2;
            var leegZ = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            var onderZ = (d * yG).toNumber() + (leegZ > 0 ? leegZ : 0) + Graphics.getFontAscent(font);
            var zcy = onderZ + 10 + zr;
            var zMin = (d * 0.67).toNumber();
            zcy = zcy < zMin ? zMin : zcy;
            dc.setColor(EbbTeken.GEEL, EbbTeken.GEEL);
            dc.fillCircle(w / 2, zcy, zr);
            EbbTeken.zeeBanden(dc, d, [0.64, 0.72, 0.86] as Array<Float>, [0, 1, 2] as Array<Number>, 0.014, golfFase);
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            // Beelden run 42940068457: op vivoactive 5 en fenix 8 liep deze regel in FONT_SMALL door de ronde rand.
            // Past hij niet binnen 80 procent van de koorde op 0,215 D, dan de kleinere letter.
            var kop = "big breath in, hold";
            var kopF = Graphics.FONT_SMALL;
            var koorde = 2.0 * Math.sqrt(0.16 - 0.285 * 0.285) * d;   // binnen de cirkel van 0,8 D op 0,215 D
            if (dc.getTextWidthInPixels(kop, kopF) > koorde) {
                kopF = Graphics.FONT_XTINY;
            }
            groot = ((sessie.herstelMs - t) / 1000 + 1).toString();
            // Keuring bouw 3 punt 6: het cijfer zelf in het midden, "s" los erachter; de kop minstens 12 px (454)
            // of 6 px (260) boven de bovenkant van de cijfers.
            grootDx = 0;
            yGroot = 0.415 - dc.getFontHeight(font).toFloat() / d / 2;
            var leegH = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            var topH = (d * yGroot).toNumber() + (leegH > 0 ? leegH : 0);
            var gatH = (d * 0.026).toNumber();
            gatH = gatH < 6 ? 6 : gatH;
            var yKopH = topH - gatH - dc.getFontHeight(kopF) / 2;
            var yKop0 = (d * 0.215).toNumber();
            dc.drawText(w / 2, (yKopH < yKop0 ? (yKopH < d * 0.12 ? (d * 0.12).toNumber() : yKopH) : yKop0), kopF, kop, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            var onderH = (d * yGroot).toNumber() + (leegH > 0 ? leegH : 0) + Graphics.getFontAscent(font);
            var bg = dc.getTextWidthInPixels(groot, font);
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2 + grootDx + bg / 2 + 3, onderH - Graphics.getFontAscent(Graphics.FONT_SMALL), Graphics.FONT_SMALL, "s", Graphics.TEXT_JUSTIFY_LEFT);
            var n = sessie.inhoudtijden.size();
            if (n > 0) {
                var hs = (sessie.inhoudtijden[n - 1] + 500) / 1000;
                klein = "round " + n + " held " + (hs / 60).toString() + ":" + (hs % 60).format("%02d");
            }
            yKlein = ONDER_MIDDEN - dc.getFontHeight(Graphics.FONT_XTINY).toFloat() / d / 2;
        } else {
            // Na de sessie: eindscherm, 8 weeks of today.
            if (einde) {
                tekenEinde(dc, d);
            } else if (getij) {
                tekenGetij(dc, d);
            } else {
                tekenProfiel(dc, d);
            }
        }
        if (woord.length() > 0) {
            // Staat het lichte water tot boven, dan leest het zachte woord niet meer: dan donkerblauw.
            dc.setColor(donker ? EbbTeken.DIEPTE[3] : EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * 0.13).toNumber(), Graphics.FONT_SMALL, woord, Graphics.TEXT_JUSTIFY_CENTER);
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (groot.length() > 0) {
            dc.drawText(w / 2 + grootDx, (d * yGroot).toNumber() + dc.getFontHeight(font) / 2, font, groot, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        if (klein.length() > 0) {
            dc.setColor(fase == Ebb.FASE_INHOUDEN ? EbbTeken.ZACHT : Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * yKlein).toNumber(), Graphics.FONT_XTINY, klein, Graphics.TEXT_JUSTIFY_CENTER);
        }
        if (EbbBouw.DEMO) {
            meet(dc, w, fase as Number, groot, font);
            if (fase == Ebb.FASE_ADEMEN && !_onderGemeld && klein.length() > 0) {
                meetOnder(dc, d, klein);
            }
        }
    }

    // Daan M1, alleen in de testbouw: ruimte tussen de laagste golfrand en de ondertekst, en of de ondertekst
    // op zijn breedste regel (de onderkant) binnen het ronde scherm past. Alles in pixels.
    private var _onderGemeld as Boolean = false;
    function meetOnder(dc as Graphics.Dc, d as Number, klein as String) as Void {
        _onderGemeld = true;
        var golf = (d * (EbbTeken.ADEM_TOP + EbbTeken.ADEM_AMP)).toNumber() + (d / 160 > 1 ? d / 160 : 1) / 2 + 1;
        var top = (d * YKLEIN_ADEMEN).toNumber();
        var leeg = dc.getFontHeight(Graphics.FONT_XTINY) - Graphics.getFontAscent(Graphics.FONT_XTINY) - Graphics.getFontDescent(Graphics.FONT_XTINY);
        var letterTop = top + (leeg > 0 ? leeg : 0);
        var onder = top + Graphics.getFontAscent(Graphics.FONT_XTINY) + (leeg > 0 ? leeg : 0);
        var breed = dc.getTextWidthInPixels(klein, Graphics.FONT_XTINY);
        var r = d / 2.0;
        var dy = onder - r;
        var koorde = (dy < r) ? (2.0 * Math.sqrt(r * r - dy * dy)).toNumber() : 0;
        System.println("ONDERTEKST golf " + golf + " lettertop " + letterTop + " ruimte " + (letterTop - golf) + " breedte " + breed + " koorde " + koorde + " over " + (koorde - breed));
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

    // Blad v6 scherm 6 (today, keuring 01:55 punt 2 en 5): de hele dag als staande staven in één egale tint
    // (geen nadruk op de langste), per sessie een groepje met de klok eronder, onderaan "6 holds · avg 1:44".
    function vandaagSessies() as Array<Array> {
        if (EbbBouw.PLAATJE) {
            // Keuring bouw 3 punt 14: today met 3 sessies (het meeste dat Today toont).
            return [[460, [70, 85, 100]], [765, [92, 110]], [1275, [80, 105, 184]]] as Array<Array>;
        }
        if (EbbBouw.DEMO) {
            return [[460, [70, 85, 100]], [1275, [80, 105, 184]]] as Array<Array>;
        }
        var lijst = EbbVandaag.lees(vandaag());
        if (lijst.size() == 0 && sessie.inhoudtijden.size() > 0) {
            // Niet opgeslagen (weggegooid): dan alleen deze sessie, zonder klok.
            var secs = [] as Array<Number>;
            for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
                secs.add((sessie.inhoudtijden[i] + 500) / 1000);
            }
            lijst.add([-1, secs] as Array);
        }
        return lijst;
    }

    // Tekst midden op hoogte y; FONT_SMALL als hij binnen de koorde past (met marge), anders FONT_XTINY.
    function tekstInRonde(dc as Graphics.Dc, d as Number, y as Float, tekst as String, kleur as Number) as Void {
        var dy = y - 0.5;
        var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.86;
        var f = (dc.getTextWidthInPixels(tekst, Graphics.FONT_SMALL) <= koorde) ? Graphics.FONT_SMALL : Graphics.FONT_XTINY;
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v7 scherm 6b en 6c (keuring bouw 1 punt 7): kop "3 rounds done", de tijden, de zee met het nieuwe dier (6b)
    // of het volgende dier als silhouet (6c), een regel, stippen voor het weekdoel met de reeks in weken.
    // Past bij 1 tot 6 rondes: tot 3 tijden op één regel, daarna twee regels in de kleine letter.
    function tekenEinde(dc as Graphics.Dc, d as Number) as Void {
        var w = d;
        var n = sessie.inhoudtijden.size();
        var tijden = [] as Array<String>;
        for (var i = 0; i < n; i += 1) {
            var s = (sessie.inhoudtijden[i] + 500) / 1000;
            tijden.add((s / 60) + ":" + (s % 60).format("%02d"));
        }
        var kopY = (n > 3) ? 0.14 : 0.17;
        // Beelden run 42955254555: bij 4 tot 6 rondes raakte de tweede regel tijden de schuimkam. De zee begint nu
        // 8 px plus de golfhoogte onder de onderkant van de tweede regel, gerekend met de echte letterhoogtes.
        var lhX = dc.getFontHeight(Graphics.FONT_XTINY);
        var lhS = dc.getFontHeight(Graphics.FONT_SMALL);
        // Keuring bouw 3 punt 6: tijden minstens 10 px onder de titel op 454 en 6 px op 260 (0,022 D).
        var gat = (d * 0.022).toNumber();
        gat = gat < 6 ? 6 : gat;
        var y1 = (d * kopY).toNumber() + lhS / 2 + gat + lhX / 2;
        var yTijden = (d * kopY).toNumber() + lhS + gat;   // midden van de ene regel tijden in de grote letter
        var onderTijden = (n > 3) ? y1 + lhX + lhX / 2 : yTijden + lhS / 2;
        var zeeTop = 0.326;
        var t = (onderTijden + 8 + d * 0.02) / d.toFloat();
        zeeTop = t > zeeTop ? t : zeeTop;
        EbbTeken.zeeBanden(dc, d, [zeeTop, 0.60, 0.88] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * kopY).toNumber(), Graphics.FONT_SMALL, n + (n == 1 ? " round done" : " rounds done"), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (n <= 3) {
            dc.drawText(w / 2, yTijden, Graphics.FONT_SMALL, regel(tijden, 0, n), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        } else {
            var helft = (n + 1) / 2;
            // Keuring bouw 2 punt 4: twee regels van 3, de eerste 6 px onder de titel.
            var lh = lhX;
            dc.drawText(w / 2, y1, Graphics.FONT_XTINY, regel(tijden, 0, helft), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            dc.drawText(w / 2, y1 + lh, Graphics.FONT_XTINY, regel(tijden, helft, n), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        var cy = (d * (n > 3 ? 0.48 : 0.465)).toNumber();
        if (nieuweDieren.size() > 0) {
            var dier = nieuweDieren[0];
            // Keuring bouw 3 punt 8: het nieuwe dier 15 px lager (op 454).
            EbbDierData.teken(dc, dier, w / 2, cy + (d * 0.033).toNumber(), (d * 0.15).toNumber(), -1);
            tekstInRonde(dc, d, 0.645, "new friend: " + EbbDierData.NAMEN[dier], EbbTeken.LICHT);
        } else if (eindVolgend >= 0) {
            // Mila v8: silhouet met rand en kenmerk (banden van de clownvis, vlek van de orka) in 00AAFF.
            EbbDierData.silhouet(dc, eindVolgend, w / 2, cy, (d * (n > 3 ? 0.09 : 0.105)).toNumber());
            tekstInRonde(dc, d, 0.645, volgendTekst(), Graphics.COLOR_WHITE);
        } else {
            // Keuring bouw 3 punt 12 (besluit 2): na de walvis "sea complete" met je eigen dier; de reeks in weken
            // eronder blijft groeien ("12 weeks in a row"), zonder nieuwe dieren.
            var eigen = EbbTrouw.zwemmer();
            if (eigen >= 0) {
                EbbDierData.teken(dc, eigen, w / 2, cy, EbbDierMaat.inVak(eigen, (d * 0.26).toNumber(), (d * 0.18).toNumber()), -1);
            }
            tekstInRonde(dc, d, 0.645, "sea complete", EbbTeken.LICHT);
        }
        // Besluit 11 nov 04:30: de week in plaats van dagen op rij; geen rustdagzin meer (een week heeft vanzelf rust).
        var dag = vandaag();
        var boven = (d * 0.645).toNumber() + dc.getFontHeight(Graphics.FONT_SMALL) / 2;
        EbbTeken.weekStippen(dc, d, eindReeks, ((EbbBouw.DEMO || EbbBouw.PLAATJE) ? plaatjeWeek : EbbTrouw.dezeWeek(dag)), EbbTrouw.weekdoel(), boven);
    }

    function regel(tijden as Array<String>, van as Number, tot as Number) as String {
        var s = "";
        for (var i = van; i < tot; i += 1) {
            s += (i > van ? "   " : "") + tijden[i];
        }
        return s;
    }

    // Keuring bouw 2 punt 4: geen "next:" (besluit 22:53 punt 3), wel wat er nog nodig is: "1 more session",
    // "2 more weeks in a row", of "next session" als het dier al klaar ligt.
    function volgendTekst() as String {
        // Keuring bouw 3 punt 11: zeg wat er komt ("1 more session: new friend").
        if (eindRest <= 0) {
            return "next session: new friend";
        }
        if ((EbbTrouw.DIEREN[eindVolgend][1] as Number) == EbbTrouw.SOORT_REEKS) {
            return eindRest + (eindRest == 1 ? " more week: new friend" : " more weeks: new friend");
        }
        return eindRest + (eindRest == 1 ? " more session: new friend" : " more sessions: new friend");
    }

    function tekenProfiel(dc as Graphics.Dc, d as Number) as Void {
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.18).toNumber(), Graphics.FONT_SMALL, "today", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbTeken.strook(dc, d);
        var sessies = vandaagSessies();
        var samen = EbbVandaag.samen(sessies);
        if (samen[0] == 0) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, d / 2, Graphics.FONT_SMALL, "no holds yet", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            return;
        }
        var lo = d * 0.20;
        var ro = d * 0.80;
        var bod = (d * 0.62).toNumber();
        var hoog = d * 0.27;
        var gat = d * 0.08;
        var maxS = 200;
        for (var i = 0; i < sessies.size(); i += 1) {
            var t = sessies[i][1] as Array<Number>;
            for (var j = 0; j < t.size(); j += 1) {
                if (t[j] > maxS) { maxS = t[j]; }
            }
        }
        var kol = (ro - lo - gat * (sessies.size() - 1)) / samen[0];
        var bw = (kol * 0.62).toNumber();
        bw = bw < 2 ? 2 : bw;
        var r = (bw * 3) / 10;
        dc.setColor(EbbTeken.staafKleur(), EbbTeken.staafKleur());
        var x = lo;
        var midden = [] as Array<Float>;
        var breedte = [] as Array<Float>;
        for (var i = 0; i < sessies.size(); i += 1) {
            var t = sessies[i][1] as Array<Number>;
            midden.add(x + kol * t.size() / 2.0);
            breedte.add(kol * t.size());
            for (var j = 0; j < t.size(); j += 1) {
                var xm = x + kol * (j + 0.5);
                var h = (hoog * t[j] / maxS).toNumber();
                h = h < 2 ? 2 : h;
                dc.fillRoundedRectangle((xm - bw / 2.0).toNumber(), bod - h, bw, h, r);
            }
            x += kol * t.size() + gat;
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 150 > 2 ? d / 150 : 2);
        dc.drawLine((lo - d * 0.01).toNumber(), bod, (ro + d * 0.01).toNumber(), bod);
        // Klok onder elke sessie, alleen als hij onder zijn groepje past (anders lopen de tijden in elkaar).
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < sessies.size(); i += 1) {
            var k = sessies[i][0] as Number;
            if (k < 0) { continue; }
            var tekst = EbbVandaag.klokTekst(k);
            if (dc.getTextWidthInPixels(tekst, Graphics.FONT_XTINY) <= breedte[i] + gat * 0.8) {
                dc.drawText(midden[i].toNumber(), bod + (d * 0.055).toNumber(), Graphics.FONT_XTINY, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
        }
        var gem = samen[1];
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.775).toNumber(), Graphics.FONT_XTINY,
            samen[0] + (samen[0] == 1 ? " hold · avg " : " holds · avg ") + (gem / 60) + ":" + (gem % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v6 scherm 7 (8 weeks, keuring 01:55 punt 2): sessies per week als staven met het getal erboven, een lege
    // week als stip, onderaan "sessions per week" en het gemiddelde over 8 weken als getal.
    function wekenData() as Array<Array<Number> > {
        if (EbbBouw.DEMO || EbbBouw.PLAATJE) {
            var nep = [] as Array<Array<Number> >;
            var n = [0, 0, 0, 0, 0, 0, 3, 6] as Array<Number>;
            for (var i = 0; i < 8; i += 1) {
                nep.add([n[i] > 0 ? 101 : 0, n[i], n[i] * 3] as Array<Number>);
            }
            return nep;
        }
        return EbbProfiel.weken(new EbbOpslag(), EbbTrouw.sessieDagen(), vandaag());
    }

    function tekenGetij(dc as Graphics.Dc, d as Number) as Void {
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.18).toNumber(), Graphics.FONT_SMALL, "8 weeks", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbTeken.strook(dc, d);
        var weken = wekenData();
        var hoogN = 7;
        var som = 0;
        var holds = 0;
        var sessies = 0;
        for (var i = 0; i < weken.size(); i += 1) {
            if (weken[i][1] > hoogN) { hoogN = weken[i][1]; }
            som += weken[i][0] * weken[i][2];
            holds += weken[i][2];
            sessies += weken[i][1];
        }
        // Keuring bouw 3 punt 11: leeg is zonder sessies, niet zonder inhouden (alleen Calm telt ook).
        if (sessies == 0) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, d / 2, Graphics.FONT_SMALL, "no sessions yet", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            return;
        }
        var lo = d * 0.20;
        var top = d * 0.33;
        var bod = (d * 0.58).toNumber();
        var kol = d * 0.60 / 8;
        var bw = (kol * 0.66).toNumber();
        var r = (bw * 3) / 10;
        for (var i = 0; i < weken.size(); i += 1) {
            var n = weken[i][1];
            var xm = (lo + kol * (i + 0.5)).toNumber();
            if (n > 0) {
                var h = ((bod - top) * n / hoogN).toNumber();
                dc.setColor(EbbTeken.staafKleur(), EbbTeken.staafKleur());
                dc.fillRoundedRectangle(xm - bw / 2, bod - h, bw, h, r);
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
                dc.drawText(xm, bod - h - (d * 0.045).toNumber(), Graphics.FONT_XTINY, n.toString(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            } else {
                dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);   // lege week: kleine stip, donkerder dan de staven
                var rr = (d * 0.013).toNumber();
                dc.fillCircle(xm, bod - (d * 0.03).toNumber(), rr < 2 ? 2 : rr);
            }
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 150 > 2 ? d / 150 : 2);
        dc.drawLine(lo.toNumber(), bod, (d * 0.80).toNumber(), bod);
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.665).toNumber(), Graphics.FONT_XTINY, "sessions per week", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        if (holds == 0) {
            return;
        }
        var gem = (som + holds / 2) / holds;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.75).toNumber(), Graphics.FONT_XTINY, "avg hold " + (gem / 60) + ":" + (gem % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
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

    // Wat terug doet: tijdens inhouden stoppen, na de sessie naar het menu (nooit het pauzemenu,
    // keuring bouw 1 punt 1), anders het pauzemenu (doorgaan, opslaan, weggooien).
    function terugActie() as Symbol {
        var f = _view.sessie.fase;
        if (f == Ebb.FASE_KLAAR) {
            return :menu;
        }
        return (f == Ebb.FASE_INHOUDEN) ? :stop : :pauze;
    }

    function onBack() as Boolean {
        var actie = terugActie();
        if (actie == :stop) {
            return stop();
        }
        if (actie == :menu) {
            // De sessie is af en al bewaard (tik slaat op bij FASE_KLAAR); opslaan() telt hoogstens één keer.
            _view.opslaan();
            var mv = new EbbMenuView();
            WatchUi.switchToView(mv, new EbbMenuDelegate(mv), WatchUi.SLIDE_RIGHT);
            return true;
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

    // Aanraakscherm uit tijdens een sessie (productkeuring): tikken en vegen doen niets, alleen de knoppen werken.
    // Na de sessie mag vegen weer wisselen tussen vandaag en 8 weken.
    function aanraakAan() as Boolean {
        return _view.sessie.fase == Ebb.FASE_KLAAR;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return !aanraakAan();
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        return !aanraakAan();
    }

    // Na de sessie wisselen omhoog en omlaag in de rij eindscherm, today, 8 weeks; anders stoppen ze het inhouden.
    function wissel() as Boolean {
        if (_view.sessie.fase == Ebb.FASE_KLAAR) {
            if (_view.einde) {
                _view.einde = false;
                _view.getij = false;
            } else if (!_view.getij) {
                _view.getij = true;
            } else {
                _view.einde = true;
            }
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
