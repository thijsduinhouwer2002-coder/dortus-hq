import Toybox.Application;
import Toybox.Lang;

// Wat de drager kiest in Garmin Connect (resources/settings/settings.xml). Stap (d) van de kern.
module Keuze {
    // Maakt van wat de instellingen teruggeven een geldig thema. De telefoon stuurt soms een tekst of een
    // kommagetal in plaats van een heel getal; niets, onzin of buiten de lijst: Tide.
    function thema(ruw as Object?) as Number {
        var n = getal(ruw);
        if (n == null) {
            return Thema.TIDE;
        }
        return Thema.geldig(n as Number);
    }

    // Heel getal uit wat de telefoon stuurt, of null als er geen getal in zit.
    function getal(ruw as Object?) as Number? {
        var n = null;
        if (ruw instanceof Lang.Number) {
            n = ruw as Number;
        } else if (ruw instanceof Lang.Float) {
            n = (ruw as Float).toNumber();
        } else if (ruw instanceof Lang.Double) {
            n = (ruw as Double).toNumber();
        } else if (ruw instanceof Lang.Long) {
            n = (ruw as Long).toNumber();
        } else if (ruw instanceof Lang.String) {
            // Geen getal in de tekst: toNumber geeft null.
            n = (ruw as String).toNumber();
        }
        return n;
    }

    // De soort van een veld uit de instellingen. Niets, onzin of buiten de lijst: de standaard van dat veld.
    function veld(ruw as Object?, standaard as Number) as Number {
        var n = getal(ruw);
        if (n == null) {
            return standaard;
        }
        return Veld.geldig(n as Number, standaard);
    }

    // Leest de drie gekozen velden (links, midden, rechts). Standaard hartslag, stress, stappen.
    function leesVelden() as Array<Number> {
        var sleutels = ["Veld1", "Veld2", "Veld3"] as Array<String>;
        var uit = [Veld.HART, Veld.STRESS, Veld.STAPPEN] as Array<Number>;
        for (var i = 0; i < 3; i++) {
            var ruw = null;
            try {
                ruw = Application.Properties.getValue(sleutels[i]);
            } catch (e instanceof Lang.Exception) {
                ruw = null;
            }
            uit[i] = veld(ruw, uit[i]);
        }
        return uit;
    }

    // Leest het gekozen thema. Bestaat de instelling niet of geeft het horloge een fout: Tide, de plaat stopt niet.
    function leesThema() as Number {
        var ruw = null;
        try {
            ruw = Application.Properties.getValue("Thema");
        } catch (e instanceof Lang.Exception) {
            ruw = null;
        }
        return thema(ruw);
    }
}
