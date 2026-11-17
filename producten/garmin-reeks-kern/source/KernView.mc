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
    // De dunne tijd voor de slaapstand; alleen geladen op een scherm dat kan inbranden (anders null en geen geheugen).
    var fontS as WatchUi.FontResource? = null;
    var fontV as WatchUi.FontResource? = null;
    var fontD as WatchUi.FontResource? = null;
    var slaap as Boolean = false;
    var start as Number = 0;
    var gelezenOp as Number = 0;
    // Thema van de plaat: betaald kiest de drager in Garmin Connect (Keuze), gratis is het Tide (Soort). Alleen in de bouwstraat per proefhorloge een ander (Proef.thema).
    var thema as Number = Thema.TIDE;
    // De drie velden onder de tijd (links, midden, rechts): betaald kiest de drager, gratis ligt vast (Soort.velden).
    var soorten as Array<Number> = [Veld.HART, Veld.STRESS, Veld.STAPPEN] as Array<Number>;
    // Scherm zonder inbrandgevaar (MIP): geen zwart slaapbeeld, en de zee krijgt vaste paletkleuren.
    var mip as Boolean = false;
    // Hoeveel kleuren: Thema.VOL, MIP64 of MIP8. 8 kleuren staat per horloge in resources-<horloge>/jsondata (Kleuren).
    var diepte as Number = Thema.VOL;

    function initialize() {
        WatchFace.initialize();
    }

    function leesAlles() as Void {
        bb = Proef.bb(Lees.hist(0) as Array<Number>, thema);
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
        mip = !inbrand;
        diepte = Thema.VOL;
        if (mip) {
            var kl = WatchUi.loadResource(Rez.JsonData.Kleuren);
            diepte = (kl instanceof Lang.Array && kl.size() > 0 && kl[0] == 8) ? Thema.MIP8 : Thema.MIP64;
        }
        if (inbrand) {
            var ms0 = System.getSystemStats().usedMemory;
            fontS = WatchUi.loadResource(Rez.Fonts.TijdSlaap) as WatchUi.FontResource;
            System.println("KERN FONT tijdslaap=" + (System.getSystemStats().usedMemory - ms0) + " vrij=" + System.getSystemStats().freeMemory);
        }
        System.println("KERN SCHERM " + ds.screenWidth + "x" + ds.screenHeight + " inbrand=" + inbrand
            + " pool=" + ((Graphics has :createBufferedBitmap) ? "ja" : "nee") + " diepte=" + diepte);
        // Stap (a) van de kern: de maten van dit scherm uit het blad van Mila.
        System.println("KERN MATEN n=" + Maten.laad().size() + " tijdPx=" + Maten.m(Maten.TIJD_PX) + " bbY=" + Maten.m(Maten.BB_Y)
            + " veilig=" + Maten.m(Maten.VEILIG) + " bytes=" + (System.getSystemStats().usedMemory - m2));
        // Het schermvullende proefplaatje wordt niet meer geladen: het paste niet op de Forerunner 245
        // (run 43985122863: Out Of Memory) en de kern tekent alles zelf.
    }

    // De drager koos iets anders in Garmin Connect: het thema opnieuw lezen en meteen tekenen. Voor het eerste
    // beeld (breedte nog niet bekend) hoeft dat niet: onUpdate leest dan zelf.
    function instellingenVeranderd() as Void {
        if (gelezen) {
            thema = Proef.thema(Soort.thema(), System.getDeviceSettings().screenWidth);
            soorten = Proef.velden(Soort.velden(), System.getDeviceSettings().screenWidth);
            bb = Proef.bb(Lees.hist(0) as Array<Number>, thema);
            System.println("KERN INSTELLING thema=" + thema + " velden=" + soorten[0] + "," + soorten[1] + "," + soorten[2]);
        }
        WatchUi.requestUpdate();
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

    // Slaapbeeld: zwart, de tijd in grijs (dun op een scherm dat kan inbranden), een dunne lijn van Body Battery
    // en het bootje als omtrek aan het eind van die lijn.
    function tekenSlaap(dc as Graphics.Dc, tekst as String, n as Number) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var sch = Slaap.schuif(n);
        var dx = sch[0];
        var dy = sch[1];
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        // Scherm dat kan inbranden: de dunne tijd. Anders (geen inbrandgevaar) de gewone tijd, dat scheelt een letter in het geheugen.
        var fs = (fontS != null) ? fontS : fontG;
        if (fs != null) {
            dc.drawText(w / 2 + dx, h * 14 / 100 + dy, fs as WatchUi.FontResource, tekst, Graphics.TEXT_JUSTIFY_CENTER);
        }
        // Het bootje als omtrek van 1 px aan het eind van de lijn (kan van Mila en Daan). Alleen met maten voor dit
        // scherm; de lijn stopt dan bij de punt van de romp (de romp ligt 15% van s lager, zodat lijn en punt elkaar raken; punt van de keurder). Onder de 10 ligt het scheef, net als wakker.
        var s = Maten.passen(w, h) ? Maten.m(Maten.BOOT_HALF) : 0;
        var x1 = w * 80 / 100;
        var lijn = Teken.profiel(bb, w * 20 / 100, x1 - s, h * 78 / 100, h * 64 / 100, 20);
        dc.setColor(Graphics.COLOR_DK_GRAY, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(1);
        for (var i = 1; i + 2 < lijn.size(); i++) {
            dc.drawLine(lijn[i][0] + dx, lijn[i][1] + dy, lijn[i + 1][0] + dx, lijn[i + 1][1] + dy);
        }
        var bbNu = Veld.laatste(bb);
        if (s > 0 && lijn.size() >= 4 && bbNu != null) {
            var eind = lijn[lijn.size() - 2];
            var stukken = Zee.bootLijnen(Zee.boot(x1, (eind[1] as Number) + s * 15 / 100, s, (bbNu < 10) ? -22 : 0));
            for (var i = 0; i < stukken.size(); i++) {
                var k = stukken[i];
                dc.drawLine(k[0] + dx, k[1] + dy, k[2] + dx, k[3] + dy);
            }
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
        var heeftMaten = Maten.passen(w, dc.getHeight());
        var yTijd = heeftMaten ? Maten.m(Maten.TIJD_Y) : dc.getHeight() / 2;
        if (fontG != null) {
            var f = fontG as WatchUi.FontResource;
            var bu = dc.getTextWidthInPixels(uur, f);
            var bp = dc.getTextWidthInPixels(":", f);
            var bm = dc.getTextWidthInPixels(minuut, f);
            var x = (w - bu - bp - bm) / 2;
            dc.setColor(Thema.uren(thema, diepte), Graphics.COLOR_TRANSPARENT);
            dc.drawText(x, yTijd, f, uur, links);
            dc.setColor(Thema.punt(thema, diepte), Graphics.COLOR_TRANSPARENT);
            dc.drawText(x + bu, yTijd, f, ":", links);
            dc.setColor(Thema.minuten(thema, diepte), Graphics.COLOR_TRANSPARENT);
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
        var yVeld = Maten.m(Maten.VELD_Y);
        var streep = Maten.m(Maten.VELD_PX) / 2;
        var dik = Maten.m(Maten.LIJN_DIK);
        var regel = "";
        for (var i = 0; i < 3; i++) {
            var v = Veld.waarde(soorten[i], st);
            var t = Veld.tekstVan(soorten[i], v);
            regel = regel + " " + ((t == null) ? "-" : t);
            // Het hart krijgt de kleur van de minuten (blad van Mila), de andere pictogrammen die van de tekst.
            dc.setColor((soorten[i] == Veld.HART) ? Thema.minuten(thema, diepte) : Thema.kleur(thema, Thema.TEKST), Graphics.COLOR_TRANSPARENT);
            Teken.icoon(dc, soorten[i], xs[i], Maten.m(Maten.ICOON_Y), Maten.m(Maten.ICOON_H));
            dc.setColor(Thema.kleur(thema, Thema.TEKST), Graphics.COLOR_TRANSPARENT);
            if (t != null && fontV != null) {
                dc.drawText(xs[i], yVeld, fontV as WatchUi.FontResource, t, mid);
                if (Veld.isMin(soorten[i], v)) {
                    // Temperatuur onder nul: het minteken als streepje links van het getal.
                    var half = dc.getTextWidthInPixels(t, fontV as WatchUi.FontResource) / 2;
                    var mm = Veld.minMaten(Maten.m(Maten.VELD_PX), dik);
                    dc.fillRectangle(xs[i] - half - mm[2] - mm[0], yVeld - mm[1] / 2, mm[0], mm[1]);
                }
            } else {
                // Geen gegevens: een streepje, getekend (de letter Veld heeft geen streepje).
                dc.fillRectangle(xs[i] - streep / 2, yVeld - dik / 2, streep, dik);
            }
        }
        if (tik < 2) {
            System.println("KERN VELDEN" + regel + " thema=" + thema);
        }
    }

    // De zee van Tij (ontwerp-kern.md, deel "De zee"): vier banden onder de waterlijn uit het verloop van Body
    // Battery, het bootje op nu, en het getal met rand en golfje. Zonder maten: niets. Zonder Body Battery:
    // een vlakke zee halverwege, geen bootje, een streepje als getal.
    function tekenZee(dc as Graphics.Dc, t as Number) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        if (!Maten.passen(w, h)) {
            return;
        }
        // Rechthoek (Venu Sq 2): geen veilige cirkel, de zee loopt van rand tot rand en het bootje blijft op zijn plek.
        var straal = Maten.m(Maten.VEILIG);
        if (straal == 0) {
            straal = w + h;
        }
        var c = w / 2;
        var yT = Maten.m(Maten.WATER_TOP);
        var yB = Maten.m(Maten.WATER_BODEM);
        var s = Maten.m(Maten.BOOT_HALF);
        var dik = Maten.m(Maten.BB_RAND);
        var lijnDik = Maten.m(Maten.LIJN_DIK);
        var g = w * 4 / 208;
        if (g < 4) {
            g = 4;
        }
        var bbNu = Veld.laatste(bb);
        var tekst = (bbNu != null) ? bbNu.format("%d") : null;
        var streep = Maten.m(Maten.VELD_PX) / 2;
        var bw = streep * 2;
        if (tekst != null && fontK != null) {
            bw = dc.getTextWidthInPixels(tekst, fontK as WatchUi.FontResource);
        }
        // Getal en golfje staan samen in het midden.
        var groep = bw + ((tekst != null) ? Maten.m(Maten.GOLF_AFSTAND) + Maten.m(Maten.GOLF_B) : 0);
        var gx1 = c + groep / 2 + dik;
        var gx0 = c - groep / 2 - dik;
        var nx = c - groep / 2 + bw / 2;
        var ny = Maten.m(Maten.BB_Y);
        var half = Maten.m(Maten.BB_PX) * 4 / 10;
        // Het bootje: rechts van het getal, binnen de veilige cirkel. Onder de 10 ligt het scheef aan de grond.
        var nuX = Maten.m(Maten.NU_X);
        var bootje = [] as Array<Graphics.Point2D>;
        var pts = [] as Array<Graphics.Point2D>;
        if (bbNu != null) {
            var laag = bbNu < 10;
            var zak = laag ? w * 12 / 1000 : 0;
            var by = Zee.niveau(bbNu, yT, yB) + zak;
            var hoek = laag ? -22 : 0;
            var stap = w / 100;
            nuX = Zee.bootX(nuX, gx1 + s * 11 / 10 + g, by, s, hoek, c, straal, stap);
            pts = Zee.lijn(bb, Maten.m(Maten.LIJN_X), nuX, w, yT, yB, t);
            // Punt van de keurder (run 130): bij één meting deint de vlakke zee; het bootje ligt op de golf, niet ernaast.
            bootje = Zee.boot(nuX, Zee.hoogte(pts, nuX) + zak, s, hoek);
        } else {
            pts = Zee.lijn(bb, Maten.m(Maten.LIJN_X), nuX, w, yT, yB, t);
        }
        // Ruimte tussen getal en water of zeil: komt het te dichtbij, dan schuift het getal omhoog, tot vlak onder de velden.
        var top = Zee.topTussen(pts, gx0 - g, gx1 + g);
        var topBoot = Zee.topTussen(bootje, gx0 - g, gx1 + g);
        if (topBoot < top) {
            top = topBoot;
        }
        var maxOmhoog = (ny - half - dik) - (Maten.m(Maten.VELD_Y) + Maten.m(Maten.VELD_PX) * 4 / 10 + w * 12 / 1000);
        ny -= Zee.schuif(ny + half + dik, g, top - lijnDik / 2, maxOmhoog);
        for (var i = 0; i < 4; i++) {
            dc.setColor(Thema.band(thema, i, diepte), Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon(Zee.band(pts, Maten.m(Maten.BAND_0 + i), w, h));
        }
        // 64 en 8 kleuren: een vaste kleur per thema uit het blad van Mila (wit las in run 44014109126 als een harde witte rand).
        var lijnKleur = Thema.waterlijn(thema, diepte);
        dc.setColor(lijnKleur, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(lijnDik);
        for (var i = 0; i + 1 < pts.size(); i++) {
            dc.drawLine(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]);
        }
        if (bootje.size() == 9) {
            dc.setColor(Thema.kleur(thema, Thema.BOOT), Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon([bootje[0], bootje[1], bootje[2], bootje[3]] as Array<Graphics.Point2D>);
            dc.setPenWidth((w >= 300) ? w / 150 : 2);
            dc.drawLine(bootje[7][0], bootje[7][1], bootje[8][0], bootje[8][1]);
            dc.setColor(Thema.zeil(thema, diepte), Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon([bootje[4], bootje[5], bootje[6]] as Array<Graphics.Point2D>);
        }
        var mid = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        if (tekst != null && fontK != null) {
            var f = fontK as WatchUi.FontResource;
            // Donkere rand van dik px om het getal, dan het getal in wit.
            dc.setColor(Thema.rand(thema, diepte), Graphics.COLOR_TRANSPARENT);
            // Acht richtingen op afstand dik (punt van de keurder: niet elk tussenpunt, dat kost 24 keer tekenen bij 2 px).
            for (var dx = -dik; dik > 0 && dx <= dik; dx += dik) {
                for (var dy = -dik; dy <= dik; dy += dik) {
                    if (dx != 0 || dy != 0) {
                        dc.drawText(nx + dx, ny + dy, f, tekst, mid);
                    }
                }
            }
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            dc.drawText(nx, ny, f, tekst, mid);
            var gk = Maten.m(Maten.GOLF_B);
            var golven = Zee.golfje(nx + bw / 2 + Maten.m(Maten.GOLF_AFSTAND) + gk / 2, ny + 1, gk);
            dc.setColor(lijnKleur, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(Maten.m(Maten.GOLF_DIK));
            for (var r = 0; r < golven.size(); r++) {
                var gp = golven[r];
                for (var i = 0; i + 1 < gp.size(); i++) {
                    dc.drawLine(gp[i][0], gp[i][1], gp[i + 1][0], gp[i + 1][1]);
                }
            }
        } else {
            dc.setColor(Thema.kleur(thema, Thema.TEKST), Graphics.COLOR_TRANSPARENT);
            dc.fillRectangle(c - streep, ny - Maten.m(Maten.LIJN_DIK) / 2, streep * 2, Maten.m(Maten.LIJN_DIK));
        }
        dc.setPenWidth(1);
        if (tik < 2) {
            System.println("KERN ZEE bb=" + bb.size() + " nu=" + ((tekst == null) ? "-" : tekst) + " bootX=" + nuX
                + " getalY=" + ny + " mip=" + mip + " diepte=" + diepte + " glad=" + ((!mip && (dc has :setAntiAlias)) ? "ja" : "nee") + " eerste=" + ((bb.size() > 0) ? bb[0].format("%d") : "-"));
        }
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        if (!gelezen) {
            gelezen = true;
            start = System.getTimer();
            thema = Proef.thema(Soort.thema(), dc.getWidth());
            soorten = Proef.velden(Soort.velden(), dc.getWidth());
            System.println("KERN SOORT betaald=" + (Soort.BETAALD ? "ja" : "nee") + " thema=" + thema
                + " velden=" + soorten[0] + "," + soorten[1] + "," + soorten[2]);
            leesAlles();
            meetBeelden();
            gelezenOp = System.getTimer();
        } else if (System.getTimer() - gelezenOp >= 300000) {
            // Punt van de keurder (run 126): Body Battery en stress elke vijf minuten opnieuw lezen,
            // anders blijft de plaat op de waarde van het opstarten staan.
            gelezenOp = System.getTimer();
            bb = Proef.bb(Lees.hist(0) as Array<Number>, thema);
            st = Lees.hist(1) as Array<Number>;
        }
        var nu = System.getClockTime();
        var tekst = nu.hour.format("%02d") + ":" + nu.min.format("%02d");
        // Alleen in de bouwstraat (proef.jungle) geeft Proef.fase iets anders dan WAKKER: zie Proef.mc.
        var fase = Proef.fase(System.getTimer() - start);
        if (fase == Proef.WIT) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_WHITE);
            dc.clear();
            return;
        }
        // Het zwarte slaapbeeld is er alleen voor schermen die kunnen inbranden. Een MIP-scherm staat bijna altijd in
        // de slaapstand en toont daar gewoon de hele plaat met de zee (punt van de keurder, run 130).
        if ((slaap || fase == Proef.SLAAP) && !mip) {
            var ts = System.getTimer();
            var sn = Proef.schuifTel(nu.min, tik);
            tekenSlaap(dc, tekst, sn);
            if (tik < 40) {
                System.println("KERN SLAAPBEELD tik=" + tik + " ms=" + (System.getTimer() - ts) + " echt=" + slaap + " schuif=" + Slaap.schuif(sn)[0] + "," + Slaap.schuif(sn)[1]);
            }
            tik++;
            return;
        }
        var t0 = System.getTimer();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var msPlaat = System.getTimer() - t0;
        // Gladde randen (moet van Daan, 17 nov): alleen op AMOLED en waar het horloge het kan. Op MIP horen harde
        // randen bij het palet; daar blijft het uit. Elke tekenbeurt aan, na de tekenbeurt weer uit.
        var glad = !mip && (dc has :setAntiAlias);
        if (glad) {
            dc.setAntiAlias(true);
        }
        // Eerst de zee, dan datum, tijd en velden erover: de tijd staat altijd boven water.
        tekenZee(dc, nu.min);
        var msZee = System.getTimer() - t0 - msPlaat;
        tekenBoven(dc, nu.hour.format("%02d"), nu.min.format("%02d"));
        if (glad) {
            dc.setAntiAlias(false);
        }
        var ms = System.getTimer() - t0;
        if (tik < 4) {
            System.println("KERN TEKEN tik=" + tik + " ms=" + ms + " plaatje_ms=" + msPlaat + " zee_ms=" + msZee);
        }
        tik++;
    }
}
