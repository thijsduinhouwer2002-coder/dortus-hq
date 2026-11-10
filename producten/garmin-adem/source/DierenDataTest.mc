import Toybox.Lang;
import Toybox.Test;

// Mila's 24 dieren als data (bron/maak_dieren_data.py): elk dier leest precies tot het eind van zijn bytes,
// elke veelhoek heeft 3 tot 60 punten (fillPolygon kan er 64), namen gelijk aan de lijst voor trouw.
(:test)
function testDierenData(logger as Test.Logger) as Boolean {
    if (EbbDierData.DATA.size() != 24 || EbbTrouw.DIEREN.size() != 24) {
        return false;
    }
    for (var i = 0; i < 24; i += 1) {
        var b = EbbDierData.DATA[i];
        var o = 1;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var n = b[o + 1];
            if (n < 3 || n > 60 || b[o] > 3) {
                logger.debug("dier " + i + " deel " + deel + " punten " + n);
                return false;
            }
            o += 2 + 2 * n;
        }
        var ogen = b[o];
        if (o + 1 + 2 * ogen != b.size() || ogen > 2) {
            logger.debug("dier " + i + " leest niet tot het eind");
            return false;
        }
        if (!(EbbDierData.NAMEN[i] as String).equals(EbbTrouw.DIEREN[i][0] as String)) {
            logger.debug("naam " + i + " " + EbbDierData.NAMEN[i]);
            return false;
        }
    }
    var t = EbbDierData.telling(23);
    logger.debug("walvis " + t);
    return t[0] == 5 && t[2] == 1;
}
