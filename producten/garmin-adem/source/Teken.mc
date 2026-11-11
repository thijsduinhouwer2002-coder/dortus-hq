import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;
import Toybox.Math;
import Toybox.System;

// Uiterlijk volgens de schets van Mila (ontwerp/garmin/tij-stijl.md en ontwerp/garmin/bron/ebb_schets.py).
// Alle maten als deel van de diameter D, alleen MIP-kleuren, geen verloop.
module EbbTeken {
    const SCHUIM = 0x55FFFF;
    const ZACHT = 0x55AAAA;
    const BEL = 0x55AAFF;
    const KORAAL = 0xFF5555;
    const LICHT = 0xFFFFAA;
    // Boven dit peil raakt het lichte water het fasewoord bovenaan; dan wordt het woord donkerblauw.
    const PEIL_DONKER = 0.74;
    const DIEPTE = [0x00AAAA, 0x0055AA, 0x0000AA, 0x000055] as Array<Number>;
    const GOLF_PUNTEN = 28;

    // Water met een golvende rand: peil is de hoogte vanaf de onderkant als deel van D, fase schuift de golf op.
    function water(dc as Graphics.Dc, d as Number, peil as Float, kleur as Number, fase as Float) as Void {
        var y0 = d * (1.0 - peil);
        var amp = d * 0.025;
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i <= GOLF_PUNTEN; i += 1) {
            var x = (d * i) / GOLF_PUNTEN;
            var y = y0 + amp * Math.sin(2.0 * Math.PI * 2.5 * i / GOLF_PUNTEN + fase);
            pts.add([x, y.toNumber()]);
        }
        var vlak = [] as Array<[Numeric, Numeric]>;
        vlak.addAll(pts);
        vlak.add([d, d]);
        vlak.add([0, d]);
        dc.setColor(kleur, kleur);
        dc.fillPolygon(vlak);
        dc.setColor(SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 110 > 2 ? d / 110 : 2);
        for (var i = 0; i < GOLF_PUNTEN; i += 1) {
            dc.drawLine(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]);
        }
    }

    // Belletjes als omtrek; elk [x, y, r] als deel van D.
    function bellen(dc as Graphics.Dc, d as Number, lijst as Array<Array<Float> >) as Void {
        dc.setColor(BEL, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 180 > 1 ? d / 180 : 1);
        for (var i = 0; i < lijst.size(); i += 1) {
            var b = lijst[i];
            var r = (b[2] * d).toNumber();
            dc.drawCircle((b[0] * d).toNumber(), (b[1] * d).toNumber(), r > 2 ? r : 2);
        }
    }

    // Dieren in koraal, ±0,12 D groot, midden op (cx, cy) in pixels.
    function dier(dc as Graphics.Dc, d as Number, soort as Number, cx as Number, cy as Number) as Void {
        var r = (d * 0.06).toNumber();
        dc.setColor(KORAAL, KORAAL);
        dc.setPenWidth(d / 130 > 2 ? d / 130 : 2);
        if (soort == 0) {
            // vis: lijf en staart, zwemt naar links
            dc.fillEllipse(cx, cy, r, (r * 6) / 10);
            dc.fillPolygon([[cx + r - 2, cy], [cx + r + (r * 7) / 10, cy - (r * 6) / 10], [cx + r + (r * 7) / 10, cy + (r * 6) / 10]]);
        } else if (soort == 1) {
            // kwal: koepel en drie slierten
            dc.fillCircle(cx, cy, r);
            dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
            dc.fillRectangle(cx - r - 1, cy + 1, 2 * r + 3, r + 1);
            dc.setColor(KORAAL, Graphics.COLOR_TRANSPARENT);
            for (var i = -1; i <= 1; i += 1) {
                var x = cx + (i * r * 6) / 10;
                for (var k = 0; k < 4; k += 1) {
                    var dx = (r * 12) / 100;
                    var a = (k % 2 == 0) ? -dx : dx;
                    dc.drawLine(x + a, cy + (k * r * 28) / 100 + 2, x - a, cy + ((k + 1) * r * 28) / 100 + 2);
                }
            }
        } else if (soort == 2) {
            schildpad(dc, cx, cy, d * 1.25 / 100.0);
        } else {
            walvis(dc, cx, cy, d * 1.5 / 100.0);
        }
    }

    // Sea log: kleinere schildpad en walvis, zodat ze naast de tijden passen.
    function dierKlein(dc as Graphics.Dc, d as Number, soort as Number, cx as Number, cy as Number) as Void {
        if (soort == 2) {
            dc.setColor(KORAAL, KORAAL);
            schildpad(dc, cx, cy, d * 0.8 / 100.0);
        } else if (soort == 3) {
            dc.setColor(KORAAL, KORAAL);
            walvis(dc, cx, cy, d * 0.6 / 100.0);
        } else {
            dier(dc, d, soort, cx, cy);
        }
    }

    // Punten in eenheden van D/100 rond het midden (schets Mila, ontwerp/garmin/bron/ebb_dieren2.py).
    function veelhoek(dc as Graphics.Dc, cx as Number, cy as Number, e as Float, pts as Array<Array<Float> >) as Void {
        var uit = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i < pts.size(); i += 1) {
            uit.add([(cx + pts[i][0] * e).toNumber(), (cy + pts[i][1] * e).toNumber()]);
        }
        dc.fillPolygon(uit);
    }

    function lijn(dc as Graphics.Dc, cx as Number, cy as Number, e as Float, x0 as Float, y0 as Float, x1 as Float, y1 as Float) as Void {
        dc.drawLine((cx + x0 * e).toNumber(), (cy + y0 * e).toNumber(), (cx + x1 * e).toNumber(), (cy + y1 * e).toNumber());
    }

    // Mila keuring 1, moet 3: walvis met platte buik, bolle rug, stompe kop, liggende V-staart en een spuitje.
    function walvis(dc as Graphics.Dc, cx as Number, cy as Number, e as Float) as Void {
        var pen = (e / 2).toNumber() > 1 ? (e / 2).toNumber() : 1;
        veelhoek(dc, cx, cy, e, [[10.0, 0.0], [14.5, -3.6], [13.4, 0.0], [14.5, 3.0]] as Array<Array<Float> >);
        veelhoek(dc, cx, cy, e, [[-11.0, 0.0], [-11.0, -2.2], [-9.0, -4.2], [-5.0, -5.0], [1.0, -4.4], [6.0, -2.6], [9.0, -1.2],
            [11.0, -0.6], [11.0, 0.6], [9.0, 1.2], [5.0, 1.6], [-9.0, 1.6], [-11.0, 0.8]] as Array<Array<Float> >);
        dc.setColor(DIEPTE[3], DIEPTE[3]);
        veelhoek(dc, cx, cy, e, [[-4.0, 1.4], [-1.0, 1.4], [-2.6, 3.4]] as Array<Array<Float> >);
        dc.setPenWidth(pen);
        lijn(dc, cx, cy, e, -11.0, 0.2, -7.4, 0.6);
        var oog = (0.7 * e).toNumber() > 1 ? (0.7 * e).toNumber() : 1;
        dc.fillCircle((cx - 8.2 * e).toNumber(), (cy - 1.2 * e).toNumber(), oog);
        dc.setColor(BEL, BEL);
        dc.setPenWidth(pen + 1);
        lijn(dc, cx, cy, e, -7.0, -6.0, -8.6, -8.6);
        lijn(dc, cx, cy, e, -6.4, -6.2, -6.4, -9.2);
        lijn(dc, cx, cy, e, -5.8, -6.0, -4.2, -8.6);
        dc.setColor(KORAAL, KORAAL);
    }

    // Moet 4: schildpad met kop naar voren, schild met naden in de waterkleur, peddels schuin naar achteren.
    function schildpad(dc as Graphics.Dc, cx as Number, cy as Number, e as Float) as Void {
        var pen = (e / 2).toNumber() > 1 ? (e / 2).toNumber() : 1;
        veelhoek(dc, cx, cy, e, [[-3.6, 1.6], [-1.4, 2.0], [-0.4, 4.6], [-2.6, 4.2]] as Array<Array<Float> >);
        veelhoek(dc, cx, cy, e, [[3.2, 1.8], [4.8, 1.2], [6.4, 3.0], [4.6, 3.4]] as Array<Array<Float> >);
        veelhoek(dc, cx, cy, e, [[5.2, -1.4], [6.2, -0.6], [7.4, -0.8], [6.4, -1.8]] as Array<Array<Float> >);
        veelhoek(dc, cx, cy, e, [[-5.0, -2.0], [-7.6, -2.4], [-8.8, -1.0], [-7.6, 0.4], [-5.0, 0.2]] as Array<Array<Float> >);
        // schild: ellips van (-5,5; -4,5) tot (5,5; 2,5)
        dc.fillEllipse(cx, (cy - 1.0 * e).toNumber(), (5.5 * e).toNumber(), (3.5 * e).toNumber());
        dc.setColor(DIEPTE[3], DIEPTE[3]);
        dc.setPenWidth(pen);
        lijn(dc, cx, cy, e, -1.8, -4.2, -1.8, 1.6);
        lijn(dc, cx, cy, e, 1.8, -4.2, 1.8, 1.6);
        lijn(dc, cx, cy, e, -5.2, -1.0, -1.8, -1.0);
        lijn(dc, cx, cy, e, 1.8, -1.0, 5.2, -1.0);
        var oog = (0.55 * e).toNumber() > 1 ? (0.55 * e).toNumber() : 1;
        dc.fillCircle((cx - 7.2 * e).toNumber(), (cy - 1.2 * e).toNumber(), oog);
        dc.setColor(KORAAL, KORAAL);
    }

    // Grootste cijferletter waarvan de cijfers (ascent) niet hoger zijn dan 40% van D
    // en waarin "0:00" niet breder is dan 72% van D, zodat niets buiten de cirkel valt.
    // Eerst kozen we op getFontHeight, maar die telt ruimte onder de letter mee en
    // verschilt per horloge; op de epix2pro47mm viel het cijfer zo op 29%.
    // Haalt de grootste systeemletter geen 30% van D (epix2pro47mm: 123 van 416 px), dan de eigen cijferletter
    // (resources-<horloge>/fonts, 130 px op 416), één keer geladen.
    function grootFont(dc as Graphics.Dc, d as Number) as Graphics.FontType {
        var lijst = GROOT_LIJST;
        var gekozen = Graphics.FONT_NUMBER_MILD;
        for (var i = 0; i < lijst.size(); i += 1) {
            if (Graphics.getFontAscent(lijst[i]) <= d * 0.40 && dc.getTextWidthInPixels("0:00", lijst[i]) <= d * 0.72) {
                gekozen = lijst[i];
                break;
            }
        }
        if (Graphics.getFontAscent(gekozen) * 100 >= d * 30) {
            return gekozen;
        }
        if (_eigen == null) {
            _eigen = WatchUi.loadResource(Rez.Fonts.EbbCijfers) as WatchUi.FontResource;
        }
        return _eigen as WatchUi.FontResource;
    }

    // Blad v6: de waterschaal W0 tot W3 (Mila ebb_blad_v3.py) voor de zee tijdens het inhouden.
    const ZEE_KLEUR = [0x00AAFF, 0x0055AA, 0x0000AA, 0x000055] as Array<Number>;
    const LICHTCYAAN = 0xAAFFFF;
    const GEEL = 0xFFFF55;

    // AMOLED-scherm (burn-in bescherming): daar mag het water per stand 10 procent donkerder (blad v5 en v6).
    function amoled() as Boolean {
        var s = System.getDeviceSettings();
        return (s has :requiresBurnInProtection) && s.requiresBurnInProtection;
    }

    // Kleur k met helderheid pct (100 is gelijk).
    function dimmer(k as Number, pct as Number) as Number {
        var r = ((k >> 16) & 0xFF) * pct / 100;
        var g = ((k >> 8) & 0xFF) * pct / 100;
        var b = (k & 0xFF) * pct / 100;
        return (r << 16) | (g << 8) | b;
    }

    // Blad v6, inhoudscherm: zee in stand 0 tot 5 (EbbProfiel.ZEE). Bovenste band met golf en schuimrand op 0,12 D,
    // de banden eronder als zachte golf zonder schuim. Op AMOLED het hele water 10 procent donkerder per stand.
    function zee(dc as Graphics.Dc, d as Number, stand as Number, fase as Float) as Void {
        var banden = EbbProfiel.ZEE[stand];
        var pct = amoled() ? EbbProfiel.amoledHelderheid(stand) : 100;
        for (var b = 0; b < banden.size(); b += 2) {
            var kleur = ZEE_KLEUR[banden[b + 1]];
            if (pct < 100) {
                kleur = dimmer(kleur, pct);
            }
            var top = banden[b] / 100.0;
            if (b == 0) {
                golf(dc, d, top, d * 0.014, kleur, fase, true);
            } else {
                golf(dc, d, top, d * 0.008, kleur, fase + 1.3 * b, false);
            }
        }
    }

    // Vlak vanaf hoogte top (deel van D vanaf boven) tot de onderkant, met een golvende bovenrand.
    function golf(dc as Graphics.Dc, d as Number, top as Float, amp as Float, kleur as Number, fase as Float, schuim as Boolean) as Void {
        var y0 = d * top;
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i <= GOLF_PUNTEN; i += 1) {
            var x = (d * i) / GOLF_PUNTEN;
            var y = y0 + amp * Math.sin(2.0 * Math.PI * 2.0 * i / GOLF_PUNTEN + fase);
            pts.add([x, y.toNumber()]);
        }
        var vlak = [] as Array<[Numeric, Numeric]>;
        vlak.addAll(pts);
        vlak.add([d, d]);
        vlak.add([0, d]);
        dc.setColor(kleur, kleur);
        dc.fillPolygon(vlak);
        if (schuim) {
            dc.setColor(SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(d / 160 > 1 ? d / 160 : 1);
            for (var i = 0; i < GOLF_PUNTEN; i += 1) {
                dc.drawLine(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]);
            }
        }
    }

    // Blad v6.4: dunne zeestrook onderaan (today, 8 weeks, settings, veiligheid), zodat elk scherm bij dezelfde zee hoort.
    function strook(dc as Graphics.Dc, d as Number) as Void {
        golf(dc, d, 0.885, d * 0.008, ZEE_KLEUR[1], 0.0, false);
        golf(dc, d, 0.935, d * 0.006, ZEE_KLEUR[2], 1.1, false);
    }

    // Blad v6: knop als pil (0055AA) met witte tekst, midden op hoogte y (deel van D).
    function pil(dc as Graphics.Dc, d as Number, y as Float, breed as Float, hoog as Float, tekst as String, font as Graphics.FontType) as Void {
        var bw = (d * breed).toNumber();
        var bh = (d * hoog).toNumber();
        var fh = dc.getFontHeight(font);
        bh = bh < fh + 4 ? fh + 4 : bh;
        var tw = dc.getTextWidthInPixels(tekst, font) + fh;
        bw = bw < tw ? tw : bw;
        dc.setColor(ZEE_KLEUR[1], ZEE_KLEUR[1]);
        dc.fillRoundedRectangle(d / 2 - bw / 2, (d * y).toNumber() - bh / 2, bw, bh, bh / 2);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), font, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v6 scherm 10: rode waarschuwingsdriehoek met wit uitroepteken, midden op (d/2, cy), hoogte s.
    function driehoek(dc as Graphics.Dc, d as Number, cy as Number, s as Number) as Void {
        var cx = d / 2;
        dc.setColor(KORAAL, KORAAL);
        dc.fillPolygon([[cx, cy - s / 2], [cx + (s * 58) / 100, cy + s / 2], [cx - (s * 58) / 100, cy + s / 2]]);
        var b = s / 10 > 1 ? s / 10 : 1;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_WHITE);
        dc.fillRectangle(cx - b / 2, cy - s / 6, b > 1 ? b : 2, s / 3);
        dc.fillRectangle(cx - b / 2, cy + s / 4, b > 1 ? b : 2, b > 1 ? b : 2);
    }

    // Klein hartje (KORAAL), midden op (cx, cy), breedte s.
    function hart(dc as Graphics.Dc, cx as Number, cy as Number, s as Number) as Void {
        var r = s / 4 > 1 ? s / 4 : 1;
        dc.setColor(KORAAL, KORAAL);
        dc.fillCircle(cx - r, cy - r / 2, r);
        dc.fillCircle(cx + r, cy - r / 2, r);
        dc.fillPolygon([[cx - 2 * r, cy - r / 4], [cx + 2 * r, cy - r / 4], [cx, cy + 3 * r / 2 + 1]]);
    }

    // Blad v6 (regel_hart_ronde): hartje + hartslag in wit en "  ·  round N" in lichtcyaan, samen gecentreerd.
    function hartRonde(dc as Graphics.Dc, d as Number, y as Number, bpm as Number, ronde as Number) as Void {
        var font = Graphics.FONT_XTINY;
        var a = bpm > 0 ? bpm.toString() : "--";
        var b = "  ·  round " + ronde;
        var fh = dc.getFontHeight(font);
        var s = (fh * 6) / 10;
        var gap = fh / 5;
        var wa = dc.getTextWidthInPixels(a, font);
        var wb = dc.getTextWidthInPixels(b, font);
        var x0 = d / 2 - (s + gap + wa + wb) / 2;
        hart(dc, x0 + s / 2, y, s);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + s + gap, y, font, a, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + s + gap + wa, y, font, b, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v6 punt 3: twee gespiegelde trilboogjes links en rechts van een regel van breedte breed, in geel.
    function trilboog(dc as Graphics.Dc, d as Number, cy as Number, breed as Number) as Void {
        dc.setColor(GEEL, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 150 > 2 ? d / 150 : 2);
        var rs = [0.026, 0.044] as Array<Float>;
        for (var j = 0; j < 2; j += 1) {
            var r = (rs[j] * d).toNumber();
            var off = breed / 2 + (d * 0.008).toNumber();
            dc.drawArc(d / 2 + off, cy, r, Graphics.ARC_COUNTER_CLOCKWISE, 300, 60);
            dc.drawArc(d / 2 - off, cy, r, Graphics.ARC_COUNTER_CLOCKWISE, 120, 240);
        }
    }

    var _eigen as WatchUi.FontResource or Null = null;

    const GROOT_LIJST = [Graphics.FONT_NUMBER_THAI_HOT, Graphics.FONT_NUMBER_HOT, Graphics.FONT_NUMBER_MEDIUM, Graphics.FONT_NUMBER_MILD] as Array<Graphics.FontDefinition>;
}
