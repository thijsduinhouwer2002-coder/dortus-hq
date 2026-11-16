import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// Alle letters op het scherm: de stripletter met zwarte rand, de regel onderaan, de knophint,
// de kreet bij een slok en het eindscherm. Afgesplitst van SpelView.mc (regel van 400).
module Letters {
    // Twaalf plekken rondom voor de zwarte rand van 2 px.
    const RAND = [-2, 0, 2, 0, 0, -2, 0, 2, -2, -1, -2, 1, 2, -1, 2, 1, -1, -2, 1, -2, -1, 2, 1, 2] as Array<Number>;

    // Tekst met een zwarte rand van 2 px (stripletter), zodat hij op elke ondergrond te lezen is
    // (moet van Daan, wens van Mila). Op AMOLED (320 en breder) is het systeemfont dun: daar staat
    // de kleur twee keer, op x en x + 1 (nep-vet, moet van Mila 16 nov 07:55), met de rand eromheen.
    function tekst(dc as Graphics.Dc, x as Number, y as Number, font as Graphics.FontDefinition, s as String, uitlijning as Graphics.TextJustification, kleur as Number) as Void {
        var vet = (dc.getWidth() >= 320);
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < 24; i += 2) {
            dc.drawText(x + RAND[i], y + RAND[i + 1], font, s, uitlijning);
        }
        if (vet) {
            dc.drawText(x + 3, y - 1, font, s, uitlijning);
            dc.drawText(x + 3, y, font, s, uitlijning);
            dc.drawText(x + 3, y + 1, font, s, uitlijning);
        }
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x, y, font, s, uitlijning);
        if (vet) {
            dc.drawText(x + 1, y, font, s, uitlijning);
        }
    }

    // De regel onderaan ("START = GULP", "START = AGAIN"). Op een rond scherm is het onderaan smal:
    // past de regel daar niet tussen de randen (gezien op de Venu 3S), dan schuift hij omhoog tot
    // hij past, hooguit tot 0,80 van de hoogte.
    function onderregel(dc as Graphics.Dc, w as Number, h as Number, s as String) as Void {
        var font = Graphics.FONT_XTINY;
        var y = (h * 0.895).toNumber();
        if (System.getDeviceSettings().screenShape == System.SCREEN_SHAPE_ROUND) {
            var nodig = dc.getTextWidthInPixels(s, font) + 16;
            var fh = dc.getFontHeight(font);
            var r = h / 2;
            var grens = (h * 0.80).toNumber();
            while (y > grens) {
                var dy = y + fh - r;
                var kwadraat = r * r - dy * dy;
                if (kwadraat > 0 && 2.0 * Math.sqrt(kwadraat) >= nodig) {
                    break;
                }
                y -= 2;
            }
        }
        tekst(dc, w / 2, y, font, s, Graphics.TEXT_JUSTIFY_CENTER, 0xFFFFFF);
    }

    // Wit boogje naast de START-knop (rechtsboven, alleen op ronde schermen) en, tijdens het spel,
    // het woord GULP erbij. Op het startscherm alleen het boogje.
    function knopHint(dc as Graphics.Dc, w as Number, h as Number, metWoord as Boolean) as Void {
        if (System.getDeviceSettings().screenShape == System.SCREEN_SHAPE_ROUND) {
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(5);
            dc.drawArc(w / 2, h / 2, w / 2 - 13, Graphics.ARC_CLOCKWISE, 48, 22);
            dc.setPenWidth(1);
        }
        if (metWoord) {
            tekst(dc, (w * 0.79).toNumber(), (h * 0.27).toNumber(), Graphics.FONT_XTINY, "GULP", Graphics.TEXT_JUSTIFY_CENTER, 0xFFFFFF);
        }
    }

    // De kreet bij een slok, links van de toren waar net de held viel. Past hij niet in de ruimte
    // (breed systeemfont, lange reeks), dan liever twee regels in het grotere font dan één regel
    // piepklein; lukt dat ook niet, dan een maat kleiner.
    function kreet(dc as Graphics.Dc, w as Number, h as Number, spel as Spel, ruimte as Number) as Void {
        var reeks = (spel.raak && spel.reeks >= 3);
        var s = spel.raak ? "GULP!" : "gulp";
        if (reeks) {
            s = "GULP! x" + spel.reeks;
        }
        var kx = (w * 0.05).toNumber();
        var ky = (h * 0.40).toNumber();
        var kfont = Graphics.FONT_SMALL;
        var tweeRegels = false;
        if (dc.getTextWidthInPixels(s, kfont) > ruimte) {
            if (reeks && dc.getTextWidthInPixels("GULP!", kfont) <= ruimte) {
                tweeRegels = true;
            } else {
                kfont = Graphics.FONT_XTINY;
                tweeRegels = (dc.getTextWidthInPixels(s, kfont) > ruimte && reeks);
            }
        }
        if (tweeRegels) {
            tekst(dc, kx, ky - dc.getFontHeight(kfont) / 2, kfont, "GULP!", Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
            tekst(dc, kx, ky + dc.getFontHeight(kfont) / 2, kfont, "x" + spel.reeks, Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
        } else {
            tekst(dc, kx, ky, kfont, s, Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
        }
    }

    // Eindscherm. Moet van Daan (16 nov 06:45): "START = AGAIN" stond over het gezicht van Gloop.
    // De regel staat in de zwarte balk onder "BEST 15", zodat het gezicht vrij blijft. Past dat niet
    // boven Gloop (de balk mag niet lager komen dan tot), dan de oude plek onderaan met de rand.
    function eindscherm(dc as Graphics.Dc, w as Number, h as Number, spel as Spel, tot as Number) as Void {
        var midden = Graphics.TEXT_JUSTIFY_CENTER;
        var cx = w / 2;
        var regel = spel.nieuwBeste ? "NEW BEST!" : "BEST " + spel.beste;
        var y1 = (h * 0.17).toNumber();
        var y2 = y1 + (dc.getFontHeight(Graphics.FONT_MEDIUM) * 0.85).toNumber();
        var y3 = y2 + (dc.getFontHeight(Graphics.FONT_SMALL) * 0.90).toNumber();
        var balkOnder = y3 + dc.getFontHeight(Graphics.FONT_XTINY) + 2;
        var inBalk = (balkOnder <= tot);
        if (!inBalk) {
            balkOnder = (h * 0.50).toNumber();
        }
        var balkBoven = (h * 0.16).toNumber();
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(0, balkBoven, w, balkOnder - balkBoven);
        dc.setColor(0xFFFF00, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, y1, Graphics.FONT_MEDIUM, spel.hoeden + " HATS", midden);
        dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, y2, Graphics.FONT_SMALL, regel, midden);
        if (inBalk) {
            dc.setColor(0xAAAAAA, Graphics.COLOR_TRANSPARENT);
            dc.drawText(cx, y3, Graphics.FONT_XTINY, "START = AGAIN", midden);
        } else {
            onderregel(dc, w, h, "START = AGAIN");
        }
    }
}
