import Toybox.Lang;
import Toybox.Test;

// Eis 4: de stoptijd van het inhouden komt uit de knophandler, met nagebootste klok.
(:test)
function testInhoudenStopOpKnoptijd(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    var d = new EbbDelegate(view);
    view.sessie.bijwerken(96050);
    var inhoudStart = view.sessie.segmentStart;
    var knop = inhoudStart + 83417;
    var gestopt = d.stopOp(knop);
    var tijd = view.sessie.inhoudtijden[0];
    var afwijking = (tijd - 83417).abs();
    logger.debug("inhoudtijd " + tijd + " ms, afwijking " + afwijking + " ms");
    return gestopt && afwijking <= 100 && view.sessie.fase == Ebb.FASE_HERSTEL;
}

(:test)
function testTerugBuitenInhoudenIsPauze(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    var d = new EbbDelegate(view);
    var tijdensAdemen = d.terugActie();
    view.sessie.bijwerken(96000);
    var tijdensInhouden = d.terugActie();
    d.stopOp(120000);
    var tijdensHerstel = d.terugActie();
    return tijdensAdemen == :pauze && tijdensInhouden == :stop && tijdensHerstel == :pauze
        && !d.stopOp(121000);
}

// Eis 10 (deel in de unittest): zonder lopende opname geeft stoppen gewoon de inhoudtijd door, opslaan zonder opname geeft false.
(:test)
function testOpnameZonderSessieVeilig(logger as Test.Logger) as Boolean {
    var o = new EbbOpname();
    o.inhouden(42, 30);
    o.rondeKlaar();
    var ok = o.opslaan();
    o.weggooien();
    return !ok && !o.loopt() && o.laps == 0;
}

// Productkeuring 10 nov: aanraakscherm uit tijdens een sessie, na de sessie weer aan (wisselen vandaag en 8 weken).
(:test)
function testAanraakUitTijdensSessie(logger as Test.Logger) as Boolean {
    var view = new EbbView();
    view.sessie = new Ebb.Rondes(30, 1600, 1, 15000, 0);
    var d = new EbbDelegate(view);
    var ademen = !d.aanraakAan();
    view.sessie.bijwerken(96000);
    var inhouden = !d.aanraakAan();
    d.stopOp(120000);
    view.sessie.bijwerken(140000);
    var klaar = d.aanraakAan();
    // Tikken tijdens het inhouden stopt niet meer: alleen de knop.
    return ademen && inhouden && klaar && view.sessie.fase == Ebb.FASE_KLAAR;
}

// Blad v5.4: Connect toont "Hold times 1:20 · 1:45 · 3:04" in plaats van "Longest hold"; de tekst past altijd in het veld.
(:test)
function testTijdenTekst(logger as Test.Logger) as Boolean {
    var t = EbbOpname.tijdenTekst("", 80);
    t = EbbOpname.tijdenTekst(t, 105);
    t = EbbOpname.tijdenTekst(t, 184);
    var lang = "";
    for (var i = 0; i < 20; i += 1) {
        lang = EbbOpname.tijdenTekst(lang, 125);
    }
    logger.debug("tijden " + t + " lang " + lang);
    return t.equals("1:20 · 1:45 · 3:04") && lang.toUtf8Array().size() <= 47 && lang.length() > 0;
}
