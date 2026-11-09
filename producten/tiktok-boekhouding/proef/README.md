# Proef in de Moneybird-sandbox

Jet, 9 nov 2026, na het bericht van Thijs (22:48 NL): de sandbox-administratie "Klopt test" (id 503358859490886985) staat, het token zit als secret `MONEYBIRD_SANDBOX_TOKEN` in dortus-hq.

**Wat het doet.** `sandbox.ts` loopt via de workflow `.github/workflows/tiktok-boekhouding-sandbox.yml` (handmatig of bij een wijziging aan het script op main) de open vragen af uit `ontwerp-moneybird.md` en `rgs-codes.md`, en gebruikt daarbij onze eigen code (`boekAfrekening`, `maakMemoriaal`, `grootboekrekeningen`, `btwTarieven`, `administraties`), zodat we meteen zien of die tegen het echte Moneybird klopt:
0. toegang (401 geeft de letterlijke fout en stopt), staat de administratie erin, komt het grote id als tekst of als getal, en `period_locked_until`;
1. memoriaal zonder btw aanmaken, terugzoeken op kenmerk (exact, deel van het kenmerk, kleine letters) en nog eens boeken zonder id (verwacht `ongewijzigd`);
2. vervangen met `_destroy` en regel-id's als tekst, van 3 naar 4 regels (verwacht `vervangen`, zelfde document-id, oude regels weg), daarna `ongewijzigd`;
3. een omzetregel met `tax_rate_id` (21%) en alle velden die Moneybird teruggeeft, plus of onze vergelijking daarna nog `ongewijzigd` zegt;
4. boeken op de datum van `period_locked_until` (ruwe POST, langs onze eigen controle heen) en het letterlijke antwoord. De API kan zelf geen periode afsluiten; is er geen afgesloten periode in de sandbox, dan staat er "niet te testen";
5. rekeningen aanmaken met een RGS-code: de tegenrekening BVorOvrOvk, een tweede met dezelfde code, een code buiten de Basis-set (BVorTusTovTvp), de terugval BVorTusTov, een soort die niet bij de code past, en dezelfde naam twee keer.

**Wat het bewust niet doet.** Geen andere administratie: staat id 503358859490886985 niet in de lijst, dan stopt het zonder iets te doen. Geen TikTok, geen opslag, geen product-laag. Het token komt nooit in de uitvoer (en wordt voor de zekerheid vervangen door `***`). Het draait niet bij elke wijziging aan het product, alleen bij een wijziging aan dit script of de workflow, of met de hand.

**Opruimen.** Alles wat de proef maakt heeft kenmerk `TikTokShop-99<run>...` of een naam met "Dortus proef", en wordt aan het eind verwijderd (eerst documenten, ook die we zonder id terugkregen via zoeken op kenmerk, dan rekeningen op id en op naam); een rekening zet Moneybird bij DELETE eerst op inactief, dus die is verwijderd of uitgezet. De uitslag laat per stuk de status zien.

**Cache.** Moneybird cachet GET-antwoorden en raadt af om met GET te controleren. Daarom logt de proef het antwoord van elke POST en PATCH zelf (dat is het bewijs), en bij elke GET `version` en `updated_at`.

**Af als.** De workflow draait met het secret, de unittests van de map zijn groen, en `uitslag.md` (samenvatting en artifact van de run) geeft op elke vraag een antwoord of zegt waarom niet. De uitkomsten gaan daarna als GEZIEN naar `ontwerp-moneybird.md` en `rgs-codes.md`, en de code wordt pas daarna aangepast (bijvoorbeeld btw aan), met eigen tests en controleur.
