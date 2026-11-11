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
    // Blad v7 scherm 6b en 6c (keuring bouw 1 punt 7): kop "3 rounds done", de tijden, de zee met het nieuwe dier (6b)
    // of het volgende dier als silhouet (6c), een regel, stippen voor het weekdoel met de reeks in weken.
    // Past bij 1 tot 6 rondes: tot 3 tijden op één regel, daarna twee regels in de kleine letter.
    function teken(dc as Graphics.Dc, d as Number, v as EbbView) as Void {
        // Mila blad v9 punt 3: na de walvis een eigen feestscherm, zonder tijden; keuring bouw 6 punt 2: alleen de eerste keer.
        if (v.feest) {
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
        // Mila blad v13: alles omhoog. Kop midden op 38/260 D (bovenkant 34), tijden midden op 67 (bovenkant 63),
        // kamlijn op 94, het dier in een vast vak onder de kamlijn. Bij 4 tot 6 rondes (twee regels tijden) begint de
        // kop hoger en zakt de kamlijn mee met de tweede regel.
        var kopPx = EbbTeken.px(d, (n > 3) ? 30 : KOP);
        var lhX = dc.getFontHeight(EbbTeken.fX());
        var lhS = dc.getFontHeight(EbbTeken.fS());
        var gat = (d * 0.022).toNumber();
        gat = gat < 6 ? 6 : gat;
        var y1 = kopPx + lhS / 2 + gat + lhX / 2;
        var yTijden = EbbTeken.px(d, TIJD);   // midden van de ene regel tijden in de grote letter
        var onderTijden = (n > 3) ? y1 + lhX + lhX / 2 : yTijden + lhS / 2;
        var kam = kamlijn(d, onderTijden);
        var zeeTop = zeeTopBij(d, kam);
        EbbZee.zeeBanden(dc, d, [zeeTop, 0.60, 0.88] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, kopPx, EbbTeken.fS(), n + (n == 1 ? " round done" : " rounds done"), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
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
        // Mila blad v13: vast vak onder de kamlijn (98 tot 144, hoogstens 54 breed in 1/260 D), het midden van het
        // kader in het midden van het vak, en de grootste maat die past (krab 53 px breed op 260, was 21 tot 30).
        var bandTop = vakTop(d, kam);
        var bandOnder = EbbTeken.px(d, VAK_ONDER);
        var bandBreed = EbbTeken.px(d, VAK_BREED);
        var naamY = NAAM / 260.0;
        var naamPx = EbbTeken.px(d, NAAM);
        var extra = 0;
        if (v.nieuweDieren.size() == 0 && v.eindVolgend < 0) {
            // Keuring bouw 6 punt 2: alles gevonden en het feest al gezien: je eigen dier en "24 of 24 friends".
            EbbDierMaat.inBand(dc, v.gezelschap, w / 2, bandTop, bandOnder, bandBreed, d, EbbDierPlaatje.GEVONDEN);
            EbbTeken.tekstInRonde(dc, d, naamY, "24 of 24 friends", EbbTeken.LICHT);
        } else if (v.nieuweDieren.size() > 0) {
            var dier = v.nieuweDieren[0];
            EbbDierMaat.inBand(dc, dier, w / 2, bandTop, bandOnder, bandBreed, d, EbbDierPlaatje.GEVONDEN);
            // Keuring bouw 6 punt 5: een lange naam op twee regels in de gewone letter in plaats van kleiner.
            var zin = "new friend: " + EbbDierData.NAMEN[dier];
            var dy = naamY - 0.5;
            var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.86;
            if (dc.getTextWidthInPixels(zin, EbbTeken.fS()) <= koorde) {
                EbbTeken.tekstInRonde(dc, d, naamY, zin, EbbTeken.LICHT);
            } else {
                dc.setColor(EbbTeken.LICHT, Graphics.COLOR_TRANSPARENT);
                extra = EbbTeken.px(d, REGEL2);
                dc.drawText(w / 2, naamPx, EbbTeken.fS(), "new friend:", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
                dc.drawText(w / 2, naamPx + extra, EbbTeken.fS(), EbbDierData.NAMEN[dier], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
        } else {
            // Mila v8: silhouet met rand en kenmerk (banden van de clownvis, vlek van de orka) in 00AAFF.
            // Beelden run 42980590755: de schaduw stak met de scharen boven de kamlijn uit; Mila v9: alleen in het water.
            EbbDierMaat.inBand(dc, v.eindVolgend, w / 2, bandTop, bandOnder, bandBreed, d, EbbDierPlaatje.SCHADUW);
            EbbTeken.tekstInRonde(dc, d, naamY, volgendTekst(v), Graphics.COLOR_WHITE);
            // Mila blad v9 punt 4: "a new friend" in geel onder de regel; de week schuift een regel op.
            extra = EbbTeken.px(d, REGEL2);
            dc.setColor(EbbTeken.LICHT, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, naamPx + extra, EbbTeken.fX(), "a new friend", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        // Besluit 11 nov 04:30: de week in plaats van dagen op rij; geen rustdagzin meer (een week heeft vanzelf rust).
        var dag = EbbView.vandaag();
        var bonusNu = v.nieuweDieren.size() > 0 && EbbTrouw.bonus(v.nieuweDieren[0]);
        EbbTeken.weekStippen(dc, d, bonusNu ? -1 : v.eindReeks, ((EbbBouw.DEMO || EbbBouw.PLAATJE) ? v.plaatjeWeek : EbbTrouw.dezeWeek(dag)), EbbTrouw.weekdoel(), EbbTeken.px(d, STIP) + extra);
    }

    // Mila blad v13, in 1/260 D: midden van kop en tijden, kamlijn, vak van het dier, midden van de naamregel, afstand
    // naar een tweede regel, midden van de weekstippen. Ook voor het Calm-eindscherm (RustigView).
    const KOP = 38;
    const TIJD = 67;
    const KAM = 94;
    const VAK_ONDER = 144;
    const VAK_BREED = 54;
    const NAAM = 157;
    const REGEL2 = 23;
    const STIP = 180;

    // Kamlijn in px: op 94/260 D, of lager als de tekst erboven verder doorloopt (twee regels tijden).
    function kamlijn(d as Number, onderTekst as Number) as Number {
        var k = EbbTeken.px(d, KAM);
        // Beeld run 43104956914 (FR255, 6 rondes): met 7 raakte de tweede regel tijden de golf; nu 11.
        var t = onderTekst + EbbTeken.px(d, 11);
        return t > k ? t : k;
    }

    // De zee tekent haar kam iets onder de opgegeven top. Beeld run 43104956914 (FR255): met 0,026 D lag de kam
    // gemiddeld 3 px boven de 94 van het blad en maar 7 px onder de tijden; daarom 0,014 D.
    function zeeTopBij(d as Number, kam as Number) as Float {
        return (kam - d * 0.014) / d.toFloat();
    }

    function vakTop(d as Number, kam as Number) as Number {
        return kam + EbbTeken.px(d, 4);
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
