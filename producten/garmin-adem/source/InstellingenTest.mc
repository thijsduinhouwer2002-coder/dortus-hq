import Toybox.Lang;
import Toybox.Test;

// Instellingen: standaard volgens het ontwerp, stap verder, rond na de grootste, onthouden, sessie gebruikt ze.
(:test)
function testInstellingen(logger as Test.Logger) as Boolean {
    EbbInstellingen.wis();
    var standaard = EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) == 30 && EbbInstellingen.waarde(EbbInstellingen.TEMPO) == 15 && EbbInstellingen.tempoMs() == 2000
        && EbbInstellingen.waarde(EbbInstellingen.RONDES) == 3 && EbbInstellingen.waarde(EbbInstellingen.HERSTEL) == 15
        && EbbInstellingen.trillen();
    for (var i = 0; i < 3; i += 1) {
        EbbInstellingen.volgende(EbbInstellingen.RONDES);
    }
    var zes = EbbInstellingen.waarde(EbbInstellingen.RONDES);
    var rond = EbbInstellingen.volgende(EbbInstellingen.RONDES);
    EbbInstellingen.volgende(EbbInstellingen.TEMPO);
    var s = EbbInstellingen.rondes(0);
    var tekst = EbbInstellingen.tekst(EbbInstellingen.TEMPO);
    EbbInstellingen.zetTrillen(false);
    var uit = !EbbInstellingen.trillen() && !EbbTrillen.aan;
    EbbInstellingen.zetTrillen(true);
    var eigen = EbbInstellingen.eigenPatroon();
    logger.debug("zes " + zes + " rond " + rond + " tempo " + tekst + " eigen " + eigen);
    EbbInstellingen.wis();
    return standaard && zes == 6 && rond == 1 && s.rondes == 1 && s.tempoMs == 1875 && s.herstelMs == 15000
        && tekst.equals("16 per min") && uit && eigen[0] == 4000 && eigen[1] == 4000 && eigen[2] == 6000 && eigen[3] == 2000;
}

(:test)
function testTik30(logger as Test.Logger) as Boolean {
    EbbInstellingen.wis();
    var standaard = EbbInstellingen.tik30();
    EbbInstellingen.zetTik30(false);
    var uit = !EbbInstellingen.tik30();
    EbbInstellingen.wis();
    var laatste = EbbInstellingen.laatste3();
    EbbInstellingen.zetLaatste3(false);
    var laatsteUit = !EbbInstellingen.laatste3();
    EbbInstellingen.wis();
    return standaard && uit && EbbInstellingen.tik30() && laatste && laatsteUit && EbbInstellingen.laatste3();
}
