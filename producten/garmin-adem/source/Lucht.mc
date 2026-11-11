import Toybox.Lang;

// Besluit hoofdchat 12 nov 00:25 punt 2: de lucht volgt het uur en de maan staat in de fase van die dag.
// Alleen rekenen uit de klok en de datum, geen netwerk. Het tekenen komt bij de ademschermen (nog niet gebouwd).
module EbbLucht {
    // Maanfase in achtsten: 0 nieuw, 1 wassende sikkel, 2 eerste kwartier, 3 wassend, 4 vol, 5 afnemend,
    // 6 laatste kwartier, 7 afnemende sikkel. Gemiddelde maanmaand van 29,530588 dagen vanaf de nieuwe maan van
    // 6 jan 2000 18:14 UTC; de echte maan wijkt hoogstens ruim een halve dag af, voor acht standen is dat genoeg.
    function maanfase(unix as Number) as Number {
        var maand = 2551443;
        var r = (unix - 947182440) % maand;
        if (r < 0) {
            r += maand;
        }
        return ((r * 8 + maand / 2) / maand) % 8;
    }

    // Dagdeel uit het uur van de klok: 0 ochtend (5 tot 9), 1 dag (9 tot 18), 2 avond (18 tot 21), 3 nacht.
    function dagdeel(uur as Number) as Number {
        if (uur >= 5 && uur < 9) {
            return 0;
        }
        if (uur >= 9 && uur < 18) {
            return 1;
        }
        if (uur >= 18 && uur < 21) {
            return 2;
        }
        return 3;
    }
}
