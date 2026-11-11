import Toybox.Application;
import Toybox.Lang;
import Toybox.Test;

// Keuring G2: voor de dieren tellen hoogstens 2 sessies per dag; 8 weeks telt ze wel allemaal.
(:test)
function testHoogstensTweePerDag(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    var a = EbbTrouw.naSessie(200);
    var b = EbbTrouw.naSessie(200);
    var c = EbbTrouw.naSessie(200);
    var dd = EbbTrouw.naSessie(201);
    var lijst = EbbTrouw.sessieDagen().size();
    EbbTrouw.wis();
    return a[0] == 1 && b[0] == 2 && c[0] == 2 && dd[0] == 3 && lijst == 4;
}

// Getijdenlijn na 8 weken nagebootste gegevens met overgeslagen dagen: 56 dagen, gaten waar geen sessie was.
(:test)
function testGetijdenlijnAchtWeken(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    var vandaag = 20402;
    var sessies = 0;
    for (var d = vandaag - 70; d <= vandaag; d += 1) {
        if (d % 3 != 0) {
            o.voegToe(d, 60 + (d % 50));
            sessies += 1;
        }
    }
    var lijn = EbbProfiel.getijden(o, vandaag);
    var gaten = 0;
    var fout = 0;
    for (var i = 0; i < lijn.size(); i += 1) {
        var d = vandaag - 55 + i;
        var g = lijn[i];
        if (g == null) {
            gaten += 1;
            if (d % 3 != 0) { fout += 1; }
        } else if (d % 3 == 0 || g[0] != 60 + (d % 50)) {
            fout += 1;
        }
    }
    logger.debug("dagen " + lijn.size() + ", gaten " + gaten + ", fout " + fout);
    EbbOpslag.wis();
    return lijn.size() == 56 && gaten == 18 && fout == 0;
}

// Besluit 22:53: het dier tijdens het inhouden hangt niet af van de inhoudtijd; het zwemt in een vaste cyclus van 20 s.
(:test)
function testZwemZonderBeloning(logger as Test.Logger) as Boolean {
    return EbbProfiel.zwem(0) == 0.0 && EbbProfiel.zwem(8000) == 0.5 && EbbProfiel.zwem(16000) == -1.0
        && EbbProfiel.zwem(20000) == 0.0 && EbbProfiel.zwem(188000) == 0.5;
}

// Dieren voor trouw: 24 stuks, elk één keer, hoogstens één nieuw per sessie (de rest wacht), alleen bij het afsluiten
// van een sessie, beste reeks telt (blad v4.1).
(:test)
function testDierenVoorTrouw(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    var lijst = EbbTrouw.DIEREN.size() == 25 && (EbbTrouw.DIEREN[22][0] as String).equals("Lobster")
        && (EbbTrouw.DIEREN[23][0] as String).equals("Whale") && (EbbTrouw.DIEREN[24][0] as String).equals("Sea cucumber");
    var geen = EbbTrouw.aantal() == 0 && EbbTrouw.gezelschap() == 0;
    EbbInstellingen.wis();
    var eerste = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(95));         // 1 sessie: vis
    var tweede = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(96));         // 2 sessies: garnaal
    var derde = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(97));          // 3 sessies, 1 week: niets (kwal wil 2 weken)
    var vier = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(98));           // 4 sessies: krab
    var vijf = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(102));          // week 15, 5 sessies: niets
    var zesS = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(103));          // 6 sessies: zeepaardje
    var kwal = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(104));          // doel week 15: 2 weken op rij, kwal
    var na = EbbTrouw.aantal() == 5;
    // Na 6 dagen zonder geen zeekomkommer; na 7 dagen zonder wel.
    var zes = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(111));           // dag 105 t/m 110 zonder: 6 dagen
    var zeven = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(119));         // dag 112 t/m 118 zonder: 7 dagen
    var gehouden = EbbTrouw.aantal() == 6 && EbbTrouw.aantalGewoon() == 5 && EbbTrouw.totaal() == 24
        && EbbTrouw.bonus(24) && !EbbTrouw.bonus(23) && !EbbTrouw.bonus(22);
    var alles = EbbTrouw.verdiend(50, 7, 1) == (1 << 25) - 1 && EbbTrouw.verdiend(50, 7, 0) != (1 << 25) - 1
        && EbbTrouw.verdiend(49, 7, 1) != (1 << 25) - 1 && EbbTrouw.verdiend(50, 6, 1) != (1 << 25) - 1;
    var tekst = EbbTrouw.hoe(3).equals("3-week streak") && EbbTrouw.hoe(23).equals("50 sessions")
        && EbbTrouw.hoe(0).equals("1 session") && EbbTrouw.hoe(24).equals("bonus") && EbbTrouw.hoe(22).equals("46 sessions");
    logger.debug("eerste " + eerste + " tweede " + tweede + " derde " + derde + " vier " + vier + " zesS " + zesS + " kwal " + kwal + " zes " + zes + " zeven " + zeven);
    EbbTrouw.wis();
    return lijst && geen && eerste.size() == 1 && eerste[0] == 0 && tweede.size() == 1 && tweede[0] == 1
        && derde.size() == 0 && vier.size() == 1 && vier[0] == 4 && vijf.size() == 0 && zesS.size() == 1 && zesS[0] == 5
        && kwal.size() == 1 && kwal[0] == 2 && na && zes.size() == 0 && zeven.size() == 1 && zeven[0] == 24
        && gehouden && alles && tekst;
}

