import Toybox.Lang;

// Alleen voor de plaatjesbouw op een proeftak (bericht hoofdchat 12 nov 14:00 NL: proefrondes korter). De workflow
// garmin-adem-iq.yml vult KEUZE met de scènenummers uit proef-scenes.txt; dan toont start n de scène KEUZE[n].
// Leeg (de gewone bouw, de bouwtak): de scènes op volgorde vanaf EbbBouw.EERSTE, zoals altijd.
(:plaatje) module EbbSceneKeuze {
    const KEUZE = [] as Array<Number>;

    function scene(n as Number) as Number {
        var aantal = KEUZE.size();
        if (aantal > 0) {
            return KEUZE[n % aantal];
        }
        return (n + EbbBouw.EERSTE) % EbbBouw.SCENES;
    }
}
