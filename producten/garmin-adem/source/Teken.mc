import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;
import Toybox.Math;
import Toybox.System;

// Uiterlijk volgens de schets van Mila (ontwerp/garmin/tij-stijl.md en ontwerp/garmin/bron/ebb_schets.py).
// Alle maten als deel van de diameter D, alleen MIP-kleuren, geen verloop.
module EbbTeken {
    // Besluit hoofdchat 11 nov 04:30: onder elk eindscherm de week. Eén stip per sessie van het weekdoel (2 tot 7),
    // gevuld wat je deze week deed, en de regel "3 weeks in a row" of, zonder reeks, "2 of 3 this week".
    // Beelden run 42955254555 (FR255): vaste hoogtes lieten stippen en regels overlappen. Nu volgt alles uit de
    // letterhoogte: stippen 4 px onder boven (de onderkant van de regel erboven), de weekregel 4 px onder de stippen.
    function weekStippen(dc as Graphics.Dc, d as Number, reeks as Number, dezeWeek as Number, doel as Number, boven as Number) as Void {
        var r = (d * 0.014).toNumber();
        r = r < 3 ? 3 : r;
        var stap = (d * 0.05).toNumber();
        var sy = boven + 4 + r;
        dc.setPenWidth(r / 2 > 1 ? r / 2 : 1);
        for (var i = 0; i < doel; i += 1) {
            var sx = d / 2 + ((2 * i - (doel - 1)) * stap) / 2;
            if (i < dezeWeek) {
                dc.setColor(SCHUIM, SCHUIM);
                dc.fillCircle(sx, sy, r);
            } else {
                dc.setColor(SCHUIM, Graphics.COLOR_TRANSPARENT);
                dc.drawCircle(sx, sy, r);
            }
        }
        dc.setPenWidth(1);
        var label = "";
        if (reeks >= 1) {
            label = reeks + (reeks == 1 ? " week in a row" : " weeks in a row");
        } else {
            var n = dezeWeek < doel ? dezeWeek : doel;
            label = n + " of " + doel + " this week";
        }
        var f = Graphics.FONT_XTINY;
        dc.setColor(LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, sy + r + 4, f, label, Graphics.TEXT_JUSTIFY_CENTER);
    }

    const SCHUIM = 0x55FFFF;
    const ZACHT = 0x55AAAA;
    const BEL = 0x55AAFF;
    const KORAAL = 0xFF5555;
    const LICHT = 0xFFFFAA;
    // Boven dit peil raakt het lichte water het fasewoord bovenaan; dan wordt het woord donkerblauw.
    const PEIL_DONKER = 0.74;
    // Daan bouwkeuring 1 B1: ademen en rustig in het blauw van het blad (00AAFF), niet turkoois.
    const DIEPTE = [0x00AAFF, 0x0055AA, 0x0000AA, 0x000055] as Array<Number>;
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

