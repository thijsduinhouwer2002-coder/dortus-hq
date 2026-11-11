import Toybox.Application;
import Toybox.Lang;

// Rekenwerk voor 8 weeks, de zee tijdens het inhouden en de dieren, los van het tekenen zodat het te toetsen is.
module EbbProfiel {

    // 8 weeks (besluit 22:53, punt 6, blad v4.1 scherm 7): per week, oudste eerst, eindigend met de week tot en met
    // vandaag, [gemiddelde inhoudtijd in s over alle inhoudingen, aantal opgeslagen sessies, aantal inhoudingen].
    // sessieDagen is de lijst dagnummers met één regel per opgeslagen sessie (EbbTrouw.sessieDagen()).
    // Een lege week is [0, 0, 0].
    function weken(opslag as EbbOpslag, sessieDagen as Array<Number>, vandaag as Number) as Array<Array<Number> > {
        var uit = [] as Array<Array<Number> >;
        // Keuring bouw 3 punt 11: weken van maandag tot zondag (dag 0 was een donderdag), de laatste is deze week.
        var zondag = vandaag - (vandaag + 3) % 7 + 6;
        for (var w = 7; w >= 0; w -= 1) {
            var tot = zondag - w * 7;
            var van = tot - 6;
            tot = tot > vandaag ? vandaag : tot;
            var som = 0;
            var n = 0;
            for (var d = van; d <= tot; d += 1) {
                var g = opslag.dag(d);
                if (g != null) {
                    som += g[0] * g[1];
                    n += g[1];
                }
            }
            var sessies = 0;
            for (var i = 0; i < sessieDagen.size(); i += 1) {
                if (sessieDagen[i] >= van && sessieDagen[i] <= tot) {
                    sessies += 1;
                }
            }
            uit.add([(n > 0) ? (som + n / 2) / n : 0, sessies, n] as Array<Number>);
        }
        return uit;
    }

    // Blad v5 (Mila T2) met het besluit van de hoofdchat (keuring v5, 11 nov 00:55): de zee wordt elke 30 s inhouden
    // een stand donkerder tot 2:30 (stand 5) en blijft daarna gelijk. Niet lichter na 3:00: dan zou de kleur een
    // verborgen doel zijn. Het seintje na 3:00 is tekst, trilteken en buzz, niet de kleur.
    function zeeStand(sec as Number) as Number {
        var s = sec / 30;
        return s > 5 ? 5 : (s < 0 ? 0 : s);
    }

    // Banden per stand (ZEE_STAND in Mila's ebb_blad_v5.py): paren [bovenkant in honderdsten van D, watertint 0 tot 3].
    const ZEE = [
        [12, 0, 19, 1, 62, 2, 90, 3],
        [12, 0, 16, 1, 50, 2, 78, 3],
        [12, 1, 40, 2, 68, 3],
        [12, 1, 26, 2, 52, 3],
        [12, 2, 40, 3],
        [12, 2, 22, 3]
    ] as Array<Array<Number> >;

    // AMOLED: bovenop de banden het hele water 10 procent donkerder per stand (in procenten helderheid).
    function amoledHelderheid(stand as Number) as Number {
        return 100 - 10 * stand;
    }

}

// Eis 2: het veiligheidsscherm komt alleen tot het bevestigd is, en weer na "opnieuw tonen" in de instellingen.
module EbbVeilig {
    const SLEUTEL = "veilig";
    const DAGEN = 30;   // productkeuring: waarschuwing bij de eerste start en daarna elke 30 dagen

    // Bewaard is het dagnummer van de laatste bevestiging. Niets (of de oude waarde true) betekent: tonen.
    function moetTonenOp(vandaag as Number) as Boolean {
        var v = Application.Storage.getValue(SLEUTEL);
        if (!(v instanceof Number)) {
            return true;
        }
        return vandaag - (v as Number) >= DAGEN || vandaag < (v as Number);
    }

    function moetTonen() as Boolean {
        return moetTonenOp(EbbView.vandaag());
    }

    function bevestigOp(vandaag as Number) as Void {
        Application.Storage.setValue(SLEUTEL, vandaag);
    }