// Eis 2: na bevestigen nooit meer, behalve na "opnieuw tonen".
(:test)
function testVeiligheidsschermEenKeer(logger as Test.Logger) as Boolean {
    EbbVeilig.opnieuwTonen();
    var begin = EbbVeilig.moetTonen();
    EbbVeilig.bevestig();
    var na = EbbVeilig.moetTonen();
    var nogmaals = EbbVeilig.moetTonen();
    EbbVeilig.opnieuwTonen();
    var weer = EbbVeilig.moetTonen();
    EbbVeilig.opnieuwTonen();
    return begin && !na && !nogmaals && weer;
}

// Besluit 22:53 punt 6 en blad v4.1: 8 weeks toont gemiddelde inhoudtijd en sessies per week.
(:test)
function testWekenGemiddeldeEnSessies(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    var vandaag = 20402;
    // Deze week: drie dagen, elk twee inhoudingen van 60 en 90 s (gemiddeld 75); vier sessies (één dag twee keer).
    for (var d = vandaag - 2; d <= vandaag; d += 1) {
        o.voegToe(d, 60);
        o.voegToe(d, 90);
    }
    // Vorige week: één dag met één inhouding van 100 s. Week 3 terug leeg. Oudste dag van week 1 telt mee.
    // (Niet ouder dan 56 dagen proberen: die plek in de ring is van een nieuwere dag.)
    o.voegToe(vandaag - 7, 100);
    o.voegToe(vandaag - 55, 200);
    var sd = [vandaag - 55, vandaag - 7, vandaag - 2, vandaag - 1, vandaag, vandaag, vandaag - 60] as Array<Number>;
    var w = EbbProfiel.weken(o, sd, vandaag);
    logger.debug("weken " + w);
    EbbOpslag.wis();
    // Sessiedagen bewaren: ouder dan 56 dagen valt eruit.
    EbbTrouw.wis();
    EbbTrouw.bewaarSessieDag(100);
    EbbTrouw.bewaarSessieDag(120);
    EbbTrouw.bewaarSessieDag(160);
    var bewaard = EbbTrouw.sessieDagen();
    EbbTrouw.wis();
    return w.size() == 8
        && w[7][0] == 75 && w[7][1] == 4 && w[7][2] == 6
        && w[6][0] == 100 && w[6][1] == 1 && w[6][2] == 1
        && w[5][0] == 0 && w[5][1] == 0 && w[0][0] == 200 && w[0][1] == 1 && w[0][2] == 1
        && bewaard.size() == 2 && bewaard[0] == 120 && bewaard[1] == 160;
}

// Productkeuring: veiligheidsscherm bij de eerste start en daarna elke 30 dagen opnieuw.
(:test)
function testVeiligElkeDertigDagen(logger as Test.Logger) as Boolean {
    EbbVeilig.opnieuwTonen();
    var eerste = EbbVeilig.moetTonenOp(20400);
    EbbVeilig.bevestigOp(20400);
    var dag29 = EbbVeilig.moetTonenOp(20429);
    var dag30 = EbbVeilig.moetTonenOp(20430);
    var klokTerug = EbbVeilig.moetTonenOp(20390);
    Application.Storage.setValue(EbbVeilig.SLEUTEL, true);
    var oudeWaarde = EbbVeilig.moetTonenOp(20400);
    EbbVeilig.opnieuwTonen();
    return eerste && !dag29 && dag30 && klokTerug && oudeWaarde;
}