    // Grootste cijferletter waarvan de cijfers (ascent) niet hoger zijn dan 40% van D
    // en waarin "0:00" niet breder is dan 72% van D, zodat niets buiten de cirkel valt.
    // Eerst kozen we op getFontHeight, maar die telt ruimte onder de letter mee en
    // verschilt per horloge; op de epix2pro47mm viel het cijfer zo op 29%.
    // Haalt de grootste systeemletter geen 30% van D (epix2pro47mm: 123 van 416 px), dan de eigen cijferletter
    // (resources-<horloge>/fonts, 130 px op 416), één keer geladen.
    // Keuring bouw 1 punt 3 en Daan D1: het grote getal altijd in Ebbs eigen letter (Barlow Condensed Medium, OFL),
    // per schermmaat een eigen maat (resources: 260 82 px, 390 123 px, 416 130 px, 454 143 px, ±31 procent van D),
    // zodat Ebb niet als een standaard Garmin-scherm oogt en "0:00" overal binnen 72 procent van de breedte past.
    function grootFont(dc as Graphics.Dc, d as Number) as Graphics.FontType {
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
        if (amoled()) {
            zeeVerloop(dc, d, banden, pct, fase);
            return;
        }
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

    // Daan B6 en D3, keuring bouw 1 punt 4: op AMOLED een zacht verloop in plaats van rechte banden. Onder de bovenste golf
    // (met schuimkam) 18 smalle stroken met een lichte golf, de kleur loopt geleidelijk van band naar band.
    const VERLOOP_STROKEN = 18;
    function zeeVerloop(dc as Graphics.Dc, d as Number, banden as Array<Number>, pct as Number, fase as Float) as Void {
        var top = banden[0] / 100.0;
        var kleur0 = dimmer(ZEE_KLEUR[banden[1]], pct);
        golf(dc, d, top, d * 0.014, kleur0, fase, true);
        var n = banden.size() / 2;
        for (var j = 1; j < VERLOOP_STROKEN; j += 1) {
            var y = top + (1.0 - top) * j / VERLOOP_STROKEN;
            // Band waarin y valt, en hoe ver naar de volgende grens (de laatste band loopt door tot 000055).
            var b = 0;
            while (b + 1 < n && banden[2 * (b + 1)] / 100.0 <= y) {
                b += 1;
            }
            var van = banden[2 * b] / 100.0;
            var tot = (b + 1 < n) ? banden[2 * (b + 1)] / 100.0 : 1.0;
            var k1 = ZEE_KLEUR[banden[2 * b + 1]];
            var k2 = (b + 1 < n) ? ZEE_KLEUR[banden[2 * (b + 1) + 1]] : ZEE_KLEUR[3];
            var f = (tot > van) ? (y - van) / (tot - van) : 0.0;
            golf(dc, d, y, d * 0.004, dimmer(meng(k1, k2, f), pct), fase + 0.35 * j, false);
        }
    }

    // Kleur tussen a (f = 0) en b (f = 1).
    function meng(a as Number, b as Number, f as Float) as Number {
        var r = (((a >> 16) & 0xFF) * (1.0 - f) + ((b >> 16) & 0xFF) * f).toNumber();
        var g = (((a >> 8) & 0xFF) * (1.0 - f) + ((b >> 8) & 0xFF) * f).toNumber();
        var c = ((a & 0xFF) * (1.0 - f) + (b & 0xFF) * f).toNumber();
        return (r << 16) | (g << 8) | c;
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

    // Blad v6 scherm 2 en 5 (keuring bouw 1 punt 5, Daan B2): zee onderaan die zacht mee ademt. water 0 (uit) tot 1 (in):
    // bovenkant van 0,68 D naar 0,60 D, golf 0,012 D, dus de hoogste golftop is 0,588 D en het grote getal (midden 0,39 D)
    // blijft er altijd boven. Bovenste band 00AAFF, daaronder 0055AA (daar staat de ondertekst, wit haalt 6:1), onderin 0000AA.
    const ADEM_TOP = 0.68;
    const ADEM_SLAG = 0.08;
    const ADEM_AMP = 0.012;
    function ademZee(dc as Graphics.Dc, d as Number, water as Float, fase as Float) as Void {
        var top = ADEM_TOP - ADEM_SLAG * water;
        golf(dc, d, top, d * ADEM_AMP, ZEE_KLEUR[0], fase, true);
        golf(dc, d, top + 0.09, d * 0.007, ZEE_KLEUR[1], fase + 1.7, false);
        golf(dc, d, 0.93, d * 0.006, ZEE_KLEUR[2], fase + 2.9, false);
    }

    // Blad v6.4: dunne zeestrook onderaan (today, 8 weeks, settings, veiligheid), zodat elk scherm bij dezelfde zee hoort.
    const STROOK_TOP = 0.877;   // hoogste golftop van de strook (0,885 min amplitude 0,008)
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

    // Blad v7: staven van today en 8 weeks in 00AAFF op MIP (0055AA haalde maar 2,9:1), op AMOLED 0055AA zoals blad v6.
    function staafKleur() as Number {
        return amoled() ? ZEE_KLEUR[1] : ZEE_KLEUR[0];
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

    // Blad v6 punt 3: twee gespiegelde trilboogjes links en rechts van een regel van breedte breed; blad v7 punt 7: wit.
    function trilboog(dc as Graphics.Dc, d as Number, cy as Number, breed as Number) as Void {
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
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
