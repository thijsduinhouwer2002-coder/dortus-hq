import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Eindscherm na de sessie (blad v7 6b en 6c): kop, tijden, zee met het dier, weekstippen.
module EbbEindScherm {
    // Tekst midden op hoogte y; FONT_SMALL als hij binnen de koorde past (met marge), anders FONT_XTINY.
    function tekstInRonde(dc as Graphics.Dc, d as Number, y as Float, tekst as String, kleur as Number) as Void {
        var dy = y - 0.5;
        var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.86;
        var f = (dc.getTextWidthInPixels(tekst, EbbTeken.fS()) <= koorde) ? EbbTeken.fS() : EbbTeken.fX();
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    // Blad v7 scherm 6b en 6c (keuring bouw 1 punt 7): kop "3 rounds done", de tijden, de zee met het nieuwe dier (6b)
    // of het volgende dier als silhouet (6c), een regel, stippen voor het weekdoel met de reeks in weken.
    // Past bij 1 tot 6 rondes: tot 3 tijden op één regel, daarna twee regels in de kleine letter.
    function teken(dc as Graphics.Dc, d as Number, v as EbbView) as Void {
        // Mila blad v9 punt 3: na de walvis een eigen feestscherm, zonder tijden.
        if (v.nieuweDieren.size() == 0 && v.eindVolgend < 0) {
            EbbSeaComplete.teken(dc, d, v.eindReeks);
            return;
        }
        var w = d;
        var n = v.sessie.inhoudtijden.size();
        var tijden = [] as Array<String>;
        for (var i = 0; i < n; i += 1) {
            var s = (v.sessie.inhoudtijden[i] + 500) / 1000;
            tijden.add((s / 60) + ":" + (s % 60).format("%02d"));
        }
        var kopY = (n > 3) ? 0.14 : 0.17;
        // Beelden run 42955254555: bij 4 tot 6 rondes raakte de tweede regel tijden de schuimkam. De zee begint nu
        // 8 px plus de golfhoogte onder de onderkant van de tweede regel, gerekend met de echte letterhoogtes.
        var lhX = dc.getFontHeight(EbbTeken.fX());
        var lhS = dc.getFontHeight(EbbTeken.fS());
        // Keuring bouw 3 punt 6: tijden minstens 10 px onder de titel op 454 en 6 px op 260 (0,022 D).
        var gat = (d * 0.022).toNumber();
        gat = gat < 6 ? 6 : gat;
        var y1 = (d * kopY).toNumber() + lhS / 2 + gat + lhX / 2;
        var yTijden = (d * kopY).toNumber() + lhS + gat;   // midden van de ene regel tijden in de grote letter
        var onderTijden = (n > 3) ? y1 + lhX + lhX / 2 : yTijden + lhS / 2;
        var zeeTop = 0.326;
        var t = (onderTijden + 8 + d * 0.02) / d.toFloat();
        zeeTop = t > zeeTop ? t : zeeTop;
        EbbZee.zeeBanden(dc, d, [zeeTop, 0.60, 0.88] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * kopY).toNumber(), EbbTeken.fS(), n + (n == 1 ? " round done" : " rounds done"), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (n <= 3) {
            dc.drawText(w / 2, yTijden, EbbTeken.fS(), regel(tijden, 0, n), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        } else {
            var helft = (n + 1) / 2;
            // Keuring bouw 2 punt 4: twee regels van 3, de eerste 6 px onder de titel.
            var lh = lhX;
            dc.drawText(w / 2, y1, EbbTeken.fX(), regel(tijden, 0, helft), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            dc.drawText(w / 2, y1 + lh, EbbTeken.fX(), regel(tijden, helft, n), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        // Keuring bouw 4 punt 5: het dier past tussen de tijden en de regel eronder (8 px lucht boven, 6 px onder).
        var bandTop = onderTijden + 8;
        var bandOnder = (d * 0.645).toNumber() - lhS / 2 - 6;
        var bandBreed = (d * 0.30).toNumber();
        var extra = 0;
        if (v.nieuweDieren.size() > 0) {
            var dier = v.nieuweDieren[0];
            // Keuring bouw 3 punt 8: het nieuwe dier 15 px lager (op 454).
            EbbDierMaat.inBand(dc, dier, w / 2, bandTop, bandOnder, bandBreed, (d * 0.15).toNumber(), EbbDierPlaatje.GEVONDEN);
            tekstInRonde(dc, d, 0.645, "new friend: " + EbbDierData.NAMEN[dier], EbbTeken.LICHT);
        } else {
            // Mila v8: silhouet met rand en kenmerk (banden van de clownvis, vlek van de orka) in 00AAFF.
            // Beelden run 42980590755: de schaduw stak met de scharen boven de kamlijn uit; Mila v9: alleen in het water.
            var inWater = (d * (zeeTop + 0.010)).toNumber() + 6;
            EbbDierMaat.inBand(dc, v.eindVolgend, w / 2, bandTop > inWater ? bandTop : inWater, bandOnder, bandBreed, (d * (n > 3 ? 0.09 : 0.105)).toNumber(), EbbDierPlaatje.SCHADUW);
            tekstInRonde(dc, d, 0.645, volgendTekst(v), Graphics.COLOR_WHITE);
            // Mila blad v9 punt 4: "a new friend" in geel onder de regel; de week schuift een regel op.
            extra = dc.getFontHeight(EbbTeken.fX());
            dc.setColor(EbbTeken.LICHT, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * 0.645).toNumber() + lhS / 2 + extra / 2, EbbTeken.fX(), "a new friend", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        // Besluit 11 nov 04:30: de week in plaats van dagen op rij; geen rustdagzin meer (een week heeft vanzelf rust).
        var dag = EbbView.vandaag();
        var boven = (d * 0.645).toNumber() + dc.getFontHeight(EbbTeken.fS()) / 2 + extra;
        EbbTeken.weekStippen(dc, d, v.eindReeks, ((EbbBouw.DEMO || EbbBouw.PLAATJE) ? v.plaatjeWeek : EbbTrouw.dezeWeek(dag)), EbbTrouw.weekdoel(), boven);
    }

    function regel(tijden as Array<String>, van as Number, tot as Number) as String {
        var s = "";
        for (var i = van; i < tot; i += 1) {
            s += (i > van ? "   " : "") + tijden[i];
        }
        return s;
    }

    // Keuring bouw 2 punt 4: geen "next:" (besluit 22:53 punt 3), wel wat er nog nodig is: "1 more session",
    // "2 more weeks in a row", of "next session" als het dier al klaar ligt.
    function volgendTekst(v as EbbView) as String {
        // Keuring bouw 3 punt 11 en Mila blad v9 punt 4: wat er nog nodig is ("1 more session:"), "a new friend" staat eronder.
        if (v.eindRest <= 0) {
            return "next session:";
        }
        if ((EbbTrouw.DIEREN[v.eindVolgend][1] as Number) == EbbTrouw.SOORT_REEKS) {
            return v.eindRest + (v.eindRest == 1 ? " more week:" : " more weeks:");
        }
        return v.eindRest + (v.eindRest == 1 ? " more session:" : " more sessions:");
    }
}
