import Toybox.Activity;
import Toybox.ActivityMonitor;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Time;
import Toybox.Time.Gregorian;
import Toybox.WatchUi;

typedef Plaatje as WatchUi.BitmapResource or Graphics.BitmapReference;

// De wijzerplaat volgens de kit van Mila (ontwerp/garmin/wijzerplaat-gloop/kit): links de datum, uren
// boven minuten als plaatjes (groot), stappen en de hoedenregel, rechts Gloop die omhoog kijkt naar zijn
// toren, onderaan een vrij veld (nu hartslag). Alle plekken komen uit Plek.mc.
class GloopFaceView extends WatchUi.WatchFace {
    // Plaatjes: 0 de achtergrond, 1 Gloop die omhoog kijkt, 2 tot 11 de tien hoeden.
    var pl as Array<Plaatje> = [] as Array<Plaatje>;
    // Maten van Gloop en de hoeden (Maten.mc, uit de kit van het spel) en de plekken (Plek.mc).
    var m as Array<Number> = [] as Array<Number>;
    var p as Array<Number> = [] as Array<Number>;
    // De vier cijfers van de tijd. Alleen de cijfers die nu in beeld staan zijn geladen (0 tot 9 de
    // witte uren, 10 tot 19 de mintkleurige minuten, 20 tot 29 grijs voor de slaapstand), dat spaart geheugen op oudere horloges.
    var cij as Array<Plaatje?> = [null, null, null, null] as Array<Plaatje?>;
    var cijNr as Array<Number> = [-1, -1, -1, -1] as Array<Number>;
    // Lijnplaatjes voor de slaapstand (alleen AMOLED), pas geladen als ze nodig zijn.
    var lijnGloop as Plaatje?;
    var lijnHoed as Plaatje?;
    var lijnHoedNr as Number = -1;
    var slaap as Boolean = false;
    var gemeld as Boolean = false;
    var regelGemeld as Number = -1;
    // Knipperen als het horloge wakker is (Knipper.mc); het plaatje met het dichte oog laadt pas als het nodig is.
    var knipper as Knipper = new Knipper();
    var dichtPl as Plaatje?;
    // Kijken wordt beloond (regel van Daan): komt er een hoed bij terwijl je niet kijkt, dan valt hij
    // pas op de toren als je de pols optilt. `gezien` is het aantal hoeden (met kroon) dat de drager
    // al heeft zien landen, `wek` staat aan in de eerste seconde na het optillen.
    var gezien as Number = -1;
    var wek as Boolean = false;
    // Standen voor de bouwstraat (Bouw.AUTO): stappen per stand; de laatste stand is de slaapstand.
    const PROEF = [0, 3420, 7612, 10000, 14800, 7612] as Array<Number>;

    function initialize() {
        WatchFace.initialize();
    }

