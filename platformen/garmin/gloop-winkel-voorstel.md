# Gloop-spel voor Garmin: voorstel naam, prijs en winkeltekst (Gijs, run 108, 16 nov ±06:10 UTC)

**Dit is een voorstel, geen besluit.** Daan keurt de stijl en de beelden, Chris kijkt naar naam, prijs en tekst, Mila maakt icoon en winkelbeelden. Er wordt niets ingediend voordat een mens het spel gespeeld heeft en Daan `Akkoord: ja` gaf. Het spel is nog door niemand gespeeld.

## 1. Naam: voorstel "Gloop: Hat Tower"
- **Vrij in de winkel (GEZIEN, 16 nov 05:58 UTC, open zoek-API, eerste 30 treffers per woord):** bij "gloop" staat geen enkele app met Gloop in de naam (wel MooveLoop, Glow Loop en andere "loop"-namen). Bij "hat tower" en "gulp" ook geen app met die woorden in de naam. Niet gezien: treffers voorbij de eerste 30, en merkenregisters (niet nagezocht).
- **Waarom deze naam:** "Gloop" is ons eigen figuur en komt terug in Het Hol; "Hat Tower" zegt in twee woorden wat je doet en wat je krijgt. Het woord "tower" helpt bij zoeken: wie "hat tower" of "stack" zoekt krijgt nu bovenaan Stack van MangoIQ (10.000+) en Stack Tower (10+), dus daar zoeken spelers.
- Alternatieven: "Gloop" alleen (kort, maar zegt niets), "Hat Tower" alleen (zegt wat het is, maar bouwt ons figuur niet op), "Gulp!" (leuk, maar onvindbaar).

## 2. Prijs: voorstel $1,99 bij de start, later omhoog als er meer in zit
- **Bewijs dat zulke spellen gekocht worden (GEZIEN vandaag via de open API, veld `pricing`):** AstroBlast (VAW.BE) $1,99, 10.000+ downloads, 287 reviews, 4,4. Fruit Spider (ReedWorks) $1,99, 10.000+, 36 reviews, 3,5. Stack (MangoIQ) $1,99, 10.000+, 86 reviews, 4,2 (was volgens Vera eerst gratis, telt dus half). Uit het onderzoek van Vera (`platformen/verkenner/iets-erbij-2026-11.md`, GEZIEN door haar): 28 van de 42 betaalde spellen van 2026 kosten $1,99, de rest $2,25 tot $3,99; van de spellen die vanaf het begin betaald waren haalt 58 tot 61 procent de 100+.
- **Waarom nu niet hoger dan de mediaan van $2,25:** de opdracht zegt hoger prijzen als het product dat waard is. Op dit moment is het één scherm met één potje van 30 seconden, en niemand heeft het gespeeld. De drie sterkste betaalde spellen zitten alle drie op $1,99; het enige voorbeeld erboven met 10.000+ is Step Farmer ($2,49), en dat was eerst gratis. Er is dus geen bewijs dat een nieuw spel van een onbekende maker boven $1,99 verkoopt. GOK: het verschil tussen $1,99 en $2,49 is 25 procent per koper; als de hogere prijs meer dan één op de vijf kopers kost, verdienen we er minder aan.
- **Wat het zou veranderen:** zit er een tweede speelvorm in (bijvoorbeeld een eindeloze toren zonder klok), een Instinct-versie en een beste score per dag, of zegt een mens na het spelen dat hij het vaker pakt, dan stel ik $2,49 of $2,99 voor. De prijs kan na de start in het portaal omhoog; omlaag kan ook, maar een spel dat eerst goedkoper of gratis was krijgt klachten (8 van de 42 spellen bij Vera).
- **Verwachting eerste 30 dagen (GOK van Vera, ik neem hem over):** 0 tot 150 kopers, midden rond 10, dus rond $17. Het wordt drukker in de winkel (38 nieuwe betaalde spellen in oktober, 35 daarvan onder de 10 downloads). Dit spel is dus vooral goedkoop om te maken en een reclamebord voor Gloop; reken niet op geld in de eerste maand.

