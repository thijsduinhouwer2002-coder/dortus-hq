import Toybox.Activity;
import Toybox.ActivityMonitor;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Time;
import Toybox.Time.Gregorian;
import Toybox.WatchUi;

typedef Plaatje as WatchUi.BitmapResource or Graphics.BitmapReference;

// De wijzerplaat: tijd groot links, datum erboven, stappen en hoeden eronder, hartslag en batterij klein.
// Gloop staat rechts onderin en de toren groeit langs de rechterkant omhoog (concept 1 van Mila).
class GloopFaceView extends WatchUi.WatchFace {
    // Plaatjes: 0 rust, 1 blij, 2 tot 11 de tien hoeden.
    var pl as Array<Plaatje> = [] as Array<Plaatje>;
    // Maten en ankers van de plaatjes (zie Maten.mc, uit de kit van het spel).
    var m as Array<Number> = [] as Array<Number>;
    var slaap as Boolean = false;
    var gemeld as Boolean = false;
    // Volgorde van de gewone hoeden in de toren. De kroon (hoed 4) komt alleen bij het stapdoel.
    const VOLGORDE = [1, 9, 5, 2, 0, 6, 7, 3, 8] as Array<Number>;
    const KROON = 4;
    // Standen voor de bouwstraat (Bouw.AUTO): stappen per stand; de laatste stand is de slaapstand.
    const PROEF = [0, 3420, 7612, 10230, 14800, 7612] as Array<Number>;

    function initialize() {
        WatchFace.initialize();
    }

