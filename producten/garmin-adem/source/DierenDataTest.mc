import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Test;

// Mila's 24 dieren plus bonus als data (v8 json via bron/maak_dieren_json.py): elk dier leest precies tot het eind van zijn bytes,
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
            if (n < 3 || n > 60 || b[o] > 10 || b[o] == 6) {
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

// Keuring bouw 2 punt 2: de echte sea log (DierenView.onUpdate) op 260 en 454 px, met alle dieren gevonden en met
// niets gevonden, blad 1 en blad 3 (walvis, dier 24). Per beurt hoogstens 3 nieuwe plaatjes, dus vijf beurten tekenen
// alles; daarna moet elk dier klaar staan. Het inhoudscherm tekent dier 4 en 24 groot via dezelfde plaatjes.
// De watchdog zelf telt in de toets niet; die vangt de plaatjesrun (stap "Geen crash").
(:test)
function testSeaLogEcht(logger as Test.Logger) as Boolean {
    var goed = true;
    var maten = [260, 454] as Array<Number>;
    for (var m = 0; m < 2; m += 1) {
        var d = maten[m];
        var bmp = Graphics.createBufferedBitmap({:width => d, :height => d, :palette => EbbDierData.palet()}).get() as Graphics.BufferedBitmap;
        var dc = bmp.getDc();
        for (var alles = 0; alles < 2; alles += 1) {
            EbbTrouw.wis();
            if (alles == 1) {
                Application.Storage.setValue(EbbTrouw.BITS, (1 << 25) - 1);
            }
            var view = new DierenView();
            var bladen = [0, 18] as Array<Number>;
            for (var b = 0; b < 2; b += 1) {
                view.keuze = bladen[b];
                var t0 = System.getTimer();
                for (var beurt = 0; beurt < 5; beurt += 1) {
                    view.onUpdate(dc);
                }
                var maat = (d * 0.078).toNumber();
                var eerste = (bladen[b] / 9) * 9;
                for (var k = 0; k < 9 && eerste + k < 25; k += 1) {
                    var i = eerste + k;
                    if (!EbbDierData.klaar(i, maat, EbbTrouw.heeft(i) ? 0 : 1)) {
                        logger.debug("niet klaar " + d + " dier " + i);
                        goed = false;
                    }
                }
                System.println("SEALOG " + d + " px, alles " + alles + ", blad " + b + ": " + (System.getTimer() - t0) + " ms");
            }
        }
        EbbDierData.teken(dc, 4, d / 2, d / 2, (d * 0.15).toNumber(), -1);
        EbbDierData.teken(dc, 24, d / 2, d / 2, (d * 0.15).toNumber(), -1);
        goed = goed && EbbDierData.klaar(4, (d * 0.15).toNumber(), 0) && EbbDierData.klaar(24, (d * 0.15).toNumber(), 0);
    }
    EbbTrouw.wis();
    return goed;
}
