import Toybox.Lang;
import Toybox.Math;

// Klok en fases van een sessie, zonder tekenwerk (ontwerp eis 3, 4 en 5).
// Alle tijden in ms. Elke fasegrens wordt berekend vanaf het begin van het stuk (segment),
// nooit door timerstappen op te tellen, zodat er geen afwijking opbouwt.
module Ebb {
    enum Fase {
        FASE_ADEMEN = 0,
        FASE_INHOUDEN = 1,
        FASE_HERSTEL = 2,
        FASE_KLAAR = 3,
        FASE_RUSTIG = 4
    }

    // Zachte overgang (langzaam beginnen en eindigen), x van 0 tot 1.
    function zacht(x as Float) as Float {
        return ((1.0 - Math.cos(Math.PI * x)) / 2.0).toFloat();
    }

    // Rondes: ademhalingen in vast tempo, dan inhouden tot een knop, dan herstel.
    class Rondes {
        var ademhalingen as Number;   // per ronde
        var tempoMs as Number;        // duur van in en ook van uit
        var rondes as Number;
        var herstelMs as Number;

        var fase as Fase = FASE_ADEMEN;
        var ronde as Number = 0;          // 0-gebaseerd
        var segmentStart as Number = 0;   // begin van het huidige stuk
        var inhoudtijden as Array<Number> = [] as Array<Number>;

        function initialize(ademhalingen as Number, tempoMs as Number, rondes as Number, herstelMs as Number, startMs as Number) {
            self.ademhalingen = ademhalingen;
            self.tempoMs = tempoMs;
            self.rondes = rondes;
            self.herstelMs = herstelMs;
            segmentStart = startMs;
        }

        function ademDuurMs() as Number {
            return ademhalingen * 2 * tempoMs;
        }

        // Werk de fase bij tot tijdstip nu. Grenzen liggen op vaste tijden vanaf het segment.
        function bijwerken(nu as Number) as Void {
            var doorgaan = true;
            while (doorgaan) {
                doorgaan = false;
                if (fase == FASE_ADEMEN && nu - segmentStart >= ademDuurMs()) {
                    segmentStart += ademDuurMs();
                    fase = FASE_INHOUDEN;
                } else if (fase == FASE_HERSTEL && nu - segmentStart >= herstelMs) {
                    segmentStart += herstelMs;
                    ronde += 1;
                    fase = (ronde >= rondes) ? FASE_KLAAR : FASE_ADEMEN;
                    doorgaan = true;
                }
            }
        }

        // Stop het inhouden op het tijdstip van de knop (eis 4). Geeft de inhoudtijd in ms.
        function stopInhouden(nu as Number) as Number {
            if (fase != FASE_INHOUDEN) {
                return -1;
            }
            var tijd = nu - segmentStart;
            inhoudtijden.add(tijd);
            segmentStart = nu;
            fase = FASE_HERSTEL;
            return tijd;
        }

        // Tijd in het huidige stuk.
        function verstreken(nu as Number) as Number {
            return nu - segmentStart;
        }

        // Tijdens ademen: welke ademhaling (1-gebaseerd).
        function ademhaling(nu as Number) as Number {
            return (nu - segmentStart) / (2 * tempoMs) + 1;
        }

        // Tijdens ademen: true bij in, false bij uit.
        function isIn(nu as Number) as Boolean {
            return (nu - segmentStart) % (2 * tempoMs) < tempoMs;
        }

        // Hoogte van het water, 0.0 leeg tot 1.0 vol.
        function water(nu as Number) as Float {
            if (fase == FASE_ADEMEN) {
                var p = (nu - segmentStart) % (2 * tempoMs);
                if (p < tempoMs) {
                    return zacht(p.toFloat() / tempoMs);
                }
                return 1.0 - zacht((p - tempoMs).toFloat() / tempoMs);
            }
            if (fase == FASE_INHOUDEN) {
                return 0.15;
            }
            if (fase == FASE_HERSTEL) {
                return 1.0;
            }
            return 0.5;
        }
    }

    // Rustig ademen: patroon in, vast, uit, vast (ms per fase; vast mag 0).
    class Rustig {
        var patroon as Array<Number>;
        var startMs as Number;

        function initialize(patroon as Array<Number>, startMs as Number) {
            self.patroon = patroon;
            self.startMs = startMs;
        }

        function cyclus() as Number {
            return patroon[0] + patroon[1] + patroon[2] + patroon[3];
        }

        // Index van de fase: 0 in, 1 vast (vol), 2 uit, 3 vast (leeg).
        function faseIndex(nu as Number) as Number {
            var c = cyclus();
            if (c <= 0) {
                return 0;
            }
            var p = (nu - startMs) % c;
            for (var i = 0; i < 4; i += 1) {
                if (p < patroon[i]) {
                    return i;
                }
                p -= patroon[i];
            }
            return 3;
        }

        // Begin van de huidige fase (ms), voor de grens-toets.
        function faseStart(nu as Number) as Number {
            var c = cyclus();
            var basis = nu - (nu - startMs) % c;
            var i = faseIndex(nu);
            for (var j = 0; j < i; j += 1) {
                basis += patroon[j];
            }
            return basis;
        }

        function water(nu as Number) as Float {
            var i = faseIndex(nu);
            var p = (nu - faseStart(nu)).toFloat();
            if (i == 0) {
                return zacht(p / patroon[0]);
            }
            if (i == 1) {
                return 1.0;
            }
            if (i == 2) {
                return 1.0 - zacht(p / patroon[2]);
            }
            return 0.0;
        }
    }

    // De vaste patronen (ontwerp): box 4-4-4-4, 4-7-8, rustig 5,5 in en 5,5 uit.
    function patronen() as Array<Array<Number> > {
        return [
            [4000, 4000, 4000, 4000],
            [4000, 7000, 8000, 0],
            [5500, 0, 5500, 0]
        ] as Array<Array<Number> >;
    }
}
