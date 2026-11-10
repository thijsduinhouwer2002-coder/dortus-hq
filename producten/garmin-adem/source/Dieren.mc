import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Sea log: de dieren die je met trouw verdiende (besluit 22:53). Voorlopig de vier getekende dieren met eerlijk
// hoe je ze krijgt; de volledige 24 in de stijl van blad v4 volgen.
class DierenView extends WatchUi.View {
    function initialize() {
        View.initialize();
    }


    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.12).toNumber(), Graphics.FONT_XTINY, EbbTrouw.aantal() + " of " + EbbTrouw.DIEREN.size(), Graphics.TEXT_JUSTIFY_CENTER);
        for (var i = 0; i < 4; i += 1) {
            var y = (d * (0.30 + 0.15 * i)).toNumber();
            var x = (d * 0.40).toNumber();
            if (EbbTrouw.heeft(EbbTrouw.GETEKEND[i])) {
                EbbTeken.dierKlein(dc, d, i, x, y);
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            } else {
                dc.setColor(EbbTeken.DIEPTE[2], Graphics.COLOR_TRANSPARENT);
                dc.fillCircle(x, y, (d * 0.02).toNumber());
                dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
            }
            dc.drawText((d * 0.56).toNumber(), y, Graphics.FONT_XTINY, EbbTrouw.hoe(EbbTrouw.GETEKEND[i]), Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        }
    }
}
