import Toybox.Lang;

// Alleen voor de plaatjesbouw op een proeftak (bericht hoofdchat 12 nov 14:00 NL: proefrondes korter). De workflow
// garmin-adem-iq.yml vult KEUZE met de scènenummers uit proef-scenes.txt; dan toont start n de scène KEUZE[n].
// Leeg (de gewone bouw, de bouwtak): de scènes op volgorde vanaf EbbBouw.EERSTE, zoals altijd.
(:plaatje) module EbbSceneKeuze {
    const KEUZE = [] as Array<Number>;

    function scene(n as Number) as Number {
        var aantal = KEUZE.size();
        var k = (aantal > 0) ? KEUZE[n % aantal] : (n + EbbBouw.EERSTE) % EbbBouw.SCENES;
        // KIJKPROEF run 72 (terugdraaien voor de bouwtak): calm-45s (26), einde-6b (17), einde-weekdoel (29) en
        // calm-einde-krab (34) bij nacht, om Calm en het eindscherm op het thuiswater bij nacht te zien.
        if (k == 26 || k == 17 || k == 29 || k == 34) {
            EbbWereldSessie.proefNacht = 1;
            EbbThuis.proefNacht = 1;
        }
        return k;
    }
}
