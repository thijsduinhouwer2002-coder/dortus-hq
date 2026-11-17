import Toybox.Lang;

// Slaapstand op schermen die kunnen inbranden: het beeld schuift elke minuut een stukje op.
module Slaap {
    // Verschuiving [dx, dy] in px voor teller n: een vierkantje van 2 px, (0,0) (2,0) (2,2) (0,2).
    // Twee stappen na elkaar liggen 2 px uit elkaar, twee stappen verder 3 px; nooit op dezelfde plek.
    function schuif(n as Number) as Array<Number> {
        if (n < 0) {
            n = -n;
        }
        var k = n % 4;
        return [(k == 1 || k == 2) ? 2 : 0, (k >= 2) ? 2 : 0] as Array<Number>;
    }
}
