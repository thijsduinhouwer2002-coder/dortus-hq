import Toybox.Application;
import Toybox.Lang;

// Trouw: tellers, sessiedagen en de reeks in weken. De dieren zelf staan in TrouwDieren.mc (zelfde module).
module EbbTrouw {
    const SESSIES = "trSessies";
    const DAG = "trDag";
    const REEKS = "trReeks";
    const BESTE = "trBeste";
    const PAUZE = "trPauze";      // 1 zodra je terugkwam na 7 of meer dagen zonder sessie (zeekomkommer)
    const SESDAGEN = "trSesDagen"; // dagnummer van elke opgeslagen sessie in de laatste 56 dagen (8 weeks)
    const PAUZE_DAGEN = 7;
    const DAGSES = "trDagSes";     // sessies vandaag (voor de grens van 2 per dag)
    const MAX_PER_DAG = 2;         // keuring G2: voor de dieren tellen hoogstens 2 sessies per dag
    const WEEK = "trWeek";         // weeknummer (maandag tot zondag) van de laatste sessie
    const WEEKSES = "trWeekSes";   // tellende sessies in die week
    const WEEKGEH = "trWeekGeh";   // keuring bouw 3 punt 10: 1 als het weekdoel deze week al een week opleverde
    const VERSIE = "trVersie";     // opslagversie; 2 = reeks in weken (oude trReeks en trBeste waren dagen)
    const OPSLAG_VERSIE = 2;

    // Keuring bouw 3 punt 10: oude opslag één keer bijwerken. De reeks en beste reeks waren dagen en zijn nu weken;
    // bewaard laten zou dieren op weken geven voor dagen. Geeft true als er gewist is.
    function werkOpslagBij() as Boolean {
        if (getal(VERSIE) >= OPSLAG_VERSIE) {
            return false;
        }
        var oud = Application.Storage.getValue(REEKS) != null || Application.Storage.getValue(BESTE) != null;
        Application.Storage.deleteValue(REEKS);
        Application.Storage.deleteValue(BESTE);
        Application.Storage.setValue(WEEKGEH, getal(WEEKSES) >= weekdoel() ? 1 : 0);
        Application.Storage.setValue(VERSIE, OPSLAG_VERSIE);
        return oud;
    }

    // Besluit hoofdchat 11 nov 04:30 (keuring bouw 2, besluit 1): de reeks telt weken op rij waarin je je weekdoel
    // haalde (standaard 3 sessies, instelbaar 2 tot 7). Wie ma, wo, vr ademt breekt zo nooit zijn reeks.
    // Dag 0 (1 jan 1970) was een donderdag, dus (dag + 3) / 7 begint elke week op maandag.
    function weekVan(dag as Number) as Number {
        return (dag + 3) / 7;
    }

    function weekdoel() as Number {
        return EbbInstellingen.waarde(EbbInstellingen.WEEKDOEL);
    }

    // Na een sessie in week: [reeks, sessies deze week]. Een nieuwe week houdt de reeks alleen als de vorige week
    // direct ervoor zat en het doel haalde. Bij het halen van het doel komt er een week bij.
    function volgendeWeekReeks(vorigeWeek as Number, weekSes as Number, reeks as Number, week as Number, doel as Number, telt as Boolean) as Array<Number> {
        var r = weekStap(vorigeWeek, weekSes, weekSes >= doel, reeks, week, doel, telt);
        return [r[0], r[1]] as Array<Number>;
    }

    // Keuring bouw 3 punt 10: met de vlag "week gehaald" telt een week één keer, ook als je het weekdoel midden in
    // de week wisselt (van 3 naar 4 na 3 sessies gaf eerst een tweede week; van 4 naar 2 na 3 sessies gaf er geen).
    // Geeft [reeks, sessies deze week, gehaald (1 of 0)].
    function weekStap(vorigeWeek as Number, weekSes as Number, gehaald as Boolean, reeks as Number, week as Number, doel as Number, telt as Boolean) as Array<Number> {
        if (week != vorigeWeek) {
            if (!(week == vorigeWeek + 1 && gehaald)) {
                reeks = 0;
            }
            weekSes = 0;
            gehaald = false;
        }
        if (telt) {
            weekSes += 1;
        }
        if (weekSes >= doel && !gehaald) {
            reeks += 1;
            gehaald = true;
        }
        return [reeks, weekSes, gehaald ? 1 : 0] as Array<Number>;
    }

