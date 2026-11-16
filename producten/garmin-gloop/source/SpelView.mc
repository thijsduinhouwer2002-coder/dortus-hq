import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Timer;
import Toybox.WatchUi;

typedef Plaatje as WatchUi.BitmapResource or Graphics.BitmapReference;

// Het scherm van het spel, met de spritekit van Mila (keuze (c) van Daan en Mila, 16 nov):
// Gloop staat in het midden met de hoedentoren op zijn kop, de held valt schuin van linksboven
// door een lichtbaan naar zijn bek. Rondom loopt de tijd.
class SpelView extends WatchUi.View {
    var spel as Spel;
    var klok as Timer.Timer?;
    var vorige as Number = 0;
    var wasEinde as Boolean = false;
    var lietLopen as Boolean = false;
    // Korte stilstand precies op het slikken (kan 5 van Daan, ja van Mila): alles bevriest even,
    // ook de klok van het potje, dus het tempo en de regels in Spel.mc blijven gelijk.
    const STILSTAND_MS = 80;
    var stilstand as Number = 0;
    var vorigeToestand as Number = Regel.KLAAR;

    // Plaatjes: 0 rust, 1 hap, 2 blij, 3 slok, 4 held, 5 vliegende helm, 6 tot 15 de tien hoeden, 16 de titel.
    var pl as Array<Plaatje> = [] as Array<Plaatje>;
    // Maten en ankers van de plaatjes (zie Maten.mc).
    var m as Array<Number> = [] as Array<Number>;
    // Welke hoed op welke plek in de toren komt: begint met de kroon, zoals op het blad van Mila.
    const VOLGORDE = [4, 1, 9, 5, 2, 0, 6, 7, 3, 8] as Array<Number>;

    function initialize(hetSpel as Spel) {
        View.initialize();
        spel = hetSpel;
    }

