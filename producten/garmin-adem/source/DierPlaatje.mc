import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Plaatjesrun 42963243152: op de FR255 trapte de watchdog op het inhoudscherm met de krab (zee, belletjes, hart en
// het dier met stickerrand in één beurt). Daarom het dier één keer in een eigen plaatje, één laag per beurt
// (4 keer rand, dan lijf en ogen); daarna kost een beurt alleen het plakken.
// Keuring bouw 4 punt 1: op AMOLED stond er een zwart blok achter het dier. Het palet met COLOR_TRANSPARENT werkt
// op MIP (FR255, fenix 7) wel, maar op AMOLED kwam de doorzichtige kleur zwart uit. Op AMOLED daarom een plaatje
// zonder palet (volle kleur met doorzichtigheid, alle horloges hebben API 5); op MIP het bewezen palet van 64 kleuren.
// Punt 2: ook het silhouet (4 keer rand, vlak, kenmerk: 6 lagen) gaat via dit plaatje.
class EbbDierPlaatje {
    var dier as Number;
    var maat as Number;
    var sil as Boolean;
    var stap as Number = 0;
    var links as Number = 0;   // van het plaatje tot het zwaartepunt
    var boven as Number = 0;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;

    function initialize(i as Number, m as Number, s as Boolean) {
        dier = i;
        maat = m;
        sil = s;
        var g = EbbDierMaat.grenzen(i);
        var r = (s ? 2 : EbbDierData.randPx(m)) + 1;
        links = -g[0] * m / EbbDierData.SCHAAL + r;
        boven = -g[2] * m / EbbDierData.SCHAAL + r;
        var br = links + g[1] * m / EbbDierData.SCHAAL + r + 1;
        var ho = boven + g[3] * m / EbbDierData.SCHAAL + r + 1;
        // Beelden run 42973269112 (FR255): met het palet kwam op MIP soms een wit blok achter het dier (krabsilhouet op
        // 6c, walvis bij sea complete). Daarom nu overal een plaatje zonder palet, zoals op AMOLED al goed ging.
        _ref = Graphics.createBufferedBitmap({:width => br, :height => ho});
        var bb = (_ref as Graphics.BufferedBitmapReference).get() as Graphics.BufferedBitmap;
        var dc = bb.getDc();
        dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
        dc.clear();
    }

    static function amoled() as Boolean {
        var ds = System.getDeviceSettings();
        return (ds has :requiresBurnInProtection) && ds.requiresBurnInProtection;
    }

    function lagen() as Number {
        return sil ? 6 : 5;
    }

    function klaar() as Boolean {
        return stap >= lagen();
    }

    // Eén laag erbij; geeft true als het plaatje af is.
    function verder() as Boolean {
        if (klaar()) {
            return true;
        }
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            return false;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        laag(dc, dier, links, boven, maat, sil, stap);
        stap += 1;
        return klaar();
    }

    // Plak het dier met zijn zwaartepunt op (cx, cy).
    function plak(dc as Graphics.Dc, cx as Number, cy as Number) as Void {
        var bb = (_ref != null) ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb != null) {
            dc.drawBitmap(cx - links, cy - boven, bb as Graphics.BufferedBitmap);
        }
    }

    // De enige tekenfunctie voor een dier (keuring en besluit Thijs 11 nov 07:41): laag stap van dier i met zijn
    // zwaartepunt op (x, y). Gevonden: 4 keer stickerrand, dan lijf en ogen (5 lagen). Silhouet: 4 keer rand, vlak,
    // kenmerk (6 lagen). Het plaatje hieronder en het blad van de sea log gebruiken allebei deze functie.
    static function laag(dc as Graphics.Dc, i as Number, x as Number, y as Number, maat as Number, sil as Boolean, stap as Number) as Void {
        if (sil) {
            if (stap < 4) {
                EbbDierData.delen(dc, i, x + EbbDierData.RAND_DX[stap] * 2, y + EbbDierData.RAND_DY[stap] * 2, maat, EbbDierData.SIL_RAND, 1);
            } else if (stap == 4) {
                EbbDierData.delen(dc, i, x, y, maat, EbbDierData.SIL_VLAK, 1);
            } else {
                EbbDierData.delen(dc, i, x, y, maat, EbbDierData.SIL_RAND, 3);
            }
        } else {
            var k = EbbDierData.randPx(maat);
            if (stap < 4) {
                EbbDierData.delen(dc, i, x + EbbDierData.RAND_DX[stap] * k, y + EbbDierData.RAND_DY[stap] * k, maat, EbbDierData.TINT[i][3], 2);
            } else {
                var o = EbbDierData.delen(dc, i, x, y, maat, -1, 0);
                EbbDierData.ogen(dc, i, o, x, y, maat);
            }
        }
    }
}


// Keuring bouw 4 punt 2: elk dierscherm (menu, eindschermen, Calm-einde) tekent zijn dier via een plaatje, één laag
// per beurt, zodat de watchdog nergens meer de zee en een heel dier in één beurt ziet. Hoogstens vier plaatjes
// tegelijk; daarna begint de voorraad opnieuw.
module EbbDierVoorraad {
    var _plaatjes as Dictionary<String, EbbDierPlaatje> = {} as Dictionary<String, EbbDierPlaatje>;

    // Tekent dier i (sil: als silhouet) met zwaartepunt op (cx, cy); true als het er staat, anders volgt er een beurt.
    function teken(dc as Graphics.Dc, i as Number, cx as Number, cy as Number, maat as Number, sil as Boolean) as Boolean {
        var sleutel = i + "/" + maat + (sil ? "s" : "");
        var p = _plaatjes[sleutel];
        if (p == null) {
            if (_plaatjes.size() >= 4) {
                _plaatjes = {} as Dictionary<String, EbbDierPlaatje>;
            }
            p = new EbbDierPlaatje(i, maat, sil);
            _plaatjes[sleutel] = p;
        }
        if ((p as EbbDierPlaatje).verder()) {
            (p as EbbDierPlaatje).plak(dc, cx, cy);
            return true;
        }
        WatchUi.requestUpdate();
        return false;
    }
}
