import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Sea log volgens Mila blad v9 punt 1: 4 bladen van 6 (2 rijen van 3) voor de 24 gewone dieren, blad 5 alleen de
// zeekomkommer (bonus), groot. Maten in 1/260 van D (ontwerp/garmin/ebb-blad-v9.md). Dieren via EbbDierPlaatje.laag.
class DierenView extends WatchUi.View {
    var keuze as Number = 0;
    const PER_BLAD = 6;
    const BLADEN = 5;
    // Run 42953647184: met 3 per beurt (15 keer tekenen) trapte de watchdog op de FR255; 1 dier (5 keer) per beurt.
    const NIEUW_PER_BEURT = 1;
    var _plaatje as Graphics.BufferedBitmapReference or Null = null;
    var _sleutel as Number = -1;
    var _getekend as Number = 0;
    var _laag as Number = 0;
    var _opbouwBeurt as Boolean = false;

    // Tekent laag _laag van dier i; geeft true als het dier af is.
    function tekenLaag(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number) as Boolean {
        var l = _laag;
        _laag += 1;
        var soort = EbbTrouw.heeft(i) ? EbbDierPlaatje.GEVONDEN : EbbDierPlaatje.SILHOUET;
        EbbDierPlaatje.laag(dc, i, cx, cy, maat, soort, l);
        return l >= EbbDierPlaatje.lagenVan(soort) - 1;
    }

    // Voor de toets: staat het hele blad in het plaatje?
    function klaar() as Boolean {
        return _plaatje != null && _getekend >= opBlad(bladVan(keuze));
    }

    // Blad van dier i: nr 1 tot 24 in bladen van 6, de bonus (laatste) alleen op blad 5.
    function bladVan(i as Number) as Number {
        return EbbTrouw.bonus(i) ? BLADEN - 1 : i / PER_BLAD;
    }

    // Aantal dieren op een blad, en het eerste nummer.
    function opBlad(blad as Number) as Number {
        return blad == BLADEN - 1 ? 1 : PER_BLAD;
    }

    function eerste(blad as Number) as Number {
        return blad == BLADEN - 1 ? EbbTrouw.ZEEKOMKOMMER : blad * PER_BLAD;
    }

    function initialize() {
        View.initialize();
        var m = EbbTrouw.zwemmer();
        keuze = m >= 0 ? m : 0;
    }

    function bladen() as Number {
        return BLADEN;
    }

    function verschuif(stap as Number) as Void {
        var n = EbbTrouw.DIEREN.size();
        keuze = (keuze + stap + n) % n;
        WatchUi.requestUpdate();
    }

    // Wat er onder de naam staat (blad v8 C): gevonden "swims with you" of "found"; anders "next session",
    // "2 more days in a row" of "at 50 sessions"; de bonus blijft een verrassing.
    function regel(i as Number) as String {
        if (EbbTrouw.heeft(i)) {
            // Keuring bouw 3 punt 9: de hint zegt welke knop ("START: swims with you").
            return (EbbTrouw.zwemmer() == i) ? "swims with you" : WatchUi.loadResource(Rez.Strings.KiesHint) as String;
        }
        if (EbbTrouw.bonus(i)) {
            return "a surprise";
        }
        var r = EbbTrouw.DIEREN[i];
        var drempel = r[2] as Number;
        if ((r[1] as Number) == EbbTrouw.SOORT_REEKS) {
            var reeks = EbbTrouw.reeksOp(EbbView.vandaag());
            var rest = (EbbTrouw.getal(EbbTrouw.BESTE) >= drempel) ? 0 : drempel - reeks;
            if (rest <= 0) {
                return "next session";
            }
            return rest + (rest == 1 ? " more week in a row" : " more weeks in a row");
        }
        var nog = drempel - EbbTrouw.getal(EbbTrouw.SESSIES);
        return (nog <= 1) ? "next session" : "at " + drempel + " sessions";
    }

    // Plek van dier k op het blad in px: [x, y, maat] (zwaartepunt), volgens blad v9.
    function plek(d as Number, blad as Number, k as Number) as Array<Number> {
        var m = EbbTeken.px(d, 23);
        if (blad == BLADEN - 1) {
            return [d / 2, EbbTeken.px(d, 132), m + 14] as Array<Number>;
        }
        return [d / 2 + (k % 3 - 1) * EbbTeken.px(d, 62), EbbTeken.px(d, 103 + (k / 3) * 47), m] as Array<Number>;
    }

