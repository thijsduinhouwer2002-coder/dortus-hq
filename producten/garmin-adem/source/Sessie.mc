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

    // Signaal tijdens het inhouden tussen twee tikken (inhoudtijd vorig en nu, ms):
    // 2 bij het passeren van 3 minuten en daarna elke 30 s zolang je inhoudt (altijd, ook met "Buzz every 30 s" uit;
    // veiligheidskeuring blad v5.4), 1 bij elke 30 s daarvoor als elke30 aan staat, anders 0.
    function inhoudSignaal(vorigMs as Number, nuMs as Number, elke30 as Boolean) as Number {
        if (nuMs >= 180000 && (vorigMs < 180000 || nuMs / 30000 > vorigMs / 30000)) {
            return 2;
        }
        if (elke30 && nuMs >= 30000 && nuMs / 30000 > vorigMs / 30000) {
            return 1;
        }
        return 0;
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

        var pauzeVan as Number = -1;      // -1: niet gepauzeerd

        function gepauzeerd() as Boolean {
            return pauzeVan >= 0;
        }

        // Pauze zet de klok stil: bij doorgaan schuift het huidige stuk op met de pauzeduur.
        function pauzeer(nu as Number) as Void {
            if (pauzeVan < 0 && fase != FASE_KLAAR) {
                bijwerken(nu);
                pauzeVan = nu;
            }
        }

        function hervat(nu as Number) as Void {
            if (pauzeVan >= 0) {
                segmentStart += nu - pauzeVan;
                pauzeVan = -1;
            }
        }

        // Werk de fase bij tot tijdstip nu. Grenzen liggen op vaste tijden vanaf het segment.
        function bijwerken(nu as Number) as Void {
            if (pauzeVan >= 0) {
                return;
            }
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

        // Tijd in het huidige stuk (tijdens pauze stilgezet op het pauzemoment).
        function verstreken(nu as Number) as Number {
            return klok(nu) - segmentStart;
        }

        function klok(nu as Number) as Number {
            return (pauzeVan >= 0) ? pauzeVan : nu;
        }

        // Tijdens ademen: welke ademhaling (1-gebaseerd).
        function ademhaling(nu as Number) as Number {
            nu = klok(nu);
            return (nu - segmentStart) / (2 * tempoMs) + 1;
        }

        // Tijdens ademen: zit je in de laatste drie ademhalingen voor het inhouden?
        function laatsteDrie(nu as Number) as Boolean {
            return fase == FASE_ADEMEN && ademhaling(nu) > ademhalingen - 3;
        }

        // Tijdens ademen: true bij in, false bij uit.
        function isIn(nu as Number) as Boolean {
            nu = klok(nu);
            return (nu - segmentStart) % (2 * tempoMs) < tempoMs;
        }

        // Hoogte van het water, 0.0 leeg tot 1.0 vol.
        function water(nu as Number) as Float {
            nu = klok(nu);
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

        // Pauze: de klok staat stil; bij doorgaan schuift het begin op met de pauzeduur.
        var pauzeSinds as Number = -1;

        function pauzeer(nu as Number) as Void {
            if (pauzeSinds < 0) {
                pauzeSinds = nu;
            }
        }

        function hervat(nu as Number) as Void {
            if (pauzeSinds >= 0) {
                startMs += nu - pauzeSinds;
                pauzeSinds = -1;
            }
        }

        // De klok voor het scherm: tijdens pauze het moment van pauzeren.
        function klok(nu as Number) as Number {
            return pauzeSinds >= 0 ? pauzeSinds : nu;
        }

        // Hele seconden die nog over zijn in de huidige fase (afgerond naar boven), voor het grote getal.
        function overS(nu as Number) as Number {
            var i = faseIndex(nu);
            var rest = patroon[i] - (nu - faseStart(nu));
            return (rest + 999) / 1000;
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

    // Keuring bouw 3 punt 15: alleen Calm 4-7-8 staat in de app (Box en 5,5 zijn weg, besluit bouw 2); eigen patronen via My pattern.
    function calm() as Array<Number> {
        return [4000, 7000, 8000, 0] as Array<Number>;
    }
}