    function bevestig() as Void {
        bevestigOp(EbbView.vandaag());
    }

    function opnieuwTonen() as Void {
        Application.Storage.deleteValue(SLEUTEL);
    }
}

// Trouw (besluit 22:53): dieren verdien je met sessies en dagen op rij, niet met inhoudtijd.
// Hier alleen de tellers; welke dieren bij welke stand horen komt uit blad v4 van Mila.
// Een opgeslagen sessie telt (rondes en rustig ademen); weggooien telt niet.
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

    // De 24 dieren voor trouw plus de bonus (besluit 22:53, lijst van blad v6 van Mila). Per dier [naam, soort, drempel]:
    // soort 0 is aantal opgeslagen sessies, soort 1 is weken op rij met je weekdoel (besluit 11 nov 04:30; je beste reeks telt, dus een gemiste week pakt
    // niets af), soort 2 is "back after a break": je eerste sessie na 7 of meer dagen zonder (de zeekomkommer).
    // Schema van blad v5.4 (eerlijk voor wie ±4 keer per week ademt; de walvis bij 50 sessies, ±3 maanden).
    const SOORT_SESSIES = 0;
    const SOORT_REEKS = 1;
    const SOORT_PAUZE = 2;
    const DIEREN = [
        ["Fish", 0, 1], ["Shrimp", 0, 2], ["Jellyfish", 1, 2], ["Turtle", 1, 3],
        ["Crab", 0, 4], ["Seahorse", 0, 6], ["Starfish", 1, 4], ["Clownfish", 0, 10],
        ["Pufferfish", 1, 5], ["Octopus", 0, 12], ["Eel", 0, 14], ["Ray", 0, 16],
        ["Seal", 1, 6], ["Dolphin", 0, 18], ["Swordfish", 0, 20], ["Sea otter", 0, 22],
        ["Manta", 1, 7], ["Shark", 0, 25], ["Sunfish", 0, 28], ["Orca", 0, 32],
        ["Narwhal", 0, 36], ["Giant squid", 0, 42], ["Lobster", 0, 46], ["Whale", 0, 50],
        ["Sea cucumber", 2, 7]
    ] as Array<Array>;
    const ZEEKOMKOMMER = 24;
    // Besluit hoofdchat 11 nov 00:55: de zeekomkommer is een bonus. Hij telt niet mee in "x of N", zodat je alle
    // gewone dieren haalt zonder ooit te stoppen. Blad v6 (keuring 01:55, punt 3): de Lobster vult nr. 23 (46 sessies), de zeekomkommer staat achteraan als 25e.
    function bonus(i as Number) as Boolean {
        return i == ZEEKOMKOMMER;
    }

    // Aantal gewone dieren (zonder bonus), voor "x of N" in de sea log.
    function totaal() as Number {
        return DIEREN.size() - 1;
    }

    // Gevonden gewone dieren (zonder bonus).
    function aantalGewoon() as Number {
        return aantal() - (heeft(ZEEKOMKOMMER) ? 1 : 0);
    }
    const LAATST = "trLaatst";   // nummer van het laatst gevonden dier
    const GEKOZEN = "trGekozen"; // dier dat je in de sea log koos ("swims with you", blad v5 8c)
    const BITS = "trDieren";

    // Welke dieren je hebt bij deze tellers: één bit per dier. pauze is 1 als je ooit terugkwam na een pauze.
    function verdiend(sessies as Number, besteReeks as Number, pauze as Number) as Number {
        var bits = 0;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            var r = DIEREN[i];
            var soort = r[1] as Number;
            var stand = (soort == SOORT_SESSIES) ? sessies : ((soort == SOORT_REEKS) ? besteReeks : pauze);
            var drempel = (soort == SOORT_PAUZE) ? 1 : (r[2] as Number);
            if (stand >= drempel) {
                bits |= (1 << i);
            }
        }
        return bits;
    }

    // Na een sessie: hoogstens één nieuw dier (blad v4.1: "hoogstens één nieuw dier per sessie, de rest wacht").
    // Bij meer kandidaten het laagste nummer eerst (blad v5.4). Wat wacht komt bij een volgende sessie,
    // want de tellers zakken nooit. Geeft [] of [nummer].
    function nieuweDieren(tellers as Array<Number>) as Array<Number> {
        var oud = getal(BITS);
        var klaar = verdiend(tellers[0], tellers[2], tellers.size() > 3 ? tellers[3] : 0) & ~oud;
        var nieuw = [] as Array<Number>;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            if ((klaar & (1 << i)) != 0) {
                nieuw.add(i);
                break;
            }
        }
        if (nieuw.size() > 0) {
            Application.Storage.setValue(BITS, oud | (1 << nieuw[0]));
            Application.Storage.setValue(LAATST, nieuw[0]);
        }
        return nieuw;
    }

    // Keuring bouw 1 punt 7 (scherm 6c): het volgende gewone dier dat je nog niet hebt, het dichtstbij eerst
    // (laagste nummer bij gelijk). Geeft [nummer, nog nodig]: sessies voor een sessiedier, dagen op rij voor een
    // reeksdier, 0 als het al verdiend is en bij de volgende sessie komt. [-1, 0] als je alle gewone dieren hebt.
    function volgende(tellers as Array<Number>) as Array<Number> {
        var beste = -1;
        var besteRest = 0;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            if (bonus(i) || heeft(i)) {
                continue;
            }
            var r = DIEREN[i];
            var stand = ((r[1] as Number) == SOORT_SESSIES) ? tellers[0] : tellers[1];
            if ((r[1] as Number) == SOORT_REEKS && tellers[2] >= (r[2] as Number)) {
                stand = tellers[2];
            }
            var rest = (r[2] as Number) - stand;
            rest = rest < 0 ? 0 : rest;
            if (beste < 0 || rest < besteRest) {
                beste = i;
                besteRest = rest;
            }
        }
        return [beste, besteRest] as Array<Number>;
    }

    function heeft(i as Number) as Boolean {
        return (getal(BITS) & (1 << i)) != 0;
    }

    function aantal() as Number {
        var n = 0;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            if (heeft(i)) {
                n += 1;
            }
        }
        return n;
    }

    // Blad v5 (T1): kies in de sea log het dier dat meezwemt; alleen een dier dat je hebt. Geeft of het lukte.
    function kies(i as Number) as Boolean {
        if (i < 0 || i >= DIEREN.size() || !heeft(i)) {
            return false;
        }
        Application.Storage.setValue(GEKOZEN, i);
        return true;
    }

    // Wie meezwemt tijdens het inhouden (nummer in DIEREN): je keuze, anders het laatst gevonden dier, anders -1.
    function meezwemmer() as Number {
        var g = Application.Storage.getValue(GEKOZEN);
        if (g instanceof Number && heeft(g as Number)) {
            return g as Number;
        }
        var l = Application.Storage.getValue(LAATST);
        if (l instanceof Number && heeft(l as Number)) {
            return l as Number;
        }
        return -1;
    }

    // Keuring bouw 1 punt 6 en Daan B3: het dier op het startscherm en tijdens het inhouden is je eigen dier
    // (keuze, anders het laatst gevonden), anders het hoogste dat je hebt (oude opslag zonder "laatst"), anders -1.
    function zwemmer() as Number {
        var m = meezwemmer();
        if (m >= 0) {
            return m;
        }
        for (var i = DIEREN.size() - 1; i >= 0; i -= 1) {
            if (heeft(i)) {
                return i;
            }
        }
        return -1;
    }

    function wis() as Void {
        Application.Storage.deleteValue(LAATST);
        Application.Storage.deleteValue(GEKOZEN);
        Application.Storage.deleteValue(BITS);
        Application.Storage.deleteValue(SESSIES);
        Application.Storage.deleteValue(DAG);
        Application.Storage.deleteValue(REEKS);
        Application.Storage.deleteValue(BESTE);
        Application.Storage.deleteValue(PAUZE);
        Application.Storage.deleteValue(WEEK);
        Application.Storage.deleteValue(WEEKSES);
        Application.Storage.deleteValue(WEEKGEH);
        Application.Storage.deleteValue(VERSIE);
        Application.Storage.deleteValue(SESDAGEN);
        Application.Storage.deleteValue(DAGSES);
    }
}
