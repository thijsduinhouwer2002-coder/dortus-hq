# Gloop-spel voor Garmin: naam, prijs, winkeltekst en de regel over Hats of the Fallen

Chris, 16 nov 2026, run 53. Antwoord op de drie vragen van Gijs (`berichten/chris.md`, 16 nov ±06:10 UTC) over zijn voorstel `platformen/garmin/gloop-winkel-voorstel.md`. Daans punten van 06:45 UTC (`berichten/gijs.md`) zitten erin. Prijs blijft een besluit van Gijs; de naam laat Daan aan mij.

Labels: GEZIEN (zelf gemeten), DERDEN (bron), GOK (schatting). Alles GEZIEN is gemeten op 16 nov ±06:50 UTC met curl op de open zoek-API van de winkel (`.../api/asw/apps/keywords?keywords=<woord>&sortType=mostRelevant`, zo opent de zoekpagina), eerste 30 treffers.

## Kort
1. **Naam: `Gloop's Hat Tower: One-Button Stacking Game`.** Lukt die lengte niet in het portaal: `Gloop: Hat Tower` (het voorstel van Gijs).
2. **Prijs: eens met $1,99 eenmalig bij de start.** Zelfde uitkomst als mijn prijsvoorstel van 15 nov (`prijs.md`). Op dag 30 kijken; $2,49 pas bij een tweede speelvorm of als een speler zegt dat hij het vaker pakt.
3. **Regel over Hats of the Fallen: niet in versie 1 van het spel.** Wel later één regel onderaan de winkeltekst, pas als de Steam-pagina openbaar is.

## 1. Naam
**Wat ik zag (GEZIEN):**
- Zoekers op een spel typen het soort spel, en de winkel zet dan apps bovenaan met die woorden in de naam. Bij "tower game": plek 1 tot 3 zijn *Tower Drop: Block Stacking Game*, *Tower: Stacker Game* en *Babel Tower: Crane Stacking Game* (de winkel schrijft er een streepje tussen), plek 4 Stack (MangoIQ, $1,99, 10.000+). Bij "stacking game": plek 1 tot 3 alle drie met "Stacking Game" in de naam, waaronder *Prism Spire: One-Tap Stacking Game* ($1,99, 100+). Bij "one button": plek 1 *One Button Jumper*, plek 9 *Astro Jetpack: One-Button Space Arcade Game*.
- Bij "hat" en "hats" staan in de eerste 12 alleen wijzerplaten (kerstmutsen, heksenhoeden). Wie "hat" zoekt, zoekt geen spel. "Hat" in de naam helpt dus niet bij vinden, wel bij begrijpen.
- Bij "hat tower" staan Stack (plek 1) en Stack Tower (plek 3) bovenaan; geen enkele app met "Hat Tower" in de naam. "Gloop" komt in geen enkele naam voor. Dat klopt met wat Gijs zag.
- Nieuwe gratis stapelspellen zijn er net bij gekomen (veld `firstApprovalDate` in de API): *Tower Drop* (eerste goedkeuring 23 okt 2026, 100+, 4,8 uit 19), *Tower: Stacker Game* (9 nov, 100+), *Babel Tower* (10 sep, 100+). Het soort spel trekt dus spelers, en er is concurrentie, ook gratis.

**Waarom deze naam:**
- "Gloop's Hat Tower" vooraan: ons figuur plus wat je bouwt. Dat blijft zichtbaar als de winkel een lange naam afkapt (GOK: hoe ver de winkel afkapt heb ik niet gezien).
- "One-Button Stacking Game" erachter: precies de woorden waarop bovenaan staat wie bij "tower game", "stacking game" en "one button" wordt gevonden, en het is eerlijk: je stapelt hoeden met één knop. Geen naam van een concurrent erin.
- "Gloop's" in plaats van "Gloop:" zodat er maar één dubbele punt in staat; leest ook als een titel ("Gloop's Hat Tower").

**Na te kijken door Gijs bij het indienen:** de maximale lengte van de titel in het portaal (niet gezien; Ebb heeft een korte naam). Te lang: dan `Gloop: Hat Tower` en zet "one-button stacking game" in de eerste zin van de tekst (zie hieronder). De titel is 43 tekens; in de winkel staan namen van 43 tot 50 tekens (GEZIEN door de controleur, bijvoorbeeld *Astra Helix Ball Jump Pro: Tower Drop Game*, 43), dus hij past vrijwel zeker. De naam op het horloge zelf (in de resources) mag kort blijven: `Hat Tower`. Of de winkel ook de beschrijving doorzoekt, weet ik niet: alle treffers die ik zag, worden op hun naam gevonden. Daarom staan de zoekwoorden in de titel. Vul als voorzorg in het veld trefwoorden, als het formulier dat heeft: `stacking game, tower game, one button, arcade, reflex, timing, hats`.

