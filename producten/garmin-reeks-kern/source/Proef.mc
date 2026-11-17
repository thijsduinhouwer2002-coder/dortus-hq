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
}