## 3. Winkeltekst, concept 1 (Engels, eerlijk, kort)

Titel: `Gloop: Hat Tower`

```
One button. 30 seconds. A tower of hats taller than your watch.

A hero drops into the cave. Press START when he reaches Gloop's mouth. GULP! His hat flies onto the tower on Gloop's head. Hit the timing just right and you start a streak.

HOW IT PLAYS
- One button (START) or a tap. Works on watches with and without a touch screen.
- A round takes 30 seconds. Good for a queue, a bus stop or a rest between sets.
- Miss a hero? He walks off ("bye!") and the next one falls a little slower. You never lose a hat.
- Ten different hats. The tower grows past the top of your screen.
- Your best score is saved on the watch.

HONEST LIST
- This is a paid game. You pay once in the Connect IQ Store. No ads, no subscription, nothing to unlock later.
- No account, no phone app, no internet, no permissions.
- It is a small game: one screen, one mode.

WATCHES
Forerunner 255 and 265, fenix 7 and 7X, Venu 3, Venu 3S and Venu Sq 2. More will follow. No Instinct yet.

SUPPORT AND REFUNDS
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days. Refunds follow Garmin's Connect IQ Store policy: a 48-hour return window after you buy.
```

Wat in deze tekst nog niet bewezen is en dus voor het indienen nagekeken moet worden: (1) "or a tap": de code luistert alleen naar de keuze-actie (`onSelect`, de START-knop); ik neem aan dat een tik op een aanraakscherm die actie ook geeft (GOK uit mijn kennis van de SDK, niet nagelezen en niet geprobeerd), dus eerst proberen in de simulator of op een horloge, anders deze zin weg; (2) "Your best score is saved": in de simulator gezien (de Venu Sq 2 toonde de score van het vorige horloge), niet op een echt horloge; (3) de lijst met horloges moet gelijk zijn aan het manifest op de dag van indienen; (4) de zin over terugbetalen is dezelfde als bij Ebb (`platformen/garmin/upload/ebb-en.md`). Regel 4d van Garmin (eerlijk over betalen) is gedekt met het blok HONEST LIST.

## 4. Winkelbeelden: alleen beelden die in het spel zitten
Voorstel volgorde (Mila maakt ze, uit de simulatorbeelden op tak `schermen`): (1) de slok met "GULP! x3" (het sterkste beeld bij de blinde kijkers van Mila); (2) de held valt met "!" en de open bek; (3) de hoge toren tot over de rand; (4) eindscherm "15 HATS / NEW BEST!"; (5) hetzelfde spel op een MIP-horloge (FR255), zodat een koper met een ouder horloge ziet wat hij krijgt. Geen beeld dat mooier is dan het spel zelf.

## 5. Horloges: wat nog ontbreekt
Spelers zitten volgens de reviewtelling van Vera vaak op goedkopere en oudere horloges: Venu Sq (zit erin), Forerunner 55 en 245, Instinct (zitten er niet in). De kit van Mila heeft nu zes maten (260 en 280 MIP, 320, 390, 416, 454). Voor de Forerunner 55 (208) en 245 (240) en voor de Instinct (zwart-wit) zijn eigen plaatjes nodig. Vraag aan Mila gesteld in `berichten/mila.md`. Tot die er zijn dien ik liever in met de zeven horloges die bekeken zijn dan met horloges die niemand zag.

## 6. Open vragen
- **Reclame voor Het Hol op het eindscherm** ("Gloop lives in Het Hol, coming to Steam", idee van Vera): pas als de Steam-pagina bestaat, anders verwijst het naar niets. Vraag aan Chris.
- **Eerst een mens laten spelen.** Staat op de lijst van Thijs als vrijblijvende vraag. Zonder dat is "leuk" een GOK.
- **Uitbetaling door Garmin** is voor ons nog niet bewezen: Ebb heeft 0 downloads (16 nov 05:56 UTC, GEZIEN).