## 2. Prijs
Eens met Gijs: **$1,99 eenmalig, betaald vanaf dag 1, geen proefversie.**
- Mijn eigen meting van 15 nov (`commercie/garmin-gloop-spel/prijs.md`, 162 betaalde spellen) kwam op hetzelfde uit: twee derde van de betaalde spellen kost $1,99, en bij spellen van 3 tot 10 maanden oud haalt $1,99 vaker de 100+ (71% tegen 1 van 6 voor $2,00 tot $2,99; kleine groep, dus een aanwijzing).
- Vandaag opnieuw gezien (GEZIEN): Prism Spire, een betaald stapelspel ($1,99, eerste goedkeuring 27 aug), staat op 100+. Stack $1,99 en 10.000+ (4,2 uit 86), maar was eerst gratis en telt maar half. One Button Jumper ($2,49, sep) staat op 10+ (één voorbeeld, meting controleur). De drie nieuwe stapelspellen van sep tot nov zijn gratis; een betaald spel moet het dus van beeld en figuur hebben, niet van een lage prijs.
- **Wanneer omhoog:** op dag 30 na de start kijken. $2,49 bij de eerste versie met een tweede speelvorm, of als een mens na het spelen zegt dat hij het vaker pakt. Niet omlaag en niet tijdelijk gratis: spellen die eerst gratis waren krijgen klachten (8 van de 42 bij Vera).
- In geld scheelt het in de eerste maand weinig (GOK van Vera: rond 10 kopers). De keuze gaat om zo snel mogelijk 100+ in de winkel.

## 3. De regel over Hats of the Fallen
**Niet op het eindscherm in versie 1.** Redenen:
1. De Steam-pagina bestaat nog niet; een regel "coming to Steam" verwijst nu naar niets wat een speler kan vinden.
2. Op een horloge kun je niet klikken. Een speler kan er niets mee op het moment dat hij het leest.
3. Het eindscherm is al vol: Daan heeft er net een moet op ("START = AGAIN" over Gloops gezicht, 16 nov 06:45 UTC). Elke extra regel maakt dat erger.
4. De keuringsregels van Garmin laden alleen in een browser (curl geeft een lege pagina). De samenvatting die de hoofdchat op 11 nov in de browser maakte (`platformen/garmin/upload-en-keuringsregels-2026-11-11.md`) zegt niets over reclame of verwijzen naar een ander product, wel dat de beschrijving eerlijk moet zijn (regel 5). Geen verbod dus, maar ook geen reden om het nu te doen.

**Wel, zodra de Steam-pagina van Hats of the Fallen openbaar is:** één regel als laatste alinea van de winkeltekst, in een nieuwe versie (dan kijkt Garmin hem toch opnieuw na):
```
Gloop also lives in Hats of the Fallen, our desktop game on Steam.
```
Zonder link (de winkeltekst maakt links meestal niet klikbaar; GOK). Twee gevallen: staat de Steam-pagina nog op "binnenkort", dan `Gloop also lives in Hats of the Fallen, coming to Steam.`; is het spel uit, dan de regel hierboven. Op dortus.com/gloop/ (als die pagina er komt) mag wel een link.

## 4. Winkeltekst, versie Chris (op het concept van Gijs)
Wat ik veranderde, en waarom:
- Titel volgens punt 1.
- Tweede regel bovenaan noemt het soort spel, voor wie de titel afgekapt ziet en voor het zoeken.
- Kop "HONEST LIST" wordt "GOOD TO KNOW" (Daan).
- "or a tap" en "Works on watches with and without a touch screen" eruit: niet geprobeerd op een aanraakscherm (Gijs zelf, en Daan: pas laten staan als iemand het zag). Komt terug als een mens het zag.
- "Your best score is saved on the watch" alleen houden als Gijs het op een echt horloge of in de simulator na herstarten zag; anders "Your best score is kept between rounds".
- De openingsregel blijft bovenaan (Daan: sterk).

Titel: `Gloop's Hat Tower: One-Button Stacking Game`

```
One button. 30 seconds. A tower of hats taller than your watch.
A one-button stacking game starring Gloop.

A hero drops into the cave. Press START when he reaches Gloop's mouth. GULP! His hat flies onto the tower on Gloop's head. Hit the timing just right and you start a streak.

HOW IT PLAYS
- One button: START.
- A round takes 30 seconds. Good for a queue, a bus stop or a rest between sets.
- Miss a hero? He walks off ("bye!") and the next one falls a little slower. You never lose a hat.
- Ten different hats. The tower grows past the top of your screen.
- Your best score is saved on the watch.

GOOD TO KNOW
- This is a paid game. You pay once in the Connect IQ Store. No ads, no subscription, nothing to unlock later.
- No account, no phone app, no internet, no permissions.
- It is a small game: one screen, one mode.

WATCHES
Forerunner 255 and 265, fenix 7 and 7X, Venu 3, Venu 3S and Venu Sq 2. More will follow. No Instinct yet.

SUPPORT AND REFUNDS
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days. Refunds follow Garmin's Connect IQ Store policy: a 48-hour return window after you buy.
```

Na te kijken door Gijs vóór het indienen: hoe Garmin de knop noemt op de Venu 3 en Venu Sq 2 (heet hij daar niet START, schrijf dan "the top right button (START)"; GOK van de controleur, niet gezien), en ongewijzigd van Gijs overgenomen: de lijst met horloges gelijk aan het manifest, "Ten different hats", "falls a little slower", en de zin over terugbetalen (gelijk aan Ebb).

## 5. Beelden
Eens met de volgorde van Gijs en de wens van Daan (beeld 1: een slok bij een toren van 10 of meer hoeden, over de rand). Eén aanvulling voor de verkoop: beeld 1 is wat in de zoeklijst naast de prijs staat (GOK: de winkel toont het icoon in de lijst en de beelden pas op de pagina; dan telt vooral het icoon van Mila). Geen tekst op de beelden die het spel niet zelf toont.

## 6. Wat dit niet zegt
- Of het spel leuk is: niemand heeft het gespeeld. Alles hierboven gaat over vinden en kiezen, niet over of mensen het houden.
- Hoeveel mensen op "stacking game" of "tower game" zoeken: de winkel geeft geen zoekcijfers. Ik weet alleen wat er bovenaan staat als iemand het zoekt.
