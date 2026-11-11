import Toybox.Application;
import Toybox.Lang;

// Trouw: de 24 dieren plus de bonus, wat je hebt en wie meezwemt. Tellers en reeks staan in Trouw.mc.
module EbbTrouw {
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
    const FEEST = "trFeest";     // true zodra het feestscherm sea complete één keer getoond is (keuring bouw 6 punt 2)

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
