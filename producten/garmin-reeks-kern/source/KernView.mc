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
    // Proef 2 (run 124): eigen cijferletter op twee maten, een schermvullend plaatje, de slaapstand.
    var fontK as WatchUi.FontResource? = null;
    var fontG as WatchUi.FontResource? = null;
    var achter as WatchUi.BitmapResource? = null;
    var slaap as Boolean = false;
    var start as Number = 0;

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

    // Meet wat de cijferletter en het plaatje aan geheugen kosten. Eerst de letters, het plaatje als
    // laatste: past het niet, dan staan de regels van de letters al in het log.
    function meetBeelden() as Void {
        var m0 = System.getSystemStats().usedMemory;
        fontK = WatchUi.loadResource(Rez.Fonts.CijfersKlein) as WatchUi.FontResource;
        var m1 = System.getSystemStats().usedMemory;
        fontG = WatchUi.loadResource(Rez.Fonts.CijfersGroot) as WatchUi.FontResource;
        var m2 = System.getSystemStats().usedMemory;
        System.println("KERN FONT klein=" + (m1 - m0) + " groot=" + (m2 - m1) + " gebruikt=" + m2
            + " vrij=" + System.getSystemStats().freeMemory);
        var ds = System.getDeviceSettings();
        var inbrand = (ds has :requiresBurnInProtection) ? ds.requiresBurnInProtection : false;
        System.println("KERN SCHERM " + ds.screenWidth + "x" + ds.screenHeight + " inbrand=" + inbrand
            + " pool=" + ((Graphics has :createBufferedBitmap) ? "ja" : "nee"));
        System.println("KERN PLAATJE laden, gebruikt=" + m2);
        achter = WatchUi.loadResource(Rez.Drawables.Achtergrond) as WatchUi.BitmapResource;
        var m3 = System.getSystemStats().usedMemory;
        var a = achter as WatchUi.BitmapResource;
        System.println("KERN PLAATJE bytes=" + (m3 - m2) + " maat=" + a.getWidth() + "x" + a.getHeight()
            + " gebruikt=" + m3 + " vrij=" + System.getSystemStats().freeMemory);
    }

    function onEnterSleep() as Void {
        slaap = true;
        System.println("KERN SLAAP in, tik=" + tik);
        WatchUi.requestUpdate();
    }

    function onExitSleep() as Void {
        slaap = false;
        System.println("KERN SLAAP uit, tik=" + tik);
        WatchUi.requestUpdate();
    }

    // Slaapbeeld: zwart, de tijd in de kleine cijferletter in grijs en een dunne lijn van Body Battery.
    function tekenSlaap(dc as Graphics.Dc, tekst as String) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        if (fontK != null) {
            dc.drawText(w / 2, h * 30 / 100, fontK as WatchUi.FontResource, tekst, Graphics.TEXT_JUSTIFY_CENTER);
        }
        var lijn = Teken.profiel(bb, w * 20 / 100, w * 80 / 100, h * 78 / 100, h * 64 / 100, 20);
        dc.setColor(Graphics.COLOR_DK_GRAY, Graphics.COLOR_TRANSPARENT);
        for (var i = 1; i + 2 < lijn.size(); i++) {
            dc.drawLine(lijn[i][0], lijn[i][1], lijn[i + 1][0], lijn[i + 1][1]);
        }
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        if (!gelezen) {
            gelezen = true;
            start = System.getTimer();
            leesAlles();
            meetBeelden();
        }
        var nu = System.getClockTime();
        var tekst = nu.hour.format("%02d") + ":" + nu.min.format("%02d");
        // De simulator zet de slaapstand niet vanzelf aan: na 14 s tonen we het slaapbeeld zelf.
        if (slaap || System.getTimer() - start >= 14000) {
            var ts = System.getTimer();
            tekenSlaap(dc, tekst);
            if (tik < 40) {
                System.println("KERN SLAAPBEELD tik=" + tik + " ms=" + (System.getTimer() - ts) + " echt=" + slaap);
            }
            tik++;
            return;
        }
        var t0 = System.getTimer();
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        if (achter != null) {
            dc.drawBitmap(0, 0, achter as WatchUi.BitmapResource);
        }
        var msPlaat = System.getTimer() - t0;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var f = (w >= 400) ? fontG : fontK;
        if (f != null) {
            dc.drawText(w / 2, h * 6 / 100, f as WatchUi.FontResource, tekst, Graphics.TEXT_JUSTIFY_CENTER);
        }
        var msTijd = System.getTimer() - t0 - msPlaat;
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
            System.println("KERN TEKEN tik=" + tik + " ms=" + ms + " plaatje_ms=" + msPlaat + " tijd_ms=" + msTijd);
        }
        tik++;
    }
}
