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

    // Betaald: de drager kiest de drie velden uit negen soorten.
    (:betaald)
    function velden() as Array<Number> {
        return Keuze.leesVelden();
    }

    // Gratis: één vast thema (Tide), geen instellingen. Blijft altijd werken.
    (:gratis)
    const BETAALD = false;

    (:gratis)
    function thema() as Number {
        return Thema.TIDE;
    }

    // Gratis: drie vaste velden, hartslag, stress en stappen.
    (:gratis)
    function velden() as Array<Number> {
        return [Veld.HART, Veld.STRESS, Veld.STAPPEN] as Array<Number>;
    }
}
