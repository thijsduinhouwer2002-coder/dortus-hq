import Toybox.Lang;

// Gratis en betaald uit één bron (stap (e) van de kern). monkey.jungle en proef.jungle laten :gratis weg,
// gratis.jungle laat :betaald weg. Alles wat tussen de twee versies verschilt staat hier, nergens anders.
module Soort {
    // Betaald: de drager kiest het thema in Garmin Connect.
    (:betaald)
    const BETAALD = true;

    (:betaald)
    function thema() as Number {
        return Keuze.leesThema();
    }

    // Gratis: één vast thema (Tide), geen instellingen. Blijft altijd werken.
    (:gratis)
    const BETAALD = false;

    (:gratis)
    function thema() as Number {
        return Thema.TIDE;
    }
}
