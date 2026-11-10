import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;
import Toybox.Math;

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

    var _eigen as WatchUi.FontResource or Null = null;

    const GROOT_LIJST = [Graphics.FONT_NUMBER_THAI_HOT, Graphics.FONT_NUMBER_HOT, Graphics.FONT_NUMBER_MEDIUM, Graphics.FONT_NUMBER_MILD] as Array<Graphics.FontDefinition>;
}
