import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Na de sessie: today (blad v6 scherm 6) en 8 weeks (scherm 7).
module EbbOverzicht {
    // Blad v6 scherm 6 (today, keuring 01:55 punt 2 en 5): de hele dag als staande staven in één egale tint
    // (geen nadruk op de langste), per sessie een groepje met de klok eronder, onderaan "6 holds · avg 1:44".
    function vandaagSessies(v as EbbView) as Array<Array> {
        if (EbbBouw.PLAATJE) {
            // Keuring bouw 3 punt 14: today met 3 sessies (het meeste dat Today toont).
            return [[460, [70, 85, 100]], [765, [92, 110]], [1275, [80, 105, 184]]] as Array<Array>;
        }
        if (EbbBouw.DEMO) {
            return [[460, [70, 85, 100]], [1275, [80, 105, 184]]] as Array<Array>;
        }
        var lijst = EbbVandaag.lees(EbbView.vandaag());
        if (lijst.size() == 0 && v.sessie.inhoudtijden.size() > 0) {
            // Niet opgeslagen (weggegooid): dan alleen deze sessie, zonder klok.
            var secs = [] as Array<Number>;
            for (var i = 0; i < v.sessie.inhoudtijden.size(); i += 1) {
                secs.add((v.sessie.inhoudtijden[i] + 500) / 1000);
            }
            lijst.add([-1, secs] as Array);
        }
        return lijst;
    }

    function vandaag(dc as Graphics.Dc, d as Number, v as EbbView) as Void {
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.18).toNumber(), EbbTeken.fS(), "today", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbZee.strook(dc, d);
        var sessies = vandaagSessies(v);
        var samen = EbbVandaag.samen(sessies);
        if (samen[0] == 0) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, d / 2, EbbTeken.fS(), "no holds yet", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            return;
        }
        var lo = d * 0.20;
        var ro = d * 0.80;
        var bod = (d * 0.62).toNumber();
        var hoog = d * 0.27;
        var gat = d * 0.08;
        var maxS = 200;
        for (var i = 0; i < sessies.size(); i += 1) {
            var t = sessies[i][1] as Array<Number>;
            for (var j = 0; j < t.size(); j += 1) {
                if (t[j] > maxS) { maxS = t[j]; }
            }
        }
        var kol = (ro - lo - gat * (sessies.size() - 1)) / samen[0];
        var bw = (kol * 0.62).toNumber();
        bw = bw < 2 ? 2 : bw;
        var r = (bw * 3) / 10;
        dc.setColor(EbbTeken.staafKleur(), EbbTeken.staafKleur());
        var x = lo;
        var midden = [] as Array<Float>;
        var breedte = [] as Array<Float>;
        for (var i = 0; i < sessies.size(); i += 1) {
            var t = sessies[i][1] as Array<Number>;
            midden.add(x + kol * t.size() / 2.0);
            breedte.add(kol * t.size());
            for (var j = 0; j < t.size(); j += 1) {
                var xm = x + kol * (j + 0.5);
                var h = (hoog * t[j] / maxS).toNumber();
                h = h < 2 ? 2 : h;
                dc.fillRoundedRectangle((xm - bw / 2.0).toNumber(), bod - h, bw, h, r);
            }
            x += kol * t.size() + gat;
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 150 > 2 ? d / 150 : 2);
        dc.drawLine((lo - d * 0.01).toNumber(), bod, (ro + d * 0.01).toNumber(), bod);
        // Klok onder elke sessie, alleen als hij onder zijn groepje past (anders lopen de tijden in elkaar).
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        for (var i = 0; i < sessies.size(); i += 1) {
            var k = sessies[i][0] as Number;
            if (k < 0) { continue; }
            var tekst = EbbVandaag.klokTekst(k);
            if (dc.getTextWidthInPixels(tekst, EbbTeken.fX()) <= breedte[i] + gat * 0.8) {
                dc.drawText(midden[i].toNumber(), bod + (d * 0.055).toNumber(), EbbTeken.fX(), tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
        }
        var gem = samen[1];
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.775).toNumber(), EbbTeken.fX(),
            samen[0] + (samen[0] == 1 ? " hold · avg " : " holds · avg ") + (gem / 60) + ":" + (gem % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v6 scherm 7 (8 weeks, keuring 01:55 punt 2): sessies per week als staven met het getal erboven, een lege
    // week als stip, onderaan "sessions per week" en het gemiddelde over 8 weken als getal.
    function wekenData() as Array<Array<Number> > {
        if (EbbBouw.DEMO || EbbBouw.PLAATJE) {
            var nep = [] as Array<Array<Number> >;
            var n = [0, 0, 0, 0, 0, 0, 3, 6] as Array<Number>;
            for (var i = 0; i < 8; i += 1) {
                nep.add([n[i] > 0 ? 101 : 0, n[i], n[i] * 3] as Array<Number>);
            }
            return nep;
        }
        return EbbProfiel.weken(new EbbOpslag(), EbbTrouw.sessieDagen(), EbbView.vandaag());
    }

    function weken(dc as Graphics.Dc, d as Number, v as EbbView) as Void {
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.18).toNumber(), EbbTeken.fS(), "8 weeks", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbZee.strook(dc, d);
        var weken = wekenData();
        var hoogN = 7;
        var som = 0;
        var holds = 0;
        var sessies = 0;
        for (var i = 0; i < weken.size(); i += 1) {
            if (weken[i][1] > hoogN) { hoogN = weken[i][1]; }
            som += weken[i][0] * weken[i][2];
            holds += weken[i][2];
            sessies += weken[i][1];
        }
        // Keuring bouw 3 punt 11: leeg is zonder sessies, niet zonder inhouden (alleen Calm telt ook).
        if (sessies == 0) {
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(d / 2, d / 2, EbbTeken.fS(), "no sessions yet", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            return;
        }
        var lo = d * 0.20;
        var top = d * 0.33;
        var bod = (d * 0.58).toNumber();
        var kol = d * 0.60 / 8;
        var bw = (kol * 0.66).toNumber();
        var r = (bw * 3) / 10;
        for (var i = 0; i < weken.size(); i += 1) {
            var n = weken[i][1];
            var xm = (lo + kol * (i + 0.5)).toNumber();
            if (n > 0) {
                var h = ((bod - top) * n / hoogN).toNumber();
                dc.setColor(EbbTeken.staafKleur(), EbbTeken.staafKleur());
                dc.fillRoundedRectangle(xm - bw / 2, bod - h, bw, h, r);
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
                dc.drawText(xm, bod - h - (d * 0.045).toNumber(), EbbTeken.fX(), n.toString(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            } else {
                dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);   // lege week: kleine stip, donkerder dan de staven
                var rr = (d * 0.013).toNumber();
                dc.fillCircle(xm, bod - (d * 0.03).toNumber(), rr < 2 ? 2 : rr);
            }
        }
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 150 > 2 ? d / 150 : 2);
        dc.drawLine(lo.toNumber(), bod, (d * 0.80).toNumber(), bod);
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.665).toNumber(), EbbTeken.fX(), "sessions per week", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        if (holds == 0) {
            return;
        }
        var gem = (som + holds / 2) / holds;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.75).toNumber(), EbbTeken.fX(), "avg hold " + (gem / 60) + ":" + (gem % 60).format("%02d"),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
