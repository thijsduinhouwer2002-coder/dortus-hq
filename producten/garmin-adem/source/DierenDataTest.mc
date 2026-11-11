import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Test;

// Mila's 24 dieren plus bonus als data (bron/maak_dieren_data.py): elk dier leest precies tot het eind van zijn bytes,
// elke veelhoek heeft 3 tot 60 punten (fillPolygon kan er 64), namen gelijk aan de lijst voor trouw.
(:test)
function testDierenData(logger as Test.Logger) as Boolean {
    if (EbbDierData.DATA.size() != 25 || EbbTrouw.DIEREN.size() != 25) {
        return false;
    }
    for (var i = 0; i < 25; i += 1) {
        var b = EbbDierData.DATA[i];
        var o = 1;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var n = b[o + 1];
            if (n < 3 || n > 60 || b[o] > 5) {
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
    return t[0] == 6 && t[2] == 1;   // blad v6: walvis met fontein (zesde vlak)
}

// Keuring G4: de zwaarste sea log-pagina (9 dieren, elk met lichte rand = 5 tekenbeurten per dier, plus 9 silhouetten
// met rand) in één onUpdate mag de watchdog niet raken. Deze toets draait in de e2e op fenix 7 en FR255.
(:test)
function testSeaLogWatchdog(logger as Test.Logger) as Boolean {
    var bmp = Graphics.createBufferedBitmap({:width => 260, :height => 260}).get() as Graphics.BufferedBitmap;
    var dc = bmp.getDc();
    var t0 = System.getTimer();
    // Rand om elk dier: 4 keer verschoven in de randkleur, dan het dier (ook voor dieren zonder eigen rand: zwaarste geval).
    for (var i = 0; i < 9; i += 1) {
        var x = 50 + (i % 3) * 80;
        var y = 50 + (i / 3) * 80;
        var dier = 15 + i;   // de zwaarste dieren achteraan de lijst (otter tot walvis)
        EbbDierData.vlakken(dc, dier, x - 1, y, 22, 0x0055FF);
        EbbDierData.vlakken(dc, dier, x + 1, y, 22, 0x0055FF);
        EbbDierData.vlakken(dc, dier, x, y - 1, 22, 0x0055FF);
        EbbDierData.vlakken(dc, dier, x, y + 1, 22, 0x0055FF);
        EbbDierData.teken(dc, dier, x, y, 22, -1);
    }
    var ms = System.getTimer() - t0;
    System.println("G4 SEALOG 9 dieren met rand: " + ms + " ms");
    logger.debug("G4 sea log " + ms + " ms");
    return true;
}
