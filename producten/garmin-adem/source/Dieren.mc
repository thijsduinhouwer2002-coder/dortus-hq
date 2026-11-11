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
    const NIEUW_PER_BEURT = 3;

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
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.15).toNumber(), Graphics.FONT_SMALL, "sea log", midden);
        dc.drawText(w / 2, (d * 0.22).toNumber(), Graphics.FONT_SMALL, EbbTrouw.aantalGewoon() + " of " + EbbTrouw.totaal(), midden);
        var blad = keuze / PER_BLAD;
        var maat = (d * 0.078).toNumber();
        var gekozenY = 0;
        var gekozenX = 0;
        // Keuring bouw 2 punt 1: hoogstens NIEUW_PER_BEURT nieuwe plaatjes per tekenbeurt, de rest in de volgende beurt
        // (elke beurt krijgt een eigen watchdog). Klaar staande plaatjes kosten bijna niets.
        var nieuw = 0;
        var later = false;
        for (var k = 0; k < PER_BLAD; k += 1) {
            var i = blad * PER_BLAD + k;
            if (i >= EbbTrouw.DIEREN.size()) {
                break;
            }
            var x = (d * (0.29 + 0.21 * (k % 3))).toNumber();
            var y = (d * (0.335 + 0.14 * (k / 3))).toNumber();
            var soort = EbbTrouw.heeft(i) ? 0 : 1;
            if (!EbbDierData.klaar(i, maat, soort)) {
                if (nieuw >= NIEUW_PER_BEURT) {
                    later = true;
                } else {
                    nieuw += 1;
                }
            }
            if (later && !EbbDierData.klaar(i, maat, soort)) {
                // komt in de volgende beurt
            } else if (soort == 0) {
                EbbDierData.teken(dc, i, x, y, maat, -1);
            } else {
                EbbDierData.silhouet(dc, i, x, y, maat);
            }
            if (i == keuze) {
                gekozenX = x;
                gekozenY = y;
            }
        }
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
