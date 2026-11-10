import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Logboek van de dieren (ontwerp: de eerste keer gezien wordt bewaard). Gezien in koraal met de tijd
// waarop ze komen; nog niet gezien als een stip met alleen de tijd, zodat je weet waar je naartoe werkt.
class DierenView extends WatchUi.View {
    function initialize() {
        View.initialize();
    }

    static const TIJDEN = ["1:00", "1:30", "2:00", "3:00"] as Array<String>;

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.12).toNumber(), Graphics.FONT_XTINY, "met so far", Graphics.TEXT_JUSTIFY_CENTER);
        var bits = EbbProfiel.dierenGezien();
        for (var i = 0; i < 4; i += 1) {
            var y = (d * (0.30 + 0.15 * i)).toNumber();
            var x = (d * 0.40).toNumber();
            if ((bits & (1 << i)) != 0) {
                EbbTeken.dierKlein(dc, d, i, x, y);
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            } else {
                dc.setColor(EbbTeken.DIEPTE[2], Graphics.COLOR_TRANSPARENT);
                dc.fillCircle(x, y, (d * 0.02).toNumber());
                dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
            }
            dc.drawText((d * 0.56).toNumber(), y, Graphics.FONT_XTINY, TIJDEN[i], Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        }
    }
}