    // Sessies die deze week al tellen (voor "2 of 3 this week").
    function dezeWeek(vandaag as Number) as Number {
        return (weekVan(vandaag) == getal(WEEK)) ? getal(WEEKSES) : 0;
    }

    function getal(sleutel as String) as Number {
        var v = Application.Storage.getValue(sleutel);
        return (v instanceof Number) ? v as Number : 0;
    }

    // Eerste sessie na 7 of meer hele dagen zonder: tussen de vorige sessiedag en vandaag liggen minstens 7 dagen.
    function terugNaPauze(vorigeDag as Number, sessiesTot as Number, dag as Number) as Boolean {
        return sessiesTot > 0 && dag - vorigeDag - 1 >= PAUZE_DAGEN;
    }

    function sessieDagen() as Array<Number> {
        var v = Application.Storage.getValue(SESDAGEN);
        return (v instanceof Array) ? v as Array<Number> : [] as Array<Number>;
    }

    // Een sessie op dag erbij; alles ouder dan 56 dagen eruit, en nooit meer dan 400 regels (geheugen).
    function bewaarSessieDag(dag as Number) as Void {
        var oud = sessieDagen();
        var nieuw = [] as Array<Number>;
        for (var i = 0; i < oud.size(); i += 1) {
            if (oud[i] > dag - EbbOpslag.DAGEN && oud[i] <= dag) {
                nieuw.add(oud[i]);
            }
        }
        nieuw.add(dag);
        if (nieuw.size() > 400) {
            nieuw = nieuw.slice(nieuw.size() - 400, null);
        }
        Application.Storage.setValue(SESDAGEN, nieuw as Array<Application.Storage.ValueType>);
    }

    // Na opslaan: tellers bijwerken. Geeft [sessies, reeks, beste reeks, terug na pauze (1 of 0)].
    function naSessie(dag as Number) as Array<Number> {
        var pauze = terugNaPauze(getal(DAG), getal(SESSIES), dag);
        if (pauze) {
            Application.Storage.setValue(PAUZE, 1);
        }
        bewaarSessieDag(dag);
        var vandaagAl = (dag == getal(DAG) && getal(SESSIES) > 0) ? getal(DAGSES) : 0;
        var telt = vandaagAl < MAX_PER_DAG;
        var sessies = getal(SESSIES) + (telt ? 1 : 0);
        Application.Storage.setValue(DAGSES, vandaagAl + 1);
        werkOpslagBij();
        var wr = weekStap(getal(WEEK), getal(WEEKSES), getal(WEEKGEH) == 1, getal(REEKS), weekVan(dag), weekdoel(), telt);
        var reeks = wr[0];
        Application.Storage.setValue(WEEK, weekVan(dag));
        Application.Storage.setValue(WEEKSES, wr[1]);
        Application.Storage.setValue(WEEKGEH, wr[2]);
        var beste = getal(BESTE);
        if (reeks > beste) {
            beste = reeks;
        }
        Application.Storage.setValue(SESSIES, sessies);
        Application.Storage.setValue(DAG, dag);
        Application.Storage.setValue(REEKS, reeks);
        Application.Storage.setValue(BESTE, beste);
        return [sessies, reeks, beste, getal(PAUZE)] as Array<Number>;
    }

    // Besluit hoofdchat 11 nov 04:30 (besluit 3): een sessie telt pas mee met minstens 1 inhoud, of bij Calm 1 minuut.
    const CALM_MIN_MS = 60000;
    function telt(inhouden as Number, calmMs as Number) as Boolean {
        return inhouden >= 1 || calmMs >= CALM_MIN_MS;
    }

    // De tellers zonder nieuwe sessie (voor een eindscherm van een sessie die niet meetelt).
    function stand(dag as Number) as Array<Number> {
        return [getal(SESSIES), reeksOp(dag), getal(BESTE), getal(PAUZE)] as Array<Number>;
    }

    // De reeks in weken zoals die vandaag telt: in dezelfde week, of de week erna als de vorige week het doel haalde.
    function reeksOp(vandaag as Number) as Number {
        var w = weekVan(vandaag);
        var vorige = getal(WEEK);
        if (w == vorige || (w == vorige + 1 && getal(WEEKGEH) == 1)) {
            return getal(REEKS);
        }
        return 0;
    }
}
