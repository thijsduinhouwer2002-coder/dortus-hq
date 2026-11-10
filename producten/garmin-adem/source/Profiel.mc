import Toybox.Application;
import Toybox.Lang;

// Eis 7 en 8: rekenwerk voor duikprofiel, getijdenlijn, record en dieren, los van het tekenen zodat het te toetsen is.
module EbbProfiel {
    // Duikprofiel: per ronde een V. Geeft punten [x, y]: begin aan de oppervlakte, diepste punt in het midden
    // van de ronde op diepte evenredig met de inhoudtijd (langste ronde is de volle hoogte), weer naar boven.
    function vPunten(tijden as Array<Number>, x0 as Number, y0 as Number, w as Number, h as Number) as Array<Array<Number> > {
        var punten = [[x0, y0]] as Array<Array<Number> >;
        var n = tijden.size();
        if (n == 0) {
            return punten;
        }
        var max = tijden[diepste(tijden)];
        for (var i = 0; i < n; i += 1) {
            var diep = (max > 0) ? (h * tijden[i]) / max : 0;
            punten.add([x0 + (w * (2 * i + 1)) / (2 * n), y0 + diep]);
            punten.add([x0 + (w * (i + 1)) / n, y0]);
        }
        return punten;
    }

    // Index van de langste inhoudtijd (bij gelijk de eerste); daar komt het lichtpuntje.
    function diepste(tijden as Array<Number>) as Number {
        var beste = 0;
        for (var i = 1; i < tijden.size(); i += 1) {
            if (tijden[i] > tijden[beste]) {
                beste = i;
            }
        }
        return beste;
    }

    // Gemiddelde van de daggemiddelden over de getijdenlijn (s), 0 zonder dagen. Vervangt "best" (keuring G1).
    function gemiddeldeLijn(lijn as Array<Array<Number> or Null>) as Number {
        var som = 0;
        var n = 0;
        for (var i = 0; i < lijn.size(); i += 1) {
            var g = lijn[i];
            if (g != null) {
                som += g[1];
                n += 1;
            }
        }
        return (n > 0) ? (som + n / 2) / n : 0;
    }

    // Getijdenlijn: 56 dagen, oudste eerst, eindigend op vandaag. Per dag [beste, gemiddelde] of null (gat).
    function getijden(opslag as EbbOpslag, vandaag as Number) as Array<Array<Number> or Null> {
        var lijn = [] as Array<Array<Number> or Null>;
        for (var d = vandaag - EbbOpslag.DAGEN + 1; d <= vandaag; d += 1) {
            var g = opslag.dag(d);
            lijn.add(g == null ? null : [g[0], g[1]] as Array<Number>);
        }
        return lijn;
    }

