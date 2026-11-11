import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Sea log volgens blad v7 en v8 (keuring bouw 1 punt 8): raster 3 x 3 over drie bladen met Mila's dieren als data.
// Gevonden dieren in eigen kleuren met witte stickerrand, de rest als silhouet met kenmerk. Bovenaan "sea log" en
// "8 of 24", onderaan naam en eerlijk wat er nog nodig is, daaronder drie bladstippen. Omhoog en omlaag (of vegen)
// verschuift de keuze; select kiest een gevonden dier dat met je meezwemt.
class DierenView extends WatchUi.View {
    var keuze as Number = 0;
    const PER_BLAD = 9;
    // Run 42953647184: met 3 per beurt (15 keer tekenen) trapte de watchdog op de FR255; 1 dier (5 keer) per beurt.
    const NIEUW_PER_BEURT = 1;
    var _plaatje as Graphics.BufferedBitmapReference or Null = null;
    var _sleutel as Number = -1;
    var _getekend as Number = 0;

    // De 64 kleuren van het MIP-scherm: alle dieren en silhouetten gebruiken alleen deze, 1 byte per pixel.
    function palet() as Array<Number> {
        var p = [] as Array<Number>;
        for (var r = 0; r < 4; r += 1) {
            for (var g = 0; g < 4; g += 1) {
                for (var b = 0; b < 4; b += 1) {
                    p.add(r * 0x550000 + g * 0x5500 + b * 0x55);
                }
            }
        }
        return p;
    }

    // Voor de toets: staat het hele blad in het plaatje?
    function klaar() as Boolean {
        var blad = keuze / PER_BLAD;
        return _plaatje != null && (_getekend >= PER_BLAD || blad * PER_BLAD + _getekend >= EbbTrouw.DIEREN.size());
    }

    function initialize() {
        View.initialize();
        var m = EbbTrouw.zwemmer();
        keuze = m >= 0 ? m : 0;
    }

    function bladen() as Number {
        return (EbbTrouw.DIEREN.size() + PER_BLAD - 1) / PER_BLAD;
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
            return (EbbTrouw.zwemmer() == i) ? "swims with you" : "found · select to pick";
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

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        var blad = keuze / PER_BLAD;
        var maat = (d * 0.078).toNumber();
        // Keuring bouw 2 punt 1 (watchdog): de dieren van een blad komen in één plaatje op zwart (het raster), dat over
        // een paar beurten vol getekend wordt: hoogstens NIEUW_PER_BEURT dieren per beurt, elke beurt een eigen watchdog.
        // Is het plaatje af, dan kost een beurt alleen nog het plakken. Opnieuw na een ander blad of een nieuw dier.
        var ox = (d * 0.13).toNumber();
        var oy = (d * 0.20).toNumber();
        var sleutel = blad * 100000000 + EbbTrouw.getal(EbbTrouw.BITS) % 100000000;
        var ref = _plaatje;
        var bb = (ref != null) ? ref.get() : null;
        if (bb == null || sleutel != _sleutel) {
            ref = Graphics.createBufferedBitmap({:width => (d * 0.74).toNumber(), :height => (d * 0.56).toNumber(), :palette => palet()});
            _plaatje = ref;
            bb = ref.get();
            var pdc0 = (bb as Graphics.BufferedBitmap).getDc();
            pdc0.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
            pdc0.clear();
            _sleutel = sleutel;
            _getekend = 0;
        }
        var plaatje = bb as Graphics.BufferedBitmap;
        var pdc = plaatje.getDc();
        var gekozenY = 0;
        var gekozenX = 0;
        var nu = 0;
        for (var k = 0; k < PER_BLAD; k += 1) {
            var i = blad * PER_BLAD + k;
            if (i >= EbbTrouw.DIEREN.size()) {
                break;
            }
            var x = (d * (0.29 + 0.21 * (k % 3))).toNumber();
            var y = (d * (0.335 + 0.14 * (k / 3))).toNumber();
            if (k >= _getekend && nu < NIEUW_PER_BEURT) {
                if (EbbTrouw.heeft(i)) {
                    EbbDierData.teken(pdc, i, x - ox, y - oy, maat, -1);
                } else {
                    EbbDierData.silhouet(pdc, i, x - ox, y - oy, maat);
                }
                nu += 1;
                _getekend = k + 1;
            }
            if (i == keuze) {
                gekozenX = x;
                gekozenY = y;
            }
        }
        var later = _getekend < PER_BLAD && blad * PER_BLAD + _getekend < EbbTrouw.DIEREN.size();
        dc.drawBitmap(ox, oy, plaatje);
        // Kop na het plaatje, zodat het zwarte raster de tekst niet bedekt.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        // Beelden run 42953647184: "sea log" en "8 of 24" liepen in elkaar; nu de telling kleiner eronder.
        dc.drawText(w / 2, (d * 0.135).toNumber(), Graphics.FONT_SMALL, "sea log", midden);
        dc.drawText(w / 2, (d * 0.135).toNumber() + dc.getFontHeight(Graphics.FONT_SMALL) / 2 + dc.getFontHeight(Graphics.FONT_XTINY) / 2, Graphics.FONT_XTINY, EbbTrouw.aantalGewoon() + " of " + EbbTrouw.totaal(), midden);
        // Keuzestip vast onder het gekozen dier.
        dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
        var rs = (d * 0.011).toNumber();
        rs = rs < 3 ? 3 : rs;
        dc.fillCircle(gekozenX, gekozenY + (d * 0.065).toNumber(), rs);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var naam = (EbbTrouw.bonus(keuze) && !EbbTrouw.heeft(keuze)) ? "Bonus" : EbbDierData.NAMEN[keuze];
        dc.drawText(w / 2, (d * 0.735).toNumber(), Graphics.FONT_SMALL, naam, midden);
        var tekst = regel(keuze);
        var f = (dc.getTextWidthInPixels(tekst, Graphics.FONT_SMALL) <= d * 0.74) ? Graphics.FONT_SMALL : Graphics.FONT_XTINY;
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.81).toNumber(), f, tekst, midden);
        // Bladstippen: actief schuim, de andere 00AAFF (blad v8).
        var n = bladen();
        var stap = (d * 0.04).toNumber();
        var rb = (d * 0.009).toNumber();
        rb = rb < 2 ? 2 : rb;
        for (var b = 0; b < n; b += 1) {
            var kleur = (b == blad) ? EbbTeken.SCHUIM : EbbTeken.ZEE_KLEUR[0];
            dc.setColor(kleur, kleur);
            dc.fillCircle(w / 2 + (b - (n - 1) / 2.0) * stap, (d * 0.875).toNumber(), rb);
        }
        if (later) {
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
