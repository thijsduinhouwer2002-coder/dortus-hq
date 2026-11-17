import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Time;
import Toybox.Time.Gregorian;
import Toybox.WatchUi;

class KernView extends WatchUi.WatchFace {
    var bb as Array<Number> = [] as Array<Number>;
    var st as Array<Number> = [] as Array<Number>;
    var weer as Number = -2;
    var gelezen as Boolean = false;
    var tik as Number = 0;
    // Proef 2 (run 124): de vier letters van Tij (fontG tijd, fontK BB-getal, fontV veld, fontD datum), een schermvullend plaatje, de slaapstand.
    var fontK as WatchUi.FontResource? = null;
    var fontG as WatchUi.FontResource? = null;
    var fontV as WatchUi.FontResource? = null;
    var fontD as WatchUi.FontResource? = null;
    var slaap as Boolean = false;
    var start as Number = 0;
    var gelezenOp as Number = 0;
    // Thema van de plaat. Kiezen in Garmin Connect komt in stap (d); tot dan Tide.
    var thema as Number = Thema.TIDE;

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
        fontG = WatchUi.loadResource(Rez.Fonts.Tijd) as WatchUi.FontResource;
        var m1 = System.getSystemStats().usedMemory;
        fontK = WatchUi.loadResource(Rez.Fonts.Bb) as WatchUi.FontResource;
        var m2a = System.getSystemStats().usedMemory;
        fontV = WatchUi.loadResource(Rez.Fonts.Veld) as WatchUi.FontResource;
        var m2b = System.getSystemStats().usedMemory;
        fontD = WatchUi.loadResource(Rez.Fonts.Datum) as WatchUi.FontResource;
        var m2 = System.getSystemStats().usedMemory;
        System.println("KERN FONT tijd=" + (m1 - m0) + " bb=" + (m2a - m1) + " veld=" + (m2b - m2a)
            + " datum=" + (m2 - m2b) + " samen=" + (m2 - m0) + " gebruikt=" + m2
            + " vrij=" + System.getSystemStats().freeMemory);
        var ds = System.getDeviceSettings();
        var inbrand = (ds has :requiresBurnInProtection) ? ds.requiresBurnInProtection : false;
        System.println("KERN SCHERM " + ds.screenWidth + "x" + ds.screenHeight + " inbrand=" + inbrand
            + " pool=" + ((Graphics has :createBufferedBitmap) ? "ja" : "nee"));
        // Stap (a) van de kern: de maten van dit scherm uit het blad van Mila.
        System.println("KERN MATEN n=" + Maten.laad().size() + " tijdPx=" + Maten.m(Maten.TIJD_PX) + " bbY=" + Maten.m(Maten.BB_Y)
            + " veilig=" + Maten.m(Maten.VEILIG) + " bytes=" + (System.getSystemStats().usedMemory - m2));
        // Het schermvullende proefplaatje wordt niet meer geladen: het paste niet op de Forerunner 245
        // (run 43985122863: Out Of Memory) en de kern tekent alles zelf.
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
        if (fontG != null) {
            dc.drawText(w / 2, h * 14 / 100, fontG as WatchUi.FontResource, tekst, Graphics.TEXT_JUSTIFY_CENTER);
        }
        var lijn = Teken.profiel(bb, w * 20 / 100, w * 80 / 100, h * 78 / 100, h * 64 / 100, 20);
        dc.setColor(Graphics.COLOR_DK_GRAY, Graphics.COLOR_TRANSPARENT);
        for (var i = 1; i + 2 < lijn.size(); i++) {
            dc.drawLine(lijn[i][0], lijn[i][1], lijn[i + 1][0], lijn[i + 1][1]);
        }
    }

    // Stap (b) van de kern: datum, tijd en drie velden op de maten van het blad, in de kleuren van het thema.
    // Geen maten voor dit scherm (lege lijst): alleen de tijd in het midden, zodat niets op 0,0 belandt.
    function tekenBoven(dc as Graphics.Dc, uur as String, minuut as String) as Void {
        var w = dc.getWidth();
        var mid = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        var links = Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER;
        // Punt van de keurder (run 126): een scherm zonder eigen map krijgt de maten van 260 px. Past de
        // veilige cirkel van het blad niet op dit scherm (Instinct 2), dan alleen de tijd in het midden.
        var heeftMaten = Maten.laad().size() == Maten.AANTAL && Maten.m(Maten.VEILIG) * 2 <= w;
        var yTijd = heeftMaten ? Maten.m(Maten.TIJD_Y) : dc.getHeight() / 2;
        if (fontG != null) {
            var f = fontG as WatchUi.FontResource;
            var bu = dc.getTextWidthInPixels(uur, f);
            var bp = dc.getTextWidthInPixels(":", f);
            var bm = dc.getTextWidthInPixels(minuut, f);
            var x = (w - bu - bp - bm) / 2;
            dc.setColor(Thema.kleur(thema, Thema.UREN), Graphics.COLOR_TRANSPARENT);
            dc.drawText(x, yTijd, f, uur, links);
            dc.setColor(Thema.kleur(thema, Thema.PUNT), Graphics.COLOR_TRANSPARENT);
            dc.drawText(x + bu, yTijd, f, ":", links);
            dc.setColor(Thema.kleur(thema, Thema.MINUTEN), Graphics.COLOR_TRANSPARENT);
            dc.drawText(x + bu + bp, yTijd, f, minuut, links);
        }
        if (!heeftMaten) {
            return;
        }
        dc.setColor(Thema.kleur(thema, Thema.TEKST), Graphics.COLOR_TRANSPARENT);
        if (fontD != null) {
            var dag = Gregorian.info(Time.now(), Time.FORMAT_SHORT);
            var namen = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] as Array<String>;
            var d = (dag.day_of_week as Number) - 1;
            if (d < 0 || d > 6) {
                d = 0;
            }
            dc.drawText(w / 2, Maten.m(Maten.DATUM_Y), fontD as WatchUi.FontResource,
                namen[d] + " " + (dag.day as Number).format("%d"), mid);
        }
        var xs = [Maten.m(Maten.VELD_XL), Maten.m(Maten.VELD_XM), Maten.m(Maten.VELD_XR)] as Array<Number>;
        var soorten = [Veld.HART, Veld.STRESS, Veld.STAPPEN] as Array<Number>;
        var yVeld = Maten.m(Maten.VELD_Y);
        var streep = Maten.m(Maten.VELD_PX) / 2;
        var dik = Maten.m(Maten.LIJN_DIK);
        var regel = "";
        for (var i = 0; i < 3; i++) {
            var t = Veld.tekst(Veld.waarde(soorten[i], st));
            regel = regel + " " + ((t == null) ? "-" : t);
            // Het hart krijgt de kleur van de minuten (blad van Mila), de andere pictogrammen die van de tekst.
            dc.setColor(Thema.kleur(thema, (soorten[i] == Veld.HART) ? Thema.MINUTEN : Thema.TEKST), Graphics.COLOR_TRANSPARENT);
            Teken.icoon(dc, soorten[i], xs[i], Maten.m(Maten.ICOON_Y), Maten.m(Maten.ICOON_H));
            dc.setColor(Thema.kleur(thema, Thema.TEKST), Graphics.COLOR_TRANSPARENT);
            if (t != null && fontV != null) {
                dc.drawText(xs[i], yVeld, fontV as WatchUi.FontResource, t, mid);
            } else {
                // Geen gegevens: een streepje, getekend (de letter Veld heeft geen streepje).
                dc.fillRectangle(xs[i] - streep / 2, yVeld - dik / 2, streep, dik);
            }
        }
        // Het getal van Body Battery: de laatste waarde uit de geschiedenis, of een streepje.
        var yBb = Maten.m(Maten.BB_Y);
        if (bb.size() > 0 && fontK != null) {
            dc.drawText(w / 2, yBb, fontK as WatchUi.FontResource, bb[bb.size() - 1].format("%d"), mid);
        } else {
            dc.fillRectangle(w / 2 - streep, yBb - dik / 2, streep * 2, dik);
        }
        if (tik < 2) {
            System.println("KERN VELDEN hart stress stappen:" + regel + " thema=" + thema);
        }
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        if (!gelezen) {
            gelezen = true;
            start = System.getTimer();
            leesAlles();
            meetBeelden();
            gelezenOp = System.getTimer();
        } else if (System.getTimer() - gelezenOp >= 300000) {
            // Punt van de keurder (run 126): Body Battery en stress elke vijf minuten opnieuw lezen,
            // anders blijft de plaat op de waarde van het opstarten staan.
            gelezenOp = System.getTimer();
            bb = Lees.hist(0) as Array<Number>;
            st = Lees.hist(1) as Array<Number>;
        }
        var nu = System.getClockTime();
        var tekst = nu.hour.format("%02d") + ":" + nu.min.format("%02d");
        // De simulator zet de slaapstand niet vanzelf aan: 6 s na het eerste beeld tonen we het slaapbeeld zelf.
        if (slaap || System.getTimer() - start >= 6000) {
            var ts = System.getTimer();
            tekenSlaap(dc, tekst);
            if (tik < 40) {
                System.println("KERN SLAAPBEELD tik=" + tik + " ms=" + (System.getTimer() - ts) + " echt=" + slaap);
            }
            tik++;
            return;
        }
        var t0 = System.getTimer();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var msPlaat = System.getTimer() - t0;
        tekenBoven(dc, nu.hour.format("%02d"), nu.min.format("%02d"));
        var msTijd = System.getTimer() - t0 - msPlaat;
        // Plek van de zee (komt na het ja van Daan): tot dan het verloop van Body Battery en stress als vlakken
        // tussen het plafond en de bodem van het water uit het blad. Zonder maten: niets.
        if (Maten.laad().size() == Maten.AANTAL && Maten.m(Maten.VEILIG) * 2 <= dc.getWidth()) {
            var x0 = Maten.m(Maten.LIJN_X);
            var x1 = Maten.m(Maten.NU_X);
            var yT = Maten.m(Maten.WATER_TOP);
            var yB = Maten.m(Maten.WATER_BODEM);
            var heuvel = Teken.profiel(bb, x0, x1, yB, yT, 40);
            if (heuvel.size() >= 3) {
                dc.setColor(Thema.kleur(thema, Thema.ZEE_BOVEN), Graphics.COLOR_TRANSPARENT);
                dc.fillPolygon(heuvel);
            }
            var stress = Teken.profiel(st, x0, x1, yB, (yT + yB) / 2, 40);
            if (stress.size() >= 3) {
                dc.setColor(Thema.kleur(thema, Thema.ZEE_ONDER), Graphics.COLOR_TRANSPARENT);
                dc.fillPolygon(stress);
            }
        }
        var ms = System.getTimer() - t0;
        if (tik < 4) {
            System.println("KERN TEKEN tik=" + tik + " ms=" + ms + " plaatje_ms=" + msPlaat + " tijd_ms=" + msTijd);
        }
        tik++;
    }
}