    function onLayout(dc as Graphics.Dc) as Void {
        m = Maten.voor(dc.getWidth());
        pl = [
            WatchUi.loadResource(Rez.Drawables.GloopRust) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.GloopBlij) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed0) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed1) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed2) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed3) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed4) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed5) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed6) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed7) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed8) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed9) as Plaatje
        ] as Array<Plaatje>;
    }

    function onEnterSleep() as Void {
        slaap = true;
        WatchUi.requestUpdate();
    }

    function onExitSleep() as Void {
        slaap = false;
        WatchUi.requestUpdate();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var stappen = 0;
        var doel = 10000;
        var info = ActivityMonitor.getInfo();
        if (info.steps != null) {
            stappen = info.steps as Number;
        }
        if (info.stepGoal != null) {
            doel = info.stepGoal as Number;
        }
        var slaapt = slaap;
        if (Bouw.AUTO) {
            var stand = (System.getTimer() / 3000) % 6;
            stappen = PROEF[stand];
            doel = 10000;
            slaapt = (stand == 5);
        }
        var amoled = (w >= 320);
        var klok = System.getClockTime();
        var is24 = System.getDeviceSettings().is24Hour;
        var tijd = Regel.uur(klok.hour, is24).format(is24 ? "%02d" : "%d") + ":" + klok.min.format("%02d");

        if (slaapt && amoled) {
            tekenSlaap(dc, w, h, tijd, klok.min);
        } else {
            tekenVol(dc, w, h, tijd, stappen, doel, amoled);
        }
        if (!gemeld) {
            gemeld = true;
            var st = System.getSystemStats();
            System.println("GEHEUGEN " + w + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " vrij " + st.freeMemory);
        }
    }

    // Grootste cijferfont waarbij de tijd links van de toren past.
    function tijdFont(dc as Graphics.Dc, tijd as String, ruimte as Number) as Graphics.FontDefinition {
        var fonts = [Graphics.FONT_NUMBER_THAI_HOT, Graphics.FONT_NUMBER_HOT, Graphics.FONT_NUMBER_MEDIUM, Graphics.FONT_NUMBER_MILD] as Array<Graphics.FontDefinition>;
        for (var i = 0; i < fonts.size(); i += 1) {
            if (dc.getTextWidthInPixels(tijd, fonts[i]) <= ruimte) {
                return fonts[i];
            }
        }
        return Graphics.FONT_NUMBER_MILD;
    }

    function tekenVol(dc as Graphics.Dc, w as Number, h as Number, tijd as String, stappen as Number, doel as Number, amoled as Boolean) as Void {
        var achter = amoled ? 0x000000 : 0xAA5500;
        dc.setColor(achter, achter);
        dc.clear();

        // Gloop en de toren, rechts.
        var n = Regel.hoeden(stappen);
        var kroon = Regel.kroon(stappen, doel);
        var gx = (w * 0.70).toNumber();
        var voet = (h * 0.86).toNumber();
        dc.drawBitmap(gx - m[0] / 2, voet - (kroon ? m[3] : m[1]), kroon ? pl[1] : pl[0]);
        var torenX = gx - m[0] / 2 + m[10];
        var kruinY = voet - m[1] + m[11];
        tekenToren(dc, torenX, kruinY, n, kroon, (h * 0.05).toNumber());

        // Tijd, datum, stappen en hoeden, links.
        var x0 = (w * 0.06).toNumber();
        var font = tijdFont(dc, tijd, (w * 0.54).toNumber());
        var fh = dc.getFontHeight(font);
        var ty = (h * 0.42).toNumber() - fh / 2;
        tekst(dc, x0, ty, font, tijd, 0xFFFFFF);
        var nu = Gregorian.info(Time.now(), Time.FORMAT_MEDIUM);
        var klein = Graphics.FONT_TINY;
        var kh = dc.getFontHeight(klein);
        tekst(dc, x0 + (w * 0.04).toNumber(), ty - kh + (fh * 0.10).toNumber(), klein, nu.day_of_week + " " + nu.day, 0xFFFF00);
        var sy = ty + fh - (fh * 0.08).toNumber();
        tekst(dc, x0, sy, klein, stappen.toString(), 0x55FFAA);
        // Onder de stappen: hoeveel hoeden van het doel, en na het doel "GOAL!" met het aantal.
        // Past de regel niet links van Gloop, dan een maat kleiner (Venu Sq 2).
        var vrij = gx - m[0] / 2 - x0 - 6;
        var regel = kroon ? "GOAL! " + n + " HATS" : n + "/" + Regel.hoedenBijDoel(doel) + " HATS";
        var rf = dc.getTextWidthInPixels(regel, klein) <= vrij ? klein : Graphics.FONT_XTINY;
        tekst(dc, x0, sy + kh - 2, rf, regel, kroon ? 0xFFFF00 : 0xFFFFFF);

        // Hartslag en batterij, klein linksonder.
        var hs = "--";
        var act = Activity.getActivityInfo();
        if (act != null && act.currentHeartRate != null) {
            hs = (act.currentHeartRate as Number).toString();
        }
        var bat = System.getSystemStats().battery.toNumber();
        tekst(dc, x0 + (w * 0.04).toNumber(), sy + 2 * kh - 4, Graphics.FONT_XTINY, "HR " + hs + " " + bat + "%", 0xFFAAAA);
    }

    // Stapelt n hoeden op de kruin en zet bij het doel de kroon erop. Elke hoed staat 0,56 keer zijn
    // eigen hoogte hoger (regel van Mila uit het spel); past dat niet onder de bovenrand, dan schuiven
    // de hoeden dichter in elkaar zodat de bovenste hoed altijd in beeld blijft.
    function tekenToren(dc as Graphics.Dc, torenX as Number, kruinY as Number, n as Number, kroon as Boolean, bovenrand as Number) as Void {
        var soorten = [] as Array<Number>;
        for (var i = 0; i < n; i += 1) {
            soorten.add(VOLGORDE[i % 9]);
        }
        if (kroon) {
            soorten.add(KROON);
        }
        var aantal = soorten.size();
        if (aantal == 0) {
            return;
        }
        var som = 0;
        for (var i = 0; i < aantal; i += 1) {
            som += m[13 + 2 * soorten[i]];
        }
        var top = m[13 + 2 * soorten[aantal - 1]];
        var ruimte = kruinY - bovenrand - top * 0.78;
        var nodig = (som - top) * 0.56;
        var stap = 0.56;
        if (nodig > ruimte && nodig > 0) {
            stap = 0.56 * ruimte / nodig;
        }
        var y = kruinY.toFloat();
        for (var i = 0; i < aantal; i += 1) {
            var k = soorten[i];
            var hb = m[12 + 2 * k];
            var hh = m[13 + 2 * k];
            var boven = y - hh * 0.78;
            var dx = ((i * 7) % 5) - 2;
            dc.drawBitmap(torenX - hb / 2 + dx, boven.toNumber(), pl[2 + k]);
            y = y - hh * stap;
        }
    }

    // Slaapstand op AMOLED: zwart, alleen de tijd in grijs, elke minuut een paar pixels verschoven
    // tegen inbranden. Gloop als lijn komt erbij zodra Mila die tekening heeft.
    function tekenSlaap(dc as Graphics.Dc, w as Number, h as Number, tijd as String, minuut as Number) as Void {
        dc.setColor(0x000000, 0x000000);
        dc.clear();
        var font = tijdFont(dc, tijd, (w * 0.54).toNumber());
        var fh = dc.getFontHeight(font);
        dc.setColor(0xAAAAAA, Graphics.COLOR_TRANSPARENT);
        dc.drawText((w * 0.06).toNumber() + (minuut % 5) * 2, (h * 0.42).toNumber() - fh / 2 + (minuut % 3) * 2, font, tijd, Graphics.TEXT_JUSTIFY_LEFT);
    }

    // Tekst met een zwarte rand van 1 px, zodat hij ook op de bruine grot van MIP te lezen is.
    function tekst(dc as Graphics.Dc, x as Number, y as Number, font as Graphics.FontDefinition, s as String, kleur as Number) as Void {
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x - 1, y, font, s, Graphics.TEXT_JUSTIFY_LEFT);
        dc.drawText(x + 1, y, font, s, Graphics.TEXT_JUSTIFY_LEFT);
        dc.drawText(x, y - 1, font, s, Graphics.TEXT_JUSTIFY_LEFT);
        dc.drawText(x, y + 1, font, s, Graphics.TEXT_JUSTIFY_LEFT);
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x, y, font, s, Graphics.TEXT_JUSTIFY_LEFT);
    }
}