    function onLayout(dc as Graphics.Dc) as Void {
        m = Maten.voor(dc.getWidth());
        p = Plek.voor(dc.getWidth());
        pl = [
            WatchUi.loadResource(Rez.Drawables.Achter) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.GloopKijk) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed0) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed1) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed2) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed3) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed4) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed5) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed6) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed7) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed8) as Plaatje,
            WatchUi.loadResource(Rez.Drawables.Hoed9) as Plaatje
        ] as Array<Plaatje>;
    }

    function onEnterSleep() as Void {
        slaap = true;
        knipper.stop();
        WatchUi.requestUpdate();
    }

    function onExitSleep() as Void {
        slaap = false;
        wek = true;
        knipper.start();
        WatchUi.requestUpdate();
    }

    function onShow() as Void {
        if (!slaap) {
            knipper.start();
        }
    }

    function onHide() as Void {
        knipper.stop();
    }

    // Het cijfer op vak 0 tot 3 (tiental en eenheid van de uren, daarna van de minuten). Laadt alleen
    // als het cijfer op dat vak veranderd is.
    function cijfer(vak as Number, nr as Number) as Plaatje {
        var c = cij[vak];
        if (c == null || cijNr[vak] != nr) {
            c = Laad.cijfer(nr);
            cij[vak] = c;
            cijNr[vak] = nr;
        }
        return c;
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var stappen = 0;
        var doel = 10000;
        var info = ActivityMonitor.getInfo();
        if (info.steps != null) {
            stappen = info.steps as Number;
        }
        if (info.stepGoal != null) {
            doel = info.stepGoal as Number;
        }
        var slaapt = slaap;
        if (Bouw.AUTO) {
            var stand = (System.getTimer() / 3000) % 6;
            stappen = PROEF[stand];
            doel = 10000;
            slaapt = (stand == 5);
        }
        var amoled = (w >= 320);
        var klok = System.getClockTime();
        var is24 = System.getDeviceSettings().is24Hour;
        var uur = Regel.uur(klok.hour, is24);
        var rond = System.getDeviceSettings().screenShape == System.SCREEN_SHAPE_ROUND;

        // Hoeveel hoeden nu getekend worden (de kroon telt mee) en of de bovenste nog boven de toren zweeft.
        var aantal = Regel.aantal(stappen, doel);
        var toon = aantal;
        var zweef = false;
        if (Bouw.AUTO) {
            var sn = (System.getTimer() / 3000) % 6;
            var vorige = sn > 0 ? Regel.aantal(PROEF[sn - 1], doel) : aantal;
            zweef = (System.getTimer() / 1000) % 3 == 0 && aantal > vorige;
        } else if (slaap) {
            toon = Regel.wachtend(aantal, gezien);
        } else {
            zweef = wek && gezien >= 0 && aantal > gezien;
            wek = false;
            gezien = aantal;
        }
        var kroon = Regel.kroon(stappen, doel);

        if (slaapt && amoled) {
            tekenSlaap(dc, uur, is24, klok.min, toon, kroon && toon == aantal);
        } else {
            tekenVol(dc, w, h, uur, is24, klok.min, stappen, doel, rond, toon, kroon && toon == aantal, zweef);
        }
        if (!gemeld) {
            gemeld = true;
            var st = System.getSystemStats();
            System.println("GEHEUGEN " + w + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " vrij " + st.freeMemory);
        }
    }

    // De tijd: uren boven minuten, rechts uitgelijnd op de lijn van Mila. `dx` en `dy` verschuiven de
    // tijd (slaapstand, tegen inbranden); `grijs` kiest de grijze cijfers van de slaapstand.
    function tekenTijd(dc as Graphics.Dc, uur as Number, is24 as Boolean, minuut as Number, dx as Number, dy as Number, grijs as Boolean) as Void {
        var cw = p[9];
        var over = p[11];
        var rechts = p[2] + dx;
        var x1 = rechts - cw;
        var x0 = x1 - cw + over;
        var u = grijs ? 20 : 0;
        var mi = grijs ? 20 : 10;
        if (is24 || uur >= 10) {
            dc.drawBitmap(x0, p[4] + dy, cijfer(0, u + uur / 10));
        }
        dc.drawBitmap(x1, p[4] + dy, cijfer(1, u + uur % 10));
        dc.drawBitmap(x0, p[5] + dy, cijfer(2, mi + minuut / 10));
        dc.drawBitmap(x1, p[5] + dy, cijfer(3, mi + minuut % 10));
    }

    function tekenVol(dc as Graphics.Dc, w as Number, h as Number, uur as Number, is24 as Boolean, minuut as Number, stappen as Number, doel as Number, rond as Boolean, toon as Number, kroonOp as Boolean, zweef as Boolean) as Void {
        dc.setColor(0x000000, 0x000000);
        dc.clear();
        dc.drawBitmap(0, 0, pl[0]);

        // Gloop en de toren, rechts.
        var gx = p[0] - m[0] / 2;
        var gy = p[1] - m[1];
        var oogDicht = knipper.dicht;
        if (Bouw.AUTO) {
            // Tweede foto van stand 1 (3.420 stappen): oog dicht.
            oogDicht = (System.getTimer() / 1500) % 12 == 3;
        }
        if (oogDicht) {
            var dp = dichtPl;
            if (dp == null) {
                dp = WatchUi.loadResource(Rez.Drawables.GloopDicht) as Plaatje;
                dichtPl = dp;
            }
            dc.drawBitmap(gx, gy, dp);
        } else {
            dc.drawBitmap(gx, gy, pl[1]);
        }
        Toren.teken(dc, rond, gx + m[10], gy + m[11], toon, kroonOp, zweef, pl, m, p);

        // Links, rechts uitgelijnd op de lijn van de tijd: datum, tijd, stappen en de hoedenregel.
        tekenTijd(dc, uur, is24, minuut, 0, 0, false);
        var midden = Graphics.TEXT_JUSTIFY_RIGHT | Graphics.TEXT_JUSTIFY_VCENTER;
        var nu = Gregorian.info(Time.now(), Time.FORMAT_MEDIUM);
        tekst(dc, p[2], p[3], Graphics.FONT_XTINY, (nu.day_of_week as String).toUpper() + " " + nu.day, 0xFFAA00, midden);
        // Stappen en regel links uitgelijnd op de linkerrand van de tijd (moet 4 van Daan, 16 nov 12:55 UTC):
        // het blok hoort bij de tijd en blijft zo vrij van Gloop en de toren. Op MIP de regel 4 px lager (Mila).
        var links = p[2] - 2 * p[9] + p[11];
        var linksUit = Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER;
        tekst(dc, links, p[6], Graphics.FONT_TINY, Regel.punt(stappen), 0x55FFAA, linksUit);
        // Raakt de regel de toren (Venu Sq 2), dan zonder het woord HATS (antwoord van Mila). Op AMOLED staat
        // de regel 8 px lager, anders loopt hij door de stappen heen (gezien in run 43873269986).
        var rg = Regel.regel(stappen, doel);
        var grens = p[0] - m[0] / 2 + m[10] - m[12] / 2 - 6;
        // Staat de regel lager dan Gloops kruin, dan telt ook zijn linkerrand (Venu 3S: "7/10 HATS" en
        // "GOAL! +4" raakten zijn schouder, Daan 16 nov 13:50 UTC). Dan de korte vorm: "7/10" of "GOAL+4".
        var ry = p[7] + (w < 320 ? 4 : 8);
        if (ry + dc.getFontHeight(Graphics.FONT_XTINY) / 2 > gy && gx - 6 < grens) {
            grens = gx - 6;
        }
        var breed = dc.getTextWidthInPixels(rg, Graphics.FONT_XTINY);
        if (links + breed + 2 > grens) {
            rg = Regel.kort(rg);
        }
        if (Bouw.AUTO && regelGemeld != stappen) {
            regelGemeld = stappen;
            System.println("REGEL " + w + " '" + rg + "' links " + links + " breed " + breed + " na inkorten " + dc.getTextWidthInPixels(rg, Graphics.FONT_XTINY) + " grens " + grens);
        }
        tekst(dc, links, ry, Graphics.FONT_XTINY, rg, 0xFFAA00, linksUit);

        // Vrij veld onderaan: nu de hartslag met een getekend hartje.
        // Zonder hartslag alleen het hartje (kan a van Daan); het hartje staat links van Gloops voet (Mila: 0,36).
        var hs = "";
        var act = Activity.getActivityInfo();
        if (act != null && act.currentHeartRate != null) {
            hs = (act.currentHeartRate as Number).toString();
        }
        var r = (w * 0.014).toNumber();
        if (r < 3) {
            r = 3;
        }
        var hx = (w * 0.36).toNumber();
        var hy = p[8];
        dc.setColor(0xFF5555, Graphics.COLOR_TRANSPARENT);
        dc.fillCircle(hx - r, hy - r / 2, r);
        dc.fillCircle(hx + r - 1, hy - r / 2, r);
        dc.fillPolygon([[hx - 2 * r, hy - r / 4], [hx + 2 * r - 1, hy - r / 4], [hx, hy + 2 * r - 1]] as Array<Graphics.Point2D>);
        tekst(dc, hx + 3 * r, hy, Graphics.FONT_XTINY, hs, 0xFFAAAA, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Slaapstand op AMOLED: zwart, de tijd in grijs op dezelfde plek, Gloop als mint lijn met alleen de
    // bovenste hoed als gouden lijn op zijn hoofd. Elke minuut een paar pixels verschoven tegen inbranden.
    function tekenSlaap(dc as Graphics.Dc, uur as Number, is24 as Boolean, minuut as Number, toon as Number, kroonOp as Boolean) as Void {
        dc.setColor(0x000000, 0x000000);
        dc.clear();
        var dx = (minuut % 5) * 2 - 4;
        var dy = (minuut % 3) * 2 - 2;
        tekenTijd(dc, uur, is24, minuut, dx, dy, true);
        var rand = p[12];
        var gx = p[0] - m[0] / 2 + dx;
        var gy = p[1] - m[1] + dy;
        if (toon > 0) {
            var k = Toren.hoedOp(toon - 1, toon, kroonOp);
            var lh = lijnHoed;
            if (lh == null || lijnHoedNr != k) {
                lh = Laad.lijnHoed(k);
                lijnHoed = lh;
                lijnHoedNr = k;
            }
            dc.drawBitmap(gx + m[10] - (m[12 + 2 * k] + 2 * rand) / 2, gy + m[11] - m[13 + 2 * k] - rand, lh);
        }
        var lg = lijnGloop;
        if (lg == null) {
            lg = WatchUi.loadResource(Rez.Drawables.GloopAod) as Plaatje;
            lijnGloop = lg;
        }
        dc.drawBitmap(gx - rand, gy - rand, lg);
    }

    // Tekst met een donkere rand van 1 px, zodat hij ook op de bruine grot van MIP te lezen is.
    function tekst(dc as Graphics.Dc, x as Number, y as Number, font as Graphics.FontDefinition, s as String, kleur as Number, uitlijning as Number) as Void {
        dc.setColor(0x000000, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x - 1, y, font, s, uitlijning);
        dc.drawText(x + 1, y, font, s, uitlijning);
        dc.drawText(x, y - 1, font, s, uitlijning);
        dc.drawText(x, y + 1, font, s, uitlijning);
        // Nep-vet op AMOLED (moet 2 van Daan): de systeemletter is daar dun naast de dikke cijferplaatjes.
        var vet = (dc.getWidth() >= 320);
        if (vet) {
            dc.drawText(x + 2, y, font, s, uitlijning);
        }
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x, y, font, s, uitlijning);
        if (vet) {
            dc.drawText(x + 1, y, font, s, uitlijning);
        }
    }
}
