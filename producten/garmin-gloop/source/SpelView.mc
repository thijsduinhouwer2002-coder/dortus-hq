import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Timer;
import Toybox.WatchUi;

// Het scherm van de proef. Alles met eenvoudige vormen (grijze-dozen-proef):
// links de schacht met Gloop, rechts de hoedentoren, rondom de tijd.
class SpelView extends WatchUi.View {
    var spel as Spel;
    var klok as Timer.Timer?;
    var vorige as Number = 0;
    var wasEinde as Boolean = false;
    var lietLopen as Boolean = false;

    const KLEUREN = [0xFF0000, 0x0055FF, 0xFFFF00, 0xAA00FF, 0xFFFFFF, 0x00AAAA] as Array<Number>;

    function initialize(hetSpel as Spel) {
        View.initialize();
        spel = hetSpel;
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
        spel.tik(dt);
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
        if (spel.toestand == Regel.KLAAR && spel.fase > 2500) {
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
        var w = dc.getWidth();
        var h = dc.getHeight();
        var vloer = (h * 0.80).toNumber();
        var midden = Graphics.TEXT_JUSTIFY_CENTER;

        // Grot, schacht en vloer.
        dc.setColor(0xAA5500, 0xAA5500);
        dc.clear();
        var sx = (w * 0.20).toNumber();
        var sb = (w * 0.34).toNumber();
        dc.setColor(0xFFAA55, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(sx, 0, sb, vloer);
        dc.setColor(0x550000, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(0, vloer, w, h - vloer);

        var gx = sx + sb / 2;
        var gr = (w * 0.13).toNumber();
        var gy = vloer - (gr * 0.8).toNumber();

        tekenToren(dc, w, h, vloer);
        tekenHeld(dc, w, h, vloer, gx);
        tekenGloop(dc, gx, gy, gr);
        tekenSlok(dc, w, h, gx, gy, gr);
        tekenVliegendeHoed(dc, w, h, vloer, gx, gy - gr);
        tekenTijd(dc, w, h);

        dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        if (spel.toestand == Regel.KLAAR) {
            dc.drawText(w / 2, (h * 0.10).toNumber(), Graphics.FONT_MEDIUM, "GLOOP", midden);
            dc.drawText(w / 2, (h * 0.84).toNumber(), Graphics.FONT_XTINY, "START = GULP", midden);
        } else if (spel.toestand == Regel.EINDE) {
            dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
            dc.fillRectangle(0, (h * 0.16).toNumber(), w, (h * 0.34).toNumber());
            dc.setColor(0xFFFF00, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (h * 0.17).toNumber(), Graphics.FONT_MEDIUM, spel.hoeden + " HATS", midden);
            dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
            var regel = spel.nieuwBeste ? "NEW BEST!" : "BEST " + spel.beste;
            dc.drawText(w / 2, (h * 0.34).toNumber(), Graphics.FONT_SMALL, regel, midden);
            dc.drawText(w / 2, (h * 0.84).toNumber(), Graphics.FONT_XTINY, "START = AGAIN", midden);
        } else {
            dc.drawText(w / 2, (h * 0.81).toNumber(), Graphics.FONT_SMALL, spel.hoeden.toString(), midden);
            if (spel.toestand == Regel.SLOK) {
                dc.setColor(0xFFFF00, Graphics.COLOR_TRANSPARENT);
                var kreet = spel.raak ? "GULP!" : "gulp";
                if (spel.raak && spel.reeks >= 3) {
                    kreet = "GULP! x" + spel.reeks;
                }
                dc.drawText(w / 2, (h * 0.08).toNumber(), Graphics.FONT_MEDIUM, kreet, midden);
            } else if (spel.toestand == Regel.WEG) {
                dc.drawText(w / 2, (h * 0.08).toNumber(), Graphics.FONT_XTINY, "bye!", midden);
            }
        }
    }

    function tekenHoed(dc as Graphics.Dc, x as Number, y as Number, b as Number, hh as Number, kleur as Number) as Void {
        // x is het midden, y de onderkant van de hoed.
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(x - b / 2 - 1, y - hh / 3 - 1, b + 2, hh / 3 + 1);
        dc.fillRectangle(x - b / 4 - 1, y - hh, b / 2 + 2, hh);
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(x - b / 2, y - hh / 3, b, hh / 3 - 1);
        dc.fillRectangle(x - b / 4, y - hh + 1, b / 2, hh - 2);
    }

    function tekenToren(dc as Graphics.Dc, w as Number, h as Number, vloer as Number) as Void {
        var tx = (w * 0.74).toNumber();
        var hh = (h * 0.06).toNumber();
        var b = (w * 0.17).toNumber();
        var n = spel.hoeden;
        if (spel.toestand == Regel.SLOK) {
            n -= 1; // de nieuwste hoed is nog onderweg
        }
        for (var i = 0; i < n; i += 1) {
            var y = vloer - i * hh;
            if (y < 0) {
                break;
            }
            // De toren wiebelt een beetje: om en om een paar pixels opzij.
            var dx = ((i % 2) == 0) ? -1 : 2;
            tekenHoed(dc, tx + dx, y, b, hh, KLEUREN[i % 6]);
        }
    }

    function tekenHeld(dc as Graphics.Dc, w as Number, h as Number, vloer as Number, gx as Number) as Void {
        var hb = (w * 0.09).toNumber();
        var hl = (h * 0.10).toNumber();
        var x = gx;
        var onder = 0;
        if (spel.toestand == Regel.VALT) {
            onder = (spel.y / 1000.0 * vloer).toNumber();
        } else if (spel.toestand == Regel.WEG) {
            onder = vloer;
            x = gx - (w * 0.45 * spel.fase / Regel.WEG_MS).toNumber() - hb;
        } else {
            return;
        }
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(x - hb / 2 - 1, onder - hl - 1, hb + 2, hl + 2);
        dc.setColor(0xAAAAFF, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(x - hb / 2, onder - hl, hb, hl);
        tekenHoed(dc, x, onder - hl, (w * 0.13).toNumber(), (h * 0.05).toNumber(), KLEUREN[spel.held]);
    }

    function tekenGloop(dc as Graphics.Dc, gx as Number, gy as Number, gr as Number) as Void {
        var open = (spel.toestand == Regel.VALT && spel.inVangzone() && spel.hapDicht == 0);
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(gx, gy, gr + 2);
        dc.setColor(spel.toestand == Regel.SLOK ? 0xAAFF00 : 0x55FF00, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(gx, gy, gr);
        // Ogen.
        var o = gr / 3;
        // Bij de slok zakken de ogen, want de bek staat dan wijd open bovenin.
        var ey = (spel.toestand == Regel.SLOK) ? gy + o / 2 : gy - o / 2;
        dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(gx - o, ey, o / 2 + 2);
        dc.fillCircle(gx + o, ey, o / 2 + 2);
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        var kijk = (spel.toestand == Regel.VALT) ? -2 : 0;
        dc.fillCircle(gx - o, ey + kijk, o / 4 + 1);
        dc.fillCircle(gx + o, ey + kijk, o / 4 + 1);
        // Bek: wijd open als de held te pakken is, anders een streep.
        if (open) {
            dc.fillEllipse(gx, gy - gr + o, o * 2, o);
        } else if (spel.toestand == Regel.SLOK) {
            // De bek tekent tekenSlok, met de held erin.
        } else {
            dc.fillRectangle(gx - o, gy + o, o * 2, 3);
        }
    }

    // De slok (voorstel Mila, v3): de held steekt ondersteboven half uit de open bek,
    // benen omhoog, en zakt in 0,3 seconde weg. Nog met eenvoudige vormen.
    function tekenSlok(dc as Graphics.Dc, w as Number, h as Number, gx as Number, gy as Number, gr as Number) as Void {
        if (spel.toestand != Regel.SLOK) {
            return;
        }
        var hb = (w * 0.09).toNumber();
        var hl = (h * 0.10).toNumber();
        var zak = (hl * spel.fase / Regel.SLOK_MS).toNumber();
        if (zak > hl) {
            zak = hl;
        }
        var lip = gy - gr / 2;
        var zicht = hl - zak;
        // Open bek met donkere rand, bovenin de bol.
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.fillEllipse(gx, lip, hb, gr / 3);
        if (zicht > 2) {
            // Buik en twee benen die eruit steken.
            dc.fillRectangle(gx - hb / 2 - 1, lip - zicht - 1, hb + 2, zicht + 1);
            dc.setColor(0xAAAAFF, Graphics.COLOR_TRANSPARENT);
            dc.fillRectangle(gx - hb / 2, lip - zicht + zicht / 2, hb, zicht - zicht / 2);
            dc.fillRectangle(gx - hb / 2, lip - zicht, hb / 3, zicht / 2);
            dc.fillRectangle(gx + hb / 2 - hb / 3, lip - zicht, hb / 3, zicht / 2);
        }
    }

    function tekenVliegendeHoed(dc as Graphics.Dc, w as Number, h as Number, vloer as Number, gx as Number, top as Number) as Void {
        if (spel.toestand != Regel.SLOK) {
            return;
        }
        var f = spel.fase.toFloat() / Regel.SLOK_MS;
        if (f > 1.0) {
            f = 1.0;
        }
        var hh = (h * 0.06).toNumber();
        var tx = (w * 0.74).toNumber();
        var ty = vloer - (spel.hoeden - 1) * hh;
        if (ty < hh) {
            ty = hh;
        }
        var x = gx + ((tx - gx) * f).toNumber();
        var boog = (h * 0.25 * 4.0 * f * (1.0 - f)).toNumber();
        var y = top + ((ty - top) * f).toNumber() - boog;
        tekenHoed(dc, x, y, (w * 0.17).toNumber(), hh, KLEUREN[spel.held]);
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
        dc.setColor(spel.tijdOver < 5000 ? 0xFF0000 : 0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        if (System.getDeviceSettings().screenShape != System.SCREEN_SHAPE_ROUND) {
            // Vierkant scherm: de klok is een balk langs de bovenrand die leegloopt.
            dc.fillRectangle(0, 0, (w * spel.tijdOver / Regel.RONDE_MS).toNumber(), 5);
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
