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
    // letterhoogte. Mila blad v13: sy is het midden van de stippen (180/260 D, plus een tweede naamregel); de weekregel
    // staat er vlak onder (het vak van de letter begint 1 px onder de stippen, de letters zelf een paar px lager).
    function weekStippen(dc as Graphics.Dc, d as Number, reeks as Number, dezeWeek as Number, doel as Number, sy as Number) as Void {
        var r = (d * 0.014).toNumber();
        r = r < 3 ? 3 : r;
        var stap = (d * 0.05).toNumber();
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
        // Reeks -1: de bonus (zeekomkommer) is net gevonden, die komt na een pauze (Mila blad v11 punt 1).
        if (reeks < 0) {
            label = "back after a break";
        } else if (reeks >= 1) {
            label = reeks + (reeks == 1 ? " week in a row" : " weeks in a row");
        } else {
            var n = dezeWeek < doel ? dezeWeek : doel;
            label = n + " of " + doel + " this week";
        }
        var f = EbbTeken.fX();
        dc.setColor(LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, sy + r + 1, f, label, Graphics.TEXT_JUSTIFY_CENTER);
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

    // Besluit 11 nov 09:30 punt 2: de tijd tijdens inhouden in 80 procent van de cijferletter (bron/maak_cijfers.py),
    // zodat het eigen dier 90 x 70 (454) en 50 x 40 (260) krijgt.
    var _eigenKlein as WatchUi.FontResource or Null = null;

    function grootKlein() as Graphics.FontType {
        if (_eigenKlein == null) {
            _eigenKlein = WatchUi.loadResource(Rez.Fonts.EbbCijfersKlein) as WatchUi.FontResource;
        }
        return _eigenKlein as WatchUi.FontResource;
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




    // Kleur tussen a (f = 0) en b (f = 1).
    function meng(a as Number, b as Number, f as Float) as Number {
        var r = (((a >> 16) & 0xFF) * (1.0 - f) + ((b >> 16) & 0xFF) * f).toNumber();
        var g = (((a >> 8) & 0xFF) * (1.0 - f) + ((b >> 8) & 0xFF) * f).toNumber();
        var c = ((a & 0xFF) * (1.0 - f) + (b & 0xFF) * f).toNumber();
        return (r << 16) | (g << 8) | c;
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
        var font = EbbTeken.fX();
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

    // Keuring bouw 4 punt 4: alle tekst in Barlow Condensed (OFL), per schermmaat gemaakt met bron/maak_letters.py,
    // met dezelfde regelhoogte als FONT_XTINY, FONT_SMALL en FONT_MEDIUM op dat horloge. Eén keer geladen.
    var _x as WatchUi.FontResource or Null = null;
    var _s as WatchUi.FontResource or Null = null;
    var _m as WatchUi.FontResource or Null = null;

    // Besluit hoofdchat 11 nov 09:30 punt 1: leesbaarheid gaat voor de eigen letter. Op MIP-schermen (FR255, fenix 7X,
    // fenix 8 solar) valt de kleine Barlow met grijze randen weg in het palet van 64 kleuren ("Nol if pregnant"); daar
    // gebruikt alle tekst de systeemletter, die voor dat scherm gemaakt is. Zelfde regelhoogte, dus de opmaak blijft.
    function fX() as Graphics.FontType {
        if (!amoled()) {
            return Graphics.FONT_XTINY;
        }
        if (_x == null) {
            _x = WatchUi.loadResource(Rez.Fonts.EbbXtiny) as WatchUi.FontResource;
        }
        return _x as WatchUi.FontResource;
    }

    function fS() as Graphics.FontType {
        if (!amoled()) {
            return Graphics.FONT_SMALL;
        }
        if (_s == null) {
            _s = WatchUi.loadResource(Rez.Fonts.EbbSmall) as WatchUi.FontResource;
        }
        return _s as WatchUi.FontResource;
    }

    function fM() as Graphics.FontType {
        if (!amoled()) {
            return Graphics.FONT_MEDIUM;
        }
        if (_m == null) {
            _m = WatchUi.loadResource(Rez.Fonts.EbbMedium) as WatchUi.FontResource;
        }
        return _m as WatchUi.FontResource;
    }

    // Besluit 11 nov 09:30 punt 1: veiligheid en "how it works" een maat groter op AMOLED; op MIP de systeemletter
    // XTINY (al scherp en heel, en een maat groter past niet op 260 px).
    function fLees() as Graphics.FontType {
        return amoled() ? fS() : Graphics.FONT_XTINY;
    }

    // Regelafstand voor fLees: de Barlow-regel is ruim (hoofdletters 52 procent), op AMOLED 80 procent daarvan.
    function leesRegel(dc as Graphics.Dc, f as Graphics.FontType) as Number {
        var lh = dc.getFontHeight(f);
        return amoled() ? (lh * 4) / 5 : lh;
    }

    const GROOT_LIJST = [Graphics.FONT_NUMBER_THAI_HOT, Graphics.FONT_NUMBER_HOT, Graphics.FONT_NUMBER_MEDIUM, Graphics.FONT_NUMBER_MILD] as Array<Graphics.FontDefinition>;

    // Keuring bouw 6 punt 9: gedeelde hulpen die eerst in meer schermen dubbel stonden.
    // Maat v in 1/260 van de schermdoorsnede d (Mila's bladen), afgerond.
    function px(d as Number, v as Number) as Number {
        return (v * d + 130) / 260;
    }

    // Tekst midden, met de bovenkant op y (1/260 D), zoals op het blad (sea log, sea complete).
    function tekst260(dc as Graphics.Dc, d as Number, y as Number, f as Graphics.FontType, s as String, kleur as Number) as Void {
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, px(d, y), f, s, Graphics.TEXT_JUSTIFY_CENTER);
    }

    // Tekst midden op hoogte y (deel van D); FONT_SMALL als hij binnen de koorde past (met marge), anders FONT_XTINY.
    function tekstInRonde(dc as Graphics.Dc, d as Number, y as Float, tekst as String, kleur as Number) as Void {
        var dy = y - 0.5;
        var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.86;
        var f = (dc.getTextWidthInPixels(tekst, fS()) <= koorde) ? fS() : fX();
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
