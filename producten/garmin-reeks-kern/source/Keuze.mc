import Toybox.Application;
import Toybox.Lang;

// Wat de drager kiest in Garmin Connect (resources/settings/settings.xml). Stap (d) van de kern.
module Keuze {
    // Maakt van wat de instellingen teruggeven een geldig thema. De telefoon stuurt soms een tekst of een
    // kommagetal in plaats van een heel getal; niets, onzin of buiten de lijst: Tide.
    function thema(ruw as Object?) as Number {
        var n as Number? = null;
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
        if (n == null) {
            return Thema.TIDE;
        }
        return Thema.geldig(n as Number);
    }

    // Leest het gekozen thema. Bestaat de instelling niet of geeft het horloge een fout: Tide, de plaat stopt niet.
    function leesThema() as Number {
        var ruw as Object? = null;
        try {
            ruw = Application.Properties.getValue("Thema");
        } catch (e instanceof Lang.Exception) {
            ruw = null;
        }
        return thema(ruw);
    }
}
