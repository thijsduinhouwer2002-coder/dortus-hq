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

    // Bouwstraat: elk proefhorloge een ander thema, zodat alle vier in beeld komen (Thema.voorProef). De proef van
    // de gratis versie (proef-gratis.jungle) toont zijn echte, vaste thema: dat is juist wat we willen zien.
    (:proef)
    function thema(gekozen as Number, breedte as Number) as Number {
        return Soort.BETAALD ? Thema.voorProef(breedte) : gekozen;
    }

    // Winkel: altijd het thema dat de drager koos.
    (:winkel)
    function thema(gekozen as Number, breedte as Number) as Number {
        return gekozen;
    }

    // Bouwstraat (run 134): de betaalde proef toont op vier horloges andere velden, zodat de zes nieuwe
    // pictogrammen groot en klein in beeld komen: breedte 454 en 240 vlam, trap en stopwatch; 260 en 208 speld,
    // accu en thermometer. De andere horloges (176, 320, 360, 390) houden de keuze, dus hart, bliksem en schoen
    // blijven ook in beeld (punt van de keurder). De gratis proef toont zijn echte, vaste velden.
    (:proef)
    function velden(gekozen as Array<Number>, breedte as Number) as Array<Number> {
        if (!Soort.BETAALD) {
            return gekozen;
        }
        if (breedte == 454 || breedte == 240) {
            return [Veld.CALORIE, Veld.TRAPPEN, Veld.MINUTEN] as Array<Number>;
        }
        if (breedte == 260 || breedte == 208) {
            return [Veld.AFSTAND, Veld.ACCU, Veld.TEMP] as Array<Number>;
        }
        return gekozen;
    }

    // Winkel: altijd de velden die de drager koos.
    (:winkel)
    function velden(gekozen as Array<Number>, breedte as Number) as Array<Number> {
        return gekozen;
    }

    // Bouwstraat (run 134): de simulator geeft 0 voor calorieën, trappen, minuten en afstand en nooit vorst. De
    // betaalde proef toont daarom een gewone dag: 1.840 calorieën, 12 trappen, 145 minuten, 12,4 km en 4 graden
    // onder nul, zodat een vol veld en het minteken in beeld komen. Accu en de drie oude soorten blijven echt.
    (:proef)
    function veld(soort as Number, echt as Number?) as Number? {
        if (!Soort.BETAALD) {
            return echt;
        }
        if (soort == Veld.CALORIE) {
            return 1840;
        }
        if (soort == Veld.TRAPPEN) {
            return 12;
        }
        if (soort == Veld.MINUTEN) {
            return 145;
        }
        if (soort == Veld.AFSTAND) {
            return 124;
        }
        if (soort == Veld.TEMP) {
            return -4;
        }
        return echt;
    }

    // Winkel: altijd wat het horloge geeft, ook niets.
    (:winkel)
    function veld(soort as Number, echt as Number?) as Number? {
        return echt;
    }
}
