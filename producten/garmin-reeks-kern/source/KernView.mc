import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

class KernView extends WatchUi.WatchFace {
    var bb as Array<Number> = [] as Array<Number>;
    var st as Array<Number> = [] as Array<Number>;
    var weer as Number = -2;
    var gelezen as Boolean = false;
    var tik as Number = 0;

    function initialize() {
        WatchFace.initialize();
    }

    function leesAlles() as Void {
        bb = Lees.hist(0) as Array<Number>;
        st = Lees.hist(1) as Array<Number>;
        weer = Lees.weerUren() as Number;
        var stats = System.getSystemStats();
        System.println("KERN WEER uren=" + weer + " COMPLICATIES=" + ((Toybox has :Complications) ? "ja" : "nee"));
        System.println("KERN GEHEUGEN gebruikt=" + stats.usedMemory + " totaal=" + stats.totalMemory + " vrij=" + stats.freeMemory);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        if (!gelezen) {
            gelezen = true;
            leesAlles();
        }
        var t0 = System.getTimer();
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var klok = System.getClockTime();
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, h * 10 / 100, Graphics.FONT_NUMBER_MEDIUM,
            klok.hour.format("%02d") + ":" + klok.min.format("%02d"), Graphics.TEXT_JUSTIFY_CENTER);
        var x0 = w * 14 / 100;
        var x1 = w * 86 / 100;
        var heuvel = Teken.profiel(bb, x0, x1, h * 72 / 100, h * 44 / 100, 40);
        if (heuvel.size() >= 3) {
            dc.setColor(0x00AAFF, Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon(heuvel);
        }
        var stress = Teken.profiel(st, x0, x1, h * 72 / 100, h * 58 / 100, 40);
        if (stress.size() >= 3) {
            dc.setColor(0xFF5500, Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon(stress);
        }
        dc.setColor(0x00FFAA, Graphics.COLOR_TRANSPARENT);
        dc.fillPolygon(Teken.golf(x0, x1, h * 74 / 100, h * 80 / 100, tik, 24));
        var ms = System.getTimer() - t0;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, h * 81 / 100, Graphics.FONT_XTINY,
            "BB" + bb.size() + " ST" + st.size() + " W" + weer + " " + ms + "ms", Graphics.TEXT_JUSTIFY_CENTER);
        if (tik < 4) {
            System.println("KERN TEKEN tik=" + tik + " ms=" + ms);
        }
        tik++;
    }
}
