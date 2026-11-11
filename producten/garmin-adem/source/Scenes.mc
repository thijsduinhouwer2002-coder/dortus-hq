import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Alleen in de plaatjesbouw (EbbBouw.PLAATJE): per start één stilgezette scène voor de testbeelden.
// Volgorde en namen staan ook in .github/workflows/garmin-adem-iq.yml (NAMEN).
module EbbScenes {
    function start(app as EbbApp, view as EbbView) as [WatchUi.Views, WatchUi.InputDelegates] {
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
            app.zetRustig(rv);
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
        // Keuring bouw 4 punt 2: elk dierscherm met de krab en de zeekomkommer (watchdog): 31 menu met de krab,
        // 34 Calm-einde met de krab als nieuw dier; 32 en 33 hieronder.
        if (k == 31) {
            Application.Storage.setValue(EbbTrouw.BITS, 31);
            Application.Storage.setValue(EbbTrouw.GEKOZEN, 4);
            var mvk = new EbbMenuView();
            return [mvk, new EbbMenuDelegate(mvk)];
        }
        if (k == 34) {
            Application.Storage.setValue(EbbTrouw.BITS, 31);
            return [new CalmEindeView(240000, 12, [4] as Array<Number>, 5), new CalmEindeDelegate()];
        }
        view.sessie = new Ebb.Rondes(30, 1500, 3, 15000, System.getTimer());
        view.opnemen = false;
        if (k == 32 || k == 33) {
            // 32: eindscherm 6c met de krab als silhouet (volgende dier); 33: eindscherm 6b met de zeekomkommer nieuw.
            Application.Storage.setValue(EbbTrouw.BITS, 15);
            view.sessie.fase = Ebb.FASE_KLAAR;
            view.opgeslagen = true;
            view.einde = true;
            view.eindReeks = 4;
            view.sessie.inhoudtijden = [80000, 105000, 118000] as Array<Number>;
            if (k == 32) {
                view.eindVolgend = 4;
                view.eindRest = 1;
            } else {
                view.nieuweDieren = [24] as Array<Number>;
            }
            view.gezelschap = EbbTrouw.zwemmer();
            return [view, new EbbDelegate(view)];
        }
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
}
