import Toybox.Lang;
import Toybox.Test;

// Instellingen: standaard volgens het ontwerp, stap verder, rond na de grootste, onthouden, sessie gebruikt ze.
(:test)
function testInstellingen(logger as Test.Logger) as Boolean {
    EbbInstellingen.wis();
    var standaard = EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) == 30 && EbbInstellingen.waarde(EbbInstellingen.TEMPO) == 1600
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
    return standaard && zes == 6 && rond == 1 && s.rondes == 1 && s.tempoMs == 1800 && s.herstelMs == 15000
        && tekst.equals("1.8 s") && uit && eigen[0] == 4000 && eigen[1] == 4000 && eigen[2] == 6000 && eigen[3] == 2000;
}
