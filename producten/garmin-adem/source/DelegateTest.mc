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
