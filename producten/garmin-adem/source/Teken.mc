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
            // schildpad: schild, kop en vier pootjes
            dc.fillEllipse(cx, cy, r, (r * 7) / 10);
            dc.fillCircle(cx - r - r / 3, cy, r / 3);
            dc.fillCircle(cx - r / 2, cy - (r * 7) / 10, r / 4);
            dc.fillCircle(cx + r / 2, cy - (r * 7) / 10, r / 4);
            dc.fillCircle(cx - r / 2, cy + (r * 7) / 10, r / 4);
            dc.fillCircle(cx + r / 2, cy + (r * 7) / 10, r / 4);
        } else {
            // walvis in de verte: groot lijf en staart omhoog
            var rw = (r * 18) / 10;
            dc.fillEllipse(cx, cy, rw, (rw * 5) / 10);
            dc.fillPolygon([[cx + rw - 3, cy], [cx + rw + rw / 2, cy - rw / 2], [cx + rw + rw / 3, cy + 2]]);
        }
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