    // 8 weeks (besluit 22:53, punt 6, blad v4.1 scherm 7): per week, oudste eerst, eindigend met de week tot en met
    // vandaag, [gemiddelde inhoudtijd in s over alle inhoudingen, aantal opgeslagen sessies, aantal inhoudingen].
    // sessieDagen is de lijst dagnummers met één regel per opgeslagen sessie (EbbTrouw.sessieDagen()).
    // Een lege week is [0, 0, 0].
    function weken(opslag as EbbOpslag, sessieDagen as Array<Number>, vandaag as Number) as Array<Array<Number> > {
        var uit = [] as Array<Array<Number> >;
        for (var w = 7; w >= 0; w -= 1) {
            var van = vandaag - w * 7 - 6;
            var tot = vandaag - w * 7;
            var som = 0;
            var n = 0;
            for (var d = van; d <= tot; d += 1) {
                var g = opslag.dag(d);
                if (g != null) {
                    som += g[1] * g[2];
                    n += g[2];
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

    // Scherm 5 (getijdenlijn per week): per dag [x, y beste, y gemiddelde] of null bij een gat.
    // De hoogste beste tijd van de 56 dagen is de volle hoogte h; y0 is de bodem, hoger water is een kleinere y.
    function getijPunten(lijn as Array<Array<Number> or Null>, x0 as Number, y0 as Number, w as Number, h as Number) as Array<Array<Number> or Null> {
        var max = 0;
        for (var i = 0; i < lijn.size(); i += 1) {
            var g = lijn[i];
            if (g != null && g[0] > max) {
                max = g[0];
            }
        }
        var uit = [] as Array<Array<Number> or Null>;
        var n = lijn.size();
        for (var i = 0; i < n; i += 1) {
            var g = lijn[i];
            if (g == null || max == 0) {
                uit.add(null);
            } else {
                var x = (n > 1) ? x0 + (w * i) / (n - 1) : x0;
                uit.add([x, y0 - (h * g[0]) / max, y0 - (h * g[1]) / max] as Array<Number>);
            }
        }
        return uit;
    }

    // Index van de dag met de hoogste beste tijd (de laatste bij gelijk, zodat een nieuw record rechts staat), of -1.
    function hoogsteDag(lijn as Array<Array<Number> or Null>) as Number {
        var j = -1;
        for (var i = 0; i < lijn.size(); i += 1) {
            var g = lijn[i];
            if (g != null && (j < 0 || g[0] >= (lijn[j] as Array<Number>)[0])) {
                j = i;
            }
        }
        return j;
    }

    // Besluit 22:53: geen dieren meer op inhoudtijd. Tijdens het inhouden zwemt je gezelschap (een dier dat je al hebt)
    // rustig voorbij in een vaste cyclus van 20 s: 16 s in beeld, 4 s weg. Hoe lang je inhoudt verandert er niets aan.
    const CYCLUS_MS = 20000;
    const IN_BEELD_MS = 16000;

    // Plek van het dier in de cyclus, 0.0 (rechts erin) tot 1.0 (links eruit), of -1.0 als het even weg is.
    // Blad v5 (Mila T2): de zee wordt elke 30 s inhouden een stand donkerder (0 tot 5); vanaf 3:00 terug naar
    // stand 4, iets lichter, zodat het water nooit aanmoedigt om langer te gaan.
    function zeeStand(sec as Number) as Number {
        if (sec >= 180) {
            return 4;
        }
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

    function zwem(ms as Number) as Float {
        var p = ms % CYCLUS_MS;
        if (p >= IN_BEELD_MS) {
            return -1.0;
        }
        return p.toFloat() / IN_BEELD_MS;
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

    // Nieuwe reeks na een sessie op dag, gegeven de dag en reeks van de vorige sessie.
    // Zelfde dag: gelijk. De dag erna: plus één. Later (of de klok terug): opnieuw 1.
    function volgendeReeks(vorigeDag as Number, reeks as Number, dag as Number) as Number {
        if (reeks <= 0) {
            return 1;
        }
        if (dag == vorigeDag) {
            return reeks;
        }
        if (dag == vorigeDag + 1) {
            return reeks + 1;
        }
        return 1;
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
        var sessies = getal(SESSIES) + ((vandaagAl < MAX_PER_DAG) ? 1 : 0);
        Application.Storage.setValue(DAGSES, vandaagAl + 1);
        var reeks = volgendeReeks(getal(DAG), getal(REEKS), dag);
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

    // De reeks zoals die vandaag telt: na een gemiste dag is hij voorbij (0), ook zonder nieuwe sessie.
    function reeksOp(vandaag as Number) as Number {
        var dag = getal(DAG);
        return (vandaag == dag || vandaag == dag + 1) ? getal(REEKS) : 0;
    }

    // De 24 dieren voor trouw (besluit 22:53, lijst van blad v4.1 van Mila). Per dier [naam, soort, drempel]:
    // soort 0 is aantal opgeslagen sessies, soort 1 is dagen op rij (je beste reeks telt, dus een gemiste dag pakt
    // niets af), soort 2 is "back after a break": je eerste sessie na 7 of meer dagen zonder (de zeekomkommer).
    // Na een paar maanden met ±4 sessies per week heb je de rest (de walvis bij 60 sessies, ±15 weken).
    const SOORT_SESSIES = 0;
    const SOORT_REEKS = 1;
    const SOORT_PAUZE = 2;
    const DIEREN = [
        ["Fish", 0, 1], ["Shrimp", 0, 2], ["Jellyfish", 1, 2], ["Turtle", 1, 3],
        ["Crab", 0, 5], ["Seahorse", 0, 8], ["Starfish", 1, 4], ["Clownfish", 0, 10],
        ["Pufferfish", 1, 5], ["Octopus", 0, 12], ["Squid", 1, 6], ["Ray", 0, 15],
        ["Seal", 1, 7], ["Dolphin", 0, 18], ["Swordfish", 1, 10], ["Sea otter", 0, 21],
        ["Manta", 1, 14], ["Shark", 0, 25], ["Sunfish", 0, 30], ["Orca", 1, 21],
        ["Narwhal", 0, 40], ["Giant squid", 1, 30], ["Sea cucumber", 2, 7], ["Whale", 0, 60]
    ] as Array<Array>;
    const ZEEKOMKOMMER = 22;
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
    // De zeekomkommer gaat voor, zodat hij komt op de dag dat je terug bent; verder het laagste nummer eerst.
    // Wat wacht komt bij een volgende sessie, want de tellers zakken nooit. Geeft [] of [nummer].
    function nieuweDieren(tellers as Array<Number>) as Array<Number> {
        var oud = getal(BITS);
        var klaar = verdiend(tellers[0], tellers[2], tellers.size() > 3 ? tellers[3] : 0) & ~oud;
        var nieuw = [] as Array<Number>;
        if ((klaar & (1 << ZEEKOMKOMMER)) != 0) {
            nieuw.add(ZEEKOMKOMMER);
        } else {
            for (var i = 0; i < DIEREN.size(); i += 1) {
                if ((klaar & (1 << i)) != 0) {
                    nieuw.add(i);
                    break;
                }
            }
        }
        if (nieuw.size() > 0) {
            Application.Storage.setValue(BITS, oud | (1 << nieuw[0]));
            Application.Storage.setValue(LAATST, nieuw[0]);
        }
        return nieuw;
    }

    // Hoeveel dieren er nog klaarliggen voor een volgende sessie (verdiend maar nog niet getoond).
    function wachtend() as Number {
        var klaar = verdiend(getal(SESSIES), getal(BESTE), getal(PAUZE)) & ~getal(BITS);
        var n = 0;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            if ((klaar & (1 << i)) != 0) {
                n += 1;
            }
        }
        return n;
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

    // Eerlijke tekst hoe je een dier krijgt, bijvoorbeeld "3-day streak" of "30 sessions".
    // Kort, want "3 days in a row" liep in het Sea log door de ronde rand (plaatjes run 42912712998, fenix847mm).
    function hoe(i as Number) as String {
        var r = DIEREN[i];
        var n = r[2] as Number;
        if ((r[1] as Number) == SOORT_PAUZE) {
            return "back after a break";
        }
        if ((r[1] as Number) == SOORT_REEKS) {
            return n + "-day streak";
        }
        return n == 1 ? "1 session" : n + " sessions";
    }

    // Van de vier dieren die we nu kunnen tekenen (vis, kwal, schildpad, walvis): het nummer in DIEREN.
    const GETEKEND = [0, 2, 3, 23] as Array<Number>;

    // Welk getekend dier mee zwemt tijdens het inhouden: het hoogste dat je hebt, anders de vis.
    // Het hangt niet af van hoe lang je inhoudt (geen beloning voor inhoudtijd).
    function gezelschap() as Number {
        for (var s = GETEKEND.size() - 1; s > 0; s -= 1) {
            if (heeft(GETEKEND[s])) {
                return s;
            }
        }
        return 0;
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

    function wis() as Void {
        Application.Storage.deleteValue(LAATST);
        Application.Storage.deleteValue(GEKOZEN);
        Application.Storage.deleteValue(BITS);
        Application.Storage.deleteValue(SESSIES);
        Application.Storage.deleteValue(DAG);
        Application.Storage.deleteValue(REEKS);
        Application.Storage.deleteValue(BESTE);
        Application.Storage.deleteValue(PAUZE);
        Application.Storage.deleteValue(SESDAGEN);
        Application.Storage.deleteValue(DAGSES);
    }
}
