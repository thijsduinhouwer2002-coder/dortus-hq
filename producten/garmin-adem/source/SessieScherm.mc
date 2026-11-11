import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

// Het sessiescherm van EbbView: ademen, inhouden en herstel; na de sessie eindscherm, today of 8 weeks.
module EbbSessieScherm {
    const YKLEIN_ADEMEN = 0.855;
    const ONDER_MIDDEN = 0.84;

    function teken(v as EbbView, dc as Graphics.Dc) as Void {
        var nu = System.getTimer();
        v.sessie.bijwerken(nu);
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();

        var fase = v.sessie.fase;
        var d = (w < h) ? w : h;
        // Golf schuift ±2 rad per seconde; in de plaatjesbouw stil, zodat testbeelden vóór en na pixel voor pixel te vergelijken zijn.
        var golfFase = EbbBouw.PLAATJE ? 0.0 : (nu % 3142) / 500.0;
        var t = v.sessie.verstreken(nu);
        var woord = "";
        var groot = "";
        var klein = "";
        var yGroot = 0.38;
        var yKlein = 0.73;
        var font = EbbTeken.grootFont(dc, d);
        var donker = false;
        var grootDx = 0;
        if (fase == Ebb.FASE_ADEMEN) {
            // 1. Ademen: peil volgt de adem, 20% bij uit, 72% bij in (Mila 80%; lager zodat het fasewoord nooit onder water staat, beeld run 42800407029).
            // Keuring bouw 1 punt 5 en Daan B2: zee onderaan zoals blad v6 scherm 2, het getal altijd erboven.
            EbbZee.ademZee(dc, d, v.sessie.water(nu), golfFase);
            yGroot = 0.39 - dc.getFontHeight(font).toFloat() / d / 2;
            woord = v.sessie.isIn(nu) ? "breathe in" : "breathe out";   // blad v6 scherm 2
            groot = v.sessie.ademhaling(nu).toString();
            klein = "of " + v.sessie.ademhalingen + " · round " + (v.sessie.ronde + 1);
            // Daan M1: laagste golfrand ligt op 1 - 0,20 + 0,025 = 0,825 D; de ondertekst begint eronder (0,855; run 42826914263 gaf bij 0,84 maar 2 px ruimte op 260 px),
            // zodat hij altijd helemaal in het water staat en nooit op de schuimrand.
            // Keuring bouw 2 punt 10: onderste regel op alle ademschermen op dezelfde hoogte, midden op 0,84 D (381 px op 454).
            yKlein = ONDER_MIDDEN - dc.getFontHeight(EbbTeken.fX()).toFloat() / d / 2;
        } else if (fase == Ebb.FASE_INHOUDEN) {
            // Blad v6 (3a, 3b, 3d, 3c; keuring 01:55 punt 2): de zee wordt elke 30 s een stand donkerder tot 2:30
            // (EbbProfiel.zeeStand), daarna gelijk. Bovenaan "hold" (na 3:00 "time to breathe" met trilteken),
            // daaronder hoe je stopt, dan de tijd, je dier, en onderaan hartslag en ronde.
            var s = t / 1000;
            var stand = EbbProfiel.zeeStand(s);
            EbbZee.zee(dc, d, stand, golfFase);
            var fhT = dc.getFontHeight(EbbTeken.fS());
            var fhK = dc.getFontHeight(EbbTeken.fX());
            var yKop = (d * 0.20).toNumber();
            if (s < 180) {
                dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
                dc.drawText(w / 2, yKop, EbbTeken.fS(), "hold", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            } else {
                var tb = "time to breathe";
                dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
                dc.drawText(w / 2, yKop, EbbTeken.fX(), tb, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
                EbbTeken.trilboog(dc, d, yKop, dc.getTextWidthInPixels(tb, EbbTeken.fX()));
            }
            var yStop = yKop + fhT / 2 + fhK / 2;
            dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, yStop, EbbTeken.fX(), v.stopTekst(), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            // De tijd direct onder de stopregel: de lege ruimte boven de cijfers (hoogte min ascent min descent)
            // valt weg, zodat de cijfers 2% D onder de stopregel beginnen.
            // Besluit 11 nov 09:30 punt 2: kleinere cijfers, zodat het dier 90 x 70 (454) en 50 x 40 (260) krijgt.
            // Blijft er meer ruimte over dan het dier nodig heeft, dan zakken de cijfers met de helft daarvan.
            font = EbbTeken.grootKlein();
            var leeg = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            leeg = leeg > 0 ? leeg : 0;
            var yTijd = yStop + fhK / 2 + (d * 0.02).toNumber() - leeg;
            var gatD = (d * 0.022).toNumber();
            gatD = gatD < 6 ? 6 : gatD;
            var ruimte = ((d * ONDER_MIDDEN).toNumber() - fhK / 2 - 8) - (yTijd + leeg + Graphics.getFontAscent(font) + gatD) - (d * 0.154).toNumber();
            if (ruimte > 1) {
                yTijd += ruimte / 2;
            }
            yGroot = yTijd.toFloat() / d;
            var onderCijfer = yTijd + leeg + Graphics.getFontAscent(font);
            // Beelden run 42938098473 (fr265): de walvis raakte de hartregel en met zijn fontein bijna de cijfers.
            // Daarom het kleine dier (zoals in de sea log, blad v6: 0,10 D) vlak onder de cijfers en de hartregel lager.
            // Keuring bouw 2 punt 7: het dier groter (±0,19 D breed: 86 px op 454, 49 px op 260), midden onder de tijd.
            var yDier = onderCijfer + (d * 0.085).toNumber();
            var yRegel = (d * ONDER_MIDDEN).toNumber();
            // Belletjes links en rechts van het dier, vanaf 2:30 geen belletjes meer (blad v6 punt 5).
            if (stand < 5) {
                var stijg = (t % 8000) / 8000.0;
                var yd = yDier.toFloat() / d;
                // Keuring bouw 2 punt 7: belletjes alleen bij het dier, net naast zijn kop en staart.
                EbbTeken.bellen(dc, d, [[0.37, yd - 0.02 - 0.06 * stijg, 0.011], [0.63, yd - 0.04 - 0.06 * stijg, 0.008]] as Array<Array<Float> >);
            }
            // Daan B3 en keuring bouw 1 punt 6: je eigen dier rust in het midden onder de tijd (geen rode vis die
            // voorbij zwemt), in de eigen kleuren van Mila's data; zonder dier (nieuwe gebruiker) alleen de zee.
            if (v.gezelschap >= 0) {
                // Rustig heen en weer: ±1,5 procent D in 8 s (in de testbeelden stil in het midden).
                var dx = EbbBouw.PLAATJE ? 0 : (Math.sin((t % 8000) * 2.0 * Math.PI / 8000.0) * d * 0.015).toNumber();
                // Keuring bouw 3 punt 8: het dier past in 90 x 70 op 454 (50 x 40 op 260), onderkant 8 px boven de hartslagregel.
                // Keuring bouw 4 punt 5 (scène 24): de krab raakte "1:45". Het dier past nu tussen de onderkant van de
                // cijfers (plus 0,022 D, minstens 6 px) en de hartslagregel (8 px erboven), in het midden van die band.
                var gat = (d * 0.022).toNumber();
                gat = gat < 6 ? 6 : gat;
                var bandTop = onderCijfer + gat;
                var bandOnder = yRegel - dc.getFontHeight(EbbTeken.fX()) / 2 - 8;
                var hb = bandOnder - bandTop;
                var hMax = (d * 0.154).toNumber();
                var mz = EbbDierMaat.inVak(v.gezelschap, (d * 0.198).toNumber(), hb < hMax ? hb : hMax);
                var gz = EbbDierMaat.grenzen(v.gezelschap);
                var yd2 = (bandTop + bandOnder) / 2 - (gz[2] + gz[3]) * mz / (2 * EbbDierData.SCHAAL);
                EbbDierVoorraad.teken(dc, v.gezelschap, w / 2 + dx, yd2, mz, EbbDierPlaatje.GEVONDEN);
            }
            groot = (s / 60).toString() + ":" + (s % 60).format("%02d");
            // Daan K2: in de stilgezette testbeelden een nagebootste hartslag (61), zodat je ziet hoe het eruitziet als het werkt.
            EbbTeken.hartRonde(dc, d, yRegel, EbbBouw.PLAATJE ? 61 : EbbOpname.hartslag(), v.sessie.ronde + 1);
        } else if (fase == Ebb.FASE_HERSTEL) {
            // Blad v6 scherm 4 (herstel): de zon komt op achter de zee (W0, W1, W2), bovenaan "big breath in, hold",
            // groot de seconden met een kleine "s", onderaan "round 2 held 1:45".
            // Keuring bouw 2 punt 10 en beelden run 42955254555: de zon raakte de onderkant van "15" nog. Nu staat de
            // bovenkant van de zon 10 px onder de onderkant van de cijfers (zelfde rekensom als hieronder voor "s").
            var zr = (d * 0.10).toNumber();
            var yG = 0.415 - dc.getFontHeight(font).toFloat() / d / 2;
            var leegZ = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            var onderZ = (d * yG).toNumber() + (leegZ > 0 ? leegZ : 0) + Graphics.getFontAscent(font);
            var zcy = onderZ + 10 + zr;
            var zMin = (d * 0.67).toNumber();
            zcy = zcy < zMin ? zMin : zcy;
            dc.setColor(EbbTeken.GEEL, EbbTeken.GEEL);
            dc.fillCircle(w / 2, zcy, zr);
            EbbZee.zeeBanden(dc, d, [0.64, 0.72, 0.86] as Array<Float>, [0, 1, 2] as Array<Number>, 0.014, golfFase);
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            // Beelden run 42940068457: op vivoactive 5 en fenix 8 liep deze regel in FONT_SMALL door de ronde rand.
            // Past hij niet binnen 80 procent van de koorde op 0,215 D, dan de kleinere letter.
            var kop = "big breath in, hold";
            var kopF = EbbTeken.fS();
            var koorde = 2.0 * Math.sqrt(0.16 - 0.285 * 0.285) * d;   // binnen de cirkel van 0,8 D op 0,215 D
            if (dc.getTextWidthInPixels(kop, kopF) > koorde) {
                kopF = EbbTeken.fX();
            }
            groot = ((v.sessie.herstelMs - t) / 1000 + 1).toString();
            // Keuring bouw 3 punt 6: het cijfer zelf in het midden, "s" los erachter; de kop minstens 12 px (454)
            // of 6 px (260) boven de bovenkant van de cijfers.
            grootDx = 0;
            yGroot = 0.415 - dc.getFontHeight(font).toFloat() / d / 2;
            var leegH = dc.getFontHeight(font) - Graphics.getFontAscent(font) - Graphics.getFontDescent(font);
            var topH = (d * yGroot).toNumber() + (leegH > 0 ? leegH : 0);
            var gatH = (d * 0.026).toNumber();
            gatH = gatH < 6 ? 6 : gatH;
            var yKopH = topH - gatH - dc.getFontHeight(kopF) / 2;
            var yKop0 = (d * 0.215).toNumber();
            dc.drawText(w / 2, (yKopH < yKop0 ? (yKopH < d * 0.12 ? (d * 0.12).toNumber() : yKopH) : yKop0), kopF, kop, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            var onderH = (d * yGroot).toNumber() + (leegH > 0 ? leegH : 0) + Graphics.getFontAscent(font);
            var bg = dc.getTextWidthInPixels(groot, font);
            dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2 + grootDx + bg / 2 + 3, onderH - Graphics.getFontAscent(EbbTeken.fS()), EbbTeken.fS(), "s", Graphics.TEXT_JUSTIFY_LEFT);
            var n = v.sessie.inhoudtijden.size();
            if (n > 0) {
                var hs = (v.sessie.inhoudtijden[n - 1] + 500) / 1000;
                klein = "round " + n + " held " + (hs / 60).toString() + ":" + (hs % 60).format("%02d");
            }
            yKlein = ONDER_MIDDEN - dc.getFontHeight(EbbTeken.fX()).toFloat() / d / 2;
        } else {
            // Na de sessie: eindscherm, 8 weeks of today.
            if (v.einde) {
                EbbEindScherm.teken(dc, d, v);
            } else if (v.getij) {
                EbbOverzicht.weken(dc, d, v);
            } else {
                EbbOverzicht.vandaag(dc, d, v);
            }
        }
        if (woord.length() > 0) {
            // Staat het lichte water tot boven, dan leest het zachte woord niet meer: dan donkerblauw.
            dc.setColor(donker ? EbbTeken.DIEPTE[3] : EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * 0.13).toNumber(), EbbTeken.fS(), woord, Graphics.TEXT_JUSTIFY_CENTER);
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (groot.length() > 0) {
            dc.drawText(w / 2 + grootDx, (d * yGroot).toNumber() + dc.getFontHeight(font) / 2, font, groot, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        }
        if (klein.length() > 0) {
            dc.setColor(fase == Ebb.FASE_INHOUDEN ? EbbTeken.ZACHT : Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, (d * yKlein).toNumber(), EbbTeken.fX(), klein, Graphics.TEXT_JUSTIFY_CENTER);
        }
        if (EbbBouw.DEMO) {
            meet(dc, w, fase as Number, groot, font);
            if (fase == Ebb.FASE_ADEMEN && !_onderGemeld && klein.length() > 0) {
                meetOnder(dc, d, klein);
            }
        }
    }

    // Daan M1, alleen in de testbouw: ruimte tussen de laagste golfrand en de ondertekst, en of de ondertekst
    // op zijn breedste regel (de onderkant) binnen het ronde scherm past. Alles in pixels.
    var _onderGemeld as Boolean = false;
    function meetOnder(dc as Graphics.Dc, d as Number, klein as String) as Void {
        _onderGemeld = true;
        var golf = (d * (EbbZee.ADEM_TOP + EbbZee.ADEM_AMP)).toNumber() + (d / 160 > 1 ? d / 160 : 1) / 2 + 1;
        var top = (d * YKLEIN_ADEMEN).toNumber();
        var leeg = dc.getFontHeight(EbbTeken.fX()) - Graphics.getFontAscent(EbbTeken.fX()) - Graphics.getFontDescent(EbbTeken.fX());
        var letterTop = top + (leeg > 0 ? leeg : 0);
        var onder = top + Graphics.getFontAscent(EbbTeken.fX()) + (leeg > 0 ? leeg : 0);
        var breed = dc.getTextWidthInPixels(klein, EbbTeken.fX());
        var r = d / 2.0;
        var dy = onder - r;
        var koorde = (dy < r) ? (2.0 * Math.sqrt(r * r - dy * dy)).toNumber() : 0;
        System.println("ONDERTEKST golf " + golf + " lettertop " + letterTop + " ruimte " + (letterTop - golf) + " breedte " + breed + " koorde " + koorde + " over " + (koorde - breed));
    }

    // Eis 11 en 12, alleen in de testbouw: breedte van het grote getal per fase (eerste keer)
    // en het hoogste geheugengebruik, gemeld zodra het duikprofiel getekend is.
    var _grootGemeld as Array<Boolean> = [false, false, false, false, false] as Array<Boolean>;
    var _maxGeheugen as Number = 0;
    var _geheugenGemeld as Boolean = false;

    // Eis 11 meet de hoogte van de cijfers (ascent; een "1" is nooit 30% breed), breedte staat er ter info bij.
    function meet(dc as Graphics.Dc, w as Number, fase as Number, groot as String, font as Graphics.FontType) as Void {
        if (groot.length() > 0 && !_grootGemeld[fase]) {
            _grootGemeld[fase] = true;
            if (fase == 0) {
                for (var i = 0; i < EbbTeken.GROOT_LIJST.size(); i += 1) {
                    var f = EbbTeken.GROOT_LIJST[i];
                    System.println("LETTER " + i + " ascent " + Graphics.getFontAscent(f) + " hoogte " + dc.getFontHeight(f) + " breedte0:00 " + dc.getTextWidthInPixels("0:00", f) + " van " + w);
                }
            }
            var b = dc.getTextWidthInPixels(groot, font);
            var hoog = Graphics.getFontAscent(font);
            System.println("GROOT fase " + fase + " tekst " + groot + " breedte " + b + " hoogte " + hoog + " van " + w + " = " + (hoog * 100 / w) + "%");
        }
        var st = System.getSystemStats();
        if (st.usedMemory > _maxGeheugen) {
            _maxGeheugen = st.usedMemory;
        }
        if (fase == Ebb.FASE_KLAAR && !_geheugenGemeld) {
            _geheugenGemeld = true;
            System.println("GEHEUGEN hoogste " + _maxGeheugen + " van " + st.totalMemory + " = " + (_maxGeheugen.toLong() * 100 / st.totalMemory) + "%");
        }
    }
}
