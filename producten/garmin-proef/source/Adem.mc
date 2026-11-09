import Toybox.Lang;
import Toybox.Math;

// Rekenwerk voor een ademritme, los van het scherm zodat het te testen is.
// Patroon: in, vast, uit, leeg (alle tijden in ms).
module Adem {
    // Grootte van de vorm: 0.0 is klein (leeg), 1.0 is groot (vol).
    function fractie(t as Number, inMs as Number, vastMs as Number, uitMs as Number, leegMs as Number) as Float {
        var cyclus = inMs + vastMs + uitMs + leegMs;
        if (cyclus <= 0) {
            return 0.0;
        }
        var p = t % cyclus;
        if (p < inMs) {
            return zacht(p.toFloat() / inMs);
        }
        p -= inMs;
        if (p < vastMs) {
            return 1.0;
        }
        p -= vastMs;
        if (p < uitMs) {
            return 1.0 - zacht(p.toFloat() / uitMs);
        }
        return 0.0;
    }

    // Naam van de fase op tijd t.
    function fase(t as Number, inMs as Number, vastMs as Number, uitMs as Number, leegMs as Number) as String {
        var cyclus = inMs + vastMs + uitMs + leegMs;
        if (cyclus <= 0) {
            return "";
        }
        var p = t % cyclus;
        if (p < inMs) {
            return "in";
        }
        if (p < inMs + vastMs) {
            return "vast";
        }
        if (p < inMs + vastMs + uitMs) {
            return "uit";
        }
        return "leeg";
    }

    // Zachte overgang (langzaam beginnen en eindigen), x van 0 tot 1.
    function zacht(x as Float) as Float {
        return ((1.0 - Math.cos(Math.PI * x)) / 2.0).toFloat();
    }
}