    // Het zwarte plaatje van een blad: van de bovenkant van het hoogste dier tot de onderkant van het laagste,
    // met de rand erbij. Zet _boven en _onder.
    var _boven as Number = 0;
    var _onder as Number = 0;

    function bouwBlad(d as Number, blad as Number) as Void {
        _boven = d;
        _onder = 0;
        for (var k = 0; k < opBlad(blad); k += 1) {
            var p = plek(d, blad, k);
            var g = EbbDierMaat.grenzen(eerste(blad) + k);
            var r = EbbDierData.randPx(p[2]) + 1;
            var t = p[1] + g[2] * p[2] / EbbDierData.SCHAAL - r;
            var o = p[1] + g[3] * p[2] / EbbDierData.SCHAAL + r;
            _boven = t < _boven ? t : _boven;
            _onder = o > _onder ? o : _onder;
        }
    }

    // Belletje (blad v11): ellips rx 30, ry 22 in 1/260 D om het midden van het dier, vlak 0055AA, rand 00FFFF
    // (2 px onder 390, 3 px daarboven), wit glimpje linksboven, dan het dier er opnieuw in (zwaartepunt cx, cy).
    function belletje(dc as Graphics.Dc, d as Number, i as Number, cx as Number, cy as Number, m as Number) as Void {
        var soort = EbbTrouw.heeft(i) ? EbbDierPlaatje.GEVONDEN : EbbDierPlaatje.SILHOUET;
        if (!EbbDierVoorraad.bereid(i, m, soort)) {
            return;
        }
        var g = EbbDierMaat.grenzen(i);
        var mx = cx + (g[0] + g[1]) * m / (2 * EbbDierData.SCHAAL);
        var my = cy + (g[2] + g[3]) * m / (2 * EbbDierData.SCHAAL);
        // Keuring bouw 7 punt 4: het belletje ruim om hoge dieren (maanvis, reuzeninktvis): minstens 5/260 D lucht
        // rond het kader van het dier, hoogstens 31 bij 27 zodat het de buren niet raakt.
        var rx = EbbTeken.px(d, 30);
        var ry = EbbTeken.px(d, 22);
        var hw = (g[1] - g[0]) * m / (2 * EbbDierData.SCHAAL) + EbbTeken.px(d, 5);
        var hh = (g[3] - g[2]) * m / (2 * EbbDierData.SCHAAL) + EbbTeken.px(d, 5);
        rx = hw > rx ? hw : rx;
        ry = hh > ry ? hh : ry;
        rx = rx > EbbTeken.px(d, 31) ? EbbTeken.px(d, 31) : rx;
        ry = ry > EbbTeken.px(d, 27) ? EbbTeken.px(d, 27) : ry;
        dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);
        dc.fillEllipse(mx, my, rx, ry);
        dc.setColor(0x00FFFF, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d < 390 ? 2 : 3);
        dc.drawEllipse(mx, my, rx, ry);
        dc.setPenWidth(1);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_WHITE);
        var gl = EbbTeken.px(d, 3);
        dc.fillCircle(mx - rx * 62 / 100, my - ry * 50 / 100, gl < 2 ? 2 : gl);
        EbbDierVoorraad.teken(dc, i, cx, cy, m, soort);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        // Thuiswater (Thuis.mc, vakken in ThuisSchermen.mc); het blad met de dieren is daarom doorzichtig, zonder palet.
        var water = EbbThuisSchermen.seaLog(dc, d, self);
        var blad = bladVan(keuze);
        // Keuring bouw 2 punt 1 (watchdog): de dieren van een blad komen in één plaatje op zwart, één laag per beurt.
        // Is het plaatje af, dan kost een beurt alleen nog het plakken. Opnieuw na een ander blad of een nieuw dier.
        var ox = (d * 0.13).toNumber();
        var sleutel = blad * 100000000 + EbbTrouw.getal(EbbTrouw.BITS) % 100000000;
        var ref = _plaatje;
        var bb = (ref != null) ? ref.get() : null;
        if (bb == null || sleutel != _sleutel) {
            bouwBlad(d, blad);
            ref = Graphics.createBufferedBitmap({:width => (d * 0.74).toNumber(), :height => _onder - _boven + 2});
            _plaatje = ref;
            bb = ref.get();
            var pdc0 = (bb as Graphics.BufferedBitmap).getDc();
            pdc0.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
            pdc0.clear();
            _sleutel = sleutel;
            _getekend = 0;
            _laag = 0;
            // Plaatjesrun 42966268846: op FR255 trapte de watchdog op blad 2 (opbouw plus een silhouet in één beurt).
            // Daarom in de beurt van de opbouw nog geen dier.
            _opbouwBeurt = true;
        }
        var oy = _boven;
        var plaatje = bb as Graphics.BufferedBitmap;
        var pdc = plaatje.getDc();
        var gekozenY = 0;
        var gekozenX = 0;
        var gekozenM = 0;
        var nu = 0;
        var n = opBlad(blad);
        for (var k = 0; k < n; k += 1) {
            var i = eerste(blad) + k;
            var p = plek(d, blad, k);
            if (k >= _getekend && nu < NIEUW_PER_BEURT && !_opbouwBeurt) {
                // Eén laag per beurt: gevonden 4 keer stickerrand en dan het dier, silhouet 8 keer rand en het vlak.
                if (tekenLaag(pdc, i, p[0] - ox, p[1] - oy, p[2])) {
                    _getekend = k + 1;
                    _laag = 0;
                }
                nu += 1;
            }
            if (i == keuze) {
                gekozenX = p[0];
                gekozenY = p[1];
                gekozenM = p[2];
            }
        }
        _opbouwBeurt = false;
        dc.drawBitmap(ox, oy, plaatje);
        // Tekst na het plaatje, zodat het zwarte raster de tekst niet bedekt (blad v9: kop y 28, telling 58, naam 184, regel 210).
        EbbTeken.tekst260(dc, d, 28, EbbTeken.fS(), "sea log", EbbTeken.SCHUIM);
        // Keuring bouw 6 punt 6: de bonus telt zichtbaar mee ("24 of 24 + bonus").
        var telling = EbbTrouw.aantalGewoon() + " of " + EbbTrouw.totaal() + (EbbTrouw.heeft(EbbTrouw.ZEEKOMKOMMER) ? " + bonus" : "");
        EbbTeken.tekst260(dc, d, 58, EbbTeken.fX(), telling, Graphics.COLOR_WHITE);
        if (blad == BLADEN - 1) {
            EbbTeken.tekst260(dc, d, 88, EbbTeken.fX(), "bonus", EbbTeken.LICHT);
        }
        // Mila blad v11 punt 2 (keuring bouw 6 punt 5): de keuze is een belletje om het dier, geen stip eronder.
        // Pas als het blad af is (de beurt kost dan alleen plakken), en pas als het losse dierplaatje klaar is,
        // zodat het belletje het dier nooit even bedekt.
        if (n > 1 && _getekend >= n) {
            belletje(dc, d, keuze, gekozenX, gekozenY, gekozenM);
        }
        var naam = (EbbTrouw.bonus(keuze) && !EbbTrouw.heeft(keuze)) ? "Bonus" : EbbDierData.NAMEN[keuze];
        EbbTeken.tekst260(dc, d, 184, EbbTeken.fS(), naam, Graphics.COLOR_WHITE);
        EbbTeken.tekst260(dc, d, 210, EbbTeken.fX(), regel(keuze), EbbTeken.LICHTCYAAN);
        // Bladstippen op y 236: actief vol in schuim, de andere als ring in lichtcyaan (leesbaar op het thuiswater).
        var stap = EbbTeken.px(d, 9);
        var rb = EbbTeken.px(d, 2);
        rb = rb < 2 ? 2 : rb;
        var yStip = EbbTeken.px(d, 236);
        dc.setPenWidth(1);
        for (var b = 0; b < BLADEN; b += 1) {
            var x = w / 2 + (b * 2 - (BLADEN - 1)) * stap / 2;
            if (b == blad) {
                dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
                dc.fillCircle(x, yStip, rb);
            } else {
                dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
                dc.drawCircle(x, yStip, rb);
            }
        }
        if (_getekend < n || !water) {
            WatchUi.requestUpdate();
        }
    }
}

class DierenDelegate extends WatchUi.BehaviorDelegate {
    private var _view as DierenView;

    function initialize(view as DierenView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onNextPage() as Boolean {
        _view.verschuif(1);
        return true;
    }

    function onPreviousPage() as Boolean {
        _view.verschuif(-1);
        return true;
    }

    function onSelect() as Boolean {
        if (EbbTrouw.kies(_view.keuze)) {
            WatchUi.requestUpdate();
        }
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
    }
}