// Trouw (besluit 11 nov 04:30): de reeks telt weken op rij met het weekdoel (standaard 3). Week 14 is dag 95 tot 101
// (maandag tot zondag), week 15 dag 102 tot 108. Beste reeks blijft staan na een gemiste week.
(:test)
function testTrouwTellers(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    EbbInstellingen.wis();
    var maandag = EbbTrouw.weekVan(95) == 14 && EbbTrouw.weekVan(101) == 14 && EbbTrouw.weekVan(102) == 15;
    EbbTrouw.naSessie(95);
    var twee = EbbTrouw.naSessie(97);                 // 2 van 3: nog geen week
    var t = EbbTrouw.naSessie(100);                   // doel gehaald: 1 week
    var een = twee[1] == 0 && t[0] == 3 && t[1] == 1 && t[2] == 1 && EbbTrouw.dezeWeek(100) == 3;
    var zondag = EbbTrouw.reeksOp(101) == 1;
    var weekErna = EbbTrouw.reeksOp(108) == 1 && EbbTrouw.dezeWeek(102) == 0;   // nieuwe week, reeks loopt nog
    var voorbij = EbbTrouw.reeksOp(109) == 0;         // een hele week zonder: voorbij
    EbbTrouw.naSessie(102);
    EbbTrouw.naSessie(104);
    var w2 = EbbTrouw.naSessie(106);                  // tweede week: 2
    var gemist = EbbTrouw.naSessie(117);              // week 16 overgeslagen: opnieuw 0, beste 2
    var gat = w2[1] == 2 && gemist[1] == 0 && gemist[2] == 2;
    // Rekenregel los: week erna houdt de reeks alleen als het doel gehaald was.
    var r1 = EbbTrouw.volgendeWeekReeks(20, 3, 4, 21, 3, true);   // [4, 1]
    var r2 = EbbTrouw.volgendeWeekReeks(20, 2, 4, 21, 3, true);   // [0, 1]
    var r3 = EbbTrouw.volgendeWeekReeks(20, 1, 4, 20, 2, true);   // doel 2 gehaald: [5, 2]
    var regel = r1[0] == 4 && r1[1] == 1 && r2[0] == 0 && r3[0] == 5 && r3[1] == 2;
    logger.debug("na week 1 " + t + ", week 2 " + w2 + ", na gat " + gemist);
    EbbTrouw.wis();
    return maandag && een && zondag && weekErna && voorbij && gat && regel;
}

// Blad v5 T2 met besluit 00:55: elke 30 s een stand donkerder tot 2:30 (stand 5), daarna gelijk. Zes standen met banden.
(:test)
function testZeeStand(logger as Test.Logger) as Boolean {
    return EbbProfiel.zeeStand(0) == 0 && EbbProfiel.zeeStand(29) == 0 && EbbProfiel.zeeStand(30) == 1
        && EbbProfiel.zeeStand(105) == 3 && EbbProfiel.zeeStand(150) == 5 && EbbProfiel.zeeStand(179) == 5
        && EbbProfiel.zeeStand(180) == 5 && EbbProfiel.zeeStand(400) == 5
        && EbbProfiel.ZEE.size() == 6 && EbbProfiel.amoledHelderheid(5) == 50;
}

// Blad v5 T1: meezwemmer is je keuze, anders het laatst gevonden dier; kiezen kan alleen wat je hebt.
(:test)
function testMeezwemmer(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    var leeg = EbbTrouw.meezwemmer() == -1;
    EbbTrouw.nieuweDieren(EbbTrouw.naSessie(300));     // vis
    EbbTrouw.nieuweDieren(EbbTrouw.naSessie(301));     // garnaal
    var laatst = EbbTrouw.meezwemmer() == 1;
    var nietGehad = !EbbTrouw.kies(23);
    var wel = EbbTrouw.kies(0);
    var gekozen = EbbTrouw.meezwemmer() == 0;
    EbbTrouw.nieuweDieren(EbbTrouw.naSessie(301));     // kwal: keuze blijft
    var blijft = EbbTrouw.meezwemmer() == 0;
    EbbTrouw.wis();
    return leeg && laatst && nietGehad && wel && gekozen && blijft;
}

// Keuring bouw 1 punt 7 (scherm 6c): het volgende dier is het dichtstbij, met wat er nog nodig is.
(:test)
function testVolgendDier(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    var leeg = EbbTrouw.volgende([0, 0, 0, 0] as Array<Number>);       // niets: vis, nog 1 sessie
    EbbTrouw.nieuweDieren(EbbTrouw.naSessie(400));                    // vis
    var na1 = EbbTrouw.volgende([1, 1, 1, 0] as Array<Number>);        // garnaal en kwal beide nog 1: laagste nummer
    var klaar = EbbTrouw.volgende([9, 1, 9, 0] as Array<Number>);      // 9 sessies: garnaal ligt klaar (0)
    var reeks = EbbTrouw.volgende([1, 1, 3, 0] as Array<Number>);      // beste reeks 3: kwal verdiend, ligt klaar
    logger.debug("leeg " + leeg + " na1 " + na1 + " klaar " + klaar + " reeks " + reeks);
    EbbTrouw.wis();
    return leeg[0] == 0 && leeg[1] == 1 && na1[0] == 1 && na1[1] == 1 && klaar[0] == 1 && klaar[1] == 0
        && reeks[0] == 2 && reeks[1] == 0;
}