    function onLayout(dc as Graphics.Dc) as Void {
        m = Maten.voor(dc.getWidth());
        pl = [
            WatchUi.loadResource(Rez.Drawables.GloopRust) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.GloopHap) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.GloopBlij) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.GloopSlok) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.HeldVal) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.HelmVlieg) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed0) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed1) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed2) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed3) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed4) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed5) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed6) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed7) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed8) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed9) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Titel) as Plaatje
        ] as Array<Plaatje>;
    }

    function onShow() as Void {
        vorige = System.getTimer();
        var k = new Timer.Timer();
        k.start(method(:opTik), 50, true);
        klok = k;
    }

    function onHide() as Void {
        var k = klok;
        if (k != null) {
            k.stop();
        }
        klok = null;
    }

    function opTik() as Void {
        var nu = System.getTimer();
        var dt = nu - vorige;
        vorige = nu;
        if (dt < 0) {
            dt = 0;
        }
        if (dt > 200) {
            dt = 200;
        }
        if (Bouw.AUTO) {
            speelZelf();
        }
        if (stilstand > 0) {
            stilstand -= dt;
        } else {
            spel.tik(dt);
        }
        if (spel.toestand == Regel.SLOK && vorigeToestand != Regel.SLOK) {
            stilstand = STILSTAND_MS;
            if (Bouw.AUTO && (spel.hoeden == 3 || spel.hoeden == 8 || spel.hoeden == 12)) {
                // Alleen in de bouwstraat: hetzelfde slokbeeld langer vasthouden, zodat de camera
                // (één foto per 1,5 s) het zeker pakt. In het echte spel is het 0,08 s.
                stilstand = 1700;
            }
        }
        vorigeToestand = spel.toestand;
        var einde = (spel.toestand == Regel.EINDE);
        if (einde && !wasEinde && spel.nieuwBeste) {
            Application.Storage.setValue("beste", spel.beste);
        }
        wasEinde = einde;
        WatchUi.requestUpdate();
    }

    // Alleen voor de bouwstraat: drukt zelf, en laat expres één held lopen (bij 4 hoeden),
    // zodat "bye!" in beeld komt en de toren toch over de rand groeit.
    function speelZelf() as Void {
        if (spel.toestand == Regel.KLAAR && spel.fase > 6000) {
            lietLopen = false;
            spel.druk();
        } else if (spel.toestand == Regel.WEG) {
            lietLopen = true;
        } else if (spel.toestand == Regel.VALT && spel.y >= Regel.RAAK_BOVEN && (lietLopen || spel.hoeden != 4)) {
            spel.druk();
        } else if (spel.toestand == Regel.EINDE && spel.fase > 6000) {
            spel.druk();
        }
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        if (pl.size() < 17) {
            return;
        }
        var w = dc.getWidth();
        var h = dc.getHeight();
        var cx = w / 2;
        var voet = (h * 0.90).toNumber();
        var midden = Graphics.TEXT_JUSTIFY_CENTER;

        // Grot, lichtbaan van linksboven naar de bek, vloer. Effen kleuren uit het MIP-palet.
        dc.setColor(0xAA5500, 0xAA5500);
        dc.clear();
        var d = (w * 0.11).toNumber();
        var ax = (w * -0.03).toNumber();
        var ay = (h * -0.10).toNumber();
        var bx = (w * 0.38).toNumber();
        var by = (h * 0.74).toNumber();
        if (w >= 320) {
            // AMOLED: zachtere kleur en een rand in twee stappen (kan van Daan, maat van Mila: 226,162,92).
            var r2 = (d * 1.24).toNumber();
            var r1 = (d * 1.12).toNumber();
            dc.setColor(0xBD6F1F, Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon([[ax - r2, ay], [ax + r2, ay], [bx + r2, by], [bx - r2, by]] as Array<Graphics.Point2D>);
            dc.setColor(0xCF883D, Graphics.COLOR_TRANSPARENT);
            dc.fillPolygon([[ax - r1, ay], [ax + r1, ay], [bx + r1, by], [bx - r1, by]] as Array<Graphics.Point2D>);
            dc.setColor(0xE2A25C, Graphics.COLOR_TRANSPARENT);
        } else {
            // MIP: effen, geen tussenkleuren.
            dc.setColor(0xFFAA55, Graphics.COLOR_TRANSPARENT);
        }
        dc.fillPolygon([[ax - d, ay], [ax + d, ay], [bx + d, by], [bx - d, by]] as Array<Graphics.Point2D>);
        dc.setColor(0x550000, Graphics.COLOR_TRANSPARENT);
        dc.fillEllipse(cx, h, (w * 0.80).toNumber(), (h * 0.16).toNumber());

        // De toren begint op de kruin van Gloop (anker uit de kit).
        var torenX = cx - m[0] / 2 + m[10];
        var kruinY = voet - m[1] + m[11];
        var n = spel.hoeden;
        if (spel.toestand == Regel.SLOK) {
            n -= 1; // de nieuwste hoed is nog onderweg
        }

        tekenGloop(dc, cx, voet);
        var top = tekenToren(dc, torenX, kruinY, n);
        tekenHeld(dc, w, h, voet);
        tekenVliegendeHelm(dc, w, h, cx, voet, torenX, top);
        tekenTijd(dc, w, h);

        if (spel.toestand == Regel.KLAAR) {
            // Titelplaatje van Mila ("GLOOP / HAT TOWER") in plaats van het dunne systeemfont:
            // bovenkant op 0,08 van de hoogte (anker uit de kit), en 0,07 van de breedte naar links:
            // in het midden raakte "HAT TOWER" het woord GULP van de knophint (gezien op FR255,
            // Venu 3S en Venu Sq 2, run 43820999649).
            var tx = cx - m[32] / 2 - (w * 0.07).toNumber();
            dc.drawBitmap(tx, (h * 0.08).toNumber(), pl[16]);
            tekenOnderregel(dc, w, h, "START = GULP");
            tekenKnopHint(dc, w, h);
        } else if (spel.toestand == Regel.EINDE) {
            // Eindscherm. Moet van Daan (16 nov 06:45): "START = AGAIN" stond over het gezicht van Gloop.
            // De regel staat nu in de zwarte balk onder "BEST 15", zodat het gezicht vrij blijft.
            // Past dat niet boven Gloop (balk zou over zijn kop komen), dan de oude plek onderaan,
            // met de donkere rand van 2 px.
            var regel = spel.nieuwBeste ? "NEW BEST!" : "BEST " + spel.beste;
            var y1 = (h * 0.17).toNumber();
            var y2 = y1 + (dc.getFontHeight(Graphics.FONT_MEDIUM) * 0.85).toNumber();
            var y3 = y2 + (dc.getFontHeight(Graphics.FONT_SMALL) * 0.90).toNumber();
            var balkOnder = y3 + dc.getFontHeight(Graphics.FONT_XTINY) + 2;
            var inBalk = (balkOnder <= voet - m[3] - 4);
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
                tekenOnderregel(dc, w, h, "START = AGAIN");
            }
        } else {
            tekenTeller(dc, w, h, top);
            if (spel.toestand == Regel.SLOK) {
                var kreet = spel.raak ? "GULP!" : "gulp";
                if (spel.raak && spel.reeks >= 3) {
                    kreet = "GULP! x" + spel.reeks;
                }
                // Links van de toren, waar net de held viel.
                // Past de kreet niet links van de toren (breed systeemfont, lange reeks), dan een maat kleiner.
                // Moet van Daan: altijd minstens 8 px lucht tussen de kreet en de toren. Past hij ook
                // klein niet op één regel, dan staat de reeks ("x7") op een tweede regel.
                var kx = (w * 0.05).toNumber();
                var ky = (h * 0.40).toNumber();
                var ruimte = torenX - m[12] / 2 - 2 - 8 - kx - 1;
                var kfont = Graphics.FONT_SMALL;
                var tweeRegels = false;
                if (dc.getTextWidthInPixels(kreet, kfont) > ruimte) {
                    if (spel.raak && spel.reeks >= 3 && dc.getTextWidthInPixels("GULP!", kfont) <= ruimte) {
                        // Liever twee regels in het grotere font dan één regel piepklein (260 en 280).
                        tweeRegels = true;
                    } else {
                        kfont = Graphics.FONT_XTINY;
                        tweeRegels = (dc.getTextWidthInPixels(kreet, kfont) > ruimte && spel.raak && spel.reeks >= 3);
                    }
                }
                if (tweeRegels) {
                    tekst(dc, kx, ky - dc.getFontHeight(kfont) / 2, kfont, "GULP!", Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
                    tekst(dc, kx, ky + dc.getFontHeight(kfont) / 2, kfont, "x" + spel.reeks, Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
                } else {
                    tekst(dc, kx, ky, kfont, kreet, Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF00);
                }
            } else if (spel.toestand == Regel.WEG) {
                tekst(dc, (w * 0.05).toNumber(), (h * 0.40).toNumber(), Graphics.FONT_XTINY, "bye!", Graphics.TEXT_JUSTIFY_LEFT, 0xFFFFFF);
            } else if (spel.toestand == Regel.VALT) {
                tekenKnopHint(dc, w, h);
            }
        }
    }

    // De regel onderaan ("START = GULP", "START = AGAIN"). Op een rond scherm is het onderaan smal:
    // past de regel daar niet tussen de randen (gezien op de Venu 3S: "START = AGAIN" viel links en
    // rechts buiten beeld), dan schuift hij omhoog tot hij past, hooguit tot 0,80 van de hoogte.
    function tekenOnderregel(dc as Graphics.Dc, w as Number, h as Number, s as String) as Void {
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

    // Tekst met een zwarte rand van 2 px (stripletter), zodat hij op elke ondergrond te lezen is:
    // moet van Daan voor "START = AGAIN" en wens van Mila voor alle teksten op het speelveld
    // ("GULP! x3" viel weg in de lichtbaan). Twaalf keer zwart rondom, dan de kleur erop.
    const RAND = [-2, 0, 2, 0, 0, -2, 0, 2, -2, -1, -2, 1, 2, -1, 2, 1, -1, -2, 1, -2, -1, 2, 1, 2] as Array<Number>;

    function tekst(dc as Graphics.Dc, x as Number, y as Number, font as Graphics.FontDefinition, s as String, uitlijning as Graphics.TextJustification, kleur as Number) as Void {
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < 24; i += 2) {
            dc.drawText(x + RAND[i], y + RAND[i + 1], font, s, uitlijning);
        }
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x, y, font, s, uitlijning);
    }

    // Gloop staat met zijn voet op 0,90 van het scherm; elk plaatje hangt aan die voet.
    function tekenGloop(dc as Graphics.Dc, cx as Number, voet as Number) as Void {
        var t = spel.toestand;
        if (t == Regel.SLOK) {
            // De slokplaat van Mila is even groot als de hap en staat op dezelfde plek.
            dc.drawBitmap(cx - m[0] / 2, voet - m[5], pl[3]);
        } else if (t == Regel.VALT && spel.inVangzone() && spel.hapDicht == 0) {
            dc.drawBitmap(cx - m[0] / 2, voet - m[2], pl[1]);
        } else if (t == Regel.EINDE || (t == Regel.WACHT && spel.reeks > 0)) {
            dc.drawBitmap(cx - m[0] / 2, voet - m[3], pl[2]);
        } else {
            dc.drawBitmap(cx - m[0] / 2, voet - m[1], pl[0]);
        }
    }

    // Stapelt n hoeden op de kruin. Elke hoed staat 0,56 keer zijn eigen hoogte hoger (regel van Mila).
    // Geeft de hoogte terug waar de volgende hoed op komt te staan.
    function tekenToren(dc as Graphics.Dc, torenX as Number, kruinY as Number, n as Number) as Number {
        var y = kruinY.toFloat();
        for (var i = 0; i < n; i += 1) {
            var k = VOLGORDE[i % 10];
            var hb = m[12 + 2 * k];
            var hh = m[13 + 2 * k];
            var boven = y - hh * 0.78;
            if (boven + hh > 0) {
                // De toren wiebelt een beetje: elke hoed een paar pixels opzij.
                var dx = ((i * 7) % 5) - 2;
                dc.drawBitmap(torenX - hb / 2 + dx, boven.toNumber(), pl[6 + k]);
            }
            y = boven + hh * 0.22;
        }
        return y.toNumber();
    }

    // De held volgt de lichtbaan: bij een voltreffer (y = 815) hangt zijn hoofd bij de bek.
    function tekenHeld(dc as Graphics.Dc, w as Number, h as Number, voet as Number) as Void {
        if (spel.toestand == Regel.VALT) {
            var t = spel.y / 815.0;
            var hx = (w * (0.04 + 0.34 * t)).toNumber();
            var hy = (h * 0.72 * t).toNumber();
            dc.drawBitmap(hx - m[6] / 2, hy - m[7] / 2, pl[4]);
            if (spel.inVangzone() && spel.hapDicht == 0) {
                tekst(dc, hx - m[6] / 2, hy - m[7] / 2 - 4, Graphics.FONT_MEDIUM, "!", Graphics.TEXT_JUSTIFY_RIGHT, 0xFFFF00);
            }
        } else if (spel.toestand == Regel.WEG) {
            // Gemist: hij glijdt langs Gloop naar links het beeld uit.
            var x = (w * 0.30).toNumber() - ((w * 0.30 + m[6]) * spel.fase / Regel.WEG_MS).toNumber();
            dc.drawBitmap(x, voet - m[7], pl[4]);
        }
    }

    // Bij de slok schiet de helm van boven de kruin in een boog naar rechts en landt boven op de toren.
    function tekenVliegendeHelm(dc as Graphics.Dc, w as Number, h as Number, cx as Number, voet as Number, torenX as Number, top as Number) as Void {
        if (spel.toestand != Regel.SLOK) {
            return;
        }
        var f = spel.fase.toFloat() / Regel.SLOK_MS;
        if (f > 1.0) {
            f = 1.0;
        }
        // Begint boven de kruin, zodat de helm nooit over het oog of de mond ligt (moet van Mila en Daan).
        var begin = voet - m[1] - m[9] / 2;
        var eind = top - m[9] / 2;
        if (eind < m[9] / 2) {
            eind = m[9] / 2;
        }
        // Staat de teller rechts naast een hoge toren, dan vliegt de helm links om (kan van Daan),
        // zodat hij niet over het kroontje van de teller gaat.
        var kant = (top < h * 0.24) ? -1.0 : 1.0;
        var x = cx + ((torenX - cx) * f).toNumber() + (kant * w * 0.22 * 4.0 * f * (1.0 - f)).toNumber();
        var y = begin + ((eind - begin) * f).toNumber();
        dc.drawBitmap(x - m[8] / 2, y - m[9] / 2, pl[5]);
    }

    // Teller bovenaan: de kroon en het aantal hoeden.
    // Komt de toren zo hoog dat hij de teller raakt, dan wijkt de teller uit naar rechts in het midden.
    function tekenTeller(dc as Graphics.Dc, w as Number, h as Number, top as Number) as Void {
        var hoog = (top < h * 0.24);
        var s = spel.hoeden.toString();
        var font = Graphics.FONT_MEDIUM;
        var tb = dc.getTextWidthInPixels(s, font);
        var kb = m[20];
        var kh = m[21];
        var x0 = (hoog ? (w * 0.78).toNumber() : w / 2) - (tb + kb + 4) / 2;
        var my = (h * (hoog ? 0.50 : 0.12)).toNumber();
        dc.drawBitmap(x0, my - kh / 2, pl[10]);
        tekst(dc, x0 + kb + 4, my - dc.getFontHeight(font) / 2, font, s, Graphics.TEXT_JUSTIFY_LEFT, 0xFFFF55);
    }

    // Boogje en het woord GULP naast de START-knop (rechtsboven). Op vierkante schermen alleen het woord.
    function tekenKnopHint(dc as Graphics.Dc, w as Number, h as Number) as Void {
        if (System.getDeviceSettings().screenShape == System.SCREEN_SHAPE_ROUND) {
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(5);
            dc.drawArc(w / 2, h / 2, w / 2 - 13, Graphics.ARC_CLOCKWISE, 48, 22);
            dc.setPenWidth(1);
        }
        tekst(dc, (w * 0.79).toNumber(), (h * 0.27).toNumber(), Graphics.FONT_XTINY, "GULP", Graphics.TEXT_JUSTIFY_CENTER, 0xFFFFFF);
    }

    function tekenTijd(dc as Graphics.Dc, w as Number, h as Number) as Void {
        if (spel.toestand == Regel.KLAAR || spel.toestand == Regel.EINDE) {
            return;
        }
        var graden = (360.0 * spel.tijdOver / Regel.RONDE_MS).toNumber();
        if (graden < 1) {
            return;
        }
        var r = ((w < h) ? w : h) / 2 - 4;
        // De klok is goudgeel (wit is de knophint), de laatste 5 seconden rood.
        dc.setColor(spel.tijdOver < 5000 ? 0xFF0000 : 0xFFAA00, Graphics.COLOR_TRANSPARENT);
        if (System.getDeviceSettings().screenShape != System.SCREEN_SHAPE_ROUND) {
            // Vierkant scherm: de klok is een balk langs de bovenrand die leegloopt.
            dc.fillRectangle(0, 0, (w * spel.tijdOver / Regel.RONDE_MS).toNumber(), 9);
            return;
        }
        dc.setPenWidth(5);
        if (graden >= 360) {
            dc.drawCircle(w / 2, h / 2, r);
        } else {
            dc.drawArc(w / 2, h / 2, r, Graphics.ARC_CLOCKWISE, 90, (450 - graden) % 360);
        }
        dc.setPenWidth(1);
    }
}
