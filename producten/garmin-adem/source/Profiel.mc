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

    // Koraal alleen bij een nieuw record over alle tijd (strikt langer dan het oude record).
    function nieuwRecord(tijden as Array<Number>, record as Number) as Boolean {
        return tijden.size() > 0 && tijden[diepste(tijden)] > record;
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

    // 8 weeks (besluit 22:53, punt 6): per week, oudste eerst, eindigend met de week tot en met vandaag,
    // [gemiddelde inhoudtijd in s over alle inhoudingen, dagen met een sessie, aantal inhoudingen].
    // Een lege week is [0, 0, 0]. Nog niet getekend: dat komt met blad v4 van Mila.
    function weken(opslag as EbbOpslag, vandaag as Number) as Array<Array<Number> > {
        var uit = [] as Array<Array<Number> >;
        for (var w = 7; w >= 0; w -= 1) {
            var som = 0;
            var n = 0;
            var dagen = 0;
            for (var d = vandaag - w * 7 - 6; d <= vandaag - w * 7; d += 1) {
                var g = opslag.dag(d);
                if (g != null) {
                    som += g[1] * g[2];
                    n += g[2];
                    dagen += 1;
                }
            }
            uit.add([(n > 0) ? (som + n / 2) / n : 0, dagen, n] as Array<Number>);
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
    function zwem(ms as Number) as Float {
        var p = ms % CYCLUS_MS;
        if (p >= IN_BEELD_MS) {
            return -1.0;
        }
        return p.toFloat() / IN_BEELD_MS;
    }

    function record() as Number {
        var r = Application.Storage.getValue("record");
        return (r instanceof Number) ? r as Number : 0;
    }

    function bewaarRecord(s as Number) as Void {
        Application.Storage.setValue("record", s);
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

    // Na opslaan: tellers bijwerken. Geeft [sessies, reeks, beste reeks].
    function naSessie(dag as Number) as Array<Number> {
        var sessies = getal(SESSIES) + 1;
        var reeks = volgendeReeks(getal(DAG), getal(REEKS), dag);
        var beste = getal(BESTE);
        if (reeks > beste) {
            beste = reeks;
        }
        Application.Storage.setValue(SESSIES, sessies);
        Application.Storage.setValue(DAG, dag);
        Application.Storage.setValue(REEKS, reeks);
        Application.Storage.setValue(BESTE, beste);
        return [sessies, reeks, beste] as Array<Number>;
    }

    // De reeks zoals die vandaag telt: na een gemiste dag is hij voorbij (0), ook zonder nieuwe sessie.
    function reeksOp(vandaag as Number) as Number {
        var dag = getal(DAG);
        return (vandaag == dag || vandaag == dag + 1) ? getal(REEKS) : 0;
    }

    // De 24 dieren voor trouw (besluit 22:53). Per dier [naam, soort, drempel]: soort 0 is aantal opgeslagen
    // sessies, soort 1 is dagen op rij (je beste reeks telt, dus een gemiste dag pakt niets af).
    // Na een paar maanden met ±4 sessies per week heb je ze allemaal (blauwe vinvis bij 60 sessies, ±15 weken).
    // Namen en volgorde mag Mila aanpassen; de logica blijft.
    const SOORT_SESSIES = 0;
    const SOORT_REEKS = 1;
    const DIEREN = [
        ["Fish", 0, 1], ["Shrimp", 0, 2], ["Jellyfish", 1, 2], ["Turtle", 1, 3],
        ["Crab", 0, 5], ["Seahorse", 0, 8], ["Starfish", 1, 4], ["Clownfish", 0, 10],
        ["Pufferfish", 1, 5], ["Octopus", 0, 12], ["Squid", 1, 6], ["Ray", 0, 15],
        ["Seal", 1, 7], ["Dolphin", 0, 18], ["Swordfish", 1, 10], ["Sea otter", 0, 21],
        ["Manta", 1, 14], ["Shark", 0, 25], ["Sunfish", 0, 30], ["Orca", 1, 21],
        ["Narwhal", 0, 40], ["Giant squid", 1, 30], ["Sea turtle elder", 0, 50], ["Blue whale", 0, 60]
    ] as Array<Array>;
    const BITS = "trDieren";

    // Welke dieren je hebt bij deze tellers: één bit per dier.
    function verdiend(sessies as Number, besteReeks as Number) as Number {
        var bits = 0;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            var r = DIEREN[i];
            var stand = ((r[1] as Number) == SOORT_SESSIES) ? sessies : besteReeks;
            if (stand >= (r[2] as Number)) {
                bits |= (1 << i);
            }
        }
        return bits;
    }

    // Na een sessie: zet de nieuwe dieren in de opslag en geef hun nummers terug (voor het scherm aan het eind).
    function nieuweDieren(tellers as Array<Number>) as Array<Number> {
        var oud = getal(BITS);
        var nu = verdiend(tellers[0], tellers[2]) | oud;
        var nieuw = [] as Array<Number>;
        for (var i = 0; i < DIEREN.size(); i += 1) {
            if ((nu & (1 << i)) != 0 && (oud & (1 << i)) == 0) {
                nieuw.add(i);
            }
        }
        Application.Storage.setValue(BITS, nu);
        return nieuw;
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

    // Eerlijke tekst hoe je een dier krijgt, bijvoorbeeld "3 days in a row" of "30 sessions".
    function hoe(i as Number) as String {
        var r = DIEREN[i];
        var n = r[2] as Number;
        if ((r[1] as Number) == SOORT_REEKS) {
            return n + " days in a row";
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

    function wis() as Void {
        Application.Storage.deleteValue(BITS);
        Application.Storage.deleteValue(SESSIES);
        Application.Storage.deleteValue(DAG);
        Application.Storage.deleteValue(REEKS);
        Application.Storage.deleteValue(BESTE);
    }
}
