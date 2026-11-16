import Toybox.Activity;
import Toybox.ActivityMonitor;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Time;
import Toybox.Time.Gregorian;
import Toybox.WatchUi;

typedef Plaatje as WatchUi.BitmapResource or Graphics.BitmapReference;

// De wijzerplaat: links de datum, uren boven minuten (groot), stappen, hoeden, hartslag en batterij.
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
    // Afstand van de urenregel tot de minutenregel, als deel van de fonthoogte (cijferfonts hebben
    // lucht boven en onder de cijfers).
    const PITCH = 0.80;
    // Standen voor de bouwstraat (Bouw.AUTO): stappen per stand; de laatste stand is de slaapstand.
    const PROEF = [0, 3420, 7612, 10000, 14800, 7612] as Array<Number>;

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
        var uren = Regel.uur(klok.hour, is24).format(is24 ? "%02d" : "%d");
        var minuten = klok.min.format("%02d");
        var rond = System.getDeviceSettings().screenShape == System.SCREEN_SHAPE_ROUND;

        if (slaapt && amoled) {
            tekenSlaap(dc, w, h, uren, minuten, klok.min, rond);
        } else {
            tekenVol(dc, w, h, uren, minuten, stappen, doel, amoled, rond);
        }
        if (!gemeld) {
            gemeld = true;
            var st = System.getSystemStats();
            System.println("GEHEUGEN " + w + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " vrij " + st.freeMemory);
        }
    }

    // Grootste cijferfont waarbij uren boven minuten passen: twee cijfers breed binnen `breed` px
    // en twee regels plus de kleine regels eromheen binnen `hoog` px.
    function tijdFont(dc as Graphics.Dc, breed as Number, hoog as Number) as Graphics.FontDefinition {
        var fonts = [Graphics.FONT_NUMBER_THAI_HOT, Graphics.FONT_NUMBER_HOT, Graphics.FONT_NUMBER_MEDIUM, Graphics.FONT_NUMBER_MILD] as Array<Graphics.FontDefinition>;
        for (var i = 0; i < fonts.size(); i += 1) {
            var fh = dc.getFontHeight(fonts[i]);
            if (dc.getTextWidthInPixels("00", fonts[i]) <= breed && fh * (PITCH + 0.80) <= hoog) {
                return fonts[i];
            }
        }
        return Graphics.FONT_NUMBER_MILD;
    }

    function tekenVol(dc as Graphics.Dc, w as Number, h as Number, uren as String, minuten as String, stappen as Number, doel as Number, amoled as Boolean, rond as Boolean) as Void {
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
        tekenToren(dc, w, h, rond, torenX, kruinY, n, kroon, Regel.hoedenBijDoel(doel));

        // Links: datum, uren boven minuten, stappen, hoeden, hartslag en batterij.
        var klein = Graphics.FONT_TINY;
        var kh = dc.getFontHeight(klein);
        var xh = dc.getFontHeight(Graphics.FONT_XTINY);
        var torenLinks = torenX - m[12] / 2 - 2;
        var gloopLinks = gx - m[0] / 2 - 6;
        var boven = (h * (rond ? 0.11 : 0.07)).toNumber();
        var onder = (h * 0.93).toNumber();
        var font = tijdFont(dc, torenLinks - 8 - (w * 0.10).toNumber(), onder - boven - 3 * kh - xh + 12);
        var fh = dc.getFontHeight(font);
        var pitch = (fh * PITCH).toNumber();
        var uy = boven + kh - (fh * 0.12).toNumber();
        var my = uy + pitch;
        var tx = Regel.randLinks(uy + fh / 5, my + fh * 4 / 5, w, h, rond, 6);
        if (tx < (w * 0.07).toNumber()) {
            tx = (w * 0.07).toNumber();
        }
        var nu = Gregorian.info(Time.now(), Time.FORMAT_MEDIUM);
        tekst(dc, max(tx, Regel.randLinks(boven, boven + kh, w, h, rond, 6)), boven, klein, nu.day_of_week + " " + nu.day, 0xFFFF00);
        tekst(dc, tx, uy, font, uren, 0xFFFFFF);
        tekst(dc, tx, my, font, minuten, 0xFFFFFF);

        var sy = my + (fh * 0.90).toNumber();
        tekst(dc, max(tx, Regel.randLinks(sy, sy + kh, w, h, rond, 6)), sy, klein, stappen.toString(), 0x55FFAA);
        // Onder de stappen: hoeveel hoeden van het doel; na het doel het aantal in geel.
        var hy = sy + kh - 2;
        var hx = max(tx, Regel.randLinks(hy, hy + kh, w, h, rond, 6));
        var regel = kroon ? n + " HATS!" : n + "/" + Regel.hoedenBijDoel(doel) + " HATS";
        var rf = dc.getTextWidthInPixels(regel, klein) <= gloopLinks - hx ? klein : Graphics.FONT_XTINY;
        tekst(dc, hx, hy, rf, regel, kroon ? 0xFFFF00 : 0xFFFFFF);

        // Hartslag en batterij; is er te weinig plek naast Gloop, dan alleen de hartslag.
        var hs = "--";
        var act = Activity.getActivityInfo();
        if (act != null && act.currentHeartRate != null) {
            hs = (act.currentHeartRate as Number).toString();
        }
        var bat = System.getSystemStats().battery.toNumber();
        var by = hy + kh - 2;
        var bx = max(tx, Regel.randLinks(by, by + xh, w, h, rond, 6));
        var lang = "HR " + hs + "  " + bat + "%";
        if (dc.getTextWidthInPixels(lang, Graphics.FONT_XTINY) > gloopLinks - bx) {
            lang = "HR " + hs;
        }
        tekst(dc, bx, by, Graphics.FONT_XTINY, lang, 0xFFAAAA);
    }

    function max(a as Number, b as Number) as Number {
        return a > b ? a : b;
    }

    // Stapelt n hoeden op de kruin en zet bij het doel de kroon erop. De afstand tussen de hoeden is
    // zo gekozen dat de kroon op het moment van het doel helemaal in beeld staat (ook binnen de ronde
    // rand). Daarna komen nieuwe hoeden onder de kroon en gaat de toren het scherm uit: dat is de grap.
    // De toren buigt licht naar rechts, weg van de tijd.
    function tekenToren(dc as Graphics.Dc, w as Number, h as Number, rond as Boolean, torenX as Number, kruinY as Number, n as Number, kroon as Boolean, nDoel as Number) as Void {
        var buig = (w * 0.03).toNumber();
        var som = 0;
        for (var i = 0; i < nDoel; i += 1) {
            som += m[13 + 2 * VOLGORDE[i % 9]];
        }
        var kb = m[12 + 2 * KROON];
        var khoog = m[13 + 2 * KROON];
        var bovenrand = Regel.randBoven(torenX + buig + kb / 2 + 2, w, h, rond, 3);
        var stap = Regel.stap(som, kruinY - bovenrand - (khoog * 0.78).toNumber());
        var y = kruinY.toFloat();
        var aantal = kroon ? n + 1 : n;
        for (var i = 0; i < aantal; i += 1) {
            var k = (kroon && i == n) ? KROON : VOLGORDE[i % 9];
            var hb = m[12 + 2 * k];
            var hh = m[13 + 2 * k];
            var top = (y - hh * 0.78).toNumber();
            if (top + hh < 0) {
                break;
            }
            var dx = ((i * 7) % 5) - 2 + Regel.buiging(i, nDoel, buig);
            dc.drawBitmap(torenX - hb / 2 + dx, top, pl[2 + k]);
            y = y - hh * stap;
        }
    }

    // Slaapstand op AMOLED: zwart, alleen de tijd in grijs (uren boven minuten, zelfde plek), elke
    // minuut een paar pixels verschoven tegen inbranden. Gloop als lijn komt erbij zodra Mila die
    // tekening heeft.
    function tekenSlaap(dc as Graphics.Dc, w as Number, h as Number, uren as String, minuten as String, minuut as Number, rond as Boolean) as Void {
        dc.setColor(0x000000, 0x000000);
        dc.clear();
        var kh = dc.getFontHeight(Graphics.FONT_TINY);
        var xh = dc.getFontHeight(Graphics.FONT_XTINY);
        var boven = (h * (rond ? 0.11 : 0.07)).toNumber();
        var torenLinks = (w * 0.70).toNumber() - m[0] / 2 + m[10] - m[12] / 2 - 2;
        var font = tijdFont(dc, torenLinks - 8 - (w * 0.10).toNumber(), (h * 0.93).toNumber() - boven - 3 * kh - xh + 12);
        var fh = dc.getFontHeight(font);
        var uy = boven + kh - (fh * 0.12).toNumber() + (minuut % 3) * 2;
        var x = (w * 0.10).toNumber() + (minuut % 5) * 2;
        dc.setColor(0xAAAAAA, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x, uy, font, uren, Graphics.TEXT_JUSTIFY_LEFT);
        dc.drawText(x, uy + (fh * PITCH).toNumber(), font, minuten, Graphics.TEXT_JUSTIFY_LEFT);
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
