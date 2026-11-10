import Toybox.Application;
import Toybox.Lang;

// Eis 7 en 8: rekenwerk voor duikprofiel, getijdenlijn, record en dieren, los van het tekenen zodat het te toetsen is.
module EbbProfiel {
    // Duikprofiel: per ronde een V. Geeft punten [x, y]: begin aan de oppervlakte, diepste punt in het midden
    // van de ronde op diepte evenredig met de inhoudtijd (langste ronde is de volle hoogte), weer naar boven.
    function vPunten(tijden as Array<Number>, x0 as Number, y0 as Number, w as Number, h as Number) as Array<Array<Number> > {
        var punten = [[x0, y0]] as Array<Array<Number> >;
        var n = tijden.size();
        if (n == 0) {
            return punten;
        }
        var max = tijden[diepste(tijden)];
        for (var i = 0; i < n; i += 1) {
            var diep = (max > 0) ? (h * tijden[i]) / max : 0;
            punten.add([x0 + (w * (2 * i + 1)) / (2 * n), y0 + diep]);
            punten.add([x0 + (w * (i + 1)) / n, y0]);
        }
        return punten;
    }

    // Index van de langste inhoudtijd (bij gelijk de eerste); daar komt het lichtpuntje.
    function diepste(tijden as Array<Number>) as Number {
        var beste = 0;
        for (var i = 1; i < tijden.size(); i += 1) {
            if (tijden[i] > tijden[beste]) {
                beste = i;
            }
        }
        return beste;
    }

    // Koraal alleen bij een nieuw record over alle tijd (strikt langer dan het oude record).
    function nieuwRecord(tijden as Array<Number>, record as Number) as Boolean {
        return tijden.size() > 0 && tijden[diepste(tijden)] > record;
    }

    // Getijdenlijn: 56 dagen, oudste eerst, eindigend op vandaag. Per dag [beste, gemiddelde] of null (gat).
    function getijden(opslag as EbbOpslag, vandaag as Number) as Array<Array<Number> or Null> {
        var lijn = [] as Array<Array<Number> or Null>;
        for (var d = vandaag - EbbOpslag.DAGEN + 1; d <= vandaag; d += 1) {
            var g = opslag.dag(d);
            lijn.add(g == null ? null : [g[0], g[1]] as Array<Number>);
        }
        return lijn;
    }

    // Dieren bij 1:00, 1:30, 2:00 en 3:00 inhouden (vis, kwal, schildpad, walvis), elk 8 s in beeld.
    const DREMPELS = [60000, 90000, 120000, 180000] as Array<Number>;
    const IN_BEELD_MS = 8000;

    // Welk dier zwemt er op inhoudtijd ms voorbij: 0 tot 3, of -1.
    function dier(ms as Number) as Number {
        for (var i = DREMPELS.size() - 1; i >= 0; i -= 1) {
            if (ms >= DREMPELS[i] && ms < DREMPELS[i] + IN_BEELD_MS) {
                return i;
            }
        }
        return -1;
    }

    // Hoogste drempel die gehaald is (voor het logboek), of -1.
    function gehaald(ms as Number) as Number {
        for (var i = DREMPELS.size() - 1; i >= 0; i -= 1) {
            if (ms >= DREMPELS[i]) {
                return i;
            }
        }
        return -1;
    }

    // Gezien-bits in de opslag. Geeft true als dit dier voor het eerst gezien is (dan wordt het één keer bewaard).
    function eersteKeer(i as Number) as Boolean {
        var bits = Application.Storage.getValue("dieren");
        var b = (bits instanceof Number) ? bits as Number : 0;
        if ((b & (1 << i)) != 0) {
            return false;
        }
        Application.Storage.setValue("dieren", b | (1 << i));
        return true;
    }

    function dierenGezien() as Number {
        var bits = Application.Storage.getValue("dieren");
        return (bits instanceof Number) ? bits as Number : 0;
    }

    function record() as Number {
        var r = Application.Storage.getValue("record");
        return (r instanceof Number) ? r as Number : 0;
    }

    function bewaarRecord(s as Number) as Void {
        Application.Storage.setValue("record", s);
    }
}

// Eis 2: het veiligheidsscherm komt alleen tot het bevestigd is, en weer na "opnieuw tonen" in de instellingen.
module EbbVeilig {
    const SLEUTEL = "veilig";

    function moetTonen() as Boolean {
        return Application.Storage.getValue(SLEUTEL) != true;
    }

    function bevestig() as Void {
        Application.Storage.setValue(SLEUTEL, true);
    }

    function opnieuwTonen() as Void {
        Application.Storage.deleteValue(SLEUTEL);
    }
}
