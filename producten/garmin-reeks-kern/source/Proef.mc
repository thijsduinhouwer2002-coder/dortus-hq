import Toybox.Lang;

// Wat alleen de bouwstraat nodig heeft. De winkel bouwt met monkey.jungle (laat :proef weg), de bouwstraat maakt
// de schermafbeeldingen met proef.jungle (laat :winkel weg). Zo zit er in het winkelpakket geen proefgedrag.
module Proef {
    const WIT = 0;
    const WAKKER = 1;
    const SLAAP = 2;

    // Bouwstraat: eerst 8 s een wit scherm (daarmee vindt tel_slaap.py het scherm in de schermafbeelding),
    // dan 10 s wakker, dan het slaapbeeld, omdat de simulator de slaapstand niet vanzelf aanzet.
    (:proef)
    function fase(ms as Number) as Number {
        if (ms < 8000) {
            return WIT;
        }
        if (ms < 18000) {
            return WAKKER;
        }
        return SLAAP;
    }

    // Winkel: altijd wakker; alleen het horloge zelf zet de slaapstand aan.
    (:winkel)
    function fase(ms as Number) as Number {
        return WAKKER;
    }

    // Teller voor het verschuiven van het slaapbeeld. Bouwstraat: elke drie tikken een stap, zodat twee
    // schermafbeeldingen vier seconden na elkaar verschillen.
    (:proef)
    function schuifTel(minuut as Number, tik as Number) as Number {
        return tik / 3;
    }

    // Winkel: elke minuut een stap.
    (:winkel)
    function schuifTel(minuut as Number, tik as Number) as Number {
        return minuut;
    }

    // Bouwstraat: een vaste dag per thema in plaats van de geschiedenis van de simulator (die loopt in één streep
    // van 93 naar 5). Zo zien we op de beelden een dag met een dip en een stijging (moet van Daan voor plaatje 1),
    // het plafond bij 100 (Kelp) en het bootje aan de grond (Night). Dezelfde standen als het blad van Mila.
    (:proef)
    function bb(echt as Array<Number>, thema as Number) as Array<Number> {
        if (thema == Thema.KELP) {
            return [80, 86, 93, 98, 100, 100] as Array<Number>;
        }
        if (thema == Thema.NIGHT) {
            return [30, 22, 15, 9, 4, 2] as Array<Number>;
        }
        return [62, 58, 52, 47, 44, 52, 66, 80, 88, 85, 78, 72] as Array<Number>;
    }

    // Winkel: altijd de echte geschiedenis van het horloge.
    (:winkel)
    function bb(echt as Array<Number>, thema as Number) as Array<Number> {
        return echt;
    }
}
