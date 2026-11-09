import Toybox.Lang;
import Toybox.Test;

(:test)
function testFractieBegintLeeg(logger as Test.Logger) as Boolean {
    return Adem.fractie(0, 4000, 4000, 4000, 4000) == 0.0;
}

(:test)
function testFractieHalverwegeIn(logger as Test.Logger) as Boolean {
    var f = Adem.fractie(2000, 4000, 4000, 4000, 4000);
    logger.debug("halverwege in: " + f);
    return (f - 0.5).abs() < 0.01;
}

(:test)
function testFractieVolTijdensVast(logger as Test.Logger) as Boolean {
    return Adem.fractie(5000, 4000, 4000, 4000, 4000) == 1.0;
}

(:test)
function testFaseNamen(logger as Test.Logger) as Boolean {
    return Adem.fase(100, 4000, 4000, 4000, 4000).equals("in")
        && Adem.fase(4100, 4000, 4000, 4000, 4000).equals("vast")
        && Adem.fase(8100, 4000, 4000, 4000, 4000).equals("uit")
        && Adem.fase(12100, 4000, 4000, 4000, 4000).equals("leeg")
        && Adem.fase(16100, 4000, 4000, 4000, 4000).equals("in");
}
